from google.ads.googleads.v16.common import policy_pb2 as _policy_pb2
from google.ads.googleads.v16.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.googleads.v16.enums import asset_performance_label_pb2 as _asset_performance_label_pb2
from google.ads.googleads.v16.enums import asset_source_pb2 as _asset_source_pb2
from google.ads.googleads.v16.enums import policy_approval_status_pb2 as _policy_approval_status_pb2
from google.ads.googleads.v16.enums import policy_review_status_pb2 as _policy_review_status_pb2
from google.ads.googleads.v16.enums import served_asset_field_type_pb2 as _served_asset_field_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAdAssetView(_message.Message):
    __slots__ = ("resource_name", "ad_group_ad", "asset", "field_type", "enabled", "policy_summary", "performance_label", "pinned_field", "source")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_AD_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    POLICY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_LABEL_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    ad_group_ad: str
    asset: str
    field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType
    enabled: bool
    policy_summary: AdGroupAdAssetPolicySummary
    performance_label: _asset_performance_label_pb2.AssetPerformanceLabelEnum.AssetPerformanceLabel
    pinned_field: _served_asset_field_type_pb2.ServedAssetFieldTypeEnum.ServedAssetFieldType
    source: _asset_source_pb2.AssetSourceEnum.AssetSource
    def __init__(self, resource_name: _Optional[str] = ..., ad_group_ad: _Optional[str] = ..., asset: _Optional[str] = ..., field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]] = ..., enabled: bool = ..., policy_summary: _Optional[_Union[AdGroupAdAssetPolicySummary, _Mapping]] = ..., performance_label: _Optional[_Union[_asset_performance_label_pb2.AssetPerformanceLabelEnum.AssetPerformanceLabel, str]] = ..., pinned_field: _Optional[_Union[_served_asset_field_type_pb2.ServedAssetFieldTypeEnum.ServedAssetFieldType, str]] = ..., source: _Optional[_Union[_asset_source_pb2.AssetSourceEnum.AssetSource, str]] = ...) -> None: ...

class AdGroupAdAssetPolicySummary(_message.Message):
    __slots__ = ("policy_topic_entries", "review_status", "approval_status")
    POLICY_TOPIC_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    policy_topic_entries: _containers.RepeatedCompositeFieldContainer[_policy_pb2.PolicyTopicEntry]
    review_status: _policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: _policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(self, policy_topic_entries: _Optional[_Iterable[_Union[_policy_pb2.PolicyTopicEntry, _Mapping]]] = ..., review_status: _Optional[_Union[_policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus, str]] = ..., approval_status: _Optional[_Union[_policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus, str]] = ...) -> None: ...
