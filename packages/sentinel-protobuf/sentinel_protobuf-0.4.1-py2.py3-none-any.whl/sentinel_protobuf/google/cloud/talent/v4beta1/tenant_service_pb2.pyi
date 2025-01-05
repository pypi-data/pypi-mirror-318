from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.talent.v4beta1 import common_pb2 as _common_pb2
from google.cloud.talent.v4beta1 import tenant_pb2 as _tenant_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateTenantRequest(_message.Message):
    __slots__ = ('parent', 'tenant')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tenant: _tenant_pb2.Tenant

    def __init__(self, parent: _Optional[str]=..., tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]]=...) -> None:
        ...

class GetTenantRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateTenantRequest(_message.Message):
    __slots__ = ('tenant', 'update_mask')
    TENANT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tenant: _tenant_pb2.Tenant
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteTenantRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTenantsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListTenantsResponse(_message.Message):
    __slots__ = ('tenants', 'next_page_token', 'metadata')
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    tenants: _containers.RepeatedCompositeFieldContainer[_tenant_pb2.Tenant]
    next_page_token: str
    metadata: _common_pb2.ResponseMetadata

    def __init__(self, tenants: _Optional[_Iterable[_Union[_tenant_pb2.Tenant, _Mapping]]]=..., next_page_token: _Optional[str]=..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]]=...) -> None:
        ...