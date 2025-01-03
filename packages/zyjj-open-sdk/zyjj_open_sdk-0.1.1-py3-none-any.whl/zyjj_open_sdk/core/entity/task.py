import logging
import time
from zyjj_open_sdk.core.client import OpenClient, MqttClient, MqttResponse
from zyjj_open_sdk.core.exception import ServerError
from zyjj_open_sdk.core.entity.type import T, data_class_init
from dataclasses import dataclass
from typing import Generic, Callable, Type, Optional

# 各种回调
ProgressCallback = Callable[[float], None]
SuccessCallback = Callable[[T], None]
ErrorCallback = Callable[[ServerError], None]


# 任务异步执行结果
class TaskAsyncExecuteResult(Generic[T]):
    def __init__(self, task_id: str, client: OpenClient, mqtt: MqttClient, output: dataclass):
        self.__task_id = task_id
        self.__mqtt = mqtt
        self.__client = client
        # 任务输出结果
        self.__output = output
        # 任务执行进度
        self.__progress: float = 0
        # 任务执行状态
        self.__status = 1  # 1 开始 2 进度 3 成功 4 失败 5 追加 6 设置
        # 异常信息
        self.__exception = None
        # 监听mqtt状态回调
        self.__mqtt.add_listener(self.__task_id, self.__on_mqtt_message)
        # 各种监听器
        self.__progress_callbacks: list[ProgressCallback] = []
        self.__success_callbacks: list[SuccessCallback] = []
        self.__error_callbacks: list[ErrorCallback] = []

    def __on_mqtt_message(self, msg: Type[MqttResponse]):
        self.__status = msg.event_type
        if self.__status == 2:  # 进度
            self.__progress = float(msg.data)
            for callback in self.__progress_callbacks:
                callback(self.__progress)
        elif self.__status == 3:  # 成功
            self.__output = data_class_init(msg.data, self.__output)
            for callback in self.__success_callbacks:
                callback(self.__output)
        elif self.__status == 4:  # 失败
            self.__exception = ServerError(msg.code, msg.data)
            for callback in self.__error_callbacks:
                callback(self.__exception)

    @property
    def err(self) -> Optional[ServerError]:
        """
        获取任务的错误信息
        :return: 错误信息
        """
        return self.__exception

    @property
    def output(self) -> Optional[T]:
        """
        获取任务的错误信息
        :return: 任务结果（任务未成功或进行中为None）
        """
        if self.__status != 2:
            return None
        return self.__output

    @property
    def progress(self) -> float:
        """
        获取任务执行进度
        :return: 进度信息
        """
        return self.__progress

    @property
    def status(self) -> int:
        """
        获取任务状态
        :return: 任务状态信息 1 创建 2 执行中 3 成功 4 失败
        """
        if self.__status in [3, 4, 1]:
            return self.__status
        else:
            return 2

    def wait(self, progress_callback: ProgressCallback = None) -> T:
        """
        一直阻塞直到任务完成
        :param progress_callback: 进度回调
        :return:
        """
        if progress_callback is not None:
            self.__progress_callbacks.append(progress_callback)
        while True:
            time.sleep(0.1)
            if self.__status == 3:
                logging.info(f"[debug] async out {self.__output}")
                return self.__output
            elif self.__status == 4:
                raise self.__exception

    def listener(
            self,
            on_progress: ProgressCallback = None,
            on_success: SuccessCallback = None,
            on_error: ErrorCallback = None
    ):
        """
        后台监听当前任务完成，不阻塞流程
        :param on_progress: 进度回调
        :param on_success: 成功回调
        :param on_error: 失败回调
        :return:
        """
        if on_progress is not None:
            self.__progress_callbacks.append(on_progress)
        if on_success is not None:
            self.__success_callbacks.append(on_success)
        if on_error is not None:
            self.__error_callbacks.append(on_error)


# 任务执行器
class TaskExecute(Generic[T]):
    def __init__(self, client: OpenClient, mqtt: MqttClient, task_type: int, _input: dict, output: T):
        self.__client = client
        self.__mqtt = mqtt
        self.__task_type = task_type
        self.__input = _input
        self.__output = output

    def execute(self) -> T:
        """同步执行"""
        return data_class_init(self.__client.execute(self.__task_type, self.__input), self.__output)

    def execute_async(self) -> TaskAsyncExecuteResult[T]:
        """异步执行"""
        task_id = self.__client.execute_async(self.__task_type, self.__input)
        return TaskAsyncExecuteResult[T](task_id, self.__client, self.__mqtt, self.__output)

    @staticmethod
    def _get_input(init: dict, **kwargs) -> dict:
        data = init.copy()
        for k, v in kwargs.items():
            if v is not None:
                data[k] = v
        return data
