from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Model(_message.Message):
    __slots__ = ("name", "base_model_id", "version", "display_name", "description", "input_token_limit", "output_token_limit", "supported_generation_methods", "temperature", "max_temperature", "top_p", "top_k")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKEN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKEN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_GENERATION_METHODS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MAX_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    name: str
    base_model_id: str
    version: str
    display_name: str
    description: str
    input_token_limit: int
    output_token_limit: int
    supported_generation_methods: _containers.RepeatedScalarFieldContainer[str]
    temperature: float
    max_temperature: float
    top_p: float
    top_k: int
    def __init__(self, name: _Optional[str] = ..., base_model_id: _Optional[str] = ..., version: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., input_token_limit: _Optional[int] = ..., output_token_limit: _Optional[int] = ..., supported_generation_methods: _Optional[_Iterable[str]] = ..., temperature: _Optional[float] = ..., max_temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., top_k: _Optional[int] = ...) -> None: ...
