from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Webhook(_message.Message):
    __slots__ = ('handlers', 'https_endpoint', 'inline_cloud_function')

    class Handler(_message.Message):
        __slots__ = ('name',)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str

        def __init__(self, name: _Optional[str]=...) -> None:
            ...

    class HttpsEndpoint(_message.Message):
        __slots__ = ('base_url', 'http_headers', 'endpoint_api_version')

        class HttpHeadersEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        BASE_URL_FIELD_NUMBER: _ClassVar[int]
        HTTP_HEADERS_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_API_VERSION_FIELD_NUMBER: _ClassVar[int]
        base_url: str
        http_headers: _containers.ScalarMap[str, str]
        endpoint_api_version: int

        def __init__(self, base_url: _Optional[str]=..., http_headers: _Optional[_Mapping[str, str]]=..., endpoint_api_version: _Optional[int]=...) -> None:
            ...

    class InlineCloudFunction(_message.Message):
        __slots__ = ('execute_function',)
        EXECUTE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
        execute_function: str

        def __init__(self, execute_function: _Optional[str]=...) -> None:
            ...
    HANDLERS_FIELD_NUMBER: _ClassVar[int]
    HTTPS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INLINE_CLOUD_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    handlers: _containers.RepeatedCompositeFieldContainer[Webhook.Handler]
    https_endpoint: Webhook.HttpsEndpoint
    inline_cloud_function: Webhook.InlineCloudFunction

    def __init__(self, handlers: _Optional[_Iterable[_Union[Webhook.Handler, _Mapping]]]=..., https_endpoint: _Optional[_Union[Webhook.HttpsEndpoint, _Mapping]]=..., inline_cloud_function: _Optional[_Union[Webhook.InlineCloudFunction, _Mapping]]=...) -> None:
        ...