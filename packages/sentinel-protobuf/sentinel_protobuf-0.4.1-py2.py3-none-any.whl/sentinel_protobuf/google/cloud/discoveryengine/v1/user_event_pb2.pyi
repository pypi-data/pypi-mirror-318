from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1 import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserEvent(_message.Message):
    __slots__ = ("event_type", "user_pseudo_id", "engine", "data_store", "event_time", "user_info", "direct_user_request", "session_id", "page_info", "attribution_token", "filter", "documents", "panel", "search_info", "completion_info", "transaction_info", "tag_ids", "promotion_ids", "attributes", "media_info")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.CustomAttribute
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.CustomAttribute, _Mapping]] = ...) -> None: ...
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_PSEUDO_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    DIRECT_USER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    PANEL_FIELD_NUMBER: _ClassVar[int]
    SEARCH_INFO_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_INFO_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_INFO_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_IDS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    MEDIA_INFO_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    user_pseudo_id: str
    engine: str
    data_store: str
    event_time: _timestamp_pb2.Timestamp
    user_info: _common_pb2.UserInfo
    direct_user_request: bool
    session_id: str
    page_info: PageInfo
    attribution_token: str
    filter: str
    documents: _containers.RepeatedCompositeFieldContainer[DocumentInfo]
    panel: PanelInfo
    search_info: SearchInfo
    completion_info: CompletionInfo
    transaction_info: TransactionInfo
    tag_ids: _containers.RepeatedScalarFieldContainer[str]
    promotion_ids: _containers.RepeatedScalarFieldContainer[str]
    attributes: _containers.MessageMap[str, _common_pb2.CustomAttribute]
    media_info: MediaInfo
    def __init__(self, event_type: _Optional[str] = ..., user_pseudo_id: _Optional[str] = ..., engine: _Optional[str] = ..., data_store: _Optional[str] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_info: _Optional[_Union[_common_pb2.UserInfo, _Mapping]] = ..., direct_user_request: bool = ..., session_id: _Optional[str] = ..., page_info: _Optional[_Union[PageInfo, _Mapping]] = ..., attribution_token: _Optional[str] = ..., filter: _Optional[str] = ..., documents: _Optional[_Iterable[_Union[DocumentInfo, _Mapping]]] = ..., panel: _Optional[_Union[PanelInfo, _Mapping]] = ..., search_info: _Optional[_Union[SearchInfo, _Mapping]] = ..., completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., transaction_info: _Optional[_Union[TransactionInfo, _Mapping]] = ..., tag_ids: _Optional[_Iterable[str]] = ..., promotion_ids: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Mapping[str, _common_pb2.CustomAttribute]] = ..., media_info: _Optional[_Union[MediaInfo, _Mapping]] = ...) -> None: ...

class PageInfo(_message.Message):
    __slots__ = ("pageview_id", "page_category", "uri", "referrer_uri")
    PAGEVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    REFERRER_URI_FIELD_NUMBER: _ClassVar[int]
    pageview_id: str
    page_category: str
    uri: str
    referrer_uri: str
    def __init__(self, pageview_id: _Optional[str] = ..., page_category: _Optional[str] = ..., uri: _Optional[str] = ..., referrer_uri: _Optional[str] = ...) -> None: ...

class SearchInfo(_message.Message):
    __slots__ = ("search_query", "order_by", "offset")
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    search_query: str
    order_by: str
    offset: int
    def __init__(self, search_query: _Optional[str] = ..., order_by: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class CompletionInfo(_message.Message):
    __slots__ = ("selected_suggestion", "selected_position")
    SELECTED_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    SELECTED_POSITION_FIELD_NUMBER: _ClassVar[int]
    selected_suggestion: str
    selected_position: int
    def __init__(self, selected_suggestion: _Optional[str] = ..., selected_position: _Optional[int] = ...) -> None: ...

class TransactionInfo(_message.Message):
    __slots__ = ("value", "currency", "transaction_id", "tax", "cost", "discount_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    currency: str
    transaction_id: str
    tax: float
    cost: float
    discount_value: float
    def __init__(self, value: _Optional[float] = ..., currency: _Optional[str] = ..., transaction_id: _Optional[str] = ..., tax: _Optional[float] = ..., cost: _Optional[float] = ..., discount_value: _Optional[float] = ...) -> None: ...

class DocumentInfo(_message.Message):
    __slots__ = ("id", "name", "uri", "quantity", "promotion_ids", "joined")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_IDS_FIELD_NUMBER: _ClassVar[int]
    JOINED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    uri: str
    quantity: int
    promotion_ids: _containers.RepeatedScalarFieldContainer[str]
    joined: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., uri: _Optional[str] = ..., quantity: _Optional[int] = ..., promotion_ids: _Optional[_Iterable[str]] = ..., joined: bool = ...) -> None: ...

class PanelInfo(_message.Message):
    __slots__ = ("panel_id", "display_name", "panel_position", "total_panels")
    PANEL_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PANEL_POSITION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PANELS_FIELD_NUMBER: _ClassVar[int]
    panel_id: str
    display_name: str
    panel_position: int
    total_panels: int
    def __init__(self, panel_id: _Optional[str] = ..., display_name: _Optional[str] = ..., panel_position: _Optional[int] = ..., total_panels: _Optional[int] = ...) -> None: ...

class MediaInfo(_message.Message):
    __slots__ = ("media_progress_duration", "media_progress_percentage")
    MEDIA_PROGRESS_DURATION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_PROGRESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    media_progress_duration: _duration_pb2.Duration
    media_progress_percentage: float
    def __init__(self, media_progress_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., media_progress_percentage: _Optional[float] = ...) -> None: ...
