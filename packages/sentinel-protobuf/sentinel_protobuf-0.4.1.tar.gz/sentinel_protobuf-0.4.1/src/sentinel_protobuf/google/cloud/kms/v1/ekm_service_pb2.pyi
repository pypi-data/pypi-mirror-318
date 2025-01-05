from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
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

class ListEkmConnectionsRequest(_message.Message):
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

class ListEkmConnectionsResponse(_message.Message):
    __slots__ = ('ekm_connections', 'next_page_token', 'total_size')
    EKM_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    ekm_connections: _containers.RepeatedCompositeFieldContainer[EkmConnection]
    next_page_token: str
    total_size: int

    def __init__(self, ekm_connections: _Optional[_Iterable[_Union[EkmConnection, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class GetEkmConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEkmConnectionRequest(_message.Message):
    __slots__ = ('parent', 'ekm_connection_id', 'ekm_connection')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EKM_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    EKM_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    ekm_connection_id: str
    ekm_connection: EkmConnection

    def __init__(self, parent: _Optional[str]=..., ekm_connection_id: _Optional[str]=..., ekm_connection: _Optional[_Union[EkmConnection, _Mapping]]=...) -> None:
        ...

class UpdateEkmConnectionRequest(_message.Message):
    __slots__ = ('ekm_connection', 'update_mask')
    EKM_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ekm_connection: EkmConnection
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, ekm_connection: _Optional[_Union[EkmConnection, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetEkmConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateEkmConfigRequest(_message.Message):
    __slots__ = ('ekm_config', 'update_mask')
    EKM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ekm_config: EkmConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, ekm_config: _Optional[_Union[EkmConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class Certificate(_message.Message):
    __slots__ = ('raw_der', 'parsed', 'issuer', 'subject', 'subject_alternative_dns_names', 'not_before_time', 'not_after_time', 'serial_number', 'sha256_fingerprint')
    RAW_DER_FIELD_NUMBER: _ClassVar[int]
    PARSED_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ALTERNATIVE_DNS_NAMES_FIELD_NUMBER: _ClassVar[int]
    NOT_BEFORE_TIME_FIELD_NUMBER: _ClassVar[int]
    NOT_AFTER_TIME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SHA256_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    raw_der: bytes
    parsed: bool
    issuer: str
    subject: str
    subject_alternative_dns_names: _containers.RepeatedScalarFieldContainer[str]
    not_before_time: _timestamp_pb2.Timestamp
    not_after_time: _timestamp_pb2.Timestamp
    serial_number: str
    sha256_fingerprint: str

    def __init__(self, raw_der: _Optional[bytes]=..., parsed: bool=..., issuer: _Optional[str]=..., subject: _Optional[str]=..., subject_alternative_dns_names: _Optional[_Iterable[str]]=..., not_before_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., not_after_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., serial_number: _Optional[str]=..., sha256_fingerprint: _Optional[str]=...) -> None:
        ...

class EkmConnection(_message.Message):
    __slots__ = ('name', 'create_time', 'service_resolvers', 'etag', 'key_management_mode', 'crypto_space_path')

    class KeyManagementMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_MANAGEMENT_MODE_UNSPECIFIED: _ClassVar[EkmConnection.KeyManagementMode]
        MANUAL: _ClassVar[EkmConnection.KeyManagementMode]
        CLOUD_KMS: _ClassVar[EkmConnection.KeyManagementMode]
    KEY_MANAGEMENT_MODE_UNSPECIFIED: EkmConnection.KeyManagementMode
    MANUAL: EkmConnection.KeyManagementMode
    CLOUD_KMS: EkmConnection.KeyManagementMode

    class ServiceResolver(_message.Message):
        __slots__ = ('service_directory_service', 'endpoint_filter', 'hostname', 'server_certificates')
        SERVICE_DIRECTORY_SERVICE_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_FILTER_FIELD_NUMBER: _ClassVar[int]
        HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        SERVER_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
        service_directory_service: str
        endpoint_filter: str
        hostname: str
        server_certificates: _containers.RepeatedCompositeFieldContainer[Certificate]

        def __init__(self, service_directory_service: _Optional[str]=..., endpoint_filter: _Optional[str]=..., hostname: _Optional[str]=..., server_certificates: _Optional[_Iterable[_Union[Certificate, _Mapping]]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_RESOLVERS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    KEY_MANAGEMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_SPACE_PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    service_resolvers: _containers.RepeatedCompositeFieldContainer[EkmConnection.ServiceResolver]
    etag: str
    key_management_mode: EkmConnection.KeyManagementMode
    crypto_space_path: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., service_resolvers: _Optional[_Iterable[_Union[EkmConnection.ServiceResolver, _Mapping]]]=..., etag: _Optional[str]=..., key_management_mode: _Optional[_Union[EkmConnection.KeyManagementMode, str]]=..., crypto_space_path: _Optional[str]=...) -> None:
        ...

class EkmConfig(_message.Message):
    __slots__ = ('name', 'default_ekm_connection')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EKM_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    default_ekm_connection: str

    def __init__(self, name: _Optional[str]=..., default_ekm_connection: _Optional[str]=...) -> None:
        ...

class VerifyConnectivityRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class VerifyConnectivityResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...