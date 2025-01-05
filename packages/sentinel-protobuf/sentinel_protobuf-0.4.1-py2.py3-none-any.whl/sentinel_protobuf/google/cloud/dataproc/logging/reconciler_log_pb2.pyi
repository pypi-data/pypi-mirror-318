from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReconciliationDecisionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECONCILIATION_DECISION_TYPE_UNSPECIFIED: _ClassVar[ReconciliationDecisionType]
    RECONCILIATION_TERMINATE_SESSION: _ClassVar[ReconciliationDecisionType]
RECONCILIATION_DECISION_TYPE_UNSPECIFIED: ReconciliationDecisionType
RECONCILIATION_TERMINATE_SESSION: ReconciliationDecisionType

class ReconciliationLog(_message.Message):
    __slots__ = ('inputs', 'outputs')

    class Inputs(_message.Message):
        __slots__ = ('idle_duration', 'idle_ttl', 'session_lifetime', 'ttl')
        IDLE_DURATION_FIELD_NUMBER: _ClassVar[int]
        IDLE_TTL_FIELD_NUMBER: _ClassVar[int]
        SESSION_LIFETIME_FIELD_NUMBER: _ClassVar[int]
        TTL_FIELD_NUMBER: _ClassVar[int]
        idle_duration: _duration_pb2.Duration
        idle_ttl: _duration_pb2.Duration
        session_lifetime: _duration_pb2.Duration
        ttl: _duration_pb2.Duration

        def __init__(self, idle_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., idle_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., session_lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class Outputs(_message.Message):
        __slots__ = ('decision', 'decision_details')
        DECISION_FIELD_NUMBER: _ClassVar[int]
        DECISION_DETAILS_FIELD_NUMBER: _ClassVar[int]
        decision: ReconciliationDecisionType
        decision_details: str

        def __init__(self, decision: _Optional[_Union[ReconciliationDecisionType, str]]=..., decision_details: _Optional[str]=...) -> None:
            ...
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: ReconciliationLog.Inputs
    outputs: ReconciliationLog.Outputs

    def __init__(self, inputs: _Optional[_Union[ReconciliationLog.Inputs, _Mapping]]=..., outputs: _Optional[_Union[ReconciliationLog.Outputs, _Mapping]]=...) -> None:
        ...

class ReconciliationClusterHealLog(_message.Message):
    __slots__ = ('outputs',)

    class Outputs(_message.Message):
        __slots__ = ('repair_operation_id', 'decision_details')
        REPAIR_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
        DECISION_DETAILS_FIELD_NUMBER: _ClassVar[int]
        repair_operation_id: str
        decision_details: str

        def __init__(self, repair_operation_id: _Optional[str]=..., decision_details: _Optional[str]=...) -> None:
            ...
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    outputs: ReconciliationClusterHealLog.Outputs

    def __init__(self, outputs: _Optional[_Union[ReconciliationClusterHealLog.Outputs, _Mapping]]=...) -> None:
        ...