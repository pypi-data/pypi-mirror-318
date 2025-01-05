from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class InvoiceErrorEnum(_message.Message):
    __slots__ = ()

    class InvoiceError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InvoiceErrorEnum.InvoiceError]
        UNKNOWN: _ClassVar[InvoiceErrorEnum.InvoiceError]
        YEAR_MONTH_TOO_OLD: _ClassVar[InvoiceErrorEnum.InvoiceError]
        NOT_INVOICED_CUSTOMER: _ClassVar[InvoiceErrorEnum.InvoiceError]
        BILLING_SETUP_NOT_APPROVED: _ClassVar[InvoiceErrorEnum.InvoiceError]
        BILLING_SETUP_NOT_ON_MONTHLY_INVOICING: _ClassVar[InvoiceErrorEnum.InvoiceError]
        NON_SERVING_CUSTOMER: _ClassVar[InvoiceErrorEnum.InvoiceError]
    UNSPECIFIED: InvoiceErrorEnum.InvoiceError
    UNKNOWN: InvoiceErrorEnum.InvoiceError
    YEAR_MONTH_TOO_OLD: InvoiceErrorEnum.InvoiceError
    NOT_INVOICED_CUSTOMER: InvoiceErrorEnum.InvoiceError
    BILLING_SETUP_NOT_APPROVED: InvoiceErrorEnum.InvoiceError
    BILLING_SETUP_NOT_ON_MONTHLY_INVOICING: InvoiceErrorEnum.InvoiceError
    NON_SERVING_CUSTOMER: InvoiceErrorEnum.InvoiceError

    def __init__(self) -> None:
        ...