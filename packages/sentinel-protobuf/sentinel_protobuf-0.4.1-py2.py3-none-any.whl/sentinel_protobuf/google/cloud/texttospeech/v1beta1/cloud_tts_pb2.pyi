from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SsmlVoiceGender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SSML_VOICE_GENDER_UNSPECIFIED: _ClassVar[SsmlVoiceGender]
    MALE: _ClassVar[SsmlVoiceGender]
    FEMALE: _ClassVar[SsmlVoiceGender]
    NEUTRAL: _ClassVar[SsmlVoiceGender]

class AudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIO_ENCODING_UNSPECIFIED: _ClassVar[AudioEncoding]
    LINEAR16: _ClassVar[AudioEncoding]
    MP3: _ClassVar[AudioEncoding]
    MP3_64_KBPS: _ClassVar[AudioEncoding]
    OGG_OPUS: _ClassVar[AudioEncoding]
    MULAW: _ClassVar[AudioEncoding]
    ALAW: _ClassVar[AudioEncoding]
    PCM: _ClassVar[AudioEncoding]
SSML_VOICE_GENDER_UNSPECIFIED: SsmlVoiceGender
MALE: SsmlVoiceGender
FEMALE: SsmlVoiceGender
NEUTRAL: SsmlVoiceGender
AUDIO_ENCODING_UNSPECIFIED: AudioEncoding
LINEAR16: AudioEncoding
MP3: AudioEncoding
MP3_64_KBPS: AudioEncoding
OGG_OPUS: AudioEncoding
MULAW: AudioEncoding
ALAW: AudioEncoding
PCM: AudioEncoding

class ListVoicesRequest(_message.Message):
    __slots__ = ("language_code",)
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    def __init__(self, language_code: _Optional[str] = ...) -> None: ...

class ListVoicesResponse(_message.Message):
    __slots__ = ("voices",)
    VOICES_FIELD_NUMBER: _ClassVar[int]
    voices: _containers.RepeatedCompositeFieldContainer[Voice]
    def __init__(self, voices: _Optional[_Iterable[_Union[Voice, _Mapping]]] = ...) -> None: ...

class Voice(_message.Message):
    __slots__ = ("language_codes", "name", "ssml_gender", "natural_sample_rate_hertz")
    LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SSML_GENDER_FIELD_NUMBER: _ClassVar[int]
    NATURAL_SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    language_codes: _containers.RepeatedScalarFieldContainer[str]
    name: str
    ssml_gender: SsmlVoiceGender
    natural_sample_rate_hertz: int
    def __init__(self, language_codes: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., ssml_gender: _Optional[_Union[SsmlVoiceGender, str]] = ..., natural_sample_rate_hertz: _Optional[int] = ...) -> None: ...

class AdvancedVoiceOptions(_message.Message):
    __slots__ = ("low_latency_journey_synthesis",)
    LOW_LATENCY_JOURNEY_SYNTHESIS_FIELD_NUMBER: _ClassVar[int]
    low_latency_journey_synthesis: bool
    def __init__(self, low_latency_journey_synthesis: bool = ...) -> None: ...

class SynthesizeSpeechRequest(_message.Message):
    __slots__ = ("input", "voice", "audio_config", "enable_time_pointing", "advanced_voice_options")
    class TimepointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIMEPOINT_TYPE_UNSPECIFIED: _ClassVar[SynthesizeSpeechRequest.TimepointType]
        SSML_MARK: _ClassVar[SynthesizeSpeechRequest.TimepointType]
    TIMEPOINT_TYPE_UNSPECIFIED: SynthesizeSpeechRequest.TimepointType
    SSML_MARK: SynthesizeSpeechRequest.TimepointType
    INPUT_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TIME_POINTING_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_VOICE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    input: SynthesisInput
    voice: VoiceSelectionParams
    audio_config: AudioConfig
    enable_time_pointing: _containers.RepeatedScalarFieldContainer[SynthesizeSpeechRequest.TimepointType]
    advanced_voice_options: AdvancedVoiceOptions
    def __init__(self, input: _Optional[_Union[SynthesisInput, _Mapping]] = ..., voice: _Optional[_Union[VoiceSelectionParams, _Mapping]] = ..., audio_config: _Optional[_Union[AudioConfig, _Mapping]] = ..., enable_time_pointing: _Optional[_Iterable[_Union[SynthesizeSpeechRequest.TimepointType, str]]] = ..., advanced_voice_options: _Optional[_Union[AdvancedVoiceOptions, _Mapping]] = ...) -> None: ...

class CustomPronunciationParams(_message.Message):
    __slots__ = ("phrase", "phonetic_encoding", "pronunciation")
    class PhoneticEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHONETIC_ENCODING_UNSPECIFIED: _ClassVar[CustomPronunciationParams.PhoneticEncoding]
        PHONETIC_ENCODING_IPA: _ClassVar[CustomPronunciationParams.PhoneticEncoding]
        PHONETIC_ENCODING_X_SAMPA: _ClassVar[CustomPronunciationParams.PhoneticEncoding]
    PHONETIC_ENCODING_UNSPECIFIED: CustomPronunciationParams.PhoneticEncoding
    PHONETIC_ENCODING_IPA: CustomPronunciationParams.PhoneticEncoding
    PHONETIC_ENCODING_X_SAMPA: CustomPronunciationParams.PhoneticEncoding
    PHRASE_FIELD_NUMBER: _ClassVar[int]
    PHONETIC_ENCODING_FIELD_NUMBER: _ClassVar[int]
    PRONUNCIATION_FIELD_NUMBER: _ClassVar[int]
    phrase: str
    phonetic_encoding: CustomPronunciationParams.PhoneticEncoding
    pronunciation: str
    def __init__(self, phrase: _Optional[str] = ..., phonetic_encoding: _Optional[_Union[CustomPronunciationParams.PhoneticEncoding, str]] = ..., pronunciation: _Optional[str] = ...) -> None: ...

class CustomPronunciations(_message.Message):
    __slots__ = ("pronunciations",)
    PRONUNCIATIONS_FIELD_NUMBER: _ClassVar[int]
    pronunciations: _containers.RepeatedCompositeFieldContainer[CustomPronunciationParams]
    def __init__(self, pronunciations: _Optional[_Iterable[_Union[CustomPronunciationParams, _Mapping]]] = ...) -> None: ...

class MultiSpeakerMarkup(_message.Message):
    __slots__ = ("turns",)
    class Turn(_message.Message):
        __slots__ = ("speaker", "text")
        SPEAKER_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        speaker: str
        text: str
        def __init__(self, speaker: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
    TURNS_FIELD_NUMBER: _ClassVar[int]
    turns: _containers.RepeatedCompositeFieldContainer[MultiSpeakerMarkup.Turn]
    def __init__(self, turns: _Optional[_Iterable[_Union[MultiSpeakerMarkup.Turn, _Mapping]]] = ...) -> None: ...

class SynthesisInput(_message.Message):
    __slots__ = ("text", "ssml", "multi_speaker_markup", "custom_pronunciations")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SSML_FIELD_NUMBER: _ClassVar[int]
    MULTI_SPEAKER_MARKUP_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PRONUNCIATIONS_FIELD_NUMBER: _ClassVar[int]
    text: str
    ssml: str
    multi_speaker_markup: MultiSpeakerMarkup
    custom_pronunciations: CustomPronunciations
    def __init__(self, text: _Optional[str] = ..., ssml: _Optional[str] = ..., multi_speaker_markup: _Optional[_Union[MultiSpeakerMarkup, _Mapping]] = ..., custom_pronunciations: _Optional[_Union[CustomPronunciations, _Mapping]] = ...) -> None: ...

class VoiceSelectionParams(_message.Message):
    __slots__ = ("language_code", "name", "ssml_gender", "custom_voice", "voice_clone")
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SSML_GENDER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VOICE_FIELD_NUMBER: _ClassVar[int]
    VOICE_CLONE_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    name: str
    ssml_gender: SsmlVoiceGender
    custom_voice: CustomVoiceParams
    voice_clone: VoiceCloneParams
    def __init__(self, language_code: _Optional[str] = ..., name: _Optional[str] = ..., ssml_gender: _Optional[_Union[SsmlVoiceGender, str]] = ..., custom_voice: _Optional[_Union[CustomVoiceParams, _Mapping]] = ..., voice_clone: _Optional[_Union[VoiceCloneParams, _Mapping]] = ...) -> None: ...

class AudioConfig(_message.Message):
    __slots__ = ("audio_encoding", "speaking_rate", "pitch", "volume_gain_db", "sample_rate_hertz", "effects_profile_id")
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SPEAKING_RATE_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GAIN_DB_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    audio_encoding: AudioEncoding
    speaking_rate: float
    pitch: float
    volume_gain_db: float
    sample_rate_hertz: int
    effects_profile_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, audio_encoding: _Optional[_Union[AudioEncoding, str]] = ..., speaking_rate: _Optional[float] = ..., pitch: _Optional[float] = ..., volume_gain_db: _Optional[float] = ..., sample_rate_hertz: _Optional[int] = ..., effects_profile_id: _Optional[_Iterable[str]] = ...) -> None: ...

class CustomVoiceParams(_message.Message):
    __slots__ = ("model", "reported_usage")
    class ReportedUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPORTED_USAGE_UNSPECIFIED: _ClassVar[CustomVoiceParams.ReportedUsage]
        REALTIME: _ClassVar[CustomVoiceParams.ReportedUsage]
        OFFLINE: _ClassVar[CustomVoiceParams.ReportedUsage]
    REPORTED_USAGE_UNSPECIFIED: CustomVoiceParams.ReportedUsage
    REALTIME: CustomVoiceParams.ReportedUsage
    OFFLINE: CustomVoiceParams.ReportedUsage
    MODEL_FIELD_NUMBER: _ClassVar[int]
    REPORTED_USAGE_FIELD_NUMBER: _ClassVar[int]
    model: str
    reported_usage: CustomVoiceParams.ReportedUsage
    def __init__(self, model: _Optional[str] = ..., reported_usage: _Optional[_Union[CustomVoiceParams.ReportedUsage, str]] = ...) -> None: ...

class VoiceCloneParams(_message.Message):
    __slots__ = ("voice_cloning_key",)
    VOICE_CLONING_KEY_FIELD_NUMBER: _ClassVar[int]
    voice_cloning_key: str
    def __init__(self, voice_cloning_key: _Optional[str] = ...) -> None: ...

class SynthesizeSpeechResponse(_message.Message):
    __slots__ = ("audio_content", "timepoints", "audio_config")
    AUDIO_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TIMEPOINTS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    audio_content: bytes
    timepoints: _containers.RepeatedCompositeFieldContainer[Timepoint]
    audio_config: AudioConfig
    def __init__(self, audio_content: _Optional[bytes] = ..., timepoints: _Optional[_Iterable[_Union[Timepoint, _Mapping]]] = ..., audio_config: _Optional[_Union[AudioConfig, _Mapping]] = ...) -> None: ...

class Timepoint(_message.Message):
    __slots__ = ("mark_name", "time_seconds")
    MARK_NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    mark_name: str
    time_seconds: float
    def __init__(self, mark_name: _Optional[str] = ..., time_seconds: _Optional[float] = ...) -> None: ...

class StreamingAudioConfig(_message.Message):
    __slots__ = ("audio_encoding", "sample_rate_hertz")
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    audio_encoding: AudioEncoding
    sample_rate_hertz: int
    def __init__(self, audio_encoding: _Optional[_Union[AudioEncoding, str]] = ..., sample_rate_hertz: _Optional[int] = ...) -> None: ...

class StreamingSynthesizeConfig(_message.Message):
    __slots__ = ("voice", "streaming_audio_config")
    VOICE_FIELD_NUMBER: _ClassVar[int]
    STREAMING_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    voice: VoiceSelectionParams
    streaming_audio_config: StreamingAudioConfig
    def __init__(self, voice: _Optional[_Union[VoiceSelectionParams, _Mapping]] = ..., streaming_audio_config: _Optional[_Union[StreamingAudioConfig, _Mapping]] = ...) -> None: ...

class StreamingSynthesisInput(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class StreamingSynthesizeRequest(_message.Message):
    __slots__ = ("streaming_config", "input")
    STREAMING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    streaming_config: StreamingSynthesizeConfig
    input: StreamingSynthesisInput
    def __init__(self, streaming_config: _Optional[_Union[StreamingSynthesizeConfig, _Mapping]] = ..., input: _Optional[_Union[StreamingSynthesisInput, _Mapping]] = ...) -> None: ...

class StreamingSynthesizeResponse(_message.Message):
    __slots__ = ("audio_content",)
    AUDIO_CONTENT_FIELD_NUMBER: _ClassVar[int]
    audio_content: bytes
    def __init__(self, audio_content: _Optional[bytes] = ...) -> None: ...
