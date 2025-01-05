from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ChangeClientTypeEnum(_message.Message):
    __slots__ = ()

    class ChangeClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        UNKNOWN: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        GOOGLE_ADS_WEB_CLIENT: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        GOOGLE_ADS_AUTOMATED_RULE: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        GOOGLE_ADS_SCRIPTS: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        GOOGLE_ADS_BULK_UPLOAD: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        GOOGLE_ADS_API: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        GOOGLE_ADS_EDITOR: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        GOOGLE_ADS_MOBILE_APP: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        GOOGLE_ADS_RECOMMENDATIONS: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        SEARCH_ADS_360_SYNC: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        SEARCH_ADS_360_POST: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        INTERNAL_TOOL: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        OTHER: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
        GOOGLE_ADS_RECOMMENDATIONS_SUBSCRIPTION: _ClassVar[ChangeClientTypeEnum.ChangeClientType]
    UNSPECIFIED: ChangeClientTypeEnum.ChangeClientType
    UNKNOWN: ChangeClientTypeEnum.ChangeClientType
    GOOGLE_ADS_WEB_CLIENT: ChangeClientTypeEnum.ChangeClientType
    GOOGLE_ADS_AUTOMATED_RULE: ChangeClientTypeEnum.ChangeClientType
    GOOGLE_ADS_SCRIPTS: ChangeClientTypeEnum.ChangeClientType
    GOOGLE_ADS_BULK_UPLOAD: ChangeClientTypeEnum.ChangeClientType
    GOOGLE_ADS_API: ChangeClientTypeEnum.ChangeClientType
    GOOGLE_ADS_EDITOR: ChangeClientTypeEnum.ChangeClientType
    GOOGLE_ADS_MOBILE_APP: ChangeClientTypeEnum.ChangeClientType
    GOOGLE_ADS_RECOMMENDATIONS: ChangeClientTypeEnum.ChangeClientType
    SEARCH_ADS_360_SYNC: ChangeClientTypeEnum.ChangeClientType
    SEARCH_ADS_360_POST: ChangeClientTypeEnum.ChangeClientType
    INTERNAL_TOOL: ChangeClientTypeEnum.ChangeClientType
    OTHER: ChangeClientTypeEnum.ChangeClientType
    GOOGLE_ADS_RECOMMENDATIONS_SUBSCRIPTION: ChangeClientTypeEnum.ChangeClientType

    def __init__(self) -> None:
        ...