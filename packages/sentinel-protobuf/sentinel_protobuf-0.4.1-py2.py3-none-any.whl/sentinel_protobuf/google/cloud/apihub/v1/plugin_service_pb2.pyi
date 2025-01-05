from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apihub.v1 import common_fields_pb2 as _common_fields_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Plugin(_message.Message):
    __slots__ = ('name', 'display_name', 'type', 'description', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Plugin.State]
        ENABLED: _ClassVar[Plugin.State]
        DISABLED: _ClassVar[Plugin.State]
    STATE_UNSPECIFIED: Plugin.State
    ENABLED: Plugin.State
    DISABLED: Plugin.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    type: _common_fields_pb2.AttributeValues
    description: str
    state: Plugin.State

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., type: _Optional[_Union[_common_fields_pb2.AttributeValues, _Mapping]]=..., description: _Optional[str]=..., state: _Optional[_Union[Plugin.State, str]]=...) -> None:
        ...

class GetPluginRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EnablePluginRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DisablePluginRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...