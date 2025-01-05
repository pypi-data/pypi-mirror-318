from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.datacatalog.v1beta1 import common_pb2 as _common_pb2
from google.cloud.datacatalog.v1beta1 import gcs_fileset_spec_pb2 as _gcs_fileset_spec_pb2
from google.cloud.datacatalog.v1beta1 import schema_pb2 as _schema_pb2
from google.cloud.datacatalog.v1beta1 import search_pb2 as _search_pb2
from google.cloud.datacatalog.v1beta1 import table_spec_pb2 as _table_spec_pb2
from google.cloud.datacatalog.v1beta1 import tags_pb2 as _tags_pb2
from google.cloud.datacatalog.v1beta1 import timestamps_pb2 as _timestamps_pb2
from google.cloud.datacatalog.v1beta1 import usage_pb2 as _usage_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
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
ENTRY_TYPE_UNSPECIFIED: EntryType
TABLE: EntryType
MODEL: EntryType
DATA_STREAM: EntryType
FILESET: EntryType

class SearchCatalogRequest(_message.Message):
    __slots__ = ('scope', 'query', 'page_size', 'page_token', 'order_by')

    class Scope(_message.Message):
        __slots__ = ('include_org_ids', 'include_project_ids', 'include_gcp_public_datasets', 'restricted_locations')
        INCLUDE_ORG_IDS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_PROJECT_IDS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_GCP_PUBLIC_DATASETS_FIELD_NUMBER: _ClassVar[int]
        RESTRICTED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        include_org_ids: _containers.RepeatedScalarFieldContainer[str]
        include_project_ids: _containers.RepeatedScalarFieldContainer[str]
        include_gcp_public_datasets: bool
        restricted_locations: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, include_org_ids: _Optional[_Iterable[str]]=..., include_project_ids: _Optional[_Iterable[str]]=..., include_gcp_public_datasets: bool=..., restricted_locations: _Optional[_Iterable[str]]=...) -> None:
            ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    scope: SearchCatalogRequest.Scope
    query: str
    page_size: int
    page_token: str
    order_by: str

    def __init__(self, scope: _Optional[_Union[SearchCatalogRequest.Scope, _Mapping]]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class SearchCatalogResponse(_message.Message):
    __slots__ = ('results', 'total_size', 'next_page_token', 'unreachable')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_search_pb2.SearchCatalogResult]
    total_size: int
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, results: _Optional[_Iterable[_Union[_search_pb2.SearchCatalogResult, _Mapping]]]=..., total_size: _Optional[int]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateEntryGroupRequest(_message.Message):
    __slots__ = ('parent', 'entry_group_id', 'entry_group')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_GROUP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entry_group_id: str
    entry_group: EntryGroup

    def __init__(self, parent: _Optional[str]=..., entry_group_id: _Optional[str]=..., entry_group: _Optional[_Union[EntryGroup, _Mapping]]=...) -> None:
        ...

class UpdateEntryGroupRequest(_message.Message):
    __slots__ = ('entry_group', 'update_mask')
    ENTRY_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    entry_group: EntryGroup
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, entry_group: _Optional[_Union[EntryGroup, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetEntryGroupRequest(_message.Message):
    __slots__ = ('name', 'read_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteEntryGroupRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListEntryGroupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEntryGroupsResponse(_message.Message):
    __slots__ = ('entry_groups', 'next_page_token')
    ENTRY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entry_groups: _containers.RepeatedCompositeFieldContainer[EntryGroup]
    next_page_token: str

    def __init__(self, entry_groups: _Optional[_Iterable[_Union[EntryGroup, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateEntryRequest(_message.Message):
    __slots__ = ('parent', 'entry_id', 'entry')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entry_id: str
    entry: Entry

    def __init__(self, parent: _Optional[str]=..., entry_id: _Optional[str]=..., entry: _Optional[_Union[Entry, _Mapping]]=...) -> None:
        ...

class UpdateEntryRequest(_message.Message):
    __slots__ = ('entry', 'update_mask')
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    entry: Entry
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, entry: _Optional[_Union[Entry, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteEntryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetEntryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LookupEntryRequest(_message.Message):
    __slots__ = ('linked_resource', 'sql_resource')
    LINKED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SQL_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    linked_resource: str
    sql_resource: str

    def __init__(self, linked_resource: _Optional[str]=..., sql_resource: _Optional[str]=...) -> None:
        ...

class Entry(_message.Message):
    __slots__ = ('name', 'linked_resource', 'type', 'user_specified_type', 'integrated_system', 'user_specified_system', 'gcs_fileset_spec', 'bigquery_table_spec', 'bigquery_date_sharded_spec', 'display_name', 'description', 'schema', 'source_system_timestamps', 'usage_signal')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINKED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_SPECIFIED_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATED_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    USER_SPECIFIED_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    GCS_FILESET_SPEC_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_TABLE_SPEC_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DATE_SHARDED_SPEC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYSTEM_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    USAGE_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    linked_resource: str
    type: EntryType
    user_specified_type: str
    integrated_system: _common_pb2.IntegratedSystem
    user_specified_system: str
    gcs_fileset_spec: _gcs_fileset_spec_pb2.GcsFilesetSpec
    bigquery_table_spec: _table_spec_pb2.BigQueryTableSpec
    bigquery_date_sharded_spec: _table_spec_pb2.BigQueryDateShardedSpec
    display_name: str
    description: str
    schema: _schema_pb2.Schema
    source_system_timestamps: _timestamps_pb2.SystemTimestamps
    usage_signal: _usage_pb2.UsageSignal

    def __init__(self, name: _Optional[str]=..., linked_resource: _Optional[str]=..., type: _Optional[_Union[EntryType, str]]=..., user_specified_type: _Optional[str]=..., integrated_system: _Optional[_Union[_common_pb2.IntegratedSystem, str]]=..., user_specified_system: _Optional[str]=..., gcs_fileset_spec: _Optional[_Union[_gcs_fileset_spec_pb2.GcsFilesetSpec, _Mapping]]=..., bigquery_table_spec: _Optional[_Union[_table_spec_pb2.BigQueryTableSpec, _Mapping]]=..., bigquery_date_sharded_spec: _Optional[_Union[_table_spec_pb2.BigQueryDateShardedSpec, _Mapping]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., schema: _Optional[_Union[_schema_pb2.Schema, _Mapping]]=..., source_system_timestamps: _Optional[_Union[_timestamps_pb2.SystemTimestamps, _Mapping]]=..., usage_signal: _Optional[_Union[_usage_pb2.UsageSignal, _Mapping]]=...) -> None:
        ...

class EntryGroup(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'data_catalog_timestamps')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATA_CATALOG_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    data_catalog_timestamps: _timestamps_pb2.SystemTimestamps

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., data_catalog_timestamps: _Optional[_Union[_timestamps_pb2.SystemTimestamps, _Mapping]]=...) -> None:
        ...

class CreateTagTemplateRequest(_message.Message):
    __slots__ = ('parent', 'tag_template_id', 'tag_template')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tag_template_id: str
    tag_template: _tags_pb2.TagTemplate

    def __init__(self, parent: _Optional[str]=..., tag_template_id: _Optional[str]=..., tag_template: _Optional[_Union[_tags_pb2.TagTemplate, _Mapping]]=...) -> None:
        ...

class GetTagTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateTagTemplateRequest(_message.Message):
    __slots__ = ('tag_template', 'update_mask')
    TAG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tag_template: _tags_pb2.TagTemplate
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, tag_template: _Optional[_Union[_tags_pb2.TagTemplate, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteTagTemplateRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class CreateTagRequest(_message.Message):
    __slots__ = ('parent', 'tag')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tag: _tags_pb2.Tag

    def __init__(self, parent: _Optional[str]=..., tag: _Optional[_Union[_tags_pb2.Tag, _Mapping]]=...) -> None:
        ...

class UpdateTagRequest(_message.Message):
    __slots__ = ('tag', 'update_mask')
    TAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tag: _tags_pb2.Tag
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, tag: _Optional[_Union[_tags_pb2.Tag, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteTagRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTagTemplateFieldRequest(_message.Message):
    __slots__ = ('parent', 'tag_template_field_id', 'tag_template_field')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_FIELD_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tag_template_field_id: str
    tag_template_field: _tags_pb2.TagTemplateField

    def __init__(self, parent: _Optional[str]=..., tag_template_field_id: _Optional[str]=..., tag_template_field: _Optional[_Union[_tags_pb2.TagTemplateField, _Mapping]]=...) -> None:
        ...

class UpdateTagTemplateFieldRequest(_message.Message):
    __slots__ = ('name', 'tag_template_field', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_TEMPLATE_FIELD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    tag_template_field: _tags_pb2.TagTemplateField
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., tag_template_field: _Optional[_Union[_tags_pb2.TagTemplateField, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class RenameTagTemplateFieldRequest(_message.Message):
    __slots__ = ('name', 'new_tag_template_field_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_TAG_TEMPLATE_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_tag_template_field_id: str

    def __init__(self, name: _Optional[str]=..., new_tag_template_field_id: _Optional[str]=...) -> None:
        ...

class RenameTagTemplateFieldEnumValueRequest(_message.Message):
    __slots__ = ('name', 'new_enum_value_display_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_ENUM_VALUE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_enum_value_display_name: str

    def __init__(self, name: _Optional[str]=..., new_enum_value_display_name: _Optional[str]=...) -> None:
        ...

class DeleteTagTemplateFieldRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListTagsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTagsResponse(_message.Message):
    __slots__ = ('tags', 'next_page_token')
    TAGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[_tags_pb2.Tag]
    next_page_token: str

    def __init__(self, tags: _Optional[_Iterable[_Union[_tags_pb2.Tag, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListEntriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListEntriesResponse(_message.Message):
    __slots__ = ('entries', 'next_page_token')
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[Entry]
    next_page_token: str

    def __init__(self, entries: _Optional[_Iterable[_Union[Entry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...