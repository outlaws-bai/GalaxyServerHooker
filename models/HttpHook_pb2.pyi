from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StringList(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ["secure", "host", "port", "version", "method", "path", "query", "headers", "content"]
    class QueryEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StringList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[StringList, _Mapping]] = ...) -> None: ...
    class HeadersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StringList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[StringList, _Mapping]] = ...) -> None: ...
    SECURE_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    secure: bool
    host: str
    port: int
    version: str
    method: str
    path: str
    query: _containers.MessageMap[str, StringList]
    headers: _containers.MessageMap[str, StringList]
    content: bytes
    def __init__(self, secure: bool = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., version: _Optional[str] = ..., method: _Optional[str] = ..., path: _Optional[str] = ..., query: _Optional[_Mapping[str, StringList]] = ..., headers: _Optional[_Mapping[str, StringList]] = ..., content: _Optional[bytes] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["version", "statusCode", "reason", "headers", "content"]
    class HeadersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StringList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[StringList, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    version: str
    statusCode: int
    reason: str
    headers: _containers.MessageMap[str, StringList]
    content: bytes
    def __init__(self, version: _Optional[str] = ..., statusCode: _Optional[int] = ..., reason: _Optional[str] = ..., headers: _Optional[_Mapping[str, StringList]] = ..., content: _Optional[bytes] = ...) -> None: ...
