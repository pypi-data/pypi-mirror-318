from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedAttributeReferenceErrorEnum(_message.Message):
    __slots__ = ()

    class FeedAttributeReferenceError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError]
        UNKNOWN: _ClassVar[FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError]
        CANNOT_REFERENCE_REMOVED_FEED: _ClassVar[FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError]
        INVALID_FEED_NAME: _ClassVar[FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError]
        INVALID_FEED_ATTRIBUTE_NAME: _ClassVar[FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError]
    UNSPECIFIED: FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError
    UNKNOWN: FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError
    CANNOT_REFERENCE_REMOVED_FEED: FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError
    INVALID_FEED_NAME: FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError
    INVALID_FEED_ATTRIBUTE_NAME: FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError

    def __init__(self) -> None:
        ...