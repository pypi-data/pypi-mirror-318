from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetOSPolicyAssignmentReportRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListOSPolicyAssignmentReportsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'filter', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    filter: str
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., filter: _Optional[str]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOSPolicyAssignmentReportsResponse(_message.Message):
    __slots__ = ('os_policy_assignment_reports', 'next_page_token')
    OS_POLICY_ASSIGNMENT_REPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    os_policy_assignment_reports: _containers.RepeatedCompositeFieldContainer[OSPolicyAssignmentReport]
    next_page_token: str

    def __init__(self, os_policy_assignment_reports: _Optional[_Iterable[_Union[OSPolicyAssignmentReport, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class OSPolicyAssignmentReport(_message.Message):
    __slots__ = ('name', 'instance', 'os_policy_assignment', 'os_policy_compliances', 'update_time', 'last_run_id')

    class OSPolicyCompliance(_message.Message):
        __slots__ = ('os_policy_id', 'compliance_state', 'compliance_state_reason', 'os_policy_resource_compliances')

        class ComplianceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.ComplianceState]
            COMPLIANT: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.ComplianceState]
            NON_COMPLIANT: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.ComplianceState]
        UNKNOWN: OSPolicyAssignmentReport.OSPolicyCompliance.ComplianceState
        COMPLIANT: OSPolicyAssignmentReport.OSPolicyCompliance.ComplianceState
        NON_COMPLIANT: OSPolicyAssignmentReport.OSPolicyCompliance.ComplianceState

        class OSPolicyResourceCompliance(_message.Message):
            __slots__ = ('os_policy_resource_id', 'config_steps', 'compliance_state', 'compliance_state_reason', 'exec_resource_output')

            class ComplianceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ComplianceState]
                COMPLIANT: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ComplianceState]
                NON_COMPLIANT: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ComplianceState]
            UNKNOWN: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ComplianceState
            COMPLIANT: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ComplianceState
            NON_COMPLIANT: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ComplianceState

            class OSPolicyResourceConfigStep(_message.Message):
                __slots__ = ('type', 'error_message')

                class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    TYPE_UNSPECIFIED: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type]
                    VALIDATION: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type]
                    DESIRED_STATE_CHECK: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type]
                    DESIRED_STATE_ENFORCEMENT: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type]
                    DESIRED_STATE_CHECK_POST_ENFORCEMENT: _ClassVar[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type]
                TYPE_UNSPECIFIED: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type
                VALIDATION: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type
                DESIRED_STATE_CHECK: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type
                DESIRED_STATE_ENFORCEMENT: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type
                DESIRED_STATE_CHECK_POST_ENFORCEMENT: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type
                TYPE_FIELD_NUMBER: _ClassVar[int]
                ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
                type: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type
                error_message: str

                def __init__(self, type: _Optional[_Union[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type, str]]=..., error_message: _Optional[str]=...) -> None:
                    ...

            class ExecResourceOutput(_message.Message):
                __slots__ = ('enforcement_output',)
                ENFORCEMENT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
                enforcement_output: bytes

                def __init__(self, enforcement_output: _Optional[bytes]=...) -> None:
                    ...
            OS_POLICY_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
            CONFIG_STEPS_FIELD_NUMBER: _ClassVar[int]
            COMPLIANCE_STATE_FIELD_NUMBER: _ClassVar[int]
            COMPLIANCE_STATE_REASON_FIELD_NUMBER: _ClassVar[int]
            EXEC_RESOURCE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
            os_policy_resource_id: str
            config_steps: _containers.RepeatedCompositeFieldContainer[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep]
            compliance_state: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ComplianceState
            compliance_state_reason: str
            exec_resource_output: OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ExecResourceOutput

            def __init__(self, os_policy_resource_id: _Optional[str]=..., config_steps: _Optional[_Iterable[_Union[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep, _Mapping]]]=..., compliance_state: _Optional[_Union[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ComplianceState, str]]=..., compliance_state_reason: _Optional[str]=..., exec_resource_output: _Optional[_Union[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ExecResourceOutput, _Mapping]]=...) -> None:
                ...
        OS_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
        COMPLIANCE_STATE_FIELD_NUMBER: _ClassVar[int]
        COMPLIANCE_STATE_REASON_FIELD_NUMBER: _ClassVar[int]
        OS_POLICY_RESOURCE_COMPLIANCES_FIELD_NUMBER: _ClassVar[int]
        os_policy_id: str
        compliance_state: OSPolicyAssignmentReport.OSPolicyCompliance.ComplianceState
        compliance_state_reason: str
        os_policy_resource_compliances: _containers.RepeatedCompositeFieldContainer[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance]

        def __init__(self, os_policy_id: _Optional[str]=..., compliance_state: _Optional[_Union[OSPolicyAssignmentReport.OSPolicyCompliance.ComplianceState, str]]=..., compliance_state_reason: _Optional[str]=..., os_policy_resource_compliances: _Optional[_Iterable[_Union[OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance, _Mapping]]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    OS_POLICY_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OS_POLICY_COMPLIANCES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    instance: str
    os_policy_assignment: str
    os_policy_compliances: _containers.RepeatedCompositeFieldContainer[OSPolicyAssignmentReport.OSPolicyCompliance]
    update_time: _timestamp_pb2.Timestamp
    last_run_id: str

    def __init__(self, name: _Optional[str]=..., instance: _Optional[str]=..., os_policy_assignment: _Optional[str]=..., os_policy_compliances: _Optional[_Iterable[_Union[OSPolicyAssignmentReport.OSPolicyCompliance, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_run_id: _Optional[str]=...) -> None:
        ...