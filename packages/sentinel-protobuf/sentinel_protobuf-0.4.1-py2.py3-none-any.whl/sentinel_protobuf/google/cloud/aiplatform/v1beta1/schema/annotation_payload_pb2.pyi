from google.cloud.aiplatform.v1beta1.schema import annotation_spec_color_pb2 as _annotation_spec_color_pb2
from google.cloud.aiplatform.v1beta1.schema import geometry_pb2 as _geometry_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImageClassificationAnnotation(_message.Message):
    __slots__ = ('annotation_spec_id', 'display_name')
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_id: str
    display_name: str

    def __init__(self, annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class ImageBoundingBoxAnnotation(_message.Message):
    __slots__ = ('annotation_spec_id', 'display_name', 'x_min', 'x_max', 'y_min', 'y_max')
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    X_MIN_FIELD_NUMBER: _ClassVar[int]
    X_MAX_FIELD_NUMBER: _ClassVar[int]
    Y_MIN_FIELD_NUMBER: _ClassVar[int]
    Y_MAX_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_id: str
    display_name: str
    x_min: float
    x_max: float
    y_min: float
    y_max: float

    def __init__(self, annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=..., x_min: _Optional[float]=..., x_max: _Optional[float]=..., y_min: _Optional[float]=..., y_max: _Optional[float]=...) -> None:
        ...

class ImageSegmentationAnnotation(_message.Message):
    __slots__ = ('mask_annotation', 'polygon_annotation', 'polyline_annotation')

    class MaskAnnotation(_message.Message):
        __slots__ = ('mask_gcs_uri', 'annotation_spec_colors')
        MASK_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        ANNOTATION_SPEC_COLORS_FIELD_NUMBER: _ClassVar[int]
        mask_gcs_uri: str
        annotation_spec_colors: _containers.RepeatedCompositeFieldContainer[_annotation_spec_color_pb2.AnnotationSpecColor]

        def __init__(self, mask_gcs_uri: _Optional[str]=..., annotation_spec_colors: _Optional[_Iterable[_Union[_annotation_spec_color_pb2.AnnotationSpecColor, _Mapping]]]=...) -> None:
            ...

    class PolygonAnnotation(_message.Message):
        __slots__ = ('vertexes', 'annotation_spec_id', 'display_name')
        VERTEXES_FIELD_NUMBER: _ClassVar[int]
        ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        vertexes: _containers.RepeatedCompositeFieldContainer[_geometry_pb2.Vertex]
        annotation_spec_id: str
        display_name: str

        def __init__(self, vertexes: _Optional[_Iterable[_Union[_geometry_pb2.Vertex, _Mapping]]]=..., annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
            ...

    class PolylineAnnotation(_message.Message):
        __slots__ = ('vertexes', 'annotation_spec_id', 'display_name')
        VERTEXES_FIELD_NUMBER: _ClassVar[int]
        ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        vertexes: _containers.RepeatedCompositeFieldContainer[_geometry_pb2.Vertex]
        annotation_spec_id: str
        display_name: str

        def __init__(self, vertexes: _Optional[_Iterable[_Union[_geometry_pb2.Vertex, _Mapping]]]=..., annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
            ...
    MASK_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    POLYGON_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    mask_annotation: ImageSegmentationAnnotation.MaskAnnotation
    polygon_annotation: ImageSegmentationAnnotation.PolygonAnnotation
    polyline_annotation: ImageSegmentationAnnotation.PolylineAnnotation

    def __init__(self, mask_annotation: _Optional[_Union[ImageSegmentationAnnotation.MaskAnnotation, _Mapping]]=..., polygon_annotation: _Optional[_Union[ImageSegmentationAnnotation.PolygonAnnotation, _Mapping]]=..., polyline_annotation: _Optional[_Union[ImageSegmentationAnnotation.PolylineAnnotation, _Mapping]]=...) -> None:
        ...

class TextClassificationAnnotation(_message.Message):
    __slots__ = ('annotation_spec_id', 'display_name')
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    annotation_spec_id: str
    display_name: str

    def __init__(self, annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class TextExtractionAnnotation(_message.Message):
    __slots__ = ('text_segment', 'annotation_spec_id', 'display_name')
    TEXT_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    text_segment: TextSegment
    annotation_spec_id: str
    display_name: str

    def __init__(self, text_segment: _Optional[_Union[TextSegment, _Mapping]]=..., annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class TextSegment(_message.Message):
    __slots__ = ('start_offset', 'end_offset', 'content')
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    start_offset: int
    end_offset: int
    content: str

    def __init__(self, start_offset: _Optional[int]=..., end_offset: _Optional[int]=..., content: _Optional[str]=...) -> None:
        ...

class TextSentimentAnnotation(_message.Message):
    __slots__ = ('sentiment', 'sentiment_max', 'annotation_spec_id', 'display_name')
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_MAX_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    sentiment: int
    sentiment_max: int
    annotation_spec_id: str
    display_name: str

    def __init__(self, sentiment: _Optional[int]=..., sentiment_max: _Optional[int]=..., annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class VideoClassificationAnnotation(_message.Message):
    __slots__ = ('time_segment', 'annotation_spec_id', 'display_name')
    TIME_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    time_segment: TimeSegment
    annotation_spec_id: str
    display_name: str

    def __init__(self, time_segment: _Optional[_Union[TimeSegment, _Mapping]]=..., annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class TimeSegment(_message.Message):
    __slots__ = ('start_time_offset', 'end_time_offset')
    START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    start_time_offset: _duration_pb2.Duration
    end_time_offset: _duration_pb2.Duration

    def __init__(self, start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class VideoObjectTrackingAnnotation(_message.Message):
    __slots__ = ('time_offset', 'x_min', 'x_max', 'y_min', 'y_max', 'instance_id', 'annotation_spec_id', 'display_name')
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    X_MIN_FIELD_NUMBER: _ClassVar[int]
    X_MAX_FIELD_NUMBER: _ClassVar[int]
    Y_MIN_FIELD_NUMBER: _ClassVar[int]
    Y_MAX_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    time_offset: _duration_pb2.Duration
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    instance_id: int
    annotation_spec_id: str
    display_name: str

    def __init__(self, time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., x_min: _Optional[float]=..., x_max: _Optional[float]=..., y_min: _Optional[float]=..., y_max: _Optional[float]=..., instance_id: _Optional[int]=..., annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class VideoActionRecognitionAnnotation(_message.Message):
    __slots__ = ('time_segment', 'annotation_spec_id', 'display_name')
    TIME_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    time_segment: TimeSegment
    annotation_spec_id: str
    display_name: str

    def __init__(self, time_segment: _Optional[_Union[TimeSegment, _Mapping]]=..., annotation_spec_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...