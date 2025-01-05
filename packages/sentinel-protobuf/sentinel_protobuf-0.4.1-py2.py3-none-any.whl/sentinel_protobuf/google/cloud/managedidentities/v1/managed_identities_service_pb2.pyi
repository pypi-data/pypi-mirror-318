from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.managedidentities.v1 import resource_pb2 as _resource_pb2_1
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OpMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class CreateMicrosoftAdDomainRequest(_message.Message):
    __slots__ = ('parent', 'domain_name', 'domain')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    domain_name: str
    domain: _resource_pb2_1.Domain

    def __init__(self, parent: _Optional[str]=..., domain_name: _Optional[str]=..., domain: _Optional[_Union[_resource_pb2_1.Domain, _Mapping]]=...) -> None:
        ...

class ResetAdminPasswordRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ResetAdminPasswordResponse(_message.Message):
    __slots__ = ('password',)
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str

    def __init__(self, password: _Optional[str]=...) -> None:
        ...

class ListDomainsRequest(_message.Message):
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

class ListDomainsResponse(_message.Message):
    __slots__ = ('domains', 'next_page_token', 'unreachable')
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    domains: _containers.RepeatedCompositeFieldContainer[_resource_pb2_1.Domain]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, domains: _Optional[_Iterable[_Union[_resource_pb2_1.Domain, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDomainRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDomainRequest(_message.Message):
    __slots__ = ('update_mask', 'domain')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    domain: _resource_pb2_1.Domain

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., domain: _Optional[_Union[_resource_pb2_1.Domain, _Mapping]]=...) -> None:
        ...

class DeleteDomainRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class AttachTrustRequest(_message.Message):
    __slots__ = ('name', 'trust')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRUST_FIELD_NUMBER: _ClassVar[int]
    name: str
    trust: _resource_pb2_1.Trust

    def __init__(self, name: _Optional[str]=..., trust: _Optional[_Union[_resource_pb2_1.Trust, _Mapping]]=...) -> None:
        ...

class ReconfigureTrustRequest(_message.Message):
    __slots__ = ('name', 'target_domain_name', 'target_dns_ip_addresses')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_DNS_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_domain_name: str
    target_dns_ip_addresses: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., target_domain_name: _Optional[str]=..., target_dns_ip_addresses: _Optional[_Iterable[str]]=...) -> None:
        ...

class DetachTrustRequest(_message.Message):
    __slots__ = ('name', 'trust')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRUST_FIELD_NUMBER: _ClassVar[int]
    name: str
    trust: _resource_pb2_1.Trust

    def __init__(self, name: _Optional[str]=..., trust: _Optional[_Union[_resource_pb2_1.Trust, _Mapping]]=...) -> None:
        ...

class ValidateTrustRequest(_message.Message):
    __slots__ = ('name', 'trust')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRUST_FIELD_NUMBER: _ClassVar[int]
    name: str
    trust: _resource_pb2_1.Trust

    def __init__(self, name: _Optional[str]=..., trust: _Optional[_Union[_resource_pb2_1.Trust, _Mapping]]=...) -> None:
        ...