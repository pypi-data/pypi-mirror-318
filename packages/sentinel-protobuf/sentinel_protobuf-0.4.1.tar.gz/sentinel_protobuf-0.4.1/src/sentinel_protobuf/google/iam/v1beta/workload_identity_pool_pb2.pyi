from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WorkloadIdentityPool(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'state', 'disabled')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[WorkloadIdentityPool.State]
        ACTIVE: _ClassVar[WorkloadIdentityPool.State]
        DELETED: _ClassVar[WorkloadIdentityPool.State]
    STATE_UNSPECIFIED: WorkloadIdentityPool.State
    ACTIVE: WorkloadIdentityPool.State
    DELETED: WorkloadIdentityPool.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    state: WorkloadIdentityPool.State
    disabled: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[WorkloadIdentityPool.State, str]]=..., disabled: bool=...) -> None:
        ...

class WorkloadIdentityPoolProvider(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'state', 'disabled', 'attribute_mapping', 'attribute_condition', 'aws', 'oidc')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[WorkloadIdentityPoolProvider.State]
        ACTIVE: _ClassVar[WorkloadIdentityPoolProvider.State]
        DELETED: _ClassVar[WorkloadIdentityPoolProvider.State]
    STATE_UNSPECIFIED: WorkloadIdentityPoolProvider.State
    ACTIVE: WorkloadIdentityPoolProvider.State
    DELETED: WorkloadIdentityPoolProvider.State

    class Aws(_message.Message):
        __slots__ = ('account_id',)
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        account_id: str

        def __init__(self, account_id: _Optional[str]=...) -> None:
            ...

    class Oidc(_message.Message):
        __slots__ = ('issuer_uri', 'allowed_audiences')
        ISSUER_URI_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_AUDIENCES_FIELD_NUMBER: _ClassVar[int]
        issuer_uri: str
        allowed_audiences: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, issuer_uri: _Optional[str]=..., allowed_audiences: _Optional[_Iterable[str]]=...) -> None:
            ...

    class AttributeMappingEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    OIDC_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    state: WorkloadIdentityPoolProvider.State
    disabled: bool
    attribute_mapping: _containers.ScalarMap[str, str]
    attribute_condition: str
    aws: WorkloadIdentityPoolProvider.Aws
    oidc: WorkloadIdentityPoolProvider.Oidc

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[WorkloadIdentityPoolProvider.State, str]]=..., disabled: bool=..., attribute_mapping: _Optional[_Mapping[str, str]]=..., attribute_condition: _Optional[str]=..., aws: _Optional[_Union[WorkloadIdentityPoolProvider.Aws, _Mapping]]=..., oidc: _Optional[_Union[WorkloadIdentityPoolProvider.Oidc, _Mapping]]=...) -> None:
        ...

class ListWorkloadIdentityPoolsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., show_deleted: bool=...) -> None:
        ...

class ListWorkloadIdentityPoolsResponse(_message.Message):
    __slots__ = ('workload_identity_pools', 'next_page_token')
    WORKLOAD_IDENTITY_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workload_identity_pools: _containers.RepeatedCompositeFieldContainer[WorkloadIdentityPool]
    next_page_token: str

    def __init__(self, workload_identity_pools: _Optional[_Iterable[_Union[WorkloadIdentityPool, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetWorkloadIdentityPoolRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWorkloadIdentityPoolRequest(_message.Message):
    __slots__ = ('parent', 'workload_identity_pool', 'workload_identity_pool_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_IDENTITY_POOL_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_IDENTITY_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workload_identity_pool: WorkloadIdentityPool
    workload_identity_pool_id: str

    def __init__(self, parent: _Optional[str]=..., workload_identity_pool: _Optional[_Union[WorkloadIdentityPool, _Mapping]]=..., workload_identity_pool_id: _Optional[str]=...) -> None:
        ...

class UpdateWorkloadIdentityPoolRequest(_message.Message):
    __slots__ = ('workload_identity_pool', 'update_mask')
    WORKLOAD_IDENTITY_POOL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    workload_identity_pool: WorkloadIdentityPool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, workload_identity_pool: _Optional[_Union[WorkloadIdentityPool, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteWorkloadIdentityPoolRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeleteWorkloadIdentityPoolRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListWorkloadIdentityPoolProvidersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., show_deleted: bool=...) -> None:
        ...

class ListWorkloadIdentityPoolProvidersResponse(_message.Message):
    __slots__ = ('workload_identity_pool_providers', 'next_page_token')
    WORKLOAD_IDENTITY_POOL_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workload_identity_pool_providers: _containers.RepeatedCompositeFieldContainer[WorkloadIdentityPoolProvider]
    next_page_token: str

    def __init__(self, workload_identity_pool_providers: _Optional[_Iterable[_Union[WorkloadIdentityPoolProvider, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetWorkloadIdentityPoolProviderRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWorkloadIdentityPoolProviderRequest(_message.Message):
    __slots__ = ('parent', 'workload_identity_pool_provider', 'workload_identity_pool_provider_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_IDENTITY_POOL_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_IDENTITY_POOL_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workload_identity_pool_provider: WorkloadIdentityPoolProvider
    workload_identity_pool_provider_id: str

    def __init__(self, parent: _Optional[str]=..., workload_identity_pool_provider: _Optional[_Union[WorkloadIdentityPoolProvider, _Mapping]]=..., workload_identity_pool_provider_id: _Optional[str]=...) -> None:
        ...

class UpdateWorkloadIdentityPoolProviderRequest(_message.Message):
    __slots__ = ('workload_identity_pool_provider', 'update_mask')
    WORKLOAD_IDENTITY_POOL_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    workload_identity_pool_provider: WorkloadIdentityPoolProvider
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, workload_identity_pool_provider: _Optional[_Union[WorkloadIdentityPoolProvider, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteWorkloadIdentityPoolProviderRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeleteWorkloadIdentityPoolProviderRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class WorkloadIdentityPoolOperationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WorkloadIdentityPoolProviderOperationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...