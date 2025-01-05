from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OfflineUserDataJobFailureReasonEnum(_message.Message):
    __slots__ = ()

    class OfflineUserDataJobFailureReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason]
        UNKNOWN: _ClassVar[OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason]
        INSUFFICIENT_MATCHED_TRANSACTIONS: _ClassVar[OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason]
        INSUFFICIENT_TRANSACTIONS: _ClassVar[OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason]
        HIGH_AVERAGE_TRANSACTION_VALUE: _ClassVar[OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason]
        LOW_AVERAGE_TRANSACTION_VALUE: _ClassVar[OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason]
        NEWLY_OBSERVED_CURRENCY_CODE: _ClassVar[OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason]
    UNSPECIFIED: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    UNKNOWN: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    INSUFFICIENT_MATCHED_TRANSACTIONS: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    INSUFFICIENT_TRANSACTIONS: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    HIGH_AVERAGE_TRANSACTION_VALUE: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    LOW_AVERAGE_TRANSACTION_VALUE: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    NEWLY_OBSERVED_CURRENCY_CODE: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason

    def __init__(self) -> None:
        ...