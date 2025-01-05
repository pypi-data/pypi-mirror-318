from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventThreatDetectionCustomModule(_message.Message):
    __slots__ = ('name', 'config', 'ancestor_module', 'enablement_state', 'type', 'display_name', 'description', 'update_time', 'last_editor')

    class EnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[EventThreatDetectionCustomModule.EnablementState]
        ENABLED: _ClassVar[EventThreatDetectionCustomModule.EnablementState]
        DISABLED: _ClassVar[EventThreatDetectionCustomModule.EnablementState]
        INHERITED: _ClassVar[EventThreatDetectionCustomModule.EnablementState]
    ENABLEMENT_STATE_UNSPECIFIED: EventThreatDetectionCustomModule.EnablementState
    ENABLED: EventThreatDetectionCustomModule.EnablementState
    DISABLED: EventThreatDetectionCustomModule.EnablementState
    INHERITED: EventThreatDetectionCustomModule.EnablementState
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_MODULE_FIELD_NUMBER: _ClassVar[int]
    ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: _struct_pb2.Struct
    ancestor_module: str
    enablement_state: EventThreatDetectionCustomModule.EnablementState
    type: str
    display_name: str
    description: str
    update_time: _timestamp_pb2.Timestamp
    last_editor: str

    def __init__(self, name: _Optional[str]=..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., ancestor_module: _Optional[str]=..., enablement_state: _Optional[_Union[EventThreatDetectionCustomModule.EnablementState, str]]=..., type: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_editor: _Optional[str]=...) -> None:
        ...