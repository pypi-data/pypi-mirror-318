"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gsuiteaddons/logging/v1/g_suite_add_ons_log_entry.proto')
_sym_db = _symbol_database.Default()
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/cloud/gsuiteaddons/logging/v1/g_suite_add_ons_log_entry.proto\x12$google.cloud.gsuiteaddons.logging.v1\x1a\x17google/rpc/status.proto"j\n\x14GSuiteAddOnsLogEntry\x12\x12\n\ndeployment\x18\x01 \x01(\t\x12!\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x12\x1b\n\x13deployment_function\x18\x03 \x01(\tB\x84\x02\n(com.google.cloud.gsuiteaddons.logging.v1B\x19GSuiteAddOnsLogEntryProtoP\x01ZBcloud.google.com/go/gsuiteaddons/logging/apiv1/loggingpb;loggingpb\xaa\x02$Google.Cloud.GSuiteAddOns.Logging.V1\xca\x02$Google\\Cloud\\GSuiteAddOns\\Logging\\V1\xea\x02(Google::Cloud::GSuiteAddOns::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gsuiteaddons.logging.v1.g_suite_add_ons_log_entry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.cloud.gsuiteaddons.logging.v1B\x19GSuiteAddOnsLogEntryProtoP\x01ZBcloud.google.com/go/gsuiteaddons/logging/apiv1/loggingpb;loggingpb\xaa\x02$Google.Cloud.GSuiteAddOns.Logging.V1\xca\x02$Google\\Cloud\\GSuiteAddOns\\Logging\\V1\xea\x02(Google::Cloud::GSuiteAddOns::Logging::V1'
    _globals['_GSUITEADDONSLOGENTRY']._serialized_start = 135
    _globals['_GSUITEADDONSLOGENTRY']._serialized_end = 241