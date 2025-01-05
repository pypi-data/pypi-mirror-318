from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.retail.v2alpha import common_pb2 as _common_pb2
from google.cloud.retail.v2alpha import product_pb2 as _product_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserEvent(_message.Message):
    __slots__ = ("event_type", "visitor_id", "session_id", "event_time", "experiment_ids", "attribution_token", "product_details", "completion_detail", "attributes", "cart_id", "purchase_transaction", "search_query", "filter", "order_by", "offset", "page_categories", "user_info", "uri", "referrer_uri", "page_view_id", "entity")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.CustomAttribute
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.CustomAttribute, _Mapping]] = ...) -> None: ...
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VISITOR_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CART_ID_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PAGE_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    REFERRER_URI_FIELD_NUMBER: _ClassVar[int]
    PAGE_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    visitor_id: str
    session_id: str
    event_time: _timestamp_pb2.Timestamp
    experiment_ids: _containers.RepeatedScalarFieldContainer[str]
    attribution_token: str
    product_details: _containers.RepeatedCompositeFieldContainer[ProductDetail]
    completion_detail: CompletionDetail
    attributes: _containers.MessageMap[str, _common_pb2.CustomAttribute]
    cart_id: str
    purchase_transaction: PurchaseTransaction
    search_query: str
    filter: str
    order_by: str
    offset: int
    page_categories: _containers.RepeatedScalarFieldContainer[str]
    user_info: _common_pb2.UserInfo
    uri: str
    referrer_uri: str
    page_view_id: str
    entity: str
    def __init__(self, event_type: _Optional[str] = ..., visitor_id: _Optional[str] = ..., session_id: _Optional[str] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., experiment_ids: _Optional[_Iterable[str]] = ..., attribution_token: _Optional[str] = ..., product_details: _Optional[_Iterable[_Union[ProductDetail, _Mapping]]] = ..., completion_detail: _Optional[_Union[CompletionDetail, _Mapping]] = ..., attributes: _Optional[_Mapping[str, _common_pb2.CustomAttribute]] = ..., cart_id: _Optional[str] = ..., purchase_transaction: _Optional[_Union[PurchaseTransaction, _Mapping]] = ..., search_query: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., offset: _Optional[int] = ..., page_categories: _Optional[_Iterable[str]] = ..., user_info: _Optional[_Union[_common_pb2.UserInfo, _Mapping]] = ..., uri: _Optional[str] = ..., referrer_uri: _Optional[str] = ..., page_view_id: _Optional[str] = ..., entity: _Optional[str] = ...) -> None: ...

class ProductDetail(_message.Message):
    __slots__ = ("product", "quantity")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.Product
    quantity: _wrappers_pb2.Int32Value
    def __init__(self, product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ..., quantity: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class CompletionDetail(_message.Message):
    __slots__ = ("completion_attribution_token", "selected_suggestion", "selected_position")
    COMPLETION_ATTRIBUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    SELECTED_POSITION_FIELD_NUMBER: _ClassVar[int]
    completion_attribution_token: str
    selected_suggestion: str
    selected_position: int
    def __init__(self, completion_attribution_token: _Optional[str] = ..., selected_suggestion: _Optional[str] = ..., selected_position: _Optional[int] = ...) -> None: ...

class PurchaseTransaction(_message.Message):
    __slots__ = ("id", "revenue", "tax", "cost", "currency_code")
    ID_FIELD_NUMBER: _ClassVar[int]
    REVENUE_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    revenue: float
    tax: float
    cost: float
    currency_code: str
    def __init__(self, id: _Optional[str] = ..., revenue: _Optional[float] = ..., tax: _Optional[float] = ..., cost: _Optional[float] = ..., currency_code: _Optional[str] = ...) -> None: ...
