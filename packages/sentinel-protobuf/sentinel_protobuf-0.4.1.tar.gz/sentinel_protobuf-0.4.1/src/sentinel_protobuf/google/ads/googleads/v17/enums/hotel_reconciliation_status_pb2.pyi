from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class HotelReconciliationStatusEnum(_message.Message):
    __slots__ = ()

    class HotelReconciliationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[HotelReconciliationStatusEnum.HotelReconciliationStatus]
        UNKNOWN: _ClassVar[HotelReconciliationStatusEnum.HotelReconciliationStatus]
        RESERVATION_ENABLED: _ClassVar[HotelReconciliationStatusEnum.HotelReconciliationStatus]
        RECONCILIATION_NEEDED: _ClassVar[HotelReconciliationStatusEnum.HotelReconciliationStatus]
        RECONCILED: _ClassVar[HotelReconciliationStatusEnum.HotelReconciliationStatus]
        CANCELED: _ClassVar[HotelReconciliationStatusEnum.HotelReconciliationStatus]
    UNSPECIFIED: HotelReconciliationStatusEnum.HotelReconciliationStatus
    UNKNOWN: HotelReconciliationStatusEnum.HotelReconciliationStatus
    RESERVATION_ENABLED: HotelReconciliationStatusEnum.HotelReconciliationStatus
    RECONCILIATION_NEEDED: HotelReconciliationStatusEnum.HotelReconciliationStatus
    RECONCILED: HotelReconciliationStatusEnum.HotelReconciliationStatus
    CANCELED: HotelReconciliationStatusEnum.HotelReconciliationStatus

    def __init__(self) -> None:
        ...