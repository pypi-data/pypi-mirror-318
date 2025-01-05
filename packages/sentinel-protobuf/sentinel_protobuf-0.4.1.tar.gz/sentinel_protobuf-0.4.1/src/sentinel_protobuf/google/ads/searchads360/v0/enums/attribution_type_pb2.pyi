from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AttributionTypeEnum(_message.Message):
    __slots__ = ()

    class AttributionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AttributionTypeEnum.AttributionType]
        UNKNOWN: _ClassVar[AttributionTypeEnum.AttributionType]
        VISIT: _ClassVar[AttributionTypeEnum.AttributionType]
        CRITERION_AD: _ClassVar[AttributionTypeEnum.AttributionType]
    UNSPECIFIED: AttributionTypeEnum.AttributionType
    UNKNOWN: AttributionTypeEnum.AttributionType
    VISIT: AttributionTypeEnum.AttributionType
    CRITERION_AD: AttributionTypeEnum.AttributionType

    def __init__(self) -> None:
        ...