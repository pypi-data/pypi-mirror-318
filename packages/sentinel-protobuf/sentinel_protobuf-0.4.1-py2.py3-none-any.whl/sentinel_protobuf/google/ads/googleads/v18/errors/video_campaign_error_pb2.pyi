from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class VideoCampaignErrorEnum(_message.Message):
    __slots__ = ()

    class VideoCampaignError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[VideoCampaignErrorEnum.VideoCampaignError]
        UNKNOWN: _ClassVar[VideoCampaignErrorEnum.VideoCampaignError]
        MUTATE_REQUIRES_RESERVATION: _ClassVar[VideoCampaignErrorEnum.VideoCampaignError]
    UNSPECIFIED: VideoCampaignErrorEnum.VideoCampaignError
    UNKNOWN: VideoCampaignErrorEnum.VideoCampaignError
    MUTATE_REQUIRES_RESERVATION: VideoCampaignErrorEnum.VideoCampaignError

    def __init__(self) -> None:
        ...