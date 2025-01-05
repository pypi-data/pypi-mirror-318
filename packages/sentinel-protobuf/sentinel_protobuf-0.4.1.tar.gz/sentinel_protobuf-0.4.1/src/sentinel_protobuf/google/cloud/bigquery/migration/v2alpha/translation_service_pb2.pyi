from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TranslateQueryRequest(_message.Message):
    __slots__ = ('parent', 'source_dialect', 'query')

    class SqlTranslationSourceDialect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_TRANSLATION_SOURCE_DIALECT_UNSPECIFIED: _ClassVar[TranslateQueryRequest.SqlTranslationSourceDialect]
        TERADATA: _ClassVar[TranslateQueryRequest.SqlTranslationSourceDialect]
    SQL_TRANSLATION_SOURCE_DIALECT_UNSPECIFIED: TranslateQueryRequest.SqlTranslationSourceDialect
    TERADATA: TranslateQueryRequest.SqlTranslationSourceDialect
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DIALECT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source_dialect: TranslateQueryRequest.SqlTranslationSourceDialect
    query: str

    def __init__(self, parent: _Optional[str]=..., source_dialect: _Optional[_Union[TranslateQueryRequest.SqlTranslationSourceDialect, str]]=..., query: _Optional[str]=...) -> None:
        ...

class TranslateQueryResponse(_message.Message):
    __slots__ = ('translation_job', 'translated_query', 'errors', 'warnings')
    TRANSLATION_JOB_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_QUERY_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    translation_job: str
    translated_query: str
    errors: _containers.RepeatedCompositeFieldContainer[SqlTranslationError]
    warnings: _containers.RepeatedCompositeFieldContainer[SqlTranslationWarning]

    def __init__(self, translation_job: _Optional[str]=..., translated_query: _Optional[str]=..., errors: _Optional[_Iterable[_Union[SqlTranslationError, _Mapping]]]=..., warnings: _Optional[_Iterable[_Union[SqlTranslationWarning, _Mapping]]]=...) -> None:
        ...

class SqlTranslationErrorDetail(_message.Message):
    __slots__ = ('row', 'column', 'message')
    ROW_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    row: int
    column: int
    message: str

    def __init__(self, row: _Optional[int]=..., column: _Optional[int]=..., message: _Optional[str]=...) -> None:
        ...

class SqlTranslationError(_message.Message):
    __slots__ = ('error_type', 'error_detail')

    class SqlTranslationErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_TRANSLATION_ERROR_TYPE_UNSPECIFIED: _ClassVar[SqlTranslationError.SqlTranslationErrorType]
        SQL_PARSE_ERROR: _ClassVar[SqlTranslationError.SqlTranslationErrorType]
        UNSUPPORTED_SQL_FUNCTION: _ClassVar[SqlTranslationError.SqlTranslationErrorType]
    SQL_TRANSLATION_ERROR_TYPE_UNSPECIFIED: SqlTranslationError.SqlTranslationErrorType
    SQL_PARSE_ERROR: SqlTranslationError.SqlTranslationErrorType
    UNSUPPORTED_SQL_FUNCTION: SqlTranslationError.SqlTranslationErrorType
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    error_type: SqlTranslationError.SqlTranslationErrorType
    error_detail: SqlTranslationErrorDetail

    def __init__(self, error_type: _Optional[_Union[SqlTranslationError.SqlTranslationErrorType, str]]=..., error_detail: _Optional[_Union[SqlTranslationErrorDetail, _Mapping]]=...) -> None:
        ...

class SqlTranslationWarning(_message.Message):
    __slots__ = ('warning_detail',)
    WARNING_DETAIL_FIELD_NUMBER: _ClassVar[int]
    warning_detail: SqlTranslationErrorDetail

    def __init__(self, warning_detail: _Optional[_Union[SqlTranslationErrorDetail, _Mapping]]=...) -> None:
        ...