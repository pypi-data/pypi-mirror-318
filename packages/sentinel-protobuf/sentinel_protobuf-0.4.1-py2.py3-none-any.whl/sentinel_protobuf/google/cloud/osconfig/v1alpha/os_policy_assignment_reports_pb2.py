"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1alpha/os_policy_assignment_reports.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/osconfig/v1alpha/os_policy_assignment_reports.proto\x12\x1dgoogle.cloud.osconfig.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"l\n"GetOSPolicyAssignmentReportRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0osconfig.googleapis.com/OSPolicyAssignmentReport"\xa8\x01\n$ListOSPolicyAssignmentReportsRequest\x12I\n\x06parent\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1compute.googleapis.com/InstanceOSPolicyAssignment\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x12\n\npage_token\x18\x04 \x01(\t"\x9f\x01\n%ListOSPolicyAssignmentReportsResponse\x12]\n\x1cos_policy_assignment_reports\x18\x01 \x03(\x0b27.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xf1\x0e\n\x18OSPolicyAssignmentReport\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12M\n\x14os_policy_assignment\x18\x03 \x01(\tB/\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment\x12i\n\x15os_policy_compliances\x18\x04 \x03(\x0b2J.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport.OSPolicyCompliance\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x0blast_run_id\x18\x06 \x01(\t\x1a\x95\x0b\n\x12OSPolicyCompliance\x12\x14\n\x0cos_policy_id\x18\x01 \x01(\t\x12t\n\x10compliance_state\x18\x02 \x01(\x0e2Z.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport.OSPolicyCompliance.ComplianceState\x12\x1f\n\x17compliance_state_reason\x18\x03 \x01(\t\x12\x8d\x01\n\x1eos_policy_resource_compliances\x18\x04 \x03(\x0b2e.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance\x1a\xff\x07\n\x1aOSPolicyResourceCompliance\x12\x1d\n\x15os_policy_resource_id\x18\x01 \x01(\t\x12\x97\x01\n\x0cconfig_steps\x18\x02 \x03(\x0b2\x80\x01.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep\x12\x8f\x01\n\x10compliance_state\x18\x03 \x01(\x0e2u.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ComplianceState\x12\x1f\n\x17compliance_state_reason\x18\x04 \x01(\t\x12\x98\x01\n\x14exec_resource_output\x18\x05 \x01(\x0b2x.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.ExecResourceOutputH\x00\x1a\xdb\x02\n\x1aOSPolicyResourceConfigStep\x12\x94\x01\n\x04type\x18\x01 \x01(\x0e2\x85\x01.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport.OSPolicyCompliance.OSPolicyResourceCompliance.OSPolicyResourceConfigStep.Type\x12\x15\n\rerror_message\x18\x02 \x01(\t"\x8e\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nVALIDATION\x10\x01\x12\x17\n\x13DESIRED_STATE_CHECK\x10\x02\x12\x1d\n\x19DESIRED_STATE_ENFORCEMENT\x10\x03\x12(\n$DESIRED_STATE_CHECK_POST_ENFORCEMENT\x10\x04\x1a0\n\x12ExecResourceOutput\x12\x1a\n\x12enforcement_output\x18\x02 \x01(\x0c"@\n\x0fComplianceState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tCOMPLIANT\x10\x01\x12\x11\n\rNON_COMPLIANT\x10\x02B\x08\n\x06output"@\n\x0fComplianceState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tCOMPLIANT\x10\x01\x12\x11\n\rNON_COMPLIANT\x10\x02:\x9c\x01\xeaA\x98\x01\n0osconfig.googleapis.com/OSPolicyAssignmentReport\x12dprojects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reportB\xfd\x02\n!com.google.cloud.osconfig.v1alphaB\x1eOSPolicyAssignmentReportsProtoP\x01Z=cloud.google.com/go/osconfig/apiv1alpha/osconfigpb;osconfigpb\xaa\x02\x1dGoogle.Cloud.OsConfig.V1Alpha\xca\x02\x1dGoogle\\Cloud\\OsConfig\\V1alpha\xea\x02 Google::Cloud::OsConfig::V1alpha\xeaA\x92\x01\n1compute.googleapis.com/InstanceOSPolicyAssignment\x12]projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1alpha.os_policy_assignment_reports_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.osconfig.v1alphaB\x1eOSPolicyAssignmentReportsProtoP\x01Z=cloud.google.com/go/osconfig/apiv1alpha/osconfigpb;osconfigpb\xaa\x02\x1dGoogle.Cloud.OsConfig.V1Alpha\xca\x02\x1dGoogle\\Cloud\\OsConfig\\V1alpha\xea\x02 Google::Cloud::OsConfig::V1alpha\xeaA\x92\x01\n1compute.googleapis.com/InstanceOSPolicyAssignment\x12]projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}'
    _globals['_GETOSPOLICYASSIGNMENTREPORTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETOSPOLICYASSIGNMENTREPORTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0osconfig.googleapis.com/OSPolicyAssignmentReport'
    _globals['_LISTOSPOLICYASSIGNMENTREPORTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTOSPOLICYASSIGNMENTREPORTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA3\n1compute.googleapis.com/InstanceOSPolicyAssignment'
    _globals['_OSPOLICYASSIGNMENTREPORT'].fields_by_name['os_policy_assignment']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENTREPORT'].fields_by_name['os_policy_assignment']._serialized_options = b'\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment'
    _globals['_OSPOLICYASSIGNMENTREPORT']._loaded_options = None
    _globals['_OSPOLICYASSIGNMENTREPORT']._serialized_options = b'\xeaA\x98\x01\n0osconfig.googleapis.com/OSPolicyAssignmentReport\x12dprojects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report'
    _globals['_GETOSPOLICYASSIGNMENTREPORTREQUEST']._serialized_start = 192
    _globals['_GETOSPOLICYASSIGNMENTREPORTREQUEST']._serialized_end = 300
    _globals['_LISTOSPOLICYASSIGNMENTREPORTSREQUEST']._serialized_start = 303
    _globals['_LISTOSPOLICYASSIGNMENTREPORTSREQUEST']._serialized_end = 471
    _globals['_LISTOSPOLICYASSIGNMENTREPORTSRESPONSE']._serialized_start = 474
    _globals['_LISTOSPOLICYASSIGNMENTREPORTSRESPONSE']._serialized_end = 633
    _globals['_OSPOLICYASSIGNMENTREPORT']._serialized_start = 636
    _globals['_OSPOLICYASSIGNMENTREPORT']._serialized_end = 2541
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE']._serialized_start = 953
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE']._serialized_end = 2382
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE']._serialized_start = 1293
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE']._serialized_end = 2316
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE_OSPOLICYRESOURCECONFIGSTEP']._serialized_start = 1843
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE_OSPOLICYRESOURCECONFIGSTEP']._serialized_end = 2190
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE_OSPOLICYRESOURCECONFIGSTEP_TYPE']._serialized_start = 2048
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE_OSPOLICYRESOURCECONFIGSTEP_TYPE']._serialized_end = 2190
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE_EXECRESOURCEOUTPUT']._serialized_start = 2192
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE_EXECRESOURCEOUTPUT']._serialized_end = 2240
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE_COMPLIANCESTATE']._serialized_start = 2242
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_OSPOLICYRESOURCECOMPLIANCE_COMPLIANCESTATE']._serialized_end = 2306
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_COMPLIANCESTATE']._serialized_start = 2242
    _globals['_OSPOLICYASSIGNMENTREPORT_OSPOLICYCOMPLIANCE_COMPLIANCESTATE']._serialized_end = 2306