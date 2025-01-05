from google.ads.admanager.v1 import ad_unit_messages_pb2 as _ad_unit_messages_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAdUnitRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAdUnitsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "skip")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    skip: int
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., skip: _Optional[int] = ...) -> None: ...

class ListAdUnitsResponse(_message.Message):
    __slots__ = ("ad_units", "next_page_token", "total_size")
    AD_UNITS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    ad_units: _containers.RepeatedCompositeFieldContainer[_ad_unit_messages_pb2.AdUnit]
    next_page_token: str
    total_size: int
    def __init__(self, ad_units: _Optional[_Iterable[_Union[_ad_unit_messages_pb2.AdUnit, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class ListAdUnitSizesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "skip")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    skip: int
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., skip: _Optional[int] = ...) -> None: ...

class ListAdUnitSizesResponse(_message.Message):
    __slots__ = ("ad_unit_sizes", "next_page_token", "total_size")
    AD_UNIT_SIZES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    ad_unit_sizes: _containers.RepeatedCompositeFieldContainer[_ad_unit_messages_pb2.AdUnitSize]
    next_page_token: str
    total_size: int
    def __init__(self, ad_unit_sizes: _Optional[_Iterable[_Union[_ad_unit_messages_pb2.AdUnitSize, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...
