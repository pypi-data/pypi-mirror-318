from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SkAdNetworkAttributionCreditEnum(_message.Message):
    __slots__ = ()

    class SkAdNetworkAttributionCredit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit]
        UNKNOWN: _ClassVar[SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit]
        UNAVAILABLE: _ClassVar[SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit]
        WON: _ClassVar[SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit]
        CONTRIBUTED: _ClassVar[SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit]
    UNSPECIFIED: SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    UNKNOWN: SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    UNAVAILABLE: SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    WON: SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    CONTRIBUTED: SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit

    def __init__(self) -> None:
        ...