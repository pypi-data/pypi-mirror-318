from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BiddingSourceEnum(_message.Message):
    __slots__ = ()

    class BiddingSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BiddingSourceEnum.BiddingSource]
        UNKNOWN: _ClassVar[BiddingSourceEnum.BiddingSource]
        CAMPAIGN_BIDDING_STRATEGY: _ClassVar[BiddingSourceEnum.BiddingSource]
        AD_GROUP: _ClassVar[BiddingSourceEnum.BiddingSource]
        AD_GROUP_CRITERION: _ClassVar[BiddingSourceEnum.BiddingSource]
    UNSPECIFIED: BiddingSourceEnum.BiddingSource
    UNKNOWN: BiddingSourceEnum.BiddingSource
    CAMPAIGN_BIDDING_STRATEGY: BiddingSourceEnum.BiddingSource
    AD_GROUP: BiddingSourceEnum.BiddingSource
    AD_GROUP_CRITERION: BiddingSourceEnum.BiddingSource

    def __init__(self) -> None:
        ...