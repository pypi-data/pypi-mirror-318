from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.osconfig.v1 import os_policy_pb2 as _os_policy_pb2
from google.cloud.osconfig.v1 import osconfig_common_pb2 as _osconfig_common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OSPolicyAssignment(_message.Message):
    __slots__ = ('name', 'description', 'os_policies', 'instance_filter', 'rollout', 'revision_id', 'revision_create_time', 'etag', 'rollout_state', 'baseline', 'deleted', 'reconciling', 'uid')

    class RolloutState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLLOUT_STATE_UNSPECIFIED: _ClassVar[OSPolicyAssignment.RolloutState]
        IN_PROGRESS: _ClassVar[OSPolicyAssignment.RolloutState]
        CANCELLING: _ClassVar[OSPolicyAssignment.RolloutState]
        CANCELLED: _ClassVar[OSPolicyAssignment.RolloutState]
        SUCCEEDED: _ClassVar[OSPolicyAssignment.RolloutState]
    ROLLOUT_STATE_UNSPECIFIED: OSPolicyAssignment.RolloutState
    IN_PROGRESS: OSPolicyAssignment.RolloutState
    CANCELLING: OSPolicyAssignment.RolloutState
    CANCELLED: OSPolicyAssignment.RolloutState
    SUCCEEDED: OSPolicyAssignment.RolloutState

    class LabelSet(_message.Message):
        __slots__ = ('labels',)

        class LabelsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        LABELS_FIELD_NUMBER: _ClassVar[int]
        labels: _containers.ScalarMap[str, str]

        def __init__(self, labels: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class InstanceFilter(_message.Message):
        __slots__ = ('all', 'inclusion_labels', 'exclusion_labels', 'inventories')

        class Inventory(_message.Message):
            __slots__ = ('os_short_name', 'os_version')
            OS_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
            OS_VERSION_FIELD_NUMBER: _ClassVar[int]
            os_short_name: str
            os_version: str

            def __init__(self, os_short_name: _Optional[str]=..., os_version: _Optional[str]=...) -> None:
                ...
        ALL_FIELD_NUMBER: _ClassVar[int]
        INCLUSION_LABELS_FIELD_NUMBER: _ClassVar[int]
        EXCLUSION_LABELS_FIELD_NUMBER: _ClassVar[int]
        INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        all: bool
        inclusion_labels: _containers.RepeatedCompositeFieldContainer[OSPolicyAssignment.LabelSet]
        exclusion_labels: _containers.RepeatedCompositeFieldContainer[OSPolicyAssignment.LabelSet]
        inventories: _containers.RepeatedCompositeFieldContainer[OSPolicyAssignment.InstanceFilter.Inventory]

        def __init__(self, all: bool=..., inclusion_labels: _Optional[_Iterable[_Union[OSPolicyAssignment.LabelSet, _Mapping]]]=..., exclusion_labels: _Optional[_Iterable[_Union[OSPolicyAssignment.LabelSet, _Mapping]]]=..., inventories: _Optional[_Iterable[_Union[OSPolicyAssignment.InstanceFilter.Inventory, _Mapping]]]=...) -> None:
            ...

    class Rollout(_message.Message):
        __slots__ = ('disruption_budget', 'min_wait_duration')
        DISRUPTION_BUDGET_FIELD_NUMBER: _ClassVar[int]
        MIN_WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
        disruption_budget: _osconfig_common_pb2.FixedOrPercent
        min_wait_duration: _duration_pb2.Duration

        def __init__(self, disruption_budget: _Optional[_Union[_osconfig_common_pb2.FixedOrPercent, _Mapping]]=..., min_wait_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OS_POLICIES_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FILTER_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_STATE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    os_policies: _containers.RepeatedCompositeFieldContainer[_os_policy_pb2.OSPolicy]
    instance_filter: OSPolicyAssignment.InstanceFilter
    rollout: OSPolicyAssignment.Rollout
    revision_id: str
    revision_create_time: _timestamp_pb2.Timestamp
    etag: str
    rollout_state: OSPolicyAssignment.RolloutState
    baseline: bool
    deleted: bool
    reconciling: bool
    uid: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., os_policies: _Optional[_Iterable[_Union[_os_policy_pb2.OSPolicy, _Mapping]]]=..., instance_filter: _Optional[_Union[OSPolicyAssignment.InstanceFilter, _Mapping]]=..., rollout: _Optional[_Union[OSPolicyAssignment.Rollout, _Mapping]]=..., revision_id: _Optional[str]=..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., rollout_state: _Optional[_Union[OSPolicyAssignment.RolloutState, str]]=..., baseline: bool=..., deleted: bool=..., reconciling: bool=..., uid: _Optional[str]=...) -> None:
        ...

class OSPolicyAssignmentOperationMetadata(_message.Message):
    __slots__ = ('os_policy_assignment', 'api_method', 'rollout_state', 'rollout_start_time', 'rollout_update_time')

    class APIMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        API_METHOD_UNSPECIFIED: _ClassVar[OSPolicyAssignmentOperationMetadata.APIMethod]
        CREATE: _ClassVar[OSPolicyAssignmentOperationMetadata.APIMethod]
        UPDATE: _ClassVar[OSPolicyAssignmentOperationMetadata.APIMethod]
        DELETE: _ClassVar[OSPolicyAssignmentOperationMetadata.APIMethod]
    API_METHOD_UNSPECIFIED: OSPolicyAssignmentOperationMetadata.APIMethod
    CREATE: OSPolicyAssignmentOperationMetadata.APIMethod
    UPDATE: OSPolicyAssignmentOperationMetadata.APIMethod
    DELETE: OSPolicyAssignmentOperationMetadata.APIMethod

    class RolloutState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLLOUT_STATE_UNSPECIFIED: _ClassVar[OSPolicyAssignmentOperationMetadata.RolloutState]
        IN_PROGRESS: _ClassVar[OSPolicyAssignmentOperationMetadata.RolloutState]
        CANCELLING: _ClassVar[OSPolicyAssignmentOperationMetadata.RolloutState]
        CANCELLED: _ClassVar[OSPolicyAssignmentOperationMetadata.RolloutState]
        SUCCEEDED: _ClassVar[OSPolicyAssignmentOperationMetadata.RolloutState]
    ROLLOUT_STATE_UNSPECIFIED: OSPolicyAssignmentOperationMetadata.RolloutState
    IN_PROGRESS: OSPolicyAssignmentOperationMetadata.RolloutState
    CANCELLING: OSPolicyAssignmentOperationMetadata.RolloutState
    CANCELLED: OSPolicyAssignmentOperationMetadata.RolloutState
    SUCCEEDED: OSPolicyAssignmentOperationMetadata.RolloutState
    OS_POLICY_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    API_METHOD_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_STATE_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_START_TIME_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    os_policy_assignment: str
    api_method: OSPolicyAssignmentOperationMetadata.APIMethod
    rollout_state: OSPolicyAssignmentOperationMetadata.RolloutState
    rollout_start_time: _timestamp_pb2.Timestamp
    rollout_update_time: _timestamp_pb2.Timestamp

    def __init__(self, os_policy_assignment: _Optional[str]=..., api_method: _Optional[_Union[OSPolicyAssignmentOperationMetadata.APIMethod, str]]=..., rollout_state: _Optional[_Union[OSPolicyAssignmentOperationMetadata.RolloutState, str]]=..., rollout_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., rollout_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateOSPolicyAssignmentRequest(_message.Message):
    __slots__ = ('parent', 'os_policy_assignment', 'os_policy_assignment_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OS_POLICY_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OS_POLICY_ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    os_policy_assignment: OSPolicyAssignment
    os_policy_assignment_id: str

    def __init__(self, parent: _Optional[str]=..., os_policy_assignment: _Optional[_Union[OSPolicyAssignment, _Mapping]]=..., os_policy_assignment_id: _Optional[str]=...) -> None:
        ...

class UpdateOSPolicyAssignmentRequest(_message.Message):
    __slots__ = ('os_policy_assignment', 'update_mask')
    OS_POLICY_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    os_policy_assignment: OSPolicyAssignment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, os_policy_assignment: _Optional[_Union[OSPolicyAssignment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetOSPolicyAssignmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListOSPolicyAssignmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOSPolicyAssignmentsResponse(_message.Message):
    __slots__ = ('os_policy_assignments', 'next_page_token')
    OS_POLICY_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    os_policy_assignments: _containers.RepeatedCompositeFieldContainer[OSPolicyAssignment]
    next_page_token: str

    def __init__(self, os_policy_assignments: _Optional[_Iterable[_Union[OSPolicyAssignment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListOSPolicyAssignmentRevisionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOSPolicyAssignmentRevisionsResponse(_message.Message):
    __slots__ = ('os_policy_assignments', 'next_page_token')
    OS_POLICY_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    os_policy_assignments: _containers.RepeatedCompositeFieldContainer[OSPolicyAssignment]
    next_page_token: str

    def __init__(self, os_policy_assignments: _Optional[_Iterable[_Union[OSPolicyAssignment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteOSPolicyAssignmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...