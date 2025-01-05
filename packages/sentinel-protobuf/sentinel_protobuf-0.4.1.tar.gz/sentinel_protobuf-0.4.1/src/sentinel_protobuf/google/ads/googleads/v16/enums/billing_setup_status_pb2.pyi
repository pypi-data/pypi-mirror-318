from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BillingSetupStatusEnum(_message.Message):
    __slots__ = ()

    class BillingSetupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BillingSetupStatusEnum.BillingSetupStatus]
        UNKNOWN: _ClassVar[BillingSetupStatusEnum.BillingSetupStatus]
        PENDING: _ClassVar[BillingSetupStatusEnum.BillingSetupStatus]
        APPROVED_HELD: _ClassVar[BillingSetupStatusEnum.BillingSetupStatus]
        APPROVED: _ClassVar[BillingSetupStatusEnum.BillingSetupStatus]
        CANCELLED: _ClassVar[BillingSetupStatusEnum.BillingSetupStatus]
    UNSPECIFIED: BillingSetupStatusEnum.BillingSetupStatus
    UNKNOWN: BillingSetupStatusEnum.BillingSetupStatus
    PENDING: BillingSetupStatusEnum.BillingSetupStatus
    APPROVED_HELD: BillingSetupStatusEnum.BillingSetupStatus
    APPROVED: BillingSetupStatusEnum.BillingSetupStatus
    CANCELLED: BillingSetupStatusEnum.BillingSetupStatus

    def __init__(self) -> None:
        ...