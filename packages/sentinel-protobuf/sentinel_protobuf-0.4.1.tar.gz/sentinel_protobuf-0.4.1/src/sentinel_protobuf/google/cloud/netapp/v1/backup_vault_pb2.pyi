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

class BackupVault(_message.Message):
    __slots__ = ('name', 'state', 'create_time', 'description', 'labels')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BackupVault.State]
        CREATING: _ClassVar[BackupVault.State]
        READY: _ClassVar[BackupVault.State]
        DELETING: _ClassVar[BackupVault.State]
        ERROR: _ClassVar[BackupVault.State]
        UPDATING: _ClassVar[BackupVault.State]
    STATE_UNSPECIFIED: BackupVault.State
    CREATING: BackupVault.State
    READY: BackupVault.State
    DELETING: BackupVault.State
    ERROR: BackupVault.State
    UPDATING: BackupVault.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: BackupVault.State
    create_time: _timestamp_pb2.Timestamp
    description: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[BackupVault.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class GetBackupVaultRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBackupVaultsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListBackupVaultsResponse(_message.Message):
    __slots__ = ('backup_vaults', 'next_page_token', 'unreachable')
    BACKUP_VAULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backup_vaults: _containers.RepeatedCompositeFieldContainer[BackupVault]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, backup_vaults: _Optional[_Iterable[_Union[BackupVault, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateBackupVaultRequest(_message.Message):
    __slots__ = ('parent', 'backup_vault_id', 'backup_vault')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_vault_id: str
    backup_vault: BackupVault

    def __init__(self, parent: _Optional[str]=..., backup_vault_id: _Optional[str]=..., backup_vault: _Optional[_Union[BackupVault, _Mapping]]=...) -> None:
        ...

class DeleteBackupVaultRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateBackupVaultRequest(_message.Message):
    __slots__ = ('update_mask', 'backup_vault')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    backup_vault: BackupVault

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., backup_vault: _Optional[_Union[BackupVault, _Mapping]]=...) -> None:
        ...