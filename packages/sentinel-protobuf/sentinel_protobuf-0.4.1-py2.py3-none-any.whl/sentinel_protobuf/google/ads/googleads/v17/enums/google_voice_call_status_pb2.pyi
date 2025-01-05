from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class GoogleVoiceCallStatusEnum(_message.Message):
    __slots__ = ()

    class GoogleVoiceCallStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus]
        UNKNOWN: _ClassVar[GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus]
        MISSED: _ClassVar[GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus]
        RECEIVED: _ClassVar[GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus]
    UNSPECIFIED: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus
    UNKNOWN: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus
    MISSED: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus
    RECEIVED: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus

    def __init__(self) -> None:
        ...