from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.rpc import status_pb2 as _status_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TranslateSpeechConfig(_message.Message):
    __slots__ = ('audio_encoding', 'source_language_code', 'target_language_code', 'sample_rate_hertz', 'model')
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    audio_encoding: str
    source_language_code: str
    target_language_code: str
    sample_rate_hertz: int
    model: str

    def __init__(self, audio_encoding: _Optional[str]=..., source_language_code: _Optional[str]=..., target_language_code: _Optional[str]=..., sample_rate_hertz: _Optional[int]=..., model: _Optional[str]=...) -> None:
        ...

class StreamingTranslateSpeechConfig(_message.Message):
    __slots__ = ('audio_config', 'single_utterance')
    AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SINGLE_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    audio_config: TranslateSpeechConfig
    single_utterance: bool

    def __init__(self, audio_config: _Optional[_Union[TranslateSpeechConfig, _Mapping]]=..., single_utterance: bool=...) -> None:
        ...

class StreamingTranslateSpeechRequest(_message.Message):
    __slots__ = ('streaming_config', 'audio_content')
    STREAMING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CONTENT_FIELD_NUMBER: _ClassVar[int]
    streaming_config: StreamingTranslateSpeechConfig
    audio_content: bytes

    def __init__(self, streaming_config: _Optional[_Union[StreamingTranslateSpeechConfig, _Mapping]]=..., audio_content: _Optional[bytes]=...) -> None:
        ...

class StreamingTranslateSpeechResult(_message.Message):
    __slots__ = ('text_translation_result',)

    class TextTranslationResult(_message.Message):
        __slots__ = ('translation', 'is_final')
        TRANSLATION_FIELD_NUMBER: _ClassVar[int]
        IS_FINAL_FIELD_NUMBER: _ClassVar[int]
        translation: str
        is_final: bool

        def __init__(self, translation: _Optional[str]=..., is_final: bool=...) -> None:
            ...
    TEXT_TRANSLATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    text_translation_result: StreamingTranslateSpeechResult.TextTranslationResult

    def __init__(self, text_translation_result: _Optional[_Union[StreamingTranslateSpeechResult.TextTranslationResult, _Mapping]]=...) -> None:
        ...

class StreamingTranslateSpeechResponse(_message.Message):
    __slots__ = ('error', 'result', 'speech_event_type')

    class SpeechEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPEECH_EVENT_TYPE_UNSPECIFIED: _ClassVar[StreamingTranslateSpeechResponse.SpeechEventType]
        END_OF_SINGLE_UTTERANCE: _ClassVar[StreamingTranslateSpeechResponse.SpeechEventType]
    SPEECH_EVENT_TYPE_UNSPECIFIED: StreamingTranslateSpeechResponse.SpeechEventType
    END_OF_SINGLE_UTTERANCE: StreamingTranslateSpeechResponse.SpeechEventType
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SPEECH_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    error: _status_pb2.Status
    result: StreamingTranslateSpeechResult
    speech_event_type: StreamingTranslateSpeechResponse.SpeechEventType

    def __init__(self, error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., result: _Optional[_Union[StreamingTranslateSpeechResult, _Mapping]]=..., speech_event_type: _Optional[_Union[StreamingTranslateSpeechResponse.SpeechEventType, str]]=...) -> None:
        ...