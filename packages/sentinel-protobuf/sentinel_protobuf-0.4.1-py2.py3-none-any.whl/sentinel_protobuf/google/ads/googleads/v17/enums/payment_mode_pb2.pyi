from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PaymentModeEnum(_message.Message):
    __slots__ = ()

    class PaymentMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PaymentModeEnum.PaymentMode]
        UNKNOWN: _ClassVar[PaymentModeEnum.PaymentMode]
        CLICKS: _ClassVar[PaymentModeEnum.PaymentMode]
        CONVERSION_VALUE: _ClassVar[PaymentModeEnum.PaymentMode]
        CONVERSIONS: _ClassVar[PaymentModeEnum.PaymentMode]
        GUEST_STAY: _ClassVar[PaymentModeEnum.PaymentMode]
    UNSPECIFIED: PaymentModeEnum.PaymentMode
    UNKNOWN: PaymentModeEnum.PaymentMode
    CLICKS: PaymentModeEnum.PaymentMode
    CONVERSION_VALUE: PaymentModeEnum.PaymentMode
    CONVERSIONS: PaymentModeEnum.PaymentMode
    GUEST_STAY: PaymentModeEnum.PaymentMode

    def __init__(self) -> None:
        ...