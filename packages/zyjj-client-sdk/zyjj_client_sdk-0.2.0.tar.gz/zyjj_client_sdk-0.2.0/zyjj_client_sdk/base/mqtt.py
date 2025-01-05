import asyncio
import json
import logging
from enum import Enum

import httpx

from zyjj_client_sdk.base.base import Base
from zyjj_client_sdk.base.api import ApiService
from aiomqtt import Client, MqttError, ProtocolVersion


class MqttEventType(Enum):
    Start = 1  # 开始任务
    Progress = 2  # 进度事件
    Success = 3  # 成功
    Fail = 4  # 失败
    DetailAppend = 5  # 详情追加
    DetailSet = 6  # 详情覆盖


class MqttServer:
    def __init__(self, base: Base, api: ApiService):
        self.__running = False
        self.__subscribe = {}
        self.__proxy = None
        self.__base = base
        self.__api = api
        # 客户端信息
        self.__client_id = ''
        self.__username = ''
        self.__password = ''
        # 消息队列
        self.__queue = asyncio.Queue()

    async def start(self):
        """启动mqtt服务"""
        if self.__running:
            return
        self.__running = True
        # 获取客户端信息
        info = await self.__api.cloud_get_mqtt()
        host, self.__client_id, self.__username, self.__password = (info['host'], info['client_id'], info['username'], info['password'])
        logging.info(
            f"[mqtt] info host {host} client_id {self.__client_id} "
            f"username {self.__username} password {self.__password}"
        )
        # 如果不是代理我们才建立mqtt连接
        logging.info(f"[mqtt] mqtt proxy is {self.__base.mqtt_proxy}")
        if bool(self.__base.mqtt_proxy):
            self.__proxy = httpx.AsyncClient(base_url=self.__base.mqtt_proxy)
            return
        client = Client(
            hostname=host,
            port=1883,
            keepalive=30,
            protocol=ProtocolVersion.V311,
            username=self.__username,
            password=self.__password,
            identifier=self.__client_id,
        )
        interval = 5  # 重连间隔
        while True:
            try:
                async with client:
                    logging.info(f'[mqtt] connect success')
                    while self.__running:
                        try:
                            topic, data = await asyncio.wait_for(self.__queue.get(), timeout=1.0)
                            logging.info(f"[mqtt] topic {topic} data {data}")
                            await client.publish(topic, payload=data)
                        except asyncio.TimeoutError:
                            continue
                    if not self.__running:
                        return
            except Exception as e:
                print(f"[mqtt] connection lost err {e}; reconnecting in {interval} seconds ...")
                await asyncio.sleep(interval)

    def close(self):
        self.__running = False

    # 发送event事件
    async def send_task_event(self, uid: str, task_id: str, event_type: MqttEventType, data=None, code=-1):
        topic = f"task_event/{uid}"
        data = json.dumps({
            'task_id': task_id,
            'event_type': event_type.value,
            'code': code,
            'data': data
        }, ensure_ascii=False).encode()
        if bool(self.__proxy):
            logging.info(f"[mqtt] proxy {topic} send message {event_type} data {data}")
            res = await self.__proxy.post(
                topic,
                content=data,
                headers={
                    "x-cid": self.__client_id,
                    "x-username": self.__username,
                    "x-password": self.__password
                }
            )
            res.raise_for_status()
        else:
            await self.__queue.put((topic, data))
