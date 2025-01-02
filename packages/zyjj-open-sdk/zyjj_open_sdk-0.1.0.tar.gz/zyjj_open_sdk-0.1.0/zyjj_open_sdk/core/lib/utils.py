import logging

from zyjj_open_sdk.core.entity import FileObject
from zyjj_open_sdk.core.client import BaseClient
from zyjj_open_sdk.core.lib.file import FileUtils


def get_input(client: BaseClient, init: dict, data: dict) -> dict:
    for k, v in data.items():
        if v is None:
            continue
        # 如果v是文件类型就需要上传获取上传地址
        if isinstance(v, FileObject):
            v = FileUtils(client).file_upload(v)
        # 如果k包含.那么就需要拆分
        if '.' in k:
            k = k.split('.')
            # 目前只支持两级
            k0, k1 = k
            if k0 not in init:
                init[k0] = {}
            init[k0][k1] = v
        else:
            init[k] = v
    logging.info(f"input is {init}")
    return init
