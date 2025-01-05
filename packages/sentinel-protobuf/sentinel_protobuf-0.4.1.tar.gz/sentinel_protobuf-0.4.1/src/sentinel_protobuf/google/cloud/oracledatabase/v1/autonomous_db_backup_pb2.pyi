from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutonomousDatabaseBackup(_message.Message):
    __slots__ = ('name', 'autonomous_database', 'display_name', 'properties', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTONOMOUS_DATABASE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    autonomous_database: str
    display_name: str
    properties: AutonomousDatabaseBackupProperties
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., autonomous_database: _Optional[str]=..., display_name: _Optional[str]=..., properties: _Optional[_Union[AutonomousDatabaseBackupProperties, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class AutonomousDatabaseBackupProperties(_message.Message):
    __slots__ = ('ocid', 'retention_period_days', 'compartment_id', 'database_size_tb', 'db_version', 'is_long_term_backup', 'is_automatic_backup', 'is_restorable', 'key_store_id', 'key_store_wallet', 'kms_key_id', 'kms_key_version_id', 'lifecycle_details', 'lifecycle_state', 'size_tb', 'available_till_time', 'end_time', 'start_time', 'type', 'vault_id')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AutonomousDatabaseBackupProperties.State]
        CREATING: _ClassVar[AutonomousDatabaseBackupProperties.State]
        ACTIVE: _ClassVar[AutonomousDatabaseBackupProperties.State]
        DELETING: _ClassVar[AutonomousDatabaseBackupProperties.State]
        DELETED: _ClassVar[AutonomousDatabaseBackupProperties.State]
        FAILED: _ClassVar[AutonomousDatabaseBackupProperties.State]
        UPDATING: _ClassVar[AutonomousDatabaseBackupProperties.State]
    STATE_UNSPECIFIED: AutonomousDatabaseBackupProperties.State
    CREATING: AutonomousDatabaseBackupProperties.State
    ACTIVE: AutonomousDatabaseBackupProperties.State
    DELETING: AutonomousDatabaseBackupProperties.State
    DELETED: AutonomousDatabaseBackupProperties.State
    FAILED: AutonomousDatabaseBackupProperties.State
    UPDATING: AutonomousDatabaseBackupProperties.State

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AutonomousDatabaseBackupProperties.Type]
        INCREMENTAL: _ClassVar[AutonomousDatabaseBackupProperties.Type]
        FULL: _ClassVar[AutonomousDatabaseBackupProperties.Type]
        LONG_TERM: _ClassVar[AutonomousDatabaseBackupProperties.Type]
    TYPE_UNSPECIFIED: AutonomousDatabaseBackupProperties.Type
    INCREMENTAL: AutonomousDatabaseBackupProperties.Type
    FULL: AutonomousDatabaseBackupProperties.Type
    LONG_TERM: AutonomousDatabaseBackupProperties.Type
    OCID_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_SIZE_TB_FIELD_NUMBER: _ClassVar[int]
    DB_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_LONG_TERM_BACKUP_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOMATIC_BACKUP_FIELD_NUMBER: _ClassVar[int]
    IS_RESTORABLE_FIELD_NUMBER: _ClassVar[int]
    KEY_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_STORE_WALLET_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    SIZE_TB_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TILL_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    ocid: str
    retention_period_days: int
    compartment_id: str
    database_size_tb: float
    db_version: str
    is_long_term_backup: bool
    is_automatic_backup: bool
    is_restorable: bool
    key_store_id: str
    key_store_wallet: str
    kms_key_id: str
    kms_key_version_id: str
    lifecycle_details: str
    lifecycle_state: AutonomousDatabaseBackupProperties.State
    size_tb: float
    available_till_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    type: AutonomousDatabaseBackupProperties.Type
    vault_id: str

    def __init__(self, ocid: _Optional[str]=..., retention_period_days: _Optional[int]=..., compartment_id: _Optional[str]=..., database_size_tb: _Optional[float]=..., db_version: _Optional[str]=..., is_long_term_backup: bool=..., is_automatic_backup: bool=..., is_restorable: bool=..., key_store_id: _Optional[str]=..., key_store_wallet: _Optional[str]=..., kms_key_id: _Optional[str]=..., kms_key_version_id: _Optional[str]=..., lifecycle_details: _Optional[str]=..., lifecycle_state: _Optional[_Union[AutonomousDatabaseBackupProperties.State, str]]=..., size_tb: _Optional[float]=..., available_till_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., type: _Optional[_Union[AutonomousDatabaseBackupProperties.Type, str]]=..., vault_id: _Optional[str]=...) -> None:
        ...