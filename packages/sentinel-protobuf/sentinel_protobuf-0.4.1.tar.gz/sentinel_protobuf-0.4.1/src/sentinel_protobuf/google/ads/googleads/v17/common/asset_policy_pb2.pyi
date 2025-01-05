from google.ads.googleads.v17.common import policy_pb2 as _policy_pb2
from google.ads.googleads.v17.enums import asset_link_primary_status_pb2 as _asset_link_primary_status_pb2
from google.ads.googleads.v17.enums import asset_link_primary_status_reason_pb2 as _asset_link_primary_status_reason_pb2
from google.ads.googleads.v17.enums import asset_offline_evaluation_error_reasons_pb2 as _asset_offline_evaluation_error_reasons_pb2
from google.ads.googleads.v17.enums import policy_approval_status_pb2 as _policy_approval_status_pb2
from google.ads.googleads.v17.enums import policy_review_status_pb2 as _policy_review_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdAssetPolicySummary(_message.Message):
    __slots__ = ("policy_topic_entries", "review_status", "approval_status")
    POLICY_TOPIC_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    policy_topic_entries: _containers.RepeatedCompositeFieldContainer[_policy_pb2.PolicyTopicEntry]
    review_status: _policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: _policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(self, policy_topic_entries: _Optional[_Iterable[_Union[_policy_pb2.PolicyTopicEntry, _Mapping]]] = ..., review_status: _Optional[_Union[_policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus, str]] = ..., approval_status: _Optional[_Union[_policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus, str]] = ...) -> None: ...

class AssetLinkPrimaryStatusDetails(_message.Message):
    __slots__ = ("reason", "status", "asset_disapproved")
    REASON_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSET_DISAPPROVED_FIELD_NUMBER: _ClassVar[int]
    reason: _asset_link_primary_status_reason_pb2.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    status: _asset_link_primary_status_pb2.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    asset_disapproved: AssetDisapproved
    def __init__(self, reason: _Optional[_Union[_asset_link_primary_status_reason_pb2.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason, str]] = ..., status: _Optional[_Union[_asset_link_primary_status_pb2.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus, str]] = ..., asset_disapproved: _Optional[_Union[AssetDisapproved, _Mapping]] = ...) -> None: ...

class AssetDisapproved(_message.Message):
    __slots__ = ("offline_evaluation_error_reasons",)
    OFFLINE_EVALUATION_ERROR_REASONS_FIELD_NUMBER: _ClassVar[int]
    offline_evaluation_error_reasons: _containers.RepeatedScalarFieldContainer[_asset_offline_evaluation_error_reasons_pb2.AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
    def __init__(self, offline_evaluation_error_reasons: _Optional[_Iterable[_Union[_asset_offline_evaluation_error_reasons_pb2.AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons, str]]] = ...) -> None: ...
