from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MerchantCenterErrorEnum(_message.Message):
    __slots__ = ()

    class MerchantCenterError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MerchantCenterErrorEnum.MerchantCenterError]
        UNKNOWN: _ClassVar[MerchantCenterErrorEnum.MerchantCenterError]
        MERCHANT_ID_CANNOT_BE_ACCESSED: _ClassVar[MerchantCenterErrorEnum.MerchantCenterError]
        CUSTOMER_NOT_ALLOWED_FOR_SHOPPING_PERFORMANCE_MAX: _ClassVar[MerchantCenterErrorEnum.MerchantCenterError]
    UNSPECIFIED: MerchantCenterErrorEnum.MerchantCenterError
    UNKNOWN: MerchantCenterErrorEnum.MerchantCenterError
    MERCHANT_ID_CANNOT_BE_ACCESSED: MerchantCenterErrorEnum.MerchantCenterError
    CUSTOMER_NOT_ALLOWED_FOR_SHOPPING_PERFORMANCE_MAX: MerchantCenterErrorEnum.MerchantCenterError

    def __init__(self) -> None:
        ...