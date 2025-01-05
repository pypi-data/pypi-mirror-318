"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1alpha/instance_os_policies_compliance.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.osconfig.v1alpha import config_common_pb2 as google_dot_cloud_dot_osconfig_dot_v1alpha_dot_config__common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/osconfig/v1alpha/instance_os_policies_compliance.proto\x12\x1dgoogle.cloud.osconfig.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/osconfig/v1alpha/config_common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xee\x06\n\x1cInstanceOSPoliciesCompliance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08instance\x18\x02 \x01(\tB\x03\xe0A\x03\x12J\n\x05state\x18\x03 \x01(\x0e26.google.cloud.osconfig.v1alpha.OSPolicyComplianceStateB\x03\xe0A\x03\x12\x1b\n\x0edetailed_state\x18\x04 \x01(\tB\x03\xe0A\x03\x12"\n\x15detailed_state_reason\x18\x05 \x01(\tB\x03\xe0A\x03\x12r\n\x15os_policy_compliances\x18\x06 \x03(\x0b2N.google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.OSPolicyComplianceB\x03\xe0A\x03\x12C\n\x1alast_compliance_check_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12#\n\x16last_compliance_run_id\x18\x08 \x01(\tB\x03\xe0A\x03\x1a\xa7\x02\n\x12OSPolicyCompliance\x12\x14\n\x0cos_policy_id\x18\x01 \x01(\t\x12M\n\x14os_policy_assignment\x18\x02 \x01(\tB/\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment\x12E\n\x05state\x18\x04 \x01(\x0e26.google.cloud.osconfig.v1alpha.OSPolicyComplianceState\x12a\n\x1eos_policy_resource_compliances\x18\x05 \x03(\x0b29.google.cloud.osconfig.v1alpha.OSPolicyResourceCompliance:\x02\x18\x01:\x8e\x01\x18\x01\xeaA\x88\x01\n4osconfig.googleapis.com/InstanceOSPoliciesCompliance\x12Pprojects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}"x\n&GetInstanceOSPoliciesComplianceRequest\x12J\n\x04name\x18\x01 \x01(\tB<\xe0A\x02\xfaA6\n4osconfig.googleapis.com/InstanceOSPoliciesCompliance:\x02\x18\x01"\xa0\x01\n(ListInstanceOSPoliciesCompliancesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t:\x02\x18\x01"\xaf\x01\n)ListInstanceOSPoliciesCompliancesResponse\x12e\n instance_os_policies_compliances\x18\x01 \x03(\x0b2;.google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t:\x02\x18\x01B\xea\x01\n!com.google.cloud.osconfig.v1alphaB!InstanceOSPoliciesComplianceProtoP\x01Z=cloud.google.com/go/osconfig/apiv1alpha/osconfigpb;osconfigpb\xaa\x02\x1dGoogle.Cloud.OsConfig.V1Alpha\xca\x02\x1dGoogle\\Cloud\\OsConfig\\V1alpha\xea\x02 Google::Cloud::OsConfig::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1alpha.instance_os_policies_compliance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.osconfig.v1alphaB!InstanceOSPoliciesComplianceProtoP\x01Z=cloud.google.com/go/osconfig/apiv1alpha/osconfigpb;osconfigpb\xaa\x02\x1dGoogle.Cloud.OsConfig.V1Alpha\xca\x02\x1dGoogle\\Cloud\\OsConfig\\V1alpha\xea\x02 Google::Cloud::OsConfig::V1alpha'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE'].fields_by_name['os_policy_assignment']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE'].fields_by_name['os_policy_assignment']._serialized_options = b'\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE']._serialized_options = b'\x18\x01'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['instance']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['instance']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['detailed_state']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['detailed_state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['detailed_state_reason']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['detailed_state_reason']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['os_policy_compliances']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['os_policy_compliances']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['last_compliance_check_time']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['last_compliance_check_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['last_compliance_run_id']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE'].fields_by_name['last_compliance_run_id']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE']._loaded_options = None
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE']._serialized_options = b'\x18\x01\xeaA\x88\x01\n4osconfig.googleapis.com/InstanceOSPoliciesCompliance\x12Pprojects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}'
    _globals['_GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA6\n4osconfig.googleapis.com/InstanceOSPoliciesCompliance'
    _globals['_GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST']._loaded_options = None
    _globals['_GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST']._serialized_options = b'\x18\x01'
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST']._loaded_options = None
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST']._serialized_options = b'\x18\x01'
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESRESPONSE']._loaded_options = None
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE']._serialized_start = 247
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE']._serialized_end = 1125
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE']._serialized_start = 685
    _globals['_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE']._serialized_end = 980
    _globals['_GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST']._serialized_start = 1127
    _globals['_GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST']._serialized_end = 1247
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST']._serialized_start = 1250
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST']._serialized_end = 1410
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESRESPONSE']._serialized_start = 1413
    _globals['_LISTINSTANCEOSPOLICIESCOMPLIANCESRESPONSE']._serialized_end = 1588