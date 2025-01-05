from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.cloud.securitycenter.v2 import attack_path_pb2 as _attack_path_pb2
from google.cloud.securitycenter.v2 import bigquery_export_pb2 as _bigquery_export_pb2
from google.cloud.securitycenter.v2 import external_system_pb2 as _external_system_pb2
from google.cloud.securitycenter.v2 import finding_pb2 as _finding_pb2
from google.cloud.securitycenter.v2 import mute_config_pb2 as _mute_config_pb2
from google.cloud.securitycenter.v2 import notification_config_pb2 as _notification_config_pb2
from google.cloud.securitycenter.v2 import resource_pb2 as _resource_pb2_1
from google.cloud.securitycenter.v2 import resource_value_config_pb2 as _resource_value_config_pb2
from google.cloud.securitycenter.v2 import security_marks_pb2 as _security_marks_pb2
from google.cloud.securitycenter.v2 import simulation_pb2 as _simulation_pb2
from google.cloud.securitycenter.v2 import source_pb2 as _source_pb2
from google.cloud.securitycenter.v2 import valued_resource_pb2 as _valued_resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BatchCreateResourceValueConfigsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateResourceValueConfigRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateResourceValueConfigRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateResourceValueConfigsResponse(_message.Message):
    __slots__ = ('resource_value_configs',)
    RESOURCE_VALUE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    resource_value_configs: _containers.RepeatedCompositeFieldContainer[_resource_value_config_pb2.ResourceValueConfig]

    def __init__(self, resource_value_configs: _Optional[_Iterable[_Union[_resource_value_config_pb2.ResourceValueConfig, _Mapping]]]=...) -> None:
        ...

class BulkMuteFindingsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'mute_state')

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
    MUTE_STATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    mute_state: BulkMuteFindingsRequest.MuteState

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., mute_state: _Optional[_Union[BulkMuteFindingsRequest.MuteState, str]]=...) -> None:
        ...

class BulkMuteFindingsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateBigQueryExportRequest(_message.Message):
    __slots__ = ('parent', 'big_query_export', 'big_query_export_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_EXPORT_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    big_query_export: _bigquery_export_pb2.BigQueryExport
    big_query_export_id: str

    def __init__(self, parent: _Optional[str]=..., big_query_export: _Optional[_Union[_bigquery_export_pb2.BigQueryExport, _Mapping]]=..., big_query_export_id: _Optional[str]=...) -> None:
        ...

class CreateFindingRequest(_message.Message):
    __slots__ = ('parent', 'finding_id', 'finding')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    FINDING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    finding_id: str
    finding: _finding_pb2.Finding

    def __init__(self, parent: _Optional[str]=..., finding_id: _Optional[str]=..., finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]]=...) -> None:
        ...

class CreateMuteConfigRequest(_message.Message):
    __slots__ = ('parent', 'mute_config', 'mute_config_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MUTE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MUTE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    mute_config: _mute_config_pb2.MuteConfig
    mute_config_id: str

    def __init__(self, parent: _Optional[str]=..., mute_config: _Optional[_Union[_mute_config_pb2.MuteConfig, _Mapping]]=..., mute_config_id: _Optional[str]=...) -> None:
        ...

class CreateNotificationConfigRequest(_message.Message):
    __slots__ = ('parent', 'config_id', 'notification_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    config_id: str
    notification_config: _notification_config_pb2.NotificationConfig

    def __init__(self, parent: _Optional[str]=..., config_id: _Optional[str]=..., notification_config: _Optional[_Union[_notification_config_pb2.NotificationConfig, _Mapping]]=...) -> None:
        ...

class CreateResourceValueConfigRequest(_message.Message):
    __slots__ = ('parent', 'resource_value_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VALUE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    resource_value_config: _resource_value_config_pb2.ResourceValueConfig

    def __init__(self, parent: _Optional[str]=..., resource_value_config: _Optional[_Union[_resource_value_config_pb2.ResourceValueConfig, _Mapping]]=...) -> None:
        ...

class CreateSourceRequest(_message.Message):
    __slots__ = ('parent', 'source')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source: _source_pb2.Source

    def __init__(self, parent: _Optional[str]=..., source: _Optional[_Union[_source_pb2.Source, _Mapping]]=...) -> None:
        ...

class DeleteBigQueryExportRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteMuteConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteNotificationConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteResourceValueConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetBigQueryExportRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetMuteConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetNotificationConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetResourceValueConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetSourceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GroupFindingsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'group_by', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    group_by: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., group_by: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class GroupFindingsResponse(_message.Message):
    __slots__ = ('group_by_results', 'next_page_token', 'total_size')
    GROUP_BY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    group_by_results: _containers.RepeatedCompositeFieldContainer[GroupResult]
    next_page_token: str
    total_size: int

    def __init__(self, group_by_results: _Optional[_Iterable[_Union[GroupResult, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class GroupResult(_message.Message):
    __slots__ = ('properties', 'count')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.MessageMap[str, _struct_pb2.Value]
    count: int

    def __init__(self, properties: _Optional[_Mapping[str, _struct_pb2.Value]]=..., count: _Optional[int]=...) -> None:
        ...

class ListAttackPathsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListAttackPathsResponse(_message.Message):
    __slots__ = ('attack_paths', 'next_page_token')
    ATTACK_PATHS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    attack_paths: _containers.RepeatedCompositeFieldContainer[_attack_path_pb2.AttackPath]
    next_page_token: str

    def __init__(self, attack_paths: _Optional[_Iterable[_Union[_attack_path_pb2.AttackPath, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetSimulationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetValuedResourceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBigQueryExportsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBigQueryExportsResponse(_message.Message):
    __slots__ = ('big_query_exports', 'next_page_token')
    BIG_QUERY_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    big_query_exports: _containers.RepeatedCompositeFieldContainer[_bigquery_export_pb2.BigQueryExport]
    next_page_token: str

    def __init__(self, big_query_exports: _Optional[_Iterable[_Union[_bigquery_export_pb2.BigQueryExport, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListFindingsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'order_by', 'field_mask', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    order_by: str
    field_mask: _field_mask_pb2.FieldMask
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListFindingsResponse(_message.Message):
    __slots__ = ('list_findings_results', 'next_page_token', 'total_size')

    class ListFindingsResult(_message.Message):
        __slots__ = ('finding', 'resource')

        class Resource(_message.Message):
            __slots__ = ('name', 'display_name', 'type', 'cloud_provider', 'service', 'location', 'gcp_metadata', 'aws_metadata', 'azure_metadata', 'resource_path', 'resource_path_string')
            NAME_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
            SERVICE_FIELD_NUMBER: _ClassVar[int]
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            GCP_METADATA_FIELD_NUMBER: _ClassVar[int]
            AWS_METADATA_FIELD_NUMBER: _ClassVar[int]
            AZURE_METADATA_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_PATH_STRING_FIELD_NUMBER: _ClassVar[int]
            name: str
            display_name: str
            type: str
            cloud_provider: _resource_pb2_1.CloudProvider
            service: str
            location: str
            gcp_metadata: _resource_pb2_1.GcpMetadata
            aws_metadata: _resource_pb2_1.AwsMetadata
            azure_metadata: _resource_pb2_1.AzureMetadata
            resource_path: _resource_pb2_1.ResourcePath
            resource_path_string: str

            def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., type: _Optional[str]=..., cloud_provider: _Optional[_Union[_resource_pb2_1.CloudProvider, str]]=..., service: _Optional[str]=..., location: _Optional[str]=..., gcp_metadata: _Optional[_Union[_resource_pb2_1.GcpMetadata, _Mapping]]=..., aws_metadata: _Optional[_Union[_resource_pb2_1.AwsMetadata, _Mapping]]=..., azure_metadata: _Optional[_Union[_resource_pb2_1.AzureMetadata, _Mapping]]=..., resource_path: _Optional[_Union[_resource_pb2_1.ResourcePath, _Mapping]]=..., resource_path_string: _Optional[str]=...) -> None:
                ...
        FINDING_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        finding: _finding_pb2.Finding
        resource: ListFindingsResponse.ListFindingsResult.Resource

        def __init__(self, finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]]=..., resource: _Optional[_Union[ListFindingsResponse.ListFindingsResult.Resource, _Mapping]]=...) -> None:
            ...
    LIST_FINDINGS_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    list_findings_results: _containers.RepeatedCompositeFieldContainer[ListFindingsResponse.ListFindingsResult]
    next_page_token: str
    total_size: int

    def __init__(self, list_findings_results: _Optional[_Iterable[_Union[ListFindingsResponse.ListFindingsResult, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class ListMuteConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMuteConfigsResponse(_message.Message):
    __slots__ = ('mute_configs', 'next_page_token')
    MUTE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    mute_configs: _containers.RepeatedCompositeFieldContainer[_mute_config_pb2.MuteConfig]
    next_page_token: str

    def __init__(self, mute_configs: _Optional[_Iterable[_Union[_mute_config_pb2.MuteConfig, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListNotificationConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListNotificationConfigsResponse(_message.Message):
    __slots__ = ('notification_configs', 'next_page_token')
    NOTIFICATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    notification_configs: _containers.RepeatedCompositeFieldContainer[_notification_config_pb2.NotificationConfig]
    next_page_token: str

    def __init__(self, notification_configs: _Optional[_Iterable[_Union[_notification_config_pb2.NotificationConfig, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListResourceValueConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListResourceValueConfigsResponse(_message.Message):
    __slots__ = ('resource_value_configs', 'next_page_token')
    RESOURCE_VALUE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource_value_configs: _containers.RepeatedCompositeFieldContainer[_resource_value_config_pb2.ResourceValueConfig]
    next_page_token: str

    def __init__(self, resource_value_configs: _Optional[_Iterable[_Union[_resource_value_config_pb2.ResourceValueConfig, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListSourcesRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListSourcesResponse(_message.Message):
    __slots__ = ('sources', 'next_page_token')
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[_source_pb2.Source]
    next_page_token: str

    def __init__(self, sources: _Optional[_Iterable[_Union[_source_pb2.Source, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListValuedResourcesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_token', 'page_size', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListValuedResourcesResponse(_message.Message):
    __slots__ = ('valued_resources', 'next_page_token', 'total_size')
    VALUED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    valued_resources: _containers.RepeatedCompositeFieldContainer[_valued_resource_pb2.ValuedResource]
    next_page_token: str
    total_size: int

    def __init__(self, valued_resources: _Optional[_Iterable[_Union[_valued_resource_pb2.ValuedResource, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class SetFindingStateRequest(_message.Message):
    __slots__ = ('name', 'state')
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: _finding_pb2.Finding.State

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[_finding_pb2.Finding.State, str]]=...) -> None:
        ...

class SetMuteRequest(_message.Message):
    __slots__ = ('name', 'mute')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIELD_NUMBER: _ClassVar[int]
    name: str
    mute: _finding_pb2.Finding.Mute

    def __init__(self, name: _Optional[str]=..., mute: _Optional[_Union[_finding_pb2.Finding.Mute, str]]=...) -> None:
        ...

class UpdateBigQueryExportRequest(_message.Message):
    __slots__ = ('big_query_export', 'update_mask')
    BIG_QUERY_EXPORT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    big_query_export: _bigquery_export_pb2.BigQueryExport
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, big_query_export: _Optional[_Union[_bigquery_export_pb2.BigQueryExport, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateExternalSystemRequest(_message.Message):
    __slots__ = ('external_system', 'update_mask')
    EXTERNAL_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    external_system: _external_system_pb2.ExternalSystem
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, external_system: _Optional[_Union[_external_system_pb2.ExternalSystem, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateFindingRequest(_message.Message):
    __slots__ = ('finding', 'update_mask')
    FINDING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    finding: _finding_pb2.Finding
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateMuteConfigRequest(_message.Message):
    __slots__ = ('mute_config', 'update_mask')
    MUTE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    mute_config: _mute_config_pb2.MuteConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, mute_config: _Optional[_Union[_mute_config_pb2.MuteConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateNotificationConfigRequest(_message.Message):
    __slots__ = ('notification_config', 'update_mask')
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    notification_config: _notification_config_pb2.NotificationConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, notification_config: _Optional[_Union[_notification_config_pb2.NotificationConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateResourceValueConfigRequest(_message.Message):
    __slots__ = ('resource_value_config', 'update_mask')
    RESOURCE_VALUE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    resource_value_config: _resource_value_config_pb2.ResourceValueConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, resource_value_config: _Optional[_Union[_resource_value_config_pb2.ResourceValueConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateSecurityMarksRequest(_message.Message):
    __slots__ = ('security_marks', 'update_mask')
    SECURITY_MARKS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    security_marks: _security_marks_pb2.SecurityMarks
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, security_marks: _Optional[_Union[_security_marks_pb2.SecurityMarks, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateSourceRequest(_message.Message):
    __slots__ = ('source', 'update_mask')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    source: _source_pb2.Source
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, source: _Optional[_Union[_source_pb2.Source, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...