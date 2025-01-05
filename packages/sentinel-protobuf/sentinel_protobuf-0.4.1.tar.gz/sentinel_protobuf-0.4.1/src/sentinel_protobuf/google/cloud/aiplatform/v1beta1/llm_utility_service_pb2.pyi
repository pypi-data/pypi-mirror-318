from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComputeTokensRequest(_message.Message):
    __slots__ = ("endpoint", "instances", "model", "contents")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    instances: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    model: str
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    def __init__(self, endpoint: _Optional[str] = ..., instances: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ..., model: _Optional[str] = ..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]] = ...) -> None: ...

class TokensInfo(_message.Message):
    __slots__ = ("tokens", "token_ids", "role")
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IDS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedScalarFieldContainer[bytes]
    token_ids: _containers.RepeatedScalarFieldContainer[int]
    role: str
    def __init__(self, tokens: _Optional[_Iterable[bytes]] = ..., token_ids: _Optional[_Iterable[int]] = ..., role: _Optional[str] = ...) -> None: ...

class ComputeTokensResponse(_message.Message):
    __slots__ = ("tokens_info",)
    TOKENS_INFO_FIELD_NUMBER: _ClassVar[int]
    tokens_info: _containers.RepeatedCompositeFieldContainer[TokensInfo]
    def __init__(self, tokens_info: _Optional[_Iterable[_Union[TokensInfo, _Mapping]]] = ...) -> None: ...
