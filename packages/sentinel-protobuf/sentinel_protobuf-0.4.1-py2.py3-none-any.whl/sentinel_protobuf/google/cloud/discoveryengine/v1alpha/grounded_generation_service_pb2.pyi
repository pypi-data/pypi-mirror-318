from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import grounding_pb2 as _grounding_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckGroundingSpec(_message.Message):
    __slots__ = ("citation_threshold",)
    CITATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    citation_threshold: float
    def __init__(self, citation_threshold: _Optional[float] = ...) -> None: ...

class CheckGroundingRequest(_message.Message):
    __slots__ = ("grounding_config", "answer_candidate", "facts", "grounding_spec", "user_labels")
    class UserLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GROUNDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANSWER_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    GROUNDING_SPEC_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    grounding_config: str
    answer_candidate: str
    facts: _containers.RepeatedCompositeFieldContainer[_grounding_pb2.GroundingFact]
    grounding_spec: CheckGroundingSpec
    user_labels: _containers.ScalarMap[str, str]
    def __init__(self, grounding_config: _Optional[str] = ..., answer_candidate: _Optional[str] = ..., facts: _Optional[_Iterable[_Union[_grounding_pb2.GroundingFact, _Mapping]]] = ..., grounding_spec: _Optional[_Union[CheckGroundingSpec, _Mapping]] = ..., user_labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CheckGroundingResponse(_message.Message):
    __slots__ = ("support_score", "cited_chunks", "claims")
    class Claim(_message.Message):
        __slots__ = ("start_pos", "end_pos", "claim_text", "citation_indices", "grounding_check_required")
        START_POS_FIELD_NUMBER: _ClassVar[int]
        END_POS_FIELD_NUMBER: _ClassVar[int]
        CLAIM_TEXT_FIELD_NUMBER: _ClassVar[int]
        CITATION_INDICES_FIELD_NUMBER: _ClassVar[int]
        GROUNDING_CHECK_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        start_pos: int
        end_pos: int
        claim_text: str
        citation_indices: _containers.RepeatedScalarFieldContainer[int]
        grounding_check_required: bool
        def __init__(self, start_pos: _Optional[int] = ..., end_pos: _Optional[int] = ..., claim_text: _Optional[str] = ..., citation_indices: _Optional[_Iterable[int]] = ..., grounding_check_required: bool = ...) -> None: ...
    SUPPORT_SCORE_FIELD_NUMBER: _ClassVar[int]
    CITED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    support_score: float
    cited_chunks: _containers.RepeatedCompositeFieldContainer[_grounding_pb2.FactChunk]
    claims: _containers.RepeatedCompositeFieldContainer[CheckGroundingResponse.Claim]
    def __init__(self, support_score: _Optional[float] = ..., cited_chunks: _Optional[_Iterable[_Union[_grounding_pb2.FactChunk, _Mapping]]] = ..., claims: _Optional[_Iterable[_Union[CheckGroundingResponse.Claim, _Mapping]]] = ...) -> None: ...
