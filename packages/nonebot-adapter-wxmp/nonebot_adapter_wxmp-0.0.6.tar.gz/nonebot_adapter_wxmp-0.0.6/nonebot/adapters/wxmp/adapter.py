from typing import Any, Union, Callable, Optional, cast, Type
from typing_extensions import override
from pydantic import BaseModel, Field
from yarl import URL
import xmltodict
import asyncio
import hashlib
import secrets
import json
import sys
import re

from nonebot import get_plugin_config
from nonebot.utils import logger_wrapper
from nonebot.exception import WebSocketClosed
from nonebot.utils import DataclassEncoder, escape_tag
from nonebot.drivers import (
    URL,
    Driver,
    Request,
    Response,
    WebSocket,
    ForwardDriver,
    ReverseDriver,
    HTTPServerSetup,
    WebSocketServerSetup,
)

from nonebot.adapters import Adapter as BaseAdapter

from .bot import Bot
from .event import *
from .utils import log
from .config import Config, BotInfo
from .message import Message, MessageSegment
from .exception import (
    ActionFailed,
    NetworkError,
    ApiNotAvailable,
)

from nonebot import get_plugin_config
from nonebot.drivers import (
    Request,
    Response,
    ASGIMixin,
    WebSocket,
    HTTPServerSetup,
    HTTPClientMixin,
    WebSocketServerSetup
)


class Adapter(BaseAdapter):
    @override
    def __init__(self, driver: Driver, **kwargs: Any):
        super().__init__(driver, **kwargs)
        self.wxmp_config: Config = get_plugin_config(Config)
        self.tasks: set["asyncio.Task"] = set()
        self.setup()

    @classmethod
    @override
    def get_name(cls) -> str:
        """ 适配器名称: `WXMP` """
        return "WXMP"

    def setup(self) -> None:
        if not isinstance(self.driver, ASGIMixin):
            raise RuntimeError(
                f"Current driver {self.config.driver} doesn't support asgi server!"
                f"{self.get_name()} Adapter need a asgi server driver to work."
            )

        if not isinstance(self.driver, HTTPClientMixin):
            raise RuntimeError(
                f"Current driver {self.config.driver} "
                "doesn't support http client requests!"
                f"{self.get_name()} Adapter needs a HTTPClient Driver to work."
            )

        for bot_info in self.wxmp_config.wxmp_bots:
            http_setup = HTTPServerSetup(
                URL(f"/wxmp/revice/{bot_info.appid}"),
                "POST",
                f"{self.get_name()} {bot_info.appid} Event",
                self._handle_event,
            )
            self.setup_http_server(http_setup)
            if not (bot := self.bots.get(bot_info.appid, None)):
                bot = Bot(self, bot_info.appid, bot_info)
                self.bot_connect(bot)
                log("INFO", f"<y>Bot {escape_tag(bot_info.appid)}</y> connected")

            if bot_info.enable_verify:
                http_setup = HTTPServerSetup(
                    URL(f"/wxmp/revice/{bot_info.appid}"),
                    "GET",
                    f"{self.get_name()} {bot_info.appid} Verify",
                    self._handle_verify,
                )
                self.setup_http_server(http_setup)

        self.driver.on_shutdown(self.shutdown)

    async def shutdown(self) -> None:
        """ 关闭 Adapter """
        for task in self.tasks:
            if not task.done():
                task.cancel()

        await asyncio.gather(
            *(asyncio.wait_for(task, timeout=10) for task in self.tasks),
            return_exceptions=True,
        )
        self.tasks.clear()

    @classmethod
    def parse_body(cls, data: str) -> dict:
        """ 解析微信公众平台的事件数据 """
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            res: dict = xmltodict.parse(data)
            if _res := res.get("xml", None):
                return _res
            else:
                return res

    async def _handle_event(self, request: Request) -> Response:
        """ 处理微信公众平台的事件推送 """
        url = URL(request.url)
        timestamp = url.query.get("timestamp", "")
        nonce = url.query.get("nonce", "")
        signature = url.query.get("signature", "")

        bot: Bot = self.bots.get(self._get_appid(url.path), None)

        if not bot:
            return Response(404, content="Bot not found")

        if request.content:
            concat_string: str = ''.join(sorted([bot.bot_info.token, timestamp, nonce]))
            sha1_signature = hashlib.sha1(concat_string.encode('utf-8')).hexdigest()
            if not secrets.compare_digest(sha1_signature, signature):
                return Response(403, content="Invalid signature")
            else:
                payload: dict = self.parse_body(request.content)

                if bot.bot_info.type == "miniprogram":  # 小程序
                    event = MiniprogramEvent.payload_to_event(payload)
                elif bot.bot_info.type == "official":  # 公众号
                    event = OfficalAccountEvent.payload_to_event(payload)
                else:
                    raise ValueError(f"Invalid bot type: {bot.bot_info.type}")

                bot = self.bots.get(bot.bot_info.appid)
                task = asyncio.create_task(bot.handle_event(event))
                task.add_done_callback(self.tasks.discard)
                self.tasks.add(task)

                return Response(200, content="success")
        else:
            return Response(400, content="Invalid request body")

    async def _handle_verify(self, request: Request) -> Any:
        """ 响应微信公众平台的签名验证 """
        url = URL(request.url)
        signature = url.query.get("signature", "")
        echostr = url.query.get("echostr", "")
        timestamp = url.query.get("timestamp", "")
        nonce = url.query.get("nonce", "")

        bot: Bot = self.bots.get(self._get_appid(url.path), None)

        if not bot:
            return Response(404, content="Bot not found")

        concat_string: str = ''.join(sorted([timestamp, nonce, bot.bot_info.token]))
        sha1_signature = hashlib.sha1(concat_string.encode('utf-8')).hexdigest()

        if secrets.compare_digest(sha1_signature, signature):
            return Response(200, content=echostr)
        else:
            return Response(403, content="Invalid signature")

    def _get_appid(self, path: str) -> str:
        """ 从链接中获取 Bot 的 AppID """
        return path.split('/')[-1]

    async def _call_api(self, bot: Bot, api: str, **data: Any) -> Response:
        """ 调用微信公众平台 API """
        access_token = await bot._get_access_token()
        body: Any | None = data.get("json", data.get("data", data.get("body", None)))

        request = Request(
            method=data.get("method", "POST"),
            url=f"https://api.weixin.qq.com/cgi-bin{api}",
            params={
                "access_token": access_token,
            } | data.get("params", {}),
            headers=data.get("headers", {}),
            content=json.dumps(body, ensure_ascii=False).encode("utf-8") if body else None,
            files=data.get("files", None),
        )
        resp = await self.request(request)

        if resp.status_code != 200 or not resp.content:
            raise ActionFailed(retcode=resp.status_code, api=api, info=str(resp.content))

        return resp
