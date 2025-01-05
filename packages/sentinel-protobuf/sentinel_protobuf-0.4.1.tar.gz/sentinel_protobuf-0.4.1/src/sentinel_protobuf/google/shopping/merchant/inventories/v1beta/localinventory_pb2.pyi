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

class LocalInventory(_message.Message):
    __slots__ = ("name", "account", "store_code", "price", "sale_price", "sale_price_effective_date", "availability", "quantity", "pickup_method", "pickup_sla", "instore_product_location", "custom_attributes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORE_CODE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PICKUP_METHOD_FIELD_NUMBER: _ClassVar[int]
    PICKUP_SLA_FIELD_NUMBER: _ClassVar[int]
    INSTORE_PRODUCT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    account: int
    store_code: str
    price: _types_pb2.Price
    sale_price: _types_pb2.Price
    sale_price_effective_date: _interval_pb2.Interval
    availability: str
    quantity: int
    pickup_method: str
    pickup_sla: str
    instore_product_location: str
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_types_pb2.CustomAttribute]
    def __init__(self, name: _Optional[str] = ..., account: _Optional[int] = ..., store_code: _Optional[str] = ..., price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., sale_price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., sale_price_effective_date: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., availability: _Optional[str] = ..., quantity: _Optional[int] = ..., pickup_method: _Optional[str] = ..., pickup_sla: _Optional[str] = ..., instore_product_location: _Optional[str] = ..., custom_attributes: _Optional[_Iterable[_Union[_types_pb2.CustomAttribute, _Mapping]]] = ...) -> None: ...

class ListLocalInventoriesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListLocalInventoriesResponse(_message.Message):
    __slots__ = ("local_inventories", "next_page_token")
    LOCAL_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    local_inventories: _containers.RepeatedCompositeFieldContainer[LocalInventory]
    next_page_token: str
    def __init__(self, local_inventories: _Optional[_Iterable[_Union[LocalInventory, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class InsertLocalInventoryRequest(_message.Message):
    __slots__ = ("parent", "local_inventory")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    local_inventory: LocalInventory
    def __init__(self, parent: _Optional[str] = ..., local_inventory: _Optional[_Union[LocalInventory, _Mapping]] = ...) -> None: ...

class DeleteLocalInventoryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
