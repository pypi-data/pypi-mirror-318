from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.texttospeech.v1 import cloud_tts_pb2 as _cloud_tts_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SynthesizeLongAudioRequest(_message.Message):
    __slots__ = ("parent", "input", "audio_config", "output_gcs_uri", "voice")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_GCS_URI_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    input: _cloud_tts_pb2.SynthesisInput
    audio_config: _cloud_tts_pb2.AudioConfig
    output_gcs_uri: str
    voice: _cloud_tts_pb2.VoiceSelectionParams
    def __init__(self, parent: _Optional[str] = ..., input: _Optional[_Union[_cloud_tts_pb2.SynthesisInput, _Mapping]] = ..., audio_config: _Optional[_Union[_cloud_tts_pb2.AudioConfig, _Mapping]] = ..., output_gcs_uri: _Optional[str] = ..., voice: _Optional[_Union[_cloud_tts_pb2.VoiceSelectionParams, _Mapping]] = ...) -> None: ...

class SynthesizeLongAudioResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SynthesizeLongAudioMetadata(_message.Message):
    __slots__ = ("start_time", "last_update_time", "progress_percentage")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp
    progress_percentage: float
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., progress_percentage: _Optional[float] = ...) -> None: ...
