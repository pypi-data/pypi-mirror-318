"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1alpha/finding.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.websecurityscanner.v1alpha import finding_addon_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_finding__addon__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/websecurityscanner/v1alpha/finding.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a\x19google/api/resource.proto\x1a;google/cloud/websecurityscanner/v1alpha/finding_addon.proto"\xe9\x08\n\x07Finding\x12\x0c\n\x04name\x18\x01 \x01(\t\x12R\n\x0cfinding_type\x18\x02 \x01(\x0e2<.google.cloud.websecurityscanner.v1alpha.Finding.FindingType\x12\x13\n\x0bhttp_method\x18\x03 \x01(\t\x12\x12\n\nfuzzed_url\x18\x04 \x01(\t\x12\x0c\n\x04body\x18\x05 \x01(\t\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x18\n\x10reproduction_url\x18\x07 \x01(\t\x12\x11\n\tframe_url\x18\x08 \x01(\t\x12\x11\n\tfinal_url\x18\t \x01(\t\x12\x13\n\x0btracking_id\x18\n \x01(\t\x12R\n\x10outdated_library\x18\x0b \x01(\x0b28.google.cloud.websecurityscanner.v1alpha.OutdatedLibrary\x12V\n\x12violating_resource\x18\x0c \x01(\x0b2:.google.cloud.websecurityscanner.v1alpha.ViolatingResource\x12V\n\x12vulnerable_headers\x18\x0f \x01(\x0b2:.google.cloud.websecurityscanner.v1alpha.VulnerableHeaders\x12\\\n\x15vulnerable_parameters\x18\r \x01(\x0b2=.google.cloud.websecurityscanner.v1alpha.VulnerableParameters\x129\n\x03xss\x18\x0e \x01(\x0b2,.google.cloud.websecurityscanner.v1alpha.Xss"\xb6\x02\n\x0bFindingType\x12\x1c\n\x18FINDING_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rMIXED_CONTENT\x10\x01\x12\x14\n\x10OUTDATED_LIBRARY\x10\x02\x12\x11\n\rROSETTA_FLASH\x10\x05\x12\x10\n\x0cXSS_CALLBACK\x10\x03\x12\r\n\tXSS_ERROR\x10\x04\x12\x17\n\x13CLEAR_TEXT_PASSWORD\x10\x06\x12\x18\n\x14INVALID_CONTENT_TYPE\x10\x07\x12\x18\n\x14XSS_ANGULAR_CALLBACK\x10\x08\x12\x12\n\x0eINVALID_HEADER\x10\t\x12#\n\x1fMISSPELLED_SECURITY_HEADER_NAME\x10\n\x12&\n"MISMATCHING_SECURITY_HEADER_VALUES\x10\x0b:\x84\x01\xeaA\x80\x01\n)websecurityscanner.googleapis.com/Finding\x12Sprojects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}/findings/{finding}B\x9a\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x0cFindingProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1alpha.finding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.cloud.websecurityscanner.v1alphaB\x0cFindingProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpb'
    _globals['_FINDING']._loaded_options = None
    _globals['_FINDING']._serialized_options = b'\xeaA\x80\x01\n)websecurityscanner.googleapis.com/Finding\x12Sprojects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}/findings/{finding}'
    _globals['_FINDING']._serialized_start = 187
    _globals['_FINDING']._serialized_end = 1316
    _globals['_FINDING_FINDINGTYPE']._serialized_start = 871
    _globals['_FINDING_FINDINGTYPE']._serialized_end = 1181