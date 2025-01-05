from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.dialogflow.cx.v3beta1 import gcs_pb2 as _gcs_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AdvancedSettings(_message.Message):
    __slots__ = ('audio_export_gcs_destination', 'speech_settings', 'dtmf_settings', 'logging_settings')

    class SpeechSettings(_message.Message):
        __slots__ = ('endpointer_sensitivity', 'no_speech_timeout', 'use_timeout_based_endpointing', 'models')

        class ModelsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        ENDPOINTER_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        NO_SPEECH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        USE_TIMEOUT_BASED_ENDPOINTING_FIELD_NUMBER: _ClassVar[int]
        MODELS_FIELD_NUMBER: _ClassVar[int]
        endpointer_sensitivity: int
        no_speech_timeout: _duration_pb2.Duration
        use_timeout_based_endpointing: bool
        models: _containers.ScalarMap[str, str]

        def __init__(self, endpointer_sensitivity: _Optional[int]=..., no_speech_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., use_timeout_based_endpointing: bool=..., models: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class DtmfSettings(_message.Message):
        __slots__ = ('enabled', 'max_digits', 'finish_digit', 'interdigit_timeout_duration', 'endpointing_timeout_duration')
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        MAX_DIGITS_FIELD_NUMBER: _ClassVar[int]
        FINISH_DIGIT_FIELD_NUMBER: _ClassVar[int]
        INTERDIGIT_TIMEOUT_DURATION_FIELD_NUMBER: _ClassVar[int]
        ENDPOINTING_TIMEOUT_DURATION_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        max_digits: int
        finish_digit: str
        interdigit_timeout_duration: _duration_pb2.Duration
        endpointing_timeout_duration: _duration_pb2.Duration

        def __init__(self, enabled: bool=..., max_digits: _Optional[int]=..., finish_digit: _Optional[str]=..., interdigit_timeout_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., endpointing_timeout_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class LoggingSettings(_message.Message):
        __slots__ = ('enable_stackdriver_logging', 'enable_interaction_logging', 'enable_consent_based_redaction')
        ENABLE_STACKDRIVER_LOGGING_FIELD_NUMBER: _ClassVar[int]
        ENABLE_INTERACTION_LOGGING_FIELD_NUMBER: _ClassVar[int]
        ENABLE_CONSENT_BASED_REDACTION_FIELD_NUMBER: _ClassVar[int]
        enable_stackdriver_logging: bool
        enable_interaction_logging: bool
        enable_consent_based_redaction: bool

        def __init__(self, enable_stackdriver_logging: bool=..., enable_interaction_logging: bool=..., enable_consent_based_redaction: bool=...) -> None:
            ...
    AUDIO_EXPORT_GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SPEECH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DTMF_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LOGGING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    audio_export_gcs_destination: _gcs_pb2.GcsDestination
    speech_settings: AdvancedSettings.SpeechSettings
    dtmf_settings: AdvancedSettings.DtmfSettings
    logging_settings: AdvancedSettings.LoggingSettings

    def __init__(self, audio_export_gcs_destination: _Optional[_Union[_gcs_pb2.GcsDestination, _Mapping]]=..., speech_settings: _Optional[_Union[AdvancedSettings.SpeechSettings, _Mapping]]=..., dtmf_settings: _Optional[_Union[AdvancedSettings.DtmfSettings, _Mapping]]=..., logging_settings: _Optional[_Union[AdvancedSettings.LoggingSettings, _Mapping]]=...) -> None:
        ...