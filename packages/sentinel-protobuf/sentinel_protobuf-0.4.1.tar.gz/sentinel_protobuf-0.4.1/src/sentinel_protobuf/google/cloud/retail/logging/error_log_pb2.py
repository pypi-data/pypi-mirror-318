"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/logging/error_log.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/retail/logging/error_log.proto\x12\x1bgoogle.cloud.retail.logging\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17google/rpc/status.proto"!\n\x0eServiceContext\x12\x0f\n\x07service\x18\x01 \x01(\t"2\n\x12HttpRequestContext\x12\x1c\n\x14response_status_code\x18\x01 \x01(\x05"\'\n\x0eSourceLocation\x12\x15\n\rfunction_name\x18\x01 \x01(\t"\x9b\x01\n\x0cErrorContext\x12E\n\x0chttp_request\x18\x01 \x01(\x0b2/.google.cloud.retail.logging.HttpRequestContext\x12D\n\x0freport_location\x18\x02 \x01(\x0b2+.google.cloud.retail.logging.SourceLocation"\xa4\x01\n\x12ImportErrorContext\x12\x16\n\x0eoperation_name\x18\x01 \x01(\t\x12\x10\n\x08gcs_path\x18\x02 \x01(\t\x12\x13\n\x0bline_number\x18\x03 \x01(\t\x12\x16\n\x0ccatalog_item\x18\x04 \x01(\tH\x00\x12\x11\n\x07product\x18\x05 \x01(\tH\x00\x12\x14\n\nuser_event\x18\x06 \x01(\tH\x00B\x0e\n\x0cline_content"\xef\x02\n\x08ErrorLog\x12D\n\x0fservice_context\x18\x01 \x01(\x0b2+.google.cloud.retail.logging.ServiceContext\x12:\n\x07context\x18\x02 \x01(\x0b2).google.cloud.retail.logging.ErrorContext\x12\x0f\n\x07message\x18\x03 \x01(\t\x12"\n\x06status\x18\x04 \x01(\x0b2\x12.google.rpc.Status\x120\n\x0frequest_payload\x18\x05 \x01(\x0b2\x17.google.protobuf.Struct\x121\n\x10response_payload\x18\x06 \x01(\x0b2\x17.google.protobuf.Struct\x12G\n\x0eimport_payload\x18\x07 \x01(\x0b2/.google.cloud.retail.logging.ImportErrorContextB\xd0\x01\n\x1fcom.google.cloud.retail.loggingB\rErrorLogProtoP\x01Z6cloud.google.com/go/retail/logging/loggingpb;loggingpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.Logging\xca\x02\x1bGoogle\\Cloud\\Retail\\Logging\xea\x02\x1eGoogle::Cloud::Retail::Loggingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.logging.error_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.loggingB\rErrorLogProtoP\x01Z6cloud.google.com/go/retail/logging/loggingpb;loggingpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.Logging\xca\x02\x1bGoogle\\Cloud\\Retail\\Logging\xea\x02\x1eGoogle::Cloud::Retail::Logging'
    _globals['_SERVICECONTEXT']._serialized_start = 131
    _globals['_SERVICECONTEXT']._serialized_end = 164
    _globals['_HTTPREQUESTCONTEXT']._serialized_start = 166
    _globals['_HTTPREQUESTCONTEXT']._serialized_end = 216
    _globals['_SOURCELOCATION']._serialized_start = 218
    _globals['_SOURCELOCATION']._serialized_end = 257
    _globals['_ERRORCONTEXT']._serialized_start = 260
    _globals['_ERRORCONTEXT']._serialized_end = 415
    _globals['_IMPORTERRORCONTEXT']._serialized_start = 418
    _globals['_IMPORTERRORCONTEXT']._serialized_end = 582
    _globals['_ERRORLOG']._serialized_start = 585
    _globals['_ERRORLOG']._serialized_end = 952