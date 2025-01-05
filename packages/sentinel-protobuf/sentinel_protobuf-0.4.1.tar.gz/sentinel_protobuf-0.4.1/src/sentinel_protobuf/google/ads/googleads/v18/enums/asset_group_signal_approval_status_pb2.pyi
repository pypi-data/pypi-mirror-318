from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupSignalApprovalStatusEnum(_message.Message):
    __slots__ = ()

    class AssetGroupSignalApprovalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus]
        UNKNOWN: _ClassVar[AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus]
        APPROVED: _ClassVar[AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus]
        LIMITED: _ClassVar[AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus]
        DISAPPROVED: _ClassVar[AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus]
        UNDER_REVIEW: _ClassVar[AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus]
    UNSPECIFIED: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    UNKNOWN: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    APPROVED: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    LIMITED: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    DISAPPROVED: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    UNDER_REVIEW: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus

    def __init__(self) -> None:
        ...