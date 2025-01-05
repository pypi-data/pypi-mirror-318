from google.cloud.datalabeling.v1beta1 import annotation_spec_set_pb2 as _annotation_spec_set_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AnnotationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANNOTATION_SOURCE_UNSPECIFIED: _ClassVar[AnnotationSource]
    OPERATOR: _ClassVar[AnnotationSource]

class AnnotationSentiment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANNOTATION_SENTIMENT_UNSPECIFIED: _ClassVar[AnnotationSentiment]
    NEGATIVE: _ClassVar[AnnotationSentiment]
    POSITIVE: _ClassVar[AnnotationSentiment]

class AnnotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANNOTATION_TYPE_UNSPECIFIED: _ClassVar[AnnotationType]
    IMAGE_CLASSIFICATION_ANNOTATION: _ClassVar[AnnotationType]
    IMAGE_BOUNDING_BOX_ANNOTATION: _ClassVar[AnnotationType]
    IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION: _ClassVar[AnnotationType]
    IMAGE_BOUNDING_POLY_ANNOTATION: _ClassVar[AnnotationType]
    IMAGE_POLYLINE_ANNOTATION: _ClassVar[AnnotationType]
    IMAGE_SEGMENTATION_ANNOTATION: _ClassVar[AnnotationType]
    VIDEO_SHOTS_CLASSIFICATION_ANNOTATION: _ClassVar[AnnotationType]
    VIDEO_OBJECT_TRACKING_ANNOTATION: _ClassVar[AnnotationType]
    VIDEO_OBJECT_DETECTION_ANNOTATION: _ClassVar[AnnotationType]
    VIDEO_EVENT_ANNOTATION: _ClassVar[AnnotationType]
    TEXT_CLASSIFICATION_ANNOTATION: _ClassVar[AnnotationType]
    TEXT_ENTITY_EXTRACTION_ANNOTATION: _ClassVar[AnnotationType]
    GENERAL_CLASSIFICATION_ANNOTATION: _ClassVar[AnnotationType]
ANNOTATION_SOURCE_UNSPECIFIED: AnnotationSource
OPERATOR: AnnotationSource
ANNOTATION_SENTIMENT_UNSPECIFIED: AnnotationSentiment
NEGATIVE: AnnotationSentiment
POSITIVE: AnnotationSentiment
ANNOTATION_TYPE_UNSPECIFIED: AnnotationType
IMAGE_CLASSIFICATION_ANNOTATION: AnnotationType
IMAGE_BOUNDING_BOX_ANNOTATION: AnnotationType
IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION: AnnotationType
IMAGE_BOUNDING_POLY_ANNOTATION: AnnotationType
IMAGE_POLYLINE_ANNOTATION: AnnotationType
IMAGE_SEGMENTATION_ANNOTATION: AnnotationType
VIDEO_SHOTS_CLASSIFICATION_ANNOTATION: AnnotationType
VIDEO_OBJECT_TRACKING_ANNOTATION: AnnotationType
VIDEO_OBJECT_DETECTION_ANNOTATION: AnnotationType
VIDEO_EVENT_ANNOTATION: AnnotationType
TEXT_CLASSIFICATION_ANNOTATION: AnnotationType
TEXT_ENTITY_EXTRACTION_ANNOTATION: AnnotationType
GENERAL_CLASSIFICATION_ANNOTATION: AnnotationType

class Annotation(_message.Message):
    __slots__ = ('name', 'annotation_source', 'annotation_value', 'annotation_metadata', 'annotation_sentiment')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    annotation_source: AnnotationSource
    annotation_value: AnnotationValue
    annotation_metadata: AnnotationMetadata
    annotation_sentiment: AnnotationSentiment

    def __init__(self, name: _Optional[str]=..., annotation_source: _Optional[_Union[AnnotationSource, str]]=..., annotation_value: _Optional[_Union[AnnotationValue, _Mapping]]=..., annotation_metadata: _Optional[_Union[AnnotationMetadata, _Mapping]]=..., annotation_sentiment: _Optional[_Union[AnnotationSentiment, str]]=...) -> None:
        ...

class AnnotationValue(_message.Message):
    __slots__ = ('image_classification_annotation', 'image_bounding_poly_annotation', 'image_polyline_annotation', 'image_segmentation_annotation', 'text_classification_annotation', 'text_entity_extraction_annotation', 'video_classification_annotation', 'video_object_tracking_annotation', 'video_event_annotation')
    IMAGE_CLASSIFICATION_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BOUNDING_POLY_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_POLYLINE_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_SEGMENTATION_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    TEXT_CLASSIFICATION_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    TEXT_ENTITY_EXTRACTION_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CLASSIFICATION_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_OBJECT_TRACKING_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EVENT_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    image_classification_annotation: ImageClassificationAnnotation
    image_bounding_poly_annotation: ImageBoundingPolyAnnotation
    image_polyline_annotation: ImagePolylineAnnotation
    image_segmentation_annotation: ImageSegmentationAnnotation
    text_classification_annotation: TextClassificationAnnotation
    text_entity_extraction_annotation: TextEntityExtractionAnnotation
    video_classification_annotation: VideoClassificationAnnotation
    video_object_tracking_annotation: VideoObjectTrackingAnnotation
    video_event_annotation: VideoEventAnnotation

    def __init__(self, image_classification_annotation: _Optional[_Union[ImageClassificationAnnotation, _Mapping]]=..., image_bounding_poly_annotation: _Optional[_Union[ImageBoundingPolyAnnotation, _Mapping]]=..., image_polyline_annotation: _Optional[_Union[ImagePolylineAnnotation, _Mapping]]=..., image_segmentation_annotation: _Optional[_Union[ImageSegmentationAnnotation, _Mapping]]=..., text_classification_annotation: _Optional[_Union[TextClassificationAnnotation, _Mapping]]=..., text_entity_extraction_annotation: _Optional[_Union[TextEntityExtractionAnnotation, _Mapping]]=..., video_classification_annotation: _Optional[_Union[VideoClassificationAnnotation, _Mapping]]=..., video_object_tracking_annotation: _Optional[_Union[VideoObjectTrackingAnnotation, _Mapping]]=..., video_event_annotation: _Optional[_Union[VideoEventAnnotation, _Mapping]]=...) -> None:
        ...

class ImageClassificationAnnotation(_message.Message):
    __slots__ = ('annotation_spec',)
    ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    annotation_spec: _annotation_spec_set_pb2.AnnotationSpec

    def __init__(self, annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=...) -> None:
        ...

class Vertex(_message.Message):
    __slots__ = ('x', 'y')
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int

    def __init__(self, x: _Optional[int]=..., y: _Optional[int]=...) -> None:
        ...

class NormalizedVertex(_message.Message):
    __slots__ = ('x', 'y')
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float

    def __init__(self, x: _Optional[float]=..., y: _Optional[float]=...) -> None:
        ...

class BoundingPoly(_message.Message):
    __slots__ = ('vertices',)
    VERTICES_FIELD_NUMBER: _ClassVar[int]
    vertices: _containers.RepeatedCompositeFieldContainer[Vertex]

    def __init__(self, vertices: _Optional[_Iterable[_Union[Vertex, _Mapping]]]=...) -> None:
        ...

class NormalizedBoundingPoly(_message.Message):
    __slots__ = ('normalized_vertices',)
    NORMALIZED_VERTICES_FIELD_NUMBER: _ClassVar[int]
    normalized_vertices: _containers.RepeatedCompositeFieldContainer[NormalizedVertex]

    def __init__(self, normalized_vertices: _Optional[_Iterable[_Union[NormalizedVertex, _Mapping]]]=...) -> None:
        ...

class ImageBoundingPolyAnnotation(_message.Message):
    __slots__ = ('bounding_poly', 'normalized_bounding_poly', 'annotation_spec')
    BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    bounding_poly: BoundingPoly
    normalized_bounding_poly: NormalizedBoundingPoly
    annotation_spec: _annotation_spec_set_pb2.AnnotationSpec

    def __init__(self, bounding_poly: _Optional[_Union[BoundingPoly, _Mapping]]=..., normalized_bounding_poly: _Optional[_Union[NormalizedBoundingPoly, _Mapping]]=..., annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=...) -> None:
        ...

class Polyline(_message.Message):
    __slots__ = ('vertices',)
    VERTICES_FIELD_NUMBER: _ClassVar[int]
    vertices: _containers.RepeatedCompositeFieldContainer[Vertex]

    def __init__(self, vertices: _Optional[_Iterable[_Union[Vertex, _Mapping]]]=...) -> None:
        ...

class NormalizedPolyline(_message.Message):
    __slots__ = ('normalized_vertices',)
    NORMALIZED_VERTICES_FIELD_NUMBER: _ClassVar[int]
    normalized_vertices: _containers.RepeatedCompositeFieldContainer[NormalizedVertex]

    def __init__(self, normalized_vertices: _Optional[_Iterable[_Union[NormalizedVertex, _Mapping]]]=...) -> None:
        ...

class ImagePolylineAnnotation(_message.Message):
    __slots__ = ('polyline', 'normalized_polyline', 'annotation_spec')
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_POLYLINE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    polyline: Polyline
    normalized_polyline: NormalizedPolyline
    annotation_spec: _annotation_spec_set_pb2.AnnotationSpec

    def __init__(self, polyline: _Optional[_Union[Polyline, _Mapping]]=..., normalized_polyline: _Optional[_Union[NormalizedPolyline, _Mapping]]=..., annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=...) -> None:
        ...

class ImageSegmentationAnnotation(_message.Message):
    __slots__ = ('annotation_colors', 'mime_type', 'image_bytes')

    class AnnotationColorsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _annotation_spec_set_pb2.AnnotationSpec

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=...) -> None:
            ...
    ANNOTATION_COLORS_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    annotation_colors: _containers.MessageMap[str, _annotation_spec_set_pb2.AnnotationSpec]
    mime_type: str
    image_bytes: bytes

    def __init__(self, annotation_colors: _Optional[_Mapping[str, _annotation_spec_set_pb2.AnnotationSpec]]=..., mime_type: _Optional[str]=..., image_bytes: _Optional[bytes]=...) -> None:
        ...

class TextClassificationAnnotation(_message.Message):
    __slots__ = ('annotation_spec',)
    ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    annotation_spec: _annotation_spec_set_pb2.AnnotationSpec

    def __init__(self, annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=...) -> None:
        ...

class TextEntityExtractionAnnotation(_message.Message):
    __slots__ = ('annotation_spec', 'sequential_segment')
    ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SEQUENTIAL_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    annotation_spec: _annotation_spec_set_pb2.AnnotationSpec
    sequential_segment: SequentialSegment

    def __init__(self, annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=..., sequential_segment: _Optional[_Union[SequentialSegment, _Mapping]]=...) -> None:
        ...

class SequentialSegment(_message.Message):
    __slots__ = ('start', 'end')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int

    def __init__(self, start: _Optional[int]=..., end: _Optional[int]=...) -> None:
        ...

class TimeSegment(_message.Message):
    __slots__ = ('start_time_offset', 'end_time_offset')
    START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    start_time_offset: _duration_pb2.Duration
    end_time_offset: _duration_pb2.Duration

    def __init__(self, start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class VideoClassificationAnnotation(_message.Message):
    __slots__ = ('time_segment', 'annotation_spec')
    TIME_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    time_segment: TimeSegment
    annotation_spec: _annotation_spec_set_pb2.AnnotationSpec

    def __init__(self, time_segment: _Optional[_Union[TimeSegment, _Mapping]]=..., annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=...) -> None:
        ...

class ObjectTrackingFrame(_message.Message):
    __slots__ = ('bounding_poly', 'normalized_bounding_poly', 'time_offset')
    BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    bounding_poly: BoundingPoly
    normalized_bounding_poly: NormalizedBoundingPoly
    time_offset: _duration_pb2.Duration

    def __init__(self, bounding_poly: _Optional[_Union[BoundingPoly, _Mapping]]=..., normalized_bounding_poly: _Optional[_Union[NormalizedBoundingPoly, _Mapping]]=..., time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class VideoObjectTrackingAnnotation(_message.Message):
    __slots__ = ('annotation_spec', 'time_segment', 'object_tracking_frames')
    ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TRACKING_FRAMES_FIELD_NUMBER: _ClassVar[int]
    annotation_spec: _annotation_spec_set_pb2.AnnotationSpec
    time_segment: TimeSegment
    object_tracking_frames: _containers.RepeatedCompositeFieldContainer[ObjectTrackingFrame]

    def __init__(self, annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=..., time_segment: _Optional[_Union[TimeSegment, _Mapping]]=..., object_tracking_frames: _Optional[_Iterable[_Union[ObjectTrackingFrame, _Mapping]]]=...) -> None:
        ...

class VideoEventAnnotation(_message.Message):
    __slots__ = ('annotation_spec', 'time_segment')
    ANNOTATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    annotation_spec: _annotation_spec_set_pb2.AnnotationSpec
    time_segment: TimeSegment

    def __init__(self, annotation_spec: _Optional[_Union[_annotation_spec_set_pb2.AnnotationSpec, _Mapping]]=..., time_segment: _Optional[_Union[TimeSegment, _Mapping]]=...) -> None:
        ...

class AnnotationMetadata(_message.Message):
    __slots__ = ('operator_metadata',)
    OPERATOR_METADATA_FIELD_NUMBER: _ClassVar[int]
    operator_metadata: OperatorMetadata

    def __init__(self, operator_metadata: _Optional[_Union[OperatorMetadata, _Mapping]]=...) -> None:
        ...

class OperatorMetadata(_message.Message):
    __slots__ = ('score', 'total_votes', 'label_votes', 'comments')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOTES_FIELD_NUMBER: _ClassVar[int]
    LABEL_VOTES_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    score: float
    total_votes: int
    label_votes: int
    comments: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, score: _Optional[float]=..., total_votes: _Optional[int]=..., label_votes: _Optional[int]=..., comments: _Optional[_Iterable[str]]=...) -> None:
        ...