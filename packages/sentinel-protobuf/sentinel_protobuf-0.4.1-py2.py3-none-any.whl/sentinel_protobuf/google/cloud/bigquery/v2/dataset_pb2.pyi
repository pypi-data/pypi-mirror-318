from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.bigquery.v2 import dataset_reference_pb2 as _dataset_reference_pb2
from google.cloud.bigquery.v2 import encryption_config_pb2 as _encryption_config_pb2
from google.cloud.bigquery.v2 import external_catalog_dataset_options_pb2 as _external_catalog_dataset_options_pb2
from google.cloud.bigquery.v2 import external_dataset_reference_pb2 as _external_dataset_reference_pb2
from google.cloud.bigquery.v2 import restriction_config_pb2 as _restriction_config_pb2
from google.cloud.bigquery.v2 import routine_reference_pb2 as _routine_reference_pb2
from google.cloud.bigquery.v2 import table_reference_pb2 as _table_reference_pb2
from google.cloud.bigquery.v2 import table_schema_pb2 as _table_schema_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatasetAccessEntry(_message.Message):
    __slots__ = ("dataset", "target_types")
    class TargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARGET_TYPE_UNSPECIFIED: _ClassVar[DatasetAccessEntry.TargetType]
        VIEWS: _ClassVar[DatasetAccessEntry.TargetType]
        ROUTINES: _ClassVar[DatasetAccessEntry.TargetType]
    TARGET_TYPE_UNSPECIFIED: DatasetAccessEntry.TargetType
    VIEWS: DatasetAccessEntry.TargetType
    ROUTINES: DatasetAccessEntry.TargetType
    DATASET_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    dataset: _dataset_reference_pb2.DatasetReference
    target_types: _containers.RepeatedScalarFieldContainer[DatasetAccessEntry.TargetType]
    def __init__(self, dataset: _Optional[_Union[_dataset_reference_pb2.DatasetReference, _Mapping]] = ..., target_types: _Optional[_Iterable[_Union[DatasetAccessEntry.TargetType, str]]] = ...) -> None: ...

class Access(_message.Message):
    __slots__ = ("role", "user_by_email", "group_by_email", "domain", "special_group", "iam_member", "view", "routine", "dataset", "condition")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USER_BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_GROUP_FIELD_NUMBER: _ClassVar[int]
    IAM_MEMBER_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    role: str
    user_by_email: str
    group_by_email: str
    domain: str
    special_group: str
    iam_member: str
    view: _table_reference_pb2.TableReference
    routine: _routine_reference_pb2.RoutineReference
    dataset: DatasetAccessEntry
    condition: _expr_pb2.Expr
    def __init__(self, role: _Optional[str] = ..., user_by_email: _Optional[str] = ..., group_by_email: _Optional[str] = ..., domain: _Optional[str] = ..., special_group: _Optional[str] = ..., iam_member: _Optional[str] = ..., view: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., routine: _Optional[_Union[_routine_reference_pb2.RoutineReference, _Mapping]] = ..., dataset: _Optional[_Union[DatasetAccessEntry, _Mapping]] = ..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]] = ...) -> None: ...

class Dataset(_message.Message):
    __slots__ = ("kind", "etag", "id", "self_link", "dataset_reference", "friendly_name", "description", "default_table_expiration_ms", "default_partition_expiration_ms", "labels", "access", "creation_time", "last_modified_time", "location", "default_encryption_configuration", "satisfies_pzs", "satisfies_pzi", "type", "linked_dataset_source", "linked_dataset_metadata", "external_dataset_reference", "external_catalog_dataset_options", "is_case_insensitive", "default_collation", "default_rounding_mode", "max_time_travel_hours", "tags", "storage_billing_model", "restrictions", "resource_tags")
    class StorageBillingModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_BILLING_MODEL_UNSPECIFIED: _ClassVar[Dataset.StorageBillingModel]
        LOGICAL: _ClassVar[Dataset.StorageBillingModel]
        PHYSICAL: _ClassVar[Dataset.StorageBillingModel]
    STORAGE_BILLING_MODEL_UNSPECIFIED: Dataset.StorageBillingModel
    LOGICAL: Dataset.StorageBillingModel
    PHYSICAL: Dataset.StorageBillingModel
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ResourceTagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    DATASET_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TABLE_EXPIRATION_MS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PARTITION_EXPIRATION_MS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LINKED_DATASET_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LINKED_DATASET_METADATA_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DATASET_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CATALOG_DATASET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COLLATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROUNDING_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_TIME_TRAVEL_HOURS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BILLING_MODEL_FIELD_NUMBER: _ClassVar[int]
    RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TAGS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    etag: str
    id: str
    self_link: str
    dataset_reference: _dataset_reference_pb2.DatasetReference
    friendly_name: _wrappers_pb2.StringValue
    description: _wrappers_pb2.StringValue
    default_table_expiration_ms: _wrappers_pb2.Int64Value
    default_partition_expiration_ms: _wrappers_pb2.Int64Value
    labels: _containers.ScalarMap[str, str]
    access: _containers.RepeatedCompositeFieldContainer[Access]
    creation_time: int
    last_modified_time: int
    location: str
    default_encryption_configuration: _encryption_config_pb2.EncryptionConfiguration
    satisfies_pzs: _wrappers_pb2.BoolValue
    satisfies_pzi: _wrappers_pb2.BoolValue
    type: str
    linked_dataset_source: LinkedDatasetSource
    linked_dataset_metadata: LinkedDatasetMetadata
    external_dataset_reference: _external_dataset_reference_pb2.ExternalDatasetReference
    external_catalog_dataset_options: _external_catalog_dataset_options_pb2.ExternalCatalogDatasetOptions
    is_case_insensitive: _wrappers_pb2.BoolValue
    default_collation: _wrappers_pb2.StringValue
    default_rounding_mode: _table_schema_pb2.TableFieldSchema.RoundingMode
    max_time_travel_hours: _wrappers_pb2.Int64Value
    tags: _containers.RepeatedCompositeFieldContainer[GcpTag]
    storage_billing_model: Dataset.StorageBillingModel
    restrictions: _restriction_config_pb2.RestrictionConfig
    resource_tags: _containers.ScalarMap[str, str]
    def __init__(self, kind: _Optional[str] = ..., etag: _Optional[str] = ..., id: _Optional[str] = ..., self_link: _Optional[str] = ..., dataset_reference: _Optional[_Union[_dataset_reference_pb2.DatasetReference, _Mapping]] = ..., friendly_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., default_table_expiration_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., default_partition_expiration_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., access: _Optional[_Iterable[_Union[Access, _Mapping]]] = ..., creation_time: _Optional[int] = ..., last_modified_time: _Optional[int] = ..., location: _Optional[str] = ..., default_encryption_configuration: _Optional[_Union[_encryption_config_pb2.EncryptionConfiguration, _Mapping]] = ..., satisfies_pzs: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., satisfies_pzi: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., type: _Optional[str] = ..., linked_dataset_source: _Optional[_Union[LinkedDatasetSource, _Mapping]] = ..., linked_dataset_metadata: _Optional[_Union[LinkedDatasetMetadata, _Mapping]] = ..., external_dataset_reference: _Optional[_Union[_external_dataset_reference_pb2.ExternalDatasetReference, _Mapping]] = ..., external_catalog_dataset_options: _Optional[_Union[_external_catalog_dataset_options_pb2.ExternalCatalogDatasetOptions, _Mapping]] = ..., is_case_insensitive: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., default_collation: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., default_rounding_mode: _Optional[_Union[_table_schema_pb2.TableFieldSchema.RoundingMode, str]] = ..., max_time_travel_hours: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[GcpTag, _Mapping]]] = ..., storage_billing_model: _Optional[_Union[Dataset.StorageBillingModel, str]] = ..., restrictions: _Optional[_Union[_restriction_config_pb2.RestrictionConfig, _Mapping]] = ..., resource_tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GcpTag(_message.Message):
    __slots__ = ("tag_key", "tag_value")
    TAG_KEY_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    tag_key: str
    tag_value: str
    def __init__(self, tag_key: _Optional[str] = ..., tag_value: _Optional[str] = ...) -> None: ...

class LinkedDatasetSource(_message.Message):
    __slots__ = ("source_dataset",)
    SOURCE_DATASET_FIELD_NUMBER: _ClassVar[int]
    source_dataset: _dataset_reference_pb2.DatasetReference
    def __init__(self, source_dataset: _Optional[_Union[_dataset_reference_pb2.DatasetReference, _Mapping]] = ...) -> None: ...

class LinkedDatasetMetadata(_message.Message):
    __slots__ = ("link_state",)
    class LinkState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LINK_STATE_UNSPECIFIED: _ClassVar[LinkedDatasetMetadata.LinkState]
        LINKED: _ClassVar[LinkedDatasetMetadata.LinkState]
        UNLINKED: _ClassVar[LinkedDatasetMetadata.LinkState]
    LINK_STATE_UNSPECIFIED: LinkedDatasetMetadata.LinkState
    LINKED: LinkedDatasetMetadata.LinkState
    UNLINKED: LinkedDatasetMetadata.LinkState
    LINK_STATE_FIELD_NUMBER: _ClassVar[int]
    link_state: LinkedDatasetMetadata.LinkState
    def __init__(self, link_state: _Optional[_Union[LinkedDatasetMetadata.LinkState, str]] = ...) -> None: ...

class GetDatasetRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "dataset_view", "access_policy_version")
    class DatasetView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATASET_VIEW_UNSPECIFIED: _ClassVar[GetDatasetRequest.DatasetView]
        METADATA: _ClassVar[GetDatasetRequest.DatasetView]
        ACL: _ClassVar[GetDatasetRequest.DatasetView]
        FULL: _ClassVar[GetDatasetRequest.DatasetView]
    DATASET_VIEW_UNSPECIFIED: GetDatasetRequest.DatasetView
    METADATA: GetDatasetRequest.DatasetView
    ACL: GetDatasetRequest.DatasetView
    FULL: GetDatasetRequest.DatasetView
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VIEW_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    dataset_view: GetDatasetRequest.DatasetView
    access_policy_version: int
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., dataset_view: _Optional[_Union[GetDatasetRequest.DatasetView, str]] = ..., access_policy_version: _Optional[int] = ...) -> None: ...

class InsertDatasetRequest(_message.Message):
    __slots__ = ("project_id", "dataset", "access_policy_version")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset: Dataset
    access_policy_version: int
    def __init__(self, project_id: _Optional[str] = ..., dataset: _Optional[_Union[Dataset, _Mapping]] = ..., access_policy_version: _Optional[int] = ...) -> None: ...

class UpdateOrPatchDatasetRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "dataset", "access_policy_version")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    dataset: Dataset
    access_policy_version: int
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., dataset: _Optional[_Union[Dataset, _Mapping]] = ..., access_policy_version: _Optional[int] = ...) -> None: ...

class DeleteDatasetRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "delete_contents")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    delete_contents: bool
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., delete_contents: bool = ...) -> None: ...

class ListDatasetsRequest(_message.Message):
    __slots__ = ("project_id", "max_results", "page_token", "all", "filter")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    max_results: _wrappers_pb2.UInt32Value
    page_token: str
    all: bool
    filter: str
    def __init__(self, project_id: _Optional[str] = ..., max_results: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., page_token: _Optional[str] = ..., all: bool = ..., filter: _Optional[str] = ...) -> None: ...

class ListFormatDataset(_message.Message):
    __slots__ = ("kind", "id", "dataset_reference", "labels", "friendly_name", "location")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    id: str
    dataset_reference: _dataset_reference_pb2.DatasetReference
    labels: _containers.ScalarMap[str, str]
    friendly_name: _wrappers_pb2.StringValue
    location: str
    def __init__(self, kind: _Optional[str] = ..., id: _Optional[str] = ..., dataset_reference: _Optional[_Union[_dataset_reference_pb2.DatasetReference, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., friendly_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., location: _Optional[str] = ...) -> None: ...

class DatasetList(_message.Message):
    __slots__ = ("kind", "etag", "next_page_token", "datasets", "unreachable")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    etag: str
    next_page_token: str
    datasets: _containers.RepeatedCompositeFieldContainer[ListFormatDataset]
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, kind: _Optional[str] = ..., etag: _Optional[str] = ..., next_page_token: _Optional[str] = ..., datasets: _Optional[_Iterable[_Union[ListFormatDataset, _Mapping]]] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class UndeleteDatasetRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "deletion_time")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DELETION_TIME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    deletion_time: _timestamp_pb2.Timestamp
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., deletion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
