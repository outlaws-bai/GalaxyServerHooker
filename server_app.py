# coding: utf-8
# @author: outlaws-bai
# @date: 2023/12/06 20:42:30
# @description:


import time
import grpc
from concurrent import futures
from grpc_models.Counter_pb2_grpc import *
import grpc_models.Counter_pb2 as Counter

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
PORT = 50051


class GRpcServiceImpl(CounterService):
    def hookRequestToBurp(self, request, context):
        print(f'func name: hookRequestToBurp url: {request.request.url}')
        new_header = Counter.Header(name='testHeaderName', value='testHeaderValue')
        request.request.header.extend([new_header])
        return request.request

    def hookRequestToServer(self, request, context):
        ...

    def hookResponseToBurp(self, request, context):
        ...

    def hookResponseToClient(self, request, context):
        ...


def server():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CounterServiceServicer_to_server(GRpcServiceImpl(), grpcServer)
    grpcServer.add_insecure_port('[::]:%d' % PORT)
    grpcServer.start()
    print('server start successful at port %d' % PORT)
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    server()
