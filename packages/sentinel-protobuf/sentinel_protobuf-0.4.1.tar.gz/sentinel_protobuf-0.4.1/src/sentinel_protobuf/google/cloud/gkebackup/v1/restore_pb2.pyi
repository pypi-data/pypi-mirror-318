from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkebackup.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Restore(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'backup', 'cluster', 'restore_config', 'labels', 'state', 'state_reason', 'complete_time', 'resources_restored_count', 'resources_excluded_count', 'resources_failed_count', 'volumes_restored_count', 'etag', 'filter', 'volume_data_restore_policy_overrides')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Restore.State]
        CREATING: _ClassVar[Restore.State]
        IN_PROGRESS: _ClassVar[Restore.State]
        SUCCEEDED: _ClassVar[Restore.State]
        FAILED: _ClassVar[Restore.State]
        DELETING: _ClassVar[Restore.State]
    STATE_UNSPECIFIED: Restore.State
    CREATING: Restore.State
    IN_PROGRESS: Restore.State
    SUCCEEDED: Restore.State
    FAILED: Restore.State
    DELETING: Restore.State

    class Filter(_message.Message):
        __slots__ = ('inclusion_filters', 'exclusion_filters')
        INCLUSION_FILTERS_FIELD_NUMBER: _ClassVar[int]
        EXCLUSION_FILTERS_FIELD_NUMBER: _ClassVar[int]
        inclusion_filters: _containers.RepeatedCompositeFieldContainer[ResourceSelector]
        exclusion_filters: _containers.RepeatedCompositeFieldContainer[ResourceSelector]

        def __init__(self, inclusion_filters: _Optional[_Iterable[_Union[ResourceSelector, _Mapping]]]=..., exclusion_filters: _Optional[_Iterable[_Union[ResourceSelector, _Mapping]]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_RESTORED_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_EXCLUDED_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_RESTORED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DATA_RESTORE_POLICY_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    backup: str
    cluster: str
    restore_config: RestoreConfig
    labels: _containers.ScalarMap[str, str]
    state: Restore.State
    state_reason: str
    complete_time: _timestamp_pb2.Timestamp
    resources_restored_count: int
    resources_excluded_count: int
    resources_failed_count: int
    volumes_restored_count: int
    etag: str
    filter: Restore.Filter
    volume_data_restore_policy_overrides: _containers.RepeatedCompositeFieldContainer[VolumeDataRestorePolicyOverride]

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., backup: _Optional[str]=..., cluster: _Optional[str]=..., restore_config: _Optional[_Union[RestoreConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Restore.State, str]]=..., state_reason: _Optional[str]=..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., resources_restored_count: _Optional[int]=..., resources_excluded_count: _Optional[int]=..., resources_failed_count: _Optional[int]=..., volumes_restored_count: _Optional[int]=..., etag: _Optional[str]=..., filter: _Optional[_Union[Restore.Filter, _Mapping]]=..., volume_data_restore_policy_overrides: _Optional[_Iterable[_Union[VolumeDataRestorePolicyOverride, _Mapping]]]=...) -> None:
        ...

class RestoreConfig(_message.Message):
    __slots__ = ('volume_data_restore_policy', 'cluster_resource_conflict_policy', 'namespaced_resource_restore_mode', 'cluster_resource_restore_scope', 'all_namespaces', 'selected_namespaces', 'selected_applications', 'no_namespaces', 'excluded_namespaces', 'substitution_rules', 'transformation_rules', 'volume_data_restore_policy_bindings', 'restore_order')

    class VolumeDataRestorePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED: _ClassVar[RestoreConfig.VolumeDataRestorePolicy]
        RESTORE_VOLUME_DATA_FROM_BACKUP: _ClassVar[RestoreConfig.VolumeDataRestorePolicy]
        REUSE_VOLUME_HANDLE_FROM_BACKUP: _ClassVar[RestoreConfig.VolumeDataRestorePolicy]
        NO_VOLUME_DATA_RESTORATION: _ClassVar[RestoreConfig.VolumeDataRestorePolicy]
    VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED: RestoreConfig.VolumeDataRestorePolicy
    RESTORE_VOLUME_DATA_FROM_BACKUP: RestoreConfig.VolumeDataRestorePolicy
    REUSE_VOLUME_HANDLE_FROM_BACKUP: RestoreConfig.VolumeDataRestorePolicy
    NO_VOLUME_DATA_RESTORATION: RestoreConfig.VolumeDataRestorePolicy

    class ClusterResourceConflictPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED: _ClassVar[RestoreConfig.ClusterResourceConflictPolicy]
        USE_EXISTING_VERSION: _ClassVar[RestoreConfig.ClusterResourceConflictPolicy]
        USE_BACKUP_VERSION: _ClassVar[RestoreConfig.ClusterResourceConflictPolicy]
    CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED: RestoreConfig.ClusterResourceConflictPolicy
    USE_EXISTING_VERSION: RestoreConfig.ClusterResourceConflictPolicy
    USE_BACKUP_VERSION: RestoreConfig.ClusterResourceConflictPolicy

    class NamespacedResourceRestoreMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED: _ClassVar[RestoreConfig.NamespacedResourceRestoreMode]
        DELETE_AND_RESTORE: _ClassVar[RestoreConfig.NamespacedResourceRestoreMode]
        FAIL_ON_CONFLICT: _ClassVar[RestoreConfig.NamespacedResourceRestoreMode]
        MERGE_SKIP_ON_CONFLICT: _ClassVar[RestoreConfig.NamespacedResourceRestoreMode]
        MERGE_REPLACE_VOLUME_ON_CONFLICT: _ClassVar[RestoreConfig.NamespacedResourceRestoreMode]
        MERGE_REPLACE_ON_CONFLICT: _ClassVar[RestoreConfig.NamespacedResourceRestoreMode]
    NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED: RestoreConfig.NamespacedResourceRestoreMode
    DELETE_AND_RESTORE: RestoreConfig.NamespacedResourceRestoreMode
    FAIL_ON_CONFLICT: RestoreConfig.NamespacedResourceRestoreMode
    MERGE_SKIP_ON_CONFLICT: RestoreConfig.NamespacedResourceRestoreMode
    MERGE_REPLACE_VOLUME_ON_CONFLICT: RestoreConfig.NamespacedResourceRestoreMode
    MERGE_REPLACE_ON_CONFLICT: RestoreConfig.NamespacedResourceRestoreMode

    class GroupKind(_message.Message):
        __slots__ = ('resource_group', 'resource_kind')
        RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
        resource_group: str
        resource_kind: str

        def __init__(self, resource_group: _Optional[str]=..., resource_kind: _Optional[str]=...) -> None:
            ...

    class ClusterResourceRestoreScope(_message.Message):
        __slots__ = ('selected_group_kinds', 'excluded_group_kinds', 'all_group_kinds', 'no_group_kinds')
        SELECTED_GROUP_KINDS_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_GROUP_KINDS_FIELD_NUMBER: _ClassVar[int]
        ALL_GROUP_KINDS_FIELD_NUMBER: _ClassVar[int]
        NO_GROUP_KINDS_FIELD_NUMBER: _ClassVar[int]
        selected_group_kinds: _containers.RepeatedCompositeFieldContainer[RestoreConfig.GroupKind]
        excluded_group_kinds: _containers.RepeatedCompositeFieldContainer[RestoreConfig.GroupKind]
        all_group_kinds: bool
        no_group_kinds: bool

        def __init__(self, selected_group_kinds: _Optional[_Iterable[_Union[RestoreConfig.GroupKind, _Mapping]]]=..., excluded_group_kinds: _Optional[_Iterable[_Union[RestoreConfig.GroupKind, _Mapping]]]=..., all_group_kinds: bool=..., no_group_kinds: bool=...) -> None:
            ...

    class SubstitutionRule(_message.Message):
        __slots__ = ('target_namespaces', 'target_group_kinds', 'target_json_path', 'original_value_pattern', 'new_value')
        TARGET_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
        TARGET_GROUP_KINDS_FIELD_NUMBER: _ClassVar[int]
        TARGET_JSON_PATH_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_VALUE_PATTERN_FIELD_NUMBER: _ClassVar[int]
        NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
        target_namespaces: _containers.RepeatedScalarFieldContainer[str]
        target_group_kinds: _containers.RepeatedCompositeFieldContainer[RestoreConfig.GroupKind]
        target_json_path: str
        original_value_pattern: str
        new_value: str

        def __init__(self, target_namespaces: _Optional[_Iterable[str]]=..., target_group_kinds: _Optional[_Iterable[_Union[RestoreConfig.GroupKind, _Mapping]]]=..., target_json_path: _Optional[str]=..., original_value_pattern: _Optional[str]=..., new_value: _Optional[str]=...) -> None:
            ...

    class TransformationRuleAction(_message.Message):
        __slots__ = ('op', 'from_path', 'path', 'value')

        class Op(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OP_UNSPECIFIED: _ClassVar[RestoreConfig.TransformationRuleAction.Op]
            REMOVE: _ClassVar[RestoreConfig.TransformationRuleAction.Op]
            MOVE: _ClassVar[RestoreConfig.TransformationRuleAction.Op]
            COPY: _ClassVar[RestoreConfig.TransformationRuleAction.Op]
            ADD: _ClassVar[RestoreConfig.TransformationRuleAction.Op]
            TEST: _ClassVar[RestoreConfig.TransformationRuleAction.Op]
            REPLACE: _ClassVar[RestoreConfig.TransformationRuleAction.Op]
        OP_UNSPECIFIED: RestoreConfig.TransformationRuleAction.Op
        REMOVE: RestoreConfig.TransformationRuleAction.Op
        MOVE: RestoreConfig.TransformationRuleAction.Op
        COPY: RestoreConfig.TransformationRuleAction.Op
        ADD: RestoreConfig.TransformationRuleAction.Op
        TEST: RestoreConfig.TransformationRuleAction.Op
        REPLACE: RestoreConfig.TransformationRuleAction.Op
        OP_FIELD_NUMBER: _ClassVar[int]
        FROM_PATH_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        op: RestoreConfig.TransformationRuleAction.Op
        from_path: str
        path: str
        value: str

        def __init__(self, op: _Optional[_Union[RestoreConfig.TransformationRuleAction.Op, str]]=..., from_path: _Optional[str]=..., path: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class ResourceFilter(_message.Message):
        __slots__ = ('namespaces', 'group_kinds', 'json_path')
        NAMESPACES_FIELD_NUMBER: _ClassVar[int]
        GROUP_KINDS_FIELD_NUMBER: _ClassVar[int]
        JSON_PATH_FIELD_NUMBER: _ClassVar[int]
        namespaces: _containers.RepeatedScalarFieldContainer[str]
        group_kinds: _containers.RepeatedCompositeFieldContainer[RestoreConfig.GroupKind]
        json_path: str

        def __init__(self, namespaces: _Optional[_Iterable[str]]=..., group_kinds: _Optional[_Iterable[_Union[RestoreConfig.GroupKind, _Mapping]]]=..., json_path: _Optional[str]=...) -> None:
            ...

    class TransformationRule(_message.Message):
        __slots__ = ('field_actions', 'resource_filter', 'description')
        FIELD_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FILTER_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        field_actions: _containers.RepeatedCompositeFieldContainer[RestoreConfig.TransformationRuleAction]
        resource_filter: RestoreConfig.ResourceFilter
        description: str

        def __init__(self, field_actions: _Optional[_Iterable[_Union[RestoreConfig.TransformationRuleAction, _Mapping]]]=..., resource_filter: _Optional[_Union[RestoreConfig.ResourceFilter, _Mapping]]=..., description: _Optional[str]=...) -> None:
            ...

    class VolumeDataRestorePolicyBinding(_message.Message):
        __slots__ = ('policy', 'volume_type')
        POLICY_FIELD_NUMBER: _ClassVar[int]
        VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
        policy: RestoreConfig.VolumeDataRestorePolicy
        volume_type: _common_pb2.VolumeTypeEnum.VolumeType

        def __init__(self, policy: _Optional[_Union[RestoreConfig.VolumeDataRestorePolicy, str]]=..., volume_type: _Optional[_Union[_common_pb2.VolumeTypeEnum.VolumeType, str]]=...) -> None:
            ...

    class RestoreOrder(_message.Message):
        __slots__ = ('group_kind_dependencies',)

        class GroupKindDependency(_message.Message):
            __slots__ = ('satisfying', 'requiring')
            SATISFYING_FIELD_NUMBER: _ClassVar[int]
            REQUIRING_FIELD_NUMBER: _ClassVar[int]
            satisfying: RestoreConfig.GroupKind
            requiring: RestoreConfig.GroupKind

            def __init__(self, satisfying: _Optional[_Union[RestoreConfig.GroupKind, _Mapping]]=..., requiring: _Optional[_Union[RestoreConfig.GroupKind, _Mapping]]=...) -> None:
                ...
        GROUP_KIND_DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
        group_kind_dependencies: _containers.RepeatedCompositeFieldContainer[RestoreConfig.RestoreOrder.GroupKindDependency]

        def __init__(self, group_kind_dependencies: _Optional[_Iterable[_Union[RestoreConfig.RestoreOrder.GroupKindDependency, _Mapping]]]=...) -> None:
            ...
    VOLUME_DATA_RESTORE_POLICY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_RESOURCE_CONFLICT_POLICY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACED_RESOURCE_RESTORE_MODE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_RESOURCE_RESTORE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    ALL_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    SELECTED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    SELECTED_APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    NO_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTION_RULES_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATION_RULES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DATA_RESTORE_POLICY_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ORDER_FIELD_NUMBER: _ClassVar[int]
    volume_data_restore_policy: RestoreConfig.VolumeDataRestorePolicy
    cluster_resource_conflict_policy: RestoreConfig.ClusterResourceConflictPolicy
    namespaced_resource_restore_mode: RestoreConfig.NamespacedResourceRestoreMode
    cluster_resource_restore_scope: RestoreConfig.ClusterResourceRestoreScope
    all_namespaces: bool
    selected_namespaces: _common_pb2.Namespaces
    selected_applications: _common_pb2.NamespacedNames
    no_namespaces: bool
    excluded_namespaces: _common_pb2.Namespaces
    substitution_rules: _containers.RepeatedCompositeFieldContainer[RestoreConfig.SubstitutionRule]
    transformation_rules: _containers.RepeatedCompositeFieldContainer[RestoreConfig.TransformationRule]
    volume_data_restore_policy_bindings: _containers.RepeatedCompositeFieldContainer[RestoreConfig.VolumeDataRestorePolicyBinding]
    restore_order: RestoreConfig.RestoreOrder

    def __init__(self, volume_data_restore_policy: _Optional[_Union[RestoreConfig.VolumeDataRestorePolicy, str]]=..., cluster_resource_conflict_policy: _Optional[_Union[RestoreConfig.ClusterResourceConflictPolicy, str]]=..., namespaced_resource_restore_mode: _Optional[_Union[RestoreConfig.NamespacedResourceRestoreMode, str]]=..., cluster_resource_restore_scope: _Optional[_Union[RestoreConfig.ClusterResourceRestoreScope, _Mapping]]=..., all_namespaces: bool=..., selected_namespaces: _Optional[_Union[_common_pb2.Namespaces, _Mapping]]=..., selected_applications: _Optional[_Union[_common_pb2.NamespacedNames, _Mapping]]=..., no_namespaces: bool=..., excluded_namespaces: _Optional[_Union[_common_pb2.Namespaces, _Mapping]]=..., substitution_rules: _Optional[_Iterable[_Union[RestoreConfig.SubstitutionRule, _Mapping]]]=..., transformation_rules: _Optional[_Iterable[_Union[RestoreConfig.TransformationRule, _Mapping]]]=..., volume_data_restore_policy_bindings: _Optional[_Iterable[_Union[RestoreConfig.VolumeDataRestorePolicyBinding, _Mapping]]]=..., restore_order: _Optional[_Union[RestoreConfig.RestoreOrder, _Mapping]]=...) -> None:
        ...

class ResourceSelector(_message.Message):
    __slots__ = ('group_kind', 'name', 'namespace', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    GROUP_KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    group_kind: RestoreConfig.GroupKind
    name: str
    namespace: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, group_kind: _Optional[_Union[RestoreConfig.GroupKind, _Mapping]]=..., name: _Optional[str]=..., namespace: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class VolumeDataRestorePolicyOverride(_message.Message):
    __slots__ = ('policy', 'selected_pvcs')
    POLICY_FIELD_NUMBER: _ClassVar[int]
    SELECTED_PVCS_FIELD_NUMBER: _ClassVar[int]
    policy: RestoreConfig.VolumeDataRestorePolicy
    selected_pvcs: _common_pb2.NamespacedNames

    def __init__(self, policy: _Optional[_Union[RestoreConfig.VolumeDataRestorePolicy, str]]=..., selected_pvcs: _Optional[_Union[_common_pb2.NamespacedNames, _Mapping]]=...) -> None:
        ...