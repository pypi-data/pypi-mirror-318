from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ValidationError(_message.Message):
    __slots__ = ('severity', 'entries', 'error_message')

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[ValidationError.Severity]
        INFO: _ClassVar[ValidationError.Severity]
        WARNING: _ClassVar[ValidationError.Severity]
        ERROR: _ClassVar[ValidationError.Severity]
        CRITICAL: _ClassVar[ValidationError.Severity]
    SEVERITY_UNSPECIFIED: ValidationError.Severity
    INFO: ValidationError.Severity
    WARNING: ValidationError.Severity
    ERROR: ValidationError.Severity
    CRITICAL: ValidationError.Severity
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    severity: ValidationError.Severity
    entries: _containers.RepeatedScalarFieldContainer[str]
    error_message: str

    def __init__(self, severity: _Optional[_Union[ValidationError.Severity, str]]=..., entries: _Optional[_Iterable[str]]=..., error_message: _Optional[str]=...) -> None:
        ...

class ValidationResult(_message.Message):
    __slots__ = ('validation_errors',)
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    validation_errors: _containers.RepeatedCompositeFieldContainer[ValidationError]

    def __init__(self, validation_errors: _Optional[_Iterable[_Union[ValidationError, _Mapping]]]=...) -> None:
        ...