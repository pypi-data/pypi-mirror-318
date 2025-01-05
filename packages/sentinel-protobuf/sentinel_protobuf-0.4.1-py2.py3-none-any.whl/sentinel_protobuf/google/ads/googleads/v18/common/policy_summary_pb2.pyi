from google.ads.googleads.v18.common import policy_pb2 as _policy_pb2
from google.ads.googleads.v18.enums import policy_approval_status_pb2 as _policy_approval_status_pb2
from google.ads.googleads.v18.enums import policy_review_status_pb2 as _policy_review_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicySummary(_message.Message):
    __slots__ = ("policy_topic_entries", "review_status", "approval_status")
    POLICY_TOPIC_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    policy_topic_entries: _containers.RepeatedCompositeFieldContainer[_policy_pb2.PolicyTopicEntry]
    review_status: _policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: _policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(self, policy_topic_entries: _Optional[_Iterable[_Union[_policy_pb2.PolicyTopicEntry, _Mapping]]] = ..., review_status: _Optional[_Union[_policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus, str]] = ..., approval_status: _Optional[_Union[_policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus, str]] = ...) -> None: ...
