"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/clouderrorreporting/v1beta1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/devtools/clouderrorreporting/v1beta1/common.proto\x12+google.devtools.clouderrorreporting.v1beta1\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb2\x02\n\nErrorGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12S\n\x0ftracking_issues\x18\x03 \x03(\x0b2:.google.devtools.clouderrorreporting.v1beta1.TrackingIssue\x12X\n\x11resolution_status\x18\x05 \x01(\x0e2=.google.devtools.clouderrorreporting.v1beta1.ResolutionStatus:U\xeaAR\n-clouderrorreporting.googleapis.com/ErrorGroup\x12!projects/{project}/groups/{group}"\x1c\n\rTrackingIssue\x12\x0b\n\x03url\x18\x01 \x01(\t"\xef\x01\n\nErrorEvent\x12.\n\nevent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12T\n\x0fservice_context\x18\x02 \x01(\x0b2;.google.devtools.clouderrorreporting.v1beta1.ServiceContext\x12\x0f\n\x07message\x18\x03 \x01(\t\x12J\n\x07context\x18\x05 \x01(\x0b29.google.devtools.clouderrorreporting.v1beta1.ErrorContext"I\n\x0eServiceContext\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x15\n\rresource_type\x18\x04 \x01(\t"\xc9\x01\n\x0cErrorContext\x12U\n\x0chttp_request\x18\x01 \x01(\x0b2?.google.devtools.clouderrorreporting.v1beta1.HttpRequestContext\x12\x0c\n\x04user\x18\x02 \x01(\t\x12T\n\x0freport_location\x18\x03 \x01(\x0b2;.google.devtools.clouderrorreporting.v1beta1.SourceLocation"\x88\x01\n\x12HttpRequestContext\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x12\n\nuser_agent\x18\x03 \x01(\t\x12\x10\n\x08referrer\x18\x04 \x01(\t\x12\x1c\n\x14response_status_code\x18\x05 \x01(\x05\x12\x11\n\tremote_ip\x18\x06 \x01(\t"O\n\x0eSourceLocation\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x13\n\x0bline_number\x18\x02 \x01(\x05\x12\x15\n\rfunction_name\x18\x04 \x01(\t*j\n\x10ResolutionStatus\x12!\n\x1dRESOLUTION_STATUS_UNSPECIFIED\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\x10\n\x0cACKNOWLEDGED\x10\x02\x12\x0c\n\x08RESOLVED\x10\x03\x12\t\n\x05MUTED\x10\x04B\x89\x02\n/com.google.devtools.clouderrorreporting.v1beta1B\x0bCommonProtoP\x01ZOcloud.google.com/go/errorreporting/apiv1beta1/errorreportingpb;errorreportingpb\xf8\x01\x01\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1\xea\x02&Google::Cloud::ErrorReporting::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.clouderrorreporting.v1beta1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.devtools.clouderrorreporting.v1beta1B\x0bCommonProtoP\x01ZOcloud.google.com/go/errorreporting/apiv1beta1/errorreportingpb;errorreportingpb\xf8\x01\x01\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1\xea\x02&Google::Cloud::ErrorReporting::V1beta1'
    _globals['_ERRORGROUP']._loaded_options = None
    _globals['_ERRORGROUP']._serialized_options = b'\xeaAR\n-clouderrorreporting.googleapis.com/ErrorGroup\x12!projects/{project}/groups/{group}'
    _globals['_RESOLUTIONSTATUS']._serialized_start = 1245
    _globals['_RESOLUTIONSTATUS']._serialized_end = 1351
    _globals['_ERRORGROUP']._serialized_start = 166
    _globals['_ERRORGROUP']._serialized_end = 472
    _globals['_TRACKINGISSUE']._serialized_start = 474
    _globals['_TRACKINGISSUE']._serialized_end = 502
    _globals['_ERROREVENT']._serialized_start = 505
    _globals['_ERROREVENT']._serialized_end = 744
    _globals['_SERVICECONTEXT']._serialized_start = 746
    _globals['_SERVICECONTEXT']._serialized_end = 819
    _globals['_ERRORCONTEXT']._serialized_start = 822
    _globals['_ERRORCONTEXT']._serialized_end = 1023
    _globals['_HTTPREQUESTCONTEXT']._serialized_start = 1026
    _globals['_HTTPREQUESTCONTEXT']._serialized_end = 1162
    _globals['_SOURCELOCATION']._serialized_start = 1164
    _globals['_SOURCELOCATION']._serialized_end = 1243