from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class YoutubeVideoRegistrationErrorEnum(_message.Message):
    __slots__ = ()

    class YoutubeVideoRegistrationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError]
        UNKNOWN: _ClassVar[YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError]
        VIDEO_NOT_FOUND: _ClassVar[YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError]
        VIDEO_NOT_ACCESSIBLE: _ClassVar[YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError]
        VIDEO_NOT_ELIGIBLE: _ClassVar[YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError]
    UNSPECIFIED: YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError
    UNKNOWN: YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError
    VIDEO_NOT_FOUND: YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError
    VIDEO_NOT_ACCESSIBLE: YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError
    VIDEO_NOT_ELIGIBLE: YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError

    def __init__(self) -> None:
        ...