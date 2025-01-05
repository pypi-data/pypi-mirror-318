from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.v1 import asset_pb2 as _asset_pb2
from google.cloud.securitycenter.v1 import attack_path_pb2 as _attack_path_pb2
from google.cloud.securitycenter.v1 import bigquery_export_pb2 as _bigquery_export_pb2
from google.cloud.securitycenter.v1 import effective_event_threat_detection_custom_module_pb2 as _effective_event_threat_detection_custom_module_pb2
from google.cloud.securitycenter.v1 import effective_security_health_analytics_custom_module_pb2 as _effective_security_health_analytics_custom_module_pb2
from google.cloud.securitycenter.v1 import event_threat_detection_custom_module_pb2 as _event_threat_detection_custom_module_pb2
from google.cloud.securitycenter.v1 import event_threat_detection_custom_module_validation_errors_pb2 as _event_threat_detection_custom_module_validation_errors_pb2
from google.cloud.securitycenter.v1 import external_system_pb2 as _external_system_pb2
from google.cloud.securitycenter.v1 import finding_pb2 as _finding_pb2
from google.cloud.securitycenter.v1 import folder_pb2 as _folder_pb2
from google.cloud.securitycenter.v1 import mute_config_pb2 as _mute_config_pb2
from google.cloud.securitycenter.v1 import notification_config_pb2 as _notification_config_pb2
from google.cloud.securitycenter.v1 import organization_settings_pb2 as _organization_settings_pb2
from google.cloud.securitycenter.v1 import resource_pb2 as _resource_pb2_1
from google.cloud.securitycenter.v1 import resource_value_config_pb2 as _resource_value_config_pb2
from google.cloud.securitycenter.v1 import run_asset_discovery_response_pb2 as _run_asset_discovery_response_pb2
from google.cloud.securitycenter.v1 import security_health_analytics_custom_config_pb2 as _security_health_analytics_custom_config_pb2
from google.cloud.securitycenter.v1 import security_health_analytics_custom_module_pb2 as _security_health_analytics_custom_module_pb2
from google.cloud.securitycenter.v1 import security_marks_pb2 as _security_marks_pb2
from google.cloud.securitycenter.v1 import simulation_pb2 as _simulation_pb2
from google.cloud.securitycenter.v1 import source_pb2 as _source_pb2
from google.cloud.securitycenter.v1 import valued_resource_pb2 as _valued_resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BulkMuteFindingsRequest(_message.Message):
    __slots__ = ("parent", "filter", "mute_annotation", "mute_state")
    class MuteState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUTE_STATE_UNSPECIFIED: _ClassVar[BulkMuteFindingsRequest.MuteState]
        MUTED: _ClassVar[BulkMuteFindingsRequest.MuteState]
        UNDEFINED: _ClassVar[BulkMuteFindingsRequest.MuteState]
    MUTE_STATE_UNSPECIFIED: BulkMuteFindingsRequest.MuteState
    MUTED: BulkMuteFindingsRequest.MuteState
    UNDEFINED: BulkMuteFindingsRequest.MuteState
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    MUTE_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    MUTE_STATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    mute_annotation: str
    mute_state: BulkMuteFindingsRequest.MuteState
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., mute_annotation: _Optional[str] = ..., mute_state: _Optional[_Union[BulkMuteFindingsRequest.MuteState, str]] = ...) -> None: ...

class BulkMuteFindingsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateFindingRequest(_message.Message):
    __slots__ = ("parent", "finding_id", "finding")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    FINDING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    finding_id: str
    finding: _finding_pb2.Finding
    def __init__(self, parent: _Optional[str] = ..., finding_id: _Optional[str] = ..., finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]] = ...) -> None: ...

class CreateMuteConfigRequest(_message.Message):
    __slots__ = ("parent", "mute_config", "mute_config_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MUTE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MUTE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    mute_config: _mute_config_pb2.MuteConfig
    mute_config_id: str
    def __init__(self, parent: _Optional[str] = ..., mute_config: _Optional[_Union[_mute_config_pb2.MuteConfig, _Mapping]] = ..., mute_config_id: _Optional[str] = ...) -> None: ...

class CreateResourceValueConfigRequest(_message.Message):
    __slots__ = ("parent", "resource_value_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VALUE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    resource_value_config: _resource_value_config_pb2.ResourceValueConfig
    def __init__(self, parent: _Optional[str] = ..., resource_value_config: _Optional[_Union[_resource_value_config_pb2.ResourceValueConfig, _Mapping]] = ...) -> None: ...

class BatchCreateResourceValueConfigsRequest(_message.Message):
    __slots__ = ("parent", "requests")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateResourceValueConfigRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[CreateResourceValueConfigRequest, _Mapping]]] = ...) -> None: ...

class BatchCreateResourceValueConfigsResponse(_message.Message):
    __slots__ = ("resource_value_configs",)
    RESOURCE_VALUE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    resource_value_configs: _containers.RepeatedCompositeFieldContainer[_resource_value_config_pb2.ResourceValueConfig]
    def __init__(self, resource_value_configs: _Optional[_Iterable[_Union[_resource_value_config_pb2.ResourceValueConfig, _Mapping]]] = ...) -> None: ...

class DeleteResourceValueConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetResourceValueConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListResourceValueConfigsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListResourceValueConfigsResponse(_message.Message):
    __slots__ = ("resource_value_configs", "next_page_token")
    RESOURCE_VALUE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource_value_configs: _containers.RepeatedCompositeFieldContainer[_resource_value_config_pb2.ResourceValueConfig]
    next_page_token: str
    def __init__(self, resource_value_configs: _Optional[_Iterable[_Union[_resource_value_config_pb2.ResourceValueConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateResourceValueConfigRequest(_message.Message):
    __slots__ = ("resource_value_config", "update_mask")
    RESOURCE_VALUE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    resource_value_config: _resource_value_config_pb2.ResourceValueConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, resource_value_config: _Optional[_Union[_resource_value_config_pb2.ResourceValueConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateNotificationConfigRequest(_message.Message):
    __slots__ = ("parent", "config_id", "notification_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    config_id: str
    notification_config: _notification_config_pb2.NotificationConfig
    def __init__(self, parent: _Optional[str] = ..., config_id: _Optional[str] = ..., notification_config: _Optional[_Union[_notification_config_pb2.NotificationConfig, _Mapping]] = ...) -> None: ...

class CreateSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("parent", "security_health_analytics_custom_module")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    security_health_analytics_custom_module: _security_health_analytics_custom_module_pb2.SecurityHealthAnalyticsCustomModule
    def __init__(self, parent: _Optional[str] = ..., security_health_analytics_custom_module: _Optional[_Union[_security_health_analytics_custom_module_pb2.SecurityHealthAnalyticsCustomModule, _Mapping]] = ...) -> None: ...

class CreateSourceRequest(_message.Message):
    __slots__ = ("parent", "source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source: _source_pb2.Source
    def __init__(self, parent: _Optional[str] = ..., source: _Optional[_Union[_source_pb2.Source, _Mapping]] = ...) -> None: ...

class DeleteMuteConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteNotificationConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetBigQueryExportRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetMuteConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetNotificationConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetOrganizationSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetSourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GroupAssetsRequest(_message.Message):
    __slots__ = ("parent", "filter", "group_by", "compare_duration", "read_time", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    COMPARE_DURATION_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    group_by: str
    compare_duration: _duration_pb2.Duration
    read_time: _timestamp_pb2.Timestamp
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., group_by: _Optional[str] = ..., compare_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class GroupAssetsResponse(_message.Message):
    __slots__ = ("group_by_results", "read_time", "next_page_token", "total_size")
    GROUP_BY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    group_by_results: _containers.RepeatedCompositeFieldContainer[GroupResult]
    read_time: _timestamp_pb2.Timestamp
    next_page_token: str
    total_size: int
    def __init__(self, group_by_results: _Optional[_Iterable[_Union[GroupResult, _Mapping]]] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class GroupFindingsRequest(_message.Message):
    __slots__ = ("parent", "filter", "group_by", "read_time", "compare_duration", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPARE_DURATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    group_by: str
    read_time: _timestamp_pb2.Timestamp
    compare_duration: _duration_pb2.Duration
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., group_by: _Optional[str] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., compare_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class GroupFindingsResponse(_message.Message):
    __slots__ = ("group_by_results", "read_time", "next_page_token", "total_size")
    GROUP_BY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    group_by_results: _containers.RepeatedCompositeFieldContainer[GroupResult]
    read_time: _timestamp_pb2.Timestamp
    next_page_token: str
    total_size: int
    def __init__(self, group_by_results: _Optional[_Iterable[_Union[GroupResult, _Mapping]]] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class GroupResult(_message.Message):
    __slots__ = ("properties", "count")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.MessageMap[str, _struct_pb2.Value]
    count: int
    def __init__(self, properties: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., count: _Optional[int] = ...) -> None: ...

class ListDescendantSecurityHealthAnalyticsCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDescendantSecurityHealthAnalyticsCustomModulesResponse(_message.Message):
    __slots__ = ("security_health_analytics_custom_modules", "next_page_token")
    SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    security_health_analytics_custom_modules: _containers.RepeatedCompositeFieldContainer[_security_health_analytics_custom_module_pb2.SecurityHealthAnalyticsCustomModule]
    next_page_token: str
    def __init__(self, security_health_analytics_custom_modules: _Optional[_Iterable[_Union[_security_health_analytics_custom_module_pb2.SecurityHealthAnalyticsCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListValuedResourcesRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_token", "page_size", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_token: str
    page_size: int
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListValuedResourcesResponse(_message.Message):
    __slots__ = ("valued_resources", "next_page_token", "total_size")
    VALUED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    valued_resources: _containers.RepeatedCompositeFieldContainer[_valued_resource_pb2.ValuedResource]
    next_page_token: str
    total_size: int
    def __init__(self, valued_resources: _Optional[_Iterable[_Union[_valued_resource_pb2.ValuedResource, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class ListAttackPathsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListAttackPathsResponse(_message.Message):
    __slots__ = ("attack_paths", "next_page_token")
    ATTACK_PATHS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    attack_paths: _containers.RepeatedCompositeFieldContainer[_attack_path_pb2.AttackPath]
    next_page_token: str
    def __init__(self, attack_paths: _Optional[_Iterable[_Union[_attack_path_pb2.AttackPath, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSimulationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetValuedResourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListMuteConfigsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMuteConfigsResponse(_message.Message):
    __slots__ = ("mute_configs", "next_page_token")
    MUTE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    mute_configs: _containers.RepeatedCompositeFieldContainer[_mute_config_pb2.MuteConfig]
    next_page_token: str
    def __init__(self, mute_configs: _Optional[_Iterable[_Union[_mute_config_pb2.MuteConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListNotificationConfigsRequest(_message.Message):
    __slots__ = ("parent", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListNotificationConfigsResponse(_message.Message):
    __slots__ = ("notification_configs", "next_page_token")
    NOTIFICATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    notification_configs: _containers.RepeatedCompositeFieldContainer[_notification_config_pb2.NotificationConfig]
    next_page_token: str
    def __init__(self, notification_configs: _Optional[_Iterable[_Union[_notification_config_pb2.NotificationConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEffectiveSecurityHealthAnalyticsCustomModulesResponse(_message.Message):
    __slots__ = ("effective_security_health_analytics_custom_modules", "next_page_token")
    EFFECTIVE_SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    effective_security_health_analytics_custom_modules: _containers.RepeatedCompositeFieldContainer[_effective_security_health_analytics_custom_module_pb2.EffectiveSecurityHealthAnalyticsCustomModule]
    next_page_token: str
    def __init__(self, effective_security_health_analytics_custom_modules: _Optional[_Iterable[_Union[_effective_security_health_analytics_custom_module_pb2.EffectiveSecurityHealthAnalyticsCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListSecurityHealthAnalyticsCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSecurityHealthAnalyticsCustomModulesResponse(_message.Message):
    __slots__ = ("security_health_analytics_custom_modules", "next_page_token")
    SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    security_health_analytics_custom_modules: _containers.RepeatedCompositeFieldContainer[_security_health_analytics_custom_module_pb2.SecurityHealthAnalyticsCustomModule]
    next_page_token: str
    def __init__(self, security_health_analytics_custom_modules: _Optional[_Iterable[_Union[_security_health_analytics_custom_module_pb2.SecurityHealthAnalyticsCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListSourcesRequest(_message.Message):
    __slots__ = ("parent", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListSourcesResponse(_message.Message):
    __slots__ = ("sources", "next_page_token")
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[_source_pb2.Source]
    next_page_token: str
    def __init__(self, sources: _Optional[_Iterable[_Union[_source_pb2.Source, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListAssetsRequest(_message.Message):
    __slots__ = ("parent", "filter", "order_by", "read_time", "compare_duration", "field_mask", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPARE_DURATION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    order_by: str
    read_time: _timestamp_pb2.Timestamp
    compare_duration: _duration_pb2.Duration
    field_mask: _field_mask_pb2.FieldMask
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., compare_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListAssetsResponse(_message.Message):
    __slots__ = ("list_assets_results", "read_time", "next_page_token", "total_size")
    class ListAssetsResult(_message.Message):
        __slots__ = ("asset", "state_change")
        class StateChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNUSED: _ClassVar[ListAssetsResponse.ListAssetsResult.StateChange]
            ADDED: _ClassVar[ListAssetsResponse.ListAssetsResult.StateChange]
            REMOVED: _ClassVar[ListAssetsResponse.ListAssetsResult.StateChange]
            ACTIVE: _ClassVar[ListAssetsResponse.ListAssetsResult.StateChange]
        UNUSED: ListAssetsResponse.ListAssetsResult.StateChange
        ADDED: ListAssetsResponse.ListAssetsResult.StateChange
        REMOVED: ListAssetsResponse.ListAssetsResult.StateChange
        ACTIVE: ListAssetsResponse.ListAssetsResult.StateChange
        ASSET_FIELD_NUMBER: _ClassVar[int]
        STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        asset: _asset_pb2.Asset
        state_change: ListAssetsResponse.ListAssetsResult.StateChange
        def __init__(self, asset: _Optional[_Union[_asset_pb2.Asset, _Mapping]] = ..., state_change: _Optional[_Union[ListAssetsResponse.ListAssetsResult.StateChange, str]] = ...) -> None: ...
    LIST_ASSETS_RESULTS_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    list_assets_results: _containers.RepeatedCompositeFieldContainer[ListAssetsResponse.ListAssetsResult]
    read_time: _timestamp_pb2.Timestamp
    next_page_token: str
    total_size: int
    def __init__(self, list_assets_results: _Optional[_Iterable[_Union[ListAssetsResponse.ListAssetsResult, _Mapping]]] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class ListFindingsRequest(_message.Message):
    __slots__ = ("parent", "filter", "order_by", "read_time", "compare_duration", "field_mask", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPARE_DURATION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    order_by: str
    read_time: _timestamp_pb2.Timestamp
    compare_duration: _duration_pb2.Duration
    field_mask: _field_mask_pb2.FieldMask
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., compare_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListFindingsResponse(_message.Message):
    __slots__ = ("list_findings_results", "read_time", "next_page_token", "total_size")
    class ListFindingsResult(_message.Message):
        __slots__ = ("finding", "state_change", "resource")
        class StateChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNUSED: _ClassVar[ListFindingsResponse.ListFindingsResult.StateChange]
            CHANGED: _ClassVar[ListFindingsResponse.ListFindingsResult.StateChange]
            UNCHANGED: _ClassVar[ListFindingsResponse.ListFindingsResult.StateChange]
            ADDED: _ClassVar[ListFindingsResponse.ListFindingsResult.StateChange]
            REMOVED: _ClassVar[ListFindingsResponse.ListFindingsResult.StateChange]
        UNUSED: ListFindingsResponse.ListFindingsResult.StateChange
        CHANGED: ListFindingsResponse.ListFindingsResult.StateChange
        UNCHANGED: ListFindingsResponse.ListFindingsResult.StateChange
        ADDED: ListFindingsResponse.ListFindingsResult.StateChange
        REMOVED: ListFindingsResponse.ListFindingsResult.StateChange
        class Resource(_message.Message):
            __slots__ = ("name", "display_name", "type", "project_name", "project_display_name", "parent_name", "parent_display_name", "folders", "cloud_provider", "organization", "service", "location", "aws_metadata", "azure_metadata", "resource_path", "resource_path_string")
            NAME_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
            PROJECT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            PARENT_NAME_FIELD_NUMBER: _ClassVar[int]
            PARENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            FOLDERS_FIELD_NUMBER: _ClassVar[int]
            CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
            ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
            SERVICE_FIELD_NUMBER: _ClassVar[int]
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            AWS_METADATA_FIELD_NUMBER: _ClassVar[int]
            AZURE_METADATA_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_PATH_STRING_FIELD_NUMBER: _ClassVar[int]
            name: str
            display_name: str
            type: str
            project_name: str
            project_display_name: str
            parent_name: str
            parent_display_name: str
            folders: _containers.RepeatedCompositeFieldContainer[_folder_pb2.Folder]
            cloud_provider: _resource_pb2_1.CloudProvider
            organization: str
            service: str
            location: str
            aws_metadata: _resource_pb2_1.AwsMetadata
            azure_metadata: _resource_pb2_1.AzureMetadata
            resource_path: _resource_pb2_1.ResourcePath
            resource_path_string: str
            def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., type: _Optional[str] = ..., project_name: _Optional[str] = ..., project_display_name: _Optional[str] = ..., parent_name: _Optional[str] = ..., parent_display_name: _Optional[str] = ..., folders: _Optional[_Iterable[_Union[_folder_pb2.Folder, _Mapping]]] = ..., cloud_provider: _Optional[_Union[_resource_pb2_1.CloudProvider, str]] = ..., organization: _Optional[str] = ..., service: _Optional[str] = ..., location: _Optional[str] = ..., aws_metadata: _Optional[_Union[_resource_pb2_1.AwsMetadata, _Mapping]] = ..., azure_metadata: _Optional[_Union[_resource_pb2_1.AzureMetadata, _Mapping]] = ..., resource_path: _Optional[_Union[_resource_pb2_1.ResourcePath, _Mapping]] = ..., resource_path_string: _Optional[str] = ...) -> None: ...
        FINDING_FIELD_NUMBER: _ClassVar[int]
        STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        finding: _finding_pb2.Finding
        state_change: ListFindingsResponse.ListFindingsResult.StateChange
        resource: ListFindingsResponse.ListFindingsResult.Resource
        def __init__(self, finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]] = ..., state_change: _Optional[_Union[ListFindingsResponse.ListFindingsResult.StateChange, str]] = ..., resource: _Optional[_Union[ListFindingsResponse.ListFindingsResult.Resource, _Mapping]] = ...) -> None: ...
    LIST_FINDINGS_RESULTS_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    list_findings_results: _containers.RepeatedCompositeFieldContainer[ListFindingsResponse.ListFindingsResult]
    read_time: _timestamp_pb2.Timestamp
    next_page_token: str
    total_size: int
    def __init__(self, list_findings_results: _Optional[_Iterable[_Union[ListFindingsResponse.ListFindingsResult, _Mapping]]] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class SetFindingStateRequest(_message.Message):
    __slots__ = ("name", "state", "start_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: _finding_pb2.Finding.State
    start_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[_finding_pb2.Finding.State, str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SetMuteRequest(_message.Message):
    __slots__ = ("name", "mute")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIELD_NUMBER: _ClassVar[int]
    name: str
    mute: _finding_pb2.Finding.Mute
    def __init__(self, name: _Optional[str] = ..., mute: _Optional[_Union[_finding_pb2.Finding.Mute, str]] = ...) -> None: ...

class RunAssetDiscoveryRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class SimulateSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("parent", "custom_config", "resource")
    class SimulatedResource(_message.Message):
        __slots__ = ("resource_type", "resource_data", "iam_policy_data")
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_DATA_FIELD_NUMBER: _ClassVar[int]
        IAM_POLICY_DATA_FIELD_NUMBER: _ClassVar[int]
        resource_type: str
        resource_data: _struct_pb2.Struct
        iam_policy_data: _policy_pb2.Policy
        def __init__(self, resource_type: _Optional[str] = ..., resource_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., iam_policy_data: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    custom_config: _security_health_analytics_custom_config_pb2.CustomConfig
    resource: SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource
    def __init__(self, parent: _Optional[str] = ..., custom_config: _Optional[_Union[_security_health_analytics_custom_config_pb2.CustomConfig, _Mapping]] = ..., resource: _Optional[_Union[SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource, _Mapping]] = ...) -> None: ...

class SimulateSecurityHealthAnalyticsCustomModuleResponse(_message.Message):
    __slots__ = ("result",)
    class SimulatedResult(_message.Message):
        __slots__ = ("finding", "no_violation", "error")
        FINDING_FIELD_NUMBER: _ClassVar[int]
        NO_VIOLATION_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        finding: _finding_pb2.Finding
        no_violation: _empty_pb2.Empty
        error: _status_pb2.Status
        def __init__(self, finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]] = ..., no_violation: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: SimulateSecurityHealthAnalyticsCustomModuleResponse.SimulatedResult
    def __init__(self, result: _Optional[_Union[SimulateSecurityHealthAnalyticsCustomModuleResponse.SimulatedResult, _Mapping]] = ...) -> None: ...

class UpdateExternalSystemRequest(_message.Message):
    __slots__ = ("external_system", "update_mask")
    EXTERNAL_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    external_system: _external_system_pb2.ExternalSystem
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, external_system: _Optional[_Union[_external_system_pb2.ExternalSystem, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateFindingRequest(_message.Message):
    __slots__ = ("finding", "update_mask")
    FINDING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    finding: _finding_pb2.Finding
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateMuteConfigRequest(_message.Message):
    __slots__ = ("mute_config", "update_mask")
    MUTE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    mute_config: _mute_config_pb2.MuteConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, mute_config: _Optional[_Union[_mute_config_pb2.MuteConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateNotificationConfigRequest(_message.Message):
    __slots__ = ("notification_config", "update_mask")
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    notification_config: _notification_config_pb2.NotificationConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, notification_config: _Optional[_Union[_notification_config_pb2.NotificationConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateOrganizationSettingsRequest(_message.Message):
    __slots__ = ("organization_settings", "update_mask")
    ORGANIZATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    organization_settings: _organization_settings_pb2.OrganizationSettings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, organization_settings: _Optional[_Union[_organization_settings_pb2.OrganizationSettings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("security_health_analytics_custom_module", "update_mask")
    SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    security_health_analytics_custom_module: _security_health_analytics_custom_module_pb2.SecurityHealthAnalyticsCustomModule
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, security_health_analytics_custom_module: _Optional[_Union[_security_health_analytics_custom_module_pb2.SecurityHealthAnalyticsCustomModule, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSourceRequest(_message.Message):
    __slots__ = ("source", "update_mask")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    source: _source_pb2.Source
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, source: _Optional[_Union[_source_pb2.Source, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSecurityMarksRequest(_message.Message):
    __slots__ = ("security_marks", "update_mask", "start_time")
    SECURITY_MARKS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    security_marks: _security_marks_pb2.SecurityMarks
    update_mask: _field_mask_pb2.FieldMask
    start_time: _timestamp_pb2.Timestamp
    def __init__(self, security_marks: _Optional[_Union[_security_marks_pb2.SecurityMarks, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateBigQueryExportRequest(_message.Message):
    __slots__ = ("parent", "big_query_export", "big_query_export_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_EXPORT_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    big_query_export: _bigquery_export_pb2.BigQueryExport
    big_query_export_id: str
    def __init__(self, parent: _Optional[str] = ..., big_query_export: _Optional[_Union[_bigquery_export_pb2.BigQueryExport, _Mapping]] = ..., big_query_export_id: _Optional[str] = ...) -> None: ...

class UpdateBigQueryExportRequest(_message.Message):
    __slots__ = ("big_query_export", "update_mask")
    BIG_QUERY_EXPORT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    big_query_export: _bigquery_export_pb2.BigQueryExport
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, big_query_export: _Optional[_Union[_bigquery_export_pb2.BigQueryExport, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListBigQueryExportsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListBigQueryExportsResponse(_message.Message):
    __slots__ = ("big_query_exports", "next_page_token")
    BIG_QUERY_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    big_query_exports: _containers.RepeatedCompositeFieldContainer[_bigquery_export_pb2.BigQueryExport]
    next_page_token: str
    def __init__(self, big_query_exports: _Optional[_Iterable[_Union[_bigquery_export_pb2.BigQueryExport, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteBigQueryExportRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("parent", "event_threat_detection_custom_module")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_THREAT_DETECTION_CUSTOM_MODULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    event_threat_detection_custom_module: _event_threat_detection_custom_module_pb2.EventThreatDetectionCustomModule
    def __init__(self, parent: _Optional[str] = ..., event_threat_detection_custom_module: _Optional[_Union[_event_threat_detection_custom_module_pb2.EventThreatDetectionCustomModule, _Mapping]] = ...) -> None: ...

class ValidateEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("parent", "raw_text", "type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RAW_TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    raw_text: str
    type: str
    def __init__(self, parent: _Optional[str] = ..., raw_text: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class ValidateEventThreatDetectionCustomModuleResponse(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _event_threat_detection_custom_module_validation_errors_pb2.CustomModuleValidationErrors
    def __init__(self, errors: _Optional[_Union[_event_threat_detection_custom_module_validation_errors_pb2.CustomModuleValidationErrors, _Mapping]] = ...) -> None: ...

class DeleteEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDescendantEventThreatDetectionCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListDescendantEventThreatDetectionCustomModulesResponse(_message.Message):
    __slots__ = ("event_threat_detection_custom_modules", "next_page_token")
    EVENT_THREAT_DETECTION_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    event_threat_detection_custom_modules: _containers.RepeatedCompositeFieldContainer[_event_threat_detection_custom_module_pb2.EventThreatDetectionCustomModule]
    next_page_token: str
    def __init__(self, event_threat_detection_custom_modules: _Optional[_Iterable[_Union[_event_threat_detection_custom_module_pb2.EventThreatDetectionCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListEventThreatDetectionCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListEventThreatDetectionCustomModulesResponse(_message.Message):
    __slots__ = ("event_threat_detection_custom_modules", "next_page_token")
    EVENT_THREAT_DETECTION_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    event_threat_detection_custom_modules: _containers.RepeatedCompositeFieldContainer[_event_threat_detection_custom_module_pb2.EventThreatDetectionCustomModule]
    next_page_token: str
    def __init__(self, event_threat_detection_custom_modules: _Optional[_Iterable[_Union[_event_threat_detection_custom_module_pb2.EventThreatDetectionCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("event_threat_detection_custom_module", "update_mask")
    EVENT_THREAT_DETECTION_CUSTOM_MODULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    event_threat_detection_custom_module: _event_threat_detection_custom_module_pb2.EventThreatDetectionCustomModule
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, event_threat_detection_custom_module: _Optional[_Union[_event_threat_detection_custom_module_pb2.EventThreatDetectionCustomModule, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetEffectiveEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListEffectiveEventThreatDetectionCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListEffectiveEventThreatDetectionCustomModulesResponse(_message.Message):
    __slots__ = ("effective_event_threat_detection_custom_modules", "next_page_token")
    EFFECTIVE_EVENT_THREAT_DETECTION_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    effective_event_threat_detection_custom_modules: _containers.RepeatedCompositeFieldContainer[_effective_event_threat_detection_custom_module_pb2.EffectiveEventThreatDetectionCustomModule]
    next_page_token: str
    def __init__(self, effective_event_threat_detection_custom_modules: _Optional[_Iterable[_Union[_effective_event_threat_detection_custom_module_pb2.EffectiveEventThreatDetectionCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
