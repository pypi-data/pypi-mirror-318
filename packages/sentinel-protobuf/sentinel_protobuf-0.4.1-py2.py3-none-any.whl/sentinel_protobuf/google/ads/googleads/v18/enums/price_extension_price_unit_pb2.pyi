from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PriceExtensionPriceUnitEnum(_message.Message):
    __slots__ = ()

    class PriceExtensionPriceUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit]
        UNKNOWN: _ClassVar[PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit]
        PER_HOUR: _ClassVar[PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit]
        PER_DAY: _ClassVar[PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit]
        PER_WEEK: _ClassVar[PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit]
        PER_MONTH: _ClassVar[PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit]
        PER_YEAR: _ClassVar[PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit]
        PER_NIGHT: _ClassVar[PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit]
    UNSPECIFIED: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    UNKNOWN: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    PER_HOUR: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    PER_DAY: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    PER_WEEK: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    PER_MONTH: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    PER_YEAR: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    PER_NIGHT: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit

    def __init__(self) -> None:
        ...