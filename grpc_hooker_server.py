# coding: utf-8
# @author: outlaws-bai
# @date: 2024/05/31 16:07:10
# @description:
import json
import time
import grpc
import base64
from concurrent import futures
from models import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
PORT = 8443

get_encrypt_text = lambda x: json.loads(x)["data"]
to_encrypt_body = lambda x: json.dumps({"data": x.decode()}).encode()

KEY = b"32byteslongsecretkeyforaes256!aa"
IV = b"16byteslongiv456"


# AES加密函数
def aes_encrypt(data: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return base64.b64encode(ct_bytes)


# AES解密函数
def aes_decrypt(data: bytes) -> bytes:
    data1 = base64.b64decode(data)
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    pt = unpad(cipher.decrypt(data1), AES.block_size)
    return pt


class GRpcServicer(HttpHookService):
    def hookRequestToBurp(self, request: Request, *args, **kwargs) -> Request:
        print("try exec hookRequestToBurp")
        request.content = aes_decrypt(get_encrypt_text(request.content))
        return request

    def hookRequestToServer(self, request: Request, *args, **kwargs) -> Request:
        print("try exec hookRequestToServer")
        request.content = to_encrypt_body(aes_encrypt(request.content))
        return request

    def hookResponseToBurp(self, response: Response, *args, **kwargs) -> Response:
        print("try exec hookResponseToBurp")
        response.content = aes_decrypt(get_encrypt_text(response.content))
        return response

    def hookResponseToClient(self, response: Response, *args, **kwargs) -> Response:
        print("try exec hookResponseToClient")
        response.content = to_encrypt_body(aes_encrypt(response.content))
        return response


def main():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_servicer(GRpcServicer(), grpcServer)
    grpcServer.add_insecure_port("[::]:%d" % PORT)
    grpcServer.start()
    print("server start successful at port %d" % PORT)
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == "__main__":
    main()
