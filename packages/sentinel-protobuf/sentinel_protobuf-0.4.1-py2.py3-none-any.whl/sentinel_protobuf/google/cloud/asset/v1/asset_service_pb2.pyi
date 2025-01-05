from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.asset.v1 import assets_pb2 as _assets_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_TYPE_UNSPECIFIED: _ClassVar[ContentType]
    RESOURCE: _ClassVar[ContentType]
    IAM_POLICY: _ClassVar[ContentType]
    ORG_POLICY: _ClassVar[ContentType]
    ACCESS_POLICY: _ClassVar[ContentType]
    OS_INVENTORY: _ClassVar[ContentType]
    RELATIONSHIP: _ClassVar[ContentType]
CONTENT_TYPE_UNSPECIFIED: ContentType
RESOURCE: ContentType
IAM_POLICY: ContentType
ORG_POLICY: ContentType
ACCESS_POLICY: ContentType
OS_INVENTORY: ContentType
RELATIONSHIP: ContentType

class AnalyzeIamPolicyLongrunningMetadata(_message.Message):
    __slots__ = ("create_time",)
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExportAssetsRequest(_message.Message):
    __slots__ = ("parent", "read_time", "asset_types", "content_type", "output_config", "relationship_types")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    read_time: _timestamp_pb2.Timestamp
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    content_type: ContentType
    output_config: OutputConfig
    relationship_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., asset_types: _Optional[_Iterable[str]] = ..., content_type: _Optional[_Union[ContentType, str]] = ..., output_config: _Optional[_Union[OutputConfig, _Mapping]] = ..., relationship_types: _Optional[_Iterable[str]] = ...) -> None: ...

class ExportAssetsResponse(_message.Message):
    __slots__ = ("read_time", "output_config", "output_result")
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_RESULT_FIELD_NUMBER: _ClassVar[int]
    read_time: _timestamp_pb2.Timestamp
    output_config: OutputConfig
    output_result: OutputResult
    def __init__(self, read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., output_config: _Optional[_Union[OutputConfig, _Mapping]] = ..., output_result: _Optional[_Union[OutputResult, _Mapping]] = ...) -> None: ...

class ListAssetsRequest(_message.Message):
    __slots__ = ("parent", "read_time", "asset_types", "content_type", "page_size", "page_token", "relationship_types")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    read_time: _timestamp_pb2.Timestamp
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    content_type: ContentType
    page_size: int
    page_token: str
    relationship_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., asset_types: _Optional[_Iterable[str]] = ..., content_type: _Optional[_Union[ContentType, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., relationship_types: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAssetsResponse(_message.Message):
    __slots__ = ("read_time", "assets", "next_page_token")
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    read_time: _timestamp_pb2.Timestamp
    assets: _containers.RepeatedCompositeFieldContainer[_assets_pb2.Asset]
    next_page_token: str
    def __init__(self, read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assets: _Optional[_Iterable[_Union[_assets_pb2.Asset, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class BatchGetAssetsHistoryRequest(_message.Message):
    __slots__ = ("parent", "asset_names", "content_type", "read_time_window", "relationship_types")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ASSET_NAMES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    asset_names: _containers.RepeatedScalarFieldContainer[str]
    content_type: ContentType
    read_time_window: _assets_pb2.TimeWindow
    relationship_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., asset_names: _Optional[_Iterable[str]] = ..., content_type: _Optional[_Union[ContentType, str]] = ..., read_time_window: _Optional[_Union[_assets_pb2.TimeWindow, _Mapping]] = ..., relationship_types: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchGetAssetsHistoryResponse(_message.Message):
    __slots__ = ("assets",)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[_assets_pb2.TemporalAsset]
    def __init__(self, assets: _Optional[_Iterable[_Union[_assets_pb2.TemporalAsset, _Mapping]]] = ...) -> None: ...

class CreateFeedRequest(_message.Message):
    __slots__ = ("parent", "feed_id", "feed")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEED_ID_FIELD_NUMBER: _ClassVar[int]
    FEED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feed_id: str
    feed: Feed
    def __init__(self, parent: _Optional[str] = ..., feed_id: _Optional[str] = ..., feed: _Optional[_Union[Feed, _Mapping]] = ...) -> None: ...

class GetFeedRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListFeedsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListFeedsResponse(_message.Message):
    __slots__ = ("feeds",)
    FEEDS_FIELD_NUMBER: _ClassVar[int]
    feeds: _containers.RepeatedCompositeFieldContainer[Feed]
    def __init__(self, feeds: _Optional[_Iterable[_Union[Feed, _Mapping]]] = ...) -> None: ...

class UpdateFeedRequest(_message.Message):
    __slots__ = ("feed", "update_mask")
    FEED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    feed: Feed
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, feed: _Optional[_Union[Feed, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteFeedRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class OutputConfig(_message.Message):
    __slots__ = ("gcs_destination", "bigquery_destination")
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    bigquery_destination: BigQueryDestination
    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]] = ..., bigquery_destination: _Optional[_Union[BigQueryDestination, _Mapping]] = ...) -> None: ...

class OutputResult(_message.Message):
    __slots__ = ("gcs_result",)
    GCS_RESULT_FIELD_NUMBER: _ClassVar[int]
    gcs_result: GcsOutputResult
    def __init__(self, gcs_result: _Optional[_Union[GcsOutputResult, _Mapping]] = ...) -> None: ...

class GcsOutputResult(_message.Message):
    __slots__ = ("uris",)
    URIS_FIELD_NUMBER: _ClassVar[int]
    uris: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uris: _Optional[_Iterable[str]] = ...) -> None: ...

class GcsDestination(_message.Message):
    __slots__ = ("uri", "uri_prefix")
    URI_FIELD_NUMBER: _ClassVar[int]
    URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    uri: str
    uri_prefix: str
    def __init__(self, uri: _Optional[str] = ..., uri_prefix: _Optional[str] = ...) -> None: ...

class BigQueryDestination(_message.Message):
    __slots__ = ("dataset", "table", "force", "partition_spec", "separate_tables_per_asset_type")
    DATASET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SEPARATE_TABLES_PER_ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    table: str
    force: bool
    partition_spec: PartitionSpec
    separate_tables_per_asset_type: bool
    def __init__(self, dataset: _Optional[str] = ..., table: _Optional[str] = ..., force: bool = ..., partition_spec: _Optional[_Union[PartitionSpec, _Mapping]] = ..., separate_tables_per_asset_type: bool = ...) -> None: ...

class PartitionSpec(_message.Message):
    __slots__ = ("partition_key",)
    class PartitionKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTITION_KEY_UNSPECIFIED: _ClassVar[PartitionSpec.PartitionKey]
        READ_TIME: _ClassVar[PartitionSpec.PartitionKey]
        REQUEST_TIME: _ClassVar[PartitionSpec.PartitionKey]
    PARTITION_KEY_UNSPECIFIED: PartitionSpec.PartitionKey
    READ_TIME: PartitionSpec.PartitionKey
    REQUEST_TIME: PartitionSpec.PartitionKey
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    partition_key: PartitionSpec.PartitionKey
    def __init__(self, partition_key: _Optional[_Union[PartitionSpec.PartitionKey, str]] = ...) -> None: ...

class PubsubDestination(_message.Message):
    __slots__ = ("topic",)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str
    def __init__(self, topic: _Optional[str] = ...) -> None: ...

class FeedOutputConfig(_message.Message):
    __slots__ = ("pubsub_destination",)
    PUBSUB_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    pubsub_destination: PubsubDestination
    def __init__(self, pubsub_destination: _Optional[_Union[PubsubDestination, _Mapping]] = ...) -> None: ...

class Feed(_message.Message):
    __slots__ = ("name", "asset_names", "asset_types", "content_type", "feed_output_config", "condition", "relationship_types")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_NAMES_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FEED_OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    asset_names: _containers.RepeatedScalarFieldContainer[str]
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    content_type: ContentType
    feed_output_config: FeedOutputConfig
    condition: _expr_pb2.Expr
    relationship_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., asset_names: _Optional[_Iterable[str]] = ..., asset_types: _Optional[_Iterable[str]] = ..., content_type: _Optional[_Union[ContentType, str]] = ..., feed_output_config: _Optional[_Union[FeedOutputConfig, _Mapping]] = ..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]] = ..., relationship_types: _Optional[_Iterable[str]] = ...) -> None: ...

class SearchAllResourcesRequest(_message.Message):
    __slots__ = ("scope", "query", "asset_types", "page_size", "page_token", "order_by", "read_mask")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    scope: str
    query: str
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, scope: _Optional[str] = ..., query: _Optional[str] = ..., asset_types: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SearchAllResourcesResponse(_message.Message):
    __slots__ = ("results", "next_page_token")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_assets_pb2.ResourceSearchResult]
    next_page_token: str
    def __init__(self, results: _Optional[_Iterable[_Union[_assets_pb2.ResourceSearchResult, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SearchAllIamPoliciesRequest(_message.Message):
    __slots__ = ("scope", "query", "page_size", "page_token", "asset_types", "order_by")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    scope: str
    query: str
    page_size: int
    page_token: str
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    order_by: str
    def __init__(self, scope: _Optional[str] = ..., query: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., asset_types: _Optional[_Iterable[str]] = ..., order_by: _Optional[str] = ...) -> None: ...

class SearchAllIamPoliciesResponse(_message.Message):
    __slots__ = ("results", "next_page_token")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_assets_pb2.IamPolicySearchResult]
    next_page_token: str
    def __init__(self, results: _Optional[_Iterable[_Union[_assets_pb2.IamPolicySearchResult, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class IamPolicyAnalysisQuery(_message.Message):
    __slots__ = ("scope", "resource_selector", "identity_selector", "access_selector", "options", "condition_context")
    class ResourceSelector(_message.Message):
        __slots__ = ("full_resource_name",)
        FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        full_resource_name: str
        def __init__(self, full_resource_name: _Optional[str] = ...) -> None: ...
    class IdentitySelector(_message.Message):
        __slots__ = ("identity",)
        IDENTITY_FIELD_NUMBER: _ClassVar[int]
        identity: str
        def __init__(self, identity: _Optional[str] = ...) -> None: ...
    class AccessSelector(_message.Message):
        __slots__ = ("roles", "permissions")
        ROLES_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        roles: _containers.RepeatedScalarFieldContainer[str]
        permissions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, roles: _Optional[_Iterable[str]] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...
    class Options(_message.Message):
        __slots__ = ("expand_groups", "expand_roles", "expand_resources", "output_resource_edges", "output_group_edges", "analyze_service_account_impersonation")
        EXPAND_GROUPS_FIELD_NUMBER: _ClassVar[int]
        EXPAND_ROLES_FIELD_NUMBER: _ClassVar[int]
        EXPAND_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_RESOURCE_EDGES_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_GROUP_EDGES_FIELD_NUMBER: _ClassVar[int]
        ANALYZE_SERVICE_ACCOUNT_IMPERSONATION_FIELD_NUMBER: _ClassVar[int]
        expand_groups: bool
        expand_roles: bool
        expand_resources: bool
        output_resource_edges: bool
        output_group_edges: bool
        analyze_service_account_impersonation: bool
        def __init__(self, expand_groups: bool = ..., expand_roles: bool = ..., expand_resources: bool = ..., output_resource_edges: bool = ..., output_group_edges: bool = ..., analyze_service_account_impersonation: bool = ...) -> None: ...
    class ConditionContext(_message.Message):
        __slots__ = ("access_time",)
        ACCESS_TIME_FIELD_NUMBER: _ClassVar[int]
        access_time: _timestamp_pb2.Timestamp
        def __init__(self, access_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    ACCESS_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    scope: str
    resource_selector: IamPolicyAnalysisQuery.ResourceSelector
    identity_selector: IamPolicyAnalysisQuery.IdentitySelector
    access_selector: IamPolicyAnalysisQuery.AccessSelector
    options: IamPolicyAnalysisQuery.Options
    condition_context: IamPolicyAnalysisQuery.ConditionContext
    def __init__(self, scope: _Optional[str] = ..., resource_selector: _Optional[_Union[IamPolicyAnalysisQuery.ResourceSelector, _Mapping]] = ..., identity_selector: _Optional[_Union[IamPolicyAnalysisQuery.IdentitySelector, _Mapping]] = ..., access_selector: _Optional[_Union[IamPolicyAnalysisQuery.AccessSelector, _Mapping]] = ..., options: _Optional[_Union[IamPolicyAnalysisQuery.Options, _Mapping]] = ..., condition_context: _Optional[_Union[IamPolicyAnalysisQuery.ConditionContext, _Mapping]] = ...) -> None: ...

class AnalyzeIamPolicyRequest(_message.Message):
    __slots__ = ("analysis_query", "saved_analysis_query", "execution_timeout")
    ANALYSIS_QUERY_FIELD_NUMBER: _ClassVar[int]
    SAVED_ANALYSIS_QUERY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    analysis_query: IamPolicyAnalysisQuery
    saved_analysis_query: str
    execution_timeout: _duration_pb2.Duration
    def __init__(self, analysis_query: _Optional[_Union[IamPolicyAnalysisQuery, _Mapping]] = ..., saved_analysis_query: _Optional[str] = ..., execution_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class AnalyzeIamPolicyResponse(_message.Message):
    __slots__ = ("main_analysis", "service_account_impersonation_analysis", "fully_explored")
    class IamPolicyAnalysis(_message.Message):
        __slots__ = ("analysis_query", "analysis_results", "fully_explored", "non_critical_errors")
        ANALYSIS_QUERY_FIELD_NUMBER: _ClassVar[int]
        ANALYSIS_RESULTS_FIELD_NUMBER: _ClassVar[int]
        FULLY_EXPLORED_FIELD_NUMBER: _ClassVar[int]
        NON_CRITICAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
        analysis_query: IamPolicyAnalysisQuery
        analysis_results: _containers.RepeatedCompositeFieldContainer[_assets_pb2.IamPolicyAnalysisResult]
        fully_explored: bool
        non_critical_errors: _containers.RepeatedCompositeFieldContainer[_assets_pb2.IamPolicyAnalysisState]
        def __init__(self, analysis_query: _Optional[_Union[IamPolicyAnalysisQuery, _Mapping]] = ..., analysis_results: _Optional[_Iterable[_Union[_assets_pb2.IamPolicyAnalysisResult, _Mapping]]] = ..., fully_explored: bool = ..., non_critical_errors: _Optional[_Iterable[_Union[_assets_pb2.IamPolicyAnalysisState, _Mapping]]] = ...) -> None: ...
    MAIN_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_IMPERSONATION_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    FULLY_EXPLORED_FIELD_NUMBER: _ClassVar[int]
    main_analysis: AnalyzeIamPolicyResponse.IamPolicyAnalysis
    service_account_impersonation_analysis: _containers.RepeatedCompositeFieldContainer[AnalyzeIamPolicyResponse.IamPolicyAnalysis]
    fully_explored: bool
    def __init__(self, main_analysis: _Optional[_Union[AnalyzeIamPolicyResponse.IamPolicyAnalysis, _Mapping]] = ..., service_account_impersonation_analysis: _Optional[_Iterable[_Union[AnalyzeIamPolicyResponse.IamPolicyAnalysis, _Mapping]]] = ..., fully_explored: bool = ...) -> None: ...

class IamPolicyAnalysisOutputConfig(_message.Message):
    __slots__ = ("gcs_destination", "bigquery_destination")
    class GcsDestination(_message.Message):
        __slots__ = ("uri",)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str
        def __init__(self, uri: _Optional[str] = ...) -> None: ...
    class BigQueryDestination(_message.Message):
        __slots__ = ("dataset", "table_prefix", "partition_key", "write_disposition")
        class PartitionKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PARTITION_KEY_UNSPECIFIED: _ClassVar[IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey]
            REQUEST_TIME: _ClassVar[IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey]
        PARTITION_KEY_UNSPECIFIED: IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey
        REQUEST_TIME: IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey
        DATASET_FIELD_NUMBER: _ClassVar[int]
        TABLE_PREFIX_FIELD_NUMBER: _ClassVar[int]
        PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
        WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        table_prefix: str
        partition_key: IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey
        write_disposition: str
        def __init__(self, dataset: _Optional[str] = ..., table_prefix: _Optional[str] = ..., partition_key: _Optional[_Union[IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey, str]] = ..., write_disposition: _Optional[str] = ...) -> None: ...
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: IamPolicyAnalysisOutputConfig.GcsDestination
    bigquery_destination: IamPolicyAnalysisOutputConfig.BigQueryDestination
    def __init__(self, gcs_destination: _Optional[_Union[IamPolicyAnalysisOutputConfig.GcsDestination, _Mapping]] = ..., bigquery_destination: _Optional[_Union[IamPolicyAnalysisOutputConfig.BigQueryDestination, _Mapping]] = ...) -> None: ...

class AnalyzeIamPolicyLongrunningRequest(_message.Message):
    __slots__ = ("analysis_query", "saved_analysis_query", "output_config")
    ANALYSIS_QUERY_FIELD_NUMBER: _ClassVar[int]
    SAVED_ANALYSIS_QUERY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    analysis_query: IamPolicyAnalysisQuery
    saved_analysis_query: str
    output_config: IamPolicyAnalysisOutputConfig
    def __init__(self, analysis_query: _Optional[_Union[IamPolicyAnalysisQuery, _Mapping]] = ..., saved_analysis_query: _Optional[str] = ..., output_config: _Optional[_Union[IamPolicyAnalysisOutputConfig, _Mapping]] = ...) -> None: ...

class AnalyzeIamPolicyLongrunningResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SavedQuery(_message.Message):
    __slots__ = ("name", "description", "create_time", "creator", "last_update_time", "last_updater", "labels", "content")
    class QueryContent(_message.Message):
        __slots__ = ("iam_policy_analysis_query",)
        IAM_POLICY_ANALYSIS_QUERY_FIELD_NUMBER: _ClassVar[int]
        iam_policy_analysis_query: IamPolicyAnalysisQuery
        def __init__(self, iam_policy_analysis_query: _Optional[_Union[IamPolicyAnalysisQuery, _Mapping]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATER_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    creator: str
    last_update_time: _timestamp_pb2.Timestamp
    last_updater: str
    labels: _containers.ScalarMap[str, str]
    content: SavedQuery.QueryContent
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., creator: _Optional[str] = ..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updater: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., content: _Optional[_Union[SavedQuery.QueryContent, _Mapping]] = ...) -> None: ...

class CreateSavedQueryRequest(_message.Message):
    __slots__ = ("parent", "saved_query", "saved_query_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SAVED_QUERY_FIELD_NUMBER: _ClassVar[int]
    SAVED_QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    saved_query: SavedQuery
    saved_query_id: str
    def __init__(self, parent: _Optional[str] = ..., saved_query: _Optional[_Union[SavedQuery, _Mapping]] = ..., saved_query_id: _Optional[str] = ...) -> None: ...

class GetSavedQueryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSavedQueriesRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSavedQueriesResponse(_message.Message):
    __slots__ = ("saved_queries", "next_page_token")
    SAVED_QUERIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    saved_queries: _containers.RepeatedCompositeFieldContainer[SavedQuery]
    next_page_token: str
    def __init__(self, saved_queries: _Optional[_Iterable[_Union[SavedQuery, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateSavedQueryRequest(_message.Message):
    __slots__ = ("saved_query", "update_mask")
    SAVED_QUERY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    saved_query: SavedQuery
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, saved_query: _Optional[_Union[SavedQuery, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteSavedQueryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AnalyzeMoveRequest(_message.Message):
    __slots__ = ("resource", "destination_parent", "view")
    class AnalysisView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANALYSIS_VIEW_UNSPECIFIED: _ClassVar[AnalyzeMoveRequest.AnalysisView]
        FULL: _ClassVar[AnalyzeMoveRequest.AnalysisView]
        BASIC: _ClassVar[AnalyzeMoveRequest.AnalysisView]
    ANALYSIS_VIEW_UNSPECIFIED: AnalyzeMoveRequest.AnalysisView
    FULL: AnalyzeMoveRequest.AnalysisView
    BASIC: AnalyzeMoveRequest.AnalysisView
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    resource: str
    destination_parent: str
    view: AnalyzeMoveRequest.AnalysisView
    def __init__(self, resource: _Optional[str] = ..., destination_parent: _Optional[str] = ..., view: _Optional[_Union[AnalyzeMoveRequest.AnalysisView, str]] = ...) -> None: ...

class AnalyzeMoveResponse(_message.Message):
    __slots__ = ("move_analysis",)
    MOVE_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    move_analysis: _containers.RepeatedCompositeFieldContainer[MoveAnalysis]
    def __init__(self, move_analysis: _Optional[_Iterable[_Union[MoveAnalysis, _Mapping]]] = ...) -> None: ...

class MoveAnalysis(_message.Message):
    __slots__ = ("display_name", "analysis", "error")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    analysis: MoveAnalysisResult
    error: _status_pb2.Status
    def __init__(self, display_name: _Optional[str] = ..., analysis: _Optional[_Union[MoveAnalysisResult, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class MoveAnalysisResult(_message.Message):
    __slots__ = ("blockers", "warnings")
    BLOCKERS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    blockers: _containers.RepeatedCompositeFieldContainer[MoveImpact]
    warnings: _containers.RepeatedCompositeFieldContainer[MoveImpact]
    def __init__(self, blockers: _Optional[_Iterable[_Union[MoveImpact, _Mapping]]] = ..., warnings: _Optional[_Iterable[_Union[MoveImpact, _Mapping]]] = ...) -> None: ...

class MoveImpact(_message.Message):
    __slots__ = ("detail",)
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    detail: str
    def __init__(self, detail: _Optional[str] = ...) -> None: ...

class QueryAssetsOutputConfig(_message.Message):
    __slots__ = ("bigquery_destination",)
    class BigQueryDestination(_message.Message):
        __slots__ = ("dataset", "table", "write_disposition")
        DATASET_FIELD_NUMBER: _ClassVar[int]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        table: str
        write_disposition: str
        def __init__(self, dataset: _Optional[str] = ..., table: _Optional[str] = ..., write_disposition: _Optional[str] = ...) -> None: ...
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    bigquery_destination: QueryAssetsOutputConfig.BigQueryDestination
    def __init__(self, bigquery_destination: _Optional[_Union[QueryAssetsOutputConfig.BigQueryDestination, _Mapping]] = ...) -> None: ...

class QueryAssetsRequest(_message.Message):
    __slots__ = ("parent", "statement", "job_reference", "page_size", "page_token", "timeout", "read_time_window", "read_time", "output_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    JOB_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    statement: str
    job_reference: str
    page_size: int
    page_token: str
    timeout: _duration_pb2.Duration
    read_time_window: _assets_pb2.TimeWindow
    read_time: _timestamp_pb2.Timestamp
    output_config: QueryAssetsOutputConfig
    def __init__(self, parent: _Optional[str] = ..., statement: _Optional[str] = ..., job_reference: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., read_time_window: _Optional[_Union[_assets_pb2.TimeWindow, _Mapping]] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., output_config: _Optional[_Union[QueryAssetsOutputConfig, _Mapping]] = ...) -> None: ...

class QueryAssetsResponse(_message.Message):
    __slots__ = ("job_reference", "done", "error", "query_result", "output_config")
    JOB_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    job_reference: str
    done: bool
    error: _status_pb2.Status
    query_result: QueryResult
    output_config: QueryAssetsOutputConfig
    def __init__(self, job_reference: _Optional[str] = ..., done: bool = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., query_result: _Optional[_Union[QueryResult, _Mapping]] = ..., output_config: _Optional[_Union[QueryAssetsOutputConfig, _Mapping]] = ...) -> None: ...

class QueryResult(_message.Message):
    __slots__ = ("rows", "schema", "next_page_token", "total_rows")
    ROWS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    schema: TableSchema
    next_page_token: str
    total_rows: int
    def __init__(self, rows: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ..., schema: _Optional[_Union[TableSchema, _Mapping]] = ..., next_page_token: _Optional[str] = ..., total_rows: _Optional[int] = ...) -> None: ...

class TableSchema(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[TableFieldSchema]
    def __init__(self, fields: _Optional[_Iterable[_Union[TableFieldSchema, _Mapping]]] = ...) -> None: ...

class TableFieldSchema(_message.Message):
    __slots__ = ("field", "type", "mode", "fields")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    field: str
    type: str
    mode: str
    fields: _containers.RepeatedCompositeFieldContainer[TableFieldSchema]
    def __init__(self, field: _Optional[str] = ..., type: _Optional[str] = ..., mode: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[TableFieldSchema, _Mapping]]] = ...) -> None: ...

class BatchGetEffectiveIamPoliciesRequest(_message.Message):
    __slots__ = ("scope", "names")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    scope: str
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, scope: _Optional[str] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchGetEffectiveIamPoliciesResponse(_message.Message):
    __slots__ = ("policy_results",)
    class EffectiveIamPolicy(_message.Message):
        __slots__ = ("full_resource_name", "policies")
        class PolicyInfo(_message.Message):
            __slots__ = ("attached_resource", "policy")
            ATTACHED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
            POLICY_FIELD_NUMBER: _ClassVar[int]
            attached_resource: str
            policy: _policy_pb2.Policy
            def __init__(self, attached_resource: _Optional[str] = ..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...
        FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        POLICIES_FIELD_NUMBER: _ClassVar[int]
        full_resource_name: str
        policies: _containers.RepeatedCompositeFieldContainer[BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo]
        def __init__(self, full_resource_name: _Optional[str] = ..., policies: _Optional[_Iterable[_Union[BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo, _Mapping]]] = ...) -> None: ...
    POLICY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    policy_results: _containers.RepeatedCompositeFieldContainer[BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy]
    def __init__(self, policy_results: _Optional[_Iterable[_Union[BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy, _Mapping]]] = ...) -> None: ...

class AnalyzerOrgPolicy(_message.Message):
    __slots__ = ("attached_resource", "applied_resource", "rules", "inherit_from_parent", "reset")
    class Rule(_message.Message):
        __slots__ = ("values", "allow_all", "deny_all", "enforce", "condition", "condition_evaluation")
        class StringValues(_message.Message):
            __slots__ = ("allowed_values", "denied_values")
            ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
            DENIED_VALUES_FIELD_NUMBER: _ClassVar[int]
            allowed_values: _containers.RepeatedScalarFieldContainer[str]
            denied_values: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, allowed_values: _Optional[_Iterable[str]] = ..., denied_values: _Optional[_Iterable[str]] = ...) -> None: ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_ALL_FIELD_NUMBER: _ClassVar[int]
        DENY_ALL_FIELD_NUMBER: _ClassVar[int]
        ENFORCE_FIELD_NUMBER: _ClassVar[int]
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        CONDITION_EVALUATION_FIELD_NUMBER: _ClassVar[int]
        values: AnalyzerOrgPolicy.Rule.StringValues
        allow_all: bool
        deny_all: bool
        enforce: bool
        condition: _expr_pb2.Expr
        condition_evaluation: _assets_pb2.ConditionEvaluation
        def __init__(self, values: _Optional[_Union[AnalyzerOrgPolicy.Rule.StringValues, _Mapping]] = ..., allow_all: bool = ..., deny_all: bool = ..., enforce: bool = ..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]] = ..., condition_evaluation: _Optional[_Union[_assets_pb2.ConditionEvaluation, _Mapping]] = ...) -> None: ...
    ATTACHED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    APPLIED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    INHERIT_FROM_PARENT_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    attached_resource: str
    applied_resource: str
    rules: _containers.RepeatedCompositeFieldContainer[AnalyzerOrgPolicy.Rule]
    inherit_from_parent: bool
    reset: bool
    def __init__(self, attached_resource: _Optional[str] = ..., applied_resource: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[AnalyzerOrgPolicy.Rule, _Mapping]]] = ..., inherit_from_parent: bool = ..., reset: bool = ...) -> None: ...

class AnalyzerOrgPolicyConstraint(_message.Message):
    __slots__ = ("google_defined_constraint", "custom_constraint")
    class Constraint(_message.Message):
        __slots__ = ("name", "display_name", "description", "constraint_default", "list_constraint", "boolean_constraint")
        class ConstraintDefault(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONSTRAINT_DEFAULT_UNSPECIFIED: _ClassVar[AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault]
            ALLOW: _ClassVar[AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault]
            DENY: _ClassVar[AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault]
        CONSTRAINT_DEFAULT_UNSPECIFIED: AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault
        ALLOW: AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault
        DENY: AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault
        class ListConstraint(_message.Message):
            __slots__ = ("supports_in", "supports_under")
            SUPPORTS_IN_FIELD_NUMBER: _ClassVar[int]
            SUPPORTS_UNDER_FIELD_NUMBER: _ClassVar[int]
            supports_in: bool
            supports_under: bool
            def __init__(self, supports_in: bool = ..., supports_under: bool = ...) -> None: ...
        class BooleanConstraint(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CONSTRAINT_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        LIST_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
        BOOLEAN_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
        name: str
        display_name: str
        description: str
        constraint_default: AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault
        list_constraint: AnalyzerOrgPolicyConstraint.Constraint.ListConstraint
        boolean_constraint: AnalyzerOrgPolicyConstraint.Constraint.BooleanConstraint
        def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., constraint_default: _Optional[_Union[AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault, str]] = ..., list_constraint: _Optional[_Union[AnalyzerOrgPolicyConstraint.Constraint.ListConstraint, _Mapping]] = ..., boolean_constraint: _Optional[_Union[AnalyzerOrgPolicyConstraint.Constraint.BooleanConstraint, _Mapping]] = ...) -> None: ...
    class CustomConstraint(_message.Message):
        __slots__ = ("name", "resource_types", "method_types", "condition", "action_type", "display_name", "description")
        class MethodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD_TYPE_UNSPECIFIED: _ClassVar[AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType]
            CREATE: _ClassVar[AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType]
            UPDATE: _ClassVar[AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType]
            DELETE: _ClassVar[AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType]
        METHOD_TYPE_UNSPECIFIED: AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType
        CREATE: AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType
        UPDATE: AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType
        DELETE: AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType
        class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACTION_TYPE_UNSPECIFIED: _ClassVar[AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType]
            ALLOW: _ClassVar[AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType]
            DENY: _ClassVar[AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType]
        ACTION_TYPE_UNSPECIFIED: AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType
        ALLOW: AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType
        DENY: AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType
        NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
        METHOD_TYPES_FIELD_NUMBER: _ClassVar[int]
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        resource_types: _containers.RepeatedScalarFieldContainer[str]
        method_types: _containers.RepeatedScalarFieldContainer[AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType]
        condition: str
        action_type: AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType
        display_name: str
        description: str
        def __init__(self, name: _Optional[str] = ..., resource_types: _Optional[_Iterable[str]] = ..., method_types: _Optional[_Iterable[_Union[AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType, str]]] = ..., condition: _Optional[str] = ..., action_type: _Optional[_Union[AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType, str]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    GOOGLE_DEFINED_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    google_defined_constraint: AnalyzerOrgPolicyConstraint.Constraint
    custom_constraint: AnalyzerOrgPolicyConstraint.CustomConstraint
    def __init__(self, google_defined_constraint: _Optional[_Union[AnalyzerOrgPolicyConstraint.Constraint, _Mapping]] = ..., custom_constraint: _Optional[_Union[AnalyzerOrgPolicyConstraint.CustomConstraint, _Mapping]] = ...) -> None: ...

class AnalyzeOrgPoliciesRequest(_message.Message):
    __slots__ = ("scope", "constraint", "filter", "page_size", "page_token")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    scope: str
    constraint: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, scope: _Optional[str] = ..., constraint: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class AnalyzeOrgPoliciesResponse(_message.Message):
    __slots__ = ("org_policy_results", "constraint", "next_page_token")
    class OrgPolicyResult(_message.Message):
        __slots__ = ("consolidated_policy", "policy_bundle", "project", "folders", "organization")
        CONSOLIDATED_POLICY_FIELD_NUMBER: _ClassVar[int]
        POLICY_BUNDLE_FIELD_NUMBER: _ClassVar[int]
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        FOLDERS_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
        consolidated_policy: AnalyzerOrgPolicy
        policy_bundle: _containers.RepeatedCompositeFieldContainer[AnalyzerOrgPolicy]
        project: str
        folders: _containers.RepeatedScalarFieldContainer[str]
        organization: str
        def __init__(self, consolidated_policy: _Optional[_Union[AnalyzerOrgPolicy, _Mapping]] = ..., policy_bundle: _Optional[_Iterable[_Union[AnalyzerOrgPolicy, _Mapping]]] = ..., project: _Optional[str] = ..., folders: _Optional[_Iterable[str]] = ..., organization: _Optional[str] = ...) -> None: ...
    ORG_POLICY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    org_policy_results: _containers.RepeatedCompositeFieldContainer[AnalyzeOrgPoliciesResponse.OrgPolicyResult]
    constraint: AnalyzerOrgPolicyConstraint
    next_page_token: str
    def __init__(self, org_policy_results: _Optional[_Iterable[_Union[AnalyzeOrgPoliciesResponse.OrgPolicyResult, _Mapping]]] = ..., constraint: _Optional[_Union[AnalyzerOrgPolicyConstraint, _Mapping]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AnalyzeOrgPolicyGovernedContainersRequest(_message.Message):
    __slots__ = ("scope", "constraint", "filter", "page_size", "page_token")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    scope: str
    constraint: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, scope: _Optional[str] = ..., constraint: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class AnalyzeOrgPolicyGovernedContainersResponse(_message.Message):
    __slots__ = ("governed_containers", "constraint", "next_page_token")
    class GovernedContainer(_message.Message):
        __slots__ = ("full_resource_name", "parent", "consolidated_policy", "policy_bundle", "project", "folders", "organization", "effective_tags")
        FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        PARENT_FIELD_NUMBER: _ClassVar[int]
        CONSOLIDATED_POLICY_FIELD_NUMBER: _ClassVar[int]
        POLICY_BUNDLE_FIELD_NUMBER: _ClassVar[int]
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        FOLDERS_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_TAGS_FIELD_NUMBER: _ClassVar[int]
        full_resource_name: str
        parent: str
        consolidated_policy: AnalyzerOrgPolicy
        policy_bundle: _containers.RepeatedCompositeFieldContainer[AnalyzerOrgPolicy]
        project: str
        folders: _containers.RepeatedScalarFieldContainer[str]
        organization: str
        effective_tags: _containers.RepeatedCompositeFieldContainer[_assets_pb2.EffectiveTagDetails]
        def __init__(self, full_resource_name: _Optional[str] = ..., parent: _Optional[str] = ..., consolidated_policy: _Optional[_Union[AnalyzerOrgPolicy, _Mapping]] = ..., policy_bundle: _Optional[_Iterable[_Union[AnalyzerOrgPolicy, _Mapping]]] = ..., project: _Optional[str] = ..., folders: _Optional[_Iterable[str]] = ..., organization: _Optional[str] = ..., effective_tags: _Optional[_Iterable[_Union[_assets_pb2.EffectiveTagDetails, _Mapping]]] = ...) -> None: ...
    GOVERNED_CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    governed_containers: _containers.RepeatedCompositeFieldContainer[AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer]
    constraint: AnalyzerOrgPolicyConstraint
    next_page_token: str
    def __init__(self, governed_containers: _Optional[_Iterable[_Union[AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer, _Mapping]]] = ..., constraint: _Optional[_Union[AnalyzerOrgPolicyConstraint, _Mapping]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AnalyzeOrgPolicyGovernedAssetsRequest(_message.Message):
    __slots__ = ("scope", "constraint", "filter", "page_size", "page_token")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    scope: str
    constraint: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, scope: _Optional[str] = ..., constraint: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class AnalyzeOrgPolicyGovernedAssetsResponse(_message.Message):
    __slots__ = ("governed_assets", "constraint", "next_page_token")
    class GovernedResource(_message.Message):
        __slots__ = ("full_resource_name", "parent", "project", "folders", "organization", "asset_type", "effective_tags")
        FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        PARENT_FIELD_NUMBER: _ClassVar[int]
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        FOLDERS_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
        ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_TAGS_FIELD_NUMBER: _ClassVar[int]
        full_resource_name: str
        parent: str
        project: str
        folders: _containers.RepeatedScalarFieldContainer[str]
        organization: str
        asset_type: str
        effective_tags: _containers.RepeatedCompositeFieldContainer[_assets_pb2.EffectiveTagDetails]
        def __init__(self, full_resource_name: _Optional[str] = ..., parent: _Optional[str] = ..., project: _Optional[str] = ..., folders: _Optional[_Iterable[str]] = ..., organization: _Optional[str] = ..., asset_type: _Optional[str] = ..., effective_tags: _Optional[_Iterable[_Union[_assets_pb2.EffectiveTagDetails, _Mapping]]] = ...) -> None: ...
    class GovernedIamPolicy(_message.Message):
        __slots__ = ("attached_resource", "policy", "project", "folders", "organization", "asset_type")
        ATTACHED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        POLICY_FIELD_NUMBER: _ClassVar[int]
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        FOLDERS_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
        ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
        attached_resource: str
        policy: _policy_pb2.Policy
        project: str
        folders: _containers.RepeatedScalarFieldContainer[str]
        organization: str
        asset_type: str
        def __init__(self, attached_resource: _Optional[str] = ..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ..., project: _Optional[str] = ..., folders: _Optional[_Iterable[str]] = ..., organization: _Optional[str] = ..., asset_type: _Optional[str] = ...) -> None: ...
    class GovernedAsset(_message.Message):
        __slots__ = ("governed_resource", "governed_iam_policy", "consolidated_policy", "policy_bundle")
        GOVERNED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        GOVERNED_IAM_POLICY_FIELD_NUMBER: _ClassVar[int]
        CONSOLIDATED_POLICY_FIELD_NUMBER: _ClassVar[int]
        POLICY_BUNDLE_FIELD_NUMBER: _ClassVar[int]
        governed_resource: AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource
        governed_iam_policy: AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy
        consolidated_policy: AnalyzerOrgPolicy
        policy_bundle: _containers.RepeatedCompositeFieldContainer[AnalyzerOrgPolicy]
        def __init__(self, governed_resource: _Optional[_Union[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource, _Mapping]] = ..., governed_iam_policy: _Optional[_Union[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy, _Mapping]] = ..., consolidated_policy: _Optional[_Union[AnalyzerOrgPolicy, _Mapping]] = ..., policy_bundle: _Optional[_Iterable[_Union[AnalyzerOrgPolicy, _Mapping]]] = ...) -> None: ...
    GOVERNED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    governed_assets: _containers.RepeatedCompositeFieldContainer[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset]
    constraint: AnalyzerOrgPolicyConstraint
    next_page_token: str
    def __init__(self, governed_assets: _Optional[_Iterable[_Union[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset, _Mapping]]] = ..., constraint: _Optional[_Union[AnalyzerOrgPolicyConstraint, _Mapping]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
