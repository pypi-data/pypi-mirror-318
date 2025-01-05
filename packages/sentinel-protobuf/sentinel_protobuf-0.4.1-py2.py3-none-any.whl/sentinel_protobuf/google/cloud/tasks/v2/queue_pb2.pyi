from google.api import resource_pb2 as _resource_pb2
from google.cloud.tasks.v2 import target_pb2 as _target_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Queue(_message.Message):
    __slots__ = ('name', 'app_engine_routing_override', 'rate_limits', 'retry_config', 'state', 'purge_time', 'stackdriver_logging_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Queue.State]
        RUNNING: _ClassVar[Queue.State]
        PAUSED: _ClassVar[Queue.State]
        DISABLED: _ClassVar[Queue.State]
    STATE_UNSPECIFIED: Queue.State
    RUNNING: Queue.State
    PAUSED: Queue.State
    DISABLED: Queue.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_ROUTING_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    RETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PURGE_TIME_FIELD_NUMBER: _ClassVar[int]
    STACKDRIVER_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    app_engine_routing_override: _target_pb2.AppEngineRouting
    rate_limits: RateLimits
    retry_config: RetryConfig
    state: Queue.State
    purge_time: _timestamp_pb2.Timestamp
    stackdriver_logging_config: StackdriverLoggingConfig

    def __init__(self, name: _Optional[str]=..., app_engine_routing_override: _Optional[_Union[_target_pb2.AppEngineRouting, _Mapping]]=..., rate_limits: _Optional[_Union[RateLimits, _Mapping]]=..., retry_config: _Optional[_Union[RetryConfig, _Mapping]]=..., state: _Optional[_Union[Queue.State, str]]=..., purge_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., stackdriver_logging_config: _Optional[_Union[StackdriverLoggingConfig, _Mapping]]=...) -> None:
        ...

class RateLimits(_message.Message):
    __slots__ = ('max_dispatches_per_second', 'max_burst_size', 'max_concurrent_dispatches')
    MAX_DISPATCHES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    MAX_BURST_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_DISPATCHES_FIELD_NUMBER: _ClassVar[int]
    max_dispatches_per_second: float
    max_burst_size: int
    max_concurrent_dispatches: int

    def __init__(self, max_dispatches_per_second: _Optional[float]=..., max_burst_size: _Optional[int]=..., max_concurrent_dispatches: _Optional[int]=...) -> None:
        ...

class RetryConfig(_message.Message):
    __slots__ = ('max_attempts', 'max_retry_duration', 'min_backoff', 'max_backoff', 'max_doublings')
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_DURATION_FIELD_NUMBER: _ClassVar[int]
    MIN_BACKOFF_FIELD_NUMBER: _ClassVar[int]
    MAX_BACKOFF_FIELD_NUMBER: _ClassVar[int]
    MAX_DOUBLINGS_FIELD_NUMBER: _ClassVar[int]
    max_attempts: int
    max_retry_duration: _duration_pb2.Duration
    min_backoff: _duration_pb2.Duration
    max_backoff: _duration_pb2.Duration
    max_doublings: int

    def __init__(self, max_attempts: _Optional[int]=..., max_retry_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., min_backoff: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_backoff: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_doublings: _Optional[int]=...) -> None:
        ...

class StackdriverLoggingConfig(_message.Message):
    __slots__ = ('sampling_ratio',)
    SAMPLING_RATIO_FIELD_NUMBER: _ClassVar[int]
    sampling_ratio: float

    def __init__(self, sampling_ratio: _Optional[float]=...) -> None:
        ...