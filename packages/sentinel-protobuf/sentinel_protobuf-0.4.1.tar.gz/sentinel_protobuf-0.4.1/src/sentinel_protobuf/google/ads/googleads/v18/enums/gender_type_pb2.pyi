from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class GenderTypeEnum(_message.Message):
    __slots__ = ()

    class GenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[GenderTypeEnum.GenderType]
        UNKNOWN: _ClassVar[GenderTypeEnum.GenderType]
        MALE: _ClassVar[GenderTypeEnum.GenderType]
        FEMALE: _ClassVar[GenderTypeEnum.GenderType]
        UNDETERMINED: _ClassVar[GenderTypeEnum.GenderType]
    UNSPECIFIED: GenderTypeEnum.GenderType
    UNKNOWN: GenderTypeEnum.GenderType
    MALE: GenderTypeEnum.GenderType
    FEMALE: GenderTypeEnum.GenderType
    UNDETERMINED: GenderTypeEnum.GenderType

    def __init__(self) -> None:
        ...