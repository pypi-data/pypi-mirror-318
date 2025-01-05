from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignSharedSetErrorEnum(_message.Message):
    __slots__ = ()

    class CampaignSharedSetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignSharedSetErrorEnum.CampaignSharedSetError]
        UNKNOWN: _ClassVar[CampaignSharedSetErrorEnum.CampaignSharedSetError]
        SHARED_SET_ACCESS_DENIED: _ClassVar[CampaignSharedSetErrorEnum.CampaignSharedSetError]
    UNSPECIFIED: CampaignSharedSetErrorEnum.CampaignSharedSetError
    UNKNOWN: CampaignSharedSetErrorEnum.CampaignSharedSetError
    SHARED_SET_ACCESS_DENIED: CampaignSharedSetErrorEnum.CampaignSharedSetError

    def __init__(self) -> None:
        ...