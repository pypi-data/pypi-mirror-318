from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.cloudcontrolspartner.v1 import completion_state_pb2 as _completion_state_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Workload(_message.Message):
    __slots__ = ('name', 'folder_id', 'create_time', 'folder', 'workload_onboarding_state', 'is_onboarded', 'key_management_project_id', 'location', 'partner')

    class Partner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTNER_UNSPECIFIED: _ClassVar[Workload.Partner]
        PARTNER_LOCAL_CONTROLS_BY_S3NS: _ClassVar[Workload.Partner]
        PARTNER_SOVEREIGN_CONTROLS_BY_T_SYSTEMS: _ClassVar[Workload.Partner]
        PARTNER_SOVEREIGN_CONTROLS_BY_SIA_MINSAIT: _ClassVar[Workload.Partner]
        PARTNER_SOVEREIGN_CONTROLS_BY_PSN: _ClassVar[Workload.Partner]
        PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT: _ClassVar[Workload.Partner]
        PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM: _ClassVar[Workload.Partner]
    PARTNER_UNSPECIFIED: Workload.Partner
    PARTNER_LOCAL_CONTROLS_BY_S3NS: Workload.Partner
    PARTNER_SOVEREIGN_CONTROLS_BY_T_SYSTEMS: Workload.Partner
    PARTNER_SOVEREIGN_CONTROLS_BY_SIA_MINSAIT: Workload.Partner
    PARTNER_SOVEREIGN_CONTROLS_BY_PSN: Workload.Partner
    PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT: Workload.Partner
    PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM: Workload.Partner
    NAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_ONBOARDING_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_ONBOARDED_FIELD_NUMBER: _ClassVar[int]
    KEY_MANAGEMENT_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PARTNER_FIELD_NUMBER: _ClassVar[int]
    name: str
    folder_id: int
    create_time: _timestamp_pb2.Timestamp
    folder: str
    workload_onboarding_state: WorkloadOnboardingState
    is_onboarded: bool
    key_management_project_id: str
    location: str
    partner: Workload.Partner

    def __init__(self, name: _Optional[str]=..., folder_id: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., folder: _Optional[str]=..., workload_onboarding_state: _Optional[_Union[WorkloadOnboardingState, _Mapping]]=..., is_onboarded: bool=..., key_management_project_id: _Optional[str]=..., location: _Optional[str]=..., partner: _Optional[_Union[Workload.Partner, str]]=...) -> None:
        ...

class ListWorkloadsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListWorkloadsResponse(_message.Message):
    __slots__ = ('workloads', 'next_page_token', 'unreachable')
    WORKLOADS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workloads: _containers.RepeatedCompositeFieldContainer[Workload]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workloads: _Optional[_Iterable[_Union[Workload, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetWorkloadRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class WorkloadOnboardingState(_message.Message):
    __slots__ = ('onboarding_steps',)
    ONBOARDING_STEPS_FIELD_NUMBER: _ClassVar[int]
    onboarding_steps: _containers.RepeatedCompositeFieldContainer[WorkloadOnboardingStep]

    def __init__(self, onboarding_steps: _Optional[_Iterable[_Union[WorkloadOnboardingStep, _Mapping]]]=...) -> None:
        ...

class WorkloadOnboardingStep(_message.Message):
    __slots__ = ('step', 'start_time', 'completion_time', 'completion_state')

    class Step(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STEP_UNSPECIFIED: _ClassVar[WorkloadOnboardingStep.Step]
        EKM_PROVISIONED: _ClassVar[WorkloadOnboardingStep.Step]
        SIGNED_ACCESS_APPROVAL_CONFIGURED: _ClassVar[WorkloadOnboardingStep.Step]
    STEP_UNSPECIFIED: WorkloadOnboardingStep.Step
    EKM_PROVISIONED: WorkloadOnboardingStep.Step
    SIGNED_ACCESS_APPROVAL_CONFIGURED: WorkloadOnboardingStep.Step
    STEP_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_STATE_FIELD_NUMBER: _ClassVar[int]
    step: WorkloadOnboardingStep.Step
    start_time: _timestamp_pb2.Timestamp
    completion_time: _timestamp_pb2.Timestamp
    completion_state: _completion_state_pb2.CompletionState

    def __init__(self, step: _Optional[_Union[WorkloadOnboardingStep.Step, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., completion_state: _Optional[_Union[_completion_state_pb2.CompletionState, str]]=...) -> None:
        ...