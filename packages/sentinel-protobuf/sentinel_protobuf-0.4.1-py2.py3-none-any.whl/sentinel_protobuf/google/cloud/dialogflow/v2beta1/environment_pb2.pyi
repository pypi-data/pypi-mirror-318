from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2beta1 import audio_config_pb2 as _audio_config_pb2
from google.cloud.dialogflow.v2beta1 import fulfillment_pb2 as _fulfillment_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Environment(_message.Message):
    __slots__ = ('name', 'description', 'agent_version', 'state', 'update_time', 'text_to_speech_settings', 'fulfillment')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Environment.State]
        STOPPED: _ClassVar[Environment.State]
        LOADING: _ClassVar[Environment.State]
        RUNNING: _ClassVar[Environment.State]
    STATE_UNSPECIFIED: Environment.State
    STOPPED: Environment.State
    LOADING: Environment.State
    RUNNING: Environment.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TEXT_TO_SPEECH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    agent_version: str
    state: Environment.State
    update_time: _timestamp_pb2.Timestamp
    text_to_speech_settings: TextToSpeechSettings
    fulfillment: _fulfillment_pb2.Fulfillment

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., agent_version: _Optional[str]=..., state: _Optional[_Union[Environment.State, str]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., text_to_speech_settings: _Optional[_Union[TextToSpeechSettings, _Mapping]]=..., fulfillment: _Optional[_Union[_fulfillment_pb2.Fulfillment, _Mapping]]=...) -> None:
        ...

class TextToSpeechSettings(_message.Message):
    __slots__ = ('enable_text_to_speech', 'output_audio_encoding', 'sample_rate_hertz', 'synthesize_speech_configs')

    class SynthesizeSpeechConfigsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _audio_config_pb2.SynthesizeSpeechConfig

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_audio_config_pb2.SynthesizeSpeechConfig, _Mapping]]=...) -> None:
            ...
    ENABLE_TEXT_TO_SPEECH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    SYNTHESIZE_SPEECH_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    enable_text_to_speech: bool
    output_audio_encoding: _audio_config_pb2.OutputAudioEncoding
    sample_rate_hertz: int
    synthesize_speech_configs: _containers.MessageMap[str, _audio_config_pb2.SynthesizeSpeechConfig]

    def __init__(self, enable_text_to_speech: bool=..., output_audio_encoding: _Optional[_Union[_audio_config_pb2.OutputAudioEncoding, str]]=..., sample_rate_hertz: _Optional[int]=..., synthesize_speech_configs: _Optional[_Mapping[str, _audio_config_pb2.SynthesizeSpeechConfig]]=...) -> None:
        ...

class ListEnvironmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ('environments', 'next_page_token')
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[Environment]
    next_page_token: str

    def __init__(self, environments: _Optional[_Iterable[_Union[Environment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEnvironmentRequest(_message.Message):
    __slots__ = ('parent', 'environment', 'environment_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    environment: Environment
    environment_id: str

    def __init__(self, parent: _Optional[str]=..., environment: _Optional[_Union[Environment, _Mapping]]=..., environment_id: _Optional[str]=...) -> None:
        ...

class UpdateEnvironmentRequest(_message.Message):
    __slots__ = ('environment', 'update_mask', 'allow_load_to_draft_and_discard_changes')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LOAD_TO_DRAFT_AND_DISCARD_CHANGES_FIELD_NUMBER: _ClassVar[int]
    environment: Environment
    update_mask: _field_mask_pb2.FieldMask
    allow_load_to_draft_and_discard_changes: bool

    def __init__(self, environment: _Optional[_Union[Environment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_load_to_draft_and_discard_changes: bool=...) -> None:
        ...

class DeleteEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetEnvironmentHistoryRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class EnvironmentHistory(_message.Message):
    __slots__ = ('parent', 'entries', 'next_page_token')

    class Entry(_message.Message):
        __slots__ = ('agent_version', 'description', 'create_time')
        AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        agent_version: str
        description: str
        create_time: _timestamp_pb2.Timestamp

        def __init__(self, agent_version: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entries: _containers.RepeatedCompositeFieldContainer[EnvironmentHistory.Entry]
    next_page_token: str

    def __init__(self, parent: _Optional[str]=..., entries: _Optional[_Iterable[_Union[EnvironmentHistory.Entry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...