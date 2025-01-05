from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Environment(_message.Message):
    __slots__ = ('name', 'id', 'docker_image', 'state', 'web_host', 'ssh_username', 'ssh_host', 'ssh_port', 'public_keys')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Environment.State]
        SUSPENDED: _ClassVar[Environment.State]
        PENDING: _ClassVar[Environment.State]
        RUNNING: _ClassVar[Environment.State]
        DELETING: _ClassVar[Environment.State]
    STATE_UNSPECIFIED: Environment.State
    SUSPENDED: Environment.State
    PENDING: Environment.State
    RUNNING: Environment.State
    DELETING: Environment.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DOCKER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    WEB_HOST_FIELD_NUMBER: _ClassVar[int]
    SSH_USERNAME_FIELD_NUMBER: _ClassVar[int]
    SSH_HOST_FIELD_NUMBER: _ClassVar[int]
    SSH_PORT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    docker_image: str
    state: Environment.State
    web_host: str
    ssh_username: str
    ssh_host: str
    ssh_port: int
    public_keys: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., docker_image: _Optional[str]=..., state: _Optional[_Union[Environment.State, str]]=..., web_host: _Optional[str]=..., ssh_username: _Optional[str]=..., ssh_host: _Optional[str]=..., ssh_port: _Optional[int]=..., public_keys: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEnvironmentMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteEnvironmentMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class StartEnvironmentRequest(_message.Message):
    __slots__ = ('name', 'access_token', 'public_keys')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    name: str
    access_token: str
    public_keys: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., access_token: _Optional[str]=..., public_keys: _Optional[_Iterable[str]]=...) -> None:
        ...

class AuthorizeEnvironmentRequest(_message.Message):
    __slots__ = ('name', 'access_token', 'id_token', 'expire_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    access_token: str
    id_token: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., access_token: _Optional[str]=..., id_token: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AuthorizeEnvironmentResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AuthorizeEnvironmentMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class StartEnvironmentMetadata(_message.Message):
    __slots__ = ('state',)

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[StartEnvironmentMetadata.State]
        STARTING: _ClassVar[StartEnvironmentMetadata.State]
        UNARCHIVING_DISK: _ClassVar[StartEnvironmentMetadata.State]
        AWAITING_COMPUTE_RESOURCES: _ClassVar[StartEnvironmentMetadata.State]
        FINISHED: _ClassVar[StartEnvironmentMetadata.State]
    STATE_UNSPECIFIED: StartEnvironmentMetadata.State
    STARTING: StartEnvironmentMetadata.State
    UNARCHIVING_DISK: StartEnvironmentMetadata.State
    AWAITING_COMPUTE_RESOURCES: StartEnvironmentMetadata.State
    FINISHED: StartEnvironmentMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: StartEnvironmentMetadata.State

    def __init__(self, state: _Optional[_Union[StartEnvironmentMetadata.State, str]]=...) -> None:
        ...

class StartEnvironmentResponse(_message.Message):
    __slots__ = ('environment',)
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: Environment

    def __init__(self, environment: _Optional[_Union[Environment, _Mapping]]=...) -> None:
        ...

class AddPublicKeyRequest(_message.Message):
    __slots__ = ('environment', 'key')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    environment: str
    key: str

    def __init__(self, environment: _Optional[str]=..., key: _Optional[str]=...) -> None:
        ...

class AddPublicKeyResponse(_message.Message):
    __slots__ = ('key',)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str

    def __init__(self, key: _Optional[str]=...) -> None:
        ...

class AddPublicKeyMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RemovePublicKeyRequest(_message.Message):
    __slots__ = ('environment', 'key')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    environment: str
    key: str

    def __init__(self, environment: _Optional[str]=..., key: _Optional[str]=...) -> None:
        ...

class RemovePublicKeyResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RemovePublicKeyMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CloudShellErrorDetails(_message.Message):
    __slots__ = ('code',)

    class CloudShellErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLOUD_SHELL_ERROR_CODE_UNSPECIFIED: _ClassVar[CloudShellErrorDetails.CloudShellErrorCode]
        IMAGE_UNAVAILABLE: _ClassVar[CloudShellErrorDetails.CloudShellErrorCode]
        CLOUD_SHELL_DISABLED: _ClassVar[CloudShellErrorDetails.CloudShellErrorCode]
        TOS_VIOLATION: _ClassVar[CloudShellErrorDetails.CloudShellErrorCode]
        QUOTA_EXCEEDED: _ClassVar[CloudShellErrorDetails.CloudShellErrorCode]
        ENVIRONMENT_UNAVAILABLE: _ClassVar[CloudShellErrorDetails.CloudShellErrorCode]
    CLOUD_SHELL_ERROR_CODE_UNSPECIFIED: CloudShellErrorDetails.CloudShellErrorCode
    IMAGE_UNAVAILABLE: CloudShellErrorDetails.CloudShellErrorCode
    CLOUD_SHELL_DISABLED: CloudShellErrorDetails.CloudShellErrorCode
    TOS_VIOLATION: CloudShellErrorDetails.CloudShellErrorCode
    QUOTA_EXCEEDED: CloudShellErrorDetails.CloudShellErrorCode
    ENVIRONMENT_UNAVAILABLE: CloudShellErrorDetails.CloudShellErrorCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: CloudShellErrorDetails.CloudShellErrorCode

    def __init__(self, code: _Optional[_Union[CloudShellErrorDetails.CloudShellErrorCode, str]]=...) -> None:
        ...