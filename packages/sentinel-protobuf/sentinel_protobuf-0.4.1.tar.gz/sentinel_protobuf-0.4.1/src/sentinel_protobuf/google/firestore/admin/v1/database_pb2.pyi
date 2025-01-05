from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Database(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'delete_time', 'location_id', 'type', 'concurrency_mode', 'version_retention_period', 'earliest_version_time', 'point_in_time_recovery_enablement', 'app_engine_integration_mode', 'key_prefix', 'delete_protection_state', 'cmek_config', 'previous_id', 'source_info', 'etag')

    class DatabaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATABASE_TYPE_UNSPECIFIED: _ClassVar[Database.DatabaseType]
        FIRESTORE_NATIVE: _ClassVar[Database.DatabaseType]
        DATASTORE_MODE: _ClassVar[Database.DatabaseType]
    DATABASE_TYPE_UNSPECIFIED: Database.DatabaseType
    FIRESTORE_NATIVE: Database.DatabaseType
    DATASTORE_MODE: Database.DatabaseType

    class ConcurrencyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONCURRENCY_MODE_UNSPECIFIED: _ClassVar[Database.ConcurrencyMode]
        OPTIMISTIC: _ClassVar[Database.ConcurrencyMode]
        PESSIMISTIC: _ClassVar[Database.ConcurrencyMode]
        OPTIMISTIC_WITH_ENTITY_GROUPS: _ClassVar[Database.ConcurrencyMode]
    CONCURRENCY_MODE_UNSPECIFIED: Database.ConcurrencyMode
    OPTIMISTIC: Database.ConcurrencyMode
    PESSIMISTIC: Database.ConcurrencyMode
    OPTIMISTIC_WITH_ENTITY_GROUPS: Database.ConcurrencyMode

    class PointInTimeRecoveryEnablement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POINT_IN_TIME_RECOVERY_ENABLEMENT_UNSPECIFIED: _ClassVar[Database.PointInTimeRecoveryEnablement]
        POINT_IN_TIME_RECOVERY_ENABLED: _ClassVar[Database.PointInTimeRecoveryEnablement]
        POINT_IN_TIME_RECOVERY_DISABLED: _ClassVar[Database.PointInTimeRecoveryEnablement]
    POINT_IN_TIME_RECOVERY_ENABLEMENT_UNSPECIFIED: Database.PointInTimeRecoveryEnablement
    POINT_IN_TIME_RECOVERY_ENABLED: Database.PointInTimeRecoveryEnablement
    POINT_IN_TIME_RECOVERY_DISABLED: Database.PointInTimeRecoveryEnablement

    class AppEngineIntegrationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        APP_ENGINE_INTEGRATION_MODE_UNSPECIFIED: _ClassVar[Database.AppEngineIntegrationMode]
        ENABLED: _ClassVar[Database.AppEngineIntegrationMode]
        DISABLED: _ClassVar[Database.AppEngineIntegrationMode]
    APP_ENGINE_INTEGRATION_MODE_UNSPECIFIED: Database.AppEngineIntegrationMode
    ENABLED: Database.AppEngineIntegrationMode
    DISABLED: Database.AppEngineIntegrationMode

    class DeleteProtectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DELETE_PROTECTION_STATE_UNSPECIFIED: _ClassVar[Database.DeleteProtectionState]
        DELETE_PROTECTION_DISABLED: _ClassVar[Database.DeleteProtectionState]
        DELETE_PROTECTION_ENABLED: _ClassVar[Database.DeleteProtectionState]
    DELETE_PROTECTION_STATE_UNSPECIFIED: Database.DeleteProtectionState
    DELETE_PROTECTION_DISABLED: Database.DeleteProtectionState
    DELETE_PROTECTION_ENABLED: Database.DeleteProtectionState

    class CmekConfig(_message.Message):
        __slots__ = ('kms_key_name', 'active_key_version')
        KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
        kms_key_name: str
        active_key_version: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, kms_key_name: _Optional[str]=..., active_key_version: _Optional[_Iterable[str]]=...) -> None:
            ...

    class SourceInfo(_message.Message):
        __slots__ = ('backup', 'operation')

        class BackupSource(_message.Message):
            __slots__ = ('backup',)
            BACKUP_FIELD_NUMBER: _ClassVar[int]
            backup: str

            def __init__(self, backup: _Optional[str]=...) -> None:
                ...
        BACKUP_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        backup: Database.SourceInfo.BackupSource
        operation: str

        def __init__(self, backup: _Optional[_Union[Database.SourceInfo.BackupSource, _Mapping]]=..., operation: _Optional[str]=...) -> None:
            ...

    class EncryptionConfig(_message.Message):
        __slots__ = ('google_default_encryption', 'use_source_encryption', 'customer_managed_encryption')

        class GoogleDefaultEncryptionOptions(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class SourceEncryptionOptions(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class CustomerManagedEncryptionOptions(_message.Message):
            __slots__ = ('kms_key_name',)
            KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
            kms_key_name: str

            def __init__(self, kms_key_name: _Optional[str]=...) -> None:
                ...
        GOOGLE_DEFAULT_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        USE_SOURCE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        CUSTOMER_MANAGED_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        google_default_encryption: Database.EncryptionConfig.GoogleDefaultEncryptionOptions
        use_source_encryption: Database.EncryptionConfig.SourceEncryptionOptions
        customer_managed_encryption: Database.EncryptionConfig.CustomerManagedEncryptionOptions

        def __init__(self, google_default_encryption: _Optional[_Union[Database.EncryptionConfig.GoogleDefaultEncryptionOptions, _Mapping]]=..., use_source_encryption: _Optional[_Union[Database.EncryptionConfig.SourceEncryptionOptions, _Mapping]]=..., customer_managed_encryption: _Optional[_Union[Database.EncryptionConfig.CustomerManagedEncryptionOptions, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_MODE_FIELD_NUMBER: _ClassVar[int]
    VERSION_RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_VERSION_TIME_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_RECOVERY_ENABLEMENT_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_INTEGRATION_MODE_FIELD_NUMBER: _ClassVar[int]
    KEY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DELETE_PROTECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    CMEK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    location_id: str
    type: Database.DatabaseType
    concurrency_mode: Database.ConcurrencyMode
    version_retention_period: _duration_pb2.Duration
    earliest_version_time: _timestamp_pb2.Timestamp
    point_in_time_recovery_enablement: Database.PointInTimeRecoveryEnablement
    app_engine_integration_mode: Database.AppEngineIntegrationMode
    key_prefix: str
    delete_protection_state: Database.DeleteProtectionState
    cmek_config: Database.CmekConfig
    previous_id: str
    source_info: Database.SourceInfo
    etag: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., location_id: _Optional[str]=..., type: _Optional[_Union[Database.DatabaseType, str]]=..., concurrency_mode: _Optional[_Union[Database.ConcurrencyMode, str]]=..., version_retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., earliest_version_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., point_in_time_recovery_enablement: _Optional[_Union[Database.PointInTimeRecoveryEnablement, str]]=..., app_engine_integration_mode: _Optional[_Union[Database.AppEngineIntegrationMode, str]]=..., key_prefix: _Optional[str]=..., delete_protection_state: _Optional[_Union[Database.DeleteProtectionState, str]]=..., cmek_config: _Optional[_Union[Database.CmekConfig, _Mapping]]=..., previous_id: _Optional[str]=..., source_info: _Optional[_Union[Database.SourceInfo, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...