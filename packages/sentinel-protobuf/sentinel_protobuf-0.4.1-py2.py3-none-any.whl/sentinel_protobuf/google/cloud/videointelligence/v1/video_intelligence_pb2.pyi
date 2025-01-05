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
    FACE_DETECTION: _ClassVar[Feature]
    SPEECH_TRANSCRIPTION: _ClassVar[Feature]
    TEXT_DETECTION: _ClassVar[Feature]
    OBJECT_TRACKING: _ClassVar[Feature]
    LOGO_RECOGNITION: _ClassVar[Feature]
    PERSON_DETECTION: _ClassVar[Feature]

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
FACE_DETECTION: Feature
SPEECH_TRANSCRIPTION: Feature
TEXT_DETECTION: Feature
OBJECT_TRACKING: Feature
LOGO_RECOGNITION: Feature
PERSON_DETECTION: Feature
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
    __slots__ = ('segments', 'label_detection_config', 'shot_change_detection_config', 'explicit_content_detection_config', 'face_detection_config', 'speech_transcription_config', 'text_detection_config', 'person_detection_config', 'object_tracking_config')
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    LABEL_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SHOT_CHANGE_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_CONTENT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FACE_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPEECH_TRANSCRIPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PERSON_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TRACKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[VideoSegment]
    label_detection_config: LabelDetectionConfig
    shot_change_detection_config: ShotChangeDetectionConfig
    explicit_content_detection_config: ExplicitContentDetectionConfig
    face_detection_config: FaceDetectionConfig
    speech_transcription_config: SpeechTranscriptionConfig
    text_detection_config: TextDetectionConfig
    person_detection_config: PersonDetectionConfig
    object_tracking_config: ObjectTrackingConfig

    def __init__(self, segments: _Optional[_Iterable[_Union[VideoSegment, _Mapping]]]=..., label_detection_config: _Optional[_Union[LabelDetectionConfig, _Mapping]]=..., shot_change_detection_config: _Optional[_Union[ShotChangeDetectionConfig, _Mapping]]=..., explicit_content_detection_config: _Optional[_Union[ExplicitContentDetectionConfig, _Mapping]]=..., face_detection_config: _Optional[_Union[FaceDetectionConfig, _Mapping]]=..., speech_transcription_config: _Optional[_Union[SpeechTranscriptionConfig, _Mapping]]=..., text_detection_config: _Optional[_Union[TextDetectionConfig, _Mapping]]=..., person_detection_config: _Optional[_Union[PersonDetectionConfig, _Mapping]]=..., object_tracking_config: _Optional[_Union[ObjectTrackingConfig, _Mapping]]=...) -> None:
        ...

class LabelDetectionConfig(_message.Message):
    __slots__ = ('label_detection_mode', 'stationary_camera', 'model', 'frame_confidence_threshold', 'video_confidence_threshold')
    LABEL_DETECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    STATIONARY_CAMERA_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FRAME_CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    label_detection_mode: LabelDetectionMode
    stationary_camera: bool
    model: str
    frame_confidence_threshold: float
    video_confidence_threshold: float

    def __init__(self, label_detection_mode: _Optional[_Union[LabelDetectionMode, str]]=..., stationary_camera: bool=..., model: _Optional[str]=..., frame_confidence_threshold: _Optional[float]=..., video_confidence_threshold: _Optional[float]=...) -> None:
        ...

class ShotChangeDetectionConfig(_message.Message):
    __slots__ = ('model',)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str

    def __init__(self, model: _Optional[str]=...) -> None:
        ...

class ObjectTrackingConfig(_message.Message):
    __slots__ = ('model',)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str

    def __init__(self, model: _Optional[str]=...) -> None:
        ...

class FaceDetectionConfig(_message.Message):
    __slots__ = ('model', 'include_bounding_boxes', 'include_attributes')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_BOUNDING_BOXES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    model: str
    include_bounding_boxes: bool
    include_attributes: bool

    def __init__(self, model: _Optional[str]=..., include_bounding_boxes: bool=..., include_attributes: bool=...) -> None:
        ...

class PersonDetectionConfig(_message.Message):
    __slots__ = ('include_bounding_boxes', 'include_pose_landmarks', 'include_attributes')
    INCLUDE_BOUNDING_BOXES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_POSE_LANDMARKS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    include_bounding_boxes: bool
    include_pose_landmarks: bool
    include_attributes: bool

    def __init__(self, include_bounding_boxes: bool=..., include_pose_landmarks: bool=..., include_attributes: bool=...) -> None:
        ...

class ExplicitContentDetectionConfig(_message.Message):
    __slots__ = ('model',)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str

    def __init__(self, model: _Optional[str]=...) -> None:
        ...

class TextDetectionConfig(_message.Message):
    __slots__ = ('language_hints', 'model')
    LANGUAGE_HINTS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    language_hints: _containers.RepeatedScalarFieldContainer[str]
    model: str

    def __init__(self, language_hints: _Optional[_Iterable[str]]=..., model: _Optional[str]=...) -> None:
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
    __slots__ = ('entity', 'category_entities', 'segments', 'frames', 'version')
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    entity: Entity
    category_entities: _containers.RepeatedCompositeFieldContainer[Entity]
    segments: _containers.RepeatedCompositeFieldContainer[LabelSegment]
    frames: _containers.RepeatedCompositeFieldContainer[LabelFrame]
    version: str

    def __init__(self, entity: _Optional[_Union[Entity, _Mapping]]=..., category_entities: _Optional[_Iterable[_Union[Entity, _Mapping]]]=..., segments: _Optional[_Iterable[_Union[LabelSegment, _Mapping]]]=..., frames: _Optional[_Iterable[_Union[LabelFrame, _Mapping]]]=..., version: _Optional[str]=...) -> None:
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
    __slots__ = ('frames', 'version')
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedCompositeFieldContainer[ExplicitContentFrame]
    version: str

    def __init__(self, frames: _Optional[_Iterable[_Union[ExplicitContentFrame, _Mapping]]]=..., version: _Optional[str]=...) -> None:
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

class FaceDetectionAnnotation(_message.Message):
    __slots__ = ('tracks', 'thumbnail', 'version')
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    tracks: _containers.RepeatedCompositeFieldContainer[Track]
    thumbnail: bytes
    version: str

    def __init__(self, tracks: _Optional[_Iterable[_Union[Track, _Mapping]]]=..., thumbnail: _Optional[bytes]=..., version: _Optional[str]=...) -> None:
        ...

class PersonDetectionAnnotation(_message.Message):
    __slots__ = ('tracks', 'version')
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    tracks: _containers.RepeatedCompositeFieldContainer[Track]
    version: str

    def __init__(self, tracks: _Optional[_Iterable[_Union[Track, _Mapping]]]=..., version: _Optional[str]=...) -> None:
        ...

class FaceSegment(_message.Message):
    __slots__ = ('segment',)
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    segment: VideoSegment

    def __init__(self, segment: _Optional[_Union[VideoSegment, _Mapping]]=...) -> None:
        ...

class FaceFrame(_message.Message):
    __slots__ = ('normalized_bounding_boxes', 'time_offset')
    NORMALIZED_BOUNDING_BOXES_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    normalized_bounding_boxes: _containers.RepeatedCompositeFieldContainer[NormalizedBoundingBox]
    time_offset: _duration_pb2.Duration

    def __init__(self, normalized_bounding_boxes: _Optional[_Iterable[_Union[NormalizedBoundingBox, _Mapping]]]=..., time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class FaceAnnotation(_message.Message):
    __slots__ = ('thumbnail', 'segments', 'frames')
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    thumbnail: bytes
    segments: _containers.RepeatedCompositeFieldContainer[FaceSegment]
    frames: _containers.RepeatedCompositeFieldContainer[FaceFrame]

    def __init__(self, thumbnail: _Optional[bytes]=..., segments: _Optional[_Iterable[_Union[FaceSegment, _Mapping]]]=..., frames: _Optional[_Iterable[_Union[FaceFrame, _Mapping]]]=...) -> None:
        ...

class TimestampedObject(_message.Message):
    __slots__ = ('normalized_bounding_box', 'time_offset', 'attributes', 'landmarks')
    NORMALIZED_BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    LANDMARKS_FIELD_NUMBER: _ClassVar[int]
    normalized_bounding_box: NormalizedBoundingBox
    time_offset: _duration_pb2.Duration
    attributes: _containers.RepeatedCompositeFieldContainer[DetectedAttribute]
    landmarks: _containers.RepeatedCompositeFieldContainer[DetectedLandmark]

    def __init__(self, normalized_bounding_box: _Optional[_Union[NormalizedBoundingBox, _Mapping]]=..., time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., attributes: _Optional[_Iterable[_Union[DetectedAttribute, _Mapping]]]=..., landmarks: _Optional[_Iterable[_Union[DetectedLandmark, _Mapping]]]=...) -> None:
        ...

class Track(_message.Message):
    __slots__ = ('segment', 'timestamped_objects', 'attributes', 'confidence')
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    segment: VideoSegment
    timestamped_objects: _containers.RepeatedCompositeFieldContainer[TimestampedObject]
    attributes: _containers.RepeatedCompositeFieldContainer[DetectedAttribute]
    confidence: float

    def __init__(self, segment: _Optional[_Union[VideoSegment, _Mapping]]=..., timestamped_objects: _Optional[_Iterable[_Union[TimestampedObject, _Mapping]]]=..., attributes: _Optional[_Iterable[_Union[DetectedAttribute, _Mapping]]]=..., confidence: _Optional[float]=...) -> None:
        ...

class DetectedAttribute(_message.Message):
    __slots__ = ('name', 'confidence', 'value')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    confidence: float
    value: str

    def __init__(self, name: _Optional[str]=..., confidence: _Optional[float]=..., value: _Optional[str]=...) -> None:
        ...

class DetectedLandmark(_message.Message):
    __slots__ = ('name', 'point', 'confidence')
    NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    point: NormalizedVertex
    confidence: float

    def __init__(self, name: _Optional[str]=..., point: _Optional[_Union[NormalizedVertex, _Mapping]]=..., confidence: _Optional[float]=...) -> None:
        ...

class VideoAnnotationResults(_message.Message):
    __slots__ = ('input_uri', 'segment', 'segment_label_annotations', 'segment_presence_label_annotations', 'shot_label_annotations', 'shot_presence_label_annotations', 'frame_label_annotations', 'face_annotations', 'face_detection_annotations', 'shot_annotations', 'explicit_annotation', 'speech_transcriptions', 'text_annotations', 'object_annotations', 'logo_recognition_annotations', 'person_detection_annotations', 'error')
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_PRESENCE_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOT_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOT_PRESENCE_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    FRAME_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    FACE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    FACE_DETECTION_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    SPEECH_TRANSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    TEXT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LOGO_RECOGNITION_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    PERSON_DETECTION_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    input_uri: str
    segment: VideoSegment
    segment_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    segment_presence_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    shot_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    shot_presence_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    frame_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    face_annotations: _containers.RepeatedCompositeFieldContainer[FaceAnnotation]
    face_detection_annotations: _containers.RepeatedCompositeFieldContainer[FaceDetectionAnnotation]
    shot_annotations: _containers.RepeatedCompositeFieldContainer[VideoSegment]
    explicit_annotation: ExplicitContentAnnotation
    speech_transcriptions: _containers.RepeatedCompositeFieldContainer[SpeechTranscription]
    text_annotations: _containers.RepeatedCompositeFieldContainer[TextAnnotation]
    object_annotations: _containers.RepeatedCompositeFieldContainer[ObjectTrackingAnnotation]
    logo_recognition_annotations: _containers.RepeatedCompositeFieldContainer[LogoRecognitionAnnotation]
    person_detection_annotations: _containers.RepeatedCompositeFieldContainer[PersonDetectionAnnotation]
    error: _status_pb2.Status

    def __init__(self, input_uri: _Optional[str]=..., segment: _Optional[_Union[VideoSegment, _Mapping]]=..., segment_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., segment_presence_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., shot_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., shot_presence_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., frame_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., face_annotations: _Optional[_Iterable[_Union[FaceAnnotation, _Mapping]]]=..., face_detection_annotations: _Optional[_Iterable[_Union[FaceDetectionAnnotation, _Mapping]]]=..., shot_annotations: _Optional[_Iterable[_Union[VideoSegment, _Mapping]]]=..., explicit_annotation: _Optional[_Union[ExplicitContentAnnotation, _Mapping]]=..., speech_transcriptions: _Optional[_Iterable[_Union[SpeechTranscription, _Mapping]]]=..., text_annotations: _Optional[_Iterable[_Union[TextAnnotation, _Mapping]]]=..., object_annotations: _Optional[_Iterable[_Union[ObjectTrackingAnnotation, _Mapping]]]=..., logo_recognition_annotations: _Optional[_Iterable[_Union[LogoRecognitionAnnotation, _Mapping]]]=..., person_detection_annotations: _Optional[_Iterable[_Union[PersonDetectionAnnotation, _Mapping]]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class AnnotateVideoResponse(_message.Message):
    __slots__ = ('annotation_results',)
    ANNOTATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    annotation_results: _containers.RepeatedCompositeFieldContainer[VideoAnnotationResults]

    def __init__(self, annotation_results: _Optional[_Iterable[_Union[VideoAnnotationResults, _Mapping]]]=...) -> None:
        ...

class VideoAnnotationProgress(_message.Message):
    __slots__ = ('input_uri', 'progress_percent', 'start_time', 'update_time', 'feature', 'segment')
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    input_uri: str
    progress_percent: int
    start_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    feature: Feature
    segment: VideoSegment

    def __init__(self, input_uri: _Optional[str]=..., progress_percent: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., feature: _Optional[_Union[Feature, str]]=..., segment: _Optional[_Union[VideoSegment, _Mapping]]=...) -> None:
        ...

class AnnotateVideoProgress(_message.Message):
    __slots__ = ('annotation_progress',)
    ANNOTATION_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    annotation_progress: _containers.RepeatedCompositeFieldContainer[VideoAnnotationProgress]

    def __init__(self, annotation_progress: _Optional[_Iterable[_Union[VideoAnnotationProgress, _Mapping]]]=...) -> None:
        ...

class SpeechTranscriptionConfig(_message.Message):
    __slots__ = ('language_code', 'max_alternatives', 'filter_profanity', 'speech_contexts', 'enable_automatic_punctuation', 'audio_tracks', 'enable_speaker_diarization', 'diarization_speaker_count', 'enable_word_confidence')
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    MAX_ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    FILTER_PROFANITY_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTOMATIC_PUNCTUATION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TRACKS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SPEAKER_DIARIZATION_FIELD_NUMBER: _ClassVar[int]
    DIARIZATION_SPEAKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    max_alternatives: int
    filter_profanity: bool
    speech_contexts: _containers.RepeatedCompositeFieldContainer[SpeechContext]
    enable_automatic_punctuation: bool
    audio_tracks: _containers.RepeatedScalarFieldContainer[int]
    enable_speaker_diarization: bool
    diarization_speaker_count: int
    enable_word_confidence: bool

    def __init__(self, language_code: _Optional[str]=..., max_alternatives: _Optional[int]=..., filter_profanity: bool=..., speech_contexts: _Optional[_Iterable[_Union[SpeechContext, _Mapping]]]=..., enable_automatic_punctuation: bool=..., audio_tracks: _Optional[_Iterable[int]]=..., enable_speaker_diarization: bool=..., diarization_speaker_count: _Optional[int]=..., enable_word_confidence: bool=...) -> None:
        ...

class SpeechContext(_message.Message):
    __slots__ = ('phrases',)
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    phrases: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, phrases: _Optional[_Iterable[str]]=...) -> None:
        ...

class SpeechTranscription(_message.Message):
    __slots__ = ('alternatives', 'language_code')
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    alternatives: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionAlternative]
    language_code: str

    def __init__(self, alternatives: _Optional[_Iterable[_Union[SpeechRecognitionAlternative, _Mapping]]]=..., language_code: _Optional[str]=...) -> None:
        ...

class SpeechRecognitionAlternative(_message.Message):
    __slots__ = ('transcript', 'confidence', 'words')
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    transcript: str
    confidence: float
    words: _containers.RepeatedCompositeFieldContainer[WordInfo]

    def __init__(self, transcript: _Optional[str]=..., confidence: _Optional[float]=..., words: _Optional[_Iterable[_Union[WordInfo, _Mapping]]]=...) -> None:
        ...

class WordInfo(_message.Message):
    __slots__ = ('start_time', 'end_time', 'word', 'confidence', 'speaker_tag')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    WORD_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_TAG_FIELD_NUMBER: _ClassVar[int]
    start_time: _duration_pb2.Duration
    end_time: _duration_pb2.Duration
    word: str
    confidence: float
    speaker_tag: int

    def __init__(self, start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., word: _Optional[str]=..., confidence: _Optional[float]=..., speaker_tag: _Optional[int]=...) -> None:
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
    __slots__ = ('text', 'segments', 'version')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    text: str
    segments: _containers.RepeatedCompositeFieldContainer[TextSegment]
    version: str

    def __init__(self, text: _Optional[str]=..., segments: _Optional[_Iterable[_Union[TextSegment, _Mapping]]]=..., version: _Optional[str]=...) -> None:
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
    __slots__ = ('segment', 'track_id', 'entity', 'confidence', 'frames', 'version')
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    segment: VideoSegment
    track_id: int
    entity: Entity
    confidence: float
    frames: _containers.RepeatedCompositeFieldContainer[ObjectTrackingFrame]
    version: str

    def __init__(self, segment: _Optional[_Union[VideoSegment, _Mapping]]=..., track_id: _Optional[int]=..., entity: _Optional[_Union[Entity, _Mapping]]=..., confidence: _Optional[float]=..., frames: _Optional[_Iterable[_Union[ObjectTrackingFrame, _Mapping]]]=..., version: _Optional[str]=...) -> None:
        ...

class LogoRecognitionAnnotation(_message.Message):
    __slots__ = ('entity', 'tracks', 'segments')
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    entity: Entity
    tracks: _containers.RepeatedCompositeFieldContainer[Track]
    segments: _containers.RepeatedCompositeFieldContainer[VideoSegment]

    def __init__(self, entity: _Optional[_Union[Entity, _Mapping]]=..., tracks: _Optional[_Iterable[_Union[Track, _Mapping]]]=..., segments: _Optional[_Iterable[_Union[VideoSegment, _Mapping]]]=...) -> None:
        ...