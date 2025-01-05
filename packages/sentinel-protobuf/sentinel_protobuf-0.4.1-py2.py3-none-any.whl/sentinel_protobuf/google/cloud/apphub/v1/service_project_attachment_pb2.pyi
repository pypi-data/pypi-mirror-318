from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ServiceProjectAttachment(_message.Message):
    __slots__ = ('name', 'service_project', 'create_time', 'uid', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ServiceProjectAttachment.State]
        CREATING: _ClassVar[ServiceProjectAttachment.State]
        ACTIVE: _ClassVar[ServiceProjectAttachment.State]
        DELETING: _ClassVar[ServiceProjectAttachment.State]
    STATE_UNSPECIFIED: ServiceProjectAttachment.State
    CREATING: ServiceProjectAttachment.State
    ACTIVE: ServiceProjectAttachment.State
    DELETING: ServiceProjectAttachment.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROJECT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_project: str
    create_time: _timestamp_pb2.Timestamp
    uid: str
    state: ServiceProjectAttachment.State

    def __init__(self, name: _Optional[str]=..., service_project: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., uid: _Optional[str]=..., state: _Optional[_Union[ServiceProjectAttachment.State, str]]=...) -> None:
        ...