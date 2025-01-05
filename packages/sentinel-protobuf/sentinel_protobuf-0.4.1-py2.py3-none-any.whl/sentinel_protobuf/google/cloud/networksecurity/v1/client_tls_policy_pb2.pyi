from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networksecurity.v1 import tls_pb2 as _tls_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ClientTlsPolicy(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'labels', 'sni', 'client_certificate', 'server_validation_ca')

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
    SNI_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    SERVER_VALIDATION_CA_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    sni: str
    client_certificate: _tls_pb2.CertificateProvider
    server_validation_ca: _containers.RepeatedCompositeFieldContainer[_tls_pb2.ValidationCA]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., sni: _Optional[str]=..., client_certificate: _Optional[_Union[_tls_pb2.CertificateProvider, _Mapping]]=..., server_validation_ca: _Optional[_Iterable[_Union[_tls_pb2.ValidationCA, _Mapping]]]=...) -> None:
        ...

class ListClientTlsPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListClientTlsPoliciesResponse(_message.Message):
    __slots__ = ('client_tls_policies', 'next_page_token')
    CLIENT_TLS_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    client_tls_policies: _containers.RepeatedCompositeFieldContainer[ClientTlsPolicy]
    next_page_token: str

    def __init__(self, client_tls_policies: _Optional[_Iterable[_Union[ClientTlsPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetClientTlsPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateClientTlsPolicyRequest(_message.Message):
    __slots__ = ('parent', 'client_tls_policy_id', 'client_tls_policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TLS_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TLS_POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    client_tls_policy_id: str
    client_tls_policy: ClientTlsPolicy

    def __init__(self, parent: _Optional[str]=..., client_tls_policy_id: _Optional[str]=..., client_tls_policy: _Optional[_Union[ClientTlsPolicy, _Mapping]]=...) -> None:
        ...

class UpdateClientTlsPolicyRequest(_message.Message):
    __slots__ = ('update_mask', 'client_tls_policy')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TLS_POLICY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    client_tls_policy: ClientTlsPolicy

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., client_tls_policy: _Optional[_Union[ClientTlsPolicy, _Mapping]]=...) -> None:
        ...

class DeleteClientTlsPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...