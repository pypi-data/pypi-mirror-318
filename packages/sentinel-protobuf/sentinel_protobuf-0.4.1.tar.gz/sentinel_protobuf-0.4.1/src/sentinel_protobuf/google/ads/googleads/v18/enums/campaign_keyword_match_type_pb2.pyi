from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignKeywordMatchTypeEnum(_message.Message):
    __slots__ = ()

    class CampaignKeywordMatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType]
        UNKNOWN: _ClassVar[CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType]
        BROAD: _ClassVar[CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType]
    UNSPECIFIED: CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType
    UNKNOWN: CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType
    BROAD: CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType

    def __init__(self) -> None:
        ...