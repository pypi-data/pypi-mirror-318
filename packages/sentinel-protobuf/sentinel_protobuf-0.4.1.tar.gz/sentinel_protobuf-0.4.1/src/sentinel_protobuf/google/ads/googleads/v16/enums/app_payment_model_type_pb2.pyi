from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AppPaymentModelTypeEnum(_message.Message):
    __slots__ = ()

    class AppPaymentModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AppPaymentModelTypeEnum.AppPaymentModelType]
        UNKNOWN: _ClassVar[AppPaymentModelTypeEnum.AppPaymentModelType]
        PAID: _ClassVar[AppPaymentModelTypeEnum.AppPaymentModelType]
    UNSPECIFIED: AppPaymentModelTypeEnum.AppPaymentModelType
    UNKNOWN: AppPaymentModelTypeEnum.AppPaymentModelType
    PAID: AppPaymentModelTypeEnum.AppPaymentModelType

    def __init__(self) -> None:
        ...