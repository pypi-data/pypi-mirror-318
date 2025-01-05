from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v3beta import operation_metadata_pb2 as _operation_metadata_pb2
from google.iam.v3beta import policy_binding_resources_pb2 as _policy_binding_resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreatePolicyBindingRequest(_message.Message):
    __slots__ = ('parent', 'policy_binding_id', 'policy_binding', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_BINDING_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_BINDING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    policy_binding_id: str
    policy_binding: _policy_binding_resources_pb2.PolicyBinding
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., policy_binding_id: _Optional[str]=..., policy_binding: _Optional[_Union[_policy_binding_resources_pb2.PolicyBinding, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class GetPolicyBindingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdatePolicyBindingRequest(_message.Message):
    __slots__ = ('policy_binding', 'validate_only', 'update_mask')
    POLICY_BINDING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    policy_binding: _policy_binding_resources_pb2.PolicyBinding
    validate_only: bool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, policy_binding: _Optional[_Union[_policy_binding_resources_pb2.PolicyBinding, _Mapping]]=..., validate_only: bool=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeletePolicyBindingRequest(_message.Message):
    __slots__ = ('name', 'etag', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class ListPolicyBindingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListPolicyBindingsResponse(_message.Message):
    __slots__ = ('policy_bindings', 'next_page_token')
    POLICY_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policy_bindings: _containers.RepeatedCompositeFieldContainer[_policy_binding_resources_pb2.PolicyBinding]
    next_page_token: str

    def __init__(self, policy_bindings: _Optional[_Iterable[_Union[_policy_binding_resources_pb2.PolicyBinding, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchTargetPolicyBindingsRequest(_message.Message):
    __slots__ = ('target', 'page_size', 'page_token', 'parent')
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    target: str
    page_size: int
    page_token: str
    parent: str

    def __init__(self, target: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., parent: _Optional[str]=...) -> None:
        ...

class SearchTargetPolicyBindingsResponse(_message.Message):
    __slots__ = ('policy_bindings', 'next_page_token')
    POLICY_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policy_bindings: _containers.RepeatedCompositeFieldContainer[_policy_binding_resources_pb2.PolicyBinding]
    next_page_token: str

    def __init__(self, policy_bindings: _Optional[_Iterable[_Union[_policy_binding_resources_pb2.PolicyBinding, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...