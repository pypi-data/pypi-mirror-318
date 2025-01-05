from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegionalInventory(_message.Message):
    __slots__ = ("name", "account", "region", "price", "sale_price", "sale_price_effective_date", "availability", "custom_attributes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    account: int
    region: str
    price: _types_pb2.Price
    sale_price: _types_pb2.Price
    sale_price_effective_date: _interval_pb2.Interval
    availability: str
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_types_pb2.CustomAttribute]
    def __init__(self, name: _Optional[str] = ..., account: _Optional[int] = ..., region: _Optional[str] = ..., price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., sale_price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., sale_price_effective_date: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., availability: _Optional[str] = ..., custom_attributes: _Optional[_Iterable[_Union[_types_pb2.CustomAttribute, _Mapping]]] = ...) -> None: ...

class ListRegionalInventoriesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRegionalInventoriesResponse(_message.Message):
    __slots__ = ("regional_inventories", "next_page_token")
    REGIONAL_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    regional_inventories: _containers.RepeatedCompositeFieldContainer[RegionalInventory]
    next_page_token: str
    def __init__(self, regional_inventories: _Optional[_Iterable[_Union[RegionalInventory, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class InsertRegionalInventoryRequest(_message.Message):
    __slots__ = ("parent", "regional_inventory")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REGIONAL_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    regional_inventory: RegionalInventory
    def __init__(self, parent: _Optional[str] = ..., regional_inventory: _Optional[_Union[RegionalInventory, _Mapping]] = ...) -> None: ...

class DeleteRegionalInventoryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
