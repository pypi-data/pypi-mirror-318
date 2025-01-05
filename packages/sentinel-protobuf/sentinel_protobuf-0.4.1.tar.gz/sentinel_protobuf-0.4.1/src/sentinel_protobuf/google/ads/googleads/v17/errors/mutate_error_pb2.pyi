from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MutateErrorEnum(_message.Message):
    __slots__ = ()

    class MutateError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MutateErrorEnum.MutateError]
        UNKNOWN: _ClassVar[MutateErrorEnum.MutateError]
        RESOURCE_NOT_FOUND: _ClassVar[MutateErrorEnum.MutateError]
        ID_EXISTS_IN_MULTIPLE_MUTATES: _ClassVar[MutateErrorEnum.MutateError]
        INCONSISTENT_FIELD_VALUES: _ClassVar[MutateErrorEnum.MutateError]
        MUTATE_NOT_ALLOWED: _ClassVar[MutateErrorEnum.MutateError]
        RESOURCE_NOT_IN_GOOGLE_ADS: _ClassVar[MutateErrorEnum.MutateError]
        RESOURCE_ALREADY_EXISTS: _ClassVar[MutateErrorEnum.MutateError]
        RESOURCE_DOES_NOT_SUPPORT_VALIDATE_ONLY: _ClassVar[MutateErrorEnum.MutateError]
        OPERATION_DOES_NOT_SUPPORT_PARTIAL_FAILURE: _ClassVar[MutateErrorEnum.MutateError]
        RESOURCE_READ_ONLY: _ClassVar[MutateErrorEnum.MutateError]
    UNSPECIFIED: MutateErrorEnum.MutateError
    UNKNOWN: MutateErrorEnum.MutateError
    RESOURCE_NOT_FOUND: MutateErrorEnum.MutateError
    ID_EXISTS_IN_MULTIPLE_MUTATES: MutateErrorEnum.MutateError
    INCONSISTENT_FIELD_VALUES: MutateErrorEnum.MutateError
    MUTATE_NOT_ALLOWED: MutateErrorEnum.MutateError
    RESOURCE_NOT_IN_GOOGLE_ADS: MutateErrorEnum.MutateError
    RESOURCE_ALREADY_EXISTS: MutateErrorEnum.MutateError
    RESOURCE_DOES_NOT_SUPPORT_VALIDATE_ONLY: MutateErrorEnum.MutateError
    OPERATION_DOES_NOT_SUPPORT_PARTIAL_FAILURE: MutateErrorEnum.MutateError
    RESOURCE_READ_ONLY: MutateErrorEnum.MutateError

    def __init__(self) -> None:
        ...