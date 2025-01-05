from google.ads.googleads.v16.common import policy_pb2 as _policy_pb2
from google.ads.googleads.v16.enums import ad_group_ad_primary_status_pb2 as _ad_group_ad_primary_status_pb2
from google.ads.googleads.v16.enums import ad_group_ad_primary_status_reason_pb2 as _ad_group_ad_primary_status_reason_pb2
from google.ads.googleads.v16.enums import ad_group_ad_status_pb2 as _ad_group_ad_status_pb2
from google.ads.googleads.v16.enums import ad_strength_pb2 as _ad_strength_pb2
from google.ads.googleads.v16.enums import policy_approval_status_pb2 as _policy_approval_status_pb2
from google.ads.googleads.v16.enums import policy_review_status_pb2 as _policy_review_status_pb2
from google.ads.googleads.v16.resources import ad_pb2 as _ad_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAd(_message.Message):
    __slots__ = ("resource_name", "status", "ad_group", "ad", "policy_summary", "ad_strength", "action_items", "labels", "primary_status", "primary_status_reasons")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    AD_FIELD_NUMBER: _ClassVar[int]
    POLICY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    AD_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    ACTION_ITEMS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_REASONS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    status: _ad_group_ad_status_pb2.AdGroupAdStatusEnum.AdGroupAdStatus
    ad_group: str
    ad: _ad_pb2.Ad
    policy_summary: AdGroupAdPolicySummary
    ad_strength: _ad_strength_pb2.AdStrengthEnum.AdStrength
    action_items: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.RepeatedScalarFieldContainer[str]
    primary_status: _ad_group_ad_primary_status_pb2.AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    primary_status_reasons: _containers.RepeatedScalarFieldContainer[_ad_group_ad_primary_status_reason_pb2.AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
    def __init__(self, resource_name: _Optional[str] = ..., status: _Optional[_Union[_ad_group_ad_status_pb2.AdGroupAdStatusEnum.AdGroupAdStatus, str]] = ..., ad_group: _Optional[str] = ..., ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ..., policy_summary: _Optional[_Union[AdGroupAdPolicySummary, _Mapping]] = ..., ad_strength: _Optional[_Union[_ad_strength_pb2.AdStrengthEnum.AdStrength, str]] = ..., action_items: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[str]] = ..., primary_status: _Optional[_Union[_ad_group_ad_primary_status_pb2.AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus, str]] = ..., primary_status_reasons: _Optional[_Iterable[_Union[_ad_group_ad_primary_status_reason_pb2.AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason, str]]] = ...) -> None: ...

class AdGroupAdPolicySummary(_message.Message):
    __slots__ = ("policy_topic_entries", "review_status", "approval_status")
    POLICY_TOPIC_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    policy_topic_entries: _containers.RepeatedCompositeFieldContainer[_policy_pb2.PolicyTopicEntry]
    review_status: _policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: _policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(self, policy_topic_entries: _Optional[_Iterable[_Union[_policy_pb2.PolicyTopicEntry, _Mapping]]] = ..., review_status: _Optional[_Union[_policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus, str]] = ..., approval_status: _Optional[_Union[_policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus, str]] = ...) -> None: ...
