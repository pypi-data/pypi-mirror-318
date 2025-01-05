from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.commerce.consumer.procurement.v1alpha1 import order_pb2 as _order_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PlaceOrderRequest(_message.Message):
    __slots__ = ('parent', 'display_name', 'line_item_info', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    display_name: str
    line_item_info: _containers.RepeatedCompositeFieldContainer[_order_pb2.LineItemInfo]
    request_id: str

    def __init__(self, parent: _Optional[str]=..., display_name: _Optional[str]=..., line_item_info: _Optional[_Iterable[_Union[_order_pb2.LineItemInfo, _Mapping]]]=..., request_id: _Optional[str]=...) -> None:
        ...

class PlaceOrderMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetOrderRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListOrdersRequest(_message.Message):
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

class ListOrdersResponse(_message.Message):
    __slots__ = ('orders', 'next_page_token')
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[_order_pb2.Order]
    next_page_token: str

    def __init__(self, orders: _Optional[_Iterable[_Union[_order_pb2.Order, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...