from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PaymentsAccountErrorEnum(_message.Message):
    __slots__ = ()

    class PaymentsAccountError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PaymentsAccountErrorEnum.PaymentsAccountError]
        UNKNOWN: _ClassVar[PaymentsAccountErrorEnum.PaymentsAccountError]
        NOT_SUPPORTED_FOR_MANAGER_CUSTOMER: _ClassVar[PaymentsAccountErrorEnum.PaymentsAccountError]
    UNSPECIFIED: PaymentsAccountErrorEnum.PaymentsAccountError
    UNKNOWN: PaymentsAccountErrorEnum.PaymentsAccountError
    NOT_SUPPORTED_FOR_MANAGER_CUSTOMER: PaymentsAccountErrorEnum.PaymentsAccountError

    def __init__(self) -> None:
        ...