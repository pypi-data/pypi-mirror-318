from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperatingSystemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATING_SYSTEM_TYPE_UNSPECIFIED: _ClassVar[OperatingSystemType]
    LINUX: _ClassVar[OperatingSystemType]
    WINDOWS: _ClassVar[OperatingSystemType]
OPERATING_SYSTEM_TYPE_UNSPECIFIED: OperatingSystemType
LINUX: OperatingSystemType
WINDOWS: OperatingSystemType

class PosixAccount(_message.Message):
    __slots__ = ('primary', 'username', 'uid', 'gid', 'home_directory', 'shell', 'gecos', 'system_id', 'account_id', 'operating_system_type', 'name')
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    HOME_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SHELL_FIELD_NUMBER: _ClassVar[int]
    GECOS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    primary: bool
    username: str
    uid: int
    gid: int
    home_directory: str
    shell: str
    gecos: str
    system_id: str
    account_id: str
    operating_system_type: OperatingSystemType
    name: str

    def __init__(self, primary: bool=..., username: _Optional[str]=..., uid: _Optional[int]=..., gid: _Optional[int]=..., home_directory: _Optional[str]=..., shell: _Optional[str]=..., gecos: _Optional[str]=..., system_id: _Optional[str]=..., account_id: _Optional[str]=..., operating_system_type: _Optional[_Union[OperatingSystemType, str]]=..., name: _Optional[str]=...) -> None:
        ...

class SshPublicKey(_message.Message):
    __slots__ = ('key', 'expiration_time_usec', 'fingerprint', 'name')
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_USEC_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    key: str
    expiration_time_usec: int
    fingerprint: str
    name: str

    def __init__(self, key: _Optional[str]=..., expiration_time_usec: _Optional[int]=..., fingerprint: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...