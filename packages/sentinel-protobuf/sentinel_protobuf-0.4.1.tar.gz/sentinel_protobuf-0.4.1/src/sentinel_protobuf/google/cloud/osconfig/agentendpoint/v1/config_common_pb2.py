"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/agentendpoint/v1/config_common.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/osconfig/agentendpoint/v1/config_common.proto\x12&google.cloud.osconfig.agentendpoint.v1"\xb7\x03\n\x1aOSPolicyResourceConfigStep\x12U\n\x04type\x18\x01 \x01(\x0e2G.google.cloud.osconfig.agentendpoint.v1.OSPolicyResourceConfigStep.Type\x12[\n\x07outcome\x18\x02 \x01(\x0e2J.google.cloud.osconfig.agentendpoint.v1.OSPolicyResourceConfigStep.Outcome\x12\x15\n\rerror_message\x18\x03 \x01(\t"\x8e\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nVALIDATION\x10\x01\x12\x17\n\x13DESIRED_STATE_CHECK\x10\x02\x12\x1d\n\x19DESIRED_STATE_ENFORCEMENT\x10\x03\x12(\n$DESIRED_STATE_CHECK_POST_ENFORCEMENT\x10\x04"=\n\x07Outcome\x12\x17\n\x13OUTCOME_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02"\x98\x03\n\x1aOSPolicyResourceCompliance\x12\x1d\n\x15os_policy_resource_id\x18\x01 \x01(\t\x12X\n\x0cconfig_steps\x18\x02 \x03(\x0b2B.google.cloud.osconfig.agentendpoint.v1.OSPolicyResourceConfigStep\x12N\n\x05state\x18\x03 \x01(\x0e2?.google.cloud.osconfig.agentendpoint.v1.OSPolicyComplianceState\x12u\n\x14exec_resource_output\x18\x04 \x01(\x0b2U.google.cloud.osconfig.agentendpoint.v1.OSPolicyResourceCompliance.ExecResourceOutputH\x00\x1a0\n\x12ExecResourceOutput\x12\x1a\n\x12enforcement_output\x18\x02 \x01(\x0cB\x08\n\x06output*\x93\x01\n\x17OSPolicyComplianceState\x12*\n&OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED\x10\x00\x12\r\n\tCOMPLIANT\x10\x01\x12\x11\n\rNON_COMPLIANT\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03\x12\x1d\n\x19NO_OS_POLICIES_APPLICABLE\x10\x04B\x93\x01\n*com.google.cloud.osconfig.agentendpoint.v1B\x11ConfigCommonProtoP\x01ZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.agentendpoint.v1.config_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.osconfig.agentendpoint.v1B\x11ConfigCommonProtoP\x01ZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpb'
    _globals['_OSPOLICYCOMPLIANCESTATE']._serialized_start = 956
    _globals['_OSPOLICYCOMPLIANCESTATE']._serialized_end = 1103
    _globals['_OSPOLICYRESOURCECONFIGSTEP']._serialized_start = 103
    _globals['_OSPOLICYRESOURCECONFIGSTEP']._serialized_end = 542
    _globals['_OSPOLICYRESOURCECONFIGSTEP_TYPE']._serialized_start = 337
    _globals['_OSPOLICYRESOURCECONFIGSTEP_TYPE']._serialized_end = 479
    _globals['_OSPOLICYRESOURCECONFIGSTEP_OUTCOME']._serialized_start = 481
    _globals['_OSPOLICYRESOURCECONFIGSTEP_OUTCOME']._serialized_end = 542
    _globals['_OSPOLICYRESOURCECOMPLIANCE']._serialized_start = 545
    _globals['_OSPOLICYRESOURCECOMPLIANCE']._serialized_end = 953
    _globals['_OSPOLICYRESOURCECOMPLIANCE_EXECRESOURCEOUTPUT']._serialized_start = 895
    _globals['_OSPOLICYRESOURCECOMPLIANCE_EXECRESOURCEOUTPUT']._serialized_end = 943