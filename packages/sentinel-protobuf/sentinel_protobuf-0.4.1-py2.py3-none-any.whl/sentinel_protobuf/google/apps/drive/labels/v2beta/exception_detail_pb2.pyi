from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExceptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXCEPTION_TYPE_UNSPECIFIED: _ClassVar[ExceptionType]
    FIELD_REQUIRED: _ClassVar[ExceptionType]
    METAMODEL_ALREADY_EXISTS: _ClassVar[ExceptionType]
    METAMODEL_NOT_FOUND: _ClassVar[ExceptionType]
    ILLEGAL_METAMODEL_STATE_TRANSITION: _ClassVar[ExceptionType]
    INVALID_METAMODEL_DEPRECATION_POLICY: _ClassVar[ExceptionType]
    METAMODEL_DELETION_DENIED_UNTIL: _ClassVar[ExceptionType]
    INVALID_FIELD: _ClassVar[ExceptionType]
    METAMODEL_PRECONDITION_FAILED: _ClassVar[ExceptionType]
    DUPLICATE_FIELD_KEY: _ClassVar[ExceptionType]
    ILLEGAL_FIELD_REMOVAL: _ClassVar[ExceptionType]
    ILLEGAL_FIELD_OPTIONS_FOR_FIELD: _ClassVar[ExceptionType]
    UNSUPPORTED_CHANGE_TO_PUBLISHED_METAMODEL: _ClassVar[ExceptionType]
    ILLEGAL_METAMODEL_STATE_TRANSITION_IN_UPDATE: _ClassVar[ExceptionType]
    PAGE_TOKEN_EXPIRED: _ClassVar[ExceptionType]
    NOT_AUTHORIZED: _ClassVar[ExceptionType]
    ILLEGAL_FIELD_STATE_TRANSITION: _ClassVar[ExceptionType]
    ILLEGAL_CHOICE_SET_OPTION_STATE_TRANSITION: _ClassVar[ExceptionType]
    INVALID_CHOICE_SET_OPTIONS: _ClassVar[ExceptionType]
    INVALID_FIELD_KEY: _ClassVar[ExceptionType]
    INVALID_FIELD_PROPERTY_RANGE: _ClassVar[ExceptionType]
    INVALID_LOCALIZED_STRING: _ClassVar[ExceptionType]
    ILLEGAL_CHANGE_TO_PUBLISHED_FIELD: _ClassVar[ExceptionType]
    INVALID_FIELD_UPDATE_NOT_INCLUSIVE: _ClassVar[ExceptionType]
    INVALID_CHOICE_SET_STATE: _ClassVar[ExceptionType]
    INTERNAL_SERVER_ERROR: _ClassVar[ExceptionType]
EXCEPTION_TYPE_UNSPECIFIED: ExceptionType
FIELD_REQUIRED: ExceptionType
METAMODEL_ALREADY_EXISTS: ExceptionType
METAMODEL_NOT_FOUND: ExceptionType
ILLEGAL_METAMODEL_STATE_TRANSITION: ExceptionType
INVALID_METAMODEL_DEPRECATION_POLICY: ExceptionType
METAMODEL_DELETION_DENIED_UNTIL: ExceptionType
INVALID_FIELD: ExceptionType
METAMODEL_PRECONDITION_FAILED: ExceptionType
DUPLICATE_FIELD_KEY: ExceptionType
ILLEGAL_FIELD_REMOVAL: ExceptionType
ILLEGAL_FIELD_OPTIONS_FOR_FIELD: ExceptionType
UNSUPPORTED_CHANGE_TO_PUBLISHED_METAMODEL: ExceptionType
ILLEGAL_METAMODEL_STATE_TRANSITION_IN_UPDATE: ExceptionType
PAGE_TOKEN_EXPIRED: ExceptionType
NOT_AUTHORIZED: ExceptionType
ILLEGAL_FIELD_STATE_TRANSITION: ExceptionType
ILLEGAL_CHOICE_SET_OPTION_STATE_TRANSITION: ExceptionType
INVALID_CHOICE_SET_OPTIONS: ExceptionType
INVALID_FIELD_KEY: ExceptionType
INVALID_FIELD_PROPERTY_RANGE: ExceptionType
INVALID_LOCALIZED_STRING: ExceptionType
ILLEGAL_CHANGE_TO_PUBLISHED_FIELD: ExceptionType
INVALID_FIELD_UPDATE_NOT_INCLUSIVE: ExceptionType
INVALID_CHOICE_SET_STATE: ExceptionType
INTERNAL_SERVER_ERROR: ExceptionType

class ExceptionDetail(_message.Message):
    __slots__ = ('error_type',)
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    error_type: ExceptionType

    def __init__(self, error_type: _Optional[_Union[ExceptionType, str]]=...) -> None:
        ...