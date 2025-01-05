from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.clouderrorreporting.v1beta1 import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetGroupRequest(_message.Message):
    __slots__ = ('group_name',)
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    group_name: str

    def __init__(self, group_name: _Optional[str]=...) -> None:
        ...

class UpdateGroupRequest(_message.Message):
    __slots__ = ('group',)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: _common_pb2.ErrorGroup

    def __init__(self, group: _Optional[_Union[_common_pb2.ErrorGroup, _Mapping]]=...) -> None:
        ...