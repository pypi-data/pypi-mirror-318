from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanNetworkEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanNetwork(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanNetworkEnum.KeywordPlanNetwork]
        UNKNOWN: _ClassVar[KeywordPlanNetworkEnum.KeywordPlanNetwork]
        GOOGLE_SEARCH: _ClassVar[KeywordPlanNetworkEnum.KeywordPlanNetwork]
        GOOGLE_SEARCH_AND_PARTNERS: _ClassVar[KeywordPlanNetworkEnum.KeywordPlanNetwork]
    UNSPECIFIED: KeywordPlanNetworkEnum.KeywordPlanNetwork
    UNKNOWN: KeywordPlanNetworkEnum.KeywordPlanNetwork
    GOOGLE_SEARCH: KeywordPlanNetworkEnum.KeywordPlanNetwork
    GOOGLE_SEARCH_AND_PARTNERS: KeywordPlanNetworkEnum.KeywordPlanNetwork

    def __init__(self) -> None:
        ...