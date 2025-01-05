from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenerateCredentialsRequest(_message.Message):
    __slots__ = ('name', 'force_use_agent', 'version', 'kubernetes_namespace', 'operating_system')

    class OperatingSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATING_SYSTEM_UNSPECIFIED: _ClassVar[GenerateCredentialsRequest.OperatingSystem]
        OPERATING_SYSTEM_WINDOWS: _ClassVar[GenerateCredentialsRequest.OperatingSystem]
    OPERATING_SYSTEM_UNSPECIFIED: GenerateCredentialsRequest.OperatingSystem
    OPERATING_SYSTEM_WINDOWS: GenerateCredentialsRequest.OperatingSystem
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_USE_AGENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    name: str
    force_use_agent: bool
    version: str
    kubernetes_namespace: str
    operating_system: GenerateCredentialsRequest.OperatingSystem

    def __init__(self, name: _Optional[str]=..., force_use_agent: bool=..., version: _Optional[str]=..., kubernetes_namespace: _Optional[str]=..., operating_system: _Optional[_Union[GenerateCredentialsRequest.OperatingSystem, str]]=...) -> None:
        ...

class GenerateCredentialsResponse(_message.Message):
    __slots__ = ('kubeconfig', 'endpoint')
    KUBECONFIG_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    kubeconfig: bytes
    endpoint: str

    def __init__(self, kubeconfig: _Optional[bytes]=..., endpoint: _Optional[str]=...) -> None:
        ...