from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1beta1 import extension_pb2 as _extension_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteExtensionRequest(_message.Message):
    __slots__ = ("name", "operation_id", "operation_params", "runtime_auth_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    operation_id: str
    operation_params: _struct_pb2.Struct
    runtime_auth_config: _extension_pb2.AuthConfig
    def __init__(self, name: _Optional[str] = ..., operation_id: _Optional[str] = ..., operation_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., runtime_auth_config: _Optional[_Union[_extension_pb2.AuthConfig, _Mapping]] = ...) -> None: ...

class ExecuteExtensionResponse(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class QueryExtensionRequest(_message.Message):
    __slots__ = ("name", "contents")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    def __init__(self, name: _Optional[str] = ..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]] = ...) -> None: ...

class QueryExtensionResponse(_message.Message):
    __slots__ = ("steps", "failure_message")
    STEPS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    steps: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    failure_message: str
    def __init__(self, steps: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]] = ..., failure_message: _Optional[str] = ...) -> None: ...
