from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NfsShare(_message.Message):
    __slots__ = ('name', 'nfs_share_id', 'id', 'state', 'volume', 'allowed_clients', 'labels', 'requested_size_gib', 'storage_type')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[NfsShare.State]
        PROVISIONED: _ClassVar[NfsShare.State]
        CREATING: _ClassVar[NfsShare.State]
        UPDATING: _ClassVar[NfsShare.State]
        DELETING: _ClassVar[NfsShare.State]
    STATE_UNSPECIFIED: NfsShare.State
    PROVISIONED: NfsShare.State
    CREATING: NfsShare.State
    UPDATING: NfsShare.State
    DELETING: NfsShare.State

    class MountPermissions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOUNT_PERMISSIONS_UNSPECIFIED: _ClassVar[NfsShare.MountPermissions]
        READ: _ClassVar[NfsShare.MountPermissions]
        READ_WRITE: _ClassVar[NfsShare.MountPermissions]
    MOUNT_PERMISSIONS_UNSPECIFIED: NfsShare.MountPermissions
    READ: NfsShare.MountPermissions
    READ_WRITE: NfsShare.MountPermissions

    class StorageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_TYPE_UNSPECIFIED: _ClassVar[NfsShare.StorageType]
        SSD: _ClassVar[NfsShare.StorageType]
        HDD: _ClassVar[NfsShare.StorageType]
    STORAGE_TYPE_UNSPECIFIED: NfsShare.StorageType
    SSD: NfsShare.StorageType
    HDD: NfsShare.StorageType

    class AllowedClient(_message.Message):
        __slots__ = ('network', 'share_ip', 'allowed_clients_cidr', 'mount_permissions', 'allow_dev', 'allow_suid', 'no_root_squash', 'nfs_path')
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        SHARE_IP_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_CLIENTS_CIDR_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_DEV_FIELD_NUMBER: _ClassVar[int]
        ALLOW_SUID_FIELD_NUMBER: _ClassVar[int]
        NO_ROOT_SQUASH_FIELD_NUMBER: _ClassVar[int]
        NFS_PATH_FIELD_NUMBER: _ClassVar[int]
        network: str
        share_ip: str
        allowed_clients_cidr: str
        mount_permissions: NfsShare.MountPermissions
        allow_dev: bool
        allow_suid: bool
        no_root_squash: bool
        nfs_path: str

        def __init__(self, network: _Optional[str]=..., share_ip: _Optional[str]=..., allowed_clients_cidr: _Optional[str]=..., mount_permissions: _Optional[_Union[NfsShare.MountPermissions, str]]=..., allow_dev: bool=..., allow_suid: bool=..., no_root_squash: bool=..., nfs_path: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NFS_SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    nfs_share_id: str
    id: str
    state: NfsShare.State
    volume: str
    allowed_clients: _containers.RepeatedCompositeFieldContainer[NfsShare.AllowedClient]
    labels: _containers.ScalarMap[str, str]
    requested_size_gib: int
    storage_type: NfsShare.StorageType

    def __init__(self, name: _Optional[str]=..., nfs_share_id: _Optional[str]=..., id: _Optional[str]=..., state: _Optional[_Union[NfsShare.State, str]]=..., volume: _Optional[str]=..., allowed_clients: _Optional[_Iterable[_Union[NfsShare.AllowedClient, _Mapping]]]=..., labels: _Optional[_Mapping[str, str]]=..., requested_size_gib: _Optional[int]=..., storage_type: _Optional[_Union[NfsShare.StorageType, str]]=...) -> None:
        ...

class GetNfsShareRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListNfsSharesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListNfsSharesResponse(_message.Message):
    __slots__ = ('nfs_shares', 'next_page_token', 'unreachable')
    NFS_SHARES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    nfs_shares: _containers.RepeatedCompositeFieldContainer[NfsShare]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, nfs_shares: _Optional[_Iterable[_Union[NfsShare, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateNfsShareRequest(_message.Message):
    __slots__ = ('nfs_share', 'update_mask')
    NFS_SHARE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    nfs_share: NfsShare
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, nfs_share: _Optional[_Union[NfsShare, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class RenameNfsShareRequest(_message.Message):
    __slots__ = ('name', 'new_nfsshare_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NFSSHARE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_nfsshare_id: str

    def __init__(self, name: _Optional[str]=..., new_nfsshare_id: _Optional[str]=...) -> None:
        ...

class CreateNfsShareRequest(_message.Message):
    __slots__ = ('parent', 'nfs_share')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NFS_SHARE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    nfs_share: NfsShare

    def __init__(self, parent: _Optional[str]=..., nfs_share: _Optional[_Union[NfsShare, _Mapping]]=...) -> None:
        ...

class DeleteNfsShareRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...