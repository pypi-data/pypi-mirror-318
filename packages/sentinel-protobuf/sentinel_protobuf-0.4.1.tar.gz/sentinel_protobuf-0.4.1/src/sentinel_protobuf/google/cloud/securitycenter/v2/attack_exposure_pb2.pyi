from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AttackExposure(_message.Message):
    __slots__ = ('score', 'latest_calculation_time', 'attack_exposure_result', 'state', 'exposed_high_value_resources_count', 'exposed_medium_value_resources_count', 'exposed_low_value_resources_count')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AttackExposure.State]
        CALCULATED: _ClassVar[AttackExposure.State]
        NOT_CALCULATED: _ClassVar[AttackExposure.State]
    STATE_UNSPECIFIED: AttackExposure.State
    CALCULATED: AttackExposure.State
    NOT_CALCULATED: AttackExposure.State
    SCORE_FIELD_NUMBER: _ClassVar[int]
    LATEST_CALCULATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTACK_EXPOSURE_RESULT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPOSED_HIGH_VALUE_RESOURCES_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPOSED_MEDIUM_VALUE_RESOURCES_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPOSED_LOW_VALUE_RESOURCES_COUNT_FIELD_NUMBER: _ClassVar[int]
    score: float
    latest_calculation_time: _timestamp_pb2.Timestamp
    attack_exposure_result: str
    state: AttackExposure.State
    exposed_high_value_resources_count: int
    exposed_medium_value_resources_count: int
    exposed_low_value_resources_count: int

    def __init__(self, score: _Optional[float]=..., latest_calculation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., attack_exposure_result: _Optional[str]=..., state: _Optional[_Union[AttackExposure.State, str]]=..., exposed_high_value_resources_count: _Optional[int]=..., exposed_medium_value_resources_count: _Optional[int]=..., exposed_low_value_resources_count: _Optional[int]=...) -> None:
        ...