from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.apps.drive.labels.v2beta import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LabelLock(_message.Message):
    __slots__ = ('name', 'field_id', 'choice_id', 'create_time', 'creator', 'delete_time', 'capabilities', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[LabelLock.State]
        ACTIVE: _ClassVar[LabelLock.State]
        DELETING: _ClassVar[LabelLock.State]
    STATE_UNSPECIFIED: LabelLock.State
    ACTIVE: LabelLock.State
    DELETING: LabelLock.State

    class Capabilities(_message.Message):
        __slots__ = ('can_view_policy',)
        CAN_VIEW_POLICY_FIELD_NUMBER: _ClassVar[int]
        can_view_policy: bool

        def __init__(self, can_view_policy: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    CHOICE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_id: str
    choice_id: str
    create_time: _timestamp_pb2.Timestamp
    creator: _common_pb2.UserInfo
    delete_time: _timestamp_pb2.Timestamp
    capabilities: LabelLock.Capabilities
    state: LabelLock.State

    def __init__(self, name: _Optional[str]=..., field_id: _Optional[str]=..., choice_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., creator: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., capabilities: _Optional[_Union[LabelLock.Capabilities, _Mapping]]=..., state: _Optional[_Union[LabelLock.State, str]]=...) -> None:
        ...