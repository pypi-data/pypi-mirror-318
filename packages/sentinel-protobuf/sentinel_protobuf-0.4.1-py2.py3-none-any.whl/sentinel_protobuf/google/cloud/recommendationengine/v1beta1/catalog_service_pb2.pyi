from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.recommendationengine.v1beta1 import catalog_pb2 as _catalog_pb2
from google.cloud.recommendationengine.v1beta1 import import_pb2 as _import_pb2
from google.cloud.recommendationengine.v1beta1 import recommendationengine_resources_pb2 as _recommendationengine_resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateCatalogItemRequest(_message.Message):
    __slots__ = ('parent', 'catalog_item')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ITEM_FIELD_NUMBER: _ClassVar[int]
    parent: str
    catalog_item: _catalog_pb2.CatalogItem

    def __init__(self, parent: _Optional[str]=..., catalog_item: _Optional[_Union[_catalog_pb2.CatalogItem, _Mapping]]=...) -> None:
        ...

class GetCatalogItemRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCatalogItemsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListCatalogItemsResponse(_message.Message):
    __slots__ = ('catalog_items', 'next_page_token')
    CATALOG_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    catalog_items: _containers.RepeatedCompositeFieldContainer[_catalog_pb2.CatalogItem]
    next_page_token: str

    def __init__(self, catalog_items: _Optional[_Iterable[_Union[_catalog_pb2.CatalogItem, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateCatalogItemRequest(_message.Message):
    __slots__ = ('name', 'catalog_item', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ITEM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    catalog_item: _catalog_pb2.CatalogItem
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., catalog_item: _Optional[_Union[_catalog_pb2.CatalogItem, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCatalogItemRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...