from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.orgpolicy.v2 import constraint_pb2 as _constraint_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Policy(_message.Message):
    __slots__ = ('name', 'spec', 'alternate', 'dry_run_spec', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_SPEC_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    spec: PolicySpec
    alternate: AlternatePolicySpec
    dry_run_spec: PolicySpec
    etag: str

    def __init__(self, name: _Optional[str]=..., spec: _Optional[_Union[PolicySpec, _Mapping]]=..., alternate: _Optional[_Union[AlternatePolicySpec, _Mapping]]=..., dry_run_spec: _Optional[_Union[PolicySpec, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class AlternatePolicySpec(_message.Message):
    __slots__ = ('launch', 'spec')
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    launch: str
    spec: PolicySpec

    def __init__(self, launch: _Optional[str]=..., spec: _Optional[_Union[PolicySpec, _Mapping]]=...) -> None:
        ...

class PolicySpec(_message.Message):
    __slots__ = ('etag', 'update_time', 'rules', 'inherit_from_parent', 'reset')

    class PolicyRule(_message.Message):
        __slots__ = ('values', 'allow_all', 'deny_all', 'enforce', 'condition')

        class StringValues(_message.Message):
            __slots__ = ('allowed_values', 'denied_values')
            ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
            DENIED_VALUES_FIELD_NUMBER: _ClassVar[int]
            allowed_values: _containers.RepeatedScalarFieldContainer[str]
            denied_values: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, allowed_values: _Optional[_Iterable[str]]=..., denied_values: _Optional[_Iterable[str]]=...) -> None:
                ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_ALL_FIELD_NUMBER: _ClassVar[int]
        DENY_ALL_FIELD_NUMBER: _ClassVar[int]
        ENFORCE_FIELD_NUMBER: _ClassVar[int]
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        values: PolicySpec.PolicyRule.StringValues
        allow_all: bool
        deny_all: bool
        enforce: bool
        condition: _expr_pb2.Expr

        def __init__(self, values: _Optional[_Union[PolicySpec.PolicyRule.StringValues, _Mapping]]=..., allow_all: bool=..., deny_all: bool=..., enforce: bool=..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=...) -> None:
            ...
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    INHERIT_FROM_PARENT_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    etag: str
    update_time: _timestamp_pb2.Timestamp
    rules: _containers.RepeatedCompositeFieldContainer[PolicySpec.PolicyRule]
    inherit_from_parent: bool
    reset: bool

    def __init__(self, etag: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., rules: _Optional[_Iterable[_Union[PolicySpec.PolicyRule, _Mapping]]]=..., inherit_from_parent: bool=..., reset: bool=...) -> None:
        ...

class ListConstraintsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConstraintsResponse(_message.Message):
    __slots__ = ('constraints', 'next_page_token')
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    constraints: _containers.RepeatedCompositeFieldContainer[_constraint_pb2.Constraint]
    next_page_token: str

    def __init__(self, constraints: _Optional[_Iterable[_Union[_constraint_pb2.Constraint, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPoliciesResponse(_message.Message):
    __slots__ = ('policies', 'next_page_token')
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[Policy]
    next_page_token: str

    def __init__(self, policies: _Optional[_Iterable[_Union[Policy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetEffectivePolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreatePolicyRequest(_message.Message):
    __slots__ = ('parent', 'policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    policy: Policy

    def __init__(self, parent: _Optional[str]=..., policy: _Optional[_Union[Policy, _Mapping]]=...) -> None:
        ...

class UpdatePolicyRequest(_message.Message):
    __slots__ = ('policy', 'update_mask')
    POLICY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeletePolicyRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class CreateCustomConstraintRequest(_message.Message):
    __slots__ = ('parent', 'custom_constraint')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    custom_constraint: _constraint_pb2.CustomConstraint

    def __init__(self, parent: _Optional[str]=..., custom_constraint: _Optional[_Union[_constraint_pb2.CustomConstraint, _Mapping]]=...) -> None:
        ...

class GetCustomConstraintRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCustomConstraintsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListCustomConstraintsResponse(_message.Message):
    __slots__ = ('custom_constraints', 'next_page_token')
    CUSTOM_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    custom_constraints: _containers.RepeatedCompositeFieldContainer[_constraint_pb2.CustomConstraint]
    next_page_token: str

    def __init__(self, custom_constraints: _Optional[_Iterable[_Union[_constraint_pb2.CustomConstraint, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateCustomConstraintRequest(_message.Message):
    __slots__ = ('custom_constraint',)
    CUSTOM_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    custom_constraint: _constraint_pb2.CustomConstraint

    def __init__(self, custom_constraint: _Optional[_Union[_constraint_pb2.CustomConstraint, _Mapping]]=...) -> None:
        ...

class DeleteCustomConstraintRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...