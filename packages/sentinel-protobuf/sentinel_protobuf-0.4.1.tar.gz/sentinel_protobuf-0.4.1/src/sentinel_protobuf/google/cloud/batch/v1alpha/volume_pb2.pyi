from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Volume(_message.Message):
    __slots__ = ('nfs', 'pd', 'gcs', 'device_name', 'mount_path', 'mount_options')
    NFS_FIELD_NUMBER: _ClassVar[int]
    PD_FIELD_NUMBER: _ClassVar[int]
    GCS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    MOUNT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    nfs: NFS
    pd: PD
    gcs: GCS
    device_name: str
    mount_path: str
    mount_options: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, nfs: _Optional[_Union[NFS, _Mapping]]=..., pd: _Optional[_Union[PD, _Mapping]]=..., gcs: _Optional[_Union[GCS, _Mapping]]=..., device_name: _Optional[str]=..., mount_path: _Optional[str]=..., mount_options: _Optional[_Iterable[str]]=...) -> None:
        ...

class NFS(_message.Message):
    __slots__ = ('server', 'remote_path')
    SERVER_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
    server: str
    remote_path: str

    def __init__(self, server: _Optional[str]=..., remote_path: _Optional[str]=...) -> None:
        ...

class PD(_message.Message):
    __slots__ = ('disk', 'device', 'existing')
    DISK_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_FIELD_NUMBER: _ClassVar[int]
    disk: str
    device: str
    existing: bool

    def __init__(self, disk: _Optional[str]=..., device: _Optional[str]=..., existing: bool=...) -> None:
        ...

class GCS(_message.Message):
    __slots__ = ('remote_path',)
    REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
    remote_path: str

    def __init__(self, remote_path: _Optional[str]=...) -> None:
        ...