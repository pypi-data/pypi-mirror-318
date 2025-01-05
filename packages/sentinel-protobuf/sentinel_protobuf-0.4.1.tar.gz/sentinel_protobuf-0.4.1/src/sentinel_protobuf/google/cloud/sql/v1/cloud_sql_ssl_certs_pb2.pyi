from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.cloud.sql.v1 import cloud_sql_resources_pb2 as _cloud_sql_resources_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlSslCertsDeleteRequest(_message.Message):
    __slots__ = ("instance", "project", "sha1_fingerprint")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SHA1_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    sha1_fingerprint: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., sha1_fingerprint: _Optional[str] = ...) -> None: ...

class SqlSslCertsGetRequest(_message.Message):
    __slots__ = ("instance", "project", "sha1_fingerprint")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SHA1_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    sha1_fingerprint: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., sha1_fingerprint: _Optional[str] = ...) -> None: ...

class SqlSslCertsInsertRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: SslCertsInsertRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[SslCertsInsertRequest, _Mapping]] = ...) -> None: ...

class SqlSslCertsListRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SslCertsInsertRequest(_message.Message):
    __slots__ = ("common_name",)
    COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
    common_name: str
    def __init__(self, common_name: _Optional[str] = ...) -> None: ...

class SslCertsInsertResponse(_message.Message):
    __slots__ = ("kind", "operation", "server_ca_cert", "client_cert")
    KIND_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SERVER_CA_CERT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERT_FIELD_NUMBER: _ClassVar[int]
    kind: str
    operation: _cloud_sql_resources_pb2.Operation
    server_ca_cert: _cloud_sql_resources_pb2.SslCert
    client_cert: _cloud_sql_resources_pb2.SslCertDetail
    def __init__(self, kind: _Optional[str] = ..., operation: _Optional[_Union[_cloud_sql_resources_pb2.Operation, _Mapping]] = ..., server_ca_cert: _Optional[_Union[_cloud_sql_resources_pb2.SslCert, _Mapping]] = ..., client_cert: _Optional[_Union[_cloud_sql_resources_pb2.SslCertDetail, _Mapping]] = ...) -> None: ...

class SslCertsListResponse(_message.Message):
    __slots__ = ("kind", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[_cloud_sql_resources_pb2.SslCert]
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_cloud_sql_resources_pb2.SslCert, _Mapping]]] = ...) -> None: ...
