from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FulfillmentPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FULFILLMENT_PERIOD_UNSPECIFIED: _ClassVar[FulfillmentPeriod]
    FULFILLMENT_PERIOD_NORMAL: _ClassVar[FulfillmentPeriod]
    FULFILLMENT_PERIOD_EXTENDED: _ClassVar[FulfillmentPeriod]
FULFILLMENT_PERIOD_UNSPECIFIED: FulfillmentPeriod
FULFILLMENT_PERIOD_NORMAL: FulfillmentPeriod
FULFILLMENT_PERIOD_EXTENDED: FulfillmentPeriod

class OperationProgress(_message.Message):
    __slots__ = ('progress_percent', 'start_time', 'end_time')
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, progress_percent: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ReplicaSelection(_message.Message):
    __slots__ = ('location',)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: str

    def __init__(self, location: _Optional[str]=...) -> None:
        ...