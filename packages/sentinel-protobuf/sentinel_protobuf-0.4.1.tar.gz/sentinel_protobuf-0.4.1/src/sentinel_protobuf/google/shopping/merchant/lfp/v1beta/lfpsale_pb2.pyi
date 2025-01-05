from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LfpSale(_message.Message):
    __slots__ = ("name", "target_account", "store_code", "offer_id", "region_code", "content_language", "gtin", "price", "quantity", "sale_time", "uid", "feed_label")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORE_CODE_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    GTIN_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SALE_TIME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_account: int
    store_code: str
    offer_id: str
    region_code: str
    content_language: str
    gtin: str
    price: _types_pb2.Price
    quantity: int
    sale_time: _timestamp_pb2.Timestamp
    uid: str
    feed_label: str
    def __init__(self, name: _Optional[str] = ..., target_account: _Optional[int] = ..., store_code: _Optional[str] = ..., offer_id: _Optional[str] = ..., region_code: _Optional[str] = ..., content_language: _Optional[str] = ..., gtin: _Optional[str] = ..., price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., quantity: _Optional[int] = ..., sale_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., uid: _Optional[str] = ..., feed_label: _Optional[str] = ...) -> None: ...

class InsertLfpSaleRequest(_message.Message):
    __slots__ = ("parent", "lfp_sale")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LFP_SALE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    lfp_sale: LfpSale
    def __init__(self, parent: _Optional[str] = ..., lfp_sale: _Optional[_Union[LfpSale, _Mapping]] = ...) -> None: ...
