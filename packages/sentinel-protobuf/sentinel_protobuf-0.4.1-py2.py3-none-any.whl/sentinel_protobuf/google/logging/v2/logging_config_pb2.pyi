from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_STATE_UNSPECIFIED: _ClassVar[OperationState]
    OPERATION_STATE_SCHEDULED: _ClassVar[OperationState]
    OPERATION_STATE_WAITING_FOR_PERMISSIONS: _ClassVar[OperationState]
    OPERATION_STATE_RUNNING: _ClassVar[OperationState]
    OPERATION_STATE_SUCCEEDED: _ClassVar[OperationState]
    OPERATION_STATE_FAILED: _ClassVar[OperationState]
    OPERATION_STATE_CANCELLED: _ClassVar[OperationState]

class LifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[LifecycleState]
    ACTIVE: _ClassVar[LifecycleState]
    DELETE_REQUESTED: _ClassVar[LifecycleState]
    UPDATING: _ClassVar[LifecycleState]
    CREATING: _ClassVar[LifecycleState]
    FAILED: _ClassVar[LifecycleState]

class IndexType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INDEX_TYPE_UNSPECIFIED: _ClassVar[IndexType]
    INDEX_TYPE_STRING: _ClassVar[IndexType]
    INDEX_TYPE_INTEGER: _ClassVar[IndexType]
OPERATION_STATE_UNSPECIFIED: OperationState
OPERATION_STATE_SCHEDULED: OperationState
OPERATION_STATE_WAITING_FOR_PERMISSIONS: OperationState
OPERATION_STATE_RUNNING: OperationState
OPERATION_STATE_SUCCEEDED: OperationState
OPERATION_STATE_FAILED: OperationState
OPERATION_STATE_CANCELLED: OperationState
LIFECYCLE_STATE_UNSPECIFIED: LifecycleState
ACTIVE: LifecycleState
DELETE_REQUESTED: LifecycleState
UPDATING: LifecycleState
CREATING: LifecycleState
FAILED: LifecycleState
INDEX_TYPE_UNSPECIFIED: IndexType
INDEX_TYPE_STRING: IndexType
INDEX_TYPE_INTEGER: IndexType

class IndexConfig(_message.Message):
    __slots__ = ('field_path', 'type', 'create_time')
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    field_path: str
    type: IndexType
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, field_path: _Optional[str]=..., type: _Optional[_Union[IndexType, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class LogBucket(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'retention_days', 'locked', 'lifecycle_state', 'analytics_enabled', 'restricted_fields', 'index_configs', 'cmek_settings')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    CMEK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    retention_days: int
    locked: bool
    lifecycle_state: LifecycleState
    analytics_enabled: bool
    restricted_fields: _containers.RepeatedScalarFieldContainer[str]
    index_configs: _containers.RepeatedCompositeFieldContainer[IndexConfig]
    cmek_settings: CmekSettings

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., retention_days: _Optional[int]=..., locked: bool=..., lifecycle_state: _Optional[_Union[LifecycleState, str]]=..., analytics_enabled: bool=..., restricted_fields: _Optional[_Iterable[str]]=..., index_configs: _Optional[_Iterable[_Union[IndexConfig, _Mapping]]]=..., cmek_settings: _Optional[_Union[CmekSettings, _Mapping]]=...) -> None:
        ...

class LogView(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'filter')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    filter: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., filter: _Optional[str]=...) -> None:
        ...

class LogSink(_message.Message):
    __slots__ = ('name', 'destination', 'filter', 'description', 'disabled', 'exclusions', 'output_version_format', 'writer_identity', 'include_children', 'bigquery_options', 'create_time', 'update_time')

    class VersionFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERSION_FORMAT_UNSPECIFIED: _ClassVar[LogSink.VersionFormat]
        V2: _ClassVar[LogSink.VersionFormat]
        V1: _ClassVar[LogSink.VersionFormat]
    VERSION_FORMAT_UNSPECIFIED: LogSink.VersionFormat
    V2: LogSink.VersionFormat
    V1: LogSink.VersionFormat
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VERSION_FORMAT_FIELD_NUMBER: _ClassVar[int]
    WRITER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination: str
    filter: str
    description: str
    disabled: bool
    exclusions: _containers.RepeatedCompositeFieldContainer[LogExclusion]
    output_version_format: LogSink.VersionFormat
    writer_identity: str
    include_children: bool
    bigquery_options: BigQueryOptions
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., destination: _Optional[str]=..., filter: _Optional[str]=..., description: _Optional[str]=..., disabled: bool=..., exclusions: _Optional[_Iterable[_Union[LogExclusion, _Mapping]]]=..., output_version_format: _Optional[_Union[LogSink.VersionFormat, str]]=..., writer_identity: _Optional[str]=..., include_children: bool=..., bigquery_options: _Optional[_Union[BigQueryOptions, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BigQueryDataset(_message.Message):
    __slots__ = ('dataset_id',)
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str

    def __init__(self, dataset_id: _Optional[str]=...) -> None:
        ...

class Link(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'lifecycle_state', 'bigquery_dataset')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DATASET_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    lifecycle_state: LifecycleState
    bigquery_dataset: BigQueryDataset

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., lifecycle_state: _Optional[_Union[LifecycleState, str]]=..., bigquery_dataset: _Optional[_Union[BigQueryDataset, _Mapping]]=...) -> None:
        ...

class BigQueryOptions(_message.Message):
    __slots__ = ('use_partitioned_tables', 'uses_timestamp_column_partitioning')
    USE_PARTITIONED_TABLES_FIELD_NUMBER: _ClassVar[int]
    USES_TIMESTAMP_COLUMN_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    use_partitioned_tables: bool
    uses_timestamp_column_partitioning: bool

    def __init__(self, use_partitioned_tables: bool=..., uses_timestamp_column_partitioning: bool=...) -> None:
        ...

class ListBucketsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListBucketsResponse(_message.Message):
    __slots__ = ('buckets', 'next_page_token')
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[LogBucket]
    next_page_token: str

    def __init__(self, buckets: _Optional[_Iterable[_Union[LogBucket, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateBucketRequest(_message.Message):
    __slots__ = ('parent', 'bucket_id', 'bucket')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    bucket_id: str
    bucket: LogBucket

    def __init__(self, parent: _Optional[str]=..., bucket_id: _Optional[str]=..., bucket: _Optional[_Union[LogBucket, _Mapping]]=...) -> None:
        ...

class UpdateBucketRequest(_message.Message):
    __slots__ = ('name', 'bucket', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    bucket: LogBucket
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., bucket: _Optional[_Union[LogBucket, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetBucketRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteBucketRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeleteBucketRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListViewsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListViewsResponse(_message.Message):
    __slots__ = ('views', 'next_page_token')
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    views: _containers.RepeatedCompositeFieldContainer[LogView]
    next_page_token: str

    def __init__(self, views: _Optional[_Iterable[_Union[LogView, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateViewRequest(_message.Message):
    __slots__ = ('parent', 'view_id', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view_id: str
    view: LogView

    def __init__(self, parent: _Optional[str]=..., view_id: _Optional[str]=..., view: _Optional[_Union[LogView, _Mapping]]=...) -> None:
        ...

class UpdateViewRequest(_message.Message):
    __slots__ = ('name', 'view', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: LogView
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[LogView, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetViewRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteViewRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSinksRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListSinksResponse(_message.Message):
    __slots__ = ('sinks', 'next_page_token')
    SINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sinks: _containers.RepeatedCompositeFieldContainer[LogSink]
    next_page_token: str

    def __init__(self, sinks: _Optional[_Iterable[_Union[LogSink, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetSinkRequest(_message.Message):
    __slots__ = ('sink_name',)
    SINK_NAME_FIELD_NUMBER: _ClassVar[int]
    sink_name: str

    def __init__(self, sink_name: _Optional[str]=...) -> None:
        ...

class CreateSinkRequest(_message.Message):
    __slots__ = ('parent', 'sink', 'unique_writer_identity')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SINK_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_WRITER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    sink: LogSink
    unique_writer_identity: bool

    def __init__(self, parent: _Optional[str]=..., sink: _Optional[_Union[LogSink, _Mapping]]=..., unique_writer_identity: bool=...) -> None:
        ...

class UpdateSinkRequest(_message.Message):
    __slots__ = ('sink_name', 'sink', 'unique_writer_identity', 'update_mask')
    SINK_NAME_FIELD_NUMBER: _ClassVar[int]
    SINK_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_WRITER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    sink_name: str
    sink: LogSink
    unique_writer_identity: bool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, sink_name: _Optional[str]=..., sink: _Optional[_Union[LogSink, _Mapping]]=..., unique_writer_identity: bool=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteSinkRequest(_message.Message):
    __slots__ = ('sink_name',)
    SINK_NAME_FIELD_NUMBER: _ClassVar[int]
    sink_name: str

    def __init__(self, sink_name: _Optional[str]=...) -> None:
        ...

class CreateLinkRequest(_message.Message):
    __slots__ = ('parent', 'link', 'link_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    link: Link
    link_id: str

    def __init__(self, parent: _Optional[str]=..., link: _Optional[_Union[Link, _Mapping]]=..., link_id: _Optional[str]=...) -> None:
        ...

class DeleteLinkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListLinksRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListLinksResponse(_message.Message):
    __slots__ = ('links', 'next_page_token')
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[Link]
    next_page_token: str

    def __init__(self, links: _Optional[_Iterable[_Union[Link, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetLinkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LogExclusion(_message.Message):
    __slots__ = ('name', 'description', 'filter', 'disabled', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    filter: str
    disabled: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., filter: _Optional[str]=..., disabled: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListExclusionsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListExclusionsResponse(_message.Message):
    __slots__ = ('exclusions', 'next_page_token')
    EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    exclusions: _containers.RepeatedCompositeFieldContainer[LogExclusion]
    next_page_token: str

    def __init__(self, exclusions: _Optional[_Iterable[_Union[LogExclusion, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetExclusionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateExclusionRequest(_message.Message):
    __slots__ = ('parent', 'exclusion')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    exclusion: LogExclusion

    def __init__(self, parent: _Optional[str]=..., exclusion: _Optional[_Union[LogExclusion, _Mapping]]=...) -> None:
        ...

class UpdateExclusionRequest(_message.Message):
    __slots__ = ('name', 'exclusion', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    exclusion: LogExclusion
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., exclusion: _Optional[_Union[LogExclusion, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteExclusionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetCmekSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateCmekSettingsRequest(_message.Message):
    __slots__ = ('name', 'cmek_settings', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CMEK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    cmek_settings: CmekSettings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., cmek_settings: _Optional[_Union[CmekSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class CmekSettings(_message.Message):
    __slots__ = ('name', 'kms_key_name', 'kms_key_version_name', 'service_account_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    kms_key_name: str
    kms_key_version_name: str
    service_account_id: str

    def __init__(self, name: _Optional[str]=..., kms_key_name: _Optional[str]=..., kms_key_version_name: _Optional[str]=..., service_account_id: _Optional[str]=...) -> None:
        ...

class GetSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ('name', 'settings', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    settings: Settings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., settings: _Optional[_Union[Settings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class Settings(_message.Message):
    __slots__ = ('name', 'kms_key_name', 'kms_service_account_id', 'storage_location', 'disable_default_sink')
    NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DEFAULT_SINK_FIELD_NUMBER: _ClassVar[int]
    name: str
    kms_key_name: str
    kms_service_account_id: str
    storage_location: str
    disable_default_sink: bool

    def __init__(self, name: _Optional[str]=..., kms_key_name: _Optional[str]=..., kms_service_account_id: _Optional[str]=..., storage_location: _Optional[str]=..., disable_default_sink: bool=...) -> None:
        ...

class CopyLogEntriesRequest(_message.Message):
    __slots__ = ('name', 'filter', 'destination')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str
    destination: str

    def __init__(self, name: _Optional[str]=..., filter: _Optional[str]=..., destination: _Optional[str]=...) -> None:
        ...

class CopyLogEntriesMetadata(_message.Message):
    __slots__ = ('start_time', 'end_time', 'state', 'cancellation_requested', 'request', 'progress', 'writer_identity')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    WRITER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: OperationState
    cancellation_requested: bool
    request: CopyLogEntriesRequest
    progress: int
    writer_identity: str

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[OperationState, str]]=..., cancellation_requested: bool=..., request: _Optional[_Union[CopyLogEntriesRequest, _Mapping]]=..., progress: _Optional[int]=..., writer_identity: _Optional[str]=...) -> None:
        ...

class CopyLogEntriesResponse(_message.Message):
    __slots__ = ('log_entries_copied_count',)
    LOG_ENTRIES_COPIED_COUNT_FIELD_NUMBER: _ClassVar[int]
    log_entries_copied_count: int

    def __init__(self, log_entries_copied_count: _Optional[int]=...) -> None:
        ...

class BucketMetadata(_message.Message):
    __slots__ = ('start_time', 'end_time', 'state', 'create_bucket_request', 'update_bucket_request')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_BUCKET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BUCKET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: OperationState
    create_bucket_request: CreateBucketRequest
    update_bucket_request: UpdateBucketRequest

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[OperationState, str]]=..., create_bucket_request: _Optional[_Union[CreateBucketRequest, _Mapping]]=..., update_bucket_request: _Optional[_Union[UpdateBucketRequest, _Mapping]]=...) -> None:
        ...

class LinkMetadata(_message.Message):
    __slots__ = ('start_time', 'end_time', 'state', 'create_link_request', 'delete_link_request')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_LINK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DELETE_LINK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: OperationState
    create_link_request: CreateLinkRequest
    delete_link_request: DeleteLinkRequest

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[OperationState, str]]=..., create_link_request: _Optional[_Union[CreateLinkRequest, _Mapping]]=..., delete_link_request: _Optional[_Union[DeleteLinkRequest, _Mapping]]=...) -> None:
        ...

class LocationMetadata(_message.Message):
    __slots__ = ('log_analytics_enabled',)
    LOG_ANALYTICS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    log_analytics_enabled: bool

    def __init__(self, log_analytics_enabled: bool=...) -> None:
        ...