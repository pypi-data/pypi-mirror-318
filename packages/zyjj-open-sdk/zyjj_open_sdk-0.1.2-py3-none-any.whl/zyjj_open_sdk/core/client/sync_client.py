from typing import Literal, Any

from zyjj_open_sdk.core.client.base import BaseClient, BASE
from zyjj_open_sdk.core.exception import SDKError, ServerError, RequestError
from httpx import Client, Response


class OpenClient(BaseClient):
    def __init__(self, sk: str):
        super().__init__(sk)
        self.__sk = sk
        self.__client = Client(
            base_url=BASE,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.__sk}"
            },
            timeout=600
        )
        self.__report_event()

    def __request(self, method: Literal['get', 'post'], url: str, data: dict = None) -> Any:
        res: Response
        if method == 'get':
            res = self.__client.get(url)
        elif method == 'post':
            res = self.__client.post(url, json=data)
        else:
            raise SDKError("method error")
        if res.status_code != 200:
            raise RequestError(res.status_code, res.content)
        data = res.json()
        code = data.get('code', -1)
        if code != 0:
            raise ServerError(code, data.get('message', ''))
        return data.get('data', None)

    def __report_event(self):
        self.__request('get', url=f'common/app/info?os=sdk-python&version={super().version}')

    def get_point(self) -> int:
        return self.__request('get', 'open/account/point')

    def execute(self, task_type: int, _input: dict) -> dict:
        return self.__request('post', 'open/task/sync', {
            "task_type": task_type,
            "input": _input
        })

    def execute_async(self, task_type: int, _input: dict) -> str:
        return self.__request('post', 'open/task', {
            "task_type": task_type,
            "input": _input
        })

    def get_task_status(self, task_id: str) -> dict:
        return self.__request('get', f'open/task/{task_id}')

    def get_file_token(self, file_name: str, file_size: int, source: int = 1) -> dict:
        return self.__request('post', f'open/file', {
            "file_name": file_name,
            "file_size": file_size,
            "source": source
        })

    def file_multipart_init(self, file_name: str, file_size: int, source: int = 1) -> dict:
        return self.__request('post', f'open/file/multipart/init', {
            "file_name": file_name,
            "file_size": file_size,
            "source": source
        })

    def file_multipart_part(self, upload_id: str, part_num: int) -> dict:
        return self.__request('post', f'open/file/multipart/part', {
            "upload_id": upload_id,
            "part_num": part_num
        })

    def file_multipart_complete(self, upload_id: str, part_list: list) -> dict:
        return self.__request('post', f'open/file/multipart/complete', {
            "upload_id": upload_id,
            "part_list": part_list
        })

    def get_mqtt_task(self) -> dict:
        return self.__request('get', f'open/mqtt/task')
