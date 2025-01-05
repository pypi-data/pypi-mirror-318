from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.shopping.merchant.promotions.v1beta import promotions_common_pb2 as _promotions_common_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Promotion(_message.Message):
    __slots__ = ("name", "promotion_id", "content_language", "target_country", "redemption_channel", "data_source", "attributes", "custom_attributes", "promotion_status", "version_number")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REDEMPTION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    name: str
    promotion_id: str
    content_language: str
    target_country: str
    redemption_channel: _containers.RepeatedScalarFieldContainer[_promotions_common_pb2.RedemptionChannel]
    data_source: str
    attributes: _promotions_common_pb2.Attributes
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_types_pb2.CustomAttribute]
    promotion_status: _promotions_common_pb2.PromotionStatus
    version_number: int
    def __init__(self, name: _Optional[str] = ..., promotion_id: _Optional[str] = ..., content_language: _Optional[str] = ..., target_country: _Optional[str] = ..., redemption_channel: _Optional[_Iterable[_Union[_promotions_common_pb2.RedemptionChannel, str]]] = ..., data_source: _Optional[str] = ..., attributes: _Optional[_Union[_promotions_common_pb2.Attributes, _Mapping]] = ..., custom_attributes: _Optional[_Iterable[_Union[_types_pb2.CustomAttribute, _Mapping]]] = ..., promotion_status: _Optional[_Union[_promotions_common_pb2.PromotionStatus, _Mapping]] = ..., version_number: _Optional[int] = ...) -> None: ...

class InsertPromotionRequest(_message.Message):
    __slots__ = ("parent", "promotion", "data_source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    promotion: Promotion
    data_source: str
    def __init__(self, parent: _Optional[str] = ..., promotion: _Optional[_Union[Promotion, _Mapping]] = ..., data_source: _Optional[str] = ...) -> None: ...

class GetPromotionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPromotionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListPromotionsResponse(_message.Message):
    __slots__ = ("promotions", "next_page_token")
    PROMOTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    promotions: _containers.RepeatedCompositeFieldContainer[Promotion]
    next_page_token: str
    def __init__(self, promotions: _Optional[_Iterable[_Union[Promotion, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
