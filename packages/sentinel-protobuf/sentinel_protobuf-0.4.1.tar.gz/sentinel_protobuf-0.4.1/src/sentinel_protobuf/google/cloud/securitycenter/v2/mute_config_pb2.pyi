from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MuteConfig(_message.Message):
    __slots__ = ('name', 'description', 'filter', 'create_time', 'update_time', 'most_recent_editor', 'type', 'expiry_time')

    class MuteConfigType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUTE_CONFIG_TYPE_UNSPECIFIED: _ClassVar[MuteConfig.MuteConfigType]
        STATIC: _ClassVar[MuteConfig.MuteConfigType]
        DYNAMIC: _ClassVar[MuteConfig.MuteConfigType]
    MUTE_CONFIG_TYPE_UNSPECIFIED: MuteConfig.MuteConfigType
    STATIC: MuteConfig.MuteConfigType
    DYNAMIC: MuteConfig.MuteConfigType
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MOST_RECENT_EDITOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    filter: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    most_recent_editor: str
    type: MuteConfig.MuteConfigType
    expiry_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., filter: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., most_recent_editor: _Optional[str]=..., type: _Optional[_Union[MuteConfig.MuteConfigType, str]]=..., expiry_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...