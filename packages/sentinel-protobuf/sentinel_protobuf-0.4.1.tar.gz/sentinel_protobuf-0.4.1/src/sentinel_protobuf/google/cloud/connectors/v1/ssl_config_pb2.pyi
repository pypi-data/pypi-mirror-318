from google.cloud.connectors.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SslType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SSL_TYPE_UNSPECIFIED: _ClassVar[SslType]
    TLS: _ClassVar[SslType]
    MTLS: _ClassVar[SslType]

class CertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CERT_TYPE_UNSPECIFIED: _ClassVar[CertType]
    PEM: _ClassVar[CertType]
SSL_TYPE_UNSPECIFIED: SslType
TLS: SslType
MTLS: SslType
CERT_TYPE_UNSPECIFIED: CertType
PEM: CertType

class SslConfigTemplate(_message.Message):
    __slots__ = ('ssl_type', 'is_tls_mandatory', 'server_cert_type', 'client_cert_type', 'additional_variables')
    SSL_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_TLS_MANDATORY_FIELD_NUMBER: _ClassVar[int]
    SERVER_CERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    ssl_type: SslType
    is_tls_mandatory: bool
    server_cert_type: _containers.RepeatedScalarFieldContainer[CertType]
    client_cert_type: _containers.RepeatedScalarFieldContainer[CertType]
    additional_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.ConfigVariableTemplate]

    def __init__(self, ssl_type: _Optional[_Union[SslType, str]]=..., is_tls_mandatory: bool=..., server_cert_type: _Optional[_Iterable[_Union[CertType, str]]]=..., client_cert_type: _Optional[_Iterable[_Union[CertType, str]]]=..., additional_variables: _Optional[_Iterable[_Union[_common_pb2.ConfigVariableTemplate, _Mapping]]]=...) -> None:
        ...

class SslConfig(_message.Message):
    __slots__ = ('type', 'trust_model', 'private_server_certificate', 'client_certificate', 'client_private_key', 'client_private_key_pass', 'server_cert_type', 'client_cert_type', 'use_ssl', 'additional_variables')

    class TrustModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PUBLIC: _ClassVar[SslConfig.TrustModel]
        PRIVATE: _ClassVar[SslConfig.TrustModel]
        INSECURE: _ClassVar[SslConfig.TrustModel]
    PUBLIC: SslConfig.TrustModel
    PRIVATE: SslConfig.TrustModel
    INSECURE: SslConfig.TrustModel
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TRUST_MODEL_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SERVER_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PRIVATE_KEY_PASS_FIELD_NUMBER: _ClassVar[int]
    SERVER_CERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USE_SSL_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    type: SslType
    trust_model: SslConfig.TrustModel
    private_server_certificate: _common_pb2.Secret
    client_certificate: _common_pb2.Secret
    client_private_key: _common_pb2.Secret
    client_private_key_pass: _common_pb2.Secret
    server_cert_type: CertType
    client_cert_type: CertType
    use_ssl: bool
    additional_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.ConfigVariable]

    def __init__(self, type: _Optional[_Union[SslType, str]]=..., trust_model: _Optional[_Union[SslConfig.TrustModel, str]]=..., private_server_certificate: _Optional[_Union[_common_pb2.Secret, _Mapping]]=..., client_certificate: _Optional[_Union[_common_pb2.Secret, _Mapping]]=..., client_private_key: _Optional[_Union[_common_pb2.Secret, _Mapping]]=..., client_private_key_pass: _Optional[_Union[_common_pb2.Secret, _Mapping]]=..., server_cert_type: _Optional[_Union[CertType, str]]=..., client_cert_type: _Optional[_Union[CertType, str]]=..., use_ssl: bool=..., additional_variables: _Optional[_Iterable[_Union[_common_pb2.ConfigVariable, _Mapping]]]=...) -> None:
        ...