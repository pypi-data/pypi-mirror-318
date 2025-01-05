from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OSPolicyComplianceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED: _ClassVar[OSPolicyComplianceState]
    COMPLIANT: _ClassVar[OSPolicyComplianceState]
    NON_COMPLIANT: _ClassVar[OSPolicyComplianceState]
    UNKNOWN: _ClassVar[OSPolicyComplianceState]
    NO_OS_POLICIES_APPLICABLE: _ClassVar[OSPolicyComplianceState]
OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED: OSPolicyComplianceState
COMPLIANT: OSPolicyComplianceState
NON_COMPLIANT: OSPolicyComplianceState
UNKNOWN: OSPolicyComplianceState
NO_OS_POLICIES_APPLICABLE: OSPolicyComplianceState

class OSPolicyResourceConfigStep(_message.Message):
    __slots__ = ('type', 'outcome', 'error_message')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[OSPolicyResourceConfigStep.Type]
        VALIDATION: _ClassVar[OSPolicyResourceConfigStep.Type]
        DESIRED_STATE_CHECK: _ClassVar[OSPolicyResourceConfigStep.Type]
        DESIRED_STATE_ENFORCEMENT: _ClassVar[OSPolicyResourceConfigStep.Type]
        DESIRED_STATE_CHECK_POST_ENFORCEMENT: _ClassVar[OSPolicyResourceConfigStep.Type]
    TYPE_UNSPECIFIED: OSPolicyResourceConfigStep.Type
    VALIDATION: OSPolicyResourceConfigStep.Type
    DESIRED_STATE_CHECK: OSPolicyResourceConfigStep.Type
    DESIRED_STATE_ENFORCEMENT: OSPolicyResourceConfigStep.Type
    DESIRED_STATE_CHECK_POST_ENFORCEMENT: OSPolicyResourceConfigStep.Type

    class Outcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTCOME_UNSPECIFIED: _ClassVar[OSPolicyResourceConfigStep.Outcome]
        SUCCEEDED: _ClassVar[OSPolicyResourceConfigStep.Outcome]
        FAILED: _ClassVar[OSPolicyResourceConfigStep.Outcome]
    OUTCOME_UNSPECIFIED: OSPolicyResourceConfigStep.Outcome
    SUCCEEDED: OSPolicyResourceConfigStep.Outcome
    FAILED: OSPolicyResourceConfigStep.Outcome
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    type: OSPolicyResourceConfigStep.Type
    outcome: OSPolicyResourceConfigStep.Outcome
    error_message: str

    def __init__(self, type: _Optional[_Union[OSPolicyResourceConfigStep.Type, str]]=..., outcome: _Optional[_Union[OSPolicyResourceConfigStep.Outcome, str]]=..., error_message: _Optional[str]=...) -> None:
        ...

class OSPolicyResourceCompliance(_message.Message):
    __slots__ = ('os_policy_resource_id', 'config_steps', 'state', 'exec_resource_output')

    class ExecResourceOutput(_message.Message):
        __slots__ = ('enforcement_output',)
        ENFORCEMENT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
        enforcement_output: bytes

        def __init__(self, enforcement_output: _Optional[bytes]=...) -> None:
            ...
    OS_POLICY_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_STEPS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXEC_RESOURCE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    os_policy_resource_id: str
    config_steps: _containers.RepeatedCompositeFieldContainer[OSPolicyResourceConfigStep]
    state: OSPolicyComplianceState
    exec_resource_output: OSPolicyResourceCompliance.ExecResourceOutput

    def __init__(self, os_policy_resource_id: _Optional[str]=..., config_steps: _Optional[_Iterable[_Union[OSPolicyResourceConfigStep, _Mapping]]]=..., state: _Optional[_Union[OSPolicyComplianceState, str]]=..., exec_resource_output: _Optional[_Union[OSPolicyResourceCompliance.ExecResourceOutput, _Mapping]]=...) -> None:
        ...