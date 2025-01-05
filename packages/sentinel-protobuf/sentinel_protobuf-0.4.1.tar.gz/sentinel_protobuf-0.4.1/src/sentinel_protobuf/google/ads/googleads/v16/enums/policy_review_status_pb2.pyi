from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyReviewStatusEnum(_message.Message):
    __slots__ = ()

    class PolicyReviewStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PolicyReviewStatusEnum.PolicyReviewStatus]
        UNKNOWN: _ClassVar[PolicyReviewStatusEnum.PolicyReviewStatus]
        REVIEW_IN_PROGRESS: _ClassVar[PolicyReviewStatusEnum.PolicyReviewStatus]
        REVIEWED: _ClassVar[PolicyReviewStatusEnum.PolicyReviewStatus]
        UNDER_APPEAL: _ClassVar[PolicyReviewStatusEnum.PolicyReviewStatus]
        ELIGIBLE_MAY_SERVE: _ClassVar[PolicyReviewStatusEnum.PolicyReviewStatus]
    UNSPECIFIED: PolicyReviewStatusEnum.PolicyReviewStatus
    UNKNOWN: PolicyReviewStatusEnum.PolicyReviewStatus
    REVIEW_IN_PROGRESS: PolicyReviewStatusEnum.PolicyReviewStatus
    REVIEWED: PolicyReviewStatusEnum.PolicyReviewStatus
    UNDER_APPEAL: PolicyReviewStatusEnum.PolicyReviewStatus
    ELIGIBLE_MAY_SERVE: PolicyReviewStatusEnum.PolicyReviewStatus

    def __init__(self) -> None:
        ...