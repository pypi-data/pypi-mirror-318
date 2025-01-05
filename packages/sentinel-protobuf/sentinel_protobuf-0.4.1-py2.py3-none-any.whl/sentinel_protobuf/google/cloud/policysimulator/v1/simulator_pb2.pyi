from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.policysimulator.v1 import explanations_pb2 as _explanations_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Replay(_message.Message):
    __slots__ = ('name', 'state', 'config', 'results_summary')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Replay.State]
        PENDING: _ClassVar[Replay.State]
        RUNNING: _ClassVar[Replay.State]
        SUCCEEDED: _ClassVar[Replay.State]
        FAILED: _ClassVar[Replay.State]
    STATE_UNSPECIFIED: Replay.State
    PENDING: Replay.State
    RUNNING: Replay.State
    SUCCEEDED: Replay.State
    FAILED: Replay.State

    class ResultsSummary(_message.Message):
        __slots__ = ('log_count', 'unchanged_count', 'difference_count', 'error_count', 'oldest_date', 'newest_date')
        LOG_COUNT_FIELD_NUMBER: _ClassVar[int]
        UNCHANGED_COUNT_FIELD_NUMBER: _ClassVar[int]
        DIFFERENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        OLDEST_DATE_FIELD_NUMBER: _ClassVar[int]
        NEWEST_DATE_FIELD_NUMBER: _ClassVar[int]
        log_count: int
        unchanged_count: int
        difference_count: int
        error_count: int
        oldest_date: _date_pb2.Date
        newest_date: _date_pb2.Date

        def __init__(self, log_count: _Optional[int]=..., unchanged_count: _Optional[int]=..., difference_count: _Optional[int]=..., error_count: _Optional[int]=..., oldest_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., newest_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESULTS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Replay.State
    config: ReplayConfig
    results_summary: Replay.ResultsSummary

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[Replay.State, str]]=..., config: _Optional[_Union[ReplayConfig, _Mapping]]=..., results_summary: _Optional[_Union[Replay.ResultsSummary, _Mapping]]=...) -> None:
        ...

class ReplayResult(_message.Message):
    __slots__ = ('diff', 'error', 'name', 'parent', 'access_tuple', 'last_seen_date')
    DIFF_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TUPLE_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_DATE_FIELD_NUMBER: _ClassVar[int]
    diff: ReplayDiff
    error: _status_pb2.Status
    name: str
    parent: str
    access_tuple: _explanations_pb2.AccessTuple
    last_seen_date: _date_pb2.Date

    def __init__(self, diff: _Optional[_Union[ReplayDiff, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., name: _Optional[str]=..., parent: _Optional[str]=..., access_tuple: _Optional[_Union[_explanations_pb2.AccessTuple, _Mapping]]=..., last_seen_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class CreateReplayRequest(_message.Message):
    __slots__ = ('parent', 'replay')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPLAY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    replay: Replay

    def __init__(self, parent: _Optional[str]=..., replay: _Optional[_Union[Replay, _Mapping]]=...) -> None:
        ...

class ReplayOperationMetadata(_message.Message):
    __slots__ = ('start_time',)
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetReplayRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListReplayResultsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListReplayResultsResponse(_message.Message):
    __slots__ = ('replay_results', 'next_page_token')
    REPLAY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    replay_results: _containers.RepeatedCompositeFieldContainer[ReplayResult]
    next_page_token: str

    def __init__(self, replay_results: _Optional[_Iterable[_Union[ReplayResult, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ReplayConfig(_message.Message):
    __slots__ = ('policy_overlay', 'log_source')

    class LogSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOG_SOURCE_UNSPECIFIED: _ClassVar[ReplayConfig.LogSource]
        RECENT_ACCESSES: _ClassVar[ReplayConfig.LogSource]
    LOG_SOURCE_UNSPECIFIED: ReplayConfig.LogSource
    RECENT_ACCESSES: ReplayConfig.LogSource

    class PolicyOverlayEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _policy_pb2.Policy

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_policy_pb2.Policy, _Mapping]]=...) -> None:
            ...
    POLICY_OVERLAY_FIELD_NUMBER: _ClassVar[int]
    LOG_SOURCE_FIELD_NUMBER: _ClassVar[int]
    policy_overlay: _containers.MessageMap[str, _policy_pb2.Policy]
    log_source: ReplayConfig.LogSource

    def __init__(self, policy_overlay: _Optional[_Mapping[str, _policy_pb2.Policy]]=..., log_source: _Optional[_Union[ReplayConfig.LogSource, str]]=...) -> None:
        ...

class ReplayDiff(_message.Message):
    __slots__ = ('access_diff',)
    ACCESS_DIFF_FIELD_NUMBER: _ClassVar[int]
    access_diff: AccessStateDiff

    def __init__(self, access_diff: _Optional[_Union[AccessStateDiff, _Mapping]]=...) -> None:
        ...

class AccessStateDiff(_message.Message):
    __slots__ = ('baseline', 'simulated', 'access_change')

    class AccessChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCESS_CHANGE_TYPE_UNSPECIFIED: _ClassVar[AccessStateDiff.AccessChangeType]
        NO_CHANGE: _ClassVar[AccessStateDiff.AccessChangeType]
        UNKNOWN_CHANGE: _ClassVar[AccessStateDiff.AccessChangeType]
        ACCESS_REVOKED: _ClassVar[AccessStateDiff.AccessChangeType]
        ACCESS_GAINED: _ClassVar[AccessStateDiff.AccessChangeType]
        ACCESS_MAYBE_REVOKED: _ClassVar[AccessStateDiff.AccessChangeType]
        ACCESS_MAYBE_GAINED: _ClassVar[AccessStateDiff.AccessChangeType]
    ACCESS_CHANGE_TYPE_UNSPECIFIED: AccessStateDiff.AccessChangeType
    NO_CHANGE: AccessStateDiff.AccessChangeType
    UNKNOWN_CHANGE: AccessStateDiff.AccessChangeType
    ACCESS_REVOKED: AccessStateDiff.AccessChangeType
    ACCESS_GAINED: AccessStateDiff.AccessChangeType
    ACCESS_MAYBE_REVOKED: AccessStateDiff.AccessChangeType
    ACCESS_MAYBE_GAINED: AccessStateDiff.AccessChangeType
    BASELINE_FIELD_NUMBER: _ClassVar[int]
    SIMULATED_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    baseline: ExplainedAccess
    simulated: ExplainedAccess
    access_change: AccessStateDiff.AccessChangeType

    def __init__(self, baseline: _Optional[_Union[ExplainedAccess, _Mapping]]=..., simulated: _Optional[_Union[ExplainedAccess, _Mapping]]=..., access_change: _Optional[_Union[AccessStateDiff.AccessChangeType, str]]=...) -> None:
        ...

class ExplainedAccess(_message.Message):
    __slots__ = ('access_state', 'policies', 'errors')
    ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    access_state: _explanations_pb2.AccessState
    policies: _containers.RepeatedCompositeFieldContainer[_explanations_pb2.ExplainedPolicy]
    errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, access_state: _Optional[_Union[_explanations_pb2.AccessState, str]]=..., policies: _Optional[_Iterable[_Union[_explanations_pb2.ExplainedPolicy, _Mapping]]]=..., errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...