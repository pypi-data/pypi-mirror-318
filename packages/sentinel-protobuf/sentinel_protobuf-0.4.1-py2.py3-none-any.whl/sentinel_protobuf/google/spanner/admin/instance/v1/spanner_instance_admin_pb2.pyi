from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.spanner.admin.instance.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReplicaInfo(_message.Message):
    __slots__ = ('location', 'type', 'default_leader_location')

    class ReplicaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[ReplicaInfo.ReplicaType]
        READ_WRITE: _ClassVar[ReplicaInfo.ReplicaType]
        READ_ONLY: _ClassVar[ReplicaInfo.ReplicaType]
        WITNESS: _ClassVar[ReplicaInfo.ReplicaType]
    TYPE_UNSPECIFIED: ReplicaInfo.ReplicaType
    READ_WRITE: ReplicaInfo.ReplicaType
    READ_ONLY: ReplicaInfo.ReplicaType
    WITNESS: ReplicaInfo.ReplicaType
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LEADER_LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: str
    type: ReplicaInfo.ReplicaType
    default_leader_location: bool

    def __init__(self, location: _Optional[str]=..., type: _Optional[_Union[ReplicaInfo.ReplicaType, str]]=..., default_leader_location: bool=...) -> None:
        ...

class InstanceConfig(_message.Message):
    __slots__ = ('name', 'display_name', 'config_type', 'replicas', 'optional_replicas', 'base_config', 'labels', 'etag', 'leader_options', 'reconciling', 'state', 'free_instance_availability', 'quorum_type', 'storage_limit_per_processing_unit')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[InstanceConfig.Type]
        GOOGLE_MANAGED: _ClassVar[InstanceConfig.Type]
        USER_MANAGED: _ClassVar[InstanceConfig.Type]
    TYPE_UNSPECIFIED: InstanceConfig.Type
    GOOGLE_MANAGED: InstanceConfig.Type
    USER_MANAGED: InstanceConfig.Type

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[InstanceConfig.State]
        CREATING: _ClassVar[InstanceConfig.State]
        READY: _ClassVar[InstanceConfig.State]
    STATE_UNSPECIFIED: InstanceConfig.State
    CREATING: InstanceConfig.State
    READY: InstanceConfig.State

    class FreeInstanceAvailability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FREE_INSTANCE_AVAILABILITY_UNSPECIFIED: _ClassVar[InstanceConfig.FreeInstanceAvailability]
        AVAILABLE: _ClassVar[InstanceConfig.FreeInstanceAvailability]
        UNSUPPORTED: _ClassVar[InstanceConfig.FreeInstanceAvailability]
        DISABLED: _ClassVar[InstanceConfig.FreeInstanceAvailability]
        QUOTA_EXCEEDED: _ClassVar[InstanceConfig.FreeInstanceAvailability]
    FREE_INSTANCE_AVAILABILITY_UNSPECIFIED: InstanceConfig.FreeInstanceAvailability
    AVAILABLE: InstanceConfig.FreeInstanceAvailability
    UNSUPPORTED: InstanceConfig.FreeInstanceAvailability
    DISABLED: InstanceConfig.FreeInstanceAvailability
    QUOTA_EXCEEDED: InstanceConfig.FreeInstanceAvailability

    class QuorumType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        QUORUM_TYPE_UNSPECIFIED: _ClassVar[InstanceConfig.QuorumType]
        REGION: _ClassVar[InstanceConfig.QuorumType]
        DUAL_REGION: _ClassVar[InstanceConfig.QuorumType]
        MULTI_REGION: _ClassVar[InstanceConfig.QuorumType]
    QUORUM_TYPE_UNSPECIFIED: InstanceConfig.QuorumType
    REGION: InstanceConfig.QuorumType
    DUAL_REGION: InstanceConfig.QuorumType
    MULTI_REGION: InstanceConfig.QuorumType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    BASE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LEADER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FREE_INSTANCE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    QUORUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LIMIT_PER_PROCESSING_UNIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    config_type: InstanceConfig.Type
    replicas: _containers.RepeatedCompositeFieldContainer[ReplicaInfo]
    optional_replicas: _containers.RepeatedCompositeFieldContainer[ReplicaInfo]
    base_config: str
    labels: _containers.ScalarMap[str, str]
    etag: str
    leader_options: _containers.RepeatedScalarFieldContainer[str]
    reconciling: bool
    state: InstanceConfig.State
    free_instance_availability: InstanceConfig.FreeInstanceAvailability
    quorum_type: InstanceConfig.QuorumType
    storage_limit_per_processing_unit: int

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., config_type: _Optional[_Union[InstanceConfig.Type, str]]=..., replicas: _Optional[_Iterable[_Union[ReplicaInfo, _Mapping]]]=..., optional_replicas: _Optional[_Iterable[_Union[ReplicaInfo, _Mapping]]]=..., base_config: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., leader_options: _Optional[_Iterable[str]]=..., reconciling: bool=..., state: _Optional[_Union[InstanceConfig.State, str]]=..., free_instance_availability: _Optional[_Union[InstanceConfig.FreeInstanceAvailability, str]]=..., quorum_type: _Optional[_Union[InstanceConfig.QuorumType, str]]=..., storage_limit_per_processing_unit: _Optional[int]=...) -> None:
        ...

class ReplicaComputeCapacity(_message.Message):
    __slots__ = ('replica_selection', 'node_count', 'processing_units')
    REPLICA_SELECTION_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_UNITS_FIELD_NUMBER: _ClassVar[int]
    replica_selection: _common_pb2.ReplicaSelection
    node_count: int
    processing_units: int

    def __init__(self, replica_selection: _Optional[_Union[_common_pb2.ReplicaSelection, _Mapping]]=..., node_count: _Optional[int]=..., processing_units: _Optional[int]=...) -> None:
        ...

class AutoscalingConfig(_message.Message):
    __slots__ = ('autoscaling_limits', 'autoscaling_targets', 'asymmetric_autoscaling_options')

    class AutoscalingLimits(_message.Message):
        __slots__ = ('min_nodes', 'min_processing_units', 'max_nodes', 'max_processing_units')
        MIN_NODES_FIELD_NUMBER: _ClassVar[int]
        MIN_PROCESSING_UNITS_FIELD_NUMBER: _ClassVar[int]
        MAX_NODES_FIELD_NUMBER: _ClassVar[int]
        MAX_PROCESSING_UNITS_FIELD_NUMBER: _ClassVar[int]
        min_nodes: int
        min_processing_units: int
        max_nodes: int
        max_processing_units: int

        def __init__(self, min_nodes: _Optional[int]=..., min_processing_units: _Optional[int]=..., max_nodes: _Optional[int]=..., max_processing_units: _Optional[int]=...) -> None:
            ...

    class AutoscalingTargets(_message.Message):
        __slots__ = ('high_priority_cpu_utilization_percent', 'storage_utilization_percent')
        HIGH_PRIORITY_CPU_UTILIZATION_PERCENT_FIELD_NUMBER: _ClassVar[int]
        STORAGE_UTILIZATION_PERCENT_FIELD_NUMBER: _ClassVar[int]
        high_priority_cpu_utilization_percent: int
        storage_utilization_percent: int

        def __init__(self, high_priority_cpu_utilization_percent: _Optional[int]=..., storage_utilization_percent: _Optional[int]=...) -> None:
            ...

    class AsymmetricAutoscalingOption(_message.Message):
        __slots__ = ('replica_selection', 'overrides')

        class AutoscalingConfigOverrides(_message.Message):
            __slots__ = ('autoscaling_limits', 'autoscaling_target_high_priority_cpu_utilization_percent')
            AUTOSCALING_LIMITS_FIELD_NUMBER: _ClassVar[int]
            AUTOSCALING_TARGET_HIGH_PRIORITY_CPU_UTILIZATION_PERCENT_FIELD_NUMBER: _ClassVar[int]
            autoscaling_limits: AutoscalingConfig.AutoscalingLimits
            autoscaling_target_high_priority_cpu_utilization_percent: int

            def __init__(self, autoscaling_limits: _Optional[_Union[AutoscalingConfig.AutoscalingLimits, _Mapping]]=..., autoscaling_target_high_priority_cpu_utilization_percent: _Optional[int]=...) -> None:
                ...
        REPLICA_SELECTION_FIELD_NUMBER: _ClassVar[int]
        OVERRIDES_FIELD_NUMBER: _ClassVar[int]
        replica_selection: _common_pb2.ReplicaSelection
        overrides: AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides

        def __init__(self, replica_selection: _Optional[_Union[_common_pb2.ReplicaSelection, _Mapping]]=..., overrides: _Optional[_Union[AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides, _Mapping]]=...) -> None:
            ...
    AUTOSCALING_LIMITS_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_TARGETS_FIELD_NUMBER: _ClassVar[int]
    ASYMMETRIC_AUTOSCALING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    autoscaling_limits: AutoscalingConfig.AutoscalingLimits
    autoscaling_targets: AutoscalingConfig.AutoscalingTargets
    asymmetric_autoscaling_options: _containers.RepeatedCompositeFieldContainer[AutoscalingConfig.AsymmetricAutoscalingOption]

    def __init__(self, autoscaling_limits: _Optional[_Union[AutoscalingConfig.AutoscalingLimits, _Mapping]]=..., autoscaling_targets: _Optional[_Union[AutoscalingConfig.AutoscalingTargets, _Mapping]]=..., asymmetric_autoscaling_options: _Optional[_Iterable[_Union[AutoscalingConfig.AsymmetricAutoscalingOption, _Mapping]]]=...) -> None:
        ...

class Instance(_message.Message):
    __slots__ = ('name', 'config', 'display_name', 'node_count', 'processing_units', 'replica_compute_capacity', 'autoscaling_config', 'state', 'labels', 'instance_type', 'endpoint_uris', 'create_time', 'update_time', 'free_instance_metadata', 'edition', 'default_backup_schedule_type')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        READY: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    READY: Instance.State

    class InstanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTANCE_TYPE_UNSPECIFIED: _ClassVar[Instance.InstanceType]
        PROVISIONED: _ClassVar[Instance.InstanceType]
        FREE_INSTANCE: _ClassVar[Instance.InstanceType]
    INSTANCE_TYPE_UNSPECIFIED: Instance.InstanceType
    PROVISIONED: Instance.InstanceType
    FREE_INSTANCE: Instance.InstanceType

    class Edition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EDITION_UNSPECIFIED: _ClassVar[Instance.Edition]
        STANDARD: _ClassVar[Instance.Edition]
        ENTERPRISE: _ClassVar[Instance.Edition]
        ENTERPRISE_PLUS: _ClassVar[Instance.Edition]
    EDITION_UNSPECIFIED: Instance.Edition
    STANDARD: Instance.Edition
    ENTERPRISE: Instance.Edition
    ENTERPRISE_PLUS: Instance.Edition

    class DefaultBackupScheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_BACKUP_SCHEDULE_TYPE_UNSPECIFIED: _ClassVar[Instance.DefaultBackupScheduleType]
        NONE: _ClassVar[Instance.DefaultBackupScheduleType]
        AUTOMATIC: _ClassVar[Instance.DefaultBackupScheduleType]
    DEFAULT_BACKUP_SCHEDULE_TYPE_UNSPECIFIED: Instance.DefaultBackupScheduleType
    NONE: Instance.DefaultBackupScheduleType
    AUTOMATIC: Instance.DefaultBackupScheduleType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_UNITS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COMPUTE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_URIS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FREE_INSTANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    EDITION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BACKUP_SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: str
    display_name: str
    node_count: int
    processing_units: int
    replica_compute_capacity: _containers.RepeatedCompositeFieldContainer[ReplicaComputeCapacity]
    autoscaling_config: AutoscalingConfig
    state: Instance.State
    labels: _containers.ScalarMap[str, str]
    instance_type: Instance.InstanceType
    endpoint_uris: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    free_instance_metadata: FreeInstanceMetadata
    edition: Instance.Edition
    default_backup_schedule_type: Instance.DefaultBackupScheduleType

    def __init__(self, name: _Optional[str]=..., config: _Optional[str]=..., display_name: _Optional[str]=..., node_count: _Optional[int]=..., processing_units: _Optional[int]=..., replica_compute_capacity: _Optional[_Iterable[_Union[ReplicaComputeCapacity, _Mapping]]]=..., autoscaling_config: _Optional[_Union[AutoscalingConfig, _Mapping]]=..., state: _Optional[_Union[Instance.State, str]]=..., labels: _Optional[_Mapping[str, str]]=..., instance_type: _Optional[_Union[Instance.InstanceType, str]]=..., endpoint_uris: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., free_instance_metadata: _Optional[_Union[FreeInstanceMetadata, _Mapping]]=..., edition: _Optional[_Union[Instance.Edition, str]]=..., default_backup_schedule_type: _Optional[_Union[Instance.DefaultBackupScheduleType, str]]=...) -> None:
        ...

class ListInstanceConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListInstanceConfigsResponse(_message.Message):
    __slots__ = ('instance_configs', 'next_page_token')
    INSTANCE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    instance_configs: _containers.RepeatedCompositeFieldContainer[InstanceConfig]
    next_page_token: str

    def __init__(self, instance_configs: _Optional[_Iterable[_Union[InstanceConfig, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetInstanceConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceConfigRequest(_message.Message):
    __slots__ = ('parent', 'instance_config_id', 'instance_config', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_config_id: str
    instance_config: InstanceConfig
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., instance_config_id: _Optional[str]=..., instance_config: _Optional[_Union[InstanceConfig, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateInstanceConfigRequest(_message.Message):
    __slots__ = ('instance_config', 'update_mask', 'validate_only')
    INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    instance_config: InstanceConfig
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, instance_config: _Optional[_Union[InstanceConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteInstanceConfigRequest(_message.Message):
    __slots__ = ('name', 'etag', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class ListInstanceConfigOperationsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListInstanceConfigOperationsResponse(_message.Message):
    __slots__ = ('operations', 'next_page_token')
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[_operations_pb2.Operation]
    next_page_token: str

    def __init__(self, operations: _Optional[_Iterable[_Union[_operations_pb2.Operation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name', 'field_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    field_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'instance')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: Instance

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., instance: _Optional[_Union[Instance, _Mapping]]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'instance_deadline')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    instance_deadline: _timestamp_pb2.Timestamp

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., instance_deadline: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ('instance', 'field_mask')
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    instance: Instance
    field_mask: _field_mask_pb2.FieldMask

    def __init__(self, instance: _Optional[_Union[Instance, _Mapping]]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceMetadata(_message.Message):
    __slots__ = ('instance', 'start_time', 'cancel_time', 'end_time', 'expected_fulfillment_period')
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FULFILLMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    instance: Instance
    start_time: _timestamp_pb2.Timestamp
    cancel_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    expected_fulfillment_period: _common_pb2.FulfillmentPeriod

    def __init__(self, instance: _Optional[_Union[Instance, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expected_fulfillment_period: _Optional[_Union[_common_pb2.FulfillmentPeriod, str]]=...) -> None:
        ...

class UpdateInstanceMetadata(_message.Message):
    __slots__ = ('instance', 'start_time', 'cancel_time', 'end_time', 'expected_fulfillment_period')
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FULFILLMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    instance: Instance
    start_time: _timestamp_pb2.Timestamp
    cancel_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    expected_fulfillment_period: _common_pb2.FulfillmentPeriod

    def __init__(self, instance: _Optional[_Union[Instance, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expected_fulfillment_period: _Optional[_Union[_common_pb2.FulfillmentPeriod, str]]=...) -> None:
        ...

class FreeInstanceMetadata(_message.Message):
    __slots__ = ('expire_time', 'upgrade_time', 'expire_behavior')

    class ExpireBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXPIRE_BEHAVIOR_UNSPECIFIED: _ClassVar[FreeInstanceMetadata.ExpireBehavior]
        FREE_TO_PROVISIONED: _ClassVar[FreeInstanceMetadata.ExpireBehavior]
        REMOVE_AFTER_GRACE_PERIOD: _ClassVar[FreeInstanceMetadata.ExpireBehavior]
    EXPIRE_BEHAVIOR_UNSPECIFIED: FreeInstanceMetadata.ExpireBehavior
    FREE_TO_PROVISIONED: FreeInstanceMetadata.ExpireBehavior
    REMOVE_AFTER_GRACE_PERIOD: FreeInstanceMetadata.ExpireBehavior
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    expire_time: _timestamp_pb2.Timestamp
    upgrade_time: _timestamp_pb2.Timestamp
    expire_behavior: FreeInstanceMetadata.ExpireBehavior

    def __init__(self, expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., upgrade_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_behavior: _Optional[_Union[FreeInstanceMetadata.ExpireBehavior, str]]=...) -> None:
        ...

class CreateInstanceConfigMetadata(_message.Message):
    __slots__ = ('instance_config', 'progress', 'cancel_time')
    INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    instance_config: InstanceConfig
    progress: _common_pb2.OperationProgress
    cancel_time: _timestamp_pb2.Timestamp

    def __init__(self, instance_config: _Optional[_Union[InstanceConfig, _Mapping]]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpdateInstanceConfigMetadata(_message.Message):
    __slots__ = ('instance_config', 'progress', 'cancel_time')
    INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    instance_config: InstanceConfig
    progress: _common_pb2.OperationProgress
    cancel_time: _timestamp_pb2.Timestamp

    def __init__(self, instance_config: _Optional[_Union[InstanceConfig, _Mapping]]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class InstancePartition(_message.Message):
    __slots__ = ('name', 'config', 'display_name', 'node_count', 'processing_units', 'state', 'create_time', 'update_time', 'referencing_databases', 'referencing_backups', 'etag')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[InstancePartition.State]
        CREATING: _ClassVar[InstancePartition.State]
        READY: _ClassVar[InstancePartition.State]
    STATE_UNSPECIFIED: InstancePartition.State
    CREATING: InstancePartition.State
    READY: InstancePartition.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_UNITS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REFERENCING_DATABASES_FIELD_NUMBER: _ClassVar[int]
    REFERENCING_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: str
    display_name: str
    node_count: int
    processing_units: int
    state: InstancePartition.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    referencing_databases: _containers.RepeatedScalarFieldContainer[str]
    referencing_backups: _containers.RepeatedScalarFieldContainer[str]
    etag: str

    def __init__(self, name: _Optional[str]=..., config: _Optional[str]=..., display_name: _Optional[str]=..., node_count: _Optional[int]=..., processing_units: _Optional[int]=..., state: _Optional[_Union[InstancePartition.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., referencing_databases: _Optional[_Iterable[str]]=..., referencing_backups: _Optional[_Iterable[str]]=..., etag: _Optional[str]=...) -> None:
        ...

class CreateInstancePartitionMetadata(_message.Message):
    __slots__ = ('instance_partition', 'start_time', 'cancel_time', 'end_time')
    INSTANCE_PARTITION_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    instance_partition: InstancePartition
    start_time: _timestamp_pb2.Timestamp
    cancel_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, instance_partition: _Optional[_Union[InstancePartition, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateInstancePartitionRequest(_message.Message):
    __slots__ = ('parent', 'instance_partition_id', 'instance_partition')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_PARTITION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_partition_id: str
    instance_partition: InstancePartition

    def __init__(self, parent: _Optional[str]=..., instance_partition_id: _Optional[str]=..., instance_partition: _Optional[_Union[InstancePartition, _Mapping]]=...) -> None:
        ...

class DeleteInstancePartitionRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class GetInstancePartitionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateInstancePartitionRequest(_message.Message):
    __slots__ = ('instance_partition', 'field_mask')
    INSTANCE_PARTITION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    instance_partition: InstancePartition
    field_mask: _field_mask_pb2.FieldMask

    def __init__(self, instance_partition: _Optional[_Union[InstancePartition, _Mapping]]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateInstancePartitionMetadata(_message.Message):
    __slots__ = ('instance_partition', 'start_time', 'cancel_time', 'end_time')
    INSTANCE_PARTITION_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    instance_partition: InstancePartition
    start_time: _timestamp_pb2.Timestamp
    cancel_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, instance_partition: _Optional[_Union[InstancePartition, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListInstancePartitionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'instance_partition_deadline')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_PARTITION_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    instance_partition_deadline: _timestamp_pb2.Timestamp

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., instance_partition_deadline: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListInstancePartitionsResponse(_message.Message):
    __slots__ = ('instance_partitions', 'next_page_token', 'unreachable')
    INSTANCE_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instance_partitions: _containers.RepeatedCompositeFieldContainer[InstancePartition]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instance_partitions: _Optional[_Iterable[_Union[InstancePartition, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListInstancePartitionOperationsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'instance_partition_deadline')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_PARTITION_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    instance_partition_deadline: _timestamp_pb2.Timestamp

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., instance_partition_deadline: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListInstancePartitionOperationsResponse(_message.Message):
    __slots__ = ('operations', 'next_page_token', 'unreachable_instance_partitions')
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_INSTANCE_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[_operations_pb2.Operation]
    next_page_token: str
    unreachable_instance_partitions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, operations: _Optional[_Iterable[_Union[_operations_pb2.Operation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_instance_partitions: _Optional[_Iterable[str]]=...) -> None:
        ...

class MoveInstanceRequest(_message.Message):
    __slots__ = ('name', 'target_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_config: str

    def __init__(self, name: _Optional[str]=..., target_config: _Optional[str]=...) -> None:
        ...

class MoveInstanceResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MoveInstanceMetadata(_message.Message):
    __slots__ = ('target_config', 'progress', 'cancel_time')
    TARGET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    target_config: str
    progress: _common_pb2.OperationProgress
    cancel_time: _timestamp_pb2.Timestamp

    def __init__(self, target_config: _Optional[str]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...