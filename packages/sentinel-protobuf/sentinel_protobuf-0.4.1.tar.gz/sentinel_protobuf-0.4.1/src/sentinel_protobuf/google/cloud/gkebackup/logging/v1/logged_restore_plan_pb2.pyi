from google.cloud.gkebackup.logging.v1 import logged_common_pb2 as _logged_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LoggedRestorePlan(_message.Message):
    __slots__ = ('description', 'backup_plan', 'cluster', 'restore_config', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    description: str
    backup_plan: str
    cluster: str
    restore_config: RestoreConfig
    labels: _containers.ScalarMap[str, str]

    def __init__(self, description: _Optional[str]=..., backup_plan: _Optional[str]=..., cluster: _Optional[str]=..., restore_config: _Optional[_Union[RestoreConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class RestoreConfig(_message.Message):
    __slots__ = ('volume_data_restore_policy', 'cluster_resource_conflict_policy', 'namespaced_resource_restore_mode', 'cluster_resource_restore_scope', 'all_namespaces', 'selected_namespaces', 'selected_applications', 'substitution_rules')

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
    NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED: RestoreConfig.NamespacedResourceRestoreMode
    DELETE_AND_RESTORE: RestoreConfig.NamespacedResourceRestoreMode
    FAIL_ON_CONFLICT: RestoreConfig.NamespacedResourceRestoreMode

    class GroupKind(_message.Message):
        __slots__ = ('resource_group', 'resource_kind')
        RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
        resource_group: str
        resource_kind: str

        def __init__(self, resource_group: _Optional[str]=..., resource_kind: _Optional[str]=...) -> None:
            ...

    class ClusterResourceRestoreScope(_message.Message):
        __slots__ = ('selected_group_kinds',)
        SELECTED_GROUP_KINDS_FIELD_NUMBER: _ClassVar[int]
        selected_group_kinds: _containers.RepeatedCompositeFieldContainer[RestoreConfig.GroupKind]

        def __init__(self, selected_group_kinds: _Optional[_Iterable[_Union[RestoreConfig.GroupKind, _Mapping]]]=...) -> None:
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
    VOLUME_DATA_RESTORE_POLICY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_RESOURCE_CONFLICT_POLICY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACED_RESOURCE_RESTORE_MODE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_RESOURCE_RESTORE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    ALL_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    SELECTED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    SELECTED_APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTION_RULES_FIELD_NUMBER: _ClassVar[int]
    volume_data_restore_policy: RestoreConfig.VolumeDataRestorePolicy
    cluster_resource_conflict_policy: RestoreConfig.ClusterResourceConflictPolicy
    namespaced_resource_restore_mode: RestoreConfig.NamespacedResourceRestoreMode
    cluster_resource_restore_scope: RestoreConfig.ClusterResourceRestoreScope
    all_namespaces: bool
    selected_namespaces: _logged_common_pb2.Namespaces
    selected_applications: _logged_common_pb2.NamespacedNames
    substitution_rules: _containers.RepeatedCompositeFieldContainer[RestoreConfig.SubstitutionRule]

    def __init__(self, volume_data_restore_policy: _Optional[_Union[RestoreConfig.VolumeDataRestorePolicy, str]]=..., cluster_resource_conflict_policy: _Optional[_Union[RestoreConfig.ClusterResourceConflictPolicy, str]]=..., namespaced_resource_restore_mode: _Optional[_Union[RestoreConfig.NamespacedResourceRestoreMode, str]]=..., cluster_resource_restore_scope: _Optional[_Union[RestoreConfig.ClusterResourceRestoreScope, _Mapping]]=..., all_namespaces: bool=..., selected_namespaces: _Optional[_Union[_logged_common_pb2.Namespaces, _Mapping]]=..., selected_applications: _Optional[_Union[_logged_common_pb2.NamespacedNames, _Mapping]]=..., substitution_rules: _Optional[_Iterable[_Union[RestoreConfig.SubstitutionRule, _Mapping]]]=...) -> None:
        ...