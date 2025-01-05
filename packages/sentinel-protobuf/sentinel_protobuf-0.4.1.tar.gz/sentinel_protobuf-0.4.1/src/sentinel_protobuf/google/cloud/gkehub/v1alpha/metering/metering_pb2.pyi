from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MembershipState(_message.Message):
    __slots__ = ('last_measurement_time', 'precise_last_measured_cluster_vcpu_capacity')
    LAST_MEASUREMENT_TIME_FIELD_NUMBER: _ClassVar[int]
    PRECISE_LAST_MEASURED_CLUSTER_VCPU_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    last_measurement_time: _timestamp_pb2.Timestamp
    precise_last_measured_cluster_vcpu_capacity: float

    def __init__(self, last_measurement_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., precise_last_measured_cluster_vcpu_capacity: _Optional[float]=...) -> None:
        ...