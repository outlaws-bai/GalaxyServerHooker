# coding: utf-8
# @author: outlaws-bai
# @date: 2023/12/06 20:42:30
# @description:
from grpc_models.Counter_pb2_grpc import CounterService


class GRpcServiceImpl(CounterService):
    def counterRequestToBeSent(self, request, context):
        ...

    def counterResponseReceived(self, request, context):
        ...

    def counterProxyRequestReceived(self, request, context):
        ...

    def counterProxyRequestToBeSent(self, request, context):
        ...

    def counterProxyResponseReceived(self, request, context):
        ...

    def counterProxyResponseToBeSent(self, request, context):
        ...
