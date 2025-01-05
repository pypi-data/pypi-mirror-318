from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class PSCAutomationConfig(_message.Message):
    __slots__ = ('project_id', 'network')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    network: str

    def __init__(self, project_id: _Optional[str]=..., network: _Optional[str]=...) -> None:
        ...

class PrivateServiceConnectConfig(_message.Message):
    __slots__ = ('enable_private_service_connect', 'project_allowlist', 'enable_secure_private_service_connect', 'service_attachment')
    ENABLE_PRIVATE_SERVICE_CONNECT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SECURE_PRIVATE_SERVICE_CONNECT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    enable_private_service_connect: bool
    project_allowlist: _containers.RepeatedScalarFieldContainer[str]
    enable_secure_private_service_connect: bool
    service_attachment: str

    def __init__(self, enable_private_service_connect: bool=..., project_allowlist: _Optional[_Iterable[str]]=..., enable_secure_private_service_connect: bool=..., service_attachment: _Optional[str]=...) -> None:
        ...

class PscAutomatedEndpoints(_message.Message):
    __slots__ = ('project_id', 'network', 'match_address')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    MATCH_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    network: str
    match_address: str

    def __init__(self, project_id: _Optional[str]=..., network: _Optional[str]=..., match_address: _Optional[str]=...) -> None:
        ...

class PscInterfaceConfig(_message.Message):
    __slots__ = ('network_attachment',)
    NETWORK_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    network_attachment: str

    def __init__(self, network_attachment: _Optional[str]=...) -> None:
        ...