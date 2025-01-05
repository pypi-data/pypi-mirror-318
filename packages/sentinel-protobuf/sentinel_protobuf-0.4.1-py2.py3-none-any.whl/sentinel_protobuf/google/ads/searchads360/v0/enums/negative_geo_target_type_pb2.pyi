from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class NegativeGeoTargetTypeEnum(_message.Message):
    __slots__ = ()

    class NegativeGeoTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[NegativeGeoTargetTypeEnum.NegativeGeoTargetType]
        UNKNOWN: _ClassVar[NegativeGeoTargetTypeEnum.NegativeGeoTargetType]
        PRESENCE_OR_INTEREST: _ClassVar[NegativeGeoTargetTypeEnum.NegativeGeoTargetType]
        PRESENCE: _ClassVar[NegativeGeoTargetTypeEnum.NegativeGeoTargetType]
    UNSPECIFIED: NegativeGeoTargetTypeEnum.NegativeGeoTargetType
    UNKNOWN: NegativeGeoTargetTypeEnum.NegativeGeoTargetType
    PRESENCE_OR_INTEREST: NegativeGeoTargetTypeEnum.NegativeGeoTargetType
    PRESENCE: NegativeGeoTargetTypeEnum.NegativeGeoTargetType

    def __init__(self) -> None:
        ...