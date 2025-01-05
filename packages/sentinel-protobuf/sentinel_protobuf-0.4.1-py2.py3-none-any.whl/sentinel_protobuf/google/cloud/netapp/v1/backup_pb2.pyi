from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Backup(_message.Message):
    __slots__ = ("name", "state", "description", "volume_usage_bytes", "backup_type", "source_volume", "source_snapshot", "create_time", "labels", "chain_storage_bytes")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Backup.State]
        CREATING: _ClassVar[Backup.State]
        UPLOADING: _ClassVar[Backup.State]
        READY: _ClassVar[Backup.State]
        DELETING: _ClassVar[Backup.State]
        ERROR: _ClassVar[Backup.State]
        UPDATING: _ClassVar[Backup.State]
    STATE_UNSPECIFIED: Backup.State
    CREATING: Backup.State
    UPLOADING: Backup.State
    READY: Backup.State
    DELETING: Backup.State
    ERROR: Backup.State
    UPDATING: Backup.State
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Backup.Type]
        MANUAL: _ClassVar[Backup.Type]
        SCHEDULED: _ClassVar[Backup.Type]
    TYPE_UNSPECIFIED: Backup.Type
    MANUAL: Backup.Type
    SCHEDULED: Backup.Type
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VOLUME_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CHAIN_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Backup.State
    description: str
    volume_usage_bytes: int
    backup_type: Backup.Type
    source_volume: str
    source_snapshot: str
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    chain_storage_bytes: int
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[Backup.State, str]] = ..., description: _Optional[str] = ..., volume_usage_bytes: _Optional[int] = ..., backup_type: _Optional[_Union[Backup.Type, str]] = ..., source_volume: _Optional[str] = ..., source_snapshot: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., chain_storage_bytes: _Optional[int] = ...) -> None: ...

class ListBackupsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "order_by", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListBackupsResponse(_message.Message):
    __slots__ = ("backups", "next_page_token", "unreachable")
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[Backup]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, backups: _Optional[_Iterable[_Union[Backup, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBackupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateBackupRequest(_message.Message):
    __slots__ = ("parent", "backup_id", "backup")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_id: str
    backup: Backup
    def __init__(self, parent: _Optional[str] = ..., backup_id: _Optional[str] = ..., backup: _Optional[_Union[Backup, _Mapping]] = ...) -> None: ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateBackupRequest(_message.Message):
    __slots__ = ("update_mask", "backup")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    backup: Backup
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., backup: _Optional[_Union[Backup, _Mapping]] = ...) -> None: ...
