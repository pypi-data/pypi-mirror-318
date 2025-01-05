from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.datalabeling.v1beta1 import annotation_spec_set_pb2 as _annotation_spec_set_pb2
from google.cloud.datalabeling.v1beta1 import dataset_pb2 as _dataset_pb2
from google.cloud.datalabeling.v1beta1 import evaluation_pb2 as _evaluation_pb2
from google.cloud.datalabeling.v1beta1 import evaluation_job_pb2 as _evaluation_job_pb2
from google.cloud.datalabeling.v1beta1 import human_annotation_config_pb2 as _human_annotation_config_pb2
from google.cloud.datalabeling.v1beta1 import instruction_pb2 as _instruction_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDatasetRequest(_message.Message):
    __slots__ = ('parent', 'dataset')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset: _dataset_pb2.Dataset

    def __init__(self, parent: _Optional[str]=..., dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]]=...) -> None:
        ...

class GetDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDatasetsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDatasetsResponse(_message.Message):
    __slots__ = ('datasets', 'next_page_token')
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.Dataset]
    next_page_token: str

    def __init__(self, datasets: _Optional[_Iterable[_Union[_dataset_pb2.Dataset, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ImportDataRequest(_message.Message):
    __slots__ = ('name', 'input_config', 'user_email_address')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_config: _dataset_pb2.InputConfig
    user_email_address: str

    def __init__(self, name: _Optional[str]=..., input_config: _Optional[_Union[_dataset_pb2.InputConfig, _Mapping]]=..., user_email_address: _Optional[str]=...) -> None:
        ...

class ExportDataRequest(_message.Message):
    __slots__ = ('name', 'annotated_dataset', 'filter', 'output_config', 'user_email_address')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATED_DATASET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    annotated_dataset: str
    filter: str
    output_config: _dataset_pb2.OutputConfig
    user_email_address: str

    def __init__(self, name: _Optional[str]=..., annotated_dataset: _Optional[str]=..., filter: _Optional[str]=..., output_config: _Optional[_Union[_dataset_pb2.OutputConfig, _Mapping]]=..., user_email_address: _Optional[str]=...) -> None:
        ...

class GetDataItemRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDataItemsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDataItemsResponse(_message.Message):
    __slots__ = ('data_items', 'next_page_token')
    DATA_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_items: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.DataItem]
    next_page_token: str

    def __init__(self, data_items: _Optional[_Iterable[_Union[_dataset_pb2.DataItem, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetAnnotatedDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAnnotatedDatasetsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAnnotatedDatasetsResponse(_message.Message):
    __slots__ = ('annotated_datasets', 'next_page_token')
    ANNOTATED_DATASETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    annotated_datasets: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.AnnotatedDataset]
    next_page_token: str

    def __init__(self, annotated_datasets: _Optional[_Iterable[_Union[_dataset_pb2.AnnotatedDataset, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteAnnotatedDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LabelImageRequest(_message.Message):
    __slots__ = ('image_classification_config', 'bounding_poly_config', 'polyline_config', 'segmentation_config', 'parent', 'basic_config', 'feature')

    class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_UNSPECIFIED: _ClassVar[LabelImageRequest.Feature]
        CLASSIFICATION: _ClassVar[LabelImageRequest.Feature]
        BOUNDING_BOX: _ClassVar[LabelImageRequest.Feature]
        ORIENTED_BOUNDING_BOX: _ClassVar[LabelImageRequest.Feature]
        BOUNDING_POLY: _ClassVar[LabelImageRequest.Feature]
        POLYLINE: _ClassVar[LabelImageRequest.Feature]
        SEGMENTATION: _ClassVar[LabelImageRequest.Feature]
    FEATURE_UNSPECIFIED: LabelImageRequest.Feature
    CLASSIFICATION: LabelImageRequest.Feature
    BOUNDING_BOX: LabelImageRequest.Feature
    ORIENTED_BOUNDING_BOX: LabelImageRequest.Feature
    BOUNDING_POLY: LabelImageRequest.Feature
    POLYLINE: LabelImageRequest.Feature
    SEGMENTATION: LabelImageRequest.Feature
    IMAGE_CLASSIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_POLY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SEGMENTATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    image_classification_config: _human_annotation_config_pb2.ImageClassificationConfig
    bounding_poly_config: _human_annotation_config_pb2.BoundingPolyConfig
    polyline_config: _human_annotation_config_pb2.PolylineConfig
    segmentation_config: _human_annotation_config_pb2.SegmentationConfig
    parent: str
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig
    feature: LabelImageRequest.Feature

    def __init__(self, image_classification_config: _Optional[_Union[_human_annotation_config_pb2.ImageClassificationConfig, _Mapping]]=..., bounding_poly_config: _Optional[_Union[_human_annotation_config_pb2.BoundingPolyConfig, _Mapping]]=..., polyline_config: _Optional[_Union[_human_annotation_config_pb2.PolylineConfig, _Mapping]]=..., segmentation_config: _Optional[_Union[_human_annotation_config_pb2.SegmentationConfig, _Mapping]]=..., parent: _Optional[str]=..., basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=..., feature: _Optional[_Union[LabelImageRequest.Feature, str]]=...) -> None:
        ...

class LabelVideoRequest(_message.Message):
    __slots__ = ('video_classification_config', 'object_detection_config', 'object_tracking_config', 'event_config', 'parent', 'basic_config', 'feature')

    class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_UNSPECIFIED: _ClassVar[LabelVideoRequest.Feature]
        CLASSIFICATION: _ClassVar[LabelVideoRequest.Feature]
        OBJECT_DETECTION: _ClassVar[LabelVideoRequest.Feature]
        OBJECT_TRACKING: _ClassVar[LabelVideoRequest.Feature]
        EVENT: _ClassVar[LabelVideoRequest.Feature]
    FEATURE_UNSPECIFIED: LabelVideoRequest.Feature
    CLASSIFICATION: LabelVideoRequest.Feature
    OBJECT_DETECTION: LabelVideoRequest.Feature
    OBJECT_TRACKING: LabelVideoRequest.Feature
    EVENT: LabelVideoRequest.Feature
    VIDEO_CLASSIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TRACKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    video_classification_config: _human_annotation_config_pb2.VideoClassificationConfig
    object_detection_config: _human_annotation_config_pb2.ObjectDetectionConfig
    object_tracking_config: _human_annotation_config_pb2.ObjectTrackingConfig
    event_config: _human_annotation_config_pb2.EventConfig
    parent: str
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig
    feature: LabelVideoRequest.Feature

    def __init__(self, video_classification_config: _Optional[_Union[_human_annotation_config_pb2.VideoClassificationConfig, _Mapping]]=..., object_detection_config: _Optional[_Union[_human_annotation_config_pb2.ObjectDetectionConfig, _Mapping]]=..., object_tracking_config: _Optional[_Union[_human_annotation_config_pb2.ObjectTrackingConfig, _Mapping]]=..., event_config: _Optional[_Union[_human_annotation_config_pb2.EventConfig, _Mapping]]=..., parent: _Optional[str]=..., basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=..., feature: _Optional[_Union[LabelVideoRequest.Feature, str]]=...) -> None:
        ...

class LabelTextRequest(_message.Message):
    __slots__ = ('text_classification_config', 'text_entity_extraction_config', 'parent', 'basic_config', 'feature')

    class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_UNSPECIFIED: _ClassVar[LabelTextRequest.Feature]
        TEXT_CLASSIFICATION: _ClassVar[LabelTextRequest.Feature]
        TEXT_ENTITY_EXTRACTION: _ClassVar[LabelTextRequest.Feature]
    FEATURE_UNSPECIFIED: LabelTextRequest.Feature
    TEXT_CLASSIFICATION: LabelTextRequest.Feature
    TEXT_ENTITY_EXTRACTION: LabelTextRequest.Feature
    TEXT_CLASSIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_ENTITY_EXTRACTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    text_classification_config: _human_annotation_config_pb2.TextClassificationConfig
    text_entity_extraction_config: _human_annotation_config_pb2.TextEntityExtractionConfig
    parent: str
    basic_config: _human_annotation_config_pb2.HumanAnnotationConfig
    feature: LabelTextRequest.Feature

    def __init__(self, text_classification_config: _Optional[_Union[_human_annotation_config_pb2.TextClassificationConfig, _Mapping]]=..., text_entity_extraction_config: _Optional[_Union[_human_annotation_config_pb2.TextEntityExtractionConfig, _Mapping]]=..., parent: _Optional[str]=..., basic_config: _Optional[_Union[_human_annotation_config_pb2.HumanAnnotationConfig, _Mapping]]=..., feature: _Optional[_Union[LabelTextRequest.Feature, str]]=...) -> None:
        ...

class GetExampleRequest(_message.Message):
    __slots__ = ('name', 'filter')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str

    def __init__(self, name: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListExamplesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListExamplesResponse(_message.Message):
    __slots__ = ('examples', 'next_page_token')
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.Example]
    next_page_token: str

    def __init__(self, examples: _Optional[_Iterable[_Union[_dataset_pb2.Example, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateAnnotationSpecSetRequest(_message.Message):
    __slots__ = ('parent', 'annotation_spec_set')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_SET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    annotation_spec_set: _annotation_spec_set_pb2.AnnotationSpecSet

    def __init__(self, parent: _Optional[str]=..., annotation_spec_set: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpecSet, _Mapping]]=...) -> None:
        ...

class GetAnnotationSpecSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAnnotationSpecSetsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAnnotationSpecSetsResponse(_message.Message):
    __slots__ = ('annotation_spec_sets', 'next_page_token')
    ANNOTATION_SPEC_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_sets: _containers.RepeatedCompositeFieldContainer[_annotation_spec_set_pb2.AnnotationSpecSet]
    next_page_token: str

    def __init__(self, annotation_spec_sets: _Optional[_Iterable[_Union[_annotation_spec_set_pb2.AnnotationSpecSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteAnnotationSpecSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstructionRequest(_message.Message):
    __slots__ = ('parent', 'instruction')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instruction: _instruction_pb2.Instruction

    def __init__(self, parent: _Optional[str]=..., instruction: _Optional[_Union[_instruction_pb2.Instruction, _Mapping]]=...) -> None:
        ...

class GetInstructionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteInstructionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListInstructionsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListInstructionsResponse(_message.Message):
    __slots__ = ('instructions', 'next_page_token')
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    instructions: _containers.RepeatedCompositeFieldContainer[_instruction_pb2.Instruction]
    next_page_token: str

    def __init__(self, instructions: _Optional[_Iterable[_Union[_instruction_pb2.Instruction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEvaluationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SearchEvaluationsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchEvaluationsResponse(_message.Message):
    __slots__ = ('evaluations', 'next_page_token')
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    evaluations: _containers.RepeatedCompositeFieldContainer[_evaluation_pb2.Evaluation]
    next_page_token: str

    def __init__(self, evaluations: _Optional[_Iterable[_Union[_evaluation_pb2.Evaluation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchExampleComparisonsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchExampleComparisonsResponse(_message.Message):
    __slots__ = ('example_comparisons', 'next_page_token')

    class ExampleComparison(_message.Message):
        __slots__ = ('ground_truth_example', 'model_created_examples')
        GROUND_TRUTH_EXAMPLE_FIELD_NUMBER: _ClassVar[int]
        MODEL_CREATED_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
        ground_truth_example: _dataset_pb2.Example
        model_created_examples: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.Example]

        def __init__(self, ground_truth_example: _Optional[_Union[_dataset_pb2.Example, _Mapping]]=..., model_created_examples: _Optional[_Iterable[_Union[_dataset_pb2.Example, _Mapping]]]=...) -> None:
            ...
    EXAMPLE_COMPARISONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    example_comparisons: _containers.RepeatedCompositeFieldContainer[SearchExampleComparisonsResponse.ExampleComparison]
    next_page_token: str

    def __init__(self, example_comparisons: _Optional[_Iterable[_Union[SearchExampleComparisonsResponse.ExampleComparison, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateEvaluationJobRequest(_message.Message):
    __slots__ = ('parent', 'job')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    job: _evaluation_job_pb2.EvaluationJob

    def __init__(self, parent: _Optional[str]=..., job: _Optional[_Union[_evaluation_job_pb2.EvaluationJob, _Mapping]]=...) -> None:
        ...

class UpdateEvaluationJobRequest(_message.Message):
    __slots__ = ('evaluation_job', 'update_mask')
    EVALUATION_JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    evaluation_job: _evaluation_job_pb2.EvaluationJob
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, evaluation_job: _Optional[_Union[_evaluation_job_pb2.EvaluationJob, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetEvaluationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PauseEvaluationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ResumeEvaluationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteEvaluationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEvaluationJobsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEvaluationJobsResponse(_message.Message):
    __slots__ = ('evaluation_jobs', 'next_page_token')
    EVALUATION_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    evaluation_jobs: _containers.RepeatedCompositeFieldContainer[_evaluation_job_pb2.EvaluationJob]
    next_page_token: str

    def __init__(self, evaluation_jobs: _Optional[_Iterable[_Union[_evaluation_job_pb2.EvaluationJob, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...