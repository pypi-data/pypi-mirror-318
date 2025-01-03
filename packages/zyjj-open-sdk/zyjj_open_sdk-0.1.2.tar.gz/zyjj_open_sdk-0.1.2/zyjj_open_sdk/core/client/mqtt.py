import json
import logging
import threading
from dataclasses import dataclass
from typing import Callable, Type, Any
from zyjj_open_sdk.core.client.base import BaseClient
from zyjj_open_sdk.core.entity.type import data_class_init
import paho.mqtt.client as mqtt


@dataclass
class MqttResponse:
    task_id: str
    event_type: int  # 1 开始 2 执行中 3 成功 4 失败 5 详情追加 6 详情设置
    data: Any
    code: int


Callback = Callable[[Type[MqttResponse]], None]


class MqttClient:
    def __init__(self, client: BaseClient):
        # 初始化mqtt信息
        self.__mqtt_data = client.get_mqtt_task()
        logging.info(f"client info {self.__mqtt_data}")
        self.__client = mqtt.Client(client_id=self.__mqtt_data["client_id"], protocol=mqtt.MQTTv311)
        self.__client.connect(self.__mqtt_data["host"], 1883, 30)
        self.__client.username_pw_set(self.__mqtt_data["username"], self.__mqtt_data["password"])
        self.__client.on_connect = lambda client, userdata, flags, rc: self.__on_connect(rc)
        self.__client.on_message = lambda client, userdata, msg: self.__on_message(msg)
        # 监听列表
        self.__listen_map: dict[str, Callback] = {}
        logging.info(f'[mqtt] connect start')
        # 后台运行
        threading.Thread(target=self.__run).start()

    def __on_connect(self, code: int):
        if code != 0:
            logging.info(f'[mqtt] connect error {code}')
            return
        logging.info(f'[mqtt] connect success')
        # 启动后自动订阅topic
        self.__client.subscribe(self.__mqtt_data["topic"], qos=2)

    def __run(self):
        self.__client.loop_forever()

    def __on_message(self, msg: mqtt.MQTTMessage):
        logging.info(f'[mqtt] from {msg.topic} get message {msg.payload}')
        event = data_class_init(json.loads(msg.payload), MqttResponse)
        if event.task_id in self.__listen_map:
            logging.info(f"[mqtt] task id {event.task_id} in listen map")
            self.__listen_map[event.task_id](event)
        # 任务完成状态把监听器移除
        if event.event_type in [3, 4]:
            self.__listen_map.pop(event.task_id, None)

    def add_listener(self, task_id: str, callback: Callback):
        """
        添加一个监听器
        :param task_id: 任务id
        :param callback: 任务回调
        :return:
        """
        self.__listen_map[task_id] = callback

    def close(self):
        """
        关闭mqtt连接
        :return:
        """
        self.__client.disconnect()
