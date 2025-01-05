from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemQualityApprovalStatusEnum(_message.Message):
    __slots__ = ()

    class FeedItemQualityApprovalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus]
        UNKNOWN: _ClassVar[FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus]
        APPROVED: _ClassVar[FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus]
        DISAPPROVED: _ClassVar[FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus]
    UNSPECIFIED: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    UNKNOWN: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    APPROVED: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    DISAPPROVED: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus

    def __init__(self) -> None:
        ...