from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networksecurity.v1beta1 import tls_pb2 as _tls_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ServerTlsPolicy(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'labels', 'allow_open', 'server_certificate', 'mtls_policy')

    class MTLSPolicy(_message.Message):
        __slots__ = ('client_validation_ca',)
        CLIENT_VALIDATION_CA_FIELD_NUMBER: _ClassVar[int]
        client_validation_ca: _containers.RepeatedCompositeFieldContainer[_tls_pb2.ValidationCA]

        def __init__(self, client_validation_ca: _Optional[_Iterable[_Union[_tls_pb2.ValidationCA, _Mapping]]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_OPEN_FIELD_NUMBER: _ClassVar[int]
    SERVER_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    MTLS_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    allow_open: bool
    server_certificate: _tls_pb2.CertificateProvider
    mtls_policy: ServerTlsPolicy.MTLSPolicy

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., allow_open: bool=..., server_certificate: _Optional[_Union[_tls_pb2.CertificateProvider, _Mapping]]=..., mtls_policy: _Optional[_Union[ServerTlsPolicy.MTLSPolicy, _Mapping]]=...) -> None:
        ...

class ListServerTlsPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListServerTlsPoliciesResponse(_message.Message):
    __slots__ = ('server_tls_policies', 'next_page_token')
    SERVER_TLS_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    server_tls_policies: _containers.RepeatedCompositeFieldContainer[ServerTlsPolicy]
    next_page_token: str

    def __init__(self, server_tls_policies: _Optional[_Iterable[_Union[ServerTlsPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetServerTlsPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateServerTlsPolicyRequest(_message.Message):
    __slots__ = ('parent', 'server_tls_policy_id', 'server_tls_policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVER_TLS_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TLS_POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    server_tls_policy_id: str
    server_tls_policy: ServerTlsPolicy

    def __init__(self, parent: _Optional[str]=..., server_tls_policy_id: _Optional[str]=..., server_tls_policy: _Optional[_Union[ServerTlsPolicy, _Mapping]]=...) -> None:
        ...

class UpdateServerTlsPolicyRequest(_message.Message):
    __slots__ = ('update_mask', 'server_tls_policy')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVER_TLS_POLICY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    server_tls_policy: ServerTlsPolicy

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., server_tls_policy: _Optional[_Union[ServerTlsPolicy, _Mapping]]=...) -> None:
        ...

class DeleteServerTlsPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...