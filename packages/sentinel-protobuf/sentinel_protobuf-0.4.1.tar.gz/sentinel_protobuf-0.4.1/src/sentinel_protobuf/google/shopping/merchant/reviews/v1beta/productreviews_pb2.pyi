from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.shopping.merchant.reviews.v1beta import productreviews_common_pb2 as _productreviews_common_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProductReviewRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteProductReviewRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListProductReviewsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class InsertProductReviewRequest(_message.Message):
    __slots__ = ("parent", "product_review", "data_source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_REVIEW_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    product_review: ProductReview
    data_source: str
    def __init__(self, parent: _Optional[str] = ..., product_review: _Optional[_Union[ProductReview, _Mapping]] = ..., data_source: _Optional[str] = ...) -> None: ...

class ListProductReviewsResponse(_message.Message):
    __slots__ = ("product_reviews", "next_page_token")
    PRODUCT_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    product_reviews: _containers.RepeatedCompositeFieldContainer[ProductReview]
    next_page_token: str
    def __init__(self, product_reviews: _Optional[_Iterable[_Union[ProductReview, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ProductReview(_message.Message):
    __slots__ = ("name", "product_review_id", "attributes", "custom_attributes", "data_source", "product_review_status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_REVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    product_review_id: str
    attributes: _productreviews_common_pb2.ProductReviewAttributes
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_types_pb2.CustomAttribute]
    data_source: str
    product_review_status: _productreviews_common_pb2.ProductReviewStatus
    def __init__(self, name: _Optional[str] = ..., product_review_id: _Optional[str] = ..., attributes: _Optional[_Union[_productreviews_common_pb2.ProductReviewAttributes, _Mapping]] = ..., custom_attributes: _Optional[_Iterable[_Union[_types_pb2.CustomAttribute, _Mapping]]] = ..., data_source: _Optional[str] = ..., product_review_status: _Optional[_Union[_productreviews_common_pb2.ProductReviewStatus, _Mapping]] = ...) -> None: ...
