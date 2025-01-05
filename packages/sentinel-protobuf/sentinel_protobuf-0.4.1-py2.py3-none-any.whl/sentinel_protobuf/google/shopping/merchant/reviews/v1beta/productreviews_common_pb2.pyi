from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductReviewAttributes(_message.Message):
    __slots__ = ("aggregator_name", "subclient_name", "publisher_name", "publisher_favicon", "reviewer_id", "reviewer_is_anonymous", "reviewer_username", "review_language", "review_country", "review_time", "title", "content", "pros", "cons", "review_link", "reviewer_image_links", "min_rating", "max_rating", "rating", "product_names", "product_links", "asins", "gtins", "mpns", "skus", "brands", "is_spam", "collection_method", "transaction_id")
    class CollectionMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLLECTION_METHOD_UNSPECIFIED: _ClassVar[ProductReviewAttributes.CollectionMethod]
        UNSOLICITED: _ClassVar[ProductReviewAttributes.CollectionMethod]
        POST_FULFILLMENT: _ClassVar[ProductReviewAttributes.CollectionMethod]
    COLLECTION_METHOD_UNSPECIFIED: ProductReviewAttributes.CollectionMethod
    UNSOLICITED: ProductReviewAttributes.CollectionMethod
    POST_FULFILLMENT: ProductReviewAttributes.CollectionMethod
    class ReviewLink(_message.Message):
        __slots__ = ("type", "link")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[ProductReviewAttributes.ReviewLink.Type]
            SINGLETON: _ClassVar[ProductReviewAttributes.ReviewLink.Type]
            GROUP: _ClassVar[ProductReviewAttributes.ReviewLink.Type]
        TYPE_UNSPECIFIED: ProductReviewAttributes.ReviewLink.Type
        SINGLETON: ProductReviewAttributes.ReviewLink.Type
        GROUP: ProductReviewAttributes.ReviewLink.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        type: ProductReviewAttributes.ReviewLink.Type
        link: str
        def __init__(self, type: _Optional[_Union[ProductReviewAttributes.ReviewLink.Type, str]] = ..., link: _Optional[str] = ...) -> None: ...
    AGGREGATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBCLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FAVICON_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_IS_ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    REVIEW_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REVIEW_TIME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PROS_FIELD_NUMBER: _ClassVar[int]
    CONS_FIELD_NUMBER: _ClassVar[int]
    REVIEW_LINK_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_IMAGE_LINKS_FIELD_NUMBER: _ClassVar[int]
    MIN_RATING_FIELD_NUMBER: _ClassVar[int]
    MAX_RATING_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAMES_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LINKS_FIELD_NUMBER: _ClassVar[int]
    ASINS_FIELD_NUMBER: _ClassVar[int]
    GTINS_FIELD_NUMBER: _ClassVar[int]
    MPNS_FIELD_NUMBER: _ClassVar[int]
    SKUS_FIELD_NUMBER: _ClassVar[int]
    BRANDS_FIELD_NUMBER: _ClassVar[int]
    IS_SPAM_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_METHOD_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    aggregator_name: str
    subclient_name: str
    publisher_name: str
    publisher_favicon: str
    reviewer_id: str
    reviewer_is_anonymous: bool
    reviewer_username: str
    review_language: str
    review_country: str
    review_time: _timestamp_pb2.Timestamp
    title: str
    content: str
    pros: _containers.RepeatedScalarFieldContainer[str]
    cons: _containers.RepeatedScalarFieldContainer[str]
    review_link: ProductReviewAttributes.ReviewLink
    reviewer_image_links: _containers.RepeatedScalarFieldContainer[str]
    min_rating: int
    max_rating: int
    rating: float
    product_names: _containers.RepeatedScalarFieldContainer[str]
    product_links: _containers.RepeatedScalarFieldContainer[str]
    asins: _containers.RepeatedScalarFieldContainer[str]
    gtins: _containers.RepeatedScalarFieldContainer[str]
    mpns: _containers.RepeatedScalarFieldContainer[str]
    skus: _containers.RepeatedScalarFieldContainer[str]
    brands: _containers.RepeatedScalarFieldContainer[str]
    is_spam: bool
    collection_method: ProductReviewAttributes.CollectionMethod
    transaction_id: str
    def __init__(self, aggregator_name: _Optional[str] = ..., subclient_name: _Optional[str] = ..., publisher_name: _Optional[str] = ..., publisher_favicon: _Optional[str] = ..., reviewer_id: _Optional[str] = ..., reviewer_is_anonymous: bool = ..., reviewer_username: _Optional[str] = ..., review_language: _Optional[str] = ..., review_country: _Optional[str] = ..., review_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., pros: _Optional[_Iterable[str]] = ..., cons: _Optional[_Iterable[str]] = ..., review_link: _Optional[_Union[ProductReviewAttributes.ReviewLink, _Mapping]] = ..., reviewer_image_links: _Optional[_Iterable[str]] = ..., min_rating: _Optional[int] = ..., max_rating: _Optional[int] = ..., rating: _Optional[float] = ..., product_names: _Optional[_Iterable[str]] = ..., product_links: _Optional[_Iterable[str]] = ..., asins: _Optional[_Iterable[str]] = ..., gtins: _Optional[_Iterable[str]] = ..., mpns: _Optional[_Iterable[str]] = ..., skus: _Optional[_Iterable[str]] = ..., brands: _Optional[_Iterable[str]] = ..., is_spam: bool = ..., collection_method: _Optional[_Union[ProductReviewAttributes.CollectionMethod, str]] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class ProductReviewStatus(_message.Message):
    __slots__ = ("destination_statuses", "item_level_issues", "create_time", "last_update_time")
    class ProductReviewDestinationStatus(_message.Message):
        __slots__ = ("reporting_context",)
        REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
        def __init__(self, reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]] = ...) -> None: ...
    class ProductReviewItemLevelIssue(_message.Message):
        __slots__ = ("code", "severity", "resolution", "attribute", "reporting_context", "description", "detail", "documentation")
        class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEVERITY_UNSPECIFIED: _ClassVar[ProductReviewStatus.ProductReviewItemLevelIssue.Severity]
            NOT_IMPACTED: _ClassVar[ProductReviewStatus.ProductReviewItemLevelIssue.Severity]
            DISAPPROVED: _ClassVar[ProductReviewStatus.ProductReviewItemLevelIssue.Severity]
        SEVERITY_UNSPECIFIED: ProductReviewStatus.ProductReviewItemLevelIssue.Severity
        NOT_IMPACTED: ProductReviewStatus.ProductReviewItemLevelIssue.Severity
        DISAPPROVED: ProductReviewStatus.ProductReviewItemLevelIssue.Severity
        CODE_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
        code: str
        severity: ProductReviewStatus.ProductReviewItemLevelIssue.Severity
        resolution: str
        attribute: str
        reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
        description: str
        detail: str
        documentation: str
        def __init__(self, code: _Optional[str] = ..., severity: _Optional[_Union[ProductReviewStatus.ProductReviewItemLevelIssue.Severity, str]] = ..., resolution: _Optional[str] = ..., attribute: _Optional[str] = ..., reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]] = ..., description: _Optional[str] = ..., detail: _Optional[str] = ..., documentation: _Optional[str] = ...) -> None: ...
    DESTINATION_STATUSES_FIELD_NUMBER: _ClassVar[int]
    ITEM_LEVEL_ISSUES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    destination_statuses: _containers.RepeatedCompositeFieldContainer[ProductReviewStatus.ProductReviewDestinationStatus]
    item_level_issues: _containers.RepeatedCompositeFieldContainer[ProductReviewStatus.ProductReviewItemLevelIssue]
    create_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp
    def __init__(self, destination_statuses: _Optional[_Iterable[_Union[ProductReviewStatus.ProductReviewDestinationStatus, _Mapping]]] = ..., item_level_issues: _Optional[_Iterable[_Union[ProductReviewStatus.ProductReviewItemLevelIssue, _Mapping]]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
