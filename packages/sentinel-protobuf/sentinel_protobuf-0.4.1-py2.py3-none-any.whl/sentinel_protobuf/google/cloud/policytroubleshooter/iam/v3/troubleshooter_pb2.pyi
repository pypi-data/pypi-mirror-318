from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.iam.v2 import policy_pb2 as _policy_pb2_1
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AllowAccessState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALLOW_ACCESS_STATE_UNSPECIFIED: _ClassVar[AllowAccessState]
    ALLOW_ACCESS_STATE_GRANTED: _ClassVar[AllowAccessState]
    ALLOW_ACCESS_STATE_NOT_GRANTED: _ClassVar[AllowAccessState]
    ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL: _ClassVar[AllowAccessState]
    ALLOW_ACCESS_STATE_UNKNOWN_INFO: _ClassVar[AllowAccessState]

class DenyAccessState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DENY_ACCESS_STATE_UNSPECIFIED: _ClassVar[DenyAccessState]
    DENY_ACCESS_STATE_DENIED: _ClassVar[DenyAccessState]
    DENY_ACCESS_STATE_NOT_DENIED: _ClassVar[DenyAccessState]
    DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL: _ClassVar[DenyAccessState]
    DENY_ACCESS_STATE_UNKNOWN_INFO: _ClassVar[DenyAccessState]

class RolePermissionInclusionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_PERMISSION_INCLUSION_STATE_UNSPECIFIED: _ClassVar[RolePermissionInclusionState]
    ROLE_PERMISSION_INCLUDED: _ClassVar[RolePermissionInclusionState]
    ROLE_PERMISSION_NOT_INCLUDED: _ClassVar[RolePermissionInclusionState]
    ROLE_PERMISSION_UNKNOWN_INFO: _ClassVar[RolePermissionInclusionState]

class PermissionPatternMatchingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERMISSION_PATTERN_MATCHING_STATE_UNSPECIFIED: _ClassVar[PermissionPatternMatchingState]
    PERMISSION_PATTERN_MATCHED: _ClassVar[PermissionPatternMatchingState]
    PERMISSION_PATTERN_NOT_MATCHED: _ClassVar[PermissionPatternMatchingState]

class MembershipMatchingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMBERSHIP_MATCHING_STATE_UNSPECIFIED: _ClassVar[MembershipMatchingState]
    MEMBERSHIP_MATCHED: _ClassVar[MembershipMatchingState]
    MEMBERSHIP_NOT_MATCHED: _ClassVar[MembershipMatchingState]
    MEMBERSHIP_UNKNOWN_INFO: _ClassVar[MembershipMatchingState]
    MEMBERSHIP_UNKNOWN_UNSUPPORTED: _ClassVar[MembershipMatchingState]

class HeuristicRelevance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEURISTIC_RELEVANCE_UNSPECIFIED: _ClassVar[HeuristicRelevance]
    HEURISTIC_RELEVANCE_NORMAL: _ClassVar[HeuristicRelevance]
    HEURISTIC_RELEVANCE_HIGH: _ClassVar[HeuristicRelevance]
ALLOW_ACCESS_STATE_UNSPECIFIED: AllowAccessState
ALLOW_ACCESS_STATE_GRANTED: AllowAccessState
ALLOW_ACCESS_STATE_NOT_GRANTED: AllowAccessState
ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL: AllowAccessState
ALLOW_ACCESS_STATE_UNKNOWN_INFO: AllowAccessState
DENY_ACCESS_STATE_UNSPECIFIED: DenyAccessState
DENY_ACCESS_STATE_DENIED: DenyAccessState
DENY_ACCESS_STATE_NOT_DENIED: DenyAccessState
DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL: DenyAccessState
DENY_ACCESS_STATE_UNKNOWN_INFO: DenyAccessState
ROLE_PERMISSION_INCLUSION_STATE_UNSPECIFIED: RolePermissionInclusionState
ROLE_PERMISSION_INCLUDED: RolePermissionInclusionState
ROLE_PERMISSION_NOT_INCLUDED: RolePermissionInclusionState
ROLE_PERMISSION_UNKNOWN_INFO: RolePermissionInclusionState
PERMISSION_PATTERN_MATCHING_STATE_UNSPECIFIED: PermissionPatternMatchingState
PERMISSION_PATTERN_MATCHED: PermissionPatternMatchingState
PERMISSION_PATTERN_NOT_MATCHED: PermissionPatternMatchingState
MEMBERSHIP_MATCHING_STATE_UNSPECIFIED: MembershipMatchingState
MEMBERSHIP_MATCHED: MembershipMatchingState
MEMBERSHIP_NOT_MATCHED: MembershipMatchingState
MEMBERSHIP_UNKNOWN_INFO: MembershipMatchingState
MEMBERSHIP_UNKNOWN_UNSUPPORTED: MembershipMatchingState
HEURISTIC_RELEVANCE_UNSPECIFIED: HeuristicRelevance
HEURISTIC_RELEVANCE_NORMAL: HeuristicRelevance
HEURISTIC_RELEVANCE_HIGH: HeuristicRelevance

class TroubleshootIamPolicyRequest(_message.Message):
    __slots__ = ('access_tuple',)
    ACCESS_TUPLE_FIELD_NUMBER: _ClassVar[int]
    access_tuple: AccessTuple

    def __init__(self, access_tuple: _Optional[_Union[AccessTuple, _Mapping]]=...) -> None:
        ...

class TroubleshootIamPolicyResponse(_message.Message):
    __slots__ = ('overall_access_state', 'access_tuple', 'allow_policy_explanation', 'deny_policy_explanation')

    class OverallAccessState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OVERALL_ACCESS_STATE_UNSPECIFIED: _ClassVar[TroubleshootIamPolicyResponse.OverallAccessState]
        CAN_ACCESS: _ClassVar[TroubleshootIamPolicyResponse.OverallAccessState]
        CANNOT_ACCESS: _ClassVar[TroubleshootIamPolicyResponse.OverallAccessState]
        UNKNOWN_INFO: _ClassVar[TroubleshootIamPolicyResponse.OverallAccessState]
        UNKNOWN_CONDITIONAL: _ClassVar[TroubleshootIamPolicyResponse.OverallAccessState]
    OVERALL_ACCESS_STATE_UNSPECIFIED: TroubleshootIamPolicyResponse.OverallAccessState
    CAN_ACCESS: TroubleshootIamPolicyResponse.OverallAccessState
    CANNOT_ACCESS: TroubleshootIamPolicyResponse.OverallAccessState
    UNKNOWN_INFO: TroubleshootIamPolicyResponse.OverallAccessState
    UNKNOWN_CONDITIONAL: TroubleshootIamPolicyResponse.OverallAccessState
    OVERALL_ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TUPLE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_POLICY_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    DENY_POLICY_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    overall_access_state: TroubleshootIamPolicyResponse.OverallAccessState
    access_tuple: AccessTuple
    allow_policy_explanation: AllowPolicyExplanation
    deny_policy_explanation: DenyPolicyExplanation

    def __init__(self, overall_access_state: _Optional[_Union[TroubleshootIamPolicyResponse.OverallAccessState, str]]=..., access_tuple: _Optional[_Union[AccessTuple, _Mapping]]=..., allow_policy_explanation: _Optional[_Union[AllowPolicyExplanation, _Mapping]]=..., deny_policy_explanation: _Optional[_Union[DenyPolicyExplanation, _Mapping]]=...) -> None:
        ...

class AccessTuple(_message.Message):
    __slots__ = ('principal', 'full_resource_name', 'permission', 'permission_fqdn', 'condition_context')
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FQDN_FIELD_NUMBER: _ClassVar[int]
    CONDITION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    principal: str
    full_resource_name: str
    permission: str
    permission_fqdn: str
    condition_context: ConditionContext

    def __init__(self, principal: _Optional[str]=..., full_resource_name: _Optional[str]=..., permission: _Optional[str]=..., permission_fqdn: _Optional[str]=..., condition_context: _Optional[_Union[ConditionContext, _Mapping]]=...) -> None:
        ...

class ConditionContext(_message.Message):
    __slots__ = ('resource', 'destination', 'request', 'effective_tags')

    class Resource(_message.Message):
        __slots__ = ('service', 'name', 'type')
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        service: str
        name: str
        type: str

        def __init__(self, service: _Optional[str]=..., name: _Optional[str]=..., type: _Optional[str]=...) -> None:
            ...

    class Peer(_message.Message):
        __slots__ = ('ip', 'port')
        IP_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        ip: str
        port: int

        def __init__(self, ip: _Optional[str]=..., port: _Optional[int]=...) -> None:
            ...

    class Request(_message.Message):
        __slots__ = ('receive_time',)
        RECEIVE_TIME_FIELD_NUMBER: _ClassVar[int]
        receive_time: _timestamp_pb2.Timestamp

        def __init__(self, receive_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class EffectiveTag(_message.Message):
        __slots__ = ('tag_value', 'namespaced_tag_value', 'tag_key', 'namespaced_tag_key', 'tag_key_parent_name', 'inherited')
        TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
        NAMESPACED_TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
        TAG_KEY_FIELD_NUMBER: _ClassVar[int]
        NAMESPACED_TAG_KEY_FIELD_NUMBER: _ClassVar[int]
        TAG_KEY_PARENT_NAME_FIELD_NUMBER: _ClassVar[int]
        INHERITED_FIELD_NUMBER: _ClassVar[int]
        tag_value: str
        namespaced_tag_value: str
        tag_key: str
        namespaced_tag_key: str
        tag_key_parent_name: str
        inherited: bool

        def __init__(self, tag_value: _Optional[str]=..., namespaced_tag_value: _Optional[str]=..., tag_key: _Optional[str]=..., namespaced_tag_key: _Optional[str]=..., tag_key_parent_name: _Optional[str]=..., inherited: bool=...) -> None:
            ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TAGS_FIELD_NUMBER: _ClassVar[int]
    resource: ConditionContext.Resource
    destination: ConditionContext.Peer
    request: ConditionContext.Request
    effective_tags: _containers.RepeatedCompositeFieldContainer[ConditionContext.EffectiveTag]

    def __init__(self, resource: _Optional[_Union[ConditionContext.Resource, _Mapping]]=..., destination: _Optional[_Union[ConditionContext.Peer, _Mapping]]=..., request: _Optional[_Union[ConditionContext.Request, _Mapping]]=..., effective_tags: _Optional[_Iterable[_Union[ConditionContext.EffectiveTag, _Mapping]]]=...) -> None:
        ...

class AllowPolicyExplanation(_message.Message):
    __slots__ = ('allow_access_state', 'explained_policies', 'relevance')
    ALLOW_ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    EXPLAINED_POLICIES_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    allow_access_state: AllowAccessState
    explained_policies: _containers.RepeatedCompositeFieldContainer[ExplainedAllowPolicy]
    relevance: HeuristicRelevance

    def __init__(self, allow_access_state: _Optional[_Union[AllowAccessState, str]]=..., explained_policies: _Optional[_Iterable[_Union[ExplainedAllowPolicy, _Mapping]]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=...) -> None:
        ...

class ExplainedAllowPolicy(_message.Message):
    __slots__ = ('allow_access_state', 'full_resource_name', 'binding_explanations', 'relevance', 'policy')
    ALLOW_ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    BINDING_EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    allow_access_state: AllowAccessState
    full_resource_name: str
    binding_explanations: _containers.RepeatedCompositeFieldContainer[AllowBindingExplanation]
    relevance: HeuristicRelevance
    policy: _policy_pb2.Policy

    def __init__(self, allow_access_state: _Optional[_Union[AllowAccessState, str]]=..., full_resource_name: _Optional[str]=..., binding_explanations: _Optional[_Iterable[_Union[AllowBindingExplanation, _Mapping]]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]]=...) -> None:
        ...

class AllowBindingExplanation(_message.Message):
    __slots__ = ('allow_access_state', 'role', 'role_permission', 'role_permission_relevance', 'combined_membership', 'memberships', 'relevance', 'condition', 'condition_explanation')

    class AnnotatedAllowMembership(_message.Message):
        __slots__ = ('membership', 'relevance')
        MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
        RELEVANCE_FIELD_NUMBER: _ClassVar[int]
        membership: MembershipMatchingState
        relevance: HeuristicRelevance

        def __init__(self, membership: _Optional[_Union[MembershipMatchingState, str]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=...) -> None:
            ...

    class MembershipsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AllowBindingExplanation.AnnotatedAllowMembership

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AllowBindingExplanation.AnnotatedAllowMembership, _Mapping]]=...) -> None:
            ...
    ALLOW_ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    ROLE_PERMISSION_RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    COMBINED_MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    CONDITION_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    allow_access_state: AllowAccessState
    role: str
    role_permission: RolePermissionInclusionState
    role_permission_relevance: HeuristicRelevance
    combined_membership: AllowBindingExplanation.AnnotatedAllowMembership
    memberships: _containers.MessageMap[str, AllowBindingExplanation.AnnotatedAllowMembership]
    relevance: HeuristicRelevance
    condition: _expr_pb2.Expr
    condition_explanation: ConditionExplanation

    def __init__(self, allow_access_state: _Optional[_Union[AllowAccessState, str]]=..., role: _Optional[str]=..., role_permission: _Optional[_Union[RolePermissionInclusionState, str]]=..., role_permission_relevance: _Optional[_Union[HeuristicRelevance, str]]=..., combined_membership: _Optional[_Union[AllowBindingExplanation.AnnotatedAllowMembership, _Mapping]]=..., memberships: _Optional[_Mapping[str, AllowBindingExplanation.AnnotatedAllowMembership]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=..., condition_explanation: _Optional[_Union[ConditionExplanation, _Mapping]]=...) -> None:
        ...

class DenyPolicyExplanation(_message.Message):
    __slots__ = ('deny_access_state', 'explained_resources', 'relevance', 'permission_deniable')
    DENY_ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    EXPLAINED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIABLE_FIELD_NUMBER: _ClassVar[int]
    deny_access_state: DenyAccessState
    explained_resources: _containers.RepeatedCompositeFieldContainer[ExplainedDenyResource]
    relevance: HeuristicRelevance
    permission_deniable: bool

    def __init__(self, deny_access_state: _Optional[_Union[DenyAccessState, str]]=..., explained_resources: _Optional[_Iterable[_Union[ExplainedDenyResource, _Mapping]]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=..., permission_deniable: bool=...) -> None:
        ...

class ExplainedDenyResource(_message.Message):
    __slots__ = ('deny_access_state', 'full_resource_name', 'explained_policies', 'relevance')
    DENY_ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPLAINED_POLICIES_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    deny_access_state: DenyAccessState
    full_resource_name: str
    explained_policies: _containers.RepeatedCompositeFieldContainer[ExplainedDenyPolicy]
    relevance: HeuristicRelevance

    def __init__(self, deny_access_state: _Optional[_Union[DenyAccessState, str]]=..., full_resource_name: _Optional[str]=..., explained_policies: _Optional[_Iterable[_Union[ExplainedDenyPolicy, _Mapping]]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=...) -> None:
        ...

class ExplainedDenyPolicy(_message.Message):
    __slots__ = ('deny_access_state', 'policy', 'rule_explanations', 'relevance')
    DENY_ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    RULE_EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    deny_access_state: DenyAccessState
    policy: _policy_pb2_1.Policy
    rule_explanations: _containers.RepeatedCompositeFieldContainer[DenyRuleExplanation]
    relevance: HeuristicRelevance

    def __init__(self, deny_access_state: _Optional[_Union[DenyAccessState, str]]=..., policy: _Optional[_Union[_policy_pb2_1.Policy, _Mapping]]=..., rule_explanations: _Optional[_Iterable[_Union[DenyRuleExplanation, _Mapping]]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=...) -> None:
        ...

class DenyRuleExplanation(_message.Message):
    __slots__ = ('deny_access_state', 'combined_denied_permission', 'denied_permissions', 'combined_exception_permission', 'exception_permissions', 'combined_denied_principal', 'denied_principals', 'combined_exception_principal', 'exception_principals', 'relevance', 'condition', 'condition_explanation')

    class AnnotatedPermissionMatching(_message.Message):
        __slots__ = ('permission_matching_state', 'relevance')
        PERMISSION_MATCHING_STATE_FIELD_NUMBER: _ClassVar[int]
        RELEVANCE_FIELD_NUMBER: _ClassVar[int]
        permission_matching_state: PermissionPatternMatchingState
        relevance: HeuristicRelevance

        def __init__(self, permission_matching_state: _Optional[_Union[PermissionPatternMatchingState, str]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=...) -> None:
            ...

    class AnnotatedDenyPrincipalMatching(_message.Message):
        __slots__ = ('membership', 'relevance')
        MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
        RELEVANCE_FIELD_NUMBER: _ClassVar[int]
        membership: MembershipMatchingState
        relevance: HeuristicRelevance

        def __init__(self, membership: _Optional[_Union[MembershipMatchingState, str]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=...) -> None:
            ...

    class DeniedPermissionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DenyRuleExplanation.AnnotatedPermissionMatching

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[DenyRuleExplanation.AnnotatedPermissionMatching, _Mapping]]=...) -> None:
            ...

    class ExceptionPermissionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DenyRuleExplanation.AnnotatedPermissionMatching

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[DenyRuleExplanation.AnnotatedPermissionMatching, _Mapping]]=...) -> None:
            ...

    class DeniedPrincipalsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DenyRuleExplanation.AnnotatedDenyPrincipalMatching

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[DenyRuleExplanation.AnnotatedDenyPrincipalMatching, _Mapping]]=...) -> None:
            ...

    class ExceptionPrincipalsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DenyRuleExplanation.AnnotatedDenyPrincipalMatching

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[DenyRuleExplanation.AnnotatedDenyPrincipalMatching, _Mapping]]=...) -> None:
            ...
    DENY_ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    COMBINED_DENIED_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    DENIED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    COMBINED_EXCEPTION_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    COMBINED_DENIED_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    DENIED_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    COMBINED_EXCEPTION_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    CONDITION_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    deny_access_state: DenyAccessState
    combined_denied_permission: DenyRuleExplanation.AnnotatedPermissionMatching
    denied_permissions: _containers.MessageMap[str, DenyRuleExplanation.AnnotatedPermissionMatching]
    combined_exception_permission: DenyRuleExplanation.AnnotatedPermissionMatching
    exception_permissions: _containers.MessageMap[str, DenyRuleExplanation.AnnotatedPermissionMatching]
    combined_denied_principal: DenyRuleExplanation.AnnotatedDenyPrincipalMatching
    denied_principals: _containers.MessageMap[str, DenyRuleExplanation.AnnotatedDenyPrincipalMatching]
    combined_exception_principal: DenyRuleExplanation.AnnotatedDenyPrincipalMatching
    exception_principals: _containers.MessageMap[str, DenyRuleExplanation.AnnotatedDenyPrincipalMatching]
    relevance: HeuristicRelevance
    condition: _expr_pb2.Expr
    condition_explanation: ConditionExplanation

    def __init__(self, deny_access_state: _Optional[_Union[DenyAccessState, str]]=..., combined_denied_permission: _Optional[_Union[DenyRuleExplanation.AnnotatedPermissionMatching, _Mapping]]=..., denied_permissions: _Optional[_Mapping[str, DenyRuleExplanation.AnnotatedPermissionMatching]]=..., combined_exception_permission: _Optional[_Union[DenyRuleExplanation.AnnotatedPermissionMatching, _Mapping]]=..., exception_permissions: _Optional[_Mapping[str, DenyRuleExplanation.AnnotatedPermissionMatching]]=..., combined_denied_principal: _Optional[_Union[DenyRuleExplanation.AnnotatedDenyPrincipalMatching, _Mapping]]=..., denied_principals: _Optional[_Mapping[str, DenyRuleExplanation.AnnotatedDenyPrincipalMatching]]=..., combined_exception_principal: _Optional[_Union[DenyRuleExplanation.AnnotatedDenyPrincipalMatching, _Mapping]]=..., exception_principals: _Optional[_Mapping[str, DenyRuleExplanation.AnnotatedDenyPrincipalMatching]]=..., relevance: _Optional[_Union[HeuristicRelevance, str]]=..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=..., condition_explanation: _Optional[_Union[ConditionExplanation, _Mapping]]=...) -> None:
        ...

class ConditionExplanation(_message.Message):
    __slots__ = ('value', 'errors', 'evaluation_states')

    class EvaluationState(_message.Message):
        __slots__ = ('start', 'end', 'value', 'errors')
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ERRORS_FIELD_NUMBER: _ClassVar[int]
        start: int
        end: int
        value: _struct_pb2.Value
        errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

        def __init__(self, start: _Optional[int]=..., end: _Optional[int]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
            ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_STATES_FIELD_NUMBER: _ClassVar[int]
    value: _struct_pb2.Value
    errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    evaluation_states: _containers.RepeatedCompositeFieldContainer[ConditionExplanation.EvaluationState]

    def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., evaluation_states: _Optional[_Iterable[_Union[ConditionExplanation.EvaluationState, _Mapping]]]=...) -> None:
        ...