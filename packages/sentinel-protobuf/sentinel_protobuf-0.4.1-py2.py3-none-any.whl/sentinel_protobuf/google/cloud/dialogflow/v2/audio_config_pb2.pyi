from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TelephonyDtmf(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TELEPHONY_DTMF_UNSPECIFIED: _ClassVar[TelephonyDtmf]
    DTMF_ONE: _ClassVar[TelephonyDtmf]
    DTMF_TWO: _ClassVar[TelephonyDtmf]
    DTMF_THREE: _ClassVar[TelephonyDtmf]
    DTMF_FOUR: _ClassVar[TelephonyDtmf]
    DTMF_FIVE: _ClassVar[TelephonyDtmf]
    DTMF_SIX: _ClassVar[TelephonyDtmf]
    DTMF_SEVEN: _ClassVar[TelephonyDtmf]
    DTMF_EIGHT: _ClassVar[TelephonyDtmf]
    DTMF_NINE: _ClassVar[TelephonyDtmf]
    DTMF_ZERO: _ClassVar[TelephonyDtmf]
    DTMF_A: _ClassVar[TelephonyDtmf]
    DTMF_B: _ClassVar[TelephonyDtmf]
    DTMF_C: _ClassVar[TelephonyDtmf]
    DTMF_D: _ClassVar[TelephonyDtmf]
    DTMF_STAR: _ClassVar[TelephonyDtmf]
    DTMF_POUND: _ClassVar[TelephonyDtmf]

class AudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIO_ENCODING_UNSPECIFIED: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_LINEAR_16: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_FLAC: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_MULAW: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_AMR: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_AMR_WB: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_OGG_OPUS: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_ALAW: _ClassVar[AudioEncoding]

class SpeechModelVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPEECH_MODEL_VARIANT_UNSPECIFIED: _ClassVar[SpeechModelVariant]
    USE_BEST_AVAILABLE: _ClassVar[SpeechModelVariant]
    USE_STANDARD: _ClassVar[SpeechModelVariant]
    USE_ENHANCED: _ClassVar[SpeechModelVariant]

class SsmlVoiceGender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SSML_VOICE_GENDER_UNSPECIFIED: _ClassVar[SsmlVoiceGender]
    SSML_VOICE_GENDER_MALE: _ClassVar[SsmlVoiceGender]
    SSML_VOICE_GENDER_FEMALE: _ClassVar[SsmlVoiceGender]
    SSML_VOICE_GENDER_NEUTRAL: _ClassVar[SsmlVoiceGender]

class OutputAudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTPUT_AUDIO_ENCODING_UNSPECIFIED: _ClassVar[OutputAudioEncoding]
    OUTPUT_AUDIO_ENCODING_LINEAR_16: _ClassVar[OutputAudioEncoding]
    OUTPUT_AUDIO_ENCODING_MP3: _ClassVar[OutputAudioEncoding]
    OUTPUT_AUDIO_ENCODING_MP3_64_KBPS: _ClassVar[OutputAudioEncoding]
    OUTPUT_AUDIO_ENCODING_OGG_OPUS: _ClassVar[OutputAudioEncoding]
    OUTPUT_AUDIO_ENCODING_MULAW: _ClassVar[OutputAudioEncoding]
    OUTPUT_AUDIO_ENCODING_ALAW: _ClassVar[OutputAudioEncoding]
TELEPHONY_DTMF_UNSPECIFIED: TelephonyDtmf
DTMF_ONE: TelephonyDtmf
DTMF_TWO: TelephonyDtmf
DTMF_THREE: TelephonyDtmf
DTMF_FOUR: TelephonyDtmf
DTMF_FIVE: TelephonyDtmf
DTMF_SIX: TelephonyDtmf
DTMF_SEVEN: TelephonyDtmf
DTMF_EIGHT: TelephonyDtmf
DTMF_NINE: TelephonyDtmf
DTMF_ZERO: TelephonyDtmf
DTMF_A: TelephonyDtmf
DTMF_B: TelephonyDtmf
DTMF_C: TelephonyDtmf
DTMF_D: TelephonyDtmf
DTMF_STAR: TelephonyDtmf
DTMF_POUND: TelephonyDtmf
AUDIO_ENCODING_UNSPECIFIED: AudioEncoding
AUDIO_ENCODING_LINEAR_16: AudioEncoding
AUDIO_ENCODING_FLAC: AudioEncoding
AUDIO_ENCODING_MULAW: AudioEncoding
AUDIO_ENCODING_AMR: AudioEncoding
AUDIO_ENCODING_AMR_WB: AudioEncoding
AUDIO_ENCODING_OGG_OPUS: AudioEncoding
AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE: AudioEncoding
AUDIO_ENCODING_ALAW: AudioEncoding
SPEECH_MODEL_VARIANT_UNSPECIFIED: SpeechModelVariant
USE_BEST_AVAILABLE: SpeechModelVariant
USE_STANDARD: SpeechModelVariant
USE_ENHANCED: SpeechModelVariant
SSML_VOICE_GENDER_UNSPECIFIED: SsmlVoiceGender
SSML_VOICE_GENDER_MALE: SsmlVoiceGender
SSML_VOICE_GENDER_FEMALE: SsmlVoiceGender
SSML_VOICE_GENDER_NEUTRAL: SsmlVoiceGender
OUTPUT_AUDIO_ENCODING_UNSPECIFIED: OutputAudioEncoding
OUTPUT_AUDIO_ENCODING_LINEAR_16: OutputAudioEncoding
OUTPUT_AUDIO_ENCODING_MP3: OutputAudioEncoding
OUTPUT_AUDIO_ENCODING_MP3_64_KBPS: OutputAudioEncoding
OUTPUT_AUDIO_ENCODING_OGG_OPUS: OutputAudioEncoding
OUTPUT_AUDIO_ENCODING_MULAW: OutputAudioEncoding
OUTPUT_AUDIO_ENCODING_ALAW: OutputAudioEncoding

class SpeechContext(_message.Message):
    __slots__ = ('phrases', 'boost')
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    BOOST_FIELD_NUMBER: _ClassVar[int]
    phrases: _containers.RepeatedScalarFieldContainer[str]
    boost: float

    def __init__(self, phrases: _Optional[_Iterable[str]]=..., boost: _Optional[float]=...) -> None:
        ...

class SpeechWordInfo(_message.Message):
    __slots__ = ('word', 'start_offset', 'end_offset', 'confidence')
    WORD_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    word: str
    start_offset: _duration_pb2.Duration
    end_offset: _duration_pb2.Duration
    confidence: float

    def __init__(self, word: _Optional[str]=..., start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., confidence: _Optional[float]=...) -> None:
        ...

class InputAudioConfig(_message.Message):
    __slots__ = ('audio_encoding', 'sample_rate_hertz', 'language_code', 'enable_word_info', 'phrase_hints', 'speech_contexts', 'model', 'model_variant', 'single_utterance', 'disable_no_speech_recognized_event', 'enable_automatic_punctuation', 'phrase_sets', 'opt_out_conformer_model_migration')
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_INFO_FIELD_NUMBER: _ClassVar[int]
    PHRASE_HINTS_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_VARIANT_FIELD_NUMBER: _ClassVar[int]
    SINGLE_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_NO_SPEECH_RECOGNIZED_EVENT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTOMATIC_PUNCTUATION_FIELD_NUMBER: _ClassVar[int]
    PHRASE_SETS_FIELD_NUMBER: _ClassVar[int]
    OPT_OUT_CONFORMER_MODEL_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    audio_encoding: AudioEncoding
    sample_rate_hertz: int
    language_code: str
    enable_word_info: bool
    phrase_hints: _containers.RepeatedScalarFieldContainer[str]
    speech_contexts: _containers.RepeatedCompositeFieldContainer[SpeechContext]
    model: str
    model_variant: SpeechModelVariant
    single_utterance: bool
    disable_no_speech_recognized_event: bool
    enable_automatic_punctuation: bool
    phrase_sets: _containers.RepeatedScalarFieldContainer[str]
    opt_out_conformer_model_migration: bool

    def __init__(self, audio_encoding: _Optional[_Union[AudioEncoding, str]]=..., sample_rate_hertz: _Optional[int]=..., language_code: _Optional[str]=..., enable_word_info: bool=..., phrase_hints: _Optional[_Iterable[str]]=..., speech_contexts: _Optional[_Iterable[_Union[SpeechContext, _Mapping]]]=..., model: _Optional[str]=..., model_variant: _Optional[_Union[SpeechModelVariant, str]]=..., single_utterance: bool=..., disable_no_speech_recognized_event: bool=..., enable_automatic_punctuation: bool=..., phrase_sets: _Optional[_Iterable[str]]=..., opt_out_conformer_model_migration: bool=...) -> None:
        ...

class VoiceSelectionParams(_message.Message):
    __slots__ = ('name', 'ssml_gender')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SSML_GENDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    ssml_gender: SsmlVoiceGender

    def __init__(self, name: _Optional[str]=..., ssml_gender: _Optional[_Union[SsmlVoiceGender, str]]=...) -> None:
        ...

class SynthesizeSpeechConfig(_message.Message):
    __slots__ = ('speaking_rate', 'pitch', 'volume_gain_db', 'effects_profile_id', 'voice')
    SPEAKING_RATE_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GAIN_DB_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    speaking_rate: float
    pitch: float
    volume_gain_db: float
    effects_profile_id: _containers.RepeatedScalarFieldContainer[str]
    voice: VoiceSelectionParams

    def __init__(self, speaking_rate: _Optional[float]=..., pitch: _Optional[float]=..., volume_gain_db: _Optional[float]=..., effects_profile_id: _Optional[_Iterable[str]]=..., voice: _Optional[_Union[VoiceSelectionParams, _Mapping]]=...) -> None:
        ...

class OutputAudioConfig(_message.Message):
    __slots__ = ('audio_encoding', 'sample_rate_hertz', 'synthesize_speech_config')
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    SYNTHESIZE_SPEECH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    audio_encoding: OutputAudioEncoding
    sample_rate_hertz: int
    synthesize_speech_config: SynthesizeSpeechConfig

    def __init__(self, audio_encoding: _Optional[_Union[OutputAudioEncoding, str]]=..., sample_rate_hertz: _Optional[int]=..., synthesize_speech_config: _Optional[_Union[SynthesizeSpeechConfig, _Mapping]]=...) -> None:
        ...

class TelephonyDtmfEvents(_message.Message):
    __slots__ = ('dtmf_events',)
    DTMF_EVENTS_FIELD_NUMBER: _ClassVar[int]
    dtmf_events: _containers.RepeatedScalarFieldContainer[TelephonyDtmf]

    def __init__(self, dtmf_events: _Optional[_Iterable[_Union[TelephonyDtmf, str]]]=...) -> None:
        ...

class SpeechToTextConfig(_message.Message):
    __slots__ = ('speech_model_variant', 'model', 'phrase_sets', 'audio_encoding', 'sample_rate_hertz', 'language_code', 'enable_word_info', 'use_timeout_based_endpointing')
    SPEECH_MODEL_VARIANT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PHRASE_SETS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_TIMEOUT_BASED_ENDPOINTING_FIELD_NUMBER: _ClassVar[int]
    speech_model_variant: SpeechModelVariant
    model: str
    phrase_sets: _containers.RepeatedScalarFieldContainer[str]
    audio_encoding: AudioEncoding
    sample_rate_hertz: int
    language_code: str
    enable_word_info: bool
    use_timeout_based_endpointing: bool

    def __init__(self, speech_model_variant: _Optional[_Union[SpeechModelVariant, str]]=..., model: _Optional[str]=..., phrase_sets: _Optional[_Iterable[str]]=..., audio_encoding: _Optional[_Union[AudioEncoding, str]]=..., sample_rate_hertz: _Optional[int]=..., language_code: _Optional[str]=..., enable_word_info: bool=..., use_timeout_based_endpointing: bool=...) -> None:
        ...