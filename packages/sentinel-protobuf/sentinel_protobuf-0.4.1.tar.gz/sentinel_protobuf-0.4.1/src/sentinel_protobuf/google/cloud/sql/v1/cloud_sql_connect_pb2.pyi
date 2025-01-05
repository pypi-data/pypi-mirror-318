from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.sql.v1 import cloud_sql_resources_pb2 as _cloud_sql_resources_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConnectSettingsRequest(_message.Message):
    __slots__ = ("instance", "project", "read_time")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    read_time: _timestamp_pb2.Timestamp
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ConnectSettings(_message.Message):
    __slots__ = ("kind", "server_ca_cert", "ip_addresses", "region", "database_version", "backend_type", "psc_enabled", "dns_name", "server_ca_mode")
    class CaMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CA_MODE_UNSPECIFIED: _ClassVar[ConnectSettings.CaMode]
        GOOGLE_MANAGED_INTERNAL_CA: _ClassVar[ConnectSettings.CaMode]
        GOOGLE_MANAGED_CAS_CA: _ClassVar[ConnectSettings.CaMode]
    CA_MODE_UNSPECIFIED: ConnectSettings.CaMode
    GOOGLE_MANAGED_INTERNAL_CA: ConnectSettings.CaMode
    GOOGLE_MANAGED_CAS_CA: ConnectSettings.CaMode
    KIND_FIELD_NUMBER: _ClassVar[int]
    SERVER_CA_CERT_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BACKEND_TYPE_FIELD_NUMBER: _ClassVar[int]
    PSC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_CA_MODE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    server_ca_cert: _cloud_sql_resources_pb2.SslCert
    ip_addresses: _containers.RepeatedCompositeFieldContainer[_cloud_sql_resources_pb2.IpMapping]
    region: str
    database_version: _cloud_sql_resources_pb2.SqlDatabaseVersion
    backend_type: _cloud_sql_resources_pb2.SqlBackendType
    psc_enabled: bool
    dns_name: str
    server_ca_mode: ConnectSettings.CaMode
    def __init__(self, kind: _Optional[str] = ..., server_ca_cert: _Optional[_Union[_cloud_sql_resources_pb2.SslCert, _Mapping]] = ..., ip_addresses: _Optional[_Iterable[_Union[_cloud_sql_resources_pb2.IpMapping, _Mapping]]] = ..., region: _Optional[str] = ..., database_version: _Optional[_Union[_cloud_sql_resources_pb2.SqlDatabaseVersion, str]] = ..., backend_type: _Optional[_Union[_cloud_sql_resources_pb2.SqlBackendType, str]] = ..., psc_enabled: bool = ..., dns_name: _Optional[str] = ..., server_ca_mode: _Optional[_Union[ConnectSettings.CaMode, str]] = ...) -> None: ...

class GenerateEphemeralCertRequest(_message.Message):
    __slots__ = ("instance", "project", "public_key", "access_token", "read_time", "valid_duration")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    VALID_DURATION_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    public_key: str
    access_token: str
    read_time: _timestamp_pb2.Timestamp
    valid_duration: _duration_pb2.Duration
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., public_key: _Optional[str] = ..., access_token: _Optional[str] = ..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GenerateEphemeralCertResponse(_message.Message):
    __slots__ = ("ephemeral_cert",)
    EPHEMERAL_CERT_FIELD_NUMBER: _ClassVar[int]
    ephemeral_cert: _cloud_sql_resources_pb2.SslCert
    def __init__(self, ephemeral_cert: _Optional[_Union[_cloud_sql_resources_pb2.SslCert, _Mapping]] = ...) -> None: ...
