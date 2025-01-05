from google.cloud.automl.v1beta1 import classification_pb2 as _classification_pb2
from google.cloud.automl.v1beta1 import detection_pb2 as _detection_pb2
from google.cloud.automl.v1beta1 import tables_pb2 as _tables_pb2
from google.cloud.automl.v1beta1 import text_extraction_pb2 as _text_extraction_pb2
from google.cloud.automl.v1beta1 import text_sentiment_pb2 as _text_sentiment_pb2
from google.cloud.automl.v1beta1 import translation_pb2 as _translation_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AnnotationPayload(_message.Message):
    __slots__ = ('translation', 'classification', 'image_object_detection', 'video_classification', 'video_object_tracking', 'text_extraction', 'text_sentiment', 'tables', 'annotation_spec_id', 'display_name')
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_OBJECT_DETECTION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_OBJECT_TRACKING_FIELD_NUMBER: _ClassVar[int]
    TEXT_EXTRACTION_FIELD_NUMBER: _ClassVar[int]
    TEXT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    translation: _translation_pb2.TranslationAnnotation
    classification: _classification_pb2.ClassificationAnnotation
    image_object_detection: _detection_pb2.ImageObjectDetectionAnnotation
    video_classification: _classification_pb2.VideoClassificationAnnotation
    video_object_tracking: _detection_pb2.VideoObjectTrackingAnnotation
    text_extraction: _text_extraction_pb2.TextExtractionAnnotation
    text_sentiment: _text_sentiment_pb2.TextSentimentAnnotation
    tables: _tables_pb2.TablesAnnotation
    annotation_spec_id: str
    display_name: str

    def __init__(self, translation: _Optional[_Union[_translation_pb2.TranslationAnnotation, _Mapping]]=..., classification: _Optional[_Union[_classification_pb2.ClassificationAnnotation, _Mapping]]=..., image_object_detection: _Optional[_Union[_detection_pb2.ImageObjectDetectionAnnotation, _Mapping]]=..., video_classification: _Optional[_Union[_classification_pb2.VideoClassificationAnnotation, _Mapping]]=..., video_object_tracking: _Optional[_Union[_detection_pb2.VideoObjectTrackingAnnotation, _Mapping]]=..., text_extraction: _Optional[_Union[_text_extraction_pb2.TextExtractionAnnotation, _Mapping]]=..., text_sentiment: _Optional[_Union[_text_sentiment_pb2.TextSentimentAnnotation, _Mapping]]=..., tables: _Optional[_Union[_tables_pb2.TablesAnnotation, _Mapping]]=..., annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...