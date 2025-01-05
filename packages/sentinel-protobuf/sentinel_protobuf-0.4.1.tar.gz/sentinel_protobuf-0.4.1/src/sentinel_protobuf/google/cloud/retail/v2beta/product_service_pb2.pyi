from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2beta import common_pb2 as _common_pb2
from google.cloud.retail.v2beta import export_config_pb2 as _export_config_pb2
from google.cloud.retail.v2beta import import_config_pb2 as _import_config_pb2
from google.cloud.retail.v2beta import product_pb2 as _product_pb2
from google.cloud.retail.v2beta import purge_config_pb2 as _purge_config_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProductRequest(_message.Message):
    __slots__ = ("parent", "product", "product_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    product: _product_pb2.Product
    product_id: str
    def __init__(self, parent: _Optional[str] = ..., product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ..., product_id: _Optional[str] = ...) -> None: ...

class GetProductRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateProductRequest(_message.Message):
    __slots__ = ("product", "update_mask", "allow_missing")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.Product
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    def __init__(self, product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class DeleteProductRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListProductsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListProductsResponse(_message.Message):
    __slots__ = ("products", "next_page_token")
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[_product_pb2.Product]
    next_page_token: str
    def __init__(self, products: _Optional[_Iterable[_Union[_product_pb2.Product, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SetInventoryRequest(_message.Message):
    __slots__ = ("inventory", "set_mask", "set_time", "allow_missing")
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    SET_MASK_FIELD_NUMBER: _ClassVar[int]
    SET_TIME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    inventory: _product_pb2.Product
    set_mask: _field_mask_pb2.FieldMask
    set_time: _timestamp_pb2.Timestamp
    allow_missing: bool
    def __init__(self, inventory: _Optional[_Union[_product_pb2.Product, _Mapping]] = ..., set_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., set_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class SetInventoryMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetInventoryResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddFulfillmentPlacesRequest(_message.Message):
    __slots__ = ("product", "type", "place_ids", "add_time", "allow_missing")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PLACE_IDS_FIELD_NUMBER: _ClassVar[int]
    ADD_TIME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    product: str
    type: str
    place_ids: _containers.RepeatedScalarFieldContainer[str]
    add_time: _timestamp_pb2.Timestamp
    allow_missing: bool
    def __init__(self, product: _Optional[str] = ..., type: _Optional[str] = ..., place_ids: _Optional[_Iterable[str]] = ..., add_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class AddFulfillmentPlacesMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddFulfillmentPlacesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddLocalInventoriesRequest(_message.Message):
    __slots__ = ("product", "local_inventories", "add_mask", "add_time", "allow_missing")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    ADD_MASK_FIELD_NUMBER: _ClassVar[int]
    ADD_TIME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    product: str
    local_inventories: _containers.RepeatedCompositeFieldContainer[_common_pb2.LocalInventory]
    add_mask: _field_mask_pb2.FieldMask
    add_time: _timestamp_pb2.Timestamp
    allow_missing: bool
    def __init__(self, product: _Optional[str] = ..., local_inventories: _Optional[_Iterable[_Union[_common_pb2.LocalInventory, _Mapping]]] = ..., add_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., add_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class AddLocalInventoriesMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddLocalInventoriesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveLocalInventoriesRequest(_message.Message):
    __slots__ = ("product", "place_ids", "remove_time", "allow_missing")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PLACE_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_TIME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    product: str
    place_ids: _containers.RepeatedScalarFieldContainer[str]
    remove_time: _timestamp_pb2.Timestamp
    allow_missing: bool
    def __init__(self, product: _Optional[str] = ..., place_ids: _Optional[_Iterable[str]] = ..., remove_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class RemoveLocalInventoriesMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveLocalInventoriesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveFulfillmentPlacesRequest(_message.Message):
    __slots__ = ("product", "type", "place_ids", "remove_time", "allow_missing")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PLACE_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_TIME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    product: str
    type: str
    place_ids: _containers.RepeatedScalarFieldContainer[str]
    remove_time: _timestamp_pb2.Timestamp
    allow_missing: bool
    def __init__(self, product: _Optional[str] = ..., type: _Optional[str] = ..., place_ids: _Optional[_Iterable[str]] = ..., remove_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class RemoveFulfillmentPlacesMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveFulfillmentPlacesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
