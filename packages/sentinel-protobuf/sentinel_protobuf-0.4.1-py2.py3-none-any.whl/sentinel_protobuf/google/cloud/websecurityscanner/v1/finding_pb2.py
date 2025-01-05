"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1/finding.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.websecurityscanner.v1 import finding_addon_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1_dot_finding__addon__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/websecurityscanner/v1/finding.proto\x12"google.cloud.websecurityscanner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a6google/cloud/websecurityscanner/v1/finding_addon.proto"\xec\x07\n\x07Finding\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cfinding_type\x18\x02 \x01(\t\x12K\n\x08severity\x18\x11 \x01(\x0e24.google.cloud.websecurityscanner.v1.Finding.SeverityB\x03\xe0A\x03\x12\x13\n\x0bhttp_method\x18\x03 \x01(\t\x12\x12\n\nfuzzed_url\x18\x04 \x01(\t\x12\x0c\n\x04body\x18\x05 \x01(\t\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x18\n\x10reproduction_url\x18\x07 \x01(\t\x12\x11\n\tframe_url\x18\x08 \x01(\t\x12\x11\n\tfinal_url\x18\t \x01(\t\x12\x13\n\x0btracking_id\x18\n \x01(\t\x126\n\x04form\x18\x10 \x01(\x0b2(.google.cloud.websecurityscanner.v1.Form\x12M\n\x10outdated_library\x18\x0b \x01(\x0b23.google.cloud.websecurityscanner.v1.OutdatedLibrary\x12Q\n\x12violating_resource\x18\x0c \x01(\x0b25.google.cloud.websecurityscanner.v1.ViolatingResource\x12Q\n\x12vulnerable_headers\x18\x0f \x01(\x0b25.google.cloud.websecurityscanner.v1.VulnerableHeaders\x12W\n\x15vulnerable_parameters\x18\r \x01(\x0b28.google.cloud.websecurityscanner.v1.VulnerableParameters\x124\n\x03xss\x18\x0e \x01(\x0b2\'.google.cloud.websecurityscanner.v1.Xss\x129\n\x03xxe\x18\x12 \x01(\x0b2\'.google.cloud.websecurityscanner.v1.XxeB\x03\xe0A\x03"Q\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x07\n\x03LOW\x10\x04:\x84\x01\xeaA\x80\x01\n)websecurityscanner.googleapis.com/Finding\x12Sprojects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}/findings/{finding}B\x82\x02\n&com.google.cloud.websecurityscanner.v1B\x0cFindingProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1.finding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.websecurityscanner.v1B\x0cFindingProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1'
    _globals['_FINDING'].fields_by_name['severity']._loaded_options = None
    _globals['_FINDING'].fields_by_name['severity']._serialized_options = b'\xe0A\x03'
    _globals['_FINDING'].fields_by_name['xxe']._loaded_options = None
    _globals['_FINDING'].fields_by_name['xxe']._serialized_options = b'\xe0A\x03'
    _globals['_FINDING']._loaded_options = None
    _globals['_FINDING']._serialized_options = b'\xeaA\x80\x01\n)websecurityscanner.googleapis.com/Finding\x12Sprojects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}/findings/{finding}'
    _globals['_FINDING']._serialized_start = 205
    _globals['_FINDING']._serialized_end = 1209
    _globals['_FINDING_SEVERITY']._serialized_start = 993
    _globals['_FINDING_SEVERITY']._serialized_end = 1074