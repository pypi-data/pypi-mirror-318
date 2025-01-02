from zyjj_open_sdk.core.client.base import BaseClient, BASE
from httpx import Client


class OpenAsyncClient(BaseClient):
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

    # async def get_point(self) -> int:
    #     pass
    #
    # async def execute(self, task: Task):
    #     pass
    #
    # async def execute_async(self, task: Task):
    #     pass
