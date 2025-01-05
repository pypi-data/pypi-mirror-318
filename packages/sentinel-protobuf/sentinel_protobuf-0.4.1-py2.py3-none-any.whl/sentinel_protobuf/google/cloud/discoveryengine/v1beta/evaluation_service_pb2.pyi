from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import evaluation_pb2 as _evaluation_pb2
from google.cloud.discoveryengine.v1beta import sample_query_pb2 as _sample_query_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEvaluationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListEvaluationsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEvaluationsResponse(_message.Message):
    __slots__ = ("evaluations", "next_page_token")
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    evaluations: _containers.RepeatedCompositeFieldContainer[_evaluation_pb2.Evaluation]
    next_page_token: str
    def __init__(self, evaluations: _Optional[_Iterable[_Union[_evaluation_pb2.Evaluation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateEvaluationRequest(_message.Message):
    __slots__ = ("parent", "evaluation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    evaluation: _evaluation_pb2.Evaluation
    def __init__(self, parent: _Optional[str] = ..., evaluation: _Optional[_Union[_evaluation_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class CreateEvaluationMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEvaluationResultsRequest(_message.Message):
    __slots__ = ("evaluation", "page_size", "page_token")
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    evaluation: str
    page_size: int
    page_token: str
    def __init__(self, evaluation: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEvaluationResultsResponse(_message.Message):
    __slots__ = ("evaluation_results", "next_page_token")
    class EvaluationResult(_message.Message):
        __slots__ = ("sample_query", "quality_metrics")
        SAMPLE_QUERY_FIELD_NUMBER: _ClassVar[int]
        QUALITY_METRICS_FIELD_NUMBER: _ClassVar[int]
        sample_query: _sample_query_pb2.SampleQuery
        quality_metrics: _evaluation_pb2.QualityMetrics
        def __init__(self, sample_query: _Optional[_Union[_sample_query_pb2.SampleQuery, _Mapping]] = ..., quality_metrics: _Optional[_Union[_evaluation_pb2.QualityMetrics, _Mapping]] = ...) -> None: ...
    EVALUATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    evaluation_results: _containers.RepeatedCompositeFieldContainer[ListEvaluationResultsResponse.EvaluationResult]
    next_page_token: str
    def __init__(self, evaluation_results: _Optional[_Iterable[_Union[ListEvaluationResultsResponse.EvaluationResult, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
