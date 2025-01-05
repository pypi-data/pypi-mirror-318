from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupBidModifierErrorEnum(_message.Message):
    __slots__ = ()

    class AdGroupBidModifierError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupBidModifierErrorEnum.AdGroupBidModifierError]
        UNKNOWN: _ClassVar[AdGroupBidModifierErrorEnum.AdGroupBidModifierError]
        CRITERION_ID_NOT_SUPPORTED: _ClassVar[AdGroupBidModifierErrorEnum.AdGroupBidModifierError]
        CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER: _ClassVar[AdGroupBidModifierErrorEnum.AdGroupBidModifierError]
    UNSPECIFIED: AdGroupBidModifierErrorEnum.AdGroupBidModifierError
    UNKNOWN: AdGroupBidModifierErrorEnum.AdGroupBidModifierError
    CRITERION_ID_NOT_SUPPORTED: AdGroupBidModifierErrorEnum.AdGroupBidModifierError
    CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER: AdGroupBidModifierErrorEnum.AdGroupBidModifierError

    def __init__(self) -> None:
        ...