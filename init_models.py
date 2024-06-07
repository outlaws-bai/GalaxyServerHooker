# coding: utf-8
# @author: outlaws-bai
# @date: 2023/12/06 20:43:20
# @description:
import os
from pathlib import Path

# 修改HttpHook.proto

os.system(
    "python -m grpc_tools.protoc -I./proto --python_out=models --pyi_out=models --grpc_python_out=models proto/HttpHook.proto"
)

with open("./models/HttpHook_pb2_grpc.py", "r+", encoding="utf-8") as f:
    origin_str: str = f.read()
    new_str = origin_str.replace(
        "import HttpHook_pb2 as HttpHook__pb2",
        "from . import HttpHook_pb2 as HttpHook__pb2",
    )
    f.seek(0)
    f.write(new_str)
