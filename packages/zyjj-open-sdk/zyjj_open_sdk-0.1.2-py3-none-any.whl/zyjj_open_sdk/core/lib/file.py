import logging

from zyjj_open_sdk.core.client import BaseClient
from zyjj_open_sdk.core.entity import FileObject
from zyjj_open_sdk.core.exception import SDKError, RequestError
import httpx
from pathlib import Path


class FileUtils:
    def __init__(self, client: BaseClient):
        self.__client = client
        self.__timout = 600

    # 全量上传
    def __full_upload(self, file_name: str, data: bytes, source: int):
        token = self.__client.get_file_token(file_name, len(data), source)
        auth, file = token["auth"], token["file"]
        # 上传文件
        res = httpx.put(auth["url"], content=data, headers=auth["header"], timeout=self.__timout)
        if res.status_code != 200:
            raise RequestError(res.status_code, res.text)
        return file

    def __multipart_upload(self, file_name: str, file_size: int, path: str, source: int) -> dict:
        upload_id = str(self.__client.file_multipart_init(file_name, file_size, source))
        part_list = []
        # 分片读取文件信息
        with open(path, "rb") as f:
            # 我们每次分片大小为10M
            chunk_size = 1024 * 1024 * 10
            # part_num 需要从1开始
            part_num = 1
            while True:
                part_data = f.read(chunk_size)  # 读取指定大小的块
                if not part_data:  # 如果没有更多数据，退出循环
                    break
                # 获取鉴权信息
                data = self.__client.file_multipart_part(upload_id, part_num)
                # 上传文件
                res = httpx.put(data["url"], content=part_data, headers=data["header"], timeout=self.__timout)
                if res.status_code != 200:
                    raise RequestError(res.status_code, res.text)
                # 从返回的header中获取etag信息
                part_list.append({"part_num": part_num, "etag": res.headers.get("etag")})
                part_num += 1
        logging.info(f"part list {part_list}")
        # 最后我们完成上传
        return self.__client.file_multipart_complete(upload_id, part_list)

    # 文件上传
    def file_upload(self, file: FileObject, source: int = 1) -> dict:
        if file.file_content is not None and len(file.file_content):
            # 如果字节流有数据就直接从字节流中加载
            return self.__full_upload(file.file_name, file.file_content, source)
        elif file.path is not None:
            path = Path(file.path)
            # 判断一下文件是否存在
            if not path.is_file():
                raise SDKError("文件不存在")
            # 判断一下文件大小
            file_size = path.stat().st_size
            if file_size > 1024 * 1024 * 30:  # 超过30M就使用分片上传
                return self.__multipart_upload(file.file_name, file_size, file.path, source)
            else:
                return self.__full_upload(file.file_name, path.read_bytes(), source)
