from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.shopping.merchant.reviews.v1beta import merchantreviews_common_pb2 as _merchantreviews_common_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMerchantReviewRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteMerchantReviewRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListMerchantReviewsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class InsertMerchantReviewRequest(_message.Message):
    __slots__ = ("parent", "merchant_review", "data_source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_REVIEW_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    merchant_review: MerchantReview
    data_source: str
    def __init__(self, parent: _Optional[str] = ..., merchant_review: _Optional[_Union[MerchantReview, _Mapping]] = ..., data_source: _Optional[str] = ...) -> None: ...

class ListMerchantReviewsResponse(_message.Message):
    __slots__ = ("merchant_reviews", "next_page_token")
    MERCHANT_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    merchant_reviews: _containers.RepeatedCompositeFieldContainer[MerchantReview]
    next_page_token: str
    def __init__(self, merchant_reviews: _Optional[_Iterable[_Union[MerchantReview, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class MerchantReview(_message.Message):
    __slots__ = ("name", "merchant_review_id", "attributes", "custom_attributes", "data_source", "merchant_review_status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_REVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    merchant_review_id: str
    attributes: _merchantreviews_common_pb2.MerchantReviewAttributes
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_types_pb2.CustomAttribute]
    data_source: str
    merchant_review_status: _merchantreviews_common_pb2.MerchantReviewStatus
    def __init__(self, name: _Optional[str] = ..., merchant_review_id: _Optional[str] = ..., attributes: _Optional[_Union[_merchantreviews_common_pb2.MerchantReviewAttributes, _Mapping]] = ..., custom_attributes: _Optional[_Iterable[_Union[_types_pb2.CustomAttribute, _Mapping]]] = ..., data_source: _Optional[str] = ..., merchant_review_status: _Optional[_Union[_merchantreviews_common_pb2.MerchantReviewStatus, _Mapping]] = ...) -> None: ...
