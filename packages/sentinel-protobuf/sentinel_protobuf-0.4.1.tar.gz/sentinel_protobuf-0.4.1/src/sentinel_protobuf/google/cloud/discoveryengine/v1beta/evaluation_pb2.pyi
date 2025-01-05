from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import search_service_pb2 as _search_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Evaluation(_message.Message):
    __slots__ = ("name", "evaluation_spec", "quality_metrics", "state", "error", "create_time", "end_time", "error_samples")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Evaluation.State]
        PENDING: _ClassVar[Evaluation.State]
        RUNNING: _ClassVar[Evaluation.State]
        SUCCEEDED: _ClassVar[Evaluation.State]
        FAILED: _ClassVar[Evaluation.State]
    STATE_UNSPECIFIED: Evaluation.State
    PENDING: Evaluation.State
    RUNNING: Evaluation.State
    SUCCEEDED: Evaluation.State
    FAILED: Evaluation.State
    class EvaluationSpec(_message.Message):
        __slots__ = ("search_request", "query_set_spec")
        class QuerySetSpec(_message.Message):
            __slots__ = ("sample_query_set",)
            SAMPLE_QUERY_SET_FIELD_NUMBER: _ClassVar[int]
            sample_query_set: str
            def __init__(self, sample_query_set: _Optional[str] = ...) -> None: ...
        SEARCH_REQUEST_FIELD_NUMBER: _ClassVar[int]
        QUERY_SET_SPEC_FIELD_NUMBER: _ClassVar[int]
        search_request: _search_service_pb2.SearchRequest
        query_set_spec: Evaluation.EvaluationSpec.QuerySetSpec
        def __init__(self, search_request: _Optional[_Union[_search_service_pb2.SearchRequest, _Mapping]] = ..., query_set_spec: _Optional[_Union[Evaluation.EvaluationSpec.QuerySetSpec, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    QUALITY_METRICS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    evaluation_spec: Evaluation.EvaluationSpec
    quality_metrics: QualityMetrics
    state: Evaluation.State
    error: _status_pb2.Status
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, name: _Optional[str] = ..., evaluation_spec: _Optional[_Union[Evaluation.EvaluationSpec, _Mapping]] = ..., quality_metrics: _Optional[_Union[QualityMetrics, _Mapping]] = ..., state: _Optional[_Union[Evaluation.State, str]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class QualityMetrics(_message.Message):
    __slots__ = ("doc_recall", "doc_precision", "doc_ndcg", "page_recall", "page_ndcg")
    class TopkMetrics(_message.Message):
        __slots__ = ("top_1", "top_3", "top_5", "top_10")
        TOP_1_FIELD_NUMBER: _ClassVar[int]
        TOP_3_FIELD_NUMBER: _ClassVar[int]
        TOP_5_FIELD_NUMBER: _ClassVar[int]
        TOP_10_FIELD_NUMBER: _ClassVar[int]
        top_1: float
        top_3: float
        top_5: float
        top_10: float
        def __init__(self, top_1: _Optional[float] = ..., top_3: _Optional[float] = ..., top_5: _Optional[float] = ..., top_10: _Optional[float] = ...) -> None: ...
    DOC_RECALL_FIELD_NUMBER: _ClassVar[int]
    DOC_PRECISION_FIELD_NUMBER: _ClassVar[int]
    DOC_NDCG_FIELD_NUMBER: _ClassVar[int]
    PAGE_RECALL_FIELD_NUMBER: _ClassVar[int]
    PAGE_NDCG_FIELD_NUMBER: _ClassVar[int]
    doc_recall: QualityMetrics.TopkMetrics
    doc_precision: QualityMetrics.TopkMetrics
    doc_ndcg: QualityMetrics.TopkMetrics
    page_recall: QualityMetrics.TopkMetrics
    page_ndcg: QualityMetrics.TopkMetrics
    def __init__(self, doc_recall: _Optional[_Union[QualityMetrics.TopkMetrics, _Mapping]] = ..., doc_precision: _Optional[_Union[QualityMetrics.TopkMetrics, _Mapping]] = ..., doc_ndcg: _Optional[_Union[QualityMetrics.TopkMetrics, _Mapping]] = ..., page_recall: _Optional[_Union[QualityMetrics.TopkMetrics, _Mapping]] = ..., page_ndcg: _Optional[_Union[QualityMetrics.TopkMetrics, _Mapping]] = ...) -> None: ...
