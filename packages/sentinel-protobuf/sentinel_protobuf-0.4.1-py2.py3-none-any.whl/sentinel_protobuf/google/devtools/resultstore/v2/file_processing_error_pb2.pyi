from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FileProcessingErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_PROCESSING_ERROR_TYPE_UNSPECIFIED: _ClassVar[FileProcessingErrorType]
    GENERIC_READ_ERROR: _ClassVar[FileProcessingErrorType]
    GENERIC_PARSE_ERROR: _ClassVar[FileProcessingErrorType]
    FILE_TOO_LARGE: _ClassVar[FileProcessingErrorType]
    OUTPUT_TOO_LARGE: _ClassVar[FileProcessingErrorType]
    ACCESS_DENIED: _ClassVar[FileProcessingErrorType]
    DEADLINE_EXCEEDED: _ClassVar[FileProcessingErrorType]
    NOT_FOUND: _ClassVar[FileProcessingErrorType]
    FILE_EMPTY: _ClassVar[FileProcessingErrorType]
FILE_PROCESSING_ERROR_TYPE_UNSPECIFIED: FileProcessingErrorType
GENERIC_READ_ERROR: FileProcessingErrorType
GENERIC_PARSE_ERROR: FileProcessingErrorType
FILE_TOO_LARGE: FileProcessingErrorType
OUTPUT_TOO_LARGE: FileProcessingErrorType
ACCESS_DENIED: FileProcessingErrorType
DEADLINE_EXCEEDED: FileProcessingErrorType
NOT_FOUND: FileProcessingErrorType
FILE_EMPTY: FileProcessingErrorType

class FileProcessingErrors(_message.Message):
    __slots__ = ('file_uid', 'file_processing_errors')
    FILE_UID_FIELD_NUMBER: _ClassVar[int]
    FILE_PROCESSING_ERRORS_FIELD_NUMBER: _ClassVar[int]
    file_uid: str
    file_processing_errors: _containers.RepeatedCompositeFieldContainer[FileProcessingError]

    def __init__(self, file_uid: _Optional[str]=..., file_processing_errors: _Optional[_Iterable[_Union[FileProcessingError, _Mapping]]]=...) -> None:
        ...

class FileProcessingError(_message.Message):
    __slots__ = ('type', 'message')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    type: FileProcessingErrorType
    message: str

    def __init__(self, type: _Optional[_Union[FileProcessingErrorType, str]]=..., message: _Optional[str]=...) -> None:
        ...