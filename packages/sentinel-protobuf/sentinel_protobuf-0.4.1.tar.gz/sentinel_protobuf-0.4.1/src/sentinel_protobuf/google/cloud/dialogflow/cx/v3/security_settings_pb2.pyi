from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetSecuritySettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSecuritySettingsRequest(_message.Message):
    __slots__ = ('security_settings', 'update_mask')
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    security_settings: SecuritySettings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, security_settings: _Optional[_Union[SecuritySettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListSecuritySettingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSecuritySettingsResponse(_message.Message):
    __slots__ = ('security_settings', 'next_page_token')
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    security_settings: _containers.RepeatedCompositeFieldContainer[SecuritySettings]
    next_page_token: str

    def __init__(self, security_settings: _Optional[_Iterable[_Union[SecuritySettings, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateSecuritySettingsRequest(_message.Message):
    __slots__ = ('parent', 'security_settings')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    security_settings: SecuritySettings

    def __init__(self, parent: _Optional[str]=..., security_settings: _Optional[_Union[SecuritySettings, _Mapping]]=...) -> None:
        ...

class DeleteSecuritySettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SecuritySettings(_message.Message):
    __slots__ = ('name', 'display_name', 'redaction_strategy', 'redaction_scope', 'inspect_template', 'deidentify_template', 'retention_window_days', 'retention_strategy', 'purge_data_types', 'audio_export_settings', 'insights_export_settings')

    class RedactionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REDACTION_STRATEGY_UNSPECIFIED: _ClassVar[SecuritySettings.RedactionStrategy]
        REDACT_WITH_SERVICE: _ClassVar[SecuritySettings.RedactionStrategy]
    REDACTION_STRATEGY_UNSPECIFIED: SecuritySettings.RedactionStrategy
    REDACT_WITH_SERVICE: SecuritySettings.RedactionStrategy

    class RedactionScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REDACTION_SCOPE_UNSPECIFIED: _ClassVar[SecuritySettings.RedactionScope]
        REDACT_DISK_STORAGE: _ClassVar[SecuritySettings.RedactionScope]
    REDACTION_SCOPE_UNSPECIFIED: SecuritySettings.RedactionScope
    REDACT_DISK_STORAGE: SecuritySettings.RedactionScope

    class RetentionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETENTION_STRATEGY_UNSPECIFIED: _ClassVar[SecuritySettings.RetentionStrategy]
        REMOVE_AFTER_CONVERSATION: _ClassVar[SecuritySettings.RetentionStrategy]
    RETENTION_STRATEGY_UNSPECIFIED: SecuritySettings.RetentionStrategy
    REMOVE_AFTER_CONVERSATION: SecuritySettings.RetentionStrategy

    class PurgeDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PURGE_DATA_TYPE_UNSPECIFIED: _ClassVar[SecuritySettings.PurgeDataType]
        DIALOGFLOW_HISTORY: _ClassVar[SecuritySettings.PurgeDataType]
    PURGE_DATA_TYPE_UNSPECIFIED: SecuritySettings.PurgeDataType
    DIALOGFLOW_HISTORY: SecuritySettings.PurgeDataType

    class AudioExportSettings(_message.Message):
        __slots__ = ('gcs_bucket', 'audio_export_pattern', 'enable_audio_redaction', 'audio_format', 'store_tts_audio')

        class AudioFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AUDIO_FORMAT_UNSPECIFIED: _ClassVar[SecuritySettings.AudioExportSettings.AudioFormat]
            MULAW: _ClassVar[SecuritySettings.AudioExportSettings.AudioFormat]
            MP3: _ClassVar[SecuritySettings.AudioExportSettings.AudioFormat]
            OGG: _ClassVar[SecuritySettings.AudioExportSettings.AudioFormat]
        AUDIO_FORMAT_UNSPECIFIED: SecuritySettings.AudioExportSettings.AudioFormat
        MULAW: SecuritySettings.AudioExportSettings.AudioFormat
        MP3: SecuritySettings.AudioExportSettings.AudioFormat
        OGG: SecuritySettings.AudioExportSettings.AudioFormat
        GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
        AUDIO_EXPORT_PATTERN_FIELD_NUMBER: _ClassVar[int]
        ENABLE_AUDIO_REDACTION_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
        STORE_TTS_AUDIO_FIELD_NUMBER: _ClassVar[int]
        gcs_bucket: str
        audio_export_pattern: str
        enable_audio_redaction: bool
        audio_format: SecuritySettings.AudioExportSettings.AudioFormat
        store_tts_audio: bool

        def __init__(self, gcs_bucket: _Optional[str]=..., audio_export_pattern: _Optional[str]=..., enable_audio_redaction: bool=..., audio_format: _Optional[_Union[SecuritySettings.AudioExportSettings.AudioFormat, str]]=..., store_tts_audio: bool=...) -> None:
            ...

    class InsightsExportSettings(_message.Message):
        __slots__ = ('enable_insights_export',)
        ENABLE_INSIGHTS_EXPORT_FIELD_NUMBER: _ClassVar[int]
        enable_insights_export: bool

        def __init__(self, enable_insights_export: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    REDACTION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    REDACTION_SCOPE_FIELD_NUMBER: _ClassVar[int]
    INSPECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DEIDENTIFY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PURGE_DATA_TYPES_FIELD_NUMBER: _ClassVar[int]
    AUDIO_EXPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_EXPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    redaction_strategy: SecuritySettings.RedactionStrategy
    redaction_scope: SecuritySettings.RedactionScope
    inspect_template: str
    deidentify_template: str
    retention_window_days: int
    retention_strategy: SecuritySettings.RetentionStrategy
    purge_data_types: _containers.RepeatedScalarFieldContainer[SecuritySettings.PurgeDataType]
    audio_export_settings: SecuritySettings.AudioExportSettings
    insights_export_settings: SecuritySettings.InsightsExportSettings

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., redaction_strategy: _Optional[_Union[SecuritySettings.RedactionStrategy, str]]=..., redaction_scope: _Optional[_Union[SecuritySettings.RedactionScope, str]]=..., inspect_template: _Optional[str]=..., deidentify_template: _Optional[str]=..., retention_window_days: _Optional[int]=..., retention_strategy: _Optional[_Union[SecuritySettings.RetentionStrategy, str]]=..., purge_data_types: _Optional[_Iterable[_Union[SecuritySettings.PurgeDataType, str]]]=..., audio_export_settings: _Optional[_Union[SecuritySettings.AudioExportSettings, _Mapping]]=..., insights_export_settings: _Optional[_Union[SecuritySettings.InsightsExportSettings, _Mapping]]=...) -> None:
        ...