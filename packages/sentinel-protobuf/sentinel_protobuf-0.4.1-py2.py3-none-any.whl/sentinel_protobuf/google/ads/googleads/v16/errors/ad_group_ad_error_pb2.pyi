from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAdErrorEnum(_message.Message):
    __slots__ = ()

    class AdGroupAdError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        UNKNOWN: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        AD_GROUP_AD_LABEL_DOES_NOT_EXIST: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        AD_GROUP_AD_LABEL_ALREADY_EXISTS: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        AD_NOT_UNDER_ADGROUP: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        CANNOT_OPERATE_ON_REMOVED_ADGROUPAD: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        CANNOT_CREATE_DEPRECATED_ADS: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        CANNOT_CREATE_TEXT_ADS: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        EMPTY_FIELD: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        RESOURCE_REFERENCED_IN_MULTIPLE_OPS: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        AD_TYPE_CANNOT_BE_PAUSED: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        AD_TYPE_CANNOT_BE_REMOVED: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
        CANNOT_UPDATE_DEPRECATED_ADS: _ClassVar[AdGroupAdErrorEnum.AdGroupAdError]
    UNSPECIFIED: AdGroupAdErrorEnum.AdGroupAdError
    UNKNOWN: AdGroupAdErrorEnum.AdGroupAdError
    AD_GROUP_AD_LABEL_DOES_NOT_EXIST: AdGroupAdErrorEnum.AdGroupAdError
    AD_GROUP_AD_LABEL_ALREADY_EXISTS: AdGroupAdErrorEnum.AdGroupAdError
    AD_NOT_UNDER_ADGROUP: AdGroupAdErrorEnum.AdGroupAdError
    CANNOT_OPERATE_ON_REMOVED_ADGROUPAD: AdGroupAdErrorEnum.AdGroupAdError
    CANNOT_CREATE_DEPRECATED_ADS: AdGroupAdErrorEnum.AdGroupAdError
    CANNOT_CREATE_TEXT_ADS: AdGroupAdErrorEnum.AdGroupAdError
    EMPTY_FIELD: AdGroupAdErrorEnum.AdGroupAdError
    RESOURCE_REFERENCED_IN_MULTIPLE_OPS: AdGroupAdErrorEnum.AdGroupAdError
    AD_TYPE_CANNOT_BE_PAUSED: AdGroupAdErrorEnum.AdGroupAdError
    AD_TYPE_CANNOT_BE_REMOVED: AdGroupAdErrorEnum.AdGroupAdError
    CANNOT_UPDATE_DEPRECATED_ADS: AdGroupAdErrorEnum.AdGroupAdError

    def __init__(self) -> None:
        ...