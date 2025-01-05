from google.ads.googleads.v17.enums import brand_state_pb2 as _brand_state_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestBrandsRequest(_message.Message):
    __slots__ = ("customer_id", "brand_prefix", "selected_brands")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    BRAND_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SELECTED_BRANDS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    brand_prefix: str
    selected_brands: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, customer_id: _Optional[str] = ..., brand_prefix: _Optional[str] = ..., selected_brands: _Optional[_Iterable[str]] = ...) -> None: ...

class SuggestBrandsResponse(_message.Message):
    __slots__ = ("brands",)
    BRANDS_FIELD_NUMBER: _ClassVar[int]
    brands: _containers.RepeatedCompositeFieldContainer[BrandSuggestion]
    def __init__(self, brands: _Optional[_Iterable[_Union[BrandSuggestion, _Mapping]]] = ...) -> None: ...

class BrandSuggestion(_message.Message):
    __slots__ = ("id", "name", "urls", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    urls: _containers.RepeatedScalarFieldContainer[str]
    state: _brand_state_pb2.BrandStateEnum.BrandState
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., urls: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[_brand_state_pb2.BrandStateEnum.BrandState, str]] = ...) -> None: ...
