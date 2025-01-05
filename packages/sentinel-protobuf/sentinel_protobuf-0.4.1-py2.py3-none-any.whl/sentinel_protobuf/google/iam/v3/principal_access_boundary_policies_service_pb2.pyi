from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v3 import operation_metadata_pb2 as _operation_metadata_pb2
from google.iam.v3 import policy_binding_resources_pb2 as _policy_binding_resources_pb2
from google.iam.v3 import principal_access_boundary_policy_resources_pb2 as _principal_access_boundary_policy_resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreatePrincipalAccessBoundaryPolicyRequest(_message.Message):
    __slots__ = ('parent', 'principal_access_boundary_policy_id', 'principal_access_boundary_policy', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ACCESS_BOUNDARY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ACCESS_BOUNDARY_POLICY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    principal_access_boundary_policy_id: str
    principal_access_boundary_policy: _principal_access_boundary_policy_resources_pb2.PrincipalAccessBoundaryPolicy
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., principal_access_boundary_policy_id: _Optional[str]=..., principal_access_boundary_policy: _Optional[_Union[_principal_access_boundary_policy_resources_pb2.PrincipalAccessBoundaryPolicy, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class GetPrincipalAccessBoundaryPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdatePrincipalAccessBoundaryPolicyRequest(_message.Message):
    __slots__ = ('principal_access_boundary_policy', 'validate_only', 'update_mask')
    PRINCIPAL_ACCESS_BOUNDARY_POLICY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    principal_access_boundary_policy: _principal_access_boundary_policy_resources_pb2.PrincipalAccessBoundaryPolicy
    validate_only: bool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, principal_access_boundary_policy: _Optional[_Union[_principal_access_boundary_policy_resources_pb2.PrincipalAccessBoundaryPolicy, _Mapping]]=..., validate_only: bool=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeletePrincipalAccessBoundaryPolicyRequest(_message.Message):
    __slots__ = ('name', 'etag', 'validate_only', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    validate_only: bool
    force: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., validate_only: bool=..., force: bool=...) -> None:
        ...

class ListPrincipalAccessBoundaryPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPrincipalAccessBoundaryPoliciesResponse(_message.Message):
    __slots__ = ('principal_access_boundary_policies', 'next_page_token')
    PRINCIPAL_ACCESS_BOUNDARY_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    principal_access_boundary_policies: _containers.RepeatedCompositeFieldContainer[_principal_access_boundary_policy_resources_pb2.PrincipalAccessBoundaryPolicy]
    next_page_token: str

    def __init__(self, principal_access_boundary_policies: _Optional[_Iterable[_Union[_principal_access_boundary_policy_resources_pb2.PrincipalAccessBoundaryPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchPrincipalAccessBoundaryPolicyBindingsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchPrincipalAccessBoundaryPolicyBindingsResponse(_message.Message):
    __slots__ = ('policy_bindings', 'next_page_token')
    POLICY_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policy_bindings: _containers.RepeatedCompositeFieldContainer[_policy_binding_resources_pb2.PolicyBinding]
    next_page_token: str

    def __init__(self, policy_bindings: _Optional[_Iterable[_Union[_policy_binding_resources_pb2.PolicyBinding, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...