from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyApprovalStatusEnum(_message.Message):
    __slots__ = ()

    class PolicyApprovalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PolicyApprovalStatusEnum.PolicyApprovalStatus]
        UNKNOWN: _ClassVar[PolicyApprovalStatusEnum.PolicyApprovalStatus]
        DISAPPROVED: _ClassVar[PolicyApprovalStatusEnum.PolicyApprovalStatus]
        APPROVED_LIMITED: _ClassVar[PolicyApprovalStatusEnum.PolicyApprovalStatus]
        APPROVED: _ClassVar[PolicyApprovalStatusEnum.PolicyApprovalStatus]
        AREA_OF_INTEREST_ONLY: _ClassVar[PolicyApprovalStatusEnum.PolicyApprovalStatus]
    UNSPECIFIED: PolicyApprovalStatusEnum.PolicyApprovalStatus
    UNKNOWN: PolicyApprovalStatusEnum.PolicyApprovalStatus
    DISAPPROVED: PolicyApprovalStatusEnum.PolicyApprovalStatus
    APPROVED_LIMITED: PolicyApprovalStatusEnum.PolicyApprovalStatus
    APPROVED: PolicyApprovalStatusEnum.PolicyApprovalStatus
    AREA_OF_INTEREST_ONLY: PolicyApprovalStatusEnum.PolicyApprovalStatus

    def __init__(self) -> None:
        ...