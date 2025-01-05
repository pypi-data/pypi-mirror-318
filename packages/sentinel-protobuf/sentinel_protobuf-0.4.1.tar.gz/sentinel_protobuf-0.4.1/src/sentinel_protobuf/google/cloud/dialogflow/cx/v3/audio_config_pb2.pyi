from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

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

class BargeInConfig(_message.Message):
    __slots__ = ('no_barge_in_duration', 'total_duration')
    NO_BARGE_IN_DURATION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_FIELD_NUMBER: _ClassVar[int]
    no_barge_in_duration: _duration_pb2.Duration
    total_duration: _duration_pb2.Duration

    def __init__(self, no_barge_in_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., total_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class InputAudioConfig(_message.Message):
    __slots__ = ('audio_encoding', 'sample_rate_hertz', 'enable_word_info', 'phrase_hints', 'model', 'model_variant', 'single_utterance', 'barge_in_config', 'opt_out_conformer_model_migration')
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_INFO_FIELD_NUMBER: _ClassVar[int]
    PHRASE_HINTS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_VARIANT_FIELD_NUMBER: _ClassVar[int]
    SINGLE_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    BARGE_IN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OPT_OUT_CONFORMER_MODEL_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    audio_encoding: AudioEncoding
    sample_rate_hertz: int
    enable_word_info: bool
    phrase_hints: _containers.RepeatedScalarFieldContainer[str]
    model: str
    model_variant: SpeechModelVariant
    single_utterance: bool
    barge_in_config: BargeInConfig
    opt_out_conformer_model_migration: bool

    def __init__(self, audio_encoding: _Optional[_Union[AudioEncoding, str]]=..., sample_rate_hertz: _Optional[int]=..., enable_word_info: bool=..., phrase_hints: _Optional[_Iterable[str]]=..., model: _Optional[str]=..., model_variant: _Optional[_Union[SpeechModelVariant, str]]=..., single_utterance: bool=..., barge_in_config: _Optional[_Union[BargeInConfig, _Mapping]]=..., opt_out_conformer_model_migration: bool=...) -> None:
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

class TextToSpeechSettings(_message.Message):
    __slots__ = ('synthesize_speech_configs',)

    class SynthesizeSpeechConfigsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SynthesizeSpeechConfig

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[SynthesizeSpeechConfig, _Mapping]]=...) -> None:
            ...
    SYNTHESIZE_SPEECH_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    synthesize_speech_configs: _containers.MessageMap[str, SynthesizeSpeechConfig]

    def __init__(self, synthesize_speech_configs: _Optional[_Mapping[str, SynthesizeSpeechConfig]]=...) -> None:
        ...