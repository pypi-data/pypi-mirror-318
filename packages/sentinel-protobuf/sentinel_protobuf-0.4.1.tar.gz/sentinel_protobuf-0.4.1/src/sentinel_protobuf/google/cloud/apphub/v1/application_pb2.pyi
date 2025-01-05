from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apphub.v1 import attributes_pb2 as _attributes_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Application(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'attributes', 'create_time', 'update_time', 'scope', 'uid', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Application.State]
        CREATING: _ClassVar[Application.State]
        ACTIVE: _ClassVar[Application.State]
        DELETING: _ClassVar[Application.State]
    STATE_UNSPECIFIED: Application.State
    CREATING: Application.State
    ACTIVE: Application.State
    DELETING: Application.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    attributes: _attributes_pb2.Attributes
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    scope: Scope
    uid: str
    state: Application.State

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., attributes: _Optional[_Union[_attributes_pb2.Attributes, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., scope: _Optional[_Union[Scope, _Mapping]]=..., uid: _Optional[str]=..., state: _Optional[_Union[Application.State, str]]=...) -> None:
        ...

class Scope(_message.Message):
    __slots__ = ('type',)

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Scope.Type]
        REGIONAL: _ClassVar[Scope.Type]
    TYPE_UNSPECIFIED: Scope.Type
    REGIONAL: Scope.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: Scope.Type

    def __init__(self, type: _Optional[_Union[Scope.Type, str]]=...) -> None:
        ...