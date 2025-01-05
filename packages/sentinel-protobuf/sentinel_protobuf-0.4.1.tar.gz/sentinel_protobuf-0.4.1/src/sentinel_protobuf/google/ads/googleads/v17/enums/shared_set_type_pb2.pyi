from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SharedSetTypeEnum(_message.Message):
    __slots__ = ()

    class SharedSetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SharedSetTypeEnum.SharedSetType]
        UNKNOWN: _ClassVar[SharedSetTypeEnum.SharedSetType]
        NEGATIVE_KEYWORDS: _ClassVar[SharedSetTypeEnum.SharedSetType]
        NEGATIVE_PLACEMENTS: _ClassVar[SharedSetTypeEnum.SharedSetType]
        ACCOUNT_LEVEL_NEGATIVE_KEYWORDS: _ClassVar[SharedSetTypeEnum.SharedSetType]
        BRANDS: _ClassVar[SharedSetTypeEnum.SharedSetType]
    UNSPECIFIED: SharedSetTypeEnum.SharedSetType
    UNKNOWN: SharedSetTypeEnum.SharedSetType
    NEGATIVE_KEYWORDS: SharedSetTypeEnum.SharedSetType
    NEGATIVE_PLACEMENTS: SharedSetTypeEnum.SharedSetType
    ACCOUNT_LEVEL_NEGATIVE_KEYWORDS: SharedSetTypeEnum.SharedSetType
    BRANDS: SharedSetTypeEnum.SharedSetType

    def __init__(self) -> None:
        ...