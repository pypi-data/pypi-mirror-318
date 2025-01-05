from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MatchingFunctionContextTypeEnum(_message.Message):
    __slots__ = ()

    class MatchingFunctionContextType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MatchingFunctionContextTypeEnum.MatchingFunctionContextType]
        UNKNOWN: _ClassVar[MatchingFunctionContextTypeEnum.MatchingFunctionContextType]
        FEED_ITEM_ID: _ClassVar[MatchingFunctionContextTypeEnum.MatchingFunctionContextType]
        DEVICE_NAME: _ClassVar[MatchingFunctionContextTypeEnum.MatchingFunctionContextType]
        FEED_ITEM_SET_ID: _ClassVar[MatchingFunctionContextTypeEnum.MatchingFunctionContextType]
    UNSPECIFIED: MatchingFunctionContextTypeEnum.MatchingFunctionContextType
    UNKNOWN: MatchingFunctionContextTypeEnum.MatchingFunctionContextType
    FEED_ITEM_ID: MatchingFunctionContextTypeEnum.MatchingFunctionContextType
    DEVICE_NAME: MatchingFunctionContextTypeEnum.MatchingFunctionContextType
    FEED_ITEM_SET_ID: MatchingFunctionContextTypeEnum.MatchingFunctionContextType

    def __init__(self) -> None:
        ...