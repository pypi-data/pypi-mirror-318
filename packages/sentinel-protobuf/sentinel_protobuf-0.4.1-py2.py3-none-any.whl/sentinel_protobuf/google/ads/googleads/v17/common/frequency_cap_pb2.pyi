from google.ads.googleads.v17.enums import frequency_cap_event_type_pb2 as _frequency_cap_event_type_pb2
from google.ads.googleads.v17.enums import frequency_cap_level_pb2 as _frequency_cap_level_pb2
from google.ads.googleads.v17.enums import frequency_cap_time_unit_pb2 as _frequency_cap_time_unit_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FrequencyCapEntry(_message.Message):
    __slots__ = ("key", "cap")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CAP_FIELD_NUMBER: _ClassVar[int]
    key: FrequencyCapKey
    cap: int
    def __init__(self, key: _Optional[_Union[FrequencyCapKey, _Mapping]] = ..., cap: _Optional[int] = ...) -> None: ...

class FrequencyCapKey(_message.Message):
    __slots__ = ("level", "event_type", "time_unit", "time_length")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_UNIT_FIELD_NUMBER: _ClassVar[int]
    TIME_LENGTH_FIELD_NUMBER: _ClassVar[int]
    level: _frequency_cap_level_pb2.FrequencyCapLevelEnum.FrequencyCapLevel
    event_type: _frequency_cap_event_type_pb2.FrequencyCapEventTypeEnum.FrequencyCapEventType
    time_unit: _frequency_cap_time_unit_pb2.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    time_length: int
    def __init__(self, level: _Optional[_Union[_frequency_cap_level_pb2.FrequencyCapLevelEnum.FrequencyCapLevel, str]] = ..., event_type: _Optional[_Union[_frequency_cap_event_type_pb2.FrequencyCapEventTypeEnum.FrequencyCapEventType, str]] = ..., time_unit: _Optional[_Union[_frequency_cap_time_unit_pb2.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit, str]] = ..., time_length: _Optional[int] = ...) -> None: ...
