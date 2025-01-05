from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Device(_message.Message):
    __slots__ = ('id', 'type', 'traits', 'name', 'will_report_state', 'room_hint', 'structure_hint', 'device_info', 'attributes', 'custom_data', 'other_device_ids', 'notification_supported_by_agent')
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WILL_REPORT_STATE_FIELD_NUMBER: _ClassVar[int]
    ROOM_HINT_FIELD_NUMBER: _ClassVar[int]
    STRUCTURE_HINT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DATA_FIELD_NUMBER: _ClassVar[int]
    OTHER_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SUPPORTED_BY_AGENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    traits: _containers.RepeatedScalarFieldContainer[str]
    name: DeviceNames
    will_report_state: bool
    room_hint: str
    structure_hint: str
    device_info: DeviceInfo
    attributes: _struct_pb2.Struct
    custom_data: _struct_pb2.Struct
    other_device_ids: _containers.RepeatedCompositeFieldContainer[AgentOtherDeviceId]
    notification_supported_by_agent: bool

    def __init__(self, id: _Optional[str]=..., type: _Optional[str]=..., traits: _Optional[_Iterable[str]]=..., name: _Optional[_Union[DeviceNames, _Mapping]]=..., will_report_state: bool=..., room_hint: _Optional[str]=..., structure_hint: _Optional[str]=..., device_info: _Optional[_Union[DeviceInfo, _Mapping]]=..., attributes: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., custom_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., other_device_ids: _Optional[_Iterable[_Union[AgentOtherDeviceId, _Mapping]]]=..., notification_supported_by_agent: bool=...) -> None:
        ...

class DeviceNames(_message.Message):
    __slots__ = ('name', 'nicknames', 'default_names')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAMES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_NAMES_FIELD_NUMBER: _ClassVar[int]
    name: str
    nicknames: _containers.RepeatedScalarFieldContainer[str]
    default_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., nicknames: _Optional[_Iterable[str]]=..., default_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeviceInfo(_message.Message):
    __slots__ = ('manufacturer', 'model', 'hw_version', 'sw_version')
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    HW_VERSION_FIELD_NUMBER: _ClassVar[int]
    SW_VERSION_FIELD_NUMBER: _ClassVar[int]
    manufacturer: str
    model: str
    hw_version: str
    sw_version: str

    def __init__(self, manufacturer: _Optional[str]=..., model: _Optional[str]=..., hw_version: _Optional[str]=..., sw_version: _Optional[str]=...) -> None:
        ...

class AgentOtherDeviceId(_message.Message):
    __slots__ = ('agent_id', 'device_id')
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    device_id: str

    def __init__(self, agent_id: _Optional[str]=..., device_id: _Optional[str]=...) -> None:
        ...