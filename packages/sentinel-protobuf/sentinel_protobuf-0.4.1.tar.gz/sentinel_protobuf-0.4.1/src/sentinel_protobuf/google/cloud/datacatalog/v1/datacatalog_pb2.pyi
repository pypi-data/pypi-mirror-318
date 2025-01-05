from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.datacatalog.v1 import bigquery_pb2 as _bigquery_pb2
from google.cloud.datacatalog.v1 import common_pb2 as _common_pb2
from google.cloud.datacatalog.v1 import data_source_pb2 as _data_source_pb2
from google.cloud.datacatalog.v1 import dataplex_spec_pb2 as _dataplex_spec_pb2
from google.cloud.datacatalog.v1 import gcs_fileset_spec_pb2 as _gcs_fileset_spec_pb2
from google.cloud.datacatalog.v1 import schema_pb2 as _schema_pb2
from google.cloud.datacatalog.v1 import search_pb2 as _search_pb2
from google.cloud.datacatalog.v1 import table_spec_pb2 as _table_spec_pb2
from google.cloud.datacatalog.v1 import tags_pb2 as _tags_pb2
from google.cloud.datacatalog.v1 import timestamps_pb2 as _timestamps_pb2
from google.cloud.datacatalog.v1 import usage_pb2 as _usage_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTRY_TYPE_UNSPECIFIED: _ClassVar[EntryType]
    TABLE: _ClassVar[EntryType]
    MODEL: _ClassVar[EntryType]
    DATA_STREAM: _ClassVar[EntryType]
    FILESET: _ClassVar[EntryType]
    CLUSTER: _ClassVar[EntryType]
    DATABASE: _ClassVar[EntryType]
    DATA_SOURCE_CONNECTION: _ClassVar[EntryType]
    ROUTINE: _ClassVar[EntryType]
    LAKE: _ClassVar[EntryType]
    ZONE: _ClassVar[EntryType]
    SERVICE: _ClassVar[EntryType]
    DATABASE_SCHEMA: _ClassVar[EntryType]
    DASHBOARD: _ClassVar[EntryType]
    EXPLORE: _ClassVar[EntryType]
    LOOK: _ClassVar[EntryType]
    FEATURE_ONLINE_STORE: _ClassVar[EntryType]
    FEATURE_VIEW: _ClassVar[EntryType]
    FEATURE_GROUP: _ClassVar[EntryType]

class TagTemplateMigration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TAG_TEMPLATE_MIGRATION_UNSPECIFIED: _ClassVar[TagTemplateMigration]
    TAG_TEMPLATE_MIGRATION_ENABLED: _ClassVar[TagTemplateMigration]
    TAG_TEMPLATE_MIGRATION_DISABLED: _ClassVar[TagTemplateMigration]

class CatalogUIExperience(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CATALOG_UI_EXPERIENCE_UNSPECIFIED: _ClassVar[CatalogUIExperience]
    CATALOG_UI_EXPERIENCE_ENABLED: _ClassVar[CatalogUIExperience]
    CATALOG_UI_EXPERIENCE_DISABLED: _ClassVar[CatalogUIExperience]
ENTRY_TYPE_UNSPECIFIED: EntryType
TABLE: EntryType
MODEL: EntryType
DATA_STREAM: EntryType
FILESET: EntryType
CLUSTER: EntryType
DATABASE: EntryType
DATA_SOURCE_CONNECTION: EntryType
ROUTINE: EntryType
LAKE: EntryType
ZONE: EntryType
SERVICE: EntryType
DATABASE_SCHEMA: EntryType
DASHBOARD: EntryType
EXPLORE: EntryType
LOOK: EntryType
FEATURE_ONLINE_STORE: EntryType
FEATURE_VIEW: EntryType
FEATURE_GROUP: EntryType
TAG_TEMPLATE_MIGRATION_UNSPECIFIED: TagTemplateMigration
TAG_TEMPLATE_MIGRATION_ENABLED: TagTemplateMigration
TAG_TEMPLATE_MIGRATION_DISABLED: TagTemplateMigration
CATALOG_UI_EXPERIENCE_UNSPECIFIED: CatalogUIExperience
CATALOG_UI_EXPERIENCE_ENABLED: CatalogUIExperience
CATALOG_UI_EXPERIENCE_DISABLED: CatalogUIExperience

class SearchCatalogRequest(_message.Message):
    __slots__ = ("scope", "query", "page_size", "page_token", "order_by", "admin_search")
    class Scope(_message.Message):
        __slots__ = ("include_org_ids", "include_project_ids", "include_gcp_public_datasets", "restricted_locations", "starred_only", "include_public_tag_templates")
        INCLUDE_ORG_IDS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_PROJECT_IDS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_GCP_PUBLIC_DATASETS_FIELD_NUMBER: _ClassVar[int]
        RESTRICTED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        STARRED_ONLY_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_PUBLIC_TAG_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
        include_org_ids: _containers.RepeatedScalarFieldContainer[str]
        include_project_ids: _containers.RepeatedScalarFieldContainer[str]
        include_gcp_public_datasets: bool
        restricted_locations: _containers.RepeatedScalarFieldContainer[str]
        starred_only: bool
        include_public_tag_templates: bool
        def __init__(self, include_org_ids: _Optional[_Iterable[str]] = ..., include_project_ids: _Optional[_Iterable[str]] = ..., include_gcp_public_datasets: bool = ..., restricted_locations: _Optional[_Iterable[str]] = ..., starred_only: bool = ..., include_public_tag_templates: bool = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    ADMIN_SEARCH_FIELD_NUMBER: _ClassVar[int]
    scope: SearchCatalogRequest.Scope
    query: str
    page_size: int
    page_token: str
    order_by: str
    admin_search: bool
    def __init__(self, scope: _Optional[_Union[SearchCatalogRequest.Scope, _Mapping]] = ..., query: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., admin_search: bool = ...) -> None: ...

class SearchCatalogResponse(_message.Message):
    __slots__ = ("results", "total_size", "next_page_token", "unreachable")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_search_pb2.SearchCatalogResult]
    total_size: int
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, results: _Optional[_Iterable[_Union[_search_pb2.SearchCatalogResult, _Mapping]]] = ..., total_size: _Optional[int] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateEntryGroupRequest(_message.Message):
    __slots__ = ("parent", "entry_group_id", "entry_group")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_GROUP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entry_group_id: str
    entry_group: EntryGroup
    def __init__(self, parent: _Optional[str] = ..., entry_group_id: _Optional[str] = ..., entry_group: _Optional[_Union[EntryGroup, _Mapping]] = ...) -> None: ...

class UpdateEntryGroupRequest(_message.Message):
    __slots__ = ("entry_group", "update_mask")
    ENTRY_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    entry_group: EntryGroup
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, entry_group: _Optional[_Union[EntryGroup, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetEntryGroupRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEntryGroupRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class ListEntryGroupsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEntryGroupsResponse(_message.Message):
    __slots__ = ("entry_groups", "next_page_token")
    ENTRY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entry_groups: _containers.RepeatedCompositeFieldContainer[EntryGroup]
    next_page_token: str
    def __init__(self, entry_groups: _Optional[_Iterable[_Union[EntryGroup, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateEntryRequest(_message.Message):
    __slots__ = ("parent", "entry_id", "entry")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entry_id: str
    entry: Entry
    def __init__(self, parent: _Optional[str] = ..., entry_id: _Optional[str] = ..., entry: _Optional[_Union[Entry, _Mapping]] = ...) -> None: ...

class UpdateEntryRequest(_message.Message):
    __slots__ = ("entry", "update_mask")
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    entry: Entry
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, entry: _Optional[_Union[Entry, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEntryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetEntryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class LookupEntryRequest(_message.Message):
    __slots__ = ("linked_resource", "sql_resource", "fully_qualified_name", "project", "location")
    LINKED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SQL_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    FULLY_QUALIFIED_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    linked_resource: str
    sql_resource: str
    fully_qualified_name: str
    project: str
    location: str
    def __init__(self, linked_resource: _Optional[str] = ..., sql_resource: _Optional[str] = ..., fully_qualified_name: _Optional[str] = ..., project: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class Entry(_message.Message):
    __slots__ = ("name", "linked_resource", "fully_qualified_name", "type", "user_specified_type", "integrated_system", "user_specified_system", "sql_database_system_spec", "looker_system_spec", "cloud_bigtable_system_spec", "gcs_fileset_spec", "bigquery_table_spec", "bigquery_date_sharded_spec", "database_table_spec", "data_source_connection_spec", "routine_spec", "dataset_spec", "fileset_spec", "service_spec", "model_spec", "feature_online_store_spec", "display_name", "description", "business_context", "schema", "source_system_timestamps", "usage_signal", "labels", "data_source", "personal_details")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINKED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    FULLY_QUALIFIED_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_SPECIFIED_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATED_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    USER_SPECIFIED_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    SQL_DATABASE_SYSTEM_SPEC_FIELD_NUMBER: _ClassVar[int]
    LOOKER_SYSTEM_SPEC_FIELD_NUMBER: _ClassVar[int]
    CLOUD_BIGTABLE_SYSTEM_SPEC_FIELD_NUMBER: _ClassVar[int]
    GCS_FILESET_SPEC_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_TABLE_SPEC_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DATE_SHARDED_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATABASE_TABLE_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_CONNECTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATASET_SPEC_FIELD_NUMBER: _ClassVar[int]
    FILESET_SPEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_SPEC_FIELD_NUMBER: _ClassVar[int]
    MODEL_SPEC_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ONLINE_STORE_SPEC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYSTEM_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    USAGE_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    linked_resource: str
    fully_qualified_name: str
    type: EntryType
    user_specified_type: str
    integrated_system: _common_pb2.IntegratedSystem
    user_specified_system: str
    sql_database_system_spec: SqlDatabaseSystemSpec
    looker_system_spec: LookerSystemSpec
    cloud_bigtable_system_spec: CloudBigtableSystemSpec
    gcs_fileset_spec: _gcs_fileset_spec_pb2.GcsFilesetSpec
    bigquery_table_spec: _table_spec_pb2.BigQueryTableSpec
    bigquery_date_sharded_spec: _table_spec_pb2.BigQueryDateShardedSpec
    database_table_spec: DatabaseTableSpec
    data_source_connection_spec: DataSourceConnectionSpec
    routine_spec: RoutineSpec
    dataset_spec: DatasetSpec
    fileset_spec: FilesetSpec
    service_spec: ServiceSpec
    model_spec: ModelSpec
    feature_online_store_spec: FeatureOnlineStoreSpec
    display_name: str
    description: str
    business_context: BusinessContext
    schema: _schema_pb2.Schema
    source_system_timestamps: _timestamps_pb2.SystemTimestamps
    usage_signal: _usage_pb2.UsageSignal
    labels: _containers.ScalarMap[str, str]
    data_source: _data_source_pb2.DataSource
    personal_details: _common_pb2.PersonalDetails
    def __init__(self, name: _Optional[str] = ..., linked_resource: _Optional[str] = ..., fully_qualified_name: _Optional[str] = ..., type: _Optional[_Union[EntryType, str]] = ..., user_specified_type: _Optional[str] = ..., integrated_system: _Optional[_Union[_common_pb2.IntegratedSystem, str]] = ..., user_specified_system: _Optional[str] = ..., sql_database_system_spec: _Optional[_Union[SqlDatabaseSystemSpec, _Mapping]] = ..., looker_system_spec: _Optional[_Union[LookerSystemSpec, _Mapping]] = ..., cloud_bigtable_system_spec: _Optional[_Union[CloudBigtableSystemSpec, _Mapping]] = ..., gcs_fileset_spec: _Optional[_Union[_gcs_fileset_spec_pb2.GcsFilesetSpec, _Mapping]] = ..., bigquery_table_spec: _Optional[_Union[_table_spec_pb2.BigQueryTableSpec, _Mapping]] = ..., bigquery_date_sharded_spec: _Optional[_Union[_table_spec_pb2.BigQueryDateShardedSpec, _Mapping]] = ..., database_table_spec: _Optional[_Union[DatabaseTableSpec, _Mapping]] = ..., data_source_connection_spec: _Optional[_Union[DataSourceConnectionSpec, _Mapping]] = ..., routine_spec: _Optional[_Union[RoutineSpec, _Mapping]] = ..., dataset_spec: _Optional[_Union[DatasetSpec, _Mapping]] = ..., fileset_spec: _Optional[_Union[FilesetSpec, _Mapping]] = ..., service_spec: _Optional[_Union[ServiceSpec, _Mapping]] = ..., model_spec: _Optional[_Union[ModelSpec, _Mapping]] = ..., feature_online_store_spec: _Optional[_Union[FeatureOnlineStoreSpec, _Mapping]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., business_context: _Optional[_Union[BusinessContext, _Mapping]] = ..., schema: _Optional[_Union[_schema_pb2.Schema, _Mapping]] = ..., source_system_timestamps: _Optional[_Union[_timestamps_pb2.SystemTimestamps, _Mapping]] = ..., usage_signal: _Optional[_Union[_usage_pb2.UsageSignal, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., data_source: _Optional[_Union[_data_source_pb2.DataSource, _Mapping]] = ..., personal_details: _Optional[_Union[_common_pb2.PersonalDetails, _Mapping]] = ...) -> None: ...

class DatabaseTableSpec(_message.Message):
    __slots__ = ("type", "dataplex_table", "database_view_spec")
    class TableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TABLE_TYPE_UNSPECIFIED: _ClassVar[DatabaseTableSpec.TableType]
        NATIVE: _ClassVar[DatabaseTableSpec.TableType]
        EXTERNAL: _ClassVar[DatabaseTableSpec.TableType]
    TABLE_TYPE_UNSPECIFIED: DatabaseTableSpec.TableType
    NATIVE: DatabaseTableSpec.TableType
    EXTERNAL: DatabaseTableSpec.TableType
    class DatabaseViewSpec(_message.Message):
        __slots__ = ("view_type", "base_table", "sql_query")
        class ViewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VIEW_TYPE_UNSPECIFIED: _ClassVar[DatabaseTableSpec.DatabaseViewSpec.ViewType]
            STANDARD_VIEW: _ClassVar[DatabaseTableSpec.DatabaseViewSpec.ViewType]
            MATERIALIZED_VIEW: _ClassVar[DatabaseTableSpec.DatabaseViewSpec.ViewType]
        VIEW_TYPE_UNSPECIFIED: DatabaseTableSpec.DatabaseViewSpec.ViewType
        STANDARD_VIEW: DatabaseTableSpec.DatabaseViewSpec.ViewType
        MATERIALIZED_VIEW: DatabaseTableSpec.DatabaseViewSpec.ViewType
        VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
        BASE_TABLE_FIELD_NUMBER: _ClassVar[int]
        SQL_QUERY_FIELD_NUMBER: _ClassVar[int]
        view_type: DatabaseTableSpec.DatabaseViewSpec.ViewType
        base_table: str
        sql_query: str
        def __init__(self, view_type: _Optional[_Union[DatabaseTableSpec.DatabaseViewSpec.ViewType, str]] = ..., base_table: _Optional[str] = ..., sql_query: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATAPLEX_TABLE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VIEW_SPEC_FIELD_NUMBER: _ClassVar[int]
    type: DatabaseTableSpec.TableType
    dataplex_table: _dataplex_spec_pb2.DataplexTableSpec
    database_view_spec: DatabaseTableSpec.DatabaseViewSpec
    def __init__(self, type: _Optional[_Union[DatabaseTableSpec.TableType, str]] = ..., dataplex_table: _Optional[_Union[_dataplex_spec_pb2.DataplexTableSpec, _Mapping]] = ..., database_view_spec: _Optional[_Union[DatabaseTableSpec.DatabaseViewSpec, _Mapping]] = ...) -> None: ...

class FilesetSpec(_message.Message):
    __slots__ = ("dataplex_fileset",)
    DATAPLEX_FILESET_FIELD_NUMBER: _ClassVar[int]
    dataplex_fileset: _dataplex_spec_pb2.DataplexFilesetSpec
    def __init__(self, dataplex_fileset: _Optional[_Union[_dataplex_spec_pb2.DataplexFilesetSpec, _Mapping]] = ...) -> None: ...

class DataSourceConnectionSpec(_message.Message):
    __slots__ = ("bigquery_connection_spec",)
    BIGQUERY_CONNECTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    bigquery_connection_spec: _bigquery_pb2.BigQueryConnectionSpec
    def __init__(self, bigquery_connection_spec: _Optional[_Union[_bigquery_pb2.BigQueryConnectionSpec, _Mapping]] = ...) -> None: ...

class RoutineSpec(_message.Message):
    __slots__ = ("routine_type", "language", "routine_arguments", "return_type", "definition_body", "bigquery_routine_spec")
    class RoutineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROUTINE_TYPE_UNSPECIFIED: _ClassVar[RoutineSpec.RoutineType]
        SCALAR_FUNCTION: _ClassVar[RoutineSpec.RoutineType]
        PROCEDURE: _ClassVar[RoutineSpec.RoutineType]
    ROUTINE_TYPE_UNSPECIFIED: RoutineSpec.RoutineType
    SCALAR_FUNCTION: RoutineSpec.RoutineType
    PROCEDURE: RoutineSpec.RoutineType
    class Argument(_message.Message):
        __slots__ = ("name", "mode", "type")
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[RoutineSpec.Argument.Mode]
            IN: _ClassVar[RoutineSpec.Argument.Mode]
            OUT: _ClassVar[RoutineSpec.Argument.Mode]
            INOUT: _ClassVar[RoutineSpec.Argument.Mode]
        MODE_UNSPECIFIED: RoutineSpec.Argument.Mode
        IN: RoutineSpec.Argument.Mode
        OUT: RoutineSpec.Argument.Mode
        INOUT: RoutineSpec.Argument.Mode
        NAME_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        mode: RoutineSpec.Argument.Mode
        type: str
        def __init__(self, name: _Optional[str] = ..., mode: _Optional[_Union[RoutineSpec.Argument.Mode, str]] = ..., type: _Optional[str] = ...) -> None: ...
    ROUTINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_BODY_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_ROUTINE_SPEC_FIELD_NUMBER: _ClassVar[int]
    routine_type: RoutineSpec.RoutineType
    language: str
    routine_arguments: _containers.RepeatedCompositeFieldContainer[RoutineSpec.Argument]
    return_type: str
    definition_body: str
    bigquery_routine_spec: _bigquery_pb2.BigQueryRoutineSpec
    def __init__(self, routine_type: _Optional[_Union[RoutineSpec.RoutineType, str]] = ..., language: _Optional[str] = ..., routine_arguments: _Optional[_Iterable[_Union[RoutineSpec.Argument, _Mapping]]] = ..., return_type: _Optional[str] = ..., definition_body: _Optional[str] = ..., bigquery_routine_spec: _Optional[_Union[_bigquery_pb2.BigQueryRoutineSpec, _Mapping]] = ...) -> None: ...

class DatasetSpec(_message.Message):
    __slots__ = ("vertex_dataset_spec",)
    VERTEX_DATASET_SPEC_FIELD_NUMBER: _ClassVar[int]
    vertex_dataset_spec: VertexDatasetSpec
    def __init__(self, vertex_dataset_spec: _Optional[_Union[VertexDatasetSpec, _Mapping]] = ...) -> None: ...

class SqlDatabaseSystemSpec(_message.Message):
    __slots__ = ("sql_engine", "database_version", "instance_host")
    SQL_ENGINE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_HOST_FIELD_NUMBER: _ClassVar[int]
    sql_engine: str
    database_version: str
    instance_host: str
    def __init__(self, sql_engine: _Optional[str] = ..., database_version: _Optional[str] = ..., instance_host: _Optional[str] = ...) -> None: ...

class LookerSystemSpec(_message.Message):
    __slots__ = ("parent_instance_id", "parent_instance_display_name", "parent_model_id", "parent_model_display_name", "parent_view_id", "parent_view_display_name")
    PARENT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_INSTANCE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_VIEW_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    parent_instance_id: str
    parent_instance_display_name: str
    parent_model_id: str
    parent_model_display_name: str
    parent_view_id: str
    parent_view_display_name: str
    def __init__(self, parent_instance_id: _Optional[str] = ..., parent_instance_display_name: _Optional[str] = ..., parent_model_id: _Optional[str] = ..., parent_model_display_name: _Optional[str] = ..., parent_view_id: _Optional[str] = ..., parent_view_display_name: _Optional[str] = ...) -> None: ...

class CloudBigtableSystemSpec(_message.Message):
    __slots__ = ("instance_display_name",)
    INSTANCE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    instance_display_name: str
    def __init__(self, instance_display_name: _Optional[str] = ...) -> None: ...

class CloudBigtableInstanceSpec(_message.Message):
    __slots__ = ("cloud_bigtable_cluster_specs",)
    class CloudBigtableClusterSpec(_message.Message):
        __slots__ = ("display_name", "location", "type", "linked_resource")
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        LINKED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        location: str
        type: str
        linked_resource: str
        def __init__(self, display_name: _Optional[str] = ..., location: _Optional[str] = ..., type: _Optional[str] = ..., linked_resource: _Optional[str] = ...) -> None: ...
    CLOUD_BIGTABLE_CLUSTER_SPECS_FIELD_NUMBER: _ClassVar[int]
    cloud_bigtable_cluster_specs: _containers.RepeatedCompositeFieldContainer[CloudBigtableInstanceSpec.CloudBigtableClusterSpec]
    def __init__(self, cloud_bigtable_cluster_specs: _Optional[_Iterable[_Union[CloudBigtableInstanceSpec.CloudBigtableClusterSpec, _Mapping]]] = ...) -> None: ...

class ServiceSpec(_message.Message):
    __slots__ = ("cloud_bigtable_instance_spec",)
    CLOUD_BIGTABLE_INSTANCE_SPEC_FIELD_NUMBER: _ClassVar[int]
    cloud_bigtable_instance_spec: CloudBigtableInstanceSpec
    def __init__(self, cloud_bigtable_instance_spec: _Optional[_Union[CloudBigtableInstanceSpec, _Mapping]] = ...) -> None: ...

class VertexModelSourceInfo(_message.Message):
    __slots__ = ("source_type", "copy")
    class ModelSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_SOURCE_TYPE_UNSPECIFIED: _ClassVar[VertexModelSourceInfo.ModelSourceType]
        AUTOML: _ClassVar[VertexModelSourceInfo.ModelSourceType]
        CUSTOM: _ClassVar[VertexModelSourceInfo.ModelSourceType]
        BQML: _ClassVar[VertexModelSourceInfo.ModelSourceType]
        MODEL_GARDEN: _ClassVar[VertexModelSourceInfo.ModelSourceType]
        GENIE: _ClassVar[VertexModelSourceInfo.ModelSourceType]
        CUSTOM_TEXT_EMBEDDING: _ClassVar[VertexModelSourceInfo.ModelSourceType]
        MARKETPLACE: _ClassVar[VertexModelSourceInfo.ModelSourceType]
    MODEL_SOURCE_TYPE_UNSPECIFIED: VertexModelSourceInfo.ModelSourceType
    AUTOML: VertexModelSourceInfo.ModelSourceType
    CUSTOM: VertexModelSourceInfo.ModelSourceType
    BQML: VertexModelSourceInfo.ModelSourceType
    MODEL_GARDEN: VertexModelSourceInfo.ModelSourceType
    GENIE: VertexModelSourceInfo.ModelSourceType
    CUSTOM_TEXT_EMBEDDING: VertexModelSourceInfo.ModelSourceType
    MARKETPLACE: VertexModelSourceInfo.ModelSourceType
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COPY_FIELD_NUMBER: _ClassVar[int]
    source_type: VertexModelSourceInfo.ModelSourceType
    copy: bool
    def __init__(self, source_type: _Optional[_Union[VertexModelSourceInfo.ModelSourceType, str]] = ..., copy: bool = ...) -> None: ...

class VertexModelSpec(_message.Message):
    __slots__ = ("version_id", "version_aliases", "version_description", "vertex_model_source_info", "container_image_uri")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ALIASES_FIELD_NUMBER: _ClassVar[int]
    VERSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERTEX_MODEL_SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    version_aliases: _containers.RepeatedScalarFieldContainer[str]
    version_description: str
    vertex_model_source_info: VertexModelSourceInfo
    container_image_uri: str
    def __init__(self, version_id: _Optional[str] = ..., version_aliases: _Optional[_Iterable[str]] = ..., version_description: _Optional[str] = ..., vertex_model_source_info: _Optional[_Union[VertexModelSourceInfo, _Mapping]] = ..., container_image_uri: _Optional[str] = ...) -> None: ...

class VertexDatasetSpec(_message.Message):
    __slots__ = ("data_item_count", "data_type")
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[VertexDatasetSpec.DataType]
        TABLE: _ClassVar[VertexDatasetSpec.DataType]
        IMAGE: _ClassVar[VertexDatasetSpec.DataType]
        TEXT: _ClassVar[VertexDatasetSpec.DataType]
        VIDEO: _ClassVar[VertexDatasetSpec.DataType]
        CONVERSATION: _ClassVar[VertexDatasetSpec.DataType]
        TIME_SERIES: _ClassVar[VertexDatasetSpec.DataType]
        DOCUMENT: _ClassVar[VertexDatasetSpec.DataType]
        TEXT_TO_SPEECH: _ClassVar[VertexDatasetSpec.DataType]
        TRANSLATION: _ClassVar[VertexDatasetSpec.DataType]
        STORE_VISION: _ClassVar[VertexDatasetSpec.DataType]
        ENTERPRISE_KNOWLEDGE_GRAPH: _ClassVar[VertexDatasetSpec.DataType]
        TEXT_PROMPT: _ClassVar[VertexDatasetSpec.DataType]
    DATA_TYPE_UNSPECIFIED: VertexDatasetSpec.DataType
    TABLE: VertexDatasetSpec.DataType
    IMAGE: VertexDatasetSpec.DataType
    TEXT: VertexDatasetSpec.DataType
    VIDEO: VertexDatasetSpec.DataType
    CONVERSATION: VertexDatasetSpec.DataType
    TIME_SERIES: VertexDatasetSpec.DataType
    DOCUMENT: VertexDatasetSpec.DataType
    TEXT_TO_SPEECH: VertexDatasetSpec.DataType
    TRANSLATION: VertexDatasetSpec.DataType
    STORE_VISION: VertexDatasetSpec.DataType
    ENTERPRISE_KNOWLEDGE_GRAPH: VertexDatasetSpec.DataType
    TEXT_PROMPT: VertexDatasetSpec.DataType
    DATA_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    data_item_count: int
    data_type: VertexDatasetSpec.DataType
    def __init__(self, data_item_count: _Optional[int] = ..., data_type: _Optional[_Union[VertexDatasetSpec.DataType, str]] = ...) -> None: ...

class ModelSpec(_message.Message):
    __slots__ = ("vertex_model_spec",)
    VERTEX_MODEL_SPEC_FIELD_NUMBER: _ClassVar[int]
    vertex_model_spec: VertexModelSpec
    def __init__(self, vertex_model_spec: _Optional[_Union[VertexModelSpec, _Mapping]] = ...) -> None: ...

class FeatureOnlineStoreSpec(_message.Message):
    __slots__ = ("storage_type",)
    class StorageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_TYPE_UNSPECIFIED: _ClassVar[FeatureOnlineStoreSpec.StorageType]
        BIGTABLE: _ClassVar[FeatureOnlineStoreSpec.StorageType]
        OPTIMIZED: _ClassVar[FeatureOnlineStoreSpec.StorageType]
    STORAGE_TYPE_UNSPECIFIED: FeatureOnlineStoreSpec.StorageType
    BIGTABLE: FeatureOnlineStoreSpec.StorageType
    OPTIMIZED: FeatureOnlineStoreSpec.StorageType
    STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    storage_type: FeatureOnlineStoreSpec.StorageType
    def __init__(self, storage_type: _Optional[_Union[FeatureOnlineStoreSpec.StorageType, str]] = ...) -> None: ...

class BusinessContext(_message.Message):
    __slots__ = ("entry_overview", "contacts")
    ENTRY_OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    entry_overview: EntryOverview
    contacts: Contacts
    def __init__(self, entry_overview: _Optional[_Union[EntryOverview, _Mapping]] = ..., contacts: _Optional[_Union[Contacts, _Mapping]] = ...) -> None: ...

class EntryOverview(_message.Message):
    __slots__ = ("overview",)
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    overview: str
    def __init__(self, overview: _Optional[str] = ...) -> None: ...

class Contacts(_message.Message):
    __slots__ = ("people",)
    class Person(_message.Message):
        __slots__ = ("designation", "email")
        DESIGNATION_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        designation: str
        email: str
        def __init__(self, designation: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    people: _containers.RepeatedCompositeFieldContainer[Contacts.Person]
    def __init__(self, people: _Optional[_Iterable[_Union[Contacts.Person, _Mapping]]] = ...) -> None: ...

class EntryGroup(_message.Message):
    __slots__ = ("name", "display_name", "description", "data_catalog_timestamps", "transferred_to_dataplex")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATA_CATALOG_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    TRANSFERRED_TO_DATAPLEX_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    data_catalog_timestamps: _timestamps_pb2.SystemTimestamps
    transferred_to_dataplex: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., data_catalog_timestamps: _Optional[_Union[_timestamps_pb2.SystemTimestamps, _Mapping]] = ..., transferred_to_dataplex: bool = ...) -> None: ...

class CreateTagTemplateRequest(_message.Message):
    __slots__ = ("parent", "tag_template_id", "tag_template")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tag_template_id: str
    tag_template: _tags_pb2.TagTemplate
    def __init__(self, parent: _Optional[str] = ..., tag_template_id: _Optional[str] = ..., tag_template: _Optional[_Union[_tags_pb2.TagTemplate, _Mapping]] = ...) -> None: ...

class GetTagTemplateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateTagTemplateRequest(_message.Message):
    __slots__ = ("tag_template", "update_mask")
    TAG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tag_template: _tags_pb2.TagTemplate
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, tag_template: _Optional[_Union[_tags_pb2.TagTemplate, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteTagTemplateRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class CreateTagRequest(_message.Message):
    __slots__ = ("parent", "tag")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tag: _tags_pb2.Tag
    def __init__(self, parent: _Optional[str] = ..., tag: _Optional[_Union[_tags_pb2.Tag, _Mapping]] = ...) -> None: ...

class UpdateTagRequest(_message.Message):
    __slots__ = ("tag", "update_mask")
    TAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tag: _tags_pb2.Tag
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, tag: _Optional[_Union[_tags_pb2.Tag, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteTagRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateTagTemplateFieldRequest(_message.Message):
    __slots__ = ("parent", "tag_template_field_id", "tag_template_field")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_FIELD_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tag_template_field_id: str
    tag_template_field: _tags_pb2.TagTemplateField
    def __init__(self, parent: _Optional[str] = ..., tag_template_field_id: _Optional[str] = ..., tag_template_field: _Optional[_Union[_tags_pb2.TagTemplateField, _Mapping]] = ...) -> None: ...

class UpdateTagTemplateFieldRequest(_message.Message):
    __slots__ = ("name", "tag_template_field", "update_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_FIELD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    tag_template_field: _tags_pb2.TagTemplateField
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., tag_template_field: _Optional[_Union[_tags_pb2.TagTemplateField, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class RenameTagTemplateFieldRequest(_message.Message):
    __slots__ = ("name", "new_tag_template_field_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_TAG_TEMPLATE_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_tag_template_field_id: str
    def __init__(self, name: _Optional[str] = ..., new_tag_template_field_id: _Optional[str] = ...) -> None: ...

class RenameTagTemplateFieldEnumValueRequest(_message.Message):
    __slots__ = ("name", "new_enum_value_display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_ENUM_VALUE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_enum_value_display_name: str
    def __init__(self, name: _Optional[str] = ..., new_enum_value_display_name: _Optional[str] = ...) -> None: ...

class DeleteTagTemplateFieldRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class ListTagsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListTagsResponse(_message.Message):
    __slots__ = ("tags", "next_page_token")
    TAGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[_tags_pb2.Tag]
    next_page_token: str
    def __init__(self, tags: _Optional[_Iterable[_Union[_tags_pb2.Tag, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReconcileTagsRequest(_message.Message):
    __slots__ = ("parent", "tag_template", "force_delete_missing", "tags")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FORCE_DELETE_MISSING_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tag_template: str
    force_delete_missing: bool
    tags: _containers.RepeatedCompositeFieldContainer[_tags_pb2.Tag]
    def __init__(self, parent: _Optional[str] = ..., tag_template: _Optional[str] = ..., force_delete_missing: bool = ..., tags: _Optional[_Iterable[_Union[_tags_pb2.Tag, _Mapping]]] = ...) -> None: ...

class ReconcileTagsResponse(_message.Message):
    __slots__ = ("created_tags_count", "updated_tags_count", "deleted_tags_count")
    CREATED_TAGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TAGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DELETED_TAGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    created_tags_count: int
    updated_tags_count: int
    deleted_tags_count: int
    def __init__(self, created_tags_count: _Optional[int] = ..., updated_tags_count: _Optional[int] = ..., deleted_tags_count: _Optional[int] = ...) -> None: ...

class ReconcileTagsMetadata(_message.Message):
    __slots__ = ("state", "errors")
    class ReconciliationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECONCILIATION_STATE_UNSPECIFIED: _ClassVar[ReconcileTagsMetadata.ReconciliationState]
        RECONCILIATION_QUEUED: _ClassVar[ReconcileTagsMetadata.ReconciliationState]
        RECONCILIATION_IN_PROGRESS: _ClassVar[ReconcileTagsMetadata.ReconciliationState]
        RECONCILIATION_DONE: _ClassVar[ReconcileTagsMetadata.ReconciliationState]
    RECONCILIATION_STATE_UNSPECIFIED: ReconcileTagsMetadata.ReconciliationState
    RECONCILIATION_QUEUED: ReconcileTagsMetadata.ReconciliationState
    RECONCILIATION_IN_PROGRESS: ReconcileTagsMetadata.ReconciliationState
    RECONCILIATION_DONE: ReconcileTagsMetadata.ReconciliationState
    class ErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _status_pb2.Status
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    state: ReconcileTagsMetadata.ReconciliationState
    errors: _containers.MessageMap[str, _status_pb2.Status]
    def __init__(self, state: _Optional[_Union[ReconcileTagsMetadata.ReconciliationState, str]] = ..., errors: _Optional[_Mapping[str, _status_pb2.Status]] = ...) -> None: ...

class ListEntriesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListEntriesResponse(_message.Message):
    __slots__ = ("entries", "next_page_token")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[Entry]
    next_page_token: str
    def __init__(self, entries: _Optional[_Iterable[_Union[Entry, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class StarEntryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class StarEntryResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnstarEntryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UnstarEntryResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ImportEntriesRequest(_message.Message):
    __slots__ = ("parent", "gcs_bucket_path", "job_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GCS_BUCKET_PATH_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gcs_bucket_path: str
    job_id: str
    def __init__(self, parent: _Optional[str] = ..., gcs_bucket_path: _Optional[str] = ..., job_id: _Optional[str] = ...) -> None: ...

class ImportEntriesResponse(_message.Message):
    __slots__ = ("upserted_entries_count", "deleted_entries_count")
    UPSERTED_ENTRIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    DELETED_ENTRIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    upserted_entries_count: int
    deleted_entries_count: int
    def __init__(self, upserted_entries_count: _Optional[int] = ..., deleted_entries_count: _Optional[int] = ...) -> None: ...

class ImportEntriesMetadata(_message.Message):
    __slots__ = ("state", "errors")
    class ImportState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMPORT_STATE_UNSPECIFIED: _ClassVar[ImportEntriesMetadata.ImportState]
        IMPORT_QUEUED: _ClassVar[ImportEntriesMetadata.ImportState]
        IMPORT_IN_PROGRESS: _ClassVar[ImportEntriesMetadata.ImportState]
        IMPORT_DONE: _ClassVar[ImportEntriesMetadata.ImportState]
        IMPORT_OBSOLETE: _ClassVar[ImportEntriesMetadata.ImportState]
    IMPORT_STATE_UNSPECIFIED: ImportEntriesMetadata.ImportState
    IMPORT_QUEUED: ImportEntriesMetadata.ImportState
    IMPORT_IN_PROGRESS: ImportEntriesMetadata.ImportState
    IMPORT_DONE: ImportEntriesMetadata.ImportState
    IMPORT_OBSOLETE: ImportEntriesMetadata.ImportState
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    state: ImportEntriesMetadata.ImportState
    errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, state: _Optional[_Union[ImportEntriesMetadata.ImportState, str]] = ..., errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class ModifyEntryOverviewRequest(_message.Message):
    __slots__ = ("name", "entry_overview")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    entry_overview: EntryOverview
    def __init__(self, name: _Optional[str] = ..., entry_overview: _Optional[_Union[EntryOverview, _Mapping]] = ...) -> None: ...

class ModifyEntryContactsRequest(_message.Message):
    __slots__ = ("name", "contacts")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    contacts: Contacts
    def __init__(self, name: _Optional[str] = ..., contacts: _Optional[_Union[Contacts, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("name", "tag_template_migration", "catalog_ui_experience")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    CATALOG_UI_EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    tag_template_migration: TagTemplateMigration
    catalog_ui_experience: CatalogUIExperience
    def __init__(self, name: _Optional[str] = ..., tag_template_migration: _Optional[_Union[TagTemplateMigration, str]] = ..., catalog_ui_experience: _Optional[_Union[CatalogUIExperience, str]] = ...) -> None: ...

class RetrieveConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RetrieveEffectiveConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class OrganizationConfig(_message.Message):
    __slots__ = ("config",)
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MigrationConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MigrationConfig, _Mapping]] = ...) -> None: ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _containers.MessageMap[str, MigrationConfig]
    def __init__(self, config: _Optional[_Mapping[str, MigrationConfig]] = ...) -> None: ...

class MigrationConfig(_message.Message):
    __slots__ = ("tag_template_migration", "catalog_ui_experience")
    TAG_TEMPLATE_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    CATALOG_UI_EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    tag_template_migration: TagTemplateMigration
    catalog_ui_experience: CatalogUIExperience
    def __init__(self, tag_template_migration: _Optional[_Union[TagTemplateMigration, str]] = ..., catalog_ui_experience: _Optional[_Union[CatalogUIExperience, str]] = ...) -> None: ...
