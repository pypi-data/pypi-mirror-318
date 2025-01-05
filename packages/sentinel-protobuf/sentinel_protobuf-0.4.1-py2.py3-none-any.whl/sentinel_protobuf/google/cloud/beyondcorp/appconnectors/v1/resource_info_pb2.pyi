from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HealthStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTH_STATUS_UNSPECIFIED: _ClassVar[HealthStatus]
    HEALTHY: _ClassVar[HealthStatus]
    UNHEALTHY: _ClassVar[HealthStatus]
    UNRESPONSIVE: _ClassVar[HealthStatus]
    DEGRADED: _ClassVar[HealthStatus]
HEALTH_STATUS_UNSPECIFIED: HealthStatus
HEALTHY: HealthStatus
UNHEALTHY: HealthStatus
UNRESPONSIVE: HealthStatus
DEGRADED: HealthStatus

class ResourceInfo(_message.Message):
    __slots__ = ('id', 'status', 'resource', 'time', 'sub')
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: HealthStatus
    resource: _any_pb2.Any
    time: _timestamp_pb2.Timestamp
    sub: _containers.RepeatedCompositeFieldContainer[ResourceInfo]

    def __init__(self, id: _Optional[str]=..., status: _Optional[_Union[HealthStatus, str]]=..., resource: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., sub: _Optional[_Iterable[_Union[ResourceInfo, _Mapping]]]=...) -> None:
        ...