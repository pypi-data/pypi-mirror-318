from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Instance(_message.Message):
    __slots__ = ('name', 'id', 'app_engine_release', 'availability', 'vm_name', 'vm_zone_name', 'vm_id', 'start_time', 'requests', 'errors', 'qps', 'average_latency', 'memory_usage', 'vm_status', 'vm_debug_enabled', 'vm_ip', 'vm_liveness')

    class Availability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[Instance.Availability]
        RESIDENT: _ClassVar[Instance.Availability]
        DYNAMIC: _ClassVar[Instance.Availability]
    UNSPECIFIED: Instance.Availability
    RESIDENT: Instance.Availability
    DYNAMIC: Instance.Availability

    class Liveness(_message.Message):
        __slots__ = ()

        class LivenessState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LIVENESS_STATE_UNSPECIFIED: _ClassVar[Instance.Liveness.LivenessState]
            UNKNOWN: _ClassVar[Instance.Liveness.LivenessState]
            HEALTHY: _ClassVar[Instance.Liveness.LivenessState]
            UNHEALTHY: _ClassVar[Instance.Liveness.LivenessState]
            DRAINING: _ClassVar[Instance.Liveness.LivenessState]
            TIMEOUT: _ClassVar[Instance.Liveness.LivenessState]
        LIVENESS_STATE_UNSPECIFIED: Instance.Liveness.LivenessState
        UNKNOWN: Instance.Liveness.LivenessState
        HEALTHY: Instance.Liveness.LivenessState
        UNHEALTHY: Instance.Liveness.LivenessState
        DRAINING: Instance.Liveness.LivenessState
        TIMEOUT: Instance.Liveness.LivenessState

        def __init__(self) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_RELEASE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    QPS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_LATENCY_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    VM_STATUS_FIELD_NUMBER: _ClassVar[int]
    VM_DEBUG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VM_IP_FIELD_NUMBER: _ClassVar[int]
    VM_LIVENESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    app_engine_release: str
    availability: Instance.Availability
    vm_name: str
    vm_zone_name: str
    vm_id: str
    start_time: _timestamp_pb2.Timestamp
    requests: int
    errors: int
    qps: float
    average_latency: int
    memory_usage: int
    vm_status: str
    vm_debug_enabled: bool
    vm_ip: str
    vm_liveness: Instance.Liveness.LivenessState

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., app_engine_release: _Optional[str]=..., availability: _Optional[_Union[Instance.Availability, str]]=..., vm_name: _Optional[str]=..., vm_zone_name: _Optional[str]=..., vm_id: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., requests: _Optional[int]=..., errors: _Optional[int]=..., qps: _Optional[float]=..., average_latency: _Optional[int]=..., memory_usage: _Optional[int]=..., vm_status: _Optional[str]=..., vm_debug_enabled: bool=..., vm_ip: _Optional[str]=..., vm_liveness: _Optional[_Union[Instance.Liveness.LivenessState, str]]=...) -> None:
        ...