from abc import ABC, abstractmethod

BASE = 'https://api.zyjj.cc/api/v1/'

class BaseClient(ABC):
    version = "0.1.0"

    @abstractmethod
    def __init__(self, sk: str):
        pass

    @abstractmethod
    def get_point(self) -> int:
        """
        获取当前账户剩余积分
        :return:
        """
        pass

    @abstractmethod
    def execute(self, task_type: int, _input: dict) -> dict:
        """
        同步执行执行任务
        :param task_type: 任务类型
        :param _input: 任务输入
        :return: 任务执行结果
        """
        pass

    @abstractmethod
    def execute_async(self, task_type: int, _input: dict) -> str:
        """
        异步执行任务
        :param task_type: 任务类型
        :param _input: 任务输入
        :return 任务id
        """
        pass

    @abstractmethod
    def get_task_status(self, task_id: str) -> dict:
        """
        获取任务状态
        :param task_id: 任务id
        :return: 任务状态
        """

    @abstractmethod
    def get_file_token(self, file_name: str, file_size: int, source: int = 1) -> dict:
        """
        获取文件上传token
        :param file_name: 文件名称
        :param file_size: 文件大小
        :param source: 文件来源
        :return:
        """

    @abstractmethod
    def file_multipart_init(self, file_name: str, file_size: int, source: int = 1) -> dict:
        """
        初始化分片上传
        :param file_name: 文件名称
        :param file_size: 文件大小
        :param source: 文件来源
        :return:
        """

    @abstractmethod
    def file_multipart_part(self, upload_id: str, part_num: int) -> dict:
        """
        开始分片上传
        :param upload_id: 上传id
        :param part_num: 第几个分片
        :return:
        """

    @abstractmethod
    def file_multipart_complete(self, upload_id: str, part_list: list) -> dict:
        """
        完成分片上传
        :param upload_id: 上传id
        :param part_list: 分片列表
        :return:
        """

    @abstractmethod
    def get_mqtt_task(self) -> dict:
        """
        获取mqtt task客户端链接
        :return:
        """