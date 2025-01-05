from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCriterionApprovalStatusEnum(_message.Message):
    __slots__ = ()

    class AdGroupCriterionApprovalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus]
        UNKNOWN: _ClassVar[AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus]
        APPROVED: _ClassVar[AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus]
        DISAPPROVED: _ClassVar[AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus]
        PENDING_REVIEW: _ClassVar[AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus]
        UNDER_REVIEW: _ClassVar[AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus]
    UNSPECIFIED: AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    UNKNOWN: AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    APPROVED: AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    DISAPPROVED: AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    PENDING_REVIEW: AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    UNDER_REVIEW: AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus

    def __init__(self) -> None:
        ...