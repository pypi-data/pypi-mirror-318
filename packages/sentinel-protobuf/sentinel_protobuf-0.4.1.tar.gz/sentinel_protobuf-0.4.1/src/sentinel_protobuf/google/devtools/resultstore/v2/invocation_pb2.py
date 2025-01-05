"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/invocation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
from .....google.devtools.resultstore.v2 import coverage_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_coverage__pb2
from .....google.devtools.resultstore.v2 import coverage_summary_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_coverage__summary__pb2
from .....google.devtools.resultstore.v2 import file_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2
from .....google.devtools.resultstore.v2 import file_processing_error_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__processing__error__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/devtools/resultstore/v2/invocation.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/common.proto\x1a-google/devtools/resultstore/v2/coverage.proto\x1a5google/devtools/resultstore/v2/coverage_summary.proto\x1a)google/devtools/resultstore/v2/file.proto\x1a:google/devtools/resultstore/v2/file_processing_error.proto"\xc6\x06\n\nInvocation\x12\x0c\n\x04name\x18\x01 \x01(\t\x129\n\x02id\x18\x02 \x01(\x0b2-.google.devtools.resultstore.v2.Invocation.Id\x12K\n\x11status_attributes\x18\x03 \x01(\x0b20.google.devtools.resultstore.v2.StatusAttributes\x126\n\x06timing\x18\x04 \x01(\x0b2&.google.devtools.resultstore.v2.Timing\x12S\n\x15invocation_attributes\x18\x05 \x01(\x0b24.google.devtools.resultstore.v2.InvocationAttributes\x12E\n\x0eworkspace_info\x18\x06 \x01(\x0b2-.google.devtools.resultstore.v2.WorkspaceInfo\x12<\n\nproperties\x18\x07 \x03(\x0b2(.google.devtools.resultstore.v2.Property\x123\n\x05files\x18\x08 \x03(\x0b2$.google.devtools.resultstore.v2.File\x12S\n\x12coverage_summaries\x18\t \x03(\x0b27.google.devtools.resultstore.v2.LanguageCoverageSummary\x12M\n\x12aggregate_coverage\x18\n \x01(\x0b21.google.devtools.resultstore.v2.AggregateCoverage\x12T\n\x16file_processing_errors\x18\x0b \x03(\x0b24.google.devtools.resultstore.v2.FileProcessingErrors\x1a\x1b\n\x02Id\x12\x15\n\rinvocation_id\x18\x01 \x01(\t:D\xeaAA\n%resultstore.googleapis.com/Invocation\x12\x18invocations/{invocation}"\x12\n\x10WorkspaceContext"\xdf\x01\n\rWorkspaceInfo\x12K\n\x11workspace_context\x18\x01 \x01(\x0b20.google.devtools.resultstore.v2.WorkspaceContext\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\x19\n\x11working_directory\x18\x04 \x01(\t\x12\x10\n\x08tool_tag\x18\x05 \x01(\t\x12B\n\rcommand_lines\x18\x07 \x03(\x0b2+.google.devtools.resultstore.v2.CommandLine"I\n\x0bCommandLine\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0c\n\x04tool\x18\x02 \x01(\t\x12\x0c\n\x04args\x18\x03 \x03(\t\x12\x0f\n\x07command\x18\x04 \x01(\t"\xc6\x01\n\x14InvocationAttributes\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x05\x12\r\n\x05users\x18\x02 \x03(\t\x12\x0e\n\x06labels\x18\x03 \x03(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12N\n\x13invocation_contexts\x18\x06 \x03(\x0b21.google.devtools.resultstore.v2.InvocationContext\x12\x11\n\texit_code\x18\x07 \x01(\x05"6\n\x11InvocationContext\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\tB\x82\x01\n"com.google.devtools.resultstore.v2B\x0fInvocationProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.invocation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x0fInvocationProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_INVOCATION']._loaded_options = None
    _globals['_INVOCATION']._serialized_options = b'\xeaAA\n%resultstore.googleapis.com/Invocation\x12\x18invocations/{invocation}'
    _globals['_INVOCATIONATTRIBUTES'].fields_by_name['project_id']._loaded_options = None
    _globals['_INVOCATIONATTRIBUTES'].fields_by_name['project_id']._serialized_options = b'\xe0A\x05'
    _globals['_INVOCATION']._serialized_start = 394
    _globals['_INVOCATION']._serialized_end = 1232
    _globals['_INVOCATION_ID']._serialized_start = 1135
    _globals['_INVOCATION_ID']._serialized_end = 1162
    _globals['_WORKSPACECONTEXT']._serialized_start = 1234
    _globals['_WORKSPACECONTEXT']._serialized_end = 1252
    _globals['_WORKSPACEINFO']._serialized_start = 1255
    _globals['_WORKSPACEINFO']._serialized_end = 1478
    _globals['_COMMANDLINE']._serialized_start = 1480
    _globals['_COMMANDLINE']._serialized_end = 1553
    _globals['_INVOCATIONATTRIBUTES']._serialized_start = 1556
    _globals['_INVOCATIONATTRIBUTES']._serialized_end = 1754
    _globals['_INVOCATIONCONTEXT']._serialized_start = 1756
    _globals['_INVOCATIONCONTEXT']._serialized_end = 1810