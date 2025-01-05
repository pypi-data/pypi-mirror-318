from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.recommendationengine.v1beta1 import catalog_pb2 as _catalog_pb2
from google.cloud.recommendationengine.v1beta1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UserEvent(_message.Message):
    __slots__ = ('event_type', 'user_info', 'event_detail', 'product_event_detail', 'event_time', 'event_source')

    class EventSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_SOURCE_UNSPECIFIED: _ClassVar[UserEvent.EventSource]
        AUTOML: _ClassVar[UserEvent.EventSource]
        ECOMMERCE: _ClassVar[UserEvent.EventSource]
        BATCH_UPLOAD: _ClassVar[UserEvent.EventSource]
    EVENT_SOURCE_UNSPECIFIED: UserEvent.EventSource
    AUTOML: UserEvent.EventSource
    ECOMMERCE: UserEvent.EventSource
    BATCH_UPLOAD: UserEvent.EventSource
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    EVENT_DETAIL_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_EVENT_DETAIL_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    user_info: UserInfo
    event_detail: EventDetail
    product_event_detail: ProductEventDetail
    event_time: _timestamp_pb2.Timestamp
    event_source: UserEvent.EventSource

    def __init__(self, event_type: _Optional[str]=..., user_info: _Optional[_Union[UserInfo, _Mapping]]=..., event_detail: _Optional[_Union[EventDetail, _Mapping]]=..., product_event_detail: _Optional[_Union[ProductEventDetail, _Mapping]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., event_source: _Optional[_Union[UserEvent.EventSource, str]]=...) -> None:
        ...

class UserInfo(_message.Message):
    __slots__ = ('visitor_id', 'user_id', 'ip_address', 'user_agent', 'direct_user_request')
    VISITOR_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    DIRECT_USER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    visitor_id: str
    user_id: str
    ip_address: str
    user_agent: str
    direct_user_request: bool

    def __init__(self, visitor_id: _Optional[str]=..., user_id: _Optional[str]=..., ip_address: _Optional[str]=..., user_agent: _Optional[str]=..., direct_user_request: bool=...) -> None:
        ...

class EventDetail(_message.Message):
    __slots__ = ('uri', 'referrer_uri', 'page_view_id', 'experiment_ids', 'recommendation_token', 'event_attributes')
    URI_FIELD_NUMBER: _ClassVar[int]
    REFERRER_URI_FIELD_NUMBER: _ClassVar[int]
    PAGE_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    uri: str
    referrer_uri: str
    page_view_id: str
    experiment_ids: _containers.RepeatedScalarFieldContainer[str]
    recommendation_token: str
    event_attributes: _common_pb2.FeatureMap

    def __init__(self, uri: _Optional[str]=..., referrer_uri: _Optional[str]=..., page_view_id: _Optional[str]=..., experiment_ids: _Optional[_Iterable[str]]=..., recommendation_token: _Optional[str]=..., event_attributes: _Optional[_Union[_common_pb2.FeatureMap, _Mapping]]=...) -> None:
        ...

class ProductEventDetail(_message.Message):
    __slots__ = ('search_query', 'page_categories', 'product_details', 'list_id', 'cart_id', 'purchase_transaction')
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    CART_ID_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    search_query: str
    page_categories: _containers.RepeatedCompositeFieldContainer[_catalog_pb2.CatalogItem.CategoryHierarchy]
    product_details: _containers.RepeatedCompositeFieldContainer[ProductDetail]
    list_id: str
    cart_id: str
    purchase_transaction: PurchaseTransaction

    def __init__(self, search_query: _Optional[str]=..., page_categories: _Optional[_Iterable[_Union[_catalog_pb2.CatalogItem.CategoryHierarchy, _Mapping]]]=..., product_details: _Optional[_Iterable[_Union[ProductDetail, _Mapping]]]=..., list_id: _Optional[str]=..., cart_id: _Optional[str]=..., purchase_transaction: _Optional[_Union[PurchaseTransaction, _Mapping]]=...) -> None:
        ...

class PurchaseTransaction(_message.Message):
    __slots__ = ('id', 'revenue', 'taxes', 'costs', 'currency_code')

    class TaxesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float

        def __init__(self, key: _Optional[str]=..., value: _Optional[float]=...) -> None:
            ...

    class CostsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float

        def __init__(self, key: _Optional[str]=..., value: _Optional[float]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    REVENUE_FIELD_NUMBER: _ClassVar[int]
    TAXES_FIELD_NUMBER: _ClassVar[int]
    COSTS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    revenue: float
    taxes: _containers.ScalarMap[str, float]
    costs: _containers.ScalarMap[str, float]
    currency_code: str

    def __init__(self, id: _Optional[str]=..., revenue: _Optional[float]=..., taxes: _Optional[_Mapping[str, float]]=..., costs: _Optional[_Mapping[str, float]]=..., currency_code: _Optional[str]=...) -> None:
        ...

class ProductDetail(_message.Message):
    __slots__ = ('id', 'currency_code', 'original_price', 'display_price', 'stock_state', 'quantity', 'available_quantity', 'item_attributes')
    ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_PRICE_FIELD_NUMBER: _ClassVar[int]
    STOCK_STATE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    currency_code: str
    original_price: float
    display_price: float
    stock_state: _catalog_pb2.ProductCatalogItem.StockState
    quantity: int
    available_quantity: int
    item_attributes: _common_pb2.FeatureMap

    def __init__(self, id: _Optional[str]=..., currency_code: _Optional[str]=..., original_price: _Optional[float]=..., display_price: _Optional[float]=..., stock_state: _Optional[_Union[_catalog_pb2.ProductCatalogItem.StockState, str]]=..., quantity: _Optional[int]=..., available_quantity: _Optional[int]=..., item_attributes: _Optional[_Union[_common_pb2.FeatureMap, _Mapping]]=...) -> None:
        ...