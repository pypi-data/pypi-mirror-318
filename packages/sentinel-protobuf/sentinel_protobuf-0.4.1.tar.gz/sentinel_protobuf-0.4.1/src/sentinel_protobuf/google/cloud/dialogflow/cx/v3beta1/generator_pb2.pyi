from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import generative_settings_pb2 as _generative_settings_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Generator(_message.Message):
    __slots__ = ("name", "display_name", "prompt_text", "placeholders", "llm_model_settings", "model_parameter")
    class Placeholder(_message.Message):
        __slots__ = ("id", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    class ModelParameter(_message.Message):
        __slots__ = ("temperature", "max_decode_steps", "top_p", "top_k")
        TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        MAX_DECODE_STEPS_FIELD_NUMBER: _ClassVar[int]
        TOP_P_FIELD_NUMBER: _ClassVar[int]
        TOP_K_FIELD_NUMBER: _ClassVar[int]
        temperature: float
        max_decode_steps: int
        top_p: float
        top_k: int
        def __init__(self, temperature: _Optional[float] = ..., max_decode_steps: _Optional[int] = ..., top_p: _Optional[float] = ..., top_k: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEXT_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    prompt_text: Phrase
    placeholders: _containers.RepeatedCompositeFieldContainer[Generator.Placeholder]
    llm_model_settings: _generative_settings_pb2.LlmModelSettings
    model_parameter: Generator.ModelParameter
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., prompt_text: _Optional[_Union[Phrase, _Mapping]] = ..., placeholders: _Optional[_Iterable[_Union[Generator.Placeholder, _Mapping]]] = ..., llm_model_settings: _Optional[_Union[_generative_settings_pb2.LlmModelSettings, _Mapping]] = ..., model_parameter: _Optional[_Union[Generator.ModelParameter, _Mapping]] = ...) -> None: ...

class Phrase(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class ListGeneratorsRequest(_message.Message):
    __slots__ = ("parent", "language_code", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    language_code: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., language_code: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGeneratorsResponse(_message.Message):
    __slots__ = ("generators", "next_page_token")
    GENERATORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    generators: _containers.RepeatedCompositeFieldContainer[Generator]
    next_page_token: str
    def __init__(self, generators: _Optional[_Iterable[_Union[Generator, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetGeneratorRequest(_message.Message):
    __slots__ = ("name", "language_code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    def __init__(self, name: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...

class CreateGeneratorRequest(_message.Message):
    __slots__ = ("parent", "generator", "language_code")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    generator: Generator
    language_code: str
    def __init__(self, parent: _Optional[str] = ..., generator: _Optional[_Union[Generator, _Mapping]] = ..., language_code: _Optional[str] = ...) -> None: ...

class UpdateGeneratorRequest(_message.Message):
    __slots__ = ("generator", "language_code", "update_mask")
    GENERATOR_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    generator: Generator
    language_code: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, generator: _Optional[_Union[Generator, _Mapping]] = ..., language_code: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteGeneratorRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...
