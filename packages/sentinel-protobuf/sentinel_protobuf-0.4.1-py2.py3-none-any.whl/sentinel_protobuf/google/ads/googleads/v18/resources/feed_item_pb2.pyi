from google.ads.googleads.v18.common import custom_parameter_pb2 as _custom_parameter_pb2
from google.ads.googleads.v18.common import feed_common_pb2 as _feed_common_pb2
from google.ads.googleads.v18.common import policy_pb2 as _policy_pb2
from google.ads.googleads.v18.enums import feed_item_quality_approval_status_pb2 as _feed_item_quality_approval_status_pb2
from google.ads.googleads.v18.enums import feed_item_quality_disapproval_reason_pb2 as _feed_item_quality_disapproval_reason_pb2
from google.ads.googleads.v18.enums import feed_item_status_pb2 as _feed_item_status_pb2
from google.ads.googleads.v18.enums import feed_item_validation_status_pb2 as _feed_item_validation_status_pb2
from google.ads.googleads.v18.enums import geo_targeting_restriction_pb2 as _geo_targeting_restriction_pb2
from google.ads.googleads.v18.enums import placeholder_type_pb2 as _placeholder_type_pb2
from google.ads.googleads.v18.enums import policy_approval_status_pb2 as _policy_approval_status_pb2
from google.ads.googleads.v18.enums import policy_review_status_pb2 as _policy_review_status_pb2
from google.ads.googleads.v18.errors import feed_item_validation_error_pb2 as _feed_item_validation_error_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedItem(_message.Message):
    __slots__ = ("resource_name", "feed", "id", "start_date_time", "end_date_time", "attribute_values", "geo_targeting_restriction", "url_custom_parameters", "status", "policy_infos")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    FEED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VALUES_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGETING_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POLICY_INFOS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    feed: str
    id: int
    start_date_time: str
    end_date_time: str
    attribute_values: _containers.RepeatedCompositeFieldContainer[FeedItemAttributeValue]
    geo_targeting_restriction: _geo_targeting_restriction_pb2.GeoTargetingRestrictionEnum.GeoTargetingRestriction
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    status: _feed_item_status_pb2.FeedItemStatusEnum.FeedItemStatus
    policy_infos: _containers.RepeatedCompositeFieldContainer[FeedItemPlaceholderPolicyInfo]
    def __init__(self, resource_name: _Optional[str] = ..., feed: _Optional[str] = ..., id: _Optional[int] = ..., start_date_time: _Optional[str] = ..., end_date_time: _Optional[str] = ..., attribute_values: _Optional[_Iterable[_Union[FeedItemAttributeValue, _Mapping]]] = ..., geo_targeting_restriction: _Optional[_Union[_geo_targeting_restriction_pb2.GeoTargetingRestrictionEnum.GeoTargetingRestriction, str]] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., status: _Optional[_Union[_feed_item_status_pb2.FeedItemStatusEnum.FeedItemStatus, str]] = ..., policy_infos: _Optional[_Iterable[_Union[FeedItemPlaceholderPolicyInfo, _Mapping]]] = ...) -> None: ...

class FeedItemAttributeValue(_message.Message):
    __slots__ = ("feed_attribute_id", "integer_value", "boolean_value", "string_value", "double_value", "price_value", "integer_values", "boolean_values", "string_values", "double_values")
    FEED_ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    PRICE_VALUE_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUES_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_VALUES_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUES_FIELD_NUMBER: _ClassVar[int]
    feed_attribute_id: int
    integer_value: int
    boolean_value: bool
    string_value: str
    double_value: float
    price_value: _feed_common_pb2.Money
    integer_values: _containers.RepeatedScalarFieldContainer[int]
    boolean_values: _containers.RepeatedScalarFieldContainer[bool]
    string_values: _containers.RepeatedScalarFieldContainer[str]
    double_values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, feed_attribute_id: _Optional[int] = ..., integer_value: _Optional[int] = ..., boolean_value: bool = ..., string_value: _Optional[str] = ..., double_value: _Optional[float] = ..., price_value: _Optional[_Union[_feed_common_pb2.Money, _Mapping]] = ..., integer_values: _Optional[_Iterable[int]] = ..., boolean_values: _Optional[_Iterable[bool]] = ..., string_values: _Optional[_Iterable[str]] = ..., double_values: _Optional[_Iterable[float]] = ...) -> None: ...

class FeedItemPlaceholderPolicyInfo(_message.Message):
    __slots__ = ("placeholder_type_enum", "feed_mapping_resource_name", "review_status", "approval_status", "policy_topic_entries", "validation_status", "validation_errors", "quality_approval_status", "quality_disapproval_reasons")
    PLACEHOLDER_TYPE_ENUM_FIELD_NUMBER: _ClassVar[int]
    FEED_MAPPING_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    POLICY_TOPIC_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_DISAPPROVAL_REASONS_FIELD_NUMBER: _ClassVar[int]
    placeholder_type_enum: _placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType
    feed_mapping_resource_name: str
    review_status: _policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: _policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus
    policy_topic_entries: _containers.RepeatedCompositeFieldContainer[_policy_pb2.PolicyTopicEntry]
    validation_status: _feed_item_validation_status_pb2.FeedItemValidationStatusEnum.FeedItemValidationStatus
    validation_errors: _containers.RepeatedCompositeFieldContainer[FeedItemValidationError]
    quality_approval_status: _feed_item_quality_approval_status_pb2.FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    quality_disapproval_reasons: _containers.RepeatedScalarFieldContainer[_feed_item_quality_disapproval_reason_pb2.FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
    def __init__(self, placeholder_type_enum: _Optional[_Union[_placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType, str]] = ..., feed_mapping_resource_name: _Optional[str] = ..., review_status: _Optional[_Union[_policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus, str]] = ..., approval_status: _Optional[_Union[_policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus, str]] = ..., policy_topic_entries: _Optional[_Iterable[_Union[_policy_pb2.PolicyTopicEntry, _Mapping]]] = ..., validation_status: _Optional[_Union[_feed_item_validation_status_pb2.FeedItemValidationStatusEnum.FeedItemValidationStatus, str]] = ..., validation_errors: _Optional[_Iterable[_Union[FeedItemValidationError, _Mapping]]] = ..., quality_approval_status: _Optional[_Union[_feed_item_quality_approval_status_pb2.FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus, str]] = ..., quality_disapproval_reasons: _Optional[_Iterable[_Union[_feed_item_quality_disapproval_reason_pb2.FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason, str]]] = ...) -> None: ...

class FeedItemValidationError(_message.Message):
    __slots__ = ("validation_error", "description", "feed_attribute_ids", "extra_info")
    VALIDATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FEED_ATTRIBUTE_IDS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    validation_error: _feed_item_validation_error_pb2.FeedItemValidationErrorEnum.FeedItemValidationError
    description: str
    feed_attribute_ids: _containers.RepeatedScalarFieldContainer[int]
    extra_info: str
    def __init__(self, validation_error: _Optional[_Union[_feed_item_validation_error_pb2.FeedItemValidationErrorEnum.FeedItemValidationError, str]] = ..., description: _Optional[str] = ..., feed_attribute_ids: _Optional[_Iterable[int]] = ..., extra_info: _Optional[str] = ...) -> None: ...
