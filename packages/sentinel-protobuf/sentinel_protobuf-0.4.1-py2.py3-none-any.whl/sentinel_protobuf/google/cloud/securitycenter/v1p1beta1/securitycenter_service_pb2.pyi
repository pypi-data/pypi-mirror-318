from google.cloud.securitycenter.v1p1beta1 import notification_message_pb2 as _notification_message_pb2
from google.cloud.securitycenter.v1p1beta1 import run_asset_discovery_response_pb2 as _run_asset_discovery_response_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.v1p1beta1 import asset_pb2 as _asset_pb2
from google.cloud.securitycenter.v1p1beta1 import finding_pb2 as _finding_pb2
from google.cloud.securitycenter.v1p1beta1 import folder_pb2 as _folder_pb2
from google.cloud.securitycenter.v1p1beta1 import notification_config_pb2 as _notification_config_pb2
from google.cloud.securitycenter.v1p1beta1 import organization_settings_pb2 as _organization_settings_pb2
from google.cloud.securitycenter.v1p1beta1 import security_marks_pb2 as _security_marks_pb2
from google.cloud.securitycenter.v1p1beta1 import source_pb2 as _source_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.cloud.securitycenter.v1p1beta1.notification_message_pb2 import NotificationMessage as NotificationMessage
from google.cloud.securitycenter.v1p1beta1.run_asset_discovery_response_pb2 import RunAssetDiscoveryResponse as RunAssetDiscoveryResponse
DESCRIPTOR: _descriptor.FileDescriptor

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

class CreateSourceRequest(_message.Message):
    __slots__ = ('parent', 'source')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source: _source_pb2.Source

    def __init__(self, parent: _Optional[str]=..., source: _Optional[_Union[_source_pb2.Source, _Mapping]]=...) -> None:
        ...

class DeleteNotificationConfigRequest(_message.Message):
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

class GetOrganizationSettingsRequest(_message.Message):
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

class GroupAssetsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'group_by', 'compare_duration', 'read_time', 'page_token', 'page_size')
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

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., group_by: _Optional[str]=..., compare_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class GroupAssetsResponse(_message.Message):
    __slots__ = ('group_by_results', 'read_time', 'next_page_token', 'total_size')
    GROUP_BY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    group_by_results: _containers.RepeatedCompositeFieldContainer[GroupResult]
    read_time: _timestamp_pb2.Timestamp
    next_page_token: str
    total_size: int

    def __init__(self, group_by_results: _Optional[_Iterable[_Union[GroupResult, _Mapping]]]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class GroupFindingsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'group_by', 'read_time', 'compare_duration', 'page_token', 'page_size')
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

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., group_by: _Optional[str]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., compare_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class GroupFindingsResponse(_message.Message):
    __slots__ = ('group_by_results', 'read_time', 'next_page_token', 'total_size')
    GROUP_BY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    group_by_results: _containers.RepeatedCompositeFieldContainer[GroupResult]
    read_time: _timestamp_pb2.Timestamp
    next_page_token: str
    total_size: int

    def __init__(self, group_by_results: _Optional[_Iterable[_Union[GroupResult, _Mapping]]]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
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

class ListAssetsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'order_by', 'read_time', 'compare_duration', 'field_mask', 'page_token', 'page_size')
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

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., compare_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListAssetsResponse(_message.Message):
    __slots__ = ('list_assets_results', 'read_time', 'next_page_token', 'total_size')

    class ListAssetsResult(_message.Message):
        __slots__ = ('asset', 'state_change')

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

        def __init__(self, asset: _Optional[_Union[_asset_pb2.Asset, _Mapping]]=..., state_change: _Optional[_Union[ListAssetsResponse.ListAssetsResult.StateChange, str]]=...) -> None:
            ...
    LIST_ASSETS_RESULTS_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    list_assets_results: _containers.RepeatedCompositeFieldContainer[ListAssetsResponse.ListAssetsResult]
    read_time: _timestamp_pb2.Timestamp
    next_page_token: str
    total_size: int

    def __init__(self, list_assets_results: _Optional[_Iterable[_Union[ListAssetsResponse.ListAssetsResult, _Mapping]]]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class ListFindingsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'order_by', 'read_time', 'compare_duration', 'field_mask', 'page_token', 'page_size')
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

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., compare_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListFindingsResponse(_message.Message):
    __slots__ = ('list_findings_results', 'read_time', 'next_page_token', 'total_size')

    class ListFindingsResult(_message.Message):
        __slots__ = ('finding', 'state_change', 'resource')

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
            __slots__ = ('name', 'project_name', 'project_display_name', 'parent_name', 'parent_display_name', 'folders')
            NAME_FIELD_NUMBER: _ClassVar[int]
            PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
            PROJECT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            PARENT_NAME_FIELD_NUMBER: _ClassVar[int]
            PARENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            FOLDERS_FIELD_NUMBER: _ClassVar[int]
            name: str
            project_name: str
            project_display_name: str
            parent_name: str
            parent_display_name: str
            folders: _containers.RepeatedCompositeFieldContainer[_folder_pb2.Folder]

            def __init__(self, name: _Optional[str]=..., project_name: _Optional[str]=..., project_display_name: _Optional[str]=..., parent_name: _Optional[str]=..., parent_display_name: _Optional[str]=..., folders: _Optional[_Iterable[_Union[_folder_pb2.Folder, _Mapping]]]=...) -> None:
                ...
        FINDING_FIELD_NUMBER: _ClassVar[int]
        STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        finding: _finding_pb2.Finding
        state_change: ListFindingsResponse.ListFindingsResult.StateChange
        resource: ListFindingsResponse.ListFindingsResult.Resource

        def __init__(self, finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]]=..., state_change: _Optional[_Union[ListFindingsResponse.ListFindingsResult.StateChange, str]]=..., resource: _Optional[_Union[ListFindingsResponse.ListFindingsResult.Resource, _Mapping]]=...) -> None:
            ...
    LIST_FINDINGS_RESULTS_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    list_findings_results: _containers.RepeatedCompositeFieldContainer[ListFindingsResponse.ListFindingsResult]
    read_time: _timestamp_pb2.Timestamp
    next_page_token: str
    total_size: int

    def __init__(self, list_findings_results: _Optional[_Iterable[_Union[ListFindingsResponse.ListFindingsResult, _Mapping]]]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class SetFindingStateRequest(_message.Message):
    __slots__ = ('name', 'state', 'start_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: _finding_pb2.Finding.State
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[_finding_pb2.Finding.State, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RunAssetDiscoveryRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class UpdateFindingRequest(_message.Message):
    __slots__ = ('finding', 'update_mask')
    FINDING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    finding: _finding_pb2.Finding
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateNotificationConfigRequest(_message.Message):
    __slots__ = ('notification_config', 'update_mask')
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    notification_config: _notification_config_pb2.NotificationConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, notification_config: _Optional[_Union[_notification_config_pb2.NotificationConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateOrganizationSettingsRequest(_message.Message):
    __slots__ = ('organization_settings', 'update_mask')
    ORGANIZATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    organization_settings: _organization_settings_pb2.OrganizationSettings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, organization_settings: _Optional[_Union[_organization_settings_pb2.OrganizationSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateSourceRequest(_message.Message):
    __slots__ = ('source', 'update_mask')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    source: _source_pb2.Source
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, source: _Optional[_Union[_source_pb2.Source, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateSecurityMarksRequest(_message.Message):
    __slots__ = ('security_marks', 'update_mask', 'start_time')
    SECURITY_MARKS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    security_marks: _security_marks_pb2.SecurityMarks
    update_mask: _field_mask_pb2.FieldMask
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, security_marks: _Optional[_Union[_security_marks_pb2.SecurityMarks, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...