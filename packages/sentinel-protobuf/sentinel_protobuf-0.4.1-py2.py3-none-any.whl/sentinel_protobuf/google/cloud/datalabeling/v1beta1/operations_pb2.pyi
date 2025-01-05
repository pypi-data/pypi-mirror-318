from google.cloud.datalabeling.v1beta1 import dataset_pb2 as _dataset_pb2
from google.cloud.datalabeling.v1beta1 import human_annotation_config_pb2 as _human_annotation_config_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImportDataOperationResponse(_message.Message):
    __slots__ = ('dataset', 'total_count', 'import_count')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_COUNT_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    total_count: int
    import_count: int

    def __init__(self, dataset: _Optional[str]=..., total_count: _Optional[int]=..., import_count: _Optional[int]=...) -> None:
        ...

class ExportDataOperationResponse(_message.Message):
    __slots__ = ('dataset', 'total_count', 'export_count', 'label_stats', 'output_config')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPORT_COUNT_FIELD_NUMBER: _ClassVar[int]
    LABEL_STATS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    total_count: int
    export_count: int
    label_stats: _dataset_pb2.LabelStats
    output_config: _dataset_pb2.OutputConfig

    def __init__(self, dataset: _Optional[str]=..., total_count: _Optional[int]=..., export_count: _Optional[int]=..., label_stats: _Optional[_Union[_dataset_pb2.LabelStats, _Mapping]]=..., output_config: _Optional[_Union[_dataset_pb2.OutputConfig, _Mapping]]=...) -> None:
        ...

class ImportDataOperationMetadata(_message.Message):
    __slots__ = ('dataset', 'partial_failures', 'create_time')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    partial_failures: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, dataset: _Optional[str]=..., partial_failures: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportDataOperationMetadata(_message.Message):
    __slots__ = ('dataset', 'partial_failures', 'create_time')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    partial_failures: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, dataset: _Optional[str]=..., partial_failures: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class LabelOperationMetadata(_message.Message):
    __slots__ = ('image_classification_details', 'image_bounding_box_details', 'image_bounding_poly_details', 'image_oriented_bounding_box_details', 'image_polyline_details', 'image_segmentation_details', 'video_classification_details', 'video_object_detection_details', 'video_object_tracking_details', 'video_event_details', 'text_classification_details', 'text_entity_extraction_details', 'progress_percent', 'partial_failures', 'create_time')
    IMAGE_CLASSIFICATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BOUNDING_BOX_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BOUNDING_POLY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ORIENTED_BOUNDING_BOX_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_POLYLINE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_SEGMENTATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CLASSIFICATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_OBJECT_DETECTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_OBJECT_TRACKING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EVENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TEXT_CLASSIFICATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TEXT_ENTITY_EXTRACTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    image_classification_details: LabelImageClassificationOperationMetadata
    image_bounding_box_details: LabelImageBoundingBoxOperationMetadata
    image_bounding_poly_details: LabelImageBoundingPolyOperationMetadata
    image_oriented_bounding_box_details: LabelImageOrientedBoundingBoxOperationMetadata
    image_polyline_details: LabelImagePolylineOperationMetadata
    image_segmentation_details: LabelImageSegmentationOperationMetadata
    video_classification_details: LabelVideoClassificationOperationMetadata
    video_object_detection_details: LabelVideoObjectDetectionOperationMetadata
    video_object_tracking_details: LabelVideoObjectTrackingOperationMetadata
    video_event_details: LabelVideoEventOperationMetadata
    text_classification_details: LabelTextClassificationOperationMetadata
    text_entity_extraction_details: LabelTextEntityExtractionOperationMetadata
    progress_percent: int
    partial_failures: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, image_classification_details: _Optional[_Union[LabelImageClassificationOperationMetadata, _Mapping]]=..., image_bounding_box_details: _Optional[_Union[LabelImageBoundingBoxOperationMetadata, _Mapping]]=..., image_bounding_poly_details: _Optional[_Union[LabelImageBoundingPolyOperationMetadata, _Mapping]]=..., image_oriented_bounding_box_details: _Optional[_Union[LabelImageOrientedBoundingBoxOperationMetadata, _Mapping]]=..., image_polyline_details: _Optional[_Union[LabelImagePolylineOperationMetadata, _Mapping]]=..., image_segmentation_details: _Optional[_Union[LabelImageSegmentationOperationMetadata, _Mapping]]=..., video_classification_details: _Optional[_Union[LabelVideoClassificationOperationMetadata, _Mapping]]=..., video_object_detection_details: _Optional[_Union[LabelVideoObjectDetectionOperationMetadata, _Mapping]]=..., video_object_tracking_details: _Optional[_Union[LabelVideoObjectTrackingOperationMetadata, _Mapping]]=..., video_event_details: _Optional[_Union[LabelVideoEventOperationMetadata, _Mapping]]=..., text_classification_details: _Optional[_Union[LabelTextClassificationOperationMetadata, _Mapping]]=..., text_entity_extraction_details: _Optional[_Union[LabelTextEntityExtractionOperationMetadata, _Mapping]]=..., progress_percent: _Optional[int]=..., partial_failures: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class LabelImageClassificationOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelImageBoundingBoxOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelImageOrientedBoundingBoxOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelImageBoundingPolyOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelImagePolylineOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelImageSegmentationOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelVideoClassificationOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelVideoObjectDetectionOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelVideoObjectTrackingOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelVideoEventOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelTextClassificationOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class LabelTextEntityExtractionOperationMetadata(_message.Message):
    __slots__ = ('basic_config',)
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig

    def __init__(self, basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=...) -> None:
        ...

class CreateInstructionMetadata(_message.Message):
    __slots__ = ('instruction', 'partial_failures', 'create_time')
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    instruction: str
    partial_failures: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, instruction: _Optional[str]=..., partial_failures: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...