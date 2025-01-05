from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EffectiveEventThreatDetectionCustomModule(_message.Message):
    __slots__ = ('name', 'config', 'enablement_state', 'type', 'display_name', 'description')

    class EnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[EffectiveEventThreatDetectionCustomModule.EnablementState]
        ENABLED: _ClassVar[EffectiveEventThreatDetectionCustomModule.EnablementState]
        DISABLED: _ClassVar[EffectiveEventThreatDetectionCustomModule.EnablementState]
    ENABLEMENT_STATE_UNSPECIFIED: EffectiveEventThreatDetectionCustomModule.EnablementState
    ENABLED: EffectiveEventThreatDetectionCustomModule.EnablementState
    DISABLED: EffectiveEventThreatDetectionCustomModule.EnablementState
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: _struct_pb2.Struct
    enablement_state: EffectiveEventThreatDetectionCustomModule.EnablementState
    type: str
    display_name: str
    description: str

    def __init__(self, name: _Optional[str]=..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., enablement_state: _Optional[_Union[EffectiveEventThreatDetectionCustomModule.EnablementState, str]]=..., type: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...