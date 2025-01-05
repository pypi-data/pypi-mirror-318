from google.api import annotations_pb2 as _annotations_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssistRequest(_message.Message):
    __slots__ = ('config', 'audio_in')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_IN_FIELD_NUMBER: _ClassVar[int]
    config: AssistConfig
    audio_in: bytes

    def __init__(self, config: _Optional[_Union[AssistConfig, _Mapping]]=..., audio_in: _Optional[bytes]=...) -> None:
        ...

class AssistResponse(_message.Message):
    __slots__ = ('event_type', 'audio_out', 'screen_out', 'device_action', 'speech_results', 'dialog_state_out', 'debug_info')

    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[AssistResponse.EventType]
        END_OF_UTTERANCE: _ClassVar[AssistResponse.EventType]
    EVENT_TYPE_UNSPECIFIED: AssistResponse.EventType
    END_OF_UTTERANCE: AssistResponse.EventType
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUT_FIELD_NUMBER: _ClassVar[int]
    SCREEN_OUT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ACTION_FIELD_NUMBER: _ClassVar[int]
    SPEECH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    DIALOG_STATE_OUT_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    event_type: AssistResponse.EventType
    audio_out: AudioOut
    screen_out: ScreenOut
    device_action: DeviceAction
    speech_results: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionResult]
    dialog_state_out: DialogStateOut
    debug_info: DebugInfo

    def __init__(self, event_type: _Optional[_Union[AssistResponse.EventType, str]]=..., audio_out: _Optional[_Union[AudioOut, _Mapping]]=..., screen_out: _Optional[_Union[ScreenOut, _Mapping]]=..., device_action: _Optional[_Union[DeviceAction, _Mapping]]=..., speech_results: _Optional[_Iterable[_Union[SpeechRecognitionResult, _Mapping]]]=..., dialog_state_out: _Optional[_Union[DialogStateOut, _Mapping]]=..., debug_info: _Optional[_Union[DebugInfo, _Mapping]]=...) -> None:
        ...

class DebugInfo(_message.Message):
    __slots__ = ('aog_agent_to_assistant_json',)
    AOG_AGENT_TO_ASSISTANT_JSON_FIELD_NUMBER: _ClassVar[int]
    aog_agent_to_assistant_json: str

    def __init__(self, aog_agent_to_assistant_json: _Optional[str]=...) -> None:
        ...

class AssistConfig(_message.Message):
    __slots__ = ('audio_in_config', 'text_query', 'audio_out_config', 'screen_out_config', 'dialog_state_in', 'device_config', 'debug_config')
    AUDIO_IN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_QUERY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SCREEN_OUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DIALOG_STATE_IN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEBUG_CONFIG_FIELD_NUMBER: _ClassVar[int]
    audio_in_config: AudioInConfig
    text_query: str
    audio_out_config: AudioOutConfig
    screen_out_config: ScreenOutConfig
    dialog_state_in: DialogStateIn
    device_config: DeviceConfig
    debug_config: DebugConfig

    def __init__(self, audio_in_config: _Optional[_Union[AudioInConfig, _Mapping]]=..., text_query: _Optional[str]=..., audio_out_config: _Optional[_Union[AudioOutConfig, _Mapping]]=..., screen_out_config: _Optional[_Union[ScreenOutConfig, _Mapping]]=..., dialog_state_in: _Optional[_Union[DialogStateIn, _Mapping]]=..., device_config: _Optional[_Union[DeviceConfig, _Mapping]]=..., debug_config: _Optional[_Union[DebugConfig, _Mapping]]=...) -> None:
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

class ScreenOutConfig(_message.Message):
    __slots__ = ('screen_mode',)

    class ScreenMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCREEN_MODE_UNSPECIFIED: _ClassVar[ScreenOutConfig.ScreenMode]
        OFF: _ClassVar[ScreenOutConfig.ScreenMode]
        PLAYING: _ClassVar[ScreenOutConfig.ScreenMode]
    SCREEN_MODE_UNSPECIFIED: ScreenOutConfig.ScreenMode
    OFF: ScreenOutConfig.ScreenMode
    PLAYING: ScreenOutConfig.ScreenMode
    SCREEN_MODE_FIELD_NUMBER: _ClassVar[int]
    screen_mode: ScreenOutConfig.ScreenMode

    def __init__(self, screen_mode: _Optional[_Union[ScreenOutConfig.ScreenMode, str]]=...) -> None:
        ...

class DialogStateIn(_message.Message):
    __slots__ = ('conversation_state', 'language_code', 'device_location', 'is_new_conversation')
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation_state: bytes
    language_code: str
    device_location: DeviceLocation
    is_new_conversation: bool

    def __init__(self, conversation_state: _Optional[bytes]=..., language_code: _Optional[str]=..., device_location: _Optional[_Union[DeviceLocation, _Mapping]]=..., is_new_conversation: bool=...) -> None:
        ...

class DeviceConfig(_message.Message):
    __slots__ = ('device_id', 'device_model_id')
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    device_model_id: str

    def __init__(self, device_id: _Optional[str]=..., device_model_id: _Optional[str]=...) -> None:
        ...

class AudioOut(_message.Message):
    __slots__ = ('audio_data',)
    AUDIO_DATA_FIELD_NUMBER: _ClassVar[int]
    audio_data: bytes

    def __init__(self, audio_data: _Optional[bytes]=...) -> None:
        ...

class ScreenOut(_message.Message):
    __slots__ = ('format', 'data')

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[ScreenOut.Format]
        HTML: _ClassVar[ScreenOut.Format]
    FORMAT_UNSPECIFIED: ScreenOut.Format
    HTML: ScreenOut.Format
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    format: ScreenOut.Format
    data: bytes

    def __init__(self, format: _Optional[_Union[ScreenOut.Format, str]]=..., data: _Optional[bytes]=...) -> None:
        ...

class DeviceAction(_message.Message):
    __slots__ = ('device_request_json',)
    DEVICE_REQUEST_JSON_FIELD_NUMBER: _ClassVar[int]
    device_request_json: str

    def __init__(self, device_request_json: _Optional[str]=...) -> None:
        ...

class SpeechRecognitionResult(_message.Message):
    __slots__ = ('transcript', 'stability')
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    STABILITY_FIELD_NUMBER: _ClassVar[int]
    transcript: str
    stability: float

    def __init__(self, transcript: _Optional[str]=..., stability: _Optional[float]=...) -> None:
        ...

class DialogStateOut(_message.Message):
    __slots__ = ('supplemental_display_text', 'conversation_state', 'microphone_mode', 'volume_percentage')

    class MicrophoneMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MICROPHONE_MODE_UNSPECIFIED: _ClassVar[DialogStateOut.MicrophoneMode]
        CLOSE_MICROPHONE: _ClassVar[DialogStateOut.MicrophoneMode]
        DIALOG_FOLLOW_ON: _ClassVar[DialogStateOut.MicrophoneMode]
    MICROPHONE_MODE_UNSPECIFIED: DialogStateOut.MicrophoneMode
    CLOSE_MICROPHONE: DialogStateOut.MicrophoneMode
    DIALOG_FOLLOW_ON: DialogStateOut.MicrophoneMode
    SUPPLEMENTAL_DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    MICROPHONE_MODE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    supplemental_display_text: str
    conversation_state: bytes
    microphone_mode: DialogStateOut.MicrophoneMode
    volume_percentage: int

    def __init__(self, supplemental_display_text: _Optional[str]=..., conversation_state: _Optional[bytes]=..., microphone_mode: _Optional[_Union[DialogStateOut.MicrophoneMode, str]]=..., volume_percentage: _Optional[int]=...) -> None:
        ...

class DebugConfig(_message.Message):
    __slots__ = ('return_debug_info',)
    RETURN_DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    return_debug_info: bool

    def __init__(self, return_debug_info: bool=...) -> None:
        ...

class DeviceLocation(_message.Message):
    __slots__ = ('coordinates',)
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    coordinates: _latlng_pb2.LatLng

    def __init__(self, coordinates: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=...) -> None:
        ...