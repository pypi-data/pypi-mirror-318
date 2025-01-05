from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.spanner.admin.database.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Backup(_message.Message):
    __slots__ = ('database', 'version_time', 'expire_time', 'name', 'create_time', 'size_bytes', 'freeable_size_bytes', 'exclusive_size_bytes', 'state', 'referencing_databases', 'encryption_info', 'encryption_information', 'database_dialect', 'referencing_backups', 'max_expire_time', 'backup_schedules', 'incremental_backup_chain_id', 'oldest_version_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Backup.State]
        CREATING: _ClassVar[Backup.State]
        READY: _ClassVar[Backup.State]
    STATE_UNSPECIFIED: Backup.State
    CREATING: Backup.State
    READY: Backup.State
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    VERSION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FREEABLE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REFERENCING_DATABASES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    DATABASE_DIALECT_FIELD_NUMBER: _ClassVar[int]
    REFERENCING_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    MAX_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_BACKUP_CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    OLDEST_VERSION_TIME_FIELD_NUMBER: _ClassVar[int]
    database: str
    version_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    name: str
    create_time: _timestamp_pb2.Timestamp
    size_bytes: int
    freeable_size_bytes: int
    exclusive_size_bytes: int
    state: Backup.State
    referencing_databases: _containers.RepeatedScalarFieldContainer[str]
    encryption_info: _common_pb2.EncryptionInfo
    encryption_information: _containers.RepeatedCompositeFieldContainer[_common_pb2.EncryptionInfo]
    database_dialect: _common_pb2.DatabaseDialect
    referencing_backups: _containers.RepeatedScalarFieldContainer[str]
    max_expire_time: _timestamp_pb2.Timestamp
    backup_schedules: _containers.RepeatedScalarFieldContainer[str]
    incremental_backup_chain_id: str
    oldest_version_time: _timestamp_pb2.Timestamp

    def __init__(self, database: _Optional[str]=..., version_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., size_bytes: _Optional[int]=..., freeable_size_bytes: _Optional[int]=..., exclusive_size_bytes: _Optional[int]=..., state: _Optional[_Union[Backup.State, str]]=..., referencing_databases: _Optional[_Iterable[str]]=..., encryption_info: _Optional[_Union[_common_pb2.EncryptionInfo, _Mapping]]=..., encryption_information: _Optional[_Iterable[_Union[_common_pb2.EncryptionInfo, _Mapping]]]=..., database_dialect: _Optional[_Union[_common_pb2.DatabaseDialect, str]]=..., referencing_backups: _Optional[_Iterable[str]]=..., max_expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., backup_schedules: _Optional[_Iterable[str]]=..., incremental_backup_chain_id: _Optional[str]=..., oldest_version_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateBackupRequest(_message.Message):
    __slots__ = ('parent', 'backup_id', 'backup', 'encryption_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_id: str
    backup: Backup
    encryption_config: CreateBackupEncryptionConfig

    def __init__(self, parent: _Optional[str]=..., backup_id: _Optional[str]=..., backup: _Optional[_Union[Backup, _Mapping]]=..., encryption_config: _Optional[_Union[CreateBackupEncryptionConfig, _Mapping]]=...) -> None:
        ...

class CreateBackupMetadata(_message.Message):
    __slots__ = ('name', 'database', 'progress', 'cancel_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    database: str
    progress: _common_pb2.OperationProgress
    cancel_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., database: _Optional[str]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CopyBackupRequest(_message.Message):
    __slots__ = ('parent', 'backup_id', 'source_backup', 'expire_time', 'encryption_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_id: str
    source_backup: str
    expire_time: _timestamp_pb2.Timestamp
    encryption_config: CopyBackupEncryptionConfig

    def __init__(self, parent: _Optional[str]=..., backup_id: _Optional[str]=..., source_backup: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., encryption_config: _Optional[_Union[CopyBackupEncryptionConfig, _Mapping]]=...) -> None:
        ...

class CopyBackupMetadata(_message.Message):
    __slots__ = ('name', 'source_backup', 'progress', 'cancel_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_backup: str
    progress: _common_pb2.OperationProgress
    cancel_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., source_backup: _Optional[str]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpdateBackupRequest(_message.Message):
    __slots__ = ('backup', 'update_mask')
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    backup: Backup
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, backup: _Optional[_Union[Backup, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBackupsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBackupsResponse(_message.Message):
    __slots__ = ('backups', 'next_page_token')
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[Backup]
    next_page_token: str

    def __init__(self, backups: _Optional[_Iterable[_Union[Backup, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListBackupOperationsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBackupOperationsResponse(_message.Message):
    __slots__ = ('operations', 'next_page_token')
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[_operations_pb2.Operation]
    next_page_token: str

    def __init__(self, operations: _Optional[_Iterable[_Union[_operations_pb2.Operation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class BackupInfo(_message.Message):
    __slots__ = ('backup', 'version_time', 'create_time', 'source_database')
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    VERSION_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    backup: str
    version_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    source_database: str

    def __init__(self, backup: _Optional[str]=..., version_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., source_database: _Optional[str]=...) -> None:
        ...

class CreateBackupEncryptionConfig(_message.Message):
    __slots__ = ('encryption_type', 'kms_key_name', 'kms_key_names')

    class EncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCRYPTION_TYPE_UNSPECIFIED: _ClassVar[CreateBackupEncryptionConfig.EncryptionType]
        USE_DATABASE_ENCRYPTION: _ClassVar[CreateBackupEncryptionConfig.EncryptionType]
        GOOGLE_DEFAULT_ENCRYPTION: _ClassVar[CreateBackupEncryptionConfig.EncryptionType]
        CUSTOMER_MANAGED_ENCRYPTION: _ClassVar[CreateBackupEncryptionConfig.EncryptionType]
    ENCRYPTION_TYPE_UNSPECIFIED: CreateBackupEncryptionConfig.EncryptionType
    USE_DATABASE_ENCRYPTION: CreateBackupEncryptionConfig.EncryptionType
    GOOGLE_DEFAULT_ENCRYPTION: CreateBackupEncryptionConfig.EncryptionType
    CUSTOMER_MANAGED_ENCRYPTION: CreateBackupEncryptionConfig.EncryptionType
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAMES_FIELD_NUMBER: _ClassVar[int]
    encryption_type: CreateBackupEncryptionConfig.EncryptionType
    kms_key_name: str
    kms_key_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, encryption_type: _Optional[_Union[CreateBackupEncryptionConfig.EncryptionType, str]]=..., kms_key_name: _Optional[str]=..., kms_key_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class CopyBackupEncryptionConfig(_message.Message):
    __slots__ = ('encryption_type', 'kms_key_name', 'kms_key_names')

    class EncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCRYPTION_TYPE_UNSPECIFIED: _ClassVar[CopyBackupEncryptionConfig.EncryptionType]
        USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION: _ClassVar[CopyBackupEncryptionConfig.EncryptionType]
        GOOGLE_DEFAULT_ENCRYPTION: _ClassVar[CopyBackupEncryptionConfig.EncryptionType]
        CUSTOMER_MANAGED_ENCRYPTION: _ClassVar[CopyBackupEncryptionConfig.EncryptionType]
    ENCRYPTION_TYPE_UNSPECIFIED: CopyBackupEncryptionConfig.EncryptionType
    USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION: CopyBackupEncryptionConfig.EncryptionType
    GOOGLE_DEFAULT_ENCRYPTION: CopyBackupEncryptionConfig.EncryptionType
    CUSTOMER_MANAGED_ENCRYPTION: CopyBackupEncryptionConfig.EncryptionType
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAMES_FIELD_NUMBER: _ClassVar[int]
    encryption_type: CopyBackupEncryptionConfig.EncryptionType
    kms_key_name: str
    kms_key_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, encryption_type: _Optional[_Union[CopyBackupEncryptionConfig.EncryptionType, str]]=..., kms_key_name: _Optional[str]=..., kms_key_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class FullBackupSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IncrementalBackupSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...