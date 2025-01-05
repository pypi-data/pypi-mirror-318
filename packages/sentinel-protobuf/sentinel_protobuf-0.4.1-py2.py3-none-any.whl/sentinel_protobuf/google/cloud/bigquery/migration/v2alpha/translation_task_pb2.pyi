from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TranslationFileMapping(_message.Message):
    __slots__ = ('input_path', 'output_path')
    INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    input_path: str
    output_path: str

    def __init__(self, input_path: _Optional[str]=..., output_path: _Optional[str]=...) -> None:
        ...

class TranslationTaskDetails(_message.Message):
    __slots__ = ('teradata_options', 'bteq_options', 'input_path', 'output_path', 'file_paths', 'schema_path', 'file_encoding', 'identifier_settings', 'special_token_map', 'filter', 'translation_exception_table')

    class FileEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE_ENCODING_UNSPECIFIED: _ClassVar[TranslationTaskDetails.FileEncoding]
        UTF_8: _ClassVar[TranslationTaskDetails.FileEncoding]
        ISO_8859_1: _ClassVar[TranslationTaskDetails.FileEncoding]
        US_ASCII: _ClassVar[TranslationTaskDetails.FileEncoding]
        UTF_16: _ClassVar[TranslationTaskDetails.FileEncoding]
        UTF_16LE: _ClassVar[TranslationTaskDetails.FileEncoding]
        UTF_16BE: _ClassVar[TranslationTaskDetails.FileEncoding]
    FILE_ENCODING_UNSPECIFIED: TranslationTaskDetails.FileEncoding
    UTF_8: TranslationTaskDetails.FileEncoding
    ISO_8859_1: TranslationTaskDetails.FileEncoding
    US_ASCII: TranslationTaskDetails.FileEncoding
    UTF_16: TranslationTaskDetails.FileEncoding
    UTF_16LE: TranslationTaskDetails.FileEncoding
    UTF_16BE: TranslationTaskDetails.FileEncoding

    class TokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOKEN_TYPE_UNSPECIFIED: _ClassVar[TranslationTaskDetails.TokenType]
        STRING: _ClassVar[TranslationTaskDetails.TokenType]
        INT64: _ClassVar[TranslationTaskDetails.TokenType]
        NUMERIC: _ClassVar[TranslationTaskDetails.TokenType]
        BOOL: _ClassVar[TranslationTaskDetails.TokenType]
        FLOAT64: _ClassVar[TranslationTaskDetails.TokenType]
        DATE: _ClassVar[TranslationTaskDetails.TokenType]
        TIMESTAMP: _ClassVar[TranslationTaskDetails.TokenType]
    TOKEN_TYPE_UNSPECIFIED: TranslationTaskDetails.TokenType
    STRING: TranslationTaskDetails.TokenType
    INT64: TranslationTaskDetails.TokenType
    NUMERIC: TranslationTaskDetails.TokenType
    BOOL: TranslationTaskDetails.TokenType
    FLOAT64: TranslationTaskDetails.TokenType
    DATE: TranslationTaskDetails.TokenType
    TIMESTAMP: TranslationTaskDetails.TokenType

    class SpecialTokenMapEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TranslationTaskDetails.TokenType

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[TranslationTaskDetails.TokenType, str]]=...) -> None:
            ...
    TERADATA_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BTEQ_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_TOKEN_MAP_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_EXCEPTION_TABLE_FIELD_NUMBER: _ClassVar[int]
    teradata_options: TeradataOptions
    bteq_options: BteqOptions
    input_path: str
    output_path: str
    file_paths: _containers.RepeatedCompositeFieldContainer[TranslationFileMapping]
    schema_path: str
    file_encoding: TranslationTaskDetails.FileEncoding
    identifier_settings: IdentifierSettings
    special_token_map: _containers.ScalarMap[str, TranslationTaskDetails.TokenType]
    filter: Filter
    translation_exception_table: str

    def __init__(self, teradata_options: _Optional[_Union[TeradataOptions, _Mapping]]=..., bteq_options: _Optional[_Union[BteqOptions, _Mapping]]=..., input_path: _Optional[str]=..., output_path: _Optional[str]=..., file_paths: _Optional[_Iterable[_Union[TranslationFileMapping, _Mapping]]]=..., schema_path: _Optional[str]=..., file_encoding: _Optional[_Union[TranslationTaskDetails.FileEncoding, str]]=..., identifier_settings: _Optional[_Union[IdentifierSettings, _Mapping]]=..., special_token_map: _Optional[_Mapping[str, TranslationTaskDetails.TokenType]]=..., filter: _Optional[_Union[Filter, _Mapping]]=..., translation_exception_table: _Optional[str]=...) -> None:
        ...

class Filter(_message.Message):
    __slots__ = ('input_file_exclusion_prefixes',)
    INPUT_FILE_EXCLUSION_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    input_file_exclusion_prefixes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, input_file_exclusion_prefixes: _Optional[_Iterable[str]]=...) -> None:
        ...

class IdentifierSettings(_message.Message):
    __slots__ = ('output_identifier_case', 'identifier_rewrite_mode')

    class IdentifierCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IDENTIFIER_CASE_UNSPECIFIED: _ClassVar[IdentifierSettings.IdentifierCase]
        ORIGINAL: _ClassVar[IdentifierSettings.IdentifierCase]
        UPPER: _ClassVar[IdentifierSettings.IdentifierCase]
        LOWER: _ClassVar[IdentifierSettings.IdentifierCase]
    IDENTIFIER_CASE_UNSPECIFIED: IdentifierSettings.IdentifierCase
    ORIGINAL: IdentifierSettings.IdentifierCase
    UPPER: IdentifierSettings.IdentifierCase
    LOWER: IdentifierSettings.IdentifierCase

    class IdentifierRewriteMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IDENTIFIER_REWRITE_MODE_UNSPECIFIED: _ClassVar[IdentifierSettings.IdentifierRewriteMode]
        NONE: _ClassVar[IdentifierSettings.IdentifierRewriteMode]
        REWRITE_ALL: _ClassVar[IdentifierSettings.IdentifierRewriteMode]
    IDENTIFIER_REWRITE_MODE_UNSPECIFIED: IdentifierSettings.IdentifierRewriteMode
    NONE: IdentifierSettings.IdentifierRewriteMode
    REWRITE_ALL: IdentifierSettings.IdentifierRewriteMode
    OUTPUT_IDENTIFIER_CASE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_REWRITE_MODE_FIELD_NUMBER: _ClassVar[int]
    output_identifier_case: IdentifierSettings.IdentifierCase
    identifier_rewrite_mode: IdentifierSettings.IdentifierRewriteMode

    def __init__(self, output_identifier_case: _Optional[_Union[IdentifierSettings.IdentifierCase, str]]=..., identifier_rewrite_mode: _Optional[_Union[IdentifierSettings.IdentifierRewriteMode, str]]=...) -> None:
        ...

class TeradataOptions(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class BteqOptions(_message.Message):
    __slots__ = ('project_dataset', 'default_path_uri', 'file_replacement_map')

    class FileReplacementMapEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PROJECT_DATASET_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PATH_URI_FIELD_NUMBER: _ClassVar[int]
    FILE_REPLACEMENT_MAP_FIELD_NUMBER: _ClassVar[int]
    project_dataset: DatasetReference
    default_path_uri: str
    file_replacement_map: _containers.ScalarMap[str, str]

    def __init__(self, project_dataset: _Optional[_Union[DatasetReference, _Mapping]]=..., default_path_uri: _Optional[str]=..., file_replacement_map: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class DatasetReference(_message.Message):
    __slots__ = ('dataset_id', 'project_id')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    project_id: str

    def __init__(self, dataset_id: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
        ...