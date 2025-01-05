from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEATURE_UNSPECIFIED: _ClassVar[Feature]
    LABEL_DETECTION: _ClassVar[Feature]
    SHOT_CHANGE_DETECTION: _ClassVar[Feature]
    EXPLICIT_CONTENT_DETECTION: _ClassVar[Feature]
    TEXT_DETECTION: _ClassVar[Feature]
    OBJECT_TRACKING: _ClassVar[Feature]

class LabelDetectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LABEL_DETECTION_MODE_UNSPECIFIED: _ClassVar[LabelDetectionMode]
    SHOT_MODE: _ClassVar[LabelDetectionMode]
    FRAME_MODE: _ClassVar[LabelDetectionMode]
    SHOT_AND_FRAME_MODE: _ClassVar[LabelDetectionMode]

class Likelihood(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIKELIHOOD_UNSPECIFIED: _ClassVar[Likelihood]
    VERY_UNLIKELY: _ClassVar[Likelihood]
    UNLIKELY: _ClassVar[Likelihood]
    POSSIBLE: _ClassVar[Likelihood]
    LIKELY: _ClassVar[Likelihood]
    VERY_LIKELY: _ClassVar[Likelihood]
FEATURE_UNSPECIFIED: Feature
LABEL_DETECTION: Feature
SHOT_CHANGE_DETECTION: Feature
EXPLICIT_CONTENT_DETECTION: Feature
TEXT_DETECTION: Feature
OBJECT_TRACKING: Feature
LABEL_DETECTION_MODE_UNSPECIFIED: LabelDetectionMode
SHOT_MODE: LabelDetectionMode
FRAME_MODE: LabelDetectionMode
SHOT_AND_FRAME_MODE: LabelDetectionMode
LIKELIHOOD_UNSPECIFIED: Likelihood
VERY_UNLIKELY: Likelihood
UNLIKELY: Likelihood
POSSIBLE: Likelihood
LIKELY: Likelihood
VERY_LIKELY: Likelihood

class AnnotateVideoRequest(_message.Message):
    __slots__ = ('input_uri', 'input_content', 'features', 'video_context', 'output_uri', 'location_id')
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    input_uri: str
    input_content: bytes
    features: _containers.RepeatedScalarFieldContainer[Feature]
    video_context: VideoContext
    output_uri: str
    location_id: str

    def __init__(self, input_uri: _Optional[str]=..., input_content: _Optional[bytes]=..., features: _Optional[_Iterable[_Union[Feature, str]]]=..., video_context: _Optional[_Union[VideoContext, _Mapping]]=..., output_uri: _Optional[str]=..., location_id: _Optional[str]=...) -> None:
        ...

class VideoContext(_message.Message):
    __slots__ = ('segments', 'label_detection_config', 'shot_change_detection_config', 'explicit_content_detection_config', 'text_detection_config')
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    LABEL_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SHOT_CHANGE_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_CONTENT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[VideoSegment]
    label_detection_config: LabelDetectionConfig
    shot_change_detection_config: ShotChangeDetectionConfig
    explicit_content_detection_config: ExplicitContentDetectionConfig
    text_detection_config: TextDetectionConfig

    def __init__(self, segments: _Optional[_Iterable[_Union[VideoSegment, _Mapping]]]=..., label_detection_config: _Optional[_Union[LabelDetectionConfig, _Mapping]]=..., shot_change_detection_config: _Optional[_Union[ShotChangeDetectionConfig, _Mapping]]=..., explicit_content_detection_config: _Optional[_Union[ExplicitContentDetectionConfig, _Mapping]]=..., text_detection_config: _Optional[_Union[TextDetectionConfig, _Mapping]]=...) -> None:
        ...

class LabelDetectionConfig(_message.Message):
    __slots__ = ('label_detection_mode', 'stationary_camera', 'model')
    LABEL_DETECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    STATIONARY_CAMERA_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    label_detection_mode: LabelDetectionMode
    stationary_camera: bool
    model: str

    def __init__(self, label_detection_mode: _Optional[_Union[LabelDetectionMode, str]]=..., stationary_camera: bool=..., model: _Optional[str]=...) -> None:
        ...

class ShotChangeDetectionConfig(_message.Message):
    __slots__ = ('model',)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str

    def __init__(self, model: _Optional[str]=...) -> None:
        ...

class ExplicitContentDetectionConfig(_message.Message):
    __slots__ = ('model',)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str

    def __init__(self, model: _Optional[str]=...) -> None:
        ...

class TextDetectionConfig(_message.Message):
    __slots__ = ('language_hints',)
    LANGUAGE_HINTS_FIELD_NUMBER: _ClassVar[int]
    language_hints: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, language_hints: _Optional[_Iterable[str]]=...) -> None:
        ...

class VideoSegment(_message.Message):
    __slots__ = ('start_time_offset', 'end_time_offset')
    START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    start_time_offset: _duration_pb2.Duration
    end_time_offset: _duration_pb2.Duration

    def __init__(self, start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class LabelSegment(_message.Message):
    __slots__ = ('segment', 'confidence')
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    segment: VideoSegment
    confidence: float

    def __init__(self, segment: _Optional[_Union[VideoSegment, _Mapping]]=..., confidence: _Optional[float]=...) -> None:
        ...

class LabelFrame(_message.Message):
    __slots__ = ('time_offset', 'confidence')
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    time_offset: _duration_pb2.Duration
    confidence: float

    def __init__(self, time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., confidence: _Optional[float]=...) -> None:
        ...

class Entity(_message.Message):
    __slots__ = ('entity_id', 'description', 'language_code')
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    entity_id: str
    description: str
    language_code: str

    def __init__(self, entity_id: _Optional[str]=..., description: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class LabelAnnotation(_message.Message):
    __slots__ = ('entity', 'category_entities', 'segments', 'frames')
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    entity: Entity
    category_entities: _containers.RepeatedCompositeFieldContainer[Entity]
    segments: _containers.RepeatedCompositeFieldContainer[LabelSegment]
    frames: _containers.RepeatedCompositeFieldContainer[LabelFrame]

    def __init__(self, entity: _Optional[_Union[Entity, _Mapping]]=..., category_entities: _Optional[_Iterable[_Union[Entity, _Mapping]]]=..., segments: _Optional[_Iterable[_Union[LabelSegment, _Mapping]]]=..., frames: _Optional[_Iterable[_Union[LabelFrame, _Mapping]]]=...) -> None:
        ...

class ExplicitContentFrame(_message.Message):
    __slots__ = ('time_offset', 'pornography_likelihood')
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    PORNOGRAPHY_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    time_offset: _duration_pb2.Duration
    pornography_likelihood: Likelihood

    def __init__(self, time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., pornography_likelihood: _Optional[_Union[Likelihood, str]]=...) -> None:
        ...

class ExplicitContentAnnotation(_message.Message):
    __slots__ = ('frames',)
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedCompositeFieldContainer[ExplicitContentFrame]

    def __init__(self, frames: _Optional[_Iterable[_Union[ExplicitContentFrame, _Mapping]]]=...) -> None:
        ...

class NormalizedBoundingBox(_message.Message):
    __slots__ = ('left', 'top', 'right', 'bottom')
    LEFT_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_FIELD_NUMBER: _ClassVar[int]
    left: float
    top: float
    right: float
    bottom: float

    def __init__(self, left: _Optional[float]=..., top: _Optional[float]=..., right: _Optional[float]=..., bottom: _Optional[float]=...) -> None:
        ...

class VideoAnnotationResults(_message.Message):
    __slots__ = ('input_uri', 'segment_label_annotations', 'shot_label_annotations', 'frame_label_annotations', 'shot_annotations', 'explicit_annotation', 'text_annotations', 'object_annotations', 'error')
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOT_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    FRAME_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    TEXT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    input_uri: str
    segment_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    shot_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    frame_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    shot_annotations: _containers.RepeatedCompositeFieldContainer[VideoSegment]
    explicit_annotation: ExplicitContentAnnotation
    text_annotations: _containers.RepeatedCompositeFieldContainer[TextAnnotation]
    object_annotations: _containers.RepeatedCompositeFieldContainer[ObjectTrackingAnnotation]
    error: _status_pb2.Status

    def __init__(self, input_uri: _Optional[str]=..., segment_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., shot_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., frame_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., shot_annotations: _Optional[_Iterable[_Union[VideoSegment, _Mapping]]]=..., explicit_annotation: _Optional[_Union[ExplicitContentAnnotation, _Mapping]]=..., text_annotations: _Optional[_Iterable[_Union[TextAnnotation, _Mapping]]]=..., object_annotations: _Optional[_Iterable[_Union[ObjectTrackingAnnotation, _Mapping]]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class AnnotateVideoResponse(_message.Message):
    __slots__ = ('annotation_results',)
    ANNOTATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    annotation_results: _containers.RepeatedCompositeFieldContainer[VideoAnnotationResults]

    def __init__(self, annotation_results: _Optional[_Iterable[_Union[VideoAnnotationResults, _Mapping]]]=...) -> None:
        ...

class VideoAnnotationProgress(_message.Message):
    __slots__ = ('input_uri', 'progress_percent', 'start_time', 'update_time')
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    input_uri: str
    progress_percent: int
    start_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, input_uri: _Optional[str]=..., progress_percent: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AnnotateVideoProgress(_message.Message):
    __slots__ = ('annotation_progress',)
    ANNOTATION_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    annotation_progress: _containers.RepeatedCompositeFieldContainer[VideoAnnotationProgress]

    def __init__(self, annotation_progress: _Optional[_Iterable[_Union[VideoAnnotationProgress, _Mapping]]]=...) -> None:
        ...

class NormalizedVertex(_message.Message):
    __slots__ = ('x', 'y')
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float

    def __init__(self, x: _Optional[float]=..., y: _Optional[float]=...) -> None:
        ...

class NormalizedBoundingPoly(_message.Message):
    __slots__ = ('vertices',)
    VERTICES_FIELD_NUMBER: _ClassVar[int]
    vertices: _containers.RepeatedCompositeFieldContainer[NormalizedVertex]

    def __init__(self, vertices: _Optional[_Iterable[_Union[NormalizedVertex, _Mapping]]]=...) -> None:
        ...

class TextSegment(_message.Message):
    __slots__ = ('segment', 'confidence', 'frames')
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    segment: VideoSegment
    confidence: float
    frames: _containers.RepeatedCompositeFieldContainer[TextFrame]

    def __init__(self, segment: _Optional[_Union[VideoSegment, _Mapping]]=..., confidence: _Optional[float]=..., frames: _Optional[_Iterable[_Union[TextFrame, _Mapping]]]=...) -> None:
        ...

class TextFrame(_message.Message):
    __slots__ = ('rotated_bounding_box', 'time_offset')
    ROTATED_BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    rotated_bounding_box: NormalizedBoundingPoly
    time_offset: _duration_pb2.Duration

    def __init__(self, rotated_bounding_box: _Optional[_Union[NormalizedBoundingPoly, _Mapping]]=..., time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class TextAnnotation(_message.Message):
    __slots__ = ('text', 'segments')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    text: str
    segments: _containers.RepeatedCompositeFieldContainer[TextSegment]

    def __init__(self, text: _Optional[str]=..., segments: _Optional[_Iterable[_Union[TextSegment, _Mapping]]]=...) -> None:
        ...

class ObjectTrackingFrame(_message.Message):
    __slots__ = ('normalized_bounding_box', 'time_offset')
    NORMALIZED_BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    normalized_bounding_box: NormalizedBoundingBox
    time_offset: _duration_pb2.Duration

    def __init__(self, normalized_bounding_box: _Optional[_Union[NormalizedBoundingBox, _Mapping]]=..., time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class ObjectTrackingAnnotation(_message.Message):
    __slots__ = ('segment', 'track_id', 'entity', 'confidence', 'frames')
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    segment: VideoSegment
    track_id: int
    entity: Entity
    confidence: float
    frames: _containers.RepeatedCompositeFieldContainer[ObjectTrackingFrame]

    def __init__(self, segment: _Optional[_Union[VideoSegment, _Mapping]]=..., track_id: _Optional[int]=..., entity: _Optional[_Union[Entity, _Mapping]]=..., confidence: _Optional[float]=..., frames: _Optional[_Iterable[_Union[ObjectTrackingFrame, _Mapping]]]=...) -> None:
        ...