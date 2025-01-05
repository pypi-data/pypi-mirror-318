from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class InvoiceTypeEnum(_message.Message):
    __slots__ = ()

    class InvoiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InvoiceTypeEnum.InvoiceType]
        UNKNOWN: _ClassVar[InvoiceTypeEnum.InvoiceType]
        CREDIT_MEMO: _ClassVar[InvoiceTypeEnum.InvoiceType]
        INVOICE: _ClassVar[InvoiceTypeEnum.InvoiceType]
    UNSPECIFIED: InvoiceTypeEnum.InvoiceType
    UNKNOWN: InvoiceTypeEnum.InvoiceType
    CREDIT_MEMO: InvoiceTypeEnum.InvoiceType
    INVOICE: InvoiceTypeEnum.InvoiceType

    def __init__(self) -> None:
        ...