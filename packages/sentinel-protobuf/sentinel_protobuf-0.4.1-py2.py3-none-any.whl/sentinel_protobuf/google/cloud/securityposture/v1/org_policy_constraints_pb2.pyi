from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.securityposture.v1 import org_policy_config_pb2 as _org_policy_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OrgPolicyConstraint(_message.Message):
    __slots__ = ('canned_constraint_id', 'policy_rules')
    CANNED_CONSTRAINT_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_RULES_FIELD_NUMBER: _ClassVar[int]
    canned_constraint_id: str
    policy_rules: _containers.RepeatedCompositeFieldContainer[_org_policy_config_pb2.PolicyRule]

    def __init__(self, canned_constraint_id: _Optional[str]=..., policy_rules: _Optional[_Iterable[_Union[_org_policy_config_pb2.PolicyRule, _Mapping]]]=...) -> None:
        ...

class OrgPolicyConstraintCustom(_message.Message):
    __slots__ = ('custom_constraint', 'policy_rules')
    CUSTOM_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    POLICY_RULES_FIELD_NUMBER: _ClassVar[int]
    custom_constraint: _org_policy_config_pb2.CustomConstraint
    policy_rules: _containers.RepeatedCompositeFieldContainer[_org_policy_config_pb2.PolicyRule]

    def __init__(self, custom_constraint: _Optional[_Union[_org_policy_config_pb2.CustomConstraint, _Mapping]]=..., policy_rules: _Optional[_Iterable[_Union[_org_policy_config_pb2.PolicyRule, _Mapping]]]=...) -> None:
        ...