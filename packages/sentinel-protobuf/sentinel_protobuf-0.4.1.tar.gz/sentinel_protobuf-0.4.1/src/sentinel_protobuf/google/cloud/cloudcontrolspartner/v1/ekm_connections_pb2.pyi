from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EkmConnections(_message.Message):
    __slots__ = ('name', 'ekm_connections')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EKM_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    ekm_connections: _containers.RepeatedCompositeFieldContainer[EkmConnection]

    def __init__(self, name: _Optional[str]=..., ekm_connections: _Optional[_Iterable[_Union[EkmConnection, _Mapping]]]=...) -> None:
        ...

class GetEkmConnectionsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EkmConnection(_message.Message):
    __slots__ = ('connection_name', 'connection_state', 'connection_error')

    class ConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTION_STATE_UNSPECIFIED: _ClassVar[EkmConnection.ConnectionState]
        AVAILABLE: _ClassVar[EkmConnection.ConnectionState]
        NOT_AVAILABLE: _ClassVar[EkmConnection.ConnectionState]
        ERROR: _ClassVar[EkmConnection.ConnectionState]
        PERMISSION_DENIED: _ClassVar[EkmConnection.ConnectionState]
    CONNECTION_STATE_UNSPECIFIED: EkmConnection.ConnectionState
    AVAILABLE: EkmConnection.ConnectionState
    NOT_AVAILABLE: EkmConnection.ConnectionState
    ERROR: EkmConnection.ConnectionState
    PERMISSION_DENIED: EkmConnection.ConnectionState

    class ConnectionError(_message.Message):
        __slots__ = ('error_domain', 'error_message')
        ERROR_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        error_domain: str
        error_message: str

        def __init__(self, error_domain: _Optional[str]=..., error_message: _Optional[str]=...) -> None:
            ...
    CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ERROR_FIELD_NUMBER: _ClassVar[int]
    connection_name: str
    connection_state: EkmConnection.ConnectionState
    connection_error: EkmConnection.ConnectionError

    def __init__(self, connection_name: _Optional[str]=..., connection_state: _Optional[_Union[EkmConnection.ConnectionState, str]]=..., connection_error: _Optional[_Union[EkmConnection.ConnectionError, _Mapping]]=...) -> None:
        ...