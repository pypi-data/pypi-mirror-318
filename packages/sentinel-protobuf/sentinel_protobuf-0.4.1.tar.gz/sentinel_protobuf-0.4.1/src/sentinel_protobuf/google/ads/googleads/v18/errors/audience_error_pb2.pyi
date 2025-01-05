from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AudienceErrorEnum(_message.Message):
    __slots__ = ()

    class AudienceError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AudienceErrorEnum.AudienceError]
        UNKNOWN: _ClassVar[AudienceErrorEnum.AudienceError]
        NAME_ALREADY_IN_USE: _ClassVar[AudienceErrorEnum.AudienceError]
        DIMENSION_INVALID: _ClassVar[AudienceErrorEnum.AudienceError]
        AUDIENCE_SEGMENT_NOT_FOUND: _ClassVar[AudienceErrorEnum.AudienceError]
        AUDIENCE_SEGMENT_TYPE_NOT_SUPPORTED: _ClassVar[AudienceErrorEnum.AudienceError]
        DUPLICATE_AUDIENCE_SEGMENT: _ClassVar[AudienceErrorEnum.AudienceError]
        TOO_MANY_SEGMENTS: _ClassVar[AudienceErrorEnum.AudienceError]
        TOO_MANY_DIMENSIONS_OF_SAME_TYPE: _ClassVar[AudienceErrorEnum.AudienceError]
        IN_USE: _ClassVar[AudienceErrorEnum.AudienceError]
        MISSING_ASSET_GROUP_ID: _ClassVar[AudienceErrorEnum.AudienceError]
        CANNOT_CHANGE_FROM_CUSTOMER_TO_ASSET_GROUP_SCOPE: _ClassVar[AudienceErrorEnum.AudienceError]
    UNSPECIFIED: AudienceErrorEnum.AudienceError
    UNKNOWN: AudienceErrorEnum.AudienceError
    NAME_ALREADY_IN_USE: AudienceErrorEnum.AudienceError
    DIMENSION_INVALID: AudienceErrorEnum.AudienceError
    AUDIENCE_SEGMENT_NOT_FOUND: AudienceErrorEnum.AudienceError
    AUDIENCE_SEGMENT_TYPE_NOT_SUPPORTED: AudienceErrorEnum.AudienceError
    DUPLICATE_AUDIENCE_SEGMENT: AudienceErrorEnum.AudienceError
    TOO_MANY_SEGMENTS: AudienceErrorEnum.AudienceError
    TOO_MANY_DIMENSIONS_OF_SAME_TYPE: AudienceErrorEnum.AudienceError
    IN_USE: AudienceErrorEnum.AudienceError
    MISSING_ASSET_GROUP_ID: AudienceErrorEnum.AudienceError
    CANNOT_CHANGE_FROM_CUSTOMER_TO_ASSET_GROUP_SCOPE: AudienceErrorEnum.AudienceError

    def __init__(self) -> None:
        ...