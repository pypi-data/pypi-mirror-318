from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AccessState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_STATE_UNSPECIFIED: _ClassVar[AccessState]
    GRANTED: _ClassVar[AccessState]
    NOT_GRANTED: _ClassVar[AccessState]
    UNKNOWN_CONDITIONAL: _ClassVar[AccessState]
    UNKNOWN_INFO_DENIED: _ClassVar[AccessState]

class HeuristicRelevance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEURISTIC_RELEVANCE_UNSPECIFIED: _ClassVar[HeuristicRelevance]
    NORMAL: _ClassVar[HeuristicRelevance]
    HIGH: _ClassVar[HeuristicRelevance]
ACCESS_STATE_UNSPECIFIED: AccessState
GRANTED: AccessState
NOT_GRANTED: AccessState
UNKNOWN_CONDITIONAL: AccessState
UNKNOWN_INFO_DENIED: AccessState
HEURISTIC_RELEVANCE_UNSPECIFIED: HeuristicRelevance
NORMAL: HeuristicRelevance
HIGH: HeuristicRelevance

class AccessTuple(_message.Message):
    __slots__ = ('principal', 'full_resource_name', 'permission')
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    principal: str
    full_resource_name: str
    permission: str

    def __init__(self, principal: _Optional[str]=..., full_resource_name: _Optional[str]=..., permission: _Optional[str]=...) -> None:
        ...

class ExplainedPolicy(_message.Message):
    __slots__ = ('access', 'full_resource_name', 'policy', 'binding_explanations', 'relevance')
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    BINDING_EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    access: AccessState
    full_resource_name: str
    policy: _policy_pb2.Policy
    binding_explanations: _containers.RepeatedCompositeFieldContainer[BindingExplanation]
    relevance: HeuristicRelevance

    def __init__(self, access: _Optional[_Union[AccessState, str]]=..., full_resource_name: _Optional[str]=..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]]=..., binding_explanations: _Optional[_Iterable[_Union[BindingExplanation, _Mapping]]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=...) -> None:
        ...

class BindingExplanation(_message.Message):
    __slots__ = ('access', 'role', 'role_permission', 'role_permission_relevance', 'memberships', 'relevance', 'condition')

    class RolePermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_PERMISSION_UNSPECIFIED: _ClassVar[BindingExplanation.RolePermission]
        ROLE_PERMISSION_INCLUDED: _ClassVar[BindingExplanation.RolePermission]
        ROLE_PERMISSION_NOT_INCLUDED: _ClassVar[BindingExplanation.RolePermission]
        ROLE_PERMISSION_UNKNOWN_INFO_DENIED: _ClassVar[BindingExplanation.RolePermission]
    ROLE_PERMISSION_UNSPECIFIED: BindingExplanation.RolePermission
    ROLE_PERMISSION_INCLUDED: BindingExplanation.RolePermission
    ROLE_PERMISSION_NOT_INCLUDED: BindingExplanation.RolePermission
    ROLE_PERMISSION_UNKNOWN_INFO_DENIED: BindingExplanation.RolePermission

    class Membership(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEMBERSHIP_UNSPECIFIED: _ClassVar[BindingExplanation.Membership]
        MEMBERSHIP_INCLUDED: _ClassVar[BindingExplanation.Membership]
        MEMBERSHIP_NOT_INCLUDED: _ClassVar[BindingExplanation.Membership]
        MEMBERSHIP_UNKNOWN_INFO_DENIED: _ClassVar[BindingExplanation.Membership]
        MEMBERSHIP_UNKNOWN_UNSUPPORTED: _ClassVar[BindingExplanation.Membership]
    MEMBERSHIP_UNSPECIFIED: BindingExplanation.Membership
    MEMBERSHIP_INCLUDED: BindingExplanation.Membership
    MEMBERSHIP_NOT_INCLUDED: BindingExplanation.Membership
    MEMBERSHIP_UNKNOWN_INFO_DENIED: BindingExplanation.Membership
    MEMBERSHIP_UNKNOWN_UNSUPPORTED: BindingExplanation.Membership

    class AnnotatedMembership(_message.Message):
        __slots__ = ('membership', 'relevance')
        MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
        RELEVANCE_FIELD_NUMBER: _ClassVar[int]
        membership: BindingExplanation.Membership
        relevance: HeuristicRelevance

        def __init__(self, membership: _Optional[_Union[BindingExplanation.Membership, str]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=...) -> None:
            ...

    class MembershipsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BindingExplanation.AnnotatedMembership

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[BindingExplanation.AnnotatedMembership, _Mapping]]=...) -> None:
            ...
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    ROLE_PERMISSION_RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    access: AccessState
    role: str
    role_permission: BindingExplanation.RolePermission
    role_permission_relevance: HeuristicRelevance
    memberships: _containers.MessageMap[str, BindingExplanation.AnnotatedMembership]
    relevance: HeuristicRelevance
    condition: _expr_pb2.Expr

    def __init__(self, access: _Optional[_Union[AccessState, str]]=..., role: _Optional[str]=..., role_permission: _Optional[_Union[BindingExplanation.RolePermission, str]]=..., role_permission_relevance: _Optional[_Union[HeuristicRelevance, str]]=..., memberships: _Optional[_Mapping[str, BindingExplanation.AnnotatedMembership]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=...) -> None:
        ...