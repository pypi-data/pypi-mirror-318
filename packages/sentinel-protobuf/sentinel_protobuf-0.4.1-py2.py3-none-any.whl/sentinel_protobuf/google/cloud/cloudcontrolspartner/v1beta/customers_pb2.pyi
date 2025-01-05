from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.cloudcontrolspartner.v1beta import completion_state_pb2 as _completion_state_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Customer(_message.Message):
    __slots__ = ('name', 'display_name', 'customer_onboarding_state', 'is_onboarded')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ONBOARDING_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_ONBOARDED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    customer_onboarding_state: CustomerOnboardingState
    is_onboarded: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., customer_onboarding_state: _Optional[_Union[CustomerOnboardingState, _Mapping]]=..., is_onboarded: bool=...) -> None:
        ...

class ListCustomersRequest(_message.Message):
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

class ListCustomersResponse(_message.Message):
    __slots__ = ('customers', 'next_page_token', 'unreachable')
    CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    customers: _containers.RepeatedCompositeFieldContainer[Customer]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, customers: _Optional[_Iterable[_Union[Customer, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCustomerRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CustomerOnboardingState(_message.Message):
    __slots__ = ('onboarding_steps',)
    ONBOARDING_STEPS_FIELD_NUMBER: _ClassVar[int]
    onboarding_steps: _containers.RepeatedCompositeFieldContainer[CustomerOnboardingStep]

    def __init__(self, onboarding_steps: _Optional[_Iterable[_Union[CustomerOnboardingStep, _Mapping]]]=...) -> None:
        ...

class CustomerOnboardingStep(_message.Message):
    __slots__ = ('step', 'start_time', 'completion_time', 'completion_state')

    class Step(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STEP_UNSPECIFIED: _ClassVar[CustomerOnboardingStep.Step]
        KAJ_ENROLLMENT: _ClassVar[CustomerOnboardingStep.Step]
        CUSTOMER_ENVIRONMENT: _ClassVar[CustomerOnboardingStep.Step]
    STEP_UNSPECIFIED: CustomerOnboardingStep.Step
    KAJ_ENROLLMENT: CustomerOnboardingStep.Step
    CUSTOMER_ENVIRONMENT: CustomerOnboardingStep.Step
    STEP_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_STATE_FIELD_NUMBER: _ClassVar[int]
    step: CustomerOnboardingStep.Step
    start_time: _timestamp_pb2.Timestamp
    completion_time: _timestamp_pb2.Timestamp
    completion_state: _completion_state_pb2.CompletionState

    def __init__(self, step: _Optional[_Union[CustomerOnboardingStep.Step, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., completion_state: _Optional[_Union[_completion_state_pb2.CompletionState, str]]=...) -> None:
        ...