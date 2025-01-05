from google.api import resource_pb2 as _resource_pb2
from google.cloud.automl.v1 import classification_pb2 as _classification_pb2
from google.cloud.automl.v1 import detection_pb2 as _detection_pb2
from google.cloud.automl.v1 import text_extraction_pb2 as _text_extraction_pb2
from google.cloud.automl.v1 import text_sentiment_pb2 as _text_sentiment_pb2
from google.cloud.automl.v1 import translation_pb2 as _translation_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ModelEvaluation(_message.Message):
    __slots__ = ('classification_evaluation_metrics', 'translation_evaluation_metrics', 'image_object_detection_evaluation_metrics', 'text_sentiment_evaluation_metrics', 'text_extraction_evaluation_metrics', 'name', 'annotation_spec_id', 'display_name', 'create_time', 'evaluated_example_count')
    CLASSIFICATION_EVALUATION_METRICS_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_EVALUATION_METRICS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_OBJECT_DETECTION_EVALUATION_METRICS_FIELD_NUMBER: _ClassVar[int]
    TEXT_SENTIMENT_EVALUATION_METRICS_FIELD_NUMBER: _ClassVar[int]
    TEXT_EXTRACTION_EVALUATION_METRICS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    classification_evaluation_metrics: _classification_pb2.ClassificationEvaluationMetrics
    translation_evaluation_metrics: _translation_pb2.TranslationEvaluationMetrics
    image_object_detection_evaluation_metrics: _detection_pb2.ImageObjectDetectionEvaluationMetrics
    text_sentiment_evaluation_metrics: _text_sentiment_pb2.TextSentimentEvaluationMetrics
    text_extraction_evaluation_metrics: _text_extraction_pb2.TextExtractionEvaluationMetrics
    name: str
    annotation_spec_id: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    evaluated_example_count: int

    def __init__(self, classification_evaluation_metrics: _Optional[_Union[_classification_pb2.ClassificationEvaluationMetrics, _Mapping]]=..., translation_evaluation_metrics: _Optional[_Union[_translation_pb2.TranslationEvaluationMetrics, _Mapping]]=..., image_object_detection_evaluation_metrics: _Optional[_Union[_detection_pb2.ImageObjectDetectionEvaluationMetrics, _Mapping]]=..., text_sentiment_evaluation_metrics: _Optional[_Union[_text_sentiment_pb2.TextSentimentEvaluationMetrics, _Mapping]]=..., text_extraction_evaluation_metrics: _Optional[_Union[_text_extraction_pb2.TextExtractionEvaluationMetrics, _Mapping]]=..., name: _Optional[str]=..., annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., evaluated_example_count: _Optional[int]=...) -> None:
        ...