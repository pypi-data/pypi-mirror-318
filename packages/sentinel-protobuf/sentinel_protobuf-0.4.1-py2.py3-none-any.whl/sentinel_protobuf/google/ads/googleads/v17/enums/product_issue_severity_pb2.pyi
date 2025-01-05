from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProductIssueSeverityEnum(_message.Message):
    __slots__ = ()

    class ProductIssueSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProductIssueSeverityEnum.ProductIssueSeverity]
        UNKNOWN: _ClassVar[ProductIssueSeverityEnum.ProductIssueSeverity]
        WARNING: _ClassVar[ProductIssueSeverityEnum.ProductIssueSeverity]
        ERROR: _ClassVar[ProductIssueSeverityEnum.ProductIssueSeverity]
    UNSPECIFIED: ProductIssueSeverityEnum.ProductIssueSeverity
    UNKNOWN: ProductIssueSeverityEnum.ProductIssueSeverity
    WARNING: ProductIssueSeverityEnum.ProductIssueSeverity
    ERROR: ProductIssueSeverityEnum.ProductIssueSeverity

    def __init__(self) -> None:
        ...