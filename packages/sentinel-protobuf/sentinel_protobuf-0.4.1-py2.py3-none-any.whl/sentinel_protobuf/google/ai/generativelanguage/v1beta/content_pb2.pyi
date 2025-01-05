from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNSPECIFIED: _ClassVar[Type]
    STRING: _ClassVar[Type]
    NUMBER: _ClassVar[Type]
    INTEGER: _ClassVar[Type]
    BOOLEAN: _ClassVar[Type]
    ARRAY: _ClassVar[Type]
    OBJECT: _ClassVar[Type]
TYPE_UNSPECIFIED: Type
STRING: Type
NUMBER: Type
INTEGER: Type
BOOLEAN: Type
ARRAY: Type
OBJECT: Type

class Content(_message.Message):
    __slots__ = ("parts", "role")
    PARTS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[Part]
    role: str
    def __init__(self, parts: _Optional[_Iterable[_Union[Part, _Mapping]]] = ..., role: _Optional[str] = ...) -> None: ...

class Part(_message.Message):
    __slots__ = ("text", "inline_data", "function_call", "function_response", "file_data", "executable_code", "code_execution_result")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    INLINE_DATA_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_CALL_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLE_CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_EXECUTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    text: str
    inline_data: Blob
    function_call: FunctionCall
    function_response: FunctionResponse
    file_data: FileData
    executable_code: ExecutableCode
    code_execution_result: CodeExecutionResult
    def __init__(self, text: _Optional[str] = ..., inline_data: _Optional[_Union[Blob, _Mapping]] = ..., function_call: _Optional[_Union[FunctionCall, _Mapping]] = ..., function_response: _Optional[_Union[FunctionResponse, _Mapping]] = ..., file_data: _Optional[_Union[FileData, _Mapping]] = ..., executable_code: _Optional[_Union[ExecutableCode, _Mapping]] = ..., code_execution_result: _Optional[_Union[CodeExecutionResult, _Mapping]] = ...) -> None: ...

class Blob(_message.Message):
    __slots__ = ("mime_type", "data")
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    data: bytes
    def __init__(self, mime_type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class FileData(_message.Message):
    __slots__ = ("mime_type", "file_uri")
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_URI_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    file_uri: str
    def __init__(self, mime_type: _Optional[str] = ..., file_uri: _Optional[str] = ...) -> None: ...

class ExecutableCode(_message.Message):
    __slots__ = ("language", "code")
    class Language(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LANGUAGE_UNSPECIFIED: _ClassVar[ExecutableCode.Language]
        PYTHON: _ClassVar[ExecutableCode.Language]
    LANGUAGE_UNSPECIFIED: ExecutableCode.Language
    PYTHON: ExecutableCode.Language
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    language: ExecutableCode.Language
    code: str
    def __init__(self, language: _Optional[_Union[ExecutableCode.Language, str]] = ..., code: _Optional[str] = ...) -> None: ...

class CodeExecutionResult(_message.Message):
    __slots__ = ("outcome", "output")
    class Outcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTCOME_UNSPECIFIED: _ClassVar[CodeExecutionResult.Outcome]
        OUTCOME_OK: _ClassVar[CodeExecutionResult.Outcome]
        OUTCOME_FAILED: _ClassVar[CodeExecutionResult.Outcome]
        OUTCOME_DEADLINE_EXCEEDED: _ClassVar[CodeExecutionResult.Outcome]
    OUTCOME_UNSPECIFIED: CodeExecutionResult.Outcome
    OUTCOME_OK: CodeExecutionResult.Outcome
    OUTCOME_FAILED: CodeExecutionResult.Outcome
    OUTCOME_DEADLINE_EXCEEDED: CodeExecutionResult.Outcome
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    outcome: CodeExecutionResult.Outcome
    output: str
    def __init__(self, outcome: _Optional[_Union[CodeExecutionResult.Outcome, str]] = ..., output: _Optional[str] = ...) -> None: ...

class Tool(_message.Message):
    __slots__ = ("function_declarations", "google_search_retrieval", "code_execution")
    FUNCTION_DECLARATIONS_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SEARCH_RETRIEVAL_FIELD_NUMBER: _ClassVar[int]
    CODE_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    function_declarations: _containers.RepeatedCompositeFieldContainer[FunctionDeclaration]
    google_search_retrieval: GoogleSearchRetrieval
    code_execution: CodeExecution
    def __init__(self, function_declarations: _Optional[_Iterable[_Union[FunctionDeclaration, _Mapping]]] = ..., google_search_retrieval: _Optional[_Union[GoogleSearchRetrieval, _Mapping]] = ..., code_execution: _Optional[_Union[CodeExecution, _Mapping]] = ...) -> None: ...

class GoogleSearchRetrieval(_message.Message):
    __slots__ = ("dynamic_retrieval_config",)
    DYNAMIC_RETRIEVAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    dynamic_retrieval_config: DynamicRetrievalConfig
    def __init__(self, dynamic_retrieval_config: _Optional[_Union[DynamicRetrievalConfig, _Mapping]] = ...) -> None: ...

class DynamicRetrievalConfig(_message.Message):
    __slots__ = ("mode", "dynamic_threshold")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[DynamicRetrievalConfig.Mode]
        MODE_DYNAMIC: _ClassVar[DynamicRetrievalConfig.Mode]
    MODE_UNSPECIFIED: DynamicRetrievalConfig.Mode
    MODE_DYNAMIC: DynamicRetrievalConfig.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    mode: DynamicRetrievalConfig.Mode
    dynamic_threshold: float
    def __init__(self, mode: _Optional[_Union[DynamicRetrievalConfig.Mode, str]] = ..., dynamic_threshold: _Optional[float] = ...) -> None: ...

class CodeExecution(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ToolConfig(_message.Message):
    __slots__ = ("function_calling_config",)
    FUNCTION_CALLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    function_calling_config: FunctionCallingConfig
    def __init__(self, function_calling_config: _Optional[_Union[FunctionCallingConfig, _Mapping]] = ...) -> None: ...

class FunctionCallingConfig(_message.Message):
    __slots__ = ("mode", "allowed_function_names")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[FunctionCallingConfig.Mode]
        AUTO: _ClassVar[FunctionCallingConfig.Mode]
        ANY: _ClassVar[FunctionCallingConfig.Mode]
        NONE: _ClassVar[FunctionCallingConfig.Mode]
    MODE_UNSPECIFIED: FunctionCallingConfig.Mode
    AUTO: FunctionCallingConfig.Mode
    ANY: FunctionCallingConfig.Mode
    NONE: FunctionCallingConfig.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FUNCTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    mode: FunctionCallingConfig.Mode
    allowed_function_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mode: _Optional[_Union[FunctionCallingConfig.Mode, str]] = ..., allowed_function_names: _Optional[_Iterable[str]] = ...) -> None: ...

class FunctionDeclaration(_message.Message):
    __slots__ = ("name", "description", "parameters")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters: Schema
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., parameters: _Optional[_Union[Schema, _Mapping]] = ...) -> None: ...

class FunctionCall(_message.Message):
    __slots__ = ("name", "args")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    args: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., args: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class FunctionResponse(_message.Message):
    __slots__ = ("name", "response")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    name: str
    response: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., response: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Schema(_message.Message):
    __slots__ = ("type", "format", "description", "nullable", "enum", "items", "max_items", "min_items", "properties", "required")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Schema
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Schema, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MAX_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MIN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    type: Type
    format: str
    description: str
    nullable: bool
    enum: _containers.RepeatedScalarFieldContainer[str]
    items: Schema
    max_items: int
    min_items: int
    properties: _containers.MessageMap[str, Schema]
    required: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Union[Type, str]] = ..., format: _Optional[str] = ..., description: _Optional[str] = ..., nullable: bool = ..., enum: _Optional[_Iterable[str]] = ..., items: _Optional[_Union[Schema, _Mapping]] = ..., max_items: _Optional[int] = ..., min_items: _Optional[int] = ..., properties: _Optional[_Mapping[str, Schema]] = ..., required: _Optional[_Iterable[str]] = ...) -> None: ...

class GroundingPassage(_message.Message):
    __slots__ = ("id", "content")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: Content
    def __init__(self, id: _Optional[str] = ..., content: _Optional[_Union[Content, _Mapping]] = ...) -> None: ...

class GroundingPassages(_message.Message):
    __slots__ = ("passages",)
    PASSAGES_FIELD_NUMBER: _ClassVar[int]
    passages: _containers.RepeatedCompositeFieldContainer[GroundingPassage]
    def __init__(self, passages: _Optional[_Iterable[_Union[GroundingPassage, _Mapping]]] = ...) -> None: ...
