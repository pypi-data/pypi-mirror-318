from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.osconfig.v1alpha import config_common_pb2 as _config_common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InstanceOSPoliciesCompliance(_message.Message):
    __slots__ = ('name', 'instance', 'state', 'detailed_state', 'detailed_state_reason', 'os_policy_compliances', 'last_compliance_check_time', 'last_compliance_run_id')

    class OSPolicyCompliance(_message.Message):
        __slots__ = ('os_policy_id', 'os_policy_assignment', 'state', 'os_policy_resource_compliances')
        OS_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
        OS_POLICY_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        OS_POLICY_RESOURCE_COMPLIANCES_FIELD_NUMBER: _ClassVar[int]
        os_policy_id: str
        os_policy_assignment: str
        state: _config_common_pb2.OSPolicyComplianceState
        os_policy_resource_compliances: _containers.RepeatedCompositeFieldContainer[_config_common_pb2.OSPolicyResourceCompliance]

        def __init__(self, os_policy_id: _Optional[str]=..., os_policy_assignment: _Optional[str]=..., state: _Optional[_Union[_config_common_pb2.OSPolicyComplianceState, str]]=..., os_policy_resource_compliances: _Optional[_Iterable[_Union[_config_common_pb2.OSPolicyResourceCompliance, _Mapping]]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAILED_STATE_FIELD_NUMBER: _ClassVar[int]
    DETAILED_STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    OS_POLICY_COMPLIANCES_FIELD_NUMBER: _ClassVar[int]
    LAST_COMPLIANCE_CHECK_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_COMPLIANCE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    instance: str
    state: _config_common_pb2.OSPolicyComplianceState
    detailed_state: str
    detailed_state_reason: str
    os_policy_compliances: _containers.RepeatedCompositeFieldContainer[InstanceOSPoliciesCompliance.OSPolicyCompliance]
    last_compliance_check_time: _timestamp_pb2.Timestamp
    last_compliance_run_id: str

    def __init__(self, name: _Optional[str]=..., instance: _Optional[str]=..., state: _Optional[_Union[_config_common_pb2.OSPolicyComplianceState, str]]=..., detailed_state: _Optional[str]=..., detailed_state_reason: _Optional[str]=..., os_policy_compliances: _Optional[_Iterable[_Union[InstanceOSPoliciesCompliance.OSPolicyCompliance, _Mapping]]]=..., last_compliance_check_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_compliance_run_id: _Optional[str]=...) -> None:
        ...

class GetInstanceOSPoliciesComplianceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListInstanceOSPoliciesCompliancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListInstanceOSPoliciesCompliancesResponse(_message.Message):
    __slots__ = ('instance_os_policies_compliances', 'next_page_token')
    INSTANCE_OS_POLICIES_COMPLIANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    instance_os_policies_compliances: _containers.RepeatedCompositeFieldContainer[InstanceOSPoliciesCompliance]
    next_page_token: str

    def __init__(self, instance_os_policies_compliances: _Optional[_Iterable[_Union[InstanceOSPoliciesCompliance, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...