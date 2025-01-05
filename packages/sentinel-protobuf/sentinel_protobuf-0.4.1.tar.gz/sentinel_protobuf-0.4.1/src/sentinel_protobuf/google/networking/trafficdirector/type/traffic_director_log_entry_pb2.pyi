from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TrafficDirectorLogEntry(_message.Message):
    __slots__ = ('node_id', 'node_ip', 'description', 'client_type', 'client_version', 'transport_api_version')

    class ClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLIENT_TYPE_UNSPECIFIED: _ClassVar[TrafficDirectorLogEntry.ClientType]
        ENVOY: _ClassVar[TrafficDirectorLogEntry.ClientType]
        GRPC_JAVA: _ClassVar[TrafficDirectorLogEntry.ClientType]
        GRPC_CPP: _ClassVar[TrafficDirectorLogEntry.ClientType]
        GRPC_PYTHON: _ClassVar[TrafficDirectorLogEntry.ClientType]
        GRPC_GO: _ClassVar[TrafficDirectorLogEntry.ClientType]
        GRPC_RUBY: _ClassVar[TrafficDirectorLogEntry.ClientType]
        GRPC_PHP: _ClassVar[TrafficDirectorLogEntry.ClientType]
        GRPC_NODE: _ClassVar[TrafficDirectorLogEntry.ClientType]
        GRPC_CSHARP: _ClassVar[TrafficDirectorLogEntry.ClientType]
        UNKNOWN: _ClassVar[TrafficDirectorLogEntry.ClientType]
    CLIENT_TYPE_UNSPECIFIED: TrafficDirectorLogEntry.ClientType
    ENVOY: TrafficDirectorLogEntry.ClientType
    GRPC_JAVA: TrafficDirectorLogEntry.ClientType
    GRPC_CPP: TrafficDirectorLogEntry.ClientType
    GRPC_PYTHON: TrafficDirectorLogEntry.ClientType
    GRPC_GO: TrafficDirectorLogEntry.ClientType
    GRPC_RUBY: TrafficDirectorLogEntry.ClientType
    GRPC_PHP: TrafficDirectorLogEntry.ClientType
    GRPC_NODE: TrafficDirectorLogEntry.ClientType
    GRPC_CSHARP: TrafficDirectorLogEntry.ClientType
    UNKNOWN: TrafficDirectorLogEntry.ClientType

    class TransportApiVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSPORT_API_VERSION_UNSPECIFIED: _ClassVar[TrafficDirectorLogEntry.TransportApiVersion]
        V2: _ClassVar[TrafficDirectorLogEntry.TransportApiVersion]
        V3: _ClassVar[TrafficDirectorLogEntry.TransportApiVersion]
    TRANSPORT_API_VERSION_UNSPECIFIED: TrafficDirectorLogEntry.TransportApiVersion
    V2: TrafficDirectorLogEntry.TransportApiVersion
    V3: TrafficDirectorLogEntry.TransportApiVersion
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_API_VERSION_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    node_ip: str
    description: str
    client_type: TrafficDirectorLogEntry.ClientType
    client_version: str
    transport_api_version: TrafficDirectorLogEntry.TransportApiVersion

    def __init__(self, node_id: _Optional[str]=..., node_ip: _Optional[str]=..., description: _Optional[str]=..., client_type: _Optional[_Union[TrafficDirectorLogEntry.ClientType, str]]=..., client_version: _Optional[str]=..., transport_api_version: _Optional[_Union[TrafficDirectorLogEntry.TransportApiVersion, str]]=...) -> None:
        ...