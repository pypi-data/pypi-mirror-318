from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EvaluationReference(_message.Message):
    __slots__ = ('operation', 'evaluation', 'aggregate_metrics', 'aggregate_metrics_exact')
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_METRICS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_METRICS_EXACT_FIELD_NUMBER: _ClassVar[int]
    operation: str
    evaluation: str
    aggregate_metrics: Evaluation.Metrics
    aggregate_metrics_exact: Evaluation.Metrics

    def __init__(self, operation: _Optional[str]=..., evaluation: _Optional[str]=..., aggregate_metrics: _Optional[_Union[Evaluation.Metrics, _Mapping]]=..., aggregate_metrics_exact: _Optional[_Union[Evaluation.Metrics, _Mapping]]=...) -> None:
        ...

class Evaluation(_message.Message):
    __slots__ = ('name', 'create_time', 'document_counters', 'all_entities_metrics', 'entity_metrics', 'kms_key_name', 'kms_key_version_name')

    class Counters(_message.Message):
        __slots__ = ('input_documents_count', 'invalid_documents_count', 'failed_documents_count', 'evaluated_documents_count')
        INPUT_DOCUMENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        INVALID_DOCUMENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        FAILED_DOCUMENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        EVALUATED_DOCUMENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        input_documents_count: int
        invalid_documents_count: int
        failed_documents_count: int
        evaluated_documents_count: int

        def __init__(self, input_documents_count: _Optional[int]=..., invalid_documents_count: _Optional[int]=..., failed_documents_count: _Optional[int]=..., evaluated_documents_count: _Optional[int]=...) -> None:
            ...

    class Metrics(_message.Message):
        __slots__ = ('precision', 'recall', 'f1_score', 'predicted_occurrences_count', 'ground_truth_occurrences_count', 'predicted_document_count', 'ground_truth_document_count', 'true_positives_count', 'false_positives_count', 'false_negatives_count', 'total_documents_count')
        PRECISION_FIELD_NUMBER: _ClassVar[int]
        RECALL_FIELD_NUMBER: _ClassVar[int]
        F1_SCORE_FIELD_NUMBER: _ClassVar[int]
        PREDICTED_OCCURRENCES_COUNT_FIELD_NUMBER: _ClassVar[int]
        GROUND_TRUTH_OCCURRENCES_COUNT_FIELD_NUMBER: _ClassVar[int]
        PREDICTED_DOCUMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
        GROUND_TRUTH_DOCUMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
        TRUE_POSITIVES_COUNT_FIELD_NUMBER: _ClassVar[int]
        FALSE_POSITIVES_COUNT_FIELD_NUMBER: _ClassVar[int]
        FALSE_NEGATIVES_COUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_DOCUMENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        precision: float
        recall: float
        f1_score: float
        predicted_occurrences_count: int
        ground_truth_occurrences_count: int
        predicted_document_count: int
        ground_truth_document_count: int
        true_positives_count: int
        false_positives_count: int
        false_negatives_count: int
        total_documents_count: int

        def __init__(self, precision: _Optional[float]=..., recall: _Optional[float]=..., f1_score: _Optional[float]=..., predicted_occurrences_count: _Optional[int]=..., ground_truth_occurrences_count: _Optional[int]=..., predicted_document_count: _Optional[int]=..., ground_truth_document_count: _Optional[int]=..., true_positives_count: _Optional[int]=..., false_positives_count: _Optional[int]=..., false_negatives_count: _Optional[int]=..., total_documents_count: _Optional[int]=...) -> None:
            ...

    class ConfidenceLevelMetrics(_message.Message):
        __slots__ = ('confidence_level', 'metrics')
        CONFIDENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
        METRICS_FIELD_NUMBER: _ClassVar[int]
        confidence_level: float
        metrics: Evaluation.Metrics

        def __init__(self, confidence_level: _Optional[float]=..., metrics: _Optional[_Union[Evaluation.Metrics, _Mapping]]=...) -> None:
            ...

    class MultiConfidenceMetrics(_message.Message):
        __slots__ = ('confidence_level_metrics', 'confidence_level_metrics_exact', 'auprc', 'estimated_calibration_error', 'auprc_exact', 'estimated_calibration_error_exact', 'metrics_type')

        class MetricsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METRICS_TYPE_UNSPECIFIED: _ClassVar[Evaluation.MultiConfidenceMetrics.MetricsType]
            AGGREGATE: _ClassVar[Evaluation.MultiConfidenceMetrics.MetricsType]
        METRICS_TYPE_UNSPECIFIED: Evaluation.MultiConfidenceMetrics.MetricsType
        AGGREGATE: Evaluation.MultiConfidenceMetrics.MetricsType
        CONFIDENCE_LEVEL_METRICS_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_LEVEL_METRICS_EXACT_FIELD_NUMBER: _ClassVar[int]
        AUPRC_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_CALIBRATION_ERROR_FIELD_NUMBER: _ClassVar[int]
        AUPRC_EXACT_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_CALIBRATION_ERROR_EXACT_FIELD_NUMBER: _ClassVar[int]
        METRICS_TYPE_FIELD_NUMBER: _ClassVar[int]
        confidence_level_metrics: _containers.RepeatedCompositeFieldContainer[Evaluation.ConfidenceLevelMetrics]
        confidence_level_metrics_exact: _containers.RepeatedCompositeFieldContainer[Evaluation.ConfidenceLevelMetrics]
        auprc: float
        estimated_calibration_error: float
        auprc_exact: float
        estimated_calibration_error_exact: float
        metrics_type: Evaluation.MultiConfidenceMetrics.MetricsType

        def __init__(self, confidence_level_metrics: _Optional[_Iterable[_Union[Evaluation.ConfidenceLevelMetrics, _Mapping]]]=..., confidence_level_metrics_exact: _Optional[_Iterable[_Union[Evaluation.ConfidenceLevelMetrics, _Mapping]]]=..., auprc: _Optional[float]=..., estimated_calibration_error: _Optional[float]=..., auprc_exact: _Optional[float]=..., estimated_calibration_error_exact: _Optional[float]=..., metrics_type: _Optional[_Union[Evaluation.MultiConfidenceMetrics.MetricsType, str]]=...) -> None:
            ...

    class EntityMetricsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Evaluation.MultiConfidenceMetrics

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Evaluation.MultiConfidenceMetrics, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    ALL_ENTITIES_METRICS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METRICS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    document_counters: Evaluation.Counters
    all_entities_metrics: Evaluation.MultiConfidenceMetrics
    entity_metrics: _containers.MessageMap[str, Evaluation.MultiConfidenceMetrics]
    kms_key_name: str
    kms_key_version_name: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., document_counters: _Optional[_Union[Evaluation.Counters, _Mapping]]=..., all_entities_metrics: _Optional[_Union[Evaluation.MultiConfidenceMetrics, _Mapping]]=..., entity_metrics: _Optional[_Mapping[str, Evaluation.MultiConfidenceMetrics]]=..., kms_key_name: _Optional[str]=..., kms_key_version_name: _Optional[str]=...) -> None:
        ...