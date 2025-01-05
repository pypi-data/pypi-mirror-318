from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.aiplatform.v1 import explanation_pb2 as _explanation_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvaluatedAnnotation(_message.Message):
    __slots__ = ("type", "predictions", "ground_truths", "data_item_payload", "evaluated_data_item_view_id", "explanations", "error_analysis_annotations")
    class EvaluatedAnnotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVALUATED_ANNOTATION_TYPE_UNSPECIFIED: _ClassVar[EvaluatedAnnotation.EvaluatedAnnotationType]
        TRUE_POSITIVE: _ClassVar[EvaluatedAnnotation.EvaluatedAnnotationType]
        FALSE_POSITIVE: _ClassVar[EvaluatedAnnotation.EvaluatedAnnotationType]
        FALSE_NEGATIVE: _ClassVar[EvaluatedAnnotation.EvaluatedAnnotationType]
    EVALUATED_ANNOTATION_TYPE_UNSPECIFIED: EvaluatedAnnotation.EvaluatedAnnotationType
    TRUE_POSITIVE: EvaluatedAnnotation.EvaluatedAnnotationType
    FALSE_POSITIVE: EvaluatedAnnotation.EvaluatedAnnotationType
    FALSE_NEGATIVE: EvaluatedAnnotation.EvaluatedAnnotationType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    GROUND_TRUTHS_FIELD_NUMBER: _ClassVar[int]
    DATA_ITEM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_DATA_ITEM_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_ANALYSIS_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    type: EvaluatedAnnotation.EvaluatedAnnotationType
    predictions: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    ground_truths: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    data_item_payload: _struct_pb2.Value
    evaluated_data_item_view_id: str
    explanations: _containers.RepeatedCompositeFieldContainer[EvaluatedAnnotationExplanation]
    error_analysis_annotations: _containers.RepeatedCompositeFieldContainer[ErrorAnalysisAnnotation]
    def __init__(self, type: _Optional[_Union[EvaluatedAnnotation.EvaluatedAnnotationType, str]] = ..., predictions: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ..., ground_truths: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ..., data_item_payload: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., evaluated_data_item_view_id: _Optional[str] = ..., explanations: _Optional[_Iterable[_Union[EvaluatedAnnotationExplanation, _Mapping]]] = ..., error_analysis_annotations: _Optional[_Iterable[_Union[ErrorAnalysisAnnotation, _Mapping]]] = ...) -> None: ...

class EvaluatedAnnotationExplanation(_message.Message):
    __slots__ = ("explanation_type", "explanation")
    EXPLANATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    explanation_type: str
    explanation: _explanation_pb2.Explanation
    def __init__(self, explanation_type: _Optional[str] = ..., explanation: _Optional[_Union[_explanation_pb2.Explanation, _Mapping]] = ...) -> None: ...

class ErrorAnalysisAnnotation(_message.Message):
    __slots__ = ("attributed_items", "query_type", "outlier_score", "outlier_threshold")
    class QueryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        QUERY_TYPE_UNSPECIFIED: _ClassVar[ErrorAnalysisAnnotation.QueryType]
        ALL_SIMILAR: _ClassVar[ErrorAnalysisAnnotation.QueryType]
        SAME_CLASS_SIMILAR: _ClassVar[ErrorAnalysisAnnotation.QueryType]
        SAME_CLASS_DISSIMILAR: _ClassVar[ErrorAnalysisAnnotation.QueryType]
    QUERY_TYPE_UNSPECIFIED: ErrorAnalysisAnnotation.QueryType
    ALL_SIMILAR: ErrorAnalysisAnnotation.QueryType
    SAME_CLASS_SIMILAR: ErrorAnalysisAnnotation.QueryType
    SAME_CLASS_DISSIMILAR: ErrorAnalysisAnnotation.QueryType
    class AttributedItem(_message.Message):
        __slots__ = ("annotation_resource_name", "distance")
        ANNOTATION_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        annotation_resource_name: str
        distance: float
        def __init__(self, annotation_resource_name: _Optional[str] = ..., distance: _Optional[float] = ...) -> None: ...
    ATTRIBUTED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTLIER_SCORE_FIELD_NUMBER: _ClassVar[int]
    OUTLIER_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    attributed_items: _containers.RepeatedCompositeFieldContainer[ErrorAnalysisAnnotation.AttributedItem]
    query_type: ErrorAnalysisAnnotation.QueryType
    outlier_score: float
    outlier_threshold: float
    def __init__(self, attributed_items: _Optional[_Iterable[_Union[ErrorAnalysisAnnotation.AttributedItem, _Mapping]]] = ..., query_type: _Optional[_Union[ErrorAnalysisAnnotation.QueryType, str]] = ..., outlier_score: _Optional[float] = ..., outlier_threshold: _Optional[float] = ...) -> None: ...
