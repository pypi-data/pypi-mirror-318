from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdDestinationTypeEnum(_message.Message):
    __slots__ = ()

    class AdDestinationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        UNKNOWN: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        NOT_APPLICABLE: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        WEBSITE: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        APP_DEEP_LINK: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        APP_STORE: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        PHONE_CALL: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        MAP_DIRECTIONS: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        LOCATION_LISTING: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        MESSAGE: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        LEAD_FORM: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        YOUTUBE: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
        UNMODELED_FOR_CONVERSIONS: _ClassVar[AdDestinationTypeEnum.AdDestinationType]
    UNSPECIFIED: AdDestinationTypeEnum.AdDestinationType
    UNKNOWN: AdDestinationTypeEnum.AdDestinationType
    NOT_APPLICABLE: AdDestinationTypeEnum.AdDestinationType
    WEBSITE: AdDestinationTypeEnum.AdDestinationType
    APP_DEEP_LINK: AdDestinationTypeEnum.AdDestinationType
    APP_STORE: AdDestinationTypeEnum.AdDestinationType
    PHONE_CALL: AdDestinationTypeEnum.AdDestinationType
    MAP_DIRECTIONS: AdDestinationTypeEnum.AdDestinationType
    LOCATION_LISTING: AdDestinationTypeEnum.AdDestinationType
    MESSAGE: AdDestinationTypeEnum.AdDestinationType
    LEAD_FORM: AdDestinationTypeEnum.AdDestinationType
    YOUTUBE: AdDestinationTypeEnum.AdDestinationType
    UNMODELED_FOR_CONVERSIONS: AdDestinationTypeEnum.AdDestinationType

    def __init__(self) -> None:
        ...