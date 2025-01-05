from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GrpcEndpoint(_message.Message):
    __slots__ = ('target_uri',)
    TARGET_URI_FIELD_NUMBER: _ClassVar[int]
    target_uri: str

    def __init__(self, target_uri: _Optional[str]=...) -> None:
        ...

class ValidationCA(_message.Message):
    __slots__ = ('grpc_endpoint', 'certificate_provider_instance')
    GRPC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_PROVIDER_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    grpc_endpoint: GrpcEndpoint
    certificate_provider_instance: CertificateProviderInstance

    def __init__(self, grpc_endpoint: _Optional[_Union[GrpcEndpoint, _Mapping]]=..., certificate_provider_instance: _Optional[_Union[CertificateProviderInstance, _Mapping]]=...) -> None:
        ...

class CertificateProviderInstance(_message.Message):
    __slots__ = ('plugin_instance',)
    PLUGIN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    plugin_instance: str

    def __init__(self, plugin_instance: _Optional[str]=...) -> None:
        ...

class CertificateProvider(_message.Message):
    __slots__ = ('grpc_endpoint', 'certificate_provider_instance')
    GRPC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_PROVIDER_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    grpc_endpoint: GrpcEndpoint
    certificate_provider_instance: CertificateProviderInstance

    def __init__(self, grpc_endpoint: _Optional[_Union[GrpcEndpoint, _Mapping]]=..., certificate_provider_instance: _Optional[_Union[CertificateProviderInstance, _Mapping]]=...) -> None:
        ...