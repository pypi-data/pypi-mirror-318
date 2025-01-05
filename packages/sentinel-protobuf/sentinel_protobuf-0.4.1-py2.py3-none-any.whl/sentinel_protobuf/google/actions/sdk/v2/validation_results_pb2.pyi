from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ValidationResults(_message.Message):
    __slots__ = ('results',)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ValidationResult]

    def __init__(self, results: _Optional[_Iterable[_Union[ValidationResult, _Mapping]]]=...) -> None:
        ...

class ValidationResult(_message.Message):
    __slots__ = ('validation_message', 'validation_context')

    class ValidationContext(_message.Message):
        __slots__ = ('language_code',)
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        language_code: str

        def __init__(self, language_code: _Optional[str]=...) -> None:
            ...
    VALIDATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    validation_message: str
    validation_context: ValidationResult.ValidationContext

    def __init__(self, validation_message: _Optional[str]=..., validation_context: _Optional[_Union[ValidationResult.ValidationContext, _Mapping]]=...) -> None:
        ...