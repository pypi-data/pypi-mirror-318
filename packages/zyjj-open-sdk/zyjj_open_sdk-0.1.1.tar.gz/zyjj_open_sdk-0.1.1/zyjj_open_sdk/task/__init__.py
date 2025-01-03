from zyjj_open_sdk.core import OpenClient, MqttClient
from zyjj_open_sdk.task.text import Text
from zyjj_open_sdk.task.image import Image
from zyjj_open_sdk.task.audio import Audio
from zyjj_open_sdk.task.subtitle import Subtitle
from zyjj_open_sdk.task.tool import Tool

class Client:
    def __init__(self, sk: str):
        self.__client = OpenClient(sk)
        self.__mqtt = MqttClient(self.__client)
        self.text = Text(self.__client, self.__mqtt)
        self.image = Image(self.__client, self.__mqtt)
        self.audio = Audio(self.__client, self.__mqtt)
        self.subtitle = Subtitle(self.__client, self.__mqtt)
        self.tool = Tool(self.__client, self.__mqtt)

    def close(self):
        """关闭客户端，必须显式调用"""
        self.__mqtt.close()
