from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SearchTermMatchTypeEnum(_message.Message):
    __slots__ = ()

    class SearchTermMatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SearchTermMatchTypeEnum.SearchTermMatchType]
        UNKNOWN: _ClassVar[SearchTermMatchTypeEnum.SearchTermMatchType]
        BROAD: _ClassVar[SearchTermMatchTypeEnum.SearchTermMatchType]
        EXACT: _ClassVar[SearchTermMatchTypeEnum.SearchTermMatchType]
        PHRASE: _ClassVar[SearchTermMatchTypeEnum.SearchTermMatchType]
        NEAR_EXACT: _ClassVar[SearchTermMatchTypeEnum.SearchTermMatchType]
        NEAR_PHRASE: _ClassVar[SearchTermMatchTypeEnum.SearchTermMatchType]
    UNSPECIFIED: SearchTermMatchTypeEnum.SearchTermMatchType
    UNKNOWN: SearchTermMatchTypeEnum.SearchTermMatchType
    BROAD: SearchTermMatchTypeEnum.SearchTermMatchType
    EXACT: SearchTermMatchTypeEnum.SearchTermMatchType
    PHRASE: SearchTermMatchTypeEnum.SearchTermMatchType
    NEAR_EXACT: SearchTermMatchTypeEnum.SearchTermMatchType
    NEAR_PHRASE: SearchTermMatchTypeEnum.SearchTermMatchType

    def __init__(self) -> None:
        ...