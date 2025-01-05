from google.ads.googleads.v18.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v18.resources import asset_group_listing_group_filter_pb2 as _asset_group_listing_group_filter_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateAssetGroupListingGroupFiltersRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "validate_only", "response_content_type")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[AssetGroupListingGroupFilterOperation]
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[AssetGroupListingGroupFilterOperation, _Mapping]]] = ..., validate_only: bool = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class AssetGroupListingGroupFilterOperation(_message.Message):
    __slots__ = ("update_mask", "create", "update", "remove")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _asset_group_listing_group_filter_pb2.AssetGroupListingGroupFilter
    update: _asset_group_listing_group_filter_pb2.AssetGroupListingGroupFilter
    remove: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., create: _Optional[_Union[_asset_group_listing_group_filter_pb2.AssetGroupListingGroupFilter, _Mapping]] = ..., update: _Optional[_Union[_asset_group_listing_group_filter_pb2.AssetGroupListingGroupFilter, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateAssetGroupListingGroupFiltersResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MutateAssetGroupListingGroupFilterResult]
    def __init__(self, results: _Optional[_Iterable[_Union[MutateAssetGroupListingGroupFilterResult, _Mapping]]] = ...) -> None: ...

class MutateAssetGroupListingGroupFilterResult(_message.Message):
    __slots__ = ("resource_name", "asset_group_listing_group_filter")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_LISTING_GROUP_FILTER_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_group_listing_group_filter: _asset_group_listing_group_filter_pb2.AssetGroupListingGroupFilter
    def __init__(self, resource_name: _Optional[str] = ..., asset_group_listing_group_filter: _Optional[_Union[_asset_group_listing_group_filter_pb2.AssetGroupListingGroupFilter, _Mapping]] = ...) -> None: ...
