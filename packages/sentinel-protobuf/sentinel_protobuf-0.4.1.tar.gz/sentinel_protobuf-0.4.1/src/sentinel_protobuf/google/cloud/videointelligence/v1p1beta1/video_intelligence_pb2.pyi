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
    SPEECH_TRANSCRIPTION: _ClassVar[Feature]

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
SPEECH_TRANSCRIPTION: Feature
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
    __slots__ = ('segments', 'label_detection_config', 'shot_change_detection_config', 'explicit_content_detection_config', 'speech_transcription_config')
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    LABEL_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SHOT_CHANGE_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_CONTENT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPEECH_TRANSCRIPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[VideoSegment]
    label_detection_config: LabelDetectionConfig
    shot_change_detection_config: ShotChangeDetectionConfig
    explicit_content_detection_config: ExplicitContentDetectionConfig
    speech_transcription_config: SpeechTranscriptionConfig

    def __init__(self, segments: _Optional[_Iterable[_Union[VideoSegment, _Mapping]]]=..., label_detection_config: _Optional[_Union[LabelDetectionConfig, _Mapping]]=..., shot_change_detection_config: _Optional[_Union[ShotChangeDetectionConfig, _Mapping]]=..., explicit_content_detection_config: _Optional[_Union[ExplicitContentDetectionConfig, _Mapping]]=..., speech_transcription_config: _Optional[_Union[SpeechTranscriptionConfig, _Mapping]]=...) -> None:
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

class VideoAnnotationResults(_message.Message):
    __slots__ = ('input_uri', 'segment_label_annotations', 'shot_label_annotations', 'frame_label_annotations', 'shot_annotations', 'explicit_annotation', 'speech_transcriptions', 'error')
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOT_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    FRAME_LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    SPEECH_TRANSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    input_uri: str
    segment_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    shot_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    frame_label_annotations: _containers.RepeatedCompositeFieldContainer[LabelAnnotation]
    shot_annotations: _containers.RepeatedCompositeFieldContainer[VideoSegment]
    explicit_annotation: ExplicitContentAnnotation
    speech_transcriptions: _containers.RepeatedCompositeFieldContainer[SpeechTranscription]
    error: _status_pb2.Status

    def __init__(self, input_uri: _Optional[str]=..., segment_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., shot_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., frame_label_annotations: _Optional[_Iterable[_Union[LabelAnnotation, _Mapping]]]=..., shot_annotations: _Optional[_Iterable[_Union[VideoSegment, _Mapping]]]=..., explicit_annotation: _Optional[_Union[ExplicitContentAnnotation, _Mapping]]=..., speech_transcriptions: _Optional[_Iterable[_Union[SpeechTranscription, _Mapping]]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
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

class SpeechTranscriptionConfig(_message.Message):
    __slots__ = ('language_code', 'max_alternatives', 'filter_profanity', 'speech_contexts', 'enable_automatic_punctuation', 'audio_tracks')
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    MAX_ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    FILTER_PROFANITY_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTOMATIC_PUNCTUATION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TRACKS_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    max_alternatives: int
    filter_profanity: bool
    speech_contexts: _containers.RepeatedCompositeFieldContainer[SpeechContext]
    enable_automatic_punctuation: bool
    audio_tracks: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, language_code: _Optional[str]=..., max_alternatives: _Optional[int]=..., filter_profanity: bool=..., speech_contexts: _Optional[_Iterable[_Union[SpeechContext, _Mapping]]]=..., enable_automatic_punctuation: bool=..., audio_tracks: _Optional[_Iterable[int]]=...) -> None:
        ...

class SpeechContext(_message.Message):
    __slots__ = ('phrases',)
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    phrases: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, phrases: _Optional[_Iterable[str]]=...) -> None:
        ...

class SpeechTranscription(_message.Message):
    __slots__ = ('alternatives',)
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    alternatives: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionAlternative]

    def __init__(self, alternatives: _Optional[_Iterable[_Union[SpeechRecognitionAlternative, _Mapping]]]=...) -> None:
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
    __slots__ = ('start_time', 'end_time', 'word')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    WORD_FIELD_NUMBER: _ClassVar[int]
    start_time: _duration_pb2.Duration
    end_time: _duration_pb2.Duration
    word: str

    def __init__(self, start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., word: _Optional[str]=...) -> None:
        ...