# coding: utf-8
# @author: outlaws-bai
# @date: 2024/05/31 16:07:10
# @description:
import json
import time
import grpc
from concurrent import futures
from models import *
from server_fast import aes_decrypt, aes_encrypt

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
PORT = 8443

get_origin_body = lambda x: json.loads(x)["data"]
to_encrypt_body = lambda x: json.dumps({"data": x.decode()}).encode()


class GRpcServicer(HttpHookService):
    def hookRequestToBurp(self, request: Request, context) -> Request:
        request.content = aes_decrypt(get_origin_body(request.content))
        return request

    def hookRequestToServer(self, request: Request, context) -> Request:
        request.content = to_encrypt_body(aes_encrypt(request.content))
        return request

    def hookResponseToBurp(self, response: Response, context) -> Response:
        response.content = aes_decrypt(get_origin_body(response.content))
        return response

    def hookResponseToClient(self, response: Response, context) -> Response:
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
