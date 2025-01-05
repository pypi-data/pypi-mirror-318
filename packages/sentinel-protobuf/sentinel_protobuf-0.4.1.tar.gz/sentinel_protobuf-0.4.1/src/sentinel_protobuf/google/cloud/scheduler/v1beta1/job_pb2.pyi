from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.scheduler.v1beta1 import target_pb2 as _target_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ('name', 'description', 'pubsub_target', 'app_engine_http_target', 'http_target', 'schedule', 'time_zone', 'user_update_time', 'state', 'status', 'schedule_time', 'last_attempt_time', 'retry_config', 'attempt_deadline', 'legacy_app_engine_cron')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Job.State]
        ENABLED: _ClassVar[Job.State]
        PAUSED: _ClassVar[Job.State]
        DISABLED: _ClassVar[Job.State]
        UPDATE_FAILED: _ClassVar[Job.State]
    STATE_UNSPECIFIED: Job.State
    ENABLED: Job.State
    PAUSED: Job.State
    DISABLED: Job.State
    UPDATE_FAILED: Job.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_TARGET_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_HTTP_TARGET_FIELD_NUMBER: _ClassVar[int]
    HTTP_TARGET_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    USER_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_ATTEMPT_TIME_FIELD_NUMBER: _ClassVar[int]
    RETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    LEGACY_APP_ENGINE_CRON_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    pubsub_target: _target_pb2.PubsubTarget
    app_engine_http_target: _target_pb2.AppEngineHttpTarget
    http_target: _target_pb2.HttpTarget
    schedule: str
    time_zone: str
    user_update_time: _timestamp_pb2.Timestamp
    state: Job.State
    status: _status_pb2.Status
    schedule_time: _timestamp_pb2.Timestamp
    last_attempt_time: _timestamp_pb2.Timestamp
    retry_config: RetryConfig
    attempt_deadline: _duration_pb2.Duration
    legacy_app_engine_cron: bool

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., pubsub_target: _Optional[_Union[_target_pb2.PubsubTarget, _Mapping]]=..., app_engine_http_target: _Optional[_Union[_target_pb2.AppEngineHttpTarget, _Mapping]]=..., http_target: _Optional[_Union[_target_pb2.HttpTarget, _Mapping]]=..., schedule: _Optional[str]=..., time_zone: _Optional[str]=..., user_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Job.State, str]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_attempt_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., retry_config: _Optional[_Union[RetryConfig, _Mapping]]=..., attempt_deadline: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., legacy_app_engine_cron: bool=...) -> None:
        ...

class RetryConfig(_message.Message):
    __slots__ = ('retry_count', 'max_retry_duration', 'min_backoff_duration', 'max_backoff_duration', 'max_doublings')
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_DURATION_FIELD_NUMBER: _ClassVar[int]
    MIN_BACKOFF_DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_BACKOFF_DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_DOUBLINGS_FIELD_NUMBER: _ClassVar[int]
    retry_count: int
    max_retry_duration: _duration_pb2.Duration
    min_backoff_duration: _duration_pb2.Duration
    max_backoff_duration: _duration_pb2.Duration
    max_doublings: int

    def __init__(self, retry_count: _Optional[int]=..., max_retry_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., min_backoff_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_backoff_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_doublings: _Optional[int]=...) -> None:
        ...