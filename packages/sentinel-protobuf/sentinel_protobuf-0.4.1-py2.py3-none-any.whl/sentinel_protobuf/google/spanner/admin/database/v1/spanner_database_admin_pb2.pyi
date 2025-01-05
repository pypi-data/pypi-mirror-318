from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.spanner.admin.database.v1 import backup_pb2 as _backup_pb2
from google.spanner.admin.database.v1 import backup_schedule_pb2 as _backup_schedule_pb2
from google.spanner.admin.database.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RestoreSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNSPECIFIED: _ClassVar[RestoreSourceType]
    BACKUP: _ClassVar[RestoreSourceType]
TYPE_UNSPECIFIED: RestoreSourceType
BACKUP: RestoreSourceType

class RestoreInfo(_message.Message):
    __slots__ = ('source_type', 'backup_info')
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    source_type: RestoreSourceType
    backup_info: _backup_pb2.BackupInfo

    def __init__(self, source_type: _Optional[_Union[RestoreSourceType, str]]=..., backup_info: _Optional[_Union[_backup_pb2.BackupInfo, _Mapping]]=...) -> None:
        ...

class Database(_message.Message):
    __slots__ = ('name', 'state', 'create_time', 'restore_info', 'encryption_config', 'encryption_info', 'version_retention_period', 'earliest_version_time', 'default_leader', 'database_dialect', 'enable_drop_protection', 'reconciling')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Database.State]
        CREATING: _ClassVar[Database.State]
        READY: _ClassVar[Database.State]
        READY_OPTIMIZING: _ClassVar[Database.State]
    STATE_UNSPECIFIED: Database.State
    CREATING: Database.State
    READY: Database.State
    READY_OPTIMIZING: Database.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    VERSION_RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_VERSION_TIME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LEADER_FIELD_NUMBER: _ClassVar[int]
    DATABASE_DIALECT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DROP_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Database.State
    create_time: _timestamp_pb2.Timestamp
    restore_info: RestoreInfo
    encryption_config: _common_pb2.EncryptionConfig
    encryption_info: _containers.RepeatedCompositeFieldContainer[_common_pb2.EncryptionInfo]
    version_retention_period: str
    earliest_version_time: _timestamp_pb2.Timestamp
    default_leader: str
    database_dialect: _common_pb2.DatabaseDialect
    enable_drop_protection: bool
    reconciling: bool

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[Database.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., restore_info: _Optional[_Union[RestoreInfo, _Mapping]]=..., encryption_config: _Optional[_Union[_common_pb2.EncryptionConfig, _Mapping]]=..., encryption_info: _Optional[_Iterable[_Union[_common_pb2.EncryptionInfo, _Mapping]]]=..., version_retention_period: _Optional[str]=..., earliest_version_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., default_leader: _Optional[str]=..., database_dialect: _Optional[_Union[_common_pb2.DatabaseDialect, str]]=..., enable_drop_protection: bool=..., reconciling: bool=...) -> None:
        ...

class ListDatabasesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDatabasesResponse(_message.Message):
    __slots__ = ('databases', 'next_page_token')
    DATABASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    databases: _containers.RepeatedCompositeFieldContainer[Database]
    next_page_token: str

    def __init__(self, databases: _Optional[_Iterable[_Union[Database, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateDatabaseRequest(_message.Message):
    __slots__ = ('parent', 'create_statement', 'extra_statements', 'encryption_config', 'database_dialect', 'proto_descriptors')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATABASE_DIALECT_FIELD_NUMBER: _ClassVar[int]
    PROTO_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    create_statement: str
    extra_statements: _containers.RepeatedScalarFieldContainer[str]
    encryption_config: _common_pb2.EncryptionConfig
    database_dialect: _common_pb2.DatabaseDialect
    proto_descriptors: bytes

    def __init__(self, parent: _Optional[str]=..., create_statement: _Optional[str]=..., extra_statements: _Optional[_Iterable[str]]=..., encryption_config: _Optional[_Union[_common_pb2.EncryptionConfig, _Mapping]]=..., database_dialect: _Optional[_Union[_common_pb2.DatabaseDialect, str]]=..., proto_descriptors: _Optional[bytes]=...) -> None:
        ...

class CreateDatabaseMetadata(_message.Message):
    __slots__ = ('database',)
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    database: str

    def __init__(self, database: _Optional[str]=...) -> None:
        ...

class GetDatabaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDatabaseRequest(_message.Message):
    __slots__ = ('database', 'update_mask')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    database: Database
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, database: _Optional[_Union[Database, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateDatabaseMetadata(_message.Message):
    __slots__ = ('request', 'progress', 'cancel_time')
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    request: UpdateDatabaseRequest
    progress: _common_pb2.OperationProgress
    cancel_time: _timestamp_pb2.Timestamp

    def __init__(self, request: _Optional[_Union[UpdateDatabaseRequest, _Mapping]]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpdateDatabaseDdlRequest(_message.Message):
    __slots__ = ('database', 'statements', 'operation_id', 'proto_descriptors')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROTO_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    database: str
    statements: _containers.RepeatedScalarFieldContainer[str]
    operation_id: str
    proto_descriptors: bytes

    def __init__(self, database: _Optional[str]=..., statements: _Optional[_Iterable[str]]=..., operation_id: _Optional[str]=..., proto_descriptors: _Optional[bytes]=...) -> None:
        ...

class DdlStatementActionInfo(_message.Message):
    __slots__ = ('action', 'entity_type', 'entity_names')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAMES_FIELD_NUMBER: _ClassVar[int]
    action: str
    entity_type: str
    entity_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, action: _Optional[str]=..., entity_type: _Optional[str]=..., entity_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateDatabaseDdlMetadata(_message.Message):
    __slots__ = ('database', 'statements', 'commit_timestamps', 'throttled', 'progress', 'actions')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMIT_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    THROTTLED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    database: str
    statements: _containers.RepeatedScalarFieldContainer[str]
    commit_timestamps: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    throttled: bool
    progress: _containers.RepeatedCompositeFieldContainer[_common_pb2.OperationProgress]
    actions: _containers.RepeatedCompositeFieldContainer[DdlStatementActionInfo]

    def __init__(self, database: _Optional[str]=..., statements: _Optional[_Iterable[str]]=..., commit_timestamps: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]]=..., throttled: bool=..., progress: _Optional[_Iterable[_Union[_common_pb2.OperationProgress, _Mapping]]]=..., actions: _Optional[_Iterable[_Union[DdlStatementActionInfo, _Mapping]]]=...) -> None:
        ...

class DropDatabaseRequest(_message.Message):
    __slots__ = ('database',)
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    database: str

    def __init__(self, database: _Optional[str]=...) -> None:
        ...

class GetDatabaseDdlRequest(_message.Message):
    __slots__ = ('database',)
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    database: str

    def __init__(self, database: _Optional[str]=...) -> None:
        ...

class GetDatabaseDdlResponse(_message.Message):
    __slots__ = ('statements', 'proto_descriptors')
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    PROTO_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    statements: _containers.RepeatedScalarFieldContainer[str]
    proto_descriptors: bytes

    def __init__(self, statements: _Optional[_Iterable[str]]=..., proto_descriptors: _Optional[bytes]=...) -> None:
        ...

class ListDatabaseOperationsRequest(_message.Message):
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

class ListDatabaseOperationsResponse(_message.Message):
    __slots__ = ('operations', 'next_page_token')
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[_operations_pb2.Operation]
    next_page_token: str

    def __init__(self, operations: _Optional[_Iterable[_Union[_operations_pb2.Operation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class RestoreDatabaseRequest(_message.Message):
    __slots__ = ('parent', 'database_id', 'backup', 'encryption_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    database_id: str
    backup: str
    encryption_config: RestoreDatabaseEncryptionConfig

    def __init__(self, parent: _Optional[str]=..., database_id: _Optional[str]=..., backup: _Optional[str]=..., encryption_config: _Optional[_Union[RestoreDatabaseEncryptionConfig, _Mapping]]=...) -> None:
        ...

class RestoreDatabaseEncryptionConfig(_message.Message):
    __slots__ = ('encryption_type', 'kms_key_name', 'kms_key_names')

    class EncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCRYPTION_TYPE_UNSPECIFIED: _ClassVar[RestoreDatabaseEncryptionConfig.EncryptionType]
        USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION: _ClassVar[RestoreDatabaseEncryptionConfig.EncryptionType]
        GOOGLE_DEFAULT_ENCRYPTION: _ClassVar[RestoreDatabaseEncryptionConfig.EncryptionType]
        CUSTOMER_MANAGED_ENCRYPTION: _ClassVar[RestoreDatabaseEncryptionConfig.EncryptionType]
    ENCRYPTION_TYPE_UNSPECIFIED: RestoreDatabaseEncryptionConfig.EncryptionType
    USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION: RestoreDatabaseEncryptionConfig.EncryptionType
    GOOGLE_DEFAULT_ENCRYPTION: RestoreDatabaseEncryptionConfig.EncryptionType
    CUSTOMER_MANAGED_ENCRYPTION: RestoreDatabaseEncryptionConfig.EncryptionType
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAMES_FIELD_NUMBER: _ClassVar[int]
    encryption_type: RestoreDatabaseEncryptionConfig.EncryptionType
    kms_key_name: str
    kms_key_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, encryption_type: _Optional[_Union[RestoreDatabaseEncryptionConfig.EncryptionType, str]]=..., kms_key_name: _Optional[str]=..., kms_key_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class RestoreDatabaseMetadata(_message.Message):
    __slots__ = ('name', 'source_type', 'backup_info', 'progress', 'cancel_time', 'optimize_database_operation_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIME_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZE_DATABASE_OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_type: RestoreSourceType
    backup_info: _backup_pb2.BackupInfo
    progress: _common_pb2.OperationProgress
    cancel_time: _timestamp_pb2.Timestamp
    optimize_database_operation_name: str

    def __init__(self, name: _Optional[str]=..., source_type: _Optional[_Union[RestoreSourceType, str]]=..., backup_info: _Optional[_Union[_backup_pb2.BackupInfo, _Mapping]]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=..., cancel_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., optimize_database_operation_name: _Optional[str]=...) -> None:
        ...

class OptimizeRestoredDatabaseMetadata(_message.Message):
    __slots__ = ('name', 'progress')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    progress: _common_pb2.OperationProgress

    def __init__(self, name: _Optional[str]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=...) -> None:
        ...

class DatabaseRole(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDatabaseRolesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDatabaseRolesResponse(_message.Message):
    __slots__ = ('database_roles', 'next_page_token')
    DATABASE_ROLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    database_roles: _containers.RepeatedCompositeFieldContainer[DatabaseRole]
    next_page_token: str

    def __init__(self, database_roles: _Optional[_Iterable[_Union[DatabaseRole, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...