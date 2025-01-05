from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignCustomizerErrorEnum(_message.Message):
    __slots__ = ()

    class CampaignCustomizerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignCustomizerErrorEnum.CampaignCustomizerError]
        UNKNOWN: _ClassVar[CampaignCustomizerErrorEnum.CampaignCustomizerError]
    UNSPECIFIED: CampaignCustomizerErrorEnum.CampaignCustomizerError
    UNKNOWN: CampaignCustomizerErrorEnum.CampaignCustomizerError

    def __init__(self) -> None:
        ...