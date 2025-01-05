from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordMatchTypeEnum(_message.Message):
    __slots__ = ()

    class KeywordMatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordMatchTypeEnum.KeywordMatchType]
        UNKNOWN: _ClassVar[KeywordMatchTypeEnum.KeywordMatchType]
        EXACT: _ClassVar[KeywordMatchTypeEnum.KeywordMatchType]
        PHRASE: _ClassVar[KeywordMatchTypeEnum.KeywordMatchType]
        BROAD: _ClassVar[KeywordMatchTypeEnum.KeywordMatchType]
    UNSPECIFIED: KeywordMatchTypeEnum.KeywordMatchType
    UNKNOWN: KeywordMatchTypeEnum.KeywordMatchType
    EXACT: KeywordMatchTypeEnum.KeywordMatchType
    PHRASE: KeywordMatchTypeEnum.KeywordMatchType
    BROAD: KeywordMatchTypeEnum.KeywordMatchType

    def __init__(self) -> None:
        ...