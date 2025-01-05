from google.api import annotations_pb2 as _annotations_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConverseConfig(_message.Message):
    __slots__ = ('audio_in_config', 'audio_out_config', 'converse_state')
    AUDIO_IN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONVERSE_STATE_FIELD_NUMBER: _ClassVar[int]
    audio_in_config: AudioInConfig
    audio_out_config: AudioOutConfig
    converse_state: ConverseState

    def __init__(self, audio_in_config: _Optional[_Union[AudioInConfig, _Mapping]]=..., audio_out_config: _Optional[_Union[AudioOutConfig, _Mapping]]=..., converse_state: _Optional[_Union[ConverseState, _Mapping]]=...) -> None:
        ...

class AudioInConfig(_message.Message):
    __slots__ = ('encoding', 'sample_rate_hertz')

    class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCODING_UNSPECIFIED: _ClassVar[AudioInConfig.Encoding]
        LINEAR16: _ClassVar[AudioInConfig.Encoding]
        FLAC: _ClassVar[AudioInConfig.Encoding]
    ENCODING_UNSPECIFIED: AudioInConfig.Encoding
    LINEAR16: AudioInConfig.Encoding
    FLAC: AudioInConfig.Encoding
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    encoding: AudioInConfig.Encoding
    sample_rate_hertz: int

    def __init__(self, encoding: _Optional[_Union[AudioInConfig.Encoding, str]]=..., sample_rate_hertz: _Optional[int]=...) -> None:
        ...

class AudioOutConfig(_message.Message):
    __slots__ = ('encoding', 'sample_rate_hertz', 'volume_percentage')

    class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCODING_UNSPECIFIED: _ClassVar[AudioOutConfig.Encoding]
        LINEAR16: _ClassVar[AudioOutConfig.Encoding]
        MP3: _ClassVar[AudioOutConfig.Encoding]
        OPUS_IN_OGG: _ClassVar[AudioOutConfig.Encoding]
    ENCODING_UNSPECIFIED: AudioOutConfig.Encoding
    LINEAR16: AudioOutConfig.Encoding
    MP3: AudioOutConfig.Encoding
    OPUS_IN_OGG: AudioOutConfig.Encoding
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    VOLUME_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    encoding: AudioOutConfig.Encoding
    sample_rate_hertz: int
    volume_percentage: int

    def __init__(self, encoding: _Optional[_Union[AudioOutConfig.Encoding, str]]=..., sample_rate_hertz: _Optional[int]=..., volume_percentage: _Optional[int]=...) -> None:
        ...

class ConverseState(_message.Message):
    __slots__ = ('conversation_state',)
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    conversation_state: bytes

    def __init__(self, conversation_state: _Optional[bytes]=...) -> None:
        ...

class AudioOut(_message.Message):
    __slots__ = ('audio_data',)
    AUDIO_DATA_FIELD_NUMBER: _ClassVar[int]
    audio_data: bytes

    def __init__(self, audio_data: _Optional[bytes]=...) -> None:
        ...

class ConverseResult(_message.Message):
    __slots__ = ('spoken_request_text', 'spoken_response_text', 'conversation_state', 'microphone_mode', 'volume_percentage')

    class MicrophoneMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MICROPHONE_MODE_UNSPECIFIED: _ClassVar[ConverseResult.MicrophoneMode]
        CLOSE_MICROPHONE: _ClassVar[ConverseResult.MicrophoneMode]
        DIALOG_FOLLOW_ON: _ClassVar[ConverseResult.MicrophoneMode]
    MICROPHONE_MODE_UNSPECIFIED: ConverseResult.MicrophoneMode
    CLOSE_MICROPHONE: ConverseResult.MicrophoneMode
    DIALOG_FOLLOW_ON: ConverseResult.MicrophoneMode
    SPOKEN_REQUEST_TEXT_FIELD_NUMBER: _ClassVar[int]
    SPOKEN_RESPONSE_TEXT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    MICROPHONE_MODE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    spoken_request_text: str
    spoken_response_text: str
    conversation_state: bytes
    microphone_mode: ConverseResult.MicrophoneMode
    volume_percentage: int

    def __init__(self, spoken_request_text: _Optional[str]=..., spoken_response_text: _Optional[str]=..., conversation_state: _Optional[bytes]=..., microphone_mode: _Optional[_Union[ConverseResult.MicrophoneMode, str]]=..., volume_percentage: _Optional[int]=...) -> None:
        ...

class ConverseRequest(_message.Message):
    __slots__ = ('config', 'audio_in')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_IN_FIELD_NUMBER: _ClassVar[int]
    config: ConverseConfig
    audio_in: bytes

    def __init__(self, config: _Optional[_Union[ConverseConfig, _Mapping]]=..., audio_in: _Optional[bytes]=...) -> None:
        ...

class ConverseResponse(_message.Message):
    __slots__ = ('error', 'event_type', 'audio_out', 'result')

    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[ConverseResponse.EventType]
        END_OF_UTTERANCE: _ClassVar[ConverseResponse.EventType]
    EVENT_TYPE_UNSPECIFIED: ConverseResponse.EventType
    END_OF_UTTERANCE: ConverseResponse.EventType
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _status_pb2.Status
    event_type: ConverseResponse.EventType
    audio_out: AudioOut
    result: ConverseResult

    def __init__(self, error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., event_type: _Optional[_Union[ConverseResponse.EventType, str]]=..., audio_out: _Optional[_Union[AudioOut, _Mapping]]=..., result: _Optional[_Union[ConverseResult, _Mapping]]=...) -> None:
        ...