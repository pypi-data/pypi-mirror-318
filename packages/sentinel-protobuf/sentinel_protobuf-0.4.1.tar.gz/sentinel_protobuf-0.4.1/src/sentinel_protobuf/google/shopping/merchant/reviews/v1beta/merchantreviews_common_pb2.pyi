from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MerchantReviewAttributes(_message.Message):
    __slots__ = ("merchant_id", "merchant_display_name", "merchant_link", "merchant_rating_link", "min_rating", "max_rating", "rating", "title", "content", "reviewer_id", "reviewer_username", "is_anonymous", "collection_method", "review_time", "review_language", "review_country")
    class CollectionMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLLECTION_METHOD_UNSPECIFIED: _ClassVar[MerchantReviewAttributes.CollectionMethod]
        MERCHANT_UNSOLICITED: _ClassVar[MerchantReviewAttributes.CollectionMethod]
        POINT_OF_SALE: _ClassVar[MerchantReviewAttributes.CollectionMethod]
        AFTER_FULFILLMENT: _ClassVar[MerchantReviewAttributes.CollectionMethod]
    COLLECTION_METHOD_UNSPECIFIED: MerchantReviewAttributes.CollectionMethod
    MERCHANT_UNSOLICITED: MerchantReviewAttributes.CollectionMethod
    POINT_OF_SALE: MerchantReviewAttributes.CollectionMethod
    AFTER_FULFILLMENT: MerchantReviewAttributes.CollectionMethod
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_LINK_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_RATING_LINK_FIELD_NUMBER: _ClassVar[int]
    MIN_RATING_FIELD_NUMBER: _ClassVar[int]
    MAX_RATING_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    IS_ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_METHOD_FIELD_NUMBER: _ClassVar[int]
    REVIEW_TIME_FIELD_NUMBER: _ClassVar[int]
    REVIEW_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    merchant_id: str
    merchant_display_name: str
    merchant_link: str
    merchant_rating_link: str
    min_rating: int
    max_rating: int
    rating: float
    title: str
    content: str
    reviewer_id: str
    reviewer_username: str
    is_anonymous: bool
    collection_method: MerchantReviewAttributes.CollectionMethod
    review_time: _timestamp_pb2.Timestamp
    review_language: str
    review_country: str
    def __init__(self, merchant_id: _Optional[str] = ..., merchant_display_name: _Optional[str] = ..., merchant_link: _Optional[str] = ..., merchant_rating_link: _Optional[str] = ..., min_rating: _Optional[int] = ..., max_rating: _Optional[int] = ..., rating: _Optional[float] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., reviewer_id: _Optional[str] = ..., reviewer_username: _Optional[str] = ..., is_anonymous: bool = ..., collection_method: _Optional[_Union[MerchantReviewAttributes.CollectionMethod, str]] = ..., review_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., review_language: _Optional[str] = ..., review_country: _Optional[str] = ...) -> None: ...

class MerchantReviewStatus(_message.Message):
    __slots__ = ("destination_statuses", "item_level_issues", "create_time", "last_update_time")
    class MerchantReviewDestinationStatus(_message.Message):
        __slots__ = ("reporting_context",)
        REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
        def __init__(self, reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]] = ...) -> None: ...
    class MerchantReviewItemLevelIssue(_message.Message):
        __slots__ = ("code", "severity", "resolution", "attribute", "reporting_context", "description", "detail", "documentation")
        class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEVERITY_UNSPECIFIED: _ClassVar[MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity]
            NOT_IMPACTED: _ClassVar[MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity]
            DISAPPROVED: _ClassVar[MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity]
        SEVERITY_UNSPECIFIED: MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity
        NOT_IMPACTED: MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity
        DISAPPROVED: MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity
        CODE_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
        code: str
        severity: MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity
        resolution: str
        attribute: str
        reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
        description: str
        detail: str
        documentation: str
        def __init__(self, code: _Optional[str] = ..., severity: _Optional[_Union[MerchantReviewStatus.MerchantReviewItemLevelIssue.Severity, str]] = ..., resolution: _Optional[str] = ..., attribute: _Optional[str] = ..., reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]] = ..., description: _Optional[str] = ..., detail: _Optional[str] = ..., documentation: _Optional[str] = ...) -> None: ...
    DESTINATION_STATUSES_FIELD_NUMBER: _ClassVar[int]
    ITEM_LEVEL_ISSUES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    destination_statuses: _containers.RepeatedCompositeFieldContainer[MerchantReviewStatus.MerchantReviewDestinationStatus]
    item_level_issues: _containers.RepeatedCompositeFieldContainer[MerchantReviewStatus.MerchantReviewItemLevelIssue]
    create_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp
    def __init__(self, destination_statuses: _Optional[_Iterable[_Union[MerchantReviewStatus.MerchantReviewDestinationStatus, _Mapping]]] = ..., item_level_issues: _Optional[_Iterable[_Union[MerchantReviewStatus.MerchantReviewItemLevelIssue, _Mapping]]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
