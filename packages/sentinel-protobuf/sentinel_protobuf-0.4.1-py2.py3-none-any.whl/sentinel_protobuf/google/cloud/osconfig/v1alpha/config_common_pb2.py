"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1alpha/config_common.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/osconfig/v1alpha/config_common.proto\x12\x1dgoogle.cloud.osconfig.v1alpha"\xb1\x03\n\x1aOSPolicyResourceConfigStep\x12L\n\x04type\x18\x01 \x01(\x0e2>.google.cloud.osconfig.v1alpha.OSPolicyResourceConfigStep.Type\x12R\n\x07outcome\x18\x02 \x01(\x0e2A.google.cloud.osconfig.v1alpha.OSPolicyResourceConfigStep.Outcome\x12\x15\n\rerror_message\x18\x03 \x01(\t"\x92\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nVALIDATION\x10\x01\x12\x17\n\x13DESIRED_STATE_CHECK\x10\x02\x12\x1d\n\x19DESIRED_STATE_ENFORCEMENT\x10\x03\x12(\n$DESIRED_STATE_CHECK_POST_ENFORCEMENT\x10\x04\x1a\x02\x18\x01"A\n\x07Outcome\x12\x17\n\x13OUTCOME_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02\x1a\x02\x18\x01:\x02\x18\x01"\x85\x03\n\x1aOSPolicyResourceCompliance\x12\x1d\n\x15os_policy_resource_id\x18\x01 \x01(\t\x12O\n\x0cconfig_steps\x18\x02 \x03(\x0b29.google.cloud.osconfig.v1alpha.OSPolicyResourceConfigStep\x12E\n\x05state\x18\x03 \x01(\x0e26.google.cloud.osconfig.v1alpha.OSPolicyComplianceState\x12l\n\x14exec_resource_output\x18\x04 \x01(\x0b2L.google.cloud.osconfig.v1alpha.OSPolicyResourceCompliance.ExecResourceOutputH\x00\x1a4\n\x12ExecResourceOutput\x12\x1a\n\x12enforcement_output\x18\x02 \x01(\x0c:\x02\x18\x01:\x02\x18\x01B\x08\n\x06output*\x97\x01\n\x17OSPolicyComplianceState\x12*\n&OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED\x10\x00\x12\r\n\tCOMPLIANT\x10\x01\x12\x11\n\rNON_COMPLIANT\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03\x12\x1d\n\x19NO_OS_POLICIES_APPLICABLE\x10\x04\x1a\x02\x18\x01B\xda\x01\n!com.google.cloud.osconfig.v1alphaB\x11ConfigCommonProtoP\x01Z=cloud.google.com/go/osconfig/apiv1alpha/osconfigpb;osconfigpb\xaa\x02\x1dGoogle.Cloud.OsConfig.V1Alpha\xca\x02\x1dGoogle\\Cloud\\OsConfig\\V1alpha\xea\x02 Google::Cloud::OsConfig::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1alpha.config_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.osconfig.v1alphaB\x11ConfigCommonProtoP\x01Z=cloud.google.com/go/osconfig/apiv1alpha/osconfigpb;osconfigpb\xaa\x02\x1dGoogle.Cloud.OsConfig.V1Alpha\xca\x02\x1dGoogle\\Cloud\\OsConfig\\V1alpha\xea\x02 Google::Cloud::OsConfig::V1alpha'
    _globals['_OSPOLICYCOMPLIANCESTATE']._loaded_options = None
    _globals['_OSPOLICYCOMPLIANCESTATE']._serialized_options = b'\x18\x01'
    _globals['_OSPOLICYRESOURCECONFIGSTEP_TYPE']._loaded_options = None
    _globals['_OSPOLICYRESOURCECONFIGSTEP_TYPE']._serialized_options = b'\x18\x01'
    _globals['_OSPOLICYRESOURCECONFIGSTEP_OUTCOME']._loaded_options = None
    _globals['_OSPOLICYRESOURCECONFIGSTEP_OUTCOME']._serialized_options = b'\x18\x01'
    _globals['_OSPOLICYRESOURCECONFIGSTEP']._loaded_options = None
    _globals['_OSPOLICYRESOURCECONFIGSTEP']._serialized_options = b'\x18\x01'
    _globals['_OSPOLICYRESOURCECOMPLIANCE_EXECRESOURCEOUTPUT']._loaded_options = None
    _globals['_OSPOLICYRESOURCECOMPLIANCE_EXECRESOURCEOUTPUT']._serialized_options = b'\x18\x01'
    _globals['_OSPOLICYRESOURCECOMPLIANCE']._loaded_options = None
    _globals['_OSPOLICYRESOURCECOMPLIANCE']._serialized_options = b'\x18\x01'
    _globals['_OSPOLICYCOMPLIANCESTATE']._serialized_start = 913
    _globals['_OSPOLICYCOMPLIANCESTATE']._serialized_end = 1064
    _globals['_OSPOLICYRESOURCECONFIGSTEP']._serialized_start = 85
    _globals['_OSPOLICYRESOURCECONFIGSTEP']._serialized_end = 518
    _globals['_OSPOLICYRESOURCECONFIGSTEP_TYPE']._serialized_start = 301
    _globals['_OSPOLICYRESOURCECONFIGSTEP_TYPE']._serialized_end = 447
    _globals['_OSPOLICYRESOURCECONFIGSTEP_OUTCOME']._serialized_start = 449
    _globals['_OSPOLICYRESOURCECONFIGSTEP_OUTCOME']._serialized_end = 514
    _globals['_OSPOLICYRESOURCECOMPLIANCE']._serialized_start = 521
    _globals['_OSPOLICYRESOURCECOMPLIANCE']._serialized_end = 910
    _globals['_OSPOLICYRESOURCECOMPLIANCE_EXECRESOURCEOUTPUT']._serialized_start = 844
    _globals['_OSPOLICYRESOURCECOMPLIANCE_EXECRESOURCEOUTPUT']._serialized_end = 896