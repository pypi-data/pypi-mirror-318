from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.speech.v1 import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RecognizeRequest(_message.Message):
    __slots__ = ('config', 'audio')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: RecognitionConfig
    audio: RecognitionAudio

    def __init__(self, config: _Optional[_Union[RecognitionConfig, _Mapping]]=..., audio: _Optional[_Union[RecognitionAudio, _Mapping]]=...) -> None:
        ...

class LongRunningRecognizeRequest(_message.Message):
    __slots__ = ('config', 'audio', 'output_config')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: RecognitionConfig
    audio: RecognitionAudio
    output_config: TranscriptOutputConfig

    def __init__(self, config: _Optional[_Union[RecognitionConfig, _Mapping]]=..., audio: _Optional[_Union[RecognitionAudio, _Mapping]]=..., output_config: _Optional[_Union[TranscriptOutputConfig, _Mapping]]=...) -> None:
        ...

class TranscriptOutputConfig(_message.Message):
    __slots__ = ('gcs_uri',)
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    gcs_uri: str

    def __init__(self, gcs_uri: _Optional[str]=...) -> None:
        ...

class StreamingRecognizeRequest(_message.Message):
    __slots__ = ('streaming_config', 'audio_content')
    STREAMING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CONTENT_FIELD_NUMBER: _ClassVar[int]
    streaming_config: StreamingRecognitionConfig
    audio_content: bytes

    def __init__(self, streaming_config: _Optional[_Union[StreamingRecognitionConfig, _Mapping]]=..., audio_content: _Optional[bytes]=...) -> None:
        ...

class StreamingRecognitionConfig(_message.Message):
    __slots__ = ('config', 'single_utterance', 'interim_results', 'enable_voice_activity_events', 'voice_activity_timeout')

    class VoiceActivityTimeout(_message.Message):
        __slots__ = ('speech_start_timeout', 'speech_end_timeout')
        SPEECH_START_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        SPEECH_END_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        speech_start_timeout: _duration_pb2.Duration
        speech_end_timeout: _duration_pb2.Duration

        def __init__(self, speech_start_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., speech_end_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SINGLE_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    INTERIM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VOICE_ACTIVITY_EVENTS_FIELD_NUMBER: _ClassVar[int]
    VOICE_ACTIVITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    config: RecognitionConfig
    single_utterance: bool
    interim_results: bool
    enable_voice_activity_events: bool
    voice_activity_timeout: StreamingRecognitionConfig.VoiceActivityTimeout

    def __init__(self, config: _Optional[_Union[RecognitionConfig, _Mapping]]=..., single_utterance: bool=..., interim_results: bool=..., enable_voice_activity_events: bool=..., voice_activity_timeout: _Optional[_Union[StreamingRecognitionConfig.VoiceActivityTimeout, _Mapping]]=...) -> None:
        ...

class RecognitionConfig(_message.Message):
    __slots__ = ('encoding', 'sample_rate_hertz', 'audio_channel_count', 'enable_separate_recognition_per_channel', 'language_code', 'alternative_language_codes', 'max_alternatives', 'profanity_filter', 'adaptation', 'transcript_normalization', 'speech_contexts', 'enable_word_time_offsets', 'enable_word_confidence', 'enable_automatic_punctuation', 'enable_spoken_punctuation', 'enable_spoken_emojis', 'diarization_config', 'metadata', 'model', 'use_enhanced')

    class AudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCODING_UNSPECIFIED: _ClassVar[RecognitionConfig.AudioEncoding]
        LINEAR16: _ClassVar[RecognitionConfig.AudioEncoding]
        FLAC: _ClassVar[RecognitionConfig.AudioEncoding]
        MULAW: _ClassVar[RecognitionConfig.AudioEncoding]
        AMR: _ClassVar[RecognitionConfig.AudioEncoding]
        AMR_WB: _ClassVar[RecognitionConfig.AudioEncoding]
        OGG_OPUS: _ClassVar[RecognitionConfig.AudioEncoding]
        SPEEX_WITH_HEADER_BYTE: _ClassVar[RecognitionConfig.AudioEncoding]
        MP3: _ClassVar[RecognitionConfig.AudioEncoding]
        WEBM_OPUS: _ClassVar[RecognitionConfig.AudioEncoding]
    ENCODING_UNSPECIFIED: RecognitionConfig.AudioEncoding
    LINEAR16: RecognitionConfig.AudioEncoding
    FLAC: RecognitionConfig.AudioEncoding
    MULAW: RecognitionConfig.AudioEncoding
    AMR: RecognitionConfig.AudioEncoding
    AMR_WB: RecognitionConfig.AudioEncoding
    OGG_OPUS: RecognitionConfig.AudioEncoding
    SPEEX_WITH_HEADER_BYTE: RecognitionConfig.AudioEncoding
    MP3: RecognitionConfig.AudioEncoding
    WEBM_OPUS: RecognitionConfig.AudioEncoding
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SEPARATE_RECOGNITION_PER_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVE_LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    MAX_ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    PROFANITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    ADAPTATION_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_NORMALIZATION_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_TIME_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTOMATIC_PUNCTUATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SPOKEN_PUNCTUATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SPOKEN_EMOJIS_FIELD_NUMBER: _ClassVar[int]
    DIARIZATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    USE_ENHANCED_FIELD_NUMBER: _ClassVar[int]
    encoding: RecognitionConfig.AudioEncoding
    sample_rate_hertz: int
    audio_channel_count: int
    enable_separate_recognition_per_channel: bool
    language_code: str
    alternative_language_codes: _containers.RepeatedScalarFieldContainer[str]
    max_alternatives: int
    profanity_filter: bool
    adaptation: _resource_pb2.SpeechAdaptation
    transcript_normalization: _resource_pb2.TranscriptNormalization
    speech_contexts: _containers.RepeatedCompositeFieldContainer[SpeechContext]
    enable_word_time_offsets: bool
    enable_word_confidence: bool
    enable_automatic_punctuation: bool
    enable_spoken_punctuation: _wrappers_pb2.BoolValue
    enable_spoken_emojis: _wrappers_pb2.BoolValue
    diarization_config: SpeakerDiarizationConfig
    metadata: RecognitionMetadata
    model: str
    use_enhanced: bool

    def __init__(self, encoding: _Optional[_Union[RecognitionConfig.AudioEncoding, str]]=..., sample_rate_hertz: _Optional[int]=..., audio_channel_count: _Optional[int]=..., enable_separate_recognition_per_channel: bool=..., language_code: _Optional[str]=..., alternative_language_codes: _Optional[_Iterable[str]]=..., max_alternatives: _Optional[int]=..., profanity_filter: bool=..., adaptation: _Optional[_Union[_resource_pb2.SpeechAdaptation, _Mapping]]=..., transcript_normalization: _Optional[_Union[_resource_pb2.TranscriptNormalization, _Mapping]]=..., speech_contexts: _Optional[_Iterable[_Union[SpeechContext, _Mapping]]]=..., enable_word_time_offsets: bool=..., enable_word_confidence: bool=..., enable_automatic_punctuation: bool=..., enable_spoken_punctuation: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., enable_spoken_emojis: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., diarization_config: _Optional[_Union[SpeakerDiarizationConfig, _Mapping]]=..., metadata: _Optional[_Union[RecognitionMetadata, _Mapping]]=..., model: _Optional[str]=..., use_enhanced: bool=...) -> None:
        ...

class SpeakerDiarizationConfig(_message.Message):
    __slots__ = ('enable_speaker_diarization', 'min_speaker_count', 'max_speaker_count', 'speaker_tag')
    ENABLE_SPEAKER_DIARIZATION_FIELD_NUMBER: _ClassVar[int]
    MIN_SPEAKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEAKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_TAG_FIELD_NUMBER: _ClassVar[int]
    enable_speaker_diarization: bool
    min_speaker_count: int
    max_speaker_count: int
    speaker_tag: int

    def __init__(self, enable_speaker_diarization: bool=..., min_speaker_count: _Optional[int]=..., max_speaker_count: _Optional[int]=..., speaker_tag: _Optional[int]=...) -> None:
        ...

class RecognitionMetadata(_message.Message):
    __slots__ = ('interaction_type', 'industry_naics_code_of_audio', 'microphone_distance', 'original_media_type', 'recording_device_type', 'recording_device_name', 'original_mime_type', 'audio_topic')

    class InteractionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERACTION_TYPE_UNSPECIFIED: _ClassVar[RecognitionMetadata.InteractionType]
        DISCUSSION: _ClassVar[RecognitionMetadata.InteractionType]
        PRESENTATION: _ClassVar[RecognitionMetadata.InteractionType]
        PHONE_CALL: _ClassVar[RecognitionMetadata.InteractionType]
        VOICEMAIL: _ClassVar[RecognitionMetadata.InteractionType]
        PROFESSIONALLY_PRODUCED: _ClassVar[RecognitionMetadata.InteractionType]
        VOICE_SEARCH: _ClassVar[RecognitionMetadata.InteractionType]
        VOICE_COMMAND: _ClassVar[RecognitionMetadata.InteractionType]
        DICTATION: _ClassVar[RecognitionMetadata.InteractionType]
    INTERACTION_TYPE_UNSPECIFIED: RecognitionMetadata.InteractionType
    DISCUSSION: RecognitionMetadata.InteractionType
    PRESENTATION: RecognitionMetadata.InteractionType
    PHONE_CALL: RecognitionMetadata.InteractionType
    VOICEMAIL: RecognitionMetadata.InteractionType
    PROFESSIONALLY_PRODUCED: RecognitionMetadata.InteractionType
    VOICE_SEARCH: RecognitionMetadata.InteractionType
    VOICE_COMMAND: RecognitionMetadata.InteractionType
    DICTATION: RecognitionMetadata.InteractionType

    class MicrophoneDistance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MICROPHONE_DISTANCE_UNSPECIFIED: _ClassVar[RecognitionMetadata.MicrophoneDistance]
        NEARFIELD: _ClassVar[RecognitionMetadata.MicrophoneDistance]
        MIDFIELD: _ClassVar[RecognitionMetadata.MicrophoneDistance]
        FARFIELD: _ClassVar[RecognitionMetadata.MicrophoneDistance]
    MICROPHONE_DISTANCE_UNSPECIFIED: RecognitionMetadata.MicrophoneDistance
    NEARFIELD: RecognitionMetadata.MicrophoneDistance
    MIDFIELD: RecognitionMetadata.MicrophoneDistance
    FARFIELD: RecognitionMetadata.MicrophoneDistance

    class OriginalMediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORIGINAL_MEDIA_TYPE_UNSPECIFIED: _ClassVar[RecognitionMetadata.OriginalMediaType]
        AUDIO: _ClassVar[RecognitionMetadata.OriginalMediaType]
        VIDEO: _ClassVar[RecognitionMetadata.OriginalMediaType]
    ORIGINAL_MEDIA_TYPE_UNSPECIFIED: RecognitionMetadata.OriginalMediaType
    AUDIO: RecognitionMetadata.OriginalMediaType
    VIDEO: RecognitionMetadata.OriginalMediaType

    class RecordingDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECORDING_DEVICE_TYPE_UNSPECIFIED: _ClassVar[RecognitionMetadata.RecordingDeviceType]
        SMARTPHONE: _ClassVar[RecognitionMetadata.RecordingDeviceType]
        PC: _ClassVar[RecognitionMetadata.RecordingDeviceType]
        PHONE_LINE: _ClassVar[RecognitionMetadata.RecordingDeviceType]
        VEHICLE: _ClassVar[RecognitionMetadata.RecordingDeviceType]
        OTHER_OUTDOOR_DEVICE: _ClassVar[RecognitionMetadata.RecordingDeviceType]
        OTHER_INDOOR_DEVICE: _ClassVar[RecognitionMetadata.RecordingDeviceType]
    RECORDING_DEVICE_TYPE_UNSPECIFIED: RecognitionMetadata.RecordingDeviceType
    SMARTPHONE: RecognitionMetadata.RecordingDeviceType
    PC: RecognitionMetadata.RecordingDeviceType
    PHONE_LINE: RecognitionMetadata.RecordingDeviceType
    VEHICLE: RecognitionMetadata.RecordingDeviceType
    OTHER_OUTDOOR_DEVICE: RecognitionMetadata.RecordingDeviceType
    OTHER_INDOOR_DEVICE: RecognitionMetadata.RecordingDeviceType
    INTERACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_NAICS_CODE_OF_AUDIO_FIELD_NUMBER: _ClassVar[int]
    MICROPHONE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECORDING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECORDING_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TOPIC_FIELD_NUMBER: _ClassVar[int]
    interaction_type: RecognitionMetadata.InteractionType
    industry_naics_code_of_audio: int
    microphone_distance: RecognitionMetadata.MicrophoneDistance
    original_media_type: RecognitionMetadata.OriginalMediaType
    recording_device_type: RecognitionMetadata.RecordingDeviceType
    recording_device_name: str
    original_mime_type: str
    audio_topic: str

    def __init__(self, interaction_type: _Optional[_Union[RecognitionMetadata.InteractionType, str]]=..., industry_naics_code_of_audio: _Optional[int]=..., microphone_distance: _Optional[_Union[RecognitionMetadata.MicrophoneDistance, str]]=..., original_media_type: _Optional[_Union[RecognitionMetadata.OriginalMediaType, str]]=..., recording_device_type: _Optional[_Union[RecognitionMetadata.RecordingDeviceType, str]]=..., recording_device_name: _Optional[str]=..., original_mime_type: _Optional[str]=..., audio_topic: _Optional[str]=...) -> None:
        ...

class SpeechContext(_message.Message):
    __slots__ = ('phrases', 'boost')
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    BOOST_FIELD_NUMBER: _ClassVar[int]
    phrases: _containers.RepeatedScalarFieldContainer[str]
    boost: float

    def __init__(self, phrases: _Optional[_Iterable[str]]=..., boost: _Optional[float]=...) -> None:
        ...

class RecognitionAudio(_message.Message):
    __slots__ = ('content', 'uri')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    uri: str

    def __init__(self, content: _Optional[bytes]=..., uri: _Optional[str]=...) -> None:
        ...

class RecognizeResponse(_message.Message):
    __slots__ = ('results', 'total_billed_time', 'speech_adaptation_info', 'request_id')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLED_TIME_FIELD_NUMBER: _ClassVar[int]
    SPEECH_ADAPTATION_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionResult]
    total_billed_time: _duration_pb2.Duration
    speech_adaptation_info: SpeechAdaptationInfo
    request_id: int

    def __init__(self, results: _Optional[_Iterable[_Union[SpeechRecognitionResult, _Mapping]]]=..., total_billed_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., speech_adaptation_info: _Optional[_Union[SpeechAdaptationInfo, _Mapping]]=..., request_id: _Optional[int]=...) -> None:
        ...

class LongRunningRecognizeResponse(_message.Message):
    __slots__ = ('results', 'total_billed_time', 'output_config', 'output_error', 'speech_adaptation_info', 'request_id')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLED_TIME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ERROR_FIELD_NUMBER: _ClassVar[int]
    SPEECH_ADAPTATION_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionResult]
    total_billed_time: _duration_pb2.Duration
    output_config: TranscriptOutputConfig
    output_error: _status_pb2.Status
    speech_adaptation_info: SpeechAdaptationInfo
    request_id: int

    def __init__(self, results: _Optional[_Iterable[_Union[SpeechRecognitionResult, _Mapping]]]=..., total_billed_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., output_config: _Optional[_Union[TranscriptOutputConfig, _Mapping]]=..., output_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., speech_adaptation_info: _Optional[_Union[SpeechAdaptationInfo, _Mapping]]=..., request_id: _Optional[int]=...) -> None:
        ...

class LongRunningRecognizeMetadata(_message.Message):
    __slots__ = ('progress_percent', 'start_time', 'last_update_time', 'uri')
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    start_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp
    uri: str

    def __init__(self, progress_percent: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., uri: _Optional[str]=...) -> None:
        ...

class StreamingRecognizeResponse(_message.Message):
    __slots__ = ('error', 'results', 'speech_event_type', 'speech_event_time', 'total_billed_time', 'speech_adaptation_info', 'request_id')

    class SpeechEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPEECH_EVENT_UNSPECIFIED: _ClassVar[StreamingRecognizeResponse.SpeechEventType]
        END_OF_SINGLE_UTTERANCE: _ClassVar[StreamingRecognizeResponse.SpeechEventType]
        SPEECH_ACTIVITY_BEGIN: _ClassVar[StreamingRecognizeResponse.SpeechEventType]
        SPEECH_ACTIVITY_END: _ClassVar[StreamingRecognizeResponse.SpeechEventType]
        SPEECH_ACTIVITY_TIMEOUT: _ClassVar[StreamingRecognizeResponse.SpeechEventType]
    SPEECH_EVENT_UNSPECIFIED: StreamingRecognizeResponse.SpeechEventType
    END_OF_SINGLE_UTTERANCE: StreamingRecognizeResponse.SpeechEventType
    SPEECH_ACTIVITY_BEGIN: StreamingRecognizeResponse.SpeechEventType
    SPEECH_ACTIVITY_END: StreamingRecognizeResponse.SpeechEventType
    SPEECH_ACTIVITY_TIMEOUT: StreamingRecognizeResponse.SpeechEventType
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SPEECH_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPEECH_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLED_TIME_FIELD_NUMBER: _ClassVar[int]
    SPEECH_ADAPTATION_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[StreamingRecognitionResult]
    speech_event_type: StreamingRecognizeResponse.SpeechEventType
    speech_event_time: _duration_pb2.Duration
    total_billed_time: _duration_pb2.Duration
    speech_adaptation_info: SpeechAdaptationInfo
    request_id: int

    def __init__(self, error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., results: _Optional[_Iterable[_Union[StreamingRecognitionResult, _Mapping]]]=..., speech_event_type: _Optional[_Union[StreamingRecognizeResponse.SpeechEventType, str]]=..., speech_event_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., total_billed_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., speech_adaptation_info: _Optional[_Union[SpeechAdaptationInfo, _Mapping]]=..., request_id: _Optional[int]=...) -> None:
        ...

class StreamingRecognitionResult(_message.Message):
    __slots__ = ('alternatives', 'is_final', 'stability', 'result_end_time', 'channel_tag', 'language_code')
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_FIELD_NUMBER: _ClassVar[int]
    STABILITY_FIELD_NUMBER: _ClassVar[int]
    RESULT_END_TIME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TAG_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    alternatives: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionAlternative]
    is_final: bool
    stability: float
    result_end_time: _duration_pb2.Duration
    channel_tag: int
    language_code: str

    def __init__(self, alternatives: _Optional[_Iterable[_Union[SpeechRecognitionAlternative, _Mapping]]]=..., is_final: bool=..., stability: _Optional[float]=..., result_end_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., channel_tag: _Optional[int]=..., language_code: _Optional[str]=...) -> None:
        ...

class SpeechRecognitionResult(_message.Message):
    __slots__ = ('alternatives', 'channel_tag', 'result_end_time', 'language_code')
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TAG_FIELD_NUMBER: _ClassVar[int]
    RESULT_END_TIME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    alternatives: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionAlternative]
    channel_tag: int
    result_end_time: _duration_pb2.Duration
    language_code: str

    def __init__(self, alternatives: _Optional[_Iterable[_Union[SpeechRecognitionAlternative, _Mapping]]]=..., channel_tag: _Optional[int]=..., result_end_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
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
    __slots__ = ('start_time', 'end_time', 'word', 'confidence', 'speaker_tag', 'speaker_label')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    WORD_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_TAG_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_LABEL_FIELD_NUMBER: _ClassVar[int]
    start_time: _duration_pb2.Duration
    end_time: _duration_pb2.Duration
    word: str
    confidence: float
    speaker_tag: int
    speaker_label: str

    def __init__(self, start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., word: _Optional[str]=..., confidence: _Optional[float]=..., speaker_tag: _Optional[int]=..., speaker_label: _Optional[str]=...) -> None:
        ...

class SpeechAdaptationInfo(_message.Message):
    __slots__ = ('adaptation_timeout', 'timeout_message')
    ADAPTATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    adaptation_timeout: bool
    timeout_message: str

    def __init__(self, adaptation_timeout: bool=..., timeout_message: _Optional[str]=...) -> None:
        ...