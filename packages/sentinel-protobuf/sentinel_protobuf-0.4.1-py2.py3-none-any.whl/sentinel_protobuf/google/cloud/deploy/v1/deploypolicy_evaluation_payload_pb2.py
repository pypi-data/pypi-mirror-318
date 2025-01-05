"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/deploy/v1/deploypolicy_evaluation_payload.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.deploy.v1 import cloud_deploy_pb2 as google_dot_cloud_dot_deploy_dot_v1_dot_cloud__deploy__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/deploy/v1/deploypolicy_evaluation_payload.proto\x12\x16google.cloud.deploy.v1\x1a)google/cloud/deploy/v1/cloud_deploy.proto"\xa5\x05\n\x1bDeployPolicyEvaluationEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\trule_type\x18\x02 \x01(\t\x12\x0c\n\x04rule\x18\x03 \x01(\t\x12\x14\n\x0cpipeline_uid\x18\x04 \x01(\t\x12\x19\n\x11delivery_pipeline\x18\x05 \x01(\t\x12\x12\n\ntarget_uid\x18\x06 \x01(\t\x12\x0e\n\x06target\x18\x07 \x01(\t\x12=\n\x07invoker\x18\x08 \x01(\x0e2,.google.cloud.deploy.v1.DeployPolicy.Invoker\x12\x15\n\rdeploy_policy\x18\t \x01(\t\x12\x19\n\x11deploy_policy_uid\x18\n \x01(\t\x12\x0f\n\x07allowed\x18\x0b \x01(\x08\x12R\n\x07verdict\x18\x0c \x01(\x0e2A.google.cloud.deploy.v1.DeployPolicyEvaluationEvent.PolicyVerdict\x12\\\n\toverrides\x18\r \x03(\x0e2I.google.cloud.deploy.v1.DeployPolicyEvaluationEvent.PolicyVerdictOverride"\\\n\rPolicyVerdict\x12\x1e\n\x1aPOLICY_VERDICT_UNSPECIFIED\x10\x00\x12\x15\n\x11ALLOWED_BY_POLICY\x10\x01\x12\x14\n\x10DENIED_BY_POLICY\x10\x02"m\n\x15PolicyVerdictOverride\x12\'\n#POLICY_VERDICT_OVERRIDE_UNSPECIFIED\x10\x00\x12\x15\n\x11POLICY_OVERRIDDEN\x10\x01\x12\x14\n\x10POLICY_SUSPENDED\x10\x02Bv\n\x1acom.google.cloud.deploy.v1B"DeployPolicyEvaluationPayloadProtoP\x01Z2cloud.google.com/go/deploy/apiv1/deploypb;deploypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.deploy.v1.deploypolicy_evaluation_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.deploy.v1B"DeployPolicyEvaluationPayloadProtoP\x01Z2cloud.google.com/go/deploy/apiv1/deploypb;deploypb'
    _globals['_DEPLOYPOLICYEVALUATIONEVENT']._serialized_start = 132
    _globals['_DEPLOYPOLICYEVALUATIONEVENT']._serialized_end = 809
    _globals['_DEPLOYPOLICYEVALUATIONEVENT_POLICYVERDICT']._serialized_start = 606
    _globals['_DEPLOYPOLICYEVALUATIONEVENT_POLICYVERDICT']._serialized_end = 698
    _globals['_DEPLOYPOLICYEVALUATIONEVENT_POLICYVERDICTOVERRIDE']._serialized_start = 700
    _globals['_DEPLOYPOLICYEVALUATIONEVENT_POLICYVERDICTOVERRIDE']._serialized_end = 809