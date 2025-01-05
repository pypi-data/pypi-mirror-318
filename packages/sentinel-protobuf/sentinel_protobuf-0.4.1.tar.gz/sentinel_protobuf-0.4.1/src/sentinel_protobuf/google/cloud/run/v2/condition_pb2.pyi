from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Condition(_message.Message):
    __slots__ = ('type', 'state', 'message', 'last_transition_time', 'severity', 'reason', 'revision_reason', 'execution_reason')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Condition.State]
        CONDITION_PENDING: _ClassVar[Condition.State]
        CONDITION_RECONCILING: _ClassVar[Condition.State]
        CONDITION_FAILED: _ClassVar[Condition.State]
        CONDITION_SUCCEEDED: _ClassVar[Condition.State]
    STATE_UNSPECIFIED: Condition.State
    CONDITION_PENDING: Condition.State
    CONDITION_RECONCILING: Condition.State
    CONDITION_FAILED: Condition.State
    CONDITION_SUCCEEDED: Condition.State

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[Condition.Severity]
        ERROR: _ClassVar[Condition.Severity]
        WARNING: _ClassVar[Condition.Severity]
        INFO: _ClassVar[Condition.Severity]
    SEVERITY_UNSPECIFIED: Condition.Severity
    ERROR: Condition.Severity
    WARNING: Condition.Severity
    INFO: Condition.Severity

    class CommonReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMMON_REASON_UNDEFINED: _ClassVar[Condition.CommonReason]
        UNKNOWN: _ClassVar[Condition.CommonReason]
        REVISION_FAILED: _ClassVar[Condition.CommonReason]
        PROGRESS_DEADLINE_EXCEEDED: _ClassVar[Condition.CommonReason]
        CONTAINER_MISSING: _ClassVar[Condition.CommonReason]
        CONTAINER_PERMISSION_DENIED: _ClassVar[Condition.CommonReason]
        CONTAINER_IMAGE_UNAUTHORIZED: _ClassVar[Condition.CommonReason]
        CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED: _ClassVar[Condition.CommonReason]
        ENCRYPTION_KEY_PERMISSION_DENIED: _ClassVar[Condition.CommonReason]
        ENCRYPTION_KEY_CHECK_FAILED: _ClassVar[Condition.CommonReason]
        SECRETS_ACCESS_CHECK_FAILED: _ClassVar[Condition.CommonReason]
        WAITING_FOR_OPERATION: _ClassVar[Condition.CommonReason]
        IMMEDIATE_RETRY: _ClassVar[Condition.CommonReason]
        POSTPONED_RETRY: _ClassVar[Condition.CommonReason]
        INTERNAL: _ClassVar[Condition.CommonReason]
    COMMON_REASON_UNDEFINED: Condition.CommonReason
    UNKNOWN: Condition.CommonReason
    REVISION_FAILED: Condition.CommonReason
    PROGRESS_DEADLINE_EXCEEDED: Condition.CommonReason
    CONTAINER_MISSING: Condition.CommonReason
    CONTAINER_PERMISSION_DENIED: Condition.CommonReason
    CONTAINER_IMAGE_UNAUTHORIZED: Condition.CommonReason
    CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED: Condition.CommonReason
    ENCRYPTION_KEY_PERMISSION_DENIED: Condition.CommonReason
    ENCRYPTION_KEY_CHECK_FAILED: Condition.CommonReason
    SECRETS_ACCESS_CHECK_FAILED: Condition.CommonReason
    WAITING_FOR_OPERATION: Condition.CommonReason
    IMMEDIATE_RETRY: Condition.CommonReason
    POSTPONED_RETRY: Condition.CommonReason
    INTERNAL: Condition.CommonReason

    class RevisionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REVISION_REASON_UNDEFINED: _ClassVar[Condition.RevisionReason]
        PENDING: _ClassVar[Condition.RevisionReason]
        RESERVE: _ClassVar[Condition.RevisionReason]
        RETIRED: _ClassVar[Condition.RevisionReason]
        RETIRING: _ClassVar[Condition.RevisionReason]
        RECREATING: _ClassVar[Condition.RevisionReason]
        HEALTH_CHECK_CONTAINER_ERROR: _ClassVar[Condition.RevisionReason]
        CUSTOMIZED_PATH_RESPONSE_PENDING: _ClassVar[Condition.RevisionReason]
        MIN_INSTANCES_NOT_PROVISIONED: _ClassVar[Condition.RevisionReason]
        ACTIVE_REVISION_LIMIT_REACHED: _ClassVar[Condition.RevisionReason]
        NO_DEPLOYMENT: _ClassVar[Condition.RevisionReason]
        HEALTH_CHECK_SKIPPED: _ClassVar[Condition.RevisionReason]
        MIN_INSTANCES_WARMING: _ClassVar[Condition.RevisionReason]
    REVISION_REASON_UNDEFINED: Condition.RevisionReason
    PENDING: Condition.RevisionReason
    RESERVE: Condition.RevisionReason
    RETIRED: Condition.RevisionReason
    RETIRING: Condition.RevisionReason
    RECREATING: Condition.RevisionReason
    HEALTH_CHECK_CONTAINER_ERROR: Condition.RevisionReason
    CUSTOMIZED_PATH_RESPONSE_PENDING: Condition.RevisionReason
    MIN_INSTANCES_NOT_PROVISIONED: Condition.RevisionReason
    ACTIVE_REVISION_LIMIT_REACHED: Condition.RevisionReason
    NO_DEPLOYMENT: Condition.RevisionReason
    HEALTH_CHECK_SKIPPED: Condition.RevisionReason
    MIN_INSTANCES_WARMING: Condition.RevisionReason

    class ExecutionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXECUTION_REASON_UNDEFINED: _ClassVar[Condition.ExecutionReason]
        JOB_STATUS_SERVICE_POLLING_ERROR: _ClassVar[Condition.ExecutionReason]
        NON_ZERO_EXIT_CODE: _ClassVar[Condition.ExecutionReason]
        CANCELLED: _ClassVar[Condition.ExecutionReason]
        CANCELLING: _ClassVar[Condition.ExecutionReason]
        DELETED: _ClassVar[Condition.ExecutionReason]
    EXECUTION_REASON_UNDEFINED: Condition.ExecutionReason
    JOB_STATUS_SERVICE_POLLING_ERROR: Condition.ExecutionReason
    NON_ZERO_EXIT_CODE: Condition.ExecutionReason
    CANCELLED: Condition.ExecutionReason
    CANCELLING: Condition.ExecutionReason
    DELETED: Condition.ExecutionReason
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSITION_TIME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REVISION_REASON_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_REASON_FIELD_NUMBER: _ClassVar[int]
    type: str
    state: Condition.State
    message: str
    last_transition_time: _timestamp_pb2.Timestamp
    severity: Condition.Severity
    reason: Condition.CommonReason
    revision_reason: Condition.RevisionReason
    execution_reason: Condition.ExecutionReason

    def __init__(self, type: _Optional[str]=..., state: _Optional[_Union[Condition.State, str]]=..., message: _Optional[str]=..., last_transition_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., severity: _Optional[_Union[Condition.Severity, str]]=..., reason: _Optional[_Union[Condition.CommonReason, str]]=..., revision_reason: _Optional[_Union[Condition.RevisionReason, str]]=..., execution_reason: _Optional[_Union[Condition.ExecutionReason, str]]=...) -> None:
        ...