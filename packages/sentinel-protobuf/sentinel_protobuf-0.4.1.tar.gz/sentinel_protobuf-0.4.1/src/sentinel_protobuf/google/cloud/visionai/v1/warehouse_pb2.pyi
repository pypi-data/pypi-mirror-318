from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.visionai.v1 import common_pb2 as _common_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FacetBucketType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FACET_BUCKET_TYPE_UNSPECIFIED: _ClassVar[FacetBucketType]
    FACET_BUCKET_TYPE_VALUE: _ClassVar[FacetBucketType]
    FACET_BUCKET_TYPE_DATETIME: _ClassVar[FacetBucketType]
    FACET_BUCKET_TYPE_FIXED_RANGE: _ClassVar[FacetBucketType]
    FACET_BUCKET_TYPE_CUSTOM_RANGE: _ClassVar[FacetBucketType]
FACET_BUCKET_TYPE_UNSPECIFIED: FacetBucketType
FACET_BUCKET_TYPE_VALUE: FacetBucketType
FACET_BUCKET_TYPE_DATETIME: FacetBucketType
FACET_BUCKET_TYPE_FIXED_RANGE: FacetBucketType
FACET_BUCKET_TYPE_CUSTOM_RANGE: FacetBucketType

class CreateAssetRequest(_message.Message):
    __slots__ = ("parent", "asset", "asset_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    asset: Asset
    asset_id: str
    def __init__(self, parent: _Optional[str] = ..., asset: _Optional[_Union[Asset, _Mapping]] = ..., asset_id: _Optional[str] = ...) -> None: ...

class GetAssetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAssetsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListAssetsResponse(_message.Message):
    __slots__ = ("assets", "next_page_token")
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[Asset]
    next_page_token: str
    def __init__(self, assets: _Optional[_Iterable[_Union[Asset, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateAssetRequest(_message.Message):
    __slots__ = ("asset", "update_mask")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    asset: Asset
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, asset: _Optional[_Union[Asset, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAssetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AssetSource(_message.Message):
    __slots__ = ("asset_gcs_source", "asset_content_data")
    class AssetGcsSource(_message.Message):
        __slots__ = ("gcs_uri",)
        GCS_URI_FIELD_NUMBER: _ClassVar[int]
        gcs_uri: str
        def __init__(self, gcs_uri: _Optional[str] = ...) -> None: ...
    class AssetContentData(_message.Message):
        __slots__ = ("asset_content_data",)
        ASSET_CONTENT_DATA_FIELD_NUMBER: _ClassVar[int]
        asset_content_data: bytes
        def __init__(self, asset_content_data: _Optional[bytes] = ...) -> None: ...
    ASSET_GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ASSET_CONTENT_DATA_FIELD_NUMBER: _ClassVar[int]
    asset_gcs_source: AssetSource.AssetGcsSource
    asset_content_data: AssetSource.AssetContentData
    def __init__(self, asset_gcs_source: _Optional[_Union[AssetSource.AssetGcsSource, _Mapping]] = ..., asset_content_data: _Optional[_Union[AssetSource.AssetContentData, _Mapping]] = ...) -> None: ...

class UploadAssetRequest(_message.Message):
    __slots__ = ("name", "asset_source")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    asset_source: AssetSource
    def __init__(self, name: _Optional[str] = ..., asset_source: _Optional[_Union[AssetSource, _Mapping]] = ...) -> None: ...

class UploadAssetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadAssetMetadata(_message.Message):
    __slots__ = ("start_time", "update_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GenerateRetrievalUrlRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GenerateRetrievalUrlResponse(_message.Message):
    __slots__ = ("signed_uri",)
    SIGNED_URI_FIELD_NUMBER: _ClassVar[int]
    signed_uri: str
    def __init__(self, signed_uri: _Optional[str] = ...) -> None: ...

class Asset(_message.Message):
    __slots__ = ("name", "ttl", "asset_gcs_source")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    ASSET_GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    ttl: _duration_pb2.Duration
    asset_gcs_source: AssetSource.AssetGcsSource
    def __init__(self, name: _Optional[str] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., asset_gcs_source: _Optional[_Union[AssetSource.AssetGcsSource, _Mapping]] = ...) -> None: ...

class AnalyzeAssetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AnalyzeAssetMetadata(_message.Message):
    __slots__ = ("analysis_status", "start_time", "update_time")
    class AnalysisStatus(_message.Message):
        __slots__ = ("state", "status_message", "search_capability")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[AnalyzeAssetMetadata.AnalysisStatus.State]
            IN_PROGRESS: _ClassVar[AnalyzeAssetMetadata.AnalysisStatus.State]
            SUCCEEDED: _ClassVar[AnalyzeAssetMetadata.AnalysisStatus.State]
            FAILED: _ClassVar[AnalyzeAssetMetadata.AnalysisStatus.State]
        STATE_UNSPECIFIED: AnalyzeAssetMetadata.AnalysisStatus.State
        IN_PROGRESS: AnalyzeAssetMetadata.AnalysisStatus.State
        SUCCEEDED: AnalyzeAssetMetadata.AnalysisStatus.State
        FAILED: AnalyzeAssetMetadata.AnalysisStatus.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        SEARCH_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
        state: AnalyzeAssetMetadata.AnalysisStatus.State
        status_message: str
        search_capability: SearchCapability
        def __init__(self, state: _Optional[_Union[AnalyzeAssetMetadata.AnalysisStatus.State, str]] = ..., status_message: _Optional[str] = ..., search_capability: _Optional[_Union[SearchCapability, _Mapping]] = ...) -> None: ...
    ANALYSIS_STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    analysis_status: _containers.RepeatedCompositeFieldContainer[AnalyzeAssetMetadata.AnalysisStatus]
    start_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, analysis_status: _Optional[_Iterable[_Union[AnalyzeAssetMetadata.AnalysisStatus, _Mapping]]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AnalyzeAssetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IndexingStatus(_message.Message):
    __slots__ = ("state", "status_message")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[IndexingStatus.State]
        IN_PROGRESS: _ClassVar[IndexingStatus.State]
        SUCCEEDED: _ClassVar[IndexingStatus.State]
        FAILED: _ClassVar[IndexingStatus.State]
    STATE_UNSPECIFIED: IndexingStatus.State
    IN_PROGRESS: IndexingStatus.State
    SUCCEEDED: IndexingStatus.State
    FAILED: IndexingStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    state: IndexingStatus.State
    status_message: str
    def __init__(self, state: _Optional[_Union[IndexingStatus.State, str]] = ..., status_message: _Optional[str] = ...) -> None: ...

class IndexAssetRequest(_message.Message):
    __slots__ = ("name", "index")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    name: str
    index: str
    def __init__(self, name: _Optional[str] = ..., index: _Optional[str] = ...) -> None: ...

class IndexAssetMetadata(_message.Message):
    __slots__ = ("status", "start_time", "update_time")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    status: IndexingStatus
    start_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, status: _Optional[_Union[IndexingStatus, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class IndexAssetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveIndexAssetRequest(_message.Message):
    __slots__ = ("name", "index")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    name: str
    index: str
    def __init__(self, name: _Optional[str] = ..., index: _Optional[str] = ...) -> None: ...

class RemoveIndexAssetMetadata(_message.Message):
    __slots__ = ("indexing_status", "start_time", "update_time")
    INDEXING_STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    indexing_status: IndexingStatus
    start_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, indexing_status: _Optional[_Union[IndexingStatus, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RemoveIndexAssetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IndexedAsset(_message.Message):
    __slots__ = ("index", "asset", "create_time", "update_time")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    index: str
    asset: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, index: _Optional[str] = ..., asset: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ViewIndexedAssetsRequest(_message.Message):
    __slots__ = ("index", "page_size", "page_token", "filter")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    index: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, index: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ViewIndexedAssetsResponse(_message.Message):
    __slots__ = ("indexed_assets", "next_page_token")
    INDEXED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    indexed_assets: _containers.RepeatedCompositeFieldContainer[IndexedAsset]
    next_page_token: str
    def __init__(self, indexed_assets: _Optional[_Iterable[_Union[IndexedAsset, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateCorpusRequest(_message.Message):
    __slots__ = ("parent", "corpus")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    corpus: Corpus
    def __init__(self, parent: _Optional[str] = ..., corpus: _Optional[_Union[Corpus, _Mapping]] = ...) -> None: ...

class CreateCorpusMetadata(_message.Message):
    __slots__ = ("create_time", "update_time")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SearchCapability(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[SearchCapability.Type]
        EMBEDDING_SEARCH: _ClassVar[SearchCapability.Type]
    TYPE_UNSPECIFIED: SearchCapability.Type
    EMBEDDING_SEARCH: SearchCapability.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: SearchCapability.Type
    def __init__(self, type: _Optional[_Union[SearchCapability.Type, str]] = ...) -> None: ...

class SearchCapabilitySetting(_message.Message):
    __slots__ = ("search_capabilities",)
    SEARCH_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    search_capabilities: _containers.RepeatedCompositeFieldContainer[SearchCapability]
    def __init__(self, search_capabilities: _Optional[_Iterable[_Union[SearchCapability, _Mapping]]] = ...) -> None: ...

class CreateCollectionMetadata(_message.Message):
    __slots__ = ("operation_metadata",)
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: _common_pb2.OperationMetadata
    def __init__(self, operation_metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class CreateCollectionRequest(_message.Message):
    __slots__ = ("parent", "collection", "collection_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    collection: Collection
    collection_id: str
    def __init__(self, parent: _Optional[str] = ..., collection: _Optional[_Union[Collection, _Mapping]] = ..., collection_id: _Optional[str] = ...) -> None: ...

class DeleteCollectionMetadata(_message.Message):
    __slots__ = ("operation_metadata",)
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: _common_pb2.OperationMetadata
    def __init__(self, operation_metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DeleteCollectionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetCollectionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateCollectionRequest(_message.Message):
    __slots__ = ("collection", "update_mask")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    collection: Collection
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, collection: _Optional[_Union[Collection, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListCollectionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCollectionsResponse(_message.Message):
    __slots__ = ("collections", "next_page_token")
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[Collection]
    next_page_token: str
    def __init__(self, collections: _Optional[_Iterable[_Union[Collection, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AddCollectionItemRequest(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: CollectionItem
    def __init__(self, item: _Optional[_Union[CollectionItem, _Mapping]] = ...) -> None: ...

class AddCollectionItemResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: CollectionItem
    def __init__(self, item: _Optional[_Union[CollectionItem, _Mapping]] = ...) -> None: ...

class RemoveCollectionItemRequest(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: CollectionItem
    def __init__(self, item: _Optional[_Union[CollectionItem, _Mapping]] = ...) -> None: ...

class RemoveCollectionItemResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: CollectionItem
    def __init__(self, item: _Optional[_Union[CollectionItem, _Mapping]] = ...) -> None: ...

class ViewCollectionItemsRequest(_message.Message):
    __slots__ = ("collection", "page_size", "page_token")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    collection: str
    page_size: int
    page_token: str
    def __init__(self, collection: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ViewCollectionItemsResponse(_message.Message):
    __slots__ = ("items", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CollectionItem]
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[CollectionItem, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class Collection(_message.Message):
    __slots__ = ("name", "display_name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CollectionItem(_message.Message):
    __slots__ = ("collection", "type", "item_resource")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[CollectionItem.Type]
        ASSET: _ClassVar[CollectionItem.Type]
    TYPE_UNSPECIFIED: CollectionItem.Type
    ASSET: CollectionItem.Type
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    collection: str
    type: CollectionItem.Type
    item_resource: str
    def __init__(self, collection: _Optional[str] = ..., type: _Optional[_Union[CollectionItem.Type, str]] = ..., item_resource: _Optional[str] = ...) -> None: ...

class CreateIndexRequest(_message.Message):
    __slots__ = ("parent", "index_id", "index")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    parent: str
    index_id: str
    index: Index
    def __init__(self, parent: _Optional[str] = ..., index_id: _Optional[str] = ..., index: _Optional[_Union[Index, _Mapping]] = ...) -> None: ...

class CreateIndexMetadata(_message.Message):
    __slots__ = ("operation_metadata",)
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: _common_pb2.OperationMetadata
    def __init__(self, operation_metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class UpdateIndexRequest(_message.Message):
    __slots__ = ("index", "update_mask")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    index: Index
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, index: _Optional[_Union[Index, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateIndexMetadata(_message.Message):
    __slots__ = ("operation_metadata",)
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: _common_pb2.OperationMetadata
    def __init__(self, operation_metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class GetIndexRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListIndexesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListIndexesResponse(_message.Message):
    __slots__ = ("indexes", "next_page_token")
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    indexes: _containers.RepeatedCompositeFieldContainer[Index]
    next_page_token: str
    def __init__(self, indexes: _Optional[_Iterable[_Union[Index, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteIndexRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteIndexMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Index(_message.Message):
    __slots__ = ("entire_corpus", "name", "display_name", "description", "state", "create_time", "update_time", "deployed_indexes", "satisfies_pzs", "satisfies_pzi")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Index.State]
        CREATING: _ClassVar[Index.State]
        CREATED: _ClassVar[Index.State]
        UPDATING: _ClassVar[Index.State]
    STATE_UNSPECIFIED: Index.State
    CREATING: Index.State
    CREATED: Index.State
    UPDATING: Index.State
    ENTIRE_CORPUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEXES_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    entire_corpus: bool
    name: str
    display_name: str
    description: str
    state: Index.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    deployed_indexes: _containers.RepeatedCompositeFieldContainer[DeployedIndexReference]
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, entire_corpus: bool = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., state: _Optional[_Union[Index.State, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployed_indexes: _Optional[_Iterable[_Union[DeployedIndexReference, _Mapping]]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...

class DeployedIndexReference(_message.Message):
    __slots__ = ("index_endpoint",)
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: str
    def __init__(self, index_endpoint: _Optional[str] = ...) -> None: ...

class Corpus(_message.Message):
    __slots__ = ("name", "display_name", "description", "default_ttl", "type", "search_capability_setting", "satisfies_pzs", "satisfies_pzi")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Corpus.Type]
        STREAM_VIDEO: _ClassVar[Corpus.Type]
        IMAGE: _ClassVar[Corpus.Type]
        VIDEO_ON_DEMAND: _ClassVar[Corpus.Type]
    TYPE_UNSPECIFIED: Corpus.Type
    STREAM_VIDEO: Corpus.Type
    IMAGE: Corpus.Type
    VIDEO_ON_DEMAND: Corpus.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TTL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CAPABILITY_SETTING_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    default_ttl: _duration_pb2.Duration
    type: Corpus.Type
    search_capability_setting: SearchCapabilitySetting
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., default_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., type: _Optional[_Union[Corpus.Type, str]] = ..., search_capability_setting: _Optional[_Union[SearchCapabilitySetting, _Mapping]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...

class GetCorpusRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateCorpusRequest(_message.Message):
    __slots__ = ("corpus", "update_mask")
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    corpus: Corpus
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, corpus: _Optional[_Union[Corpus, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListCorporaRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListCorporaResponse(_message.Message):
    __slots__ = ("corpora", "next_page_token")
    CORPORA_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    corpora: _containers.RepeatedCompositeFieldContainer[Corpus]
    next_page_token: str
    def __init__(self, corpora: _Optional[_Iterable[_Union[Corpus, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteCorpusRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AnalyzeCorpusRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AnalyzeCorpusMetadata(_message.Message):
    __slots__ = ("metadata",)
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _common_pb2.OperationMetadata
    def __init__(self, metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class AnalyzeCorpusResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateDataSchemaRequest(_message.Message):
    __slots__ = ("parent", "data_schema")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_schema: DataSchema
    def __init__(self, parent: _Optional[str] = ..., data_schema: _Optional[_Union[DataSchema, _Mapping]] = ...) -> None: ...

class DataSchema(_message.Message):
    __slots__ = ("name", "key", "schema_details")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    schema_details: DataSchemaDetails
    def __init__(self, name: _Optional[str] = ..., key: _Optional[str] = ..., schema_details: _Optional[_Union[DataSchemaDetails, _Mapping]] = ...) -> None: ...

class DataSchemaDetails(_message.Message):
    __slots__ = ("type", "proto_any_config", "list_config", "customized_struct_config", "granularity", "search_strategy")
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[DataSchemaDetails.DataType]
        INTEGER: _ClassVar[DataSchemaDetails.DataType]
        FLOAT: _ClassVar[DataSchemaDetails.DataType]
        STRING: _ClassVar[DataSchemaDetails.DataType]
        DATETIME: _ClassVar[DataSchemaDetails.DataType]
        GEO_COORDINATE: _ClassVar[DataSchemaDetails.DataType]
        PROTO_ANY: _ClassVar[DataSchemaDetails.DataType]
        BOOLEAN: _ClassVar[DataSchemaDetails.DataType]
        LIST: _ClassVar[DataSchemaDetails.DataType]
        CUSTOMIZED_STRUCT: _ClassVar[DataSchemaDetails.DataType]
    DATA_TYPE_UNSPECIFIED: DataSchemaDetails.DataType
    INTEGER: DataSchemaDetails.DataType
    FLOAT: DataSchemaDetails.DataType
    STRING: DataSchemaDetails.DataType
    DATETIME: DataSchemaDetails.DataType
    GEO_COORDINATE: DataSchemaDetails.DataType
    PROTO_ANY: DataSchemaDetails.DataType
    BOOLEAN: DataSchemaDetails.DataType
    LIST: DataSchemaDetails.DataType
    CUSTOMIZED_STRUCT: DataSchemaDetails.DataType
    class Granularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GRANULARITY_UNSPECIFIED: _ClassVar[DataSchemaDetails.Granularity]
        GRANULARITY_ASSET_LEVEL: _ClassVar[DataSchemaDetails.Granularity]
        GRANULARITY_PARTITION_LEVEL: _ClassVar[DataSchemaDetails.Granularity]
    GRANULARITY_UNSPECIFIED: DataSchemaDetails.Granularity
    GRANULARITY_ASSET_LEVEL: DataSchemaDetails.Granularity
    GRANULARITY_PARTITION_LEVEL: DataSchemaDetails.Granularity
    class ProtoAnyConfig(_message.Message):
        __slots__ = ("type_uri",)
        TYPE_URI_FIELD_NUMBER: _ClassVar[int]
        type_uri: str
        def __init__(self, type_uri: _Optional[str] = ...) -> None: ...
    class ListConfig(_message.Message):
        __slots__ = ("value_schema",)
        VALUE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        value_schema: DataSchemaDetails
        def __init__(self, value_schema: _Optional[_Union[DataSchemaDetails, _Mapping]] = ...) -> None: ...
    class CustomizedStructConfig(_message.Message):
        __slots__ = ("field_schemas",)
        class FieldSchemasEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: DataSchemaDetails
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DataSchemaDetails, _Mapping]] = ...) -> None: ...
        FIELD_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
        field_schemas: _containers.MessageMap[str, DataSchemaDetails]
        def __init__(self, field_schemas: _Optional[_Mapping[str, DataSchemaDetails]] = ...) -> None: ...
    class SearchStrategy(_message.Message):
        __slots__ = ("search_strategy_type", "confidence_score_index_config")
        class SearchStrategyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_SEARCH: _ClassVar[DataSchemaDetails.SearchStrategy.SearchStrategyType]
            EXACT_SEARCH: _ClassVar[DataSchemaDetails.SearchStrategy.SearchStrategyType]
            SMART_SEARCH: _ClassVar[DataSchemaDetails.SearchStrategy.SearchStrategyType]
        NO_SEARCH: DataSchemaDetails.SearchStrategy.SearchStrategyType
        EXACT_SEARCH: DataSchemaDetails.SearchStrategy.SearchStrategyType
        SMART_SEARCH: DataSchemaDetails.SearchStrategy.SearchStrategyType
        class ConfidenceScoreIndexConfig(_message.Message):
            __slots__ = ("field_path", "threshold")
            FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
            THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            field_path: str
            threshold: float
            def __init__(self, field_path: _Optional[str] = ..., threshold: _Optional[float] = ...) -> None: ...
        SEARCH_STRATEGY_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_SCORE_INDEX_CONFIG_FIELD_NUMBER: _ClassVar[int]
        search_strategy_type: DataSchemaDetails.SearchStrategy.SearchStrategyType
        confidence_score_index_config: DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig
        def __init__(self, search_strategy_type: _Optional[_Union[DataSchemaDetails.SearchStrategy.SearchStrategyType, str]] = ..., confidence_score_index_config: _Optional[_Union[DataSchemaDetails.SearchStrategy.ConfidenceScoreIndexConfig, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROTO_ANY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LIST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZED_STRUCT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    type: DataSchemaDetails.DataType
    proto_any_config: DataSchemaDetails.ProtoAnyConfig
    list_config: DataSchemaDetails.ListConfig
    customized_struct_config: DataSchemaDetails.CustomizedStructConfig
    granularity: DataSchemaDetails.Granularity
    search_strategy: DataSchemaDetails.SearchStrategy
    def __init__(self, type: _Optional[_Union[DataSchemaDetails.DataType, str]] = ..., proto_any_config: _Optional[_Union[DataSchemaDetails.ProtoAnyConfig, _Mapping]] = ..., list_config: _Optional[_Union[DataSchemaDetails.ListConfig, _Mapping]] = ..., customized_struct_config: _Optional[_Union[DataSchemaDetails.CustomizedStructConfig, _Mapping]] = ..., granularity: _Optional[_Union[DataSchemaDetails.Granularity, str]] = ..., search_strategy: _Optional[_Union[DataSchemaDetails.SearchStrategy, _Mapping]] = ...) -> None: ...

class UpdateDataSchemaRequest(_message.Message):
    __slots__ = ("data_schema", "update_mask")
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_schema: DataSchema
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, data_schema: _Optional[_Union[DataSchema, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDataSchemaRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteDataSchemaRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDataSchemasRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDataSchemasResponse(_message.Message):
    __slots__ = ("data_schemas", "next_page_token")
    DATA_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_schemas: _containers.RepeatedCompositeFieldContainer[DataSchema]
    next_page_token: str
    def __init__(self, data_schemas: _Optional[_Iterable[_Union[DataSchema, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateAnnotationRequest(_message.Message):
    __slots__ = ("parent", "annotation", "annotation_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    annotation: Annotation
    annotation_id: str
    def __init__(self, parent: _Optional[str] = ..., annotation: _Optional[_Union[Annotation, _Mapping]] = ..., annotation_id: _Optional[str] = ...) -> None: ...

class Annotation(_message.Message):
    __slots__ = ("name", "user_specified_annotation")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_SPECIFIED_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_specified_annotation: UserSpecifiedAnnotation
    def __init__(self, name: _Optional[str] = ..., user_specified_annotation: _Optional[_Union[UserSpecifiedAnnotation, _Mapping]] = ...) -> None: ...

class UserSpecifiedAnnotation(_message.Message):
    __slots__ = ("key", "value", "partition")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: AnnotationValue
    partition: Partition
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AnnotationValue, _Mapping]] = ..., partition: _Optional[_Union[Partition, _Mapping]] = ...) -> None: ...

class GeoCoordinate(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class AnnotationValue(_message.Message):
    __slots__ = ("int_value", "float_value", "str_value", "datetime_value", "geo_coordinate", "proto_any_value", "bool_value", "customized_struct_data_value", "list_value", "customized_struct_value")
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STR_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    GEO_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    PROTO_ANY_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZED_STRUCT_DATA_VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZED_STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
    int_value: int
    float_value: float
    str_value: str
    datetime_value: str
    geo_coordinate: GeoCoordinate
    proto_any_value: _any_pb2.Any
    bool_value: bool
    customized_struct_data_value: _struct_pb2.Struct
    list_value: AnnotationList
    customized_struct_value: AnnotationCustomizedStruct
    def __init__(self, int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., str_value: _Optional[str] = ..., datetime_value: _Optional[str] = ..., geo_coordinate: _Optional[_Union[GeoCoordinate, _Mapping]] = ..., proto_any_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., bool_value: bool = ..., customized_struct_data_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., list_value: _Optional[_Union[AnnotationList, _Mapping]] = ..., customized_struct_value: _Optional[_Union[AnnotationCustomizedStruct, _Mapping]] = ...) -> None: ...

class AnnotationList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[AnnotationValue]
    def __init__(self, values: _Optional[_Iterable[_Union[AnnotationValue, _Mapping]]] = ...) -> None: ...

class AnnotationCustomizedStruct(_message.Message):
    __slots__ = ("elements",)
    class ElementsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AnnotationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AnnotationValue, _Mapping]] = ...) -> None: ...
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.MessageMap[str, AnnotationValue]
    def __init__(self, elements: _Optional[_Mapping[str, AnnotationValue]] = ...) -> None: ...

class ListAnnotationsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListAnnotationsResponse(_message.Message):
    __slots__ = ("annotations", "next_page_token")
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[Annotation]
    next_page_token: str
    def __init__(self, annotations: _Optional[_Iterable[_Union[Annotation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetAnnotationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateAnnotationRequest(_message.Message):
    __slots__ = ("annotation", "update_mask")
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    annotation: Annotation
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, annotation: _Optional[_Union[Annotation, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAnnotationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ImportAssetsRequest(_message.Message):
    __slots__ = ("assets_gcs_uri", "parent")
    ASSETS_GCS_URI_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    assets_gcs_uri: str
    parent: str
    def __init__(self, assets_gcs_uri: _Optional[str] = ..., parent: _Optional[str] = ...) -> None: ...

class ImportAssetsMetadata(_message.Message):
    __slots__ = ("metadata", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: _common_pb2.OperationMetadata
    status: BatchOperationStatus
    def __init__(self, metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ..., status: _Optional[_Union[BatchOperationStatus, _Mapping]] = ...) -> None: ...

class BatchOperationStatus(_message.Message):
    __slots__ = ("success_count", "failure_count")
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    success_count: int
    failure_count: int
    def __init__(self, success_count: _Optional[int] = ..., failure_count: _Optional[int] = ...) -> None: ...

class ImportAssetsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSearchConfigRequest(_message.Message):
    __slots__ = ("parent", "search_config", "search_config_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    search_config: SearchConfig
    search_config_id: str
    def __init__(self, parent: _Optional[str] = ..., search_config: _Optional[_Union[SearchConfig, _Mapping]] = ..., search_config_id: _Optional[str] = ...) -> None: ...

class UpdateSearchConfigRequest(_message.Message):
    __slots__ = ("search_config", "update_mask")
    SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    search_config: SearchConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, search_config: _Optional[_Union[SearchConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetSearchConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteSearchConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSearchConfigsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSearchConfigsResponse(_message.Message):
    __slots__ = ("search_configs", "next_page_token")
    SEARCH_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_configs: _containers.RepeatedCompositeFieldContainer[SearchConfig]
    next_page_token: str
    def __init__(self, search_configs: _Optional[_Iterable[_Union[SearchConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SearchConfig(_message.Message):
    __slots__ = ("name", "facet_property", "search_criteria_property")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FACET_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CRITERIA_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    name: str
    facet_property: FacetProperty
    search_criteria_property: SearchCriteriaProperty
    def __init__(self, name: _Optional[str] = ..., facet_property: _Optional[_Union[FacetProperty, _Mapping]] = ..., search_criteria_property: _Optional[_Union[SearchCriteriaProperty, _Mapping]] = ...) -> None: ...

class IndexEndpoint(_message.Message):
    __slots__ = ("name", "display_name", "description", "deployed_index", "state", "labels", "create_time", "update_time", "satisfies_pzs", "satisfies_pzi")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[IndexEndpoint.State]
        CREATING: _ClassVar[IndexEndpoint.State]
        CREATED: _ClassVar[IndexEndpoint.State]
        UPDATING: _ClassVar[IndexEndpoint.State]
        FAILED: _ClassVar[IndexEndpoint.State]
    STATE_UNSPECIFIED: IndexEndpoint.State
    CREATING: IndexEndpoint.State
    CREATED: IndexEndpoint.State
    UPDATING: IndexEndpoint.State
    FAILED: IndexEndpoint.State
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    deployed_index: DeployedIndex
    state: IndexEndpoint.State
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., deployed_index: _Optional[_Union[DeployedIndex, _Mapping]] = ..., state: _Optional[_Union[IndexEndpoint.State, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...

class CreateIndexEndpointRequest(_message.Message):
    __slots__ = ("parent", "index_endpoint_id", "index_endpoint")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INDEX_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    index_endpoint_id: str
    index_endpoint: IndexEndpoint
    def __init__(self, parent: _Optional[str] = ..., index_endpoint_id: _Optional[str] = ..., index_endpoint: _Optional[_Union[IndexEndpoint, _Mapping]] = ...) -> None: ...

class CreateIndexEndpointMetadata(_message.Message):
    __slots__ = ("operation_metadata",)
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: _common_pb2.OperationMetadata
    def __init__(self, operation_metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class GetIndexEndpointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListIndexEndpointsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListIndexEndpointsResponse(_message.Message):
    __slots__ = ("index_endpoints", "next_page_token")
    INDEX_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    index_endpoints: _containers.RepeatedCompositeFieldContainer[IndexEndpoint]
    next_page_token: str
    def __init__(self, index_endpoints: _Optional[_Iterable[_Union[IndexEndpoint, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateIndexEndpointRequest(_message.Message):
    __slots__ = ("index_endpoint", "update_mask")
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: IndexEndpoint
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, index_endpoint: _Optional[_Union[IndexEndpoint, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateIndexEndpointMetadata(_message.Message):
    __slots__ = ("operation_metadata",)
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: _common_pb2.OperationMetadata
    def __init__(self, operation_metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DeleteIndexEndpointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteIndexEndpointMetadata(_message.Message):
    __slots__ = ("operation_metadata",)
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: _common_pb2.OperationMetadata
    def __init__(self, operation_metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DeployIndexRequest(_message.Message):
    __slots__ = ("index_endpoint", "deployed_index")
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: str
    deployed_index: DeployedIndex
    def __init__(self, index_endpoint: _Optional[str] = ..., deployed_index: _Optional[_Union[DeployedIndex, _Mapping]] = ...) -> None: ...

class DeployIndexResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeployIndexMetadata(_message.Message):
    __slots__ = ("operation_metadata", "deployed_index")
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: _common_pb2.OperationMetadata
    deployed_index: str
    def __init__(self, operation_metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ..., deployed_index: _Optional[str] = ...) -> None: ...

class UndeployIndexMetadata(_message.Message):
    __slots__ = ("operation_metadata", "deployed_index")
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: _common_pb2.OperationMetadata
    deployed_index: str
    def __init__(self, operation_metadata: _Optional[_Union[_common_pb2.OperationMetadata, _Mapping]] = ..., deployed_index: _Optional[str] = ...) -> None: ...

class UndeployIndexRequest(_message.Message):
    __slots__ = ("index_endpoint",)
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: str
    def __init__(self, index_endpoint: _Optional[str] = ...) -> None: ...

class UndeployIndexResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeployedIndex(_message.Message):
    __slots__ = ("index",)
    INDEX_FIELD_NUMBER: _ClassVar[int]
    index: str
    def __init__(self, index: _Optional[str] = ...) -> None: ...

class FacetProperty(_message.Message):
    __slots__ = ("fixed_range_bucket_spec", "custom_range_bucket_spec", "datetime_bucket_spec", "mapped_fields", "display_name", "result_size", "bucket_type")
    class FixedRangeBucketSpec(_message.Message):
        __slots__ = ("bucket_start", "bucket_granularity", "bucket_count")
        BUCKET_START_FIELD_NUMBER: _ClassVar[int]
        BUCKET_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
        BUCKET_COUNT_FIELD_NUMBER: _ClassVar[int]
        bucket_start: FacetValue
        bucket_granularity: FacetValue
        bucket_count: int
        def __init__(self, bucket_start: _Optional[_Union[FacetValue, _Mapping]] = ..., bucket_granularity: _Optional[_Union[FacetValue, _Mapping]] = ..., bucket_count: _Optional[int] = ...) -> None: ...
    class CustomRangeBucketSpec(_message.Message):
        __slots__ = ("endpoints",)
        ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
        endpoints: _containers.RepeatedCompositeFieldContainer[FacetValue]
        def __init__(self, endpoints: _Optional[_Iterable[_Union[FacetValue, _Mapping]]] = ...) -> None: ...
    class DateTimeBucketSpec(_message.Message):
        __slots__ = ("granularity",)
        class Granularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            GRANULARITY_UNSPECIFIED: _ClassVar[FacetProperty.DateTimeBucketSpec.Granularity]
            YEAR: _ClassVar[FacetProperty.DateTimeBucketSpec.Granularity]
            MONTH: _ClassVar[FacetProperty.DateTimeBucketSpec.Granularity]
            DAY: _ClassVar[FacetProperty.DateTimeBucketSpec.Granularity]
        GRANULARITY_UNSPECIFIED: FacetProperty.DateTimeBucketSpec.Granularity
        YEAR: FacetProperty.DateTimeBucketSpec.Granularity
        MONTH: FacetProperty.DateTimeBucketSpec.Granularity
        DAY: FacetProperty.DateTimeBucketSpec.Granularity
        GRANULARITY_FIELD_NUMBER: _ClassVar[int]
        granularity: FacetProperty.DateTimeBucketSpec.Granularity
        def __init__(self, granularity: _Optional[_Union[FacetProperty.DateTimeBucketSpec.Granularity, str]] = ...) -> None: ...
    FIXED_RANGE_BUCKET_SPEC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_RANGE_BUCKET_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATETIME_BUCKET_SPEC_FIELD_NUMBER: _ClassVar[int]
    MAPPED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_SIZE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_TYPE_FIELD_NUMBER: _ClassVar[int]
    fixed_range_bucket_spec: FacetProperty.FixedRangeBucketSpec
    custom_range_bucket_spec: FacetProperty.CustomRangeBucketSpec
    datetime_bucket_spec: FacetProperty.DateTimeBucketSpec
    mapped_fields: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    result_size: int
    bucket_type: FacetBucketType
    def __init__(self, fixed_range_bucket_spec: _Optional[_Union[FacetProperty.FixedRangeBucketSpec, _Mapping]] = ..., custom_range_bucket_spec: _Optional[_Union[FacetProperty.CustomRangeBucketSpec, _Mapping]] = ..., datetime_bucket_spec: _Optional[_Union[FacetProperty.DateTimeBucketSpec, _Mapping]] = ..., mapped_fields: _Optional[_Iterable[str]] = ..., display_name: _Optional[str] = ..., result_size: _Optional[int] = ..., bucket_type: _Optional[_Union[FacetBucketType, str]] = ...) -> None: ...

class SearchHypernym(_message.Message):
    __slots__ = ("name", "hypernym", "hyponyms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HYPERNYM_FIELD_NUMBER: _ClassVar[int]
    HYPONYMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    hypernym: str
    hyponyms: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., hypernym: _Optional[str] = ..., hyponyms: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateSearchHypernymRequest(_message.Message):
    __slots__ = ("parent", "search_hypernym", "search_hypernym_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_HYPERNYM_FIELD_NUMBER: _ClassVar[int]
    SEARCH_HYPERNYM_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    search_hypernym: SearchHypernym
    search_hypernym_id: str
    def __init__(self, parent: _Optional[str] = ..., search_hypernym: _Optional[_Union[SearchHypernym, _Mapping]] = ..., search_hypernym_id: _Optional[str] = ...) -> None: ...

class UpdateSearchHypernymRequest(_message.Message):
    __slots__ = ("search_hypernym", "update_mask")
    SEARCH_HYPERNYM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    search_hypernym: SearchHypernym
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, search_hypernym: _Optional[_Union[SearchHypernym, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetSearchHypernymRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteSearchHypernymRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSearchHypernymsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSearchHypernymsResponse(_message.Message):
    __slots__ = ("search_hypernyms", "next_page_token")
    SEARCH_HYPERNYMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_hypernyms: _containers.RepeatedCompositeFieldContainer[SearchHypernym]
    next_page_token: str
    def __init__(self, search_hypernyms: _Optional[_Iterable[_Union[SearchHypernym, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SearchCriteriaProperty(_message.Message):
    __slots__ = ("mapped_fields",)
    MAPPED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    mapped_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mapped_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class FacetValue(_message.Message):
    __slots__ = ("string_value", "integer_value", "datetime_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    integer_value: int
    datetime_value: _datetime_pb2.DateTime
    def __init__(self, string_value: _Optional[str] = ..., integer_value: _Optional[int] = ..., datetime_value: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]] = ...) -> None: ...

class FacetBucket(_message.Message):
    __slots__ = ("value", "range", "selected")
    class Range(_message.Message):
        __slots__ = ("start", "end")
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: FacetValue
        end: FacetValue
        def __init__(self, start: _Optional[_Union[FacetValue, _Mapping]] = ..., end: _Optional[_Union[FacetValue, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    value: FacetValue
    range: FacetBucket.Range
    selected: bool
    def __init__(self, value: _Optional[_Union[FacetValue, _Mapping]] = ..., range: _Optional[_Union[FacetBucket.Range, _Mapping]] = ..., selected: bool = ...) -> None: ...

class FacetGroup(_message.Message):
    __slots__ = ("facet_id", "display_name", "buckets", "bucket_type", "fetch_matched_annotations")
    FACET_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    BUCKET_TYPE_FIELD_NUMBER: _ClassVar[int]
    FETCH_MATCHED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    facet_id: str
    display_name: str
    buckets: _containers.RepeatedCompositeFieldContainer[FacetBucket]
    bucket_type: FacetBucketType
    fetch_matched_annotations: bool
    def __init__(self, facet_id: _Optional[str] = ..., display_name: _Optional[str] = ..., buckets: _Optional[_Iterable[_Union[FacetBucket, _Mapping]]] = ..., bucket_type: _Optional[_Union[FacetBucketType, str]] = ..., fetch_matched_annotations: bool = ...) -> None: ...

class IngestAssetRequest(_message.Message):
    __slots__ = ("config", "time_indexed_data")
    class Config(_message.Message):
        __slots__ = ("video_type", "asset")
        class VideoType(_message.Message):
            __slots__ = ("container_format",)
            class ContainerFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CONTAINER_FORMAT_UNSPECIFIED: _ClassVar[IngestAssetRequest.Config.VideoType.ContainerFormat]
                CONTAINER_FORMAT_MP4: _ClassVar[IngestAssetRequest.Config.VideoType.ContainerFormat]
            CONTAINER_FORMAT_UNSPECIFIED: IngestAssetRequest.Config.VideoType.ContainerFormat
            CONTAINER_FORMAT_MP4: IngestAssetRequest.Config.VideoType.ContainerFormat
            CONTAINER_FORMAT_FIELD_NUMBER: _ClassVar[int]
            container_format: IngestAssetRequest.Config.VideoType.ContainerFormat
            def __init__(self, container_format: _Optional[_Union[IngestAssetRequest.Config.VideoType.ContainerFormat, str]] = ...) -> None: ...
        VIDEO_TYPE_FIELD_NUMBER: _ClassVar[int]
        ASSET_FIELD_NUMBER: _ClassVar[int]
        video_type: IngestAssetRequest.Config.VideoType
        asset: str
        def __init__(self, video_type: _Optional[_Union[IngestAssetRequest.Config.VideoType, _Mapping]] = ..., asset: _Optional[str] = ...) -> None: ...
    class TimeIndexedData(_message.Message):
        __slots__ = ("data", "temporal_partition")
        DATA_FIELD_NUMBER: _ClassVar[int]
        TEMPORAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        temporal_partition: Partition.TemporalPartition
        def __init__(self, data: _Optional[bytes] = ..., temporal_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ...) -> None: ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIME_INDEXED_DATA_FIELD_NUMBER: _ClassVar[int]
    config: IngestAssetRequest.Config
    time_indexed_data: IngestAssetRequest.TimeIndexedData
    def __init__(self, config: _Optional[_Union[IngestAssetRequest.Config, _Mapping]] = ..., time_indexed_data: _Optional[_Union[IngestAssetRequest.TimeIndexedData, _Mapping]] = ...) -> None: ...

class IngestAssetResponse(_message.Message):
    __slots__ = ("successfully_ingested_partition",)
    SUCCESSFULLY_INGESTED_PARTITION_FIELD_NUMBER: _ClassVar[int]
    successfully_ingested_partition: Partition.TemporalPartition
    def __init__(self, successfully_ingested_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ...) -> None: ...

class ClipAssetRequest(_message.Message):
    __slots__ = ("name", "temporal_partition")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPORAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
    name: str
    temporal_partition: Partition.TemporalPartition
    def __init__(self, name: _Optional[str] = ..., temporal_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ...) -> None: ...

class ClipAssetResponse(_message.Message):
    __slots__ = ("time_indexed_uris",)
    class TimeIndexedUri(_message.Message):
        __slots__ = ("temporal_partition", "uri")
        TEMPORAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
        URI_FIELD_NUMBER: _ClassVar[int]
        temporal_partition: Partition.TemporalPartition
        uri: str
        def __init__(self, temporal_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ..., uri: _Optional[str] = ...) -> None: ...
    TIME_INDEXED_URIS_FIELD_NUMBER: _ClassVar[int]
    time_indexed_uris: _containers.RepeatedCompositeFieldContainer[ClipAssetResponse.TimeIndexedUri]
    def __init__(self, time_indexed_uris: _Optional[_Iterable[_Union[ClipAssetResponse.TimeIndexedUri, _Mapping]]] = ...) -> None: ...

class GenerateHlsUriRequest(_message.Message):
    __slots__ = ("name", "temporal_partitions", "live_view_enabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPORAL_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    LIVE_VIEW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    temporal_partitions: _containers.RepeatedCompositeFieldContainer[Partition.TemporalPartition]
    live_view_enabled: bool
    def __init__(self, name: _Optional[str] = ..., temporal_partitions: _Optional[_Iterable[_Union[Partition.TemporalPartition, _Mapping]]] = ..., live_view_enabled: bool = ...) -> None: ...

class GenerateHlsUriResponse(_message.Message):
    __slots__ = ("uri", "temporal_partitions")
    URI_FIELD_NUMBER: _ClassVar[int]
    TEMPORAL_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    uri: str
    temporal_partitions: _containers.RepeatedCompositeFieldContainer[Partition.TemporalPartition]
    def __init__(self, uri: _Optional[str] = ..., temporal_partitions: _Optional[_Iterable[_Union[Partition.TemporalPartition, _Mapping]]] = ...) -> None: ...

class SearchAssetsRequest(_message.Message):
    __slots__ = ("schema_key_sorting_strategy", "corpus", "page_size", "page_token", "content_time_ranges", "criteria", "facet_selections", "result_annotation_keys", "search_query")
    SCHEMA_KEY_SORTING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    FACET_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    RESULT_ANNOTATION_KEYS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    schema_key_sorting_strategy: SchemaKeySortingStrategy
    corpus: str
    page_size: int
    page_token: str
    content_time_ranges: DateTimeRangeArray
    criteria: _containers.RepeatedCompositeFieldContainer[Criteria]
    facet_selections: _containers.RepeatedCompositeFieldContainer[FacetGroup]
    result_annotation_keys: _containers.RepeatedScalarFieldContainer[str]
    search_query: str
    def __init__(self, schema_key_sorting_strategy: _Optional[_Union[SchemaKeySortingStrategy, _Mapping]] = ..., corpus: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., content_time_ranges: _Optional[_Union[DateTimeRangeArray, _Mapping]] = ..., criteria: _Optional[_Iterable[_Union[Criteria, _Mapping]]] = ..., facet_selections: _Optional[_Iterable[_Union[FacetGroup, _Mapping]]] = ..., result_annotation_keys: _Optional[_Iterable[str]] = ..., search_query: _Optional[str] = ...) -> None: ...

class SearchIndexEndpointRequest(_message.Message):
    __slots__ = ("image_query", "text_query", "index_endpoint", "criteria", "exclusion_criteria", "page_size", "page_token")
    IMAGE_QUERY_FIELD_NUMBER: _ClassVar[int]
    TEXT_QUERY_FIELD_NUMBER: _ClassVar[int]
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    image_query: ImageQuery
    text_query: str
    index_endpoint: str
    criteria: _containers.RepeatedCompositeFieldContainer[Criteria]
    exclusion_criteria: _containers.RepeatedCompositeFieldContainer[Criteria]
    page_size: int
    page_token: str
    def __init__(self, image_query: _Optional[_Union[ImageQuery, _Mapping]] = ..., text_query: _Optional[str] = ..., index_endpoint: _Optional[str] = ..., criteria: _Optional[_Iterable[_Union[Criteria, _Mapping]]] = ..., exclusion_criteria: _Optional[_Iterable[_Union[Criteria, _Mapping]]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ImageQuery(_message.Message):
    __slots__ = ("input_image", "asset")
    INPUT_IMAGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    input_image: bytes
    asset: str
    def __init__(self, input_image: _Optional[bytes] = ..., asset: _Optional[str] = ...) -> None: ...

class SchemaKeySortingStrategy(_message.Message):
    __slots__ = ("options",)
    class Option(_message.Message):
        __slots__ = ("data_schema_key", "sort_decreasing", "aggregate_method")
        class AggregateMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AGGREGATE_METHOD_UNSPECIFIED: _ClassVar[SchemaKeySortingStrategy.Option.AggregateMethod]
            AGGREGATE_METHOD_LARGEST: _ClassVar[SchemaKeySortingStrategy.Option.AggregateMethod]
            AGGREGATE_METHOD_SMALLEST: _ClassVar[SchemaKeySortingStrategy.Option.AggregateMethod]
        AGGREGATE_METHOD_UNSPECIFIED: SchemaKeySortingStrategy.Option.AggregateMethod
        AGGREGATE_METHOD_LARGEST: SchemaKeySortingStrategy.Option.AggregateMethod
        AGGREGATE_METHOD_SMALLEST: SchemaKeySortingStrategy.Option.AggregateMethod
        DATA_SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
        SORT_DECREASING_FIELD_NUMBER: _ClassVar[int]
        AGGREGATE_METHOD_FIELD_NUMBER: _ClassVar[int]
        data_schema_key: str
        sort_decreasing: bool
        aggregate_method: SchemaKeySortingStrategy.Option.AggregateMethod
        def __init__(self, data_schema_key: _Optional[str] = ..., sort_decreasing: bool = ..., aggregate_method: _Optional[_Union[SchemaKeySortingStrategy.Option.AggregateMethod, str]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedCompositeFieldContainer[SchemaKeySortingStrategy.Option]
    def __init__(self, options: _Optional[_Iterable[_Union[SchemaKeySortingStrategy.Option, _Mapping]]] = ...) -> None: ...

class DeleteAssetMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AnnotationMatchingResult(_message.Message):
    __slots__ = ("criteria", "matched_annotations", "status")
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    MATCHED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    criteria: Criteria
    matched_annotations: _containers.RepeatedCompositeFieldContainer[Annotation]
    status: _status_pb2.Status
    def __init__(self, criteria: _Optional[_Union[Criteria, _Mapping]] = ..., matched_annotations: _Optional[_Iterable[_Union[Annotation, _Mapping]]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class SearchResultItem(_message.Message):
    __slots__ = ("asset", "segments", "segment", "relevance", "requested_annotations", "annotation_matching_results")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_MATCHING_RESULTS_FIELD_NUMBER: _ClassVar[int]
    asset: str
    segments: _containers.RepeatedCompositeFieldContainer[Partition.TemporalPartition]
    segment: Partition.TemporalPartition
    relevance: float
    requested_annotations: _containers.RepeatedCompositeFieldContainer[Annotation]
    annotation_matching_results: _containers.RepeatedCompositeFieldContainer[AnnotationMatchingResult]
    def __init__(self, asset: _Optional[str] = ..., segments: _Optional[_Iterable[_Union[Partition.TemporalPartition, _Mapping]]] = ..., segment: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ..., relevance: _Optional[float] = ..., requested_annotations: _Optional[_Iterable[_Union[Annotation, _Mapping]]] = ..., annotation_matching_results: _Optional[_Iterable[_Union[AnnotationMatchingResult, _Mapping]]] = ...) -> None: ...

class SearchAssetsResponse(_message.Message):
    __slots__ = ("search_result_items", "next_page_token", "facet_results")
    SEARCH_RESULT_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FACET_RESULTS_FIELD_NUMBER: _ClassVar[int]
    search_result_items: _containers.RepeatedCompositeFieldContainer[SearchResultItem]
    next_page_token: str
    facet_results: _containers.RepeatedCompositeFieldContainer[FacetGroup]
    def __init__(self, search_result_items: _Optional[_Iterable[_Union[SearchResultItem, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., facet_results: _Optional[_Iterable[_Union[FacetGroup, _Mapping]]] = ...) -> None: ...

class SearchIndexEndpointResponse(_message.Message):
    __slots__ = ("search_result_items", "next_page_token")
    SEARCH_RESULT_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_result_items: _containers.RepeatedCompositeFieldContainer[SearchResultItem]
    next_page_token: str
    def __init__(self, search_result_items: _Optional[_Iterable[_Union[SearchResultItem, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class IntRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class FloatRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: float
    end: float
    def __init__(self, start: _Optional[float] = ..., end: _Optional[float] = ...) -> None: ...

class StringArray(_message.Message):
    __slots__ = ("txt_values",)
    TXT_VALUES_FIELD_NUMBER: _ClassVar[int]
    txt_values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, txt_values: _Optional[_Iterable[str]] = ...) -> None: ...

class IntRangeArray(_message.Message):
    __slots__ = ("int_ranges",)
    INT_RANGES_FIELD_NUMBER: _ClassVar[int]
    int_ranges: _containers.RepeatedCompositeFieldContainer[IntRange]
    def __init__(self, int_ranges: _Optional[_Iterable[_Union[IntRange, _Mapping]]] = ...) -> None: ...

class FloatRangeArray(_message.Message):
    __slots__ = ("float_ranges",)
    FLOAT_RANGES_FIELD_NUMBER: _ClassVar[int]
    float_ranges: _containers.RepeatedCompositeFieldContainer[FloatRange]
    def __init__(self, float_ranges: _Optional[_Iterable[_Union[FloatRange, _Mapping]]] = ...) -> None: ...

class DateTimeRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: _datetime_pb2.DateTime
    end: _datetime_pb2.DateTime
    def __init__(self, start: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]] = ..., end: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]] = ...) -> None: ...

class DateTimeRangeArray(_message.Message):
    __slots__ = ("date_time_ranges",)
    DATE_TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    date_time_ranges: _containers.RepeatedCompositeFieldContainer[DateTimeRange]
    def __init__(self, date_time_ranges: _Optional[_Iterable[_Union[DateTimeRange, _Mapping]]] = ...) -> None: ...

class CircleArea(_message.Message):
    __slots__ = ("latitude", "longitude", "radius_meter")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_METER_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    radius_meter: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., radius_meter: _Optional[float] = ...) -> None: ...

class GeoLocationArray(_message.Message):
    __slots__ = ("circle_areas",)
    CIRCLE_AREAS_FIELD_NUMBER: _ClassVar[int]
    circle_areas: _containers.RepeatedCompositeFieldContainer[CircleArea]
    def __init__(self, circle_areas: _Optional[_Iterable[_Union[CircleArea, _Mapping]]] = ...) -> None: ...

class BoolValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class Criteria(_message.Message):
    __slots__ = ("text_array", "int_range_array", "float_range_array", "date_time_range_array", "geo_location_array", "bool_value", "field", "fetch_matched_annotations")
    TEXT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    INT_RANGE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    FLOAT_RANGE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_RANGE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    GEO_LOCATION_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    FETCH_MATCHED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    text_array: StringArray
    int_range_array: IntRangeArray
    float_range_array: FloatRangeArray
    date_time_range_array: DateTimeRangeArray
    geo_location_array: GeoLocationArray
    bool_value: BoolValue
    field: str
    fetch_matched_annotations: bool
    def __init__(self, text_array: _Optional[_Union[StringArray, _Mapping]] = ..., int_range_array: _Optional[_Union[IntRangeArray, _Mapping]] = ..., float_range_array: _Optional[_Union[FloatRangeArray, _Mapping]] = ..., date_time_range_array: _Optional[_Union[DateTimeRangeArray, _Mapping]] = ..., geo_location_array: _Optional[_Union[GeoLocationArray, _Mapping]] = ..., bool_value: _Optional[_Union[BoolValue, _Mapping]] = ..., field: _Optional[str] = ..., fetch_matched_annotations: bool = ...) -> None: ...

class Partition(_message.Message):
    __slots__ = ("temporal_partition", "spatial_partition", "relative_temporal_partition")
    class TemporalPartition(_message.Message):
        __slots__ = ("start_time", "end_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class SpatialPartition(_message.Message):
        __slots__ = ("x_min", "y_min", "x_max", "y_max")
        X_MIN_FIELD_NUMBER: _ClassVar[int]
        Y_MIN_FIELD_NUMBER: _ClassVar[int]
        X_MAX_FIELD_NUMBER: _ClassVar[int]
        Y_MAX_FIELD_NUMBER: _ClassVar[int]
        x_min: int
        y_min: int
        x_max: int
        y_max: int
        def __init__(self, x_min: _Optional[int] = ..., y_min: _Optional[int] = ..., x_max: _Optional[int] = ..., y_max: _Optional[int] = ...) -> None: ...
    class RelativeTemporalPartition(_message.Message):
        __slots__ = ("start_offset", "end_offset")
        START_OFFSET_FIELD_NUMBER: _ClassVar[int]
        END_OFFSET_FIELD_NUMBER: _ClassVar[int]
        start_offset: _duration_pb2.Duration
        end_offset: _duration_pb2.Duration
        def __init__(self, start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    TEMPORAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
    SPATIAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_TEMPORAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
    temporal_partition: Partition.TemporalPartition
    spatial_partition: Partition.SpatialPartition
    relative_temporal_partition: Partition.RelativeTemporalPartition
    def __init__(self, temporal_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ..., spatial_partition: _Optional[_Union[Partition.SpatialPartition, _Mapping]] = ..., relative_temporal_partition: _Optional[_Union[Partition.RelativeTemporalPartition, _Mapping]] = ...) -> None: ...
