"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/cloudcontrolspartner/v1/violations.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/cloudcontrolspartner/v1/violations.proto\x12$google.cloud.cloudcontrolspartner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/interval.proto"\xa1\r\n\tViolation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x03\x123\n\nbegin_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x125\n\x0cresolve_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x15\n\x08category\x18\x06 \x01(\tB\x03\xe0A\x03\x12I\n\x05state\x18\x07 \x01(\x0e25.google.cloud.cloudcontrolspartner.v1.Violation.StateB\x03\xe0A\x03\x12(\n\x18non_compliant_org_policy\x18\x08 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x11\n\tfolder_id\x18\t \x01(\x03\x12U\n\x0bremediation\x18\r \x01(\x0b2;.google.cloud.cloudcontrolspartner.v1.Violation.RemediationB\x03\xe0A\x03\x1a\xc0\x07\n\x0bRemediation\x12c\n\x0cinstructions\x18\x01 \x01(\x0b2H.google.cloud.cloudcontrolspartner.v1.Violation.Remediation.InstructionsB\x03\xe0A\x02\x12\x18\n\x10compliant_values\x18\x02 \x03(\t\x12j\n\x10remediation_type\x18\x03 \x01(\x0e2K.google.cloud.cloudcontrolspartner.v1.Violation.Remediation.RemediationTypeB\x03\xe0A\x03\x1a\x82\x03\n\x0cInstructions\x12l\n\x13gcloud_instructions\x18\x01 \x01(\x0b2O.google.cloud.cloudcontrolspartner.v1.Violation.Remediation.Instructions.Gcloud\x12n\n\x14console_instructions\x18\x02 \x01(\x0b2P.google.cloud.cloudcontrolspartner.v1.Violation.Remediation.Instructions.Console\x1aJ\n\x06Gcloud\x12\x17\n\x0fgcloud_commands\x18\x01 \x03(\t\x12\r\n\x05steps\x18\x02 \x03(\t\x12\x18\n\x10additional_links\x18\x03 \x03(\t\x1aH\n\x07Console\x12\x14\n\x0cconsole_uris\x18\x01 \x03(\t\x12\r\n\x05steps\x18\x02 \x03(\t\x12\x18\n\x10additional_links\x18\x03 \x03(\t"\xc0\x02\n\x0fRemediationType\x12 \n\x1cREMEDIATION_TYPE_UNSPECIFIED\x10\x00\x12,\n(REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION\x10\x01\x128\n4REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION\x10\x02\x127\n3REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION\x10\x03\x12F\nBREMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION\x10\x04\x12"\n\x1eREMEDIATION_RESOURCE_VIOLATION\x10\x05"K\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08RESOLVED\x10\x01\x12\x0e\n\nUNRESOLVED\x10\x02\x12\r\n\tEXCEPTION\x10\x03:\xbe\x01\xeaA\xba\x01\n-cloudcontrolspartner.googleapis.com/Violation\x12rorganizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/violations/{violation}*\nviolations2\tviolation"\xe9\x01\n\x15ListViolationsRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-cloudcontrolspartner.googleapis.com/Violation\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12,\n\x08interval\x18\x06 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x01"\x8b\x01\n\x16ListViolationsResponse\x12C\n\nviolations\x18\x01 \x03(\x0b2/.google.cloud.cloudcontrolspartner.v1.Violation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"Z\n\x13GetViolationRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-cloudcontrolspartner.googleapis.com/ViolationB\x93\x02\n(com.google.cloud.cloudcontrolspartner.v1B\x0fViolationsProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02\'Google::Cloud::CloudControlsPartner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudcontrolspartner.v1.violations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.cloudcontrolspartner.v1B\x0fViolationsProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02'Google::Cloud::CloudControlsPartner::V1"
    _globals['_VIOLATION_REMEDIATION'].fields_by_name['instructions']._loaded_options = None
    _globals['_VIOLATION_REMEDIATION'].fields_by_name['instructions']._serialized_options = b'\xe0A\x02'
    _globals['_VIOLATION_REMEDIATION'].fields_by_name['remediation_type']._loaded_options = None
    _globals['_VIOLATION_REMEDIATION'].fields_by_name['remediation_type']._serialized_options = b'\xe0A\x03'
    _globals['_VIOLATION'].fields_by_name['name']._loaded_options = None
    _globals['_VIOLATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_VIOLATION'].fields_by_name['description']._loaded_options = None
    _globals['_VIOLATION'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_VIOLATION'].fields_by_name['begin_time']._loaded_options = None
    _globals['_VIOLATION'].fields_by_name['begin_time']._serialized_options = b'\xe0A\x03'
    _globals['_VIOLATION'].fields_by_name['update_time']._loaded_options = None
    _globals['_VIOLATION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_VIOLATION'].fields_by_name['resolve_time']._loaded_options = None
    _globals['_VIOLATION'].fields_by_name['resolve_time']._serialized_options = b'\xe0A\x03'
    _globals['_VIOLATION'].fields_by_name['category']._loaded_options = None
    _globals['_VIOLATION'].fields_by_name['category']._serialized_options = b'\xe0A\x03'
    _globals['_VIOLATION'].fields_by_name['state']._loaded_options = None
    _globals['_VIOLATION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_VIOLATION'].fields_by_name['non_compliant_org_policy']._loaded_options = None
    _globals['_VIOLATION'].fields_by_name['non_compliant_org_policy']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_VIOLATION'].fields_by_name['remediation']._loaded_options = None
    _globals['_VIOLATION'].fields_by_name['remediation']._serialized_options = b'\xe0A\x03'
    _globals['_VIOLATION']._loaded_options = None
    _globals['_VIOLATION']._serialized_options = b'\xeaA\xba\x01\n-cloudcontrolspartner.googleapis.com/Violation\x12rorganizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/violations/{violation}*\nviolations2\tviolation'
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-cloudcontrolspartner.googleapis.com/Violation'
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['interval']._loaded_options = None
    _globals['_LISTVIOLATIONSREQUEST'].fields_by_name['interval']._serialized_options = b'\xe0A\x01'
    _globals['_GETVIOLATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETVIOLATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-cloudcontrolspartner.googleapis.com/Violation'
    _globals['_VIOLATION']._serialized_start = 217
    _globals['_VIOLATION']._serialized_end = 1914
    _globals['_VIOLATION_REMEDIATION']._serialized_start = 684
    _globals['_VIOLATION_REMEDIATION']._serialized_end = 1644
    _globals['_VIOLATION_REMEDIATION_INSTRUCTIONS']._serialized_start = 935
    _globals['_VIOLATION_REMEDIATION_INSTRUCTIONS']._serialized_end = 1321
    _globals['_VIOLATION_REMEDIATION_INSTRUCTIONS_GCLOUD']._serialized_start = 1173
    _globals['_VIOLATION_REMEDIATION_INSTRUCTIONS_GCLOUD']._serialized_end = 1247
    _globals['_VIOLATION_REMEDIATION_INSTRUCTIONS_CONSOLE']._serialized_start = 1249
    _globals['_VIOLATION_REMEDIATION_INSTRUCTIONS_CONSOLE']._serialized_end = 1321
    _globals['_VIOLATION_REMEDIATION_REMEDIATIONTYPE']._serialized_start = 1324
    _globals['_VIOLATION_REMEDIATION_REMEDIATIONTYPE']._serialized_end = 1644
    _globals['_VIOLATION_STATE']._serialized_start = 1646
    _globals['_VIOLATION_STATE']._serialized_end = 1721
    _globals['_LISTVIOLATIONSREQUEST']._serialized_start = 1917
    _globals['_LISTVIOLATIONSREQUEST']._serialized_end = 2150
    _globals['_LISTVIOLATIONSRESPONSE']._serialized_start = 2153
    _globals['_LISTVIOLATIONSRESPONSE']._serialized_end = 2292
    _globals['_GETVIOLATIONREQUEST']._serialized_start = 2294
    _globals['_GETVIOLATIONREQUEST']._serialized_end = 2384