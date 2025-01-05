from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkebackup.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VolumeBackup(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'source_pvc', 'volume_backup_handle', 'format', 'storage_bytes', 'disk_size_bytes', 'complete_time', 'state', 'state_message', 'etag')

    class VolumeBackupFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOLUME_BACKUP_FORMAT_UNSPECIFIED: _ClassVar[VolumeBackup.VolumeBackupFormat]
        GCE_PERSISTENT_DISK: _ClassVar[VolumeBackup.VolumeBackupFormat]
    VOLUME_BACKUP_FORMAT_UNSPECIFIED: VolumeBackup.VolumeBackupFormat
    GCE_PERSISTENT_DISK: VolumeBackup.VolumeBackupFormat

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[VolumeBackup.State]
        CREATING: _ClassVar[VolumeBackup.State]
        SNAPSHOTTING: _ClassVar[VolumeBackup.State]
        UPLOADING: _ClassVar[VolumeBackup.State]
        SUCCEEDED: _ClassVar[VolumeBackup.State]
        FAILED: _ClassVar[VolumeBackup.State]
        DELETING: _ClassVar[VolumeBackup.State]
    STATE_UNSPECIFIED: VolumeBackup.State
    CREATING: VolumeBackup.State
    SNAPSHOTTING: VolumeBackup.State
    UPLOADING: VolumeBackup.State
    SUCCEEDED: VolumeBackup.State
    FAILED: VolumeBackup.State
    DELETING: VolumeBackup.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PVC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_BACKUP_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    source_pvc: _common_pb2.NamespacedName
    volume_backup_handle: str
    format: VolumeBackup.VolumeBackupFormat
    storage_bytes: int
    disk_size_bytes: int
    complete_time: _timestamp_pb2.Timestamp
    state: VolumeBackup.State
    state_message: str
    etag: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., source_pvc: _Optional[_Union[_common_pb2.NamespacedName, _Mapping]]=..., volume_backup_handle: _Optional[str]=..., format: _Optional[_Union[VolumeBackup.VolumeBackupFormat, str]]=..., storage_bytes: _Optional[int]=..., disk_size_bytes: _Optional[int]=..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[VolumeBackup.State, str]]=..., state_message: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class VolumeRestore(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'volume_backup', 'target_pvc', 'volume_handle', 'volume_type', 'complete_time', 'state', 'state_message', 'etag')

    class VolumeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOLUME_TYPE_UNSPECIFIED: _ClassVar[VolumeRestore.VolumeType]
        GCE_PERSISTENT_DISK: _ClassVar[VolumeRestore.VolumeType]
    VOLUME_TYPE_UNSPECIFIED: VolumeRestore.VolumeType
    GCE_PERSISTENT_DISK: VolumeRestore.VolumeType

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[VolumeRestore.State]
        CREATING: _ClassVar[VolumeRestore.State]
        RESTORING: _ClassVar[VolumeRestore.State]
        SUCCEEDED: _ClassVar[VolumeRestore.State]
        FAILED: _ClassVar[VolumeRestore.State]
        DELETING: _ClassVar[VolumeRestore.State]
    STATE_UNSPECIFIED: VolumeRestore.State
    CREATING: VolumeRestore.State
    RESTORING: VolumeRestore.State
    SUCCEEDED: VolumeRestore.State
    FAILED: VolumeRestore.State
    DELETING: VolumeRestore.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_BACKUP_FIELD_NUMBER: _ClassVar[int]
    TARGET_PVC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_HANDLE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    volume_backup: str
    target_pvc: _common_pb2.NamespacedName
    volume_handle: str
    volume_type: VolumeRestore.VolumeType
    complete_time: _timestamp_pb2.Timestamp
    state: VolumeRestore.State
    state_message: str
    etag: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., volume_backup: _Optional[str]=..., target_pvc: _Optional[_Union[_common_pb2.NamespacedName, _Mapping]]=..., volume_handle: _Optional[str]=..., volume_type: _Optional[_Union[VolumeRestore.VolumeType, str]]=..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[VolumeRestore.State, str]]=..., state_message: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...