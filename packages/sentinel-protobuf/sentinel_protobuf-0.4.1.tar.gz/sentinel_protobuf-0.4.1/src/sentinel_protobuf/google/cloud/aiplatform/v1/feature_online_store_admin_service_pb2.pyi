from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import feature_online_store_pb2 as _feature_online_store_pb2
from google.cloud.aiplatform.v1 import feature_view_pb2 as _feature_view_pb2
from google.cloud.aiplatform.v1 import feature_view_sync_pb2 as _feature_view_sync_pb2
from google.cloud.aiplatform.v1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFeatureOnlineStoreRequest(_message.Message):
    __slots__ = ("parent", "feature_online_store", "feature_online_store_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ONLINE_STORE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ONLINE_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feature_online_store: _feature_online_store_pb2.FeatureOnlineStore
    feature_online_store_id: str
    def __init__(self, parent: _Optional[str] = ..., feature_online_store: _Optional[_Union[_feature_online_store_pb2.FeatureOnlineStore, _Mapping]] = ..., feature_online_store_id: _Optional[str] = ...) -> None: ...

class GetFeatureOnlineStoreRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListFeatureOnlineStoresRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListFeatureOnlineStoresResponse(_message.Message):
    __slots__ = ("feature_online_stores", "next_page_token")
    FEATURE_ONLINE_STORES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    feature_online_stores: _containers.RepeatedCompositeFieldContainer[_feature_online_store_pb2.FeatureOnlineStore]
    next_page_token: str
    def __init__(self, feature_online_stores: _Optional[_Iterable[_Union[_feature_online_store_pb2.FeatureOnlineStore, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateFeatureOnlineStoreRequest(_message.Message):
    __slots__ = ("feature_online_store", "update_mask")
    FEATURE_ONLINE_STORE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    feature_online_store: _feature_online_store_pb2.FeatureOnlineStore
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, feature_online_store: _Optional[_Union[_feature_online_store_pb2.FeatureOnlineStore, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteFeatureOnlineStoreRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class CreateFeatureViewRequest(_message.Message):
    __slots__ = ("parent", "feature_view", "feature_view_id", "run_sync_immediately")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_VIEW_FIELD_NUMBER: _ClassVar[int]
    FEATURE_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_SYNC_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feature_view: _feature_view_pb2.FeatureView
    feature_view_id: str
    run_sync_immediately: bool
    def __init__(self, parent: _Optional[str] = ..., feature_view: _Optional[_Union[_feature_view_pb2.FeatureView, _Mapping]] = ..., feature_view_id: _Optional[str] = ..., run_sync_immediately: bool = ...) -> None: ...

class GetFeatureViewRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListFeatureViewsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListFeatureViewsResponse(_message.Message):
    __slots__ = ("feature_views", "next_page_token")
    FEATURE_VIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    feature_views: _containers.RepeatedCompositeFieldContainer[_feature_view_pb2.FeatureView]
    next_page_token: str
    def __init__(self, feature_views: _Optional[_Iterable[_Union[_feature_view_pb2.FeatureView, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateFeatureViewRequest(_message.Message):
    __slots__ = ("feature_view", "update_mask")
    FEATURE_VIEW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    feature_view: _feature_view_pb2.FeatureView
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, feature_view: _Optional[_Union[_feature_view_pb2.FeatureView, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteFeatureViewRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFeatureOnlineStoreOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class UpdateFeatureOnlineStoreOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class CreateFeatureViewOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class UpdateFeatureViewOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class SyncFeatureViewRequest(_message.Message):
    __slots__ = ("feature_view",)
    FEATURE_VIEW_FIELD_NUMBER: _ClassVar[int]
    feature_view: str
    def __init__(self, feature_view: _Optional[str] = ...) -> None: ...

class SyncFeatureViewResponse(_message.Message):
    __slots__ = ("feature_view_sync",)
    FEATURE_VIEW_SYNC_FIELD_NUMBER: _ClassVar[int]
    feature_view_sync: str
    def __init__(self, feature_view_sync: _Optional[str] = ...) -> None: ...

class GetFeatureViewSyncRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListFeatureViewSyncsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListFeatureViewSyncsResponse(_message.Message):
    __slots__ = ("feature_view_syncs", "next_page_token")
    FEATURE_VIEW_SYNCS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    feature_view_syncs: _containers.RepeatedCompositeFieldContainer[_feature_view_sync_pb2.FeatureViewSync]
    next_page_token: str
    def __init__(self, feature_view_syncs: _Optional[_Iterable[_Union[_feature_view_sync_pb2.FeatureViewSync, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
