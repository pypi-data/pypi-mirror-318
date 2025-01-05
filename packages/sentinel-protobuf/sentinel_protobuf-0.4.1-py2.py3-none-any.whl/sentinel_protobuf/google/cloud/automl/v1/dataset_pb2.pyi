from google.api import resource_pb2 as _resource_pb2
from google.cloud.automl.v1 import image_pb2 as _image_pb2
from google.cloud.automl.v1 import text_pb2 as _text_pb2
from google.cloud.automl.v1 import translation_pb2 as _translation_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Dataset(_message.Message):
    __slots__ = ('translation_dataset_metadata', 'image_classification_dataset_metadata', 'text_classification_dataset_metadata', 'image_object_detection_dataset_metadata', 'text_extraction_dataset_metadata', 'text_sentiment_dataset_metadata', 'name', 'display_name', 'description', 'example_count', 'create_time', 'etag', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TRANSLATION_DATASET_METADATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_CLASSIFICATION_DATASET_METADATA_FIELD_NUMBER: _ClassVar[int]
    TEXT_CLASSIFICATION_DATASET_METADATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_OBJECT_DETECTION_DATASET_METADATA_FIELD_NUMBER: _ClassVar[int]
    TEXT_EXTRACTION_DATASET_METADATA_FIELD_NUMBER: _ClassVar[int]
    TEXT_SENTIMENT_DATASET_METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    translation_dataset_metadata: _translation_pb2.TranslationDatasetMetadata
    image_classification_dataset_metadata: _image_pb2.ImageClassificationDatasetMetadata
    text_classification_dataset_metadata: _text_pb2.TextClassificationDatasetMetadata
    image_object_detection_dataset_metadata: _image_pb2.ImageObjectDetectionDatasetMetadata
    text_extraction_dataset_metadata: _text_pb2.TextExtractionDatasetMetadata
    text_sentiment_dataset_metadata: _text_pb2.TextSentimentDatasetMetadata
    name: str
    display_name: str
    description: str
    example_count: int
    create_time: _timestamp_pb2.Timestamp
    etag: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, translation_dataset_metadata: _Optional[_Union[_translation_pb2.TranslationDatasetMetadata, _Mapping]]=..., image_classification_dataset_metadata: _Optional[_Union[_image_pb2.ImageClassificationDatasetMetadata, _Mapping]]=..., text_classification_dataset_metadata: _Optional[_Union[_text_pb2.TextClassificationDatasetMetadata, _Mapping]]=..., image_object_detection_dataset_metadata: _Optional[_Union[_image_pb2.ImageObjectDetectionDatasetMetadata, _Mapping]]=..., text_extraction_dataset_metadata: _Optional[_Union[_text_pb2.TextExtractionDatasetMetadata, _Mapping]]=..., text_sentiment_dataset_metadata: _Optional[_Union[_text_pb2.TextSentimentDatasetMetadata, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., example_count: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...