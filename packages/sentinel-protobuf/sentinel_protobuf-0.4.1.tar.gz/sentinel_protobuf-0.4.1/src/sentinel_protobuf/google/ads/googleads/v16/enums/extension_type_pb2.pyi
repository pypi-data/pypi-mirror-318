from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExtensionTypeEnum(_message.Message):
    __slots__ = ()

    class ExtensionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExtensionTypeEnum.ExtensionType]
        UNKNOWN: _ClassVar[ExtensionTypeEnum.ExtensionType]
        NONE: _ClassVar[ExtensionTypeEnum.ExtensionType]
        APP: _ClassVar[ExtensionTypeEnum.ExtensionType]
        CALL: _ClassVar[ExtensionTypeEnum.ExtensionType]
        CALLOUT: _ClassVar[ExtensionTypeEnum.ExtensionType]
        MESSAGE: _ClassVar[ExtensionTypeEnum.ExtensionType]
        PRICE: _ClassVar[ExtensionTypeEnum.ExtensionType]
        PROMOTION: _ClassVar[ExtensionTypeEnum.ExtensionType]
        SITELINK: _ClassVar[ExtensionTypeEnum.ExtensionType]
        STRUCTURED_SNIPPET: _ClassVar[ExtensionTypeEnum.ExtensionType]
        LOCATION: _ClassVar[ExtensionTypeEnum.ExtensionType]
        AFFILIATE_LOCATION: _ClassVar[ExtensionTypeEnum.ExtensionType]
        HOTEL_CALLOUT: _ClassVar[ExtensionTypeEnum.ExtensionType]
        IMAGE: _ClassVar[ExtensionTypeEnum.ExtensionType]
    UNSPECIFIED: ExtensionTypeEnum.ExtensionType
    UNKNOWN: ExtensionTypeEnum.ExtensionType
    NONE: ExtensionTypeEnum.ExtensionType
    APP: ExtensionTypeEnum.ExtensionType
    CALL: ExtensionTypeEnum.ExtensionType
    CALLOUT: ExtensionTypeEnum.ExtensionType
    MESSAGE: ExtensionTypeEnum.ExtensionType
    PRICE: ExtensionTypeEnum.ExtensionType
    PROMOTION: ExtensionTypeEnum.ExtensionType
    SITELINK: ExtensionTypeEnum.ExtensionType
    STRUCTURED_SNIPPET: ExtensionTypeEnum.ExtensionType
    LOCATION: ExtensionTypeEnum.ExtensionType
    AFFILIATE_LOCATION: ExtensionTypeEnum.ExtensionType
    HOTEL_CALLOUT: ExtensionTypeEnum.ExtensionType
    IMAGE: ExtensionTypeEnum.ExtensionType

    def __init__(self) -> None:
        ...