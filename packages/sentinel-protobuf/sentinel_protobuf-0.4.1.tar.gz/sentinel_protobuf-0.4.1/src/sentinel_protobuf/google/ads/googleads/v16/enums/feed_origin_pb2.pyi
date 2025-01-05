from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedOriginEnum(_message.Message):
    __slots__ = ()

    class FeedOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedOriginEnum.FeedOrigin]
        UNKNOWN: _ClassVar[FeedOriginEnum.FeedOrigin]
        USER: _ClassVar[FeedOriginEnum.FeedOrigin]
        GOOGLE: _ClassVar[FeedOriginEnum.FeedOrigin]
    UNSPECIFIED: FeedOriginEnum.FeedOrigin
    UNKNOWN: FeedOriginEnum.FeedOrigin
    USER: FeedOriginEnum.FeedOrigin
    GOOGLE: FeedOriginEnum.FeedOrigin

    def __init__(self) -> None:
        ...