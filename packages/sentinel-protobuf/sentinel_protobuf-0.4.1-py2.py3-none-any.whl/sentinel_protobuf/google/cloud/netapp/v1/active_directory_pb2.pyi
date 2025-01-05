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

class ListActiveDirectoriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListActiveDirectoriesResponse(_message.Message):
    __slots__ = ('active_directories', 'next_page_token', 'unreachable')
    ACTIVE_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    active_directories: _containers.RepeatedCompositeFieldContainer[ActiveDirectory]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, active_directories: _Optional[_Iterable[_Union[ActiveDirectory, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetActiveDirectoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateActiveDirectoryRequest(_message.Message):
    __slots__ = ('parent', 'active_directory', 'active_directory_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    active_directory: ActiveDirectory
    active_directory_id: str

    def __init__(self, parent: _Optional[str]=..., active_directory: _Optional[_Union[ActiveDirectory, _Mapping]]=..., active_directory_id: _Optional[str]=...) -> None:
        ...

class UpdateActiveDirectoryRequest(_message.Message):
    __slots__ = ('update_mask', 'active_directory')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    active_directory: ActiveDirectory

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., active_directory: _Optional[_Union[ActiveDirectory, _Mapping]]=...) -> None:
        ...

class DeleteActiveDirectoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ActiveDirectory(_message.Message):
    __slots__ = ('name', 'create_time', 'state', 'domain', 'site', 'dns', 'net_bios_prefix', 'organizational_unit', 'aes_encryption', 'username', 'password', 'backup_operators', 'administrators', 'security_operators', 'kdc_hostname', 'kdc_ip', 'nfs_users_with_ldap', 'description', 'ldap_signing', 'encrypt_dc_connections', 'labels', 'state_details')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ActiveDirectory.State]
        CREATING: _ClassVar[ActiveDirectory.State]
        READY: _ClassVar[ActiveDirectory.State]
        UPDATING: _ClassVar[ActiveDirectory.State]
        IN_USE: _ClassVar[ActiveDirectory.State]
        DELETING: _ClassVar[ActiveDirectory.State]
        ERROR: _ClassVar[ActiveDirectory.State]
        DIAGNOSING: _ClassVar[ActiveDirectory.State]
    STATE_UNSPECIFIED: ActiveDirectory.State
    CREATING: ActiveDirectory.State
    READY: ActiveDirectory.State
    UPDATING: ActiveDirectory.State
    IN_USE: ActiveDirectory.State
    DELETING: ActiveDirectory.State
    ERROR: ActiveDirectory.State
    DIAGNOSING: ActiveDirectory.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    NET_BIOS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONAL_UNIT_FIELD_NUMBER: _ClassVar[int]
    AES_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    BACKUP_OPERATORS_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATORS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_OPERATORS_FIELD_NUMBER: _ClassVar[int]
    KDC_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    KDC_IP_FIELD_NUMBER: _ClassVar[int]
    NFS_USERS_WITH_LDAP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LDAP_SIGNING_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_DC_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    state: ActiveDirectory.State
    domain: str
    site: str
    dns: str
    net_bios_prefix: str
    organizational_unit: str
    aes_encryption: bool
    username: str
    password: str
    backup_operators: _containers.RepeatedScalarFieldContainer[str]
    administrators: _containers.RepeatedScalarFieldContainer[str]
    security_operators: _containers.RepeatedScalarFieldContainer[str]
    kdc_hostname: str
    kdc_ip: str
    nfs_users_with_ldap: bool
    description: str
    ldap_signing: bool
    encrypt_dc_connections: bool
    labels: _containers.ScalarMap[str, str]
    state_details: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ActiveDirectory.State, str]]=..., domain: _Optional[str]=..., site: _Optional[str]=..., dns: _Optional[str]=..., net_bios_prefix: _Optional[str]=..., organizational_unit: _Optional[str]=..., aes_encryption: bool=..., username: _Optional[str]=..., password: _Optional[str]=..., backup_operators: _Optional[_Iterable[str]]=..., administrators: _Optional[_Iterable[str]]=..., security_operators: _Optional[_Iterable[str]]=..., kdc_hostname: _Optional[str]=..., kdc_ip: _Optional[str]=..., nfs_users_with_ldap: bool=..., description: _Optional[str]=..., ldap_signing: bool=..., encrypt_dc_connections: bool=..., labels: _Optional[_Mapping[str, str]]=..., state_details: _Optional[str]=...) -> None:
        ...