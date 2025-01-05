from google.api import resource_pb2 as _resource_pb2
from google.cloud.datalabeling.v1beta1 import annotation_pb2 as _annotation_pb2
from google.cloud.datalabeling.v1beta1 import annotation_spec_set_pb2 as _annotation_spec_set_pb2
from google.cloud.datalabeling.v1beta1 import data_payloads_pb2 as _data_payloads_pb2
from google.cloud.datalabeling.v1beta1 import human_annotation_config_pb2 as _human_annotation_config_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_TYPE_UNSPECIFIED: _ClassVar[DataType]
    IMAGE: _ClassVar[DataType]
    VIDEO: _ClassVar[DataType]
    TEXT: _ClassVar[DataType]
    GENERAL_DATA: _ClassVar[DataType]
DATA_TYPE_UNSPECIFIED: DataType
IMAGE: DataType
VIDEO: DataType
TEXT: DataType
GENERAL_DATA: DataType

class Dataset(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'create_time', 'input_configs', 'blocking_resources', 'data_item_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    DATA_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    input_configs: _containers.RepeatedCompositeFieldContainer[InputConfig]
    blocking_resources: _containers.RepeatedScalarFieldContainer[str]
    data_item_count: int

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., input_configs: _Optional[_Iterable[_Union[InputConfig, _Mapping]]]=..., blocking_resources: _Optional[_Iterable[str]]=..., data_item_count: _Optional[int]=...) -> None:
        ...

class InputConfig(_message.Message):
    __slots__ = ('text_metadata', 'gcs_source', 'bigquery_source', 'data_type', 'annotation_type', 'classification_metadata')
    TEXT_METADATA_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    text_metadata: TextMetadata
    gcs_source: GcsSource
    bigquery_source: BigQuerySource
    data_type: DataType
    annotation_type: _annotation_pb2.AnnotationType
    classification_metadata: ClassificationMetadata

    def __init__(self, text_metadata: _Optional[_Union[TextMetadata, _Mapping]]=..., gcs_source: _Optional[_Union[GcsSource, _Mapping]]=..., bigquery_source: _Optional[_Union[BigQuerySource, _Mapping]]=..., data_type: _Optional[_Union[DataType, str]]=..., annotation_type: _Optional[_Union[_annotation_pb2.AnnotationType, str]]=..., classification_metadata: _Optional[_Union[ClassificationMetadata, _Mapping]]=...) -> None:
        ...

class TextMetadata(_message.Message):
    __slots__ = ('language_code',)
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    language_code: str

    def __init__(self, language_code: _Optional[str]=...) -> None:
        ...

class ClassificationMetadata(_message.Message):
    __slots__ = ('is_multi_label',)
    IS_MULTI_LABEL_FIELD_NUMBER: _ClassVar[int]
    is_multi_label: bool

    def __init__(self, is_multi_label: bool=...) -> None:
        ...

class GcsSource(_message.Message):
    __slots__ = ('input_uri', 'mime_type')
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    input_uri: str
    mime_type: str

    def __init__(self, input_uri: _Optional[str]=..., mime_type: _Optional[str]=...) -> None:
        ...

class BigQuerySource(_message.Message):
    __slots__ = ('input_uri',)
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    input_uri: str

    def __init__(self, input_uri: _Optional[str]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'gcs_folder_destination')
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    GCS_FOLDER_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    gcs_folder_destination: GcsFolderDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=..., gcs_folder_destination: _Optional[_Union[GcsFolderDestination, _Mapping]]=...) -> None:
        ...

class GcsDestination(_message.Message):
    __slots__ = ('output_uri', 'mime_type')
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    output_uri: str
    mime_type: str

    def __init__(self, output_uri: _Optional[str]=..., mime_type: _Optional[str]=...) -> None:
        ...

class GcsFolderDestination(_message.Message):
    __slots__ = ('output_folder_uri',)
    OUTPUT_FOLDER_URI_FIELD_NUMBER: _ClassVar[int]
    output_folder_uri: str

    def __init__(self, output_folder_uri: _Optional[str]=...) -> None:
        ...

class DataItem(_message.Message):
    __slots__ = ('image_payload', 'text_payload', 'video_payload', 'name')
    IMAGE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TEXT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    image_payload: _data_payloads_pb2.ImagePayload
    text_payload: _data_payloads_pb2.TextPayload
    video_payload: _data_payloads_pb2.VideoPayload
    name: str

    def __init__(self, image_payload: _Optional[_Union[_data_payloads_pb2.ImagePayload, _Mapping]]=..., text_payload: _Optional[_Union[_data_payloads_pb2.TextPayload, _Mapping]]=..., video_payload: _Optional[_Union[_data_payloads_pb2.VideoPayload, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class AnnotatedDataset(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'annotation_source', 'annotation_type', 'example_count', 'completed_example_count', 'label_stats', 'create_time', 'metadata', 'blocking_resources')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LABEL_STATS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    annotation_source: _annotation_pb2.AnnotationSource
    annotation_type: _annotation_pb2.AnnotationType
    example_count: int
    completed_example_count: int
    label_stats: LabelStats
    create_time: _timestamp_pb2.Timestamp
    metadata: AnnotatedDatasetMetadata
    blocking_resources: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., annotation_source: _Optional[_Union[_annotation_pb2.AnnotationSource, str]]=..., annotation_type: _Optional[_Union[_annotation_pb2.AnnotationType, str]]=..., example_count: _Optional[int]=..., completed_example_count: _Optional[int]=..., label_stats: _Optional[_Union[LabelStats, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., metadata: _Optional[_Union[AnnotatedDatasetMetadata, _Mapping]]=..., blocking_resources: _Optional[_Iterable[str]]=...) -> None:
        ...

class LabelStats(_message.Message):
    __slots__ = ('example_count',)

    class ExampleCountEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...
    EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    example_count: _containers.ScalarMap[str, int]

    def __init__(self, example_count: _Optional[_Mapping[str, int]]=...) -> None:
        ...

class AnnotatedDatasetMetadata(_message.Message):
    __slots__ = ('image_classification_config', 'bounding_poly_config', 'polyline_config', 'segmentation_config', 'video_classification_config', 'object_detection_config', 'object_tracking_config', 'event_config', 'text_classification_config', 'text_entity_extraction_config', 'human_annotation_config')
    IMAGE_CLASSIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_POLY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SEGMENTATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CLASSIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TRACKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_CLASSIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_ENTITY_EXTRACTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HUMAN_ANNOTATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    image_classification_config: _human_annotation_config_pb2.ImageClassificationConfig
    bounding_poly_config: _human_annotation_config_pb2.BoundingPolyConfig
    polyline_config: _human_annotation_config_pb2.PolylineConfig
    segmentation_config: _human_annotation_config_pb2.SegmentationConfig
    video_classification_config: _human_annotation_config_pb2.VideoClassificationConfig
    object_detection_config: _human_annotation_config_pb2.ObjectDetectionConfig
    object_tracking_config: _human_annotation_config_pb2.ObjectTrackingConfig
    event_config: _human_annotation_config_pb2.EventConfig
    text_classification_config: _human_annotation_config_pb2.TextClassificationConfig
    text_entity_extraction_config: _human_annotation_config_pb2.TextEntityExtractionConfig
    human_annotation_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, image_classification_config: _Optional[_Union[_human_annotation_config_pb2.ImageClassificationConfig, _Mapping]]=..., bounding_poly_config: _Optional[_Union[_human_annotation_config_pb2.BoundingPolyConfig, _Mapping]]=..., polyline_config: _Optional[_Union[_human_annotation_config_pb2.PolylineConfig, _Mapping]]=..., segmentation_config: _Optional[_Union[_human_annotation_config_pb2.SegmentationConfig, _Mapping]]=..., video_classification_config: _Optional[_Union[_human_annotation_config_pb2.VideoClassificationConfig, _Mapping]]=..., object_detection_config: _Optional[_Union[_human_annotation_config_pb2.ObjectDetectionConfig, _Mapping]]=..., object_tracking_config: _Optional[_Union[_human_annotation_config_pb2.ObjectTrackingConfig, _Mapping]]=..., event_config: _Optional[_Union[_human_annotation_config_pb2.EventConfig, _Mapping]]=..., text_classification_config: _Optional[_Union[_human_annotation_config_pb2.TextClassificationConfig, _Mapping]]=..., text_entity_extraction_config: _Optional[_Union[_human_annotation_config_pb2.TextEntityExtractionConfig, _Mapping]]=..., human_annotation_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class Example(_message.Message):
    __slots__ = ('image_payload', 'text_payload', 'video_payload', 'name', 'annotations')
    IMAGE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TEXT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    image_payload: _data_payloads_pb2.ImagePayload
    text_payload: _data_payloads_pb2.TextPayload
    video_payload: _data_payloads_pb2.VideoPayload
    name: str
    annotations: _containers.RepeatedCompositeFieldContainer[_annotation_pb2.Annotation]

    def __init__(self, image_payload: _Optional[_Union[_data_payloads_pb2.ImagePayload, _Mapping]]=..., text_payload: _Optional[_Union[_data_payloads_pb2.TextPayload, _Mapping]]=..., video_payload: _Optional[_Union[_data_payloads_pb2.VideoPayload, _Mapping]]=..., name: _Optional[str]=..., annotations: _Optional[_Iterable[_Union[_annotation_pb2.Annotation, _Mapping]]]=...) -> None:
        ...