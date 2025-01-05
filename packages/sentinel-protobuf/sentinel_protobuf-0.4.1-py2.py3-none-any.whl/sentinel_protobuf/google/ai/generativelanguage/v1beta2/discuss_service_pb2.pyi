from google.ai.generativelanguage.v1beta2 import citation_pb2 as _citation_pb2
from google.ai.generativelanguage.v1beta2 import safety_pb2 as _safety_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateMessageRequest(_message.Message):
    __slots__ = ("model", "prompt", "temperature", "candidate_count", "top_p", "top_k")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    model: str
    prompt: MessagePrompt
    temperature: float
    candidate_count: int
    top_p: float
    top_k: int
    def __init__(self, model: _Optional[str] = ..., prompt: _Optional[_Union[MessagePrompt, _Mapping]] = ..., temperature: _Optional[float] = ..., candidate_count: _Optional[int] = ..., top_p: _Optional[float] = ..., top_k: _Optional[int] = ...) -> None: ...

class GenerateMessageResponse(_message.Message):
    __slots__ = ("candidates", "messages", "filters")
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[Message]
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    filters: _containers.RepeatedCompositeFieldContainer[_safety_pb2.ContentFilter]
    def __init__(self, candidates: _Optional[_Iterable[_Union[Message, _Mapping]]] = ..., messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ..., filters: _Optional[_Iterable[_Union[_safety_pb2.ContentFilter, _Mapping]]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("author", "content", "citation_metadata")
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CITATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    author: str
    content: str
    citation_metadata: _citation_pb2.CitationMetadata
    def __init__(self, author: _Optional[str] = ..., content: _Optional[str] = ..., citation_metadata: _Optional[_Union[_citation_pb2.CitationMetadata, _Mapping]] = ...) -> None: ...

class MessagePrompt(_message.Message):
    __slots__ = ("context", "examples", "messages")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    context: str
    examples: _containers.RepeatedCompositeFieldContainer[Example]
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    def __init__(self, context: _Optional[str] = ..., examples: _Optional[_Iterable[_Union[Example, _Mapping]]] = ..., messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ...) -> None: ...

class Example(_message.Message):
    __slots__ = ("input", "output")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    input: Message
    output: Message
    def __init__(self, input: _Optional[_Union[Message, _Mapping]] = ..., output: _Optional[_Union[Message, _Mapping]] = ...) -> None: ...

class CountMessageTokensRequest(_message.Message):
    __slots__ = ("model", "prompt")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    model: str
    prompt: MessagePrompt
    def __init__(self, model: _Optional[str] = ..., prompt: _Optional[_Union[MessagePrompt, _Mapping]] = ...) -> None: ...

class CountMessageTokensResponse(_message.Message):
    __slots__ = ("token_count",)
    TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    token_count: int
    def __init__(self, token_count: _Optional[int] = ...) -> None: ...
