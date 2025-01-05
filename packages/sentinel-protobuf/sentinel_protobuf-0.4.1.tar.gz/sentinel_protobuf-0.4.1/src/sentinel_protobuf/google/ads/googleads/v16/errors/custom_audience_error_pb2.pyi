from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomAudienceErrorEnum(_message.Message):
    __slots__ = ()

    class CustomAudienceError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
        UNKNOWN: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
        NAME_ALREADY_USED: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
        CANNOT_REMOVE_WHILE_IN_USE: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
        RESOURCE_ALREADY_REMOVED: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
        MEMBER_TYPE_AND_PARAMETER_ALREADY_EXISTED: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
        INVALID_MEMBER_TYPE: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
        MEMBER_TYPE_AND_VALUE_DOES_NOT_MATCH: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
        POLICY_VIOLATION: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
        INVALID_TYPE_CHANGE: _ClassVar[CustomAudienceErrorEnum.CustomAudienceError]
    UNSPECIFIED: CustomAudienceErrorEnum.CustomAudienceError
    UNKNOWN: CustomAudienceErrorEnum.CustomAudienceError
    NAME_ALREADY_USED: CustomAudienceErrorEnum.CustomAudienceError
    CANNOT_REMOVE_WHILE_IN_USE: CustomAudienceErrorEnum.CustomAudienceError
    RESOURCE_ALREADY_REMOVED: CustomAudienceErrorEnum.CustomAudienceError
    MEMBER_TYPE_AND_PARAMETER_ALREADY_EXISTED: CustomAudienceErrorEnum.CustomAudienceError
    INVALID_MEMBER_TYPE: CustomAudienceErrorEnum.CustomAudienceError
    MEMBER_TYPE_AND_VALUE_DOES_NOT_MATCH: CustomAudienceErrorEnum.CustomAudienceError
    POLICY_VIOLATION: CustomAudienceErrorEnum.CustomAudienceError
    INVALID_TYPE_CHANGE: CustomAudienceErrorEnum.CustomAudienceError

    def __init__(self) -> None:
        ...