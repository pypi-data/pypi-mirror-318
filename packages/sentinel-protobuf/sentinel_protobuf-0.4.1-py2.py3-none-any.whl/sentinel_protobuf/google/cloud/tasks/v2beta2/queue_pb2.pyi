from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.tasks.v2beta2 import target_pb2 as _target_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Queue(_message.Message):
    __slots__ = ("name", "app_engine_http_target", "pull_target", "http_target", "rate_limits", "retry_config", "state", "purge_time", "task_ttl", "tombstone_ttl", "stats")
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
    APP_ENGINE_HTTP_TARGET_FIELD_NUMBER: _ClassVar[int]
    PULL_TARGET_FIELD_NUMBER: _ClassVar[int]
    HTTP_TARGET_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    RETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PURGE_TIME_FIELD_NUMBER: _ClassVar[int]
    TASK_TTL_FIELD_NUMBER: _ClassVar[int]
    TOMBSTONE_TTL_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    name: str
    app_engine_http_target: _target_pb2.AppEngineHttpTarget
    pull_target: _target_pb2.PullTarget
    http_target: _target_pb2.HttpTarget
    rate_limits: RateLimits
    retry_config: RetryConfig
    state: Queue.State
    purge_time: _timestamp_pb2.Timestamp
    task_ttl: _duration_pb2.Duration
    tombstone_ttl: _duration_pb2.Duration
    stats: QueueStats
    def __init__(self, name: _Optional[str] = ..., app_engine_http_target: _Optional[_Union[_target_pb2.AppEngineHttpTarget, _Mapping]] = ..., pull_target: _Optional[_Union[_target_pb2.PullTarget, _Mapping]] = ..., http_target: _Optional[_Union[_target_pb2.HttpTarget, _Mapping]] = ..., rate_limits: _Optional[_Union[RateLimits, _Mapping]] = ..., retry_config: _Optional[_Union[RetryConfig, _Mapping]] = ..., state: _Optional[_Union[Queue.State, str]] = ..., purge_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., task_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., tombstone_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., stats: _Optional[_Union[QueueStats, _Mapping]] = ...) -> None: ...

class RateLimits(_message.Message):
    __slots__ = ("max_tasks_dispatched_per_second", "max_burst_size", "max_concurrent_tasks")
    MAX_TASKS_DISPATCHED_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    MAX_BURST_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_TASKS_FIELD_NUMBER: _ClassVar[int]
    max_tasks_dispatched_per_second: float
    max_burst_size: int
    max_concurrent_tasks: int
    def __init__(self, max_tasks_dispatched_per_second: _Optional[float] = ..., max_burst_size: _Optional[int] = ..., max_concurrent_tasks: _Optional[int] = ...) -> None: ...

class RetryConfig(_message.Message):
    __slots__ = ("max_attempts", "unlimited_attempts", "max_retry_duration", "min_backoff", "max_backoff", "max_doublings")
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    UNLIMITED_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_DURATION_FIELD_NUMBER: _ClassVar[int]
    MIN_BACKOFF_FIELD_NUMBER: _ClassVar[int]
    MAX_BACKOFF_FIELD_NUMBER: _ClassVar[int]
    MAX_DOUBLINGS_FIELD_NUMBER: _ClassVar[int]
    max_attempts: int
    unlimited_attempts: bool
    max_retry_duration: _duration_pb2.Duration
    min_backoff: _duration_pb2.Duration
    max_backoff: _duration_pb2.Duration
    max_doublings: int
    def __init__(self, max_attempts: _Optional[int] = ..., unlimited_attempts: bool = ..., max_retry_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., min_backoff: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_backoff: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_doublings: _Optional[int] = ...) -> None: ...

class QueueStats(_message.Message):
    __slots__ = ("tasks_count", "oldest_estimated_arrival_time", "executed_last_minute_count", "concurrent_dispatches_count", "effective_execution_rate")
    TASKS_COUNT_FIELD_NUMBER: _ClassVar[int]
    OLDEST_ESTIMATED_ARRIVAL_TIME_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_LAST_MINUTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_DISPATCHES_COUNT_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_EXECUTION_RATE_FIELD_NUMBER: _ClassVar[int]
    tasks_count: int
    oldest_estimated_arrival_time: _timestamp_pb2.Timestamp
    executed_last_minute_count: int
    concurrent_dispatches_count: int
    effective_execution_rate: float
    def __init__(self, tasks_count: _Optional[int] = ..., oldest_estimated_arrival_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., executed_last_minute_count: _Optional[int] = ..., concurrent_dispatches_count: _Optional[int] = ..., effective_execution_rate: _Optional[float] = ...) -> None: ...
