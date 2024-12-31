import asyncio
import weakref
import importlib
from typing import Any, Union, Literal, Optional

from nonebot.typing import T_State
from tarina import lang, init_spec
from nonebot.matcher import Matcher
from nonebot.utils import escape_tag
from pydantic import ValidationError
from nonebot.adapters import Bot, Event
from nonebot.plugin.on import on_message
from nonebot.internal.rule import Rule as Rule
from nonebot import get_driver, get_plugin_config
from arclet.alconna.exceptions import SpecialOptionTriggered
from arclet.alconna import Alconna, Arparma, CompSession, output_manager, command_manager

from .i18n import Lang
from .config import Config
from .adapters import MAPPING
from .uniseg import UniMsg, UniMessage
from .model import CompConfig, CommandResult
from .uniseg.constraint import UNISEG_MESSAGE
from .extension import Extension, ExtensionExecutor
from .consts import ALCONNA_RESULT, ALCONNA_EXTENSION, ALCONNA_EXEC_RESULT, log

_modules = set()


def check_self_send(bot: Bot, event: Event) -> bool:
    try:
        user_id = event.get_user_id()
    except ValueError:
        return False
    if bot.adapter.get_name() == "Satori":
        return user_id == bot.get_self_id()
    return user_id == bot.self_id


class AlconnaRule:
    """检查消息字符串是否能够通过此 Alconna 命令。

    参数:
        command: Alconna 命令
        skip_for_unmatch: 是否在命令不匹配时跳过该响应
        auto_send_output: 是否自动发送输出信息并跳过响应
        comp_config: 自动补全配置
        extensions: 需要加载的匹配扩展
        exclude_ext: 需要排除的匹配扩展
        use_origin: 是否使用未经 to_me 等处理过的消息
        use_cmd_start: 是否使用 nb 全局配置里的命令前缀
    """

    __slots__ = (
        "command",
        "skip",
        "auto_send",
        "response_self",
        "comp_config",
        "use_origin",
        "executor",
        "_path",
        "_namespace",
        "_waiter",
        "_matchers",
        "_futures",
        "_interfaces",
        "_comp_help",
    )

    def __init__(
        self,
        command: Alconna,
        skip_for_unmatch: bool = True,
        auto_send_output: Optional[bool] = None,
        comp_config: Optional[Union[CompConfig, bool]] = None,
        extensions: Optional[list[Union[type[Extension], Extension]]] = None,
        exclude_ext: Optional[list[Union[type[Extension], str]]] = None,
        use_origin: Optional[bool] = None,
        use_cmd_start: Optional[bool] = None,
        use_cmd_sep: Optional[bool] = None,
        response_self: Optional[bool] = None,
        _aliases: Optional[Union[set[str], tuple[str, ...]]] = None,
    ):
        if isinstance(comp_config, bool):
            self.comp_config = {} if comp_config else None
        else:
            self.comp_config = comp_config
        self.use_origin = use_origin or False
        try:
            global_config = get_driver().config
            config = get_plugin_config(Config)
            if config.alconna_global_completion is not None and self.comp_config == {}:
                self.comp_config = config.alconna_global_completion
            if auto_send_output is None:
                self.auto_send = True if config.alconna_auto_send_output is None else config.alconna_auto_send_output
            else:
                self.auto_send = auto_send_output
            if response_self is None:
                self.response_self = False if config.alconna_response_self is None else config.alconna_response_self
            else:
                self.response_self = response_self
            if use_cmd_start is None:
                _use_cmd_start = False if config.alconna_use_command_start is None else config.alconna_use_command_start
            else:
                _use_cmd_start = use_cmd_start
            if _use_cmd_start and global_config.command_start:
                with command_manager.update(command):
                    if command.prefixes:
                        if command.command:
                            command.prefixes = list(command.prefixes) + list(global_config.command_start)
                        else:
                            prefixes = list(command.prefixes)
                            command.command = prefixes[0]
                            command.prefixes = list(global_config.command_start)
                            for prefix in prefixes[1:]:
                                command.shortcut(prefix, prefix=True)  # type: ignore
                    else:
                        command.prefixes = list(global_config.command_start)
            if (config.alconna_use_command_sep if use_cmd_sep is None else use_cmd_sep) and global_config.command_sep:
                with command_manager.update(command):
                    command.separators = "".join(global_config.command_sep)
            if config.alconna_context_style:
                with command_manager.update(command):
                    command.meta.context_style = config.alconna_context_style
            self.use_origin = config.alconna_use_origin if use_origin is None else use_origin
        except ValidationError:
            raise
        except ValueError:
            self.auto_send = True if auto_send_output is None else auto_send_output
            self.response_self = False if response_self is None else response_self
            self.use_origin = False if use_origin is None else use_origin

        def _update(cmd_id: int):
            try:
                self.command = weakref.ref(command_manager._resolve(cmd_id))
            except (KeyError, AttributeError):
                pass

        self.command = weakref.ref(command, lambda _: _update(_.__hash__()))
        if _aliases:
            for alias in _aliases:
                command.shortcut(alias, prefix=True)
        self.skip = skip_for_unmatch
        self.executor = ExtensionExecutor(self, extensions, exclude_ext)
        self.executor.post_init(command)
        self._path = command.path
        self._namespace = command.namespace
        self._futures: dict[str, dict[str, asyncio.Future]] = {}
        self._matchers: dict[str, type[Matcher]] = {}
        self._interfaces: dict[str, CompSession] = {}

        self._comp_help = ""
        if self.comp_config is not None:
            _tab = self.comp_config.get("tab") or ".tab"
            _enter = self.comp_config.get("enter") or ".enter"
            _exit = self.comp_config.get("exit") or ".exit"
            disables = self.comp_config.get("disables", set())
            hides = self.comp_config.get("hides", set())
            hide_tabs = self.comp_config.get("hide_tabs", False)
            if self.comp_config.get("lite", False):
                hide_tabs = True
                hides = {"tab", "enter", "exit"}
            hides |= disables
            if len(hides) < 3:
                template = f"\n\n{{}}{{}}{{}}{Lang.nbp_alc.completion.other()}\n"
                self._comp_help = template.format(
                    (f"{Lang.nbp_alc.completion.tab(cmd=_tab)}\n" if "tab" not in hides else ""),
                    (f"{Lang.nbp_alc.completion.enter(cmd=_enter)}\n" if "enter" not in hides else ""),
                    (f"{Lang.nbp_alc.completion.exit(cmd=_exit)}\n" if "exit" not in hides else ""),
                )

            async def _waiter_handle(_bot: Bot, _event: Event, _matcher: Matcher, content: UniMsg):
                msg = str(content).lstrip()
                _future = self._futures[_bot.self_id][_event.get_session_id()]
                _interface = self._interfaces[_event.get_session_id()]
                if msg.startswith(_exit) and "exit" not in disables:
                    if msg == _exit:
                        _future.set_result(False)
                        await _matcher.finish()
                    else:
                        _future.set_result(None)
                        await _matcher.pause(
                            lang.require("analyser", "param_unmatched").format(target=msg.replace(_exit, "", 1))
                        )
                elif msg.startswith(_enter) and "enter" not in disables:
                    if msg == _enter:
                        _future.set_result(True)
                        await _matcher.finish()
                    else:
                        _future.set_result(None)
                        await _matcher.pause(
                            lang.require("analyser", "param_unmatched").format(target=msg.replace(_enter, "", 1))
                        )
                elif msg.startswith(_tab) and "tab" not in disables:
                    offset = msg.replace(_tab, "", 1).lstrip() or 1
                    try:
                        offset = int(offset)
                    except ValueError:
                        _future.set_result(None)
                        await _matcher.pause(lang.require("analyser", "param_unmatched").format(target=offset))
                    else:
                        _interface.tab(offset)
                        await _matcher.pause(
                            f"* {_interface.current()}" if hide_tabs else "\n".join(_interface.lines())
                        )
                else:
                    _future.set_result(content)
                    await _matcher.finish()

            self._waiter = _waiter_handle

    def __repr__(self) -> str:
        return f"Alconna(command={self.command()!r})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AlconnaRule) and self._path == other._path

    def __hash__(self) -> int:
        return hash(self.command.__hash__())

    async def handle(
        self, cmd: Alconna, bot: Bot, event: Event, state: T_State, msg: UniMessage
    ) -> Union[Arparma, Literal[False]]:
        ctx = await self.executor.context_provider(event, bot, state)
        if self.comp_config is None:
            return cmd.parse(msg, ctx)
        res = None
        session_id = event.get_session_id()
        if session_id not in self._interfaces:
            self._interfaces[session_id] = CompSession(cmd)
        with self._interfaces[session_id]:
            res = cmd.parse(msg, ctx)
        if res:
            self._interfaces[session_id].exit()
            del self._interfaces[session_id]
            return res
        if not await self.executor.permission_check(bot, event, cmd):
            return False

        def _checker(_event: Event):
            return session_id == _event.get_session_id()

        self._matchers[session_id] = on_message(priority=0, block=True, rule=Rule(_checker), handlers=[self._waiter])
        res = Arparma(
            cmd._hash,
            msg,
            False,
            error_info=SpecialOptionTriggered("completion"),
        )
        _futures = self._futures.setdefault(bot.self_id, {})
        _futures[session_id] = asyncio.get_running_loop().create_future()

        def _clear():
            self._interfaces[session_id].exit()
            self._matchers[session_id].destroy()
            del _futures[session_id]
            del self._matchers[session_id]
            del self._interfaces[session_id]

        while self._interfaces[session_id].available:
            await self.send(f"{str(self._interfaces[session_id])}{self._comp_help}", bot, event, res)
            while True:
                try:
                    await asyncio.wait_for(_futures[session_id], timeout=self.comp_config.get("timeout", 60))
                except asyncio.TimeoutError:
                    await self.send(Lang.nbp_alc.completion.timeout(), bot, event, res)
                    _clear()
                    return res
                finally:
                    if not _futures[session_id].done():
                        _futures[session_id].cancel()
                ans: Union[UniMessage, bool, None] = _futures[session_id].result()
                _futures[session_id] = asyncio.get_running_loop().create_future()
                if ans is False:
                    await self.send(Lang.nbp_alc.completion.exited(), bot, event, res)
                    _clear()
                    return res
                elif ans is None:
                    continue
                _res = self._interfaces[session_id].enter(None if ans is True else ans)
                if _res.result:
                    res = _res.result
                elif _res.exception and not isinstance(_res.exception, SpecialOptionTriggered):
                    await self.send(str(_res.exception), bot, event, res)
                break
        _clear()
        return res

    async def __call__(self, event: Event, state: T_State, bot: Bot) -> bool:
        self.executor.select(bot, event)
        if not (msg := await self.executor.message_provider(event, state, bot, self.use_origin)):
            self.executor.clear()
            return False
        if not self.response_self and check_self_send(bot, event):
            self.executor.clear()
            return False
        cmd = self.command()
        if not cmd:
            self.executor.clear()
            return False
        if command_manager.is_disable(cmd):
            self.executor.clear()
            return False
        msg = await self.executor.receive_wrapper(bot, event, cmd, msg)
        Arparma._additional.update(bot=lambda: bot, event=lambda: event, state=lambda: state)
        adapter_name = bot.adapter.get_name()
        if adapter_name in MAPPING and MAPPING[adapter_name] not in _modules:
            importlib.import_module(f"nonebot_plugin_alconna.adapters.{MAPPING[adapter_name]}")
        if isinstance(msg, UniMessage):
            _msg = msg
        else:
            _msg = await UniMessage.generate(message=msg, adapter=adapter_name)
        state[UNISEG_MESSAGE] = _msg

        with output_manager.capture(cmd.name) as cap:
            output_manager.set_action(lambda x: x, cmd.name)
            try:
                arp = await self.handle(cmd, bot, event, state, _msg)
                if arp is False:
                    self.executor.clear()
                    return False
            except Exception as e:
                arp = Arparma(cmd._hash, msg, False, error_info=e)
            may_help_text: Optional[str] = cap.get("output", None)
        if not arp.head_matched:
            self.executor.clear()
            return False
        if not arp.matched and not may_help_text and self.skip:
            log(
                "TRACE",
                escape_tag(Lang.nbp_alc.log.parse(msg=msg, cmd=self._path, arp=arp)),
            )
            self.executor.clear()
            return False
        if arp.head_matched:
            log(
                "DEBUG",
                escape_tag(Lang.nbp_alc.log.parse(msg=msg, cmd=self._path, arp=arp)),
            )
        if not may_help_text and arp.error_info:
            may_help_text = str(arp.error_info)
        if self.auto_send and may_help_text:
            await self.send(may_help_text, bot, event, arp)
            self.executor.clear()
            return False
        if self.skip and may_help_text:
            self.executor.clear()
            return False
        if not await self.executor.permission_check(bot, event, cmd):
            self.executor.clear()
            return False
        await self.executor.parse_wrapper(bot, state, event, arp)
        state[ALCONNA_RESULT] = CommandResult(result=arp, output=may_help_text)
        state[ALCONNA_EXEC_RESULT] = cmd.exec_result
        state[ALCONNA_EXTENSION] = self.executor.context
        return True

    async def send(self, text: str, bot: Bot, event: Event, arp: Arparma) -> Any:
        _t = str(arp.error_info) if isinstance(arp.error_info, SpecialOptionTriggered) else "error"
        try:
            msg = await self.executor.output_converter(_t, text)  # type: ignore
            if not msg:
                return await bot.send(event, text)
            msg = await self.executor.send_wrapper(bot, event, msg)
            return await bot.send(event, await msg.export(bot, fallback=True))  # type: ignore
        except NotImplementedError:
            return await bot.send(event, event.get_message().__class__(text))


@init_spec(AlconnaRule)
def alconna(rule: AlconnaRule) -> Rule:
    return Rule(rule)
