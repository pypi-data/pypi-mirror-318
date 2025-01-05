from google.cloud.deploy.v1 import cloud_deploy_pb2 as _cloud_deploy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeployPolicyEvaluationEvent(_message.Message):
    __slots__ = ('message', 'rule_type', 'rule', 'pipeline_uid', 'delivery_pipeline', 'target_uid', 'target', 'invoker', 'deploy_policy', 'deploy_policy_uid', 'allowed', 'verdict', 'overrides')

    class PolicyVerdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POLICY_VERDICT_UNSPECIFIED: _ClassVar[DeployPolicyEvaluationEvent.PolicyVerdict]
        ALLOWED_BY_POLICY: _ClassVar[DeployPolicyEvaluationEvent.PolicyVerdict]
        DENIED_BY_POLICY: _ClassVar[DeployPolicyEvaluationEvent.PolicyVerdict]
    POLICY_VERDICT_UNSPECIFIED: DeployPolicyEvaluationEvent.PolicyVerdict
    ALLOWED_BY_POLICY: DeployPolicyEvaluationEvent.PolicyVerdict
    DENIED_BY_POLICY: DeployPolicyEvaluationEvent.PolicyVerdict

    class PolicyVerdictOverride(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POLICY_VERDICT_OVERRIDE_UNSPECIFIED: _ClassVar[DeployPolicyEvaluationEvent.PolicyVerdictOverride]
        POLICY_OVERRIDDEN: _ClassVar[DeployPolicyEvaluationEvent.PolicyVerdictOverride]
        POLICY_SUSPENDED: _ClassVar[DeployPolicyEvaluationEvent.PolicyVerdictOverride]
    POLICY_VERDICT_OVERRIDE_UNSPECIFIED: DeployPolicyEvaluationEvent.PolicyVerdictOverride
    POLICY_OVERRIDDEN: DeployPolicyEvaluationEvent.PolicyVerdictOverride
    POLICY_SUSPENDED: DeployPolicyEvaluationEvent.PolicyVerdictOverride
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_UID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    INVOKER_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_POLICY_UID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    message: str
    rule_type: str
    rule: str
    pipeline_uid: str
    delivery_pipeline: str
    target_uid: str
    target: str
    invoker: _cloud_deploy_pb2.DeployPolicy.Invoker
    deploy_policy: str
    deploy_policy_uid: str
    allowed: bool
    verdict: DeployPolicyEvaluationEvent.PolicyVerdict
    overrides: _containers.RepeatedScalarFieldContainer[DeployPolicyEvaluationEvent.PolicyVerdictOverride]

    def __init__(self, message: _Optional[str]=..., rule_type: _Optional[str]=..., rule: _Optional[str]=..., pipeline_uid: _Optional[str]=..., delivery_pipeline: _Optional[str]=..., target_uid: _Optional[str]=..., target: _Optional[str]=..., invoker: _Optional[_Union[_cloud_deploy_pb2.DeployPolicy.Invoker, str]]=..., deploy_policy: _Optional[str]=..., deploy_policy_uid: _Optional[str]=..., allowed: bool=..., verdict: _Optional[_Union[DeployPolicyEvaluationEvent.PolicyVerdict, str]]=..., overrides: _Optional[_Iterable[_Union[DeployPolicyEvaluationEvent.PolicyVerdictOverride, str]]]=...) -> None:
        ...