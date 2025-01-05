"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/identitytoolkit/logging/request_log.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/identitytoolkit/logging/request_log.proto\x12$google.cloud.identitytoolkit.logging\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17google/rpc/status.proto"\xb2\x02\n\nRequestLog\x12\x13\n\x0bmethod_name\x18\x01 \x01(\t\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x12O\n\x10request_metadata\x18\x03 \x01(\x0b25.google.cloud.identitytoolkit.logging.RequestMetadata\x12(\n\x07request\x18\x04 \x01(\x0b2\x17.google.protobuf.Struct\x12)\n\x08response\x18\x05 \x01(\x0b2\x17.google.protobuf.Struct\x12\x1a\n\x12num_response_items\x18\x06 \x01(\x03\x12)\n\x08metadata\x18\x07 \x01(\x0b2\x17.google.protobuf.Struct"H\n\x0fRequestMetadata\x12\x11\n\tcaller_ip\x18\x01 \x01(\t\x12"\n\x1acaller_supplied_user_agent\x18\x02 \x01(\tB~\n(com.google.cloud.identitytoolkit.loggingB\x0fRequestLogProtoP\x01Z?cloud.google.com/go/identitytoolkit/logging/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.identitytoolkit.logging.request_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.cloud.identitytoolkit.loggingB\x0fRequestLogProtoP\x01Z?cloud.google.com/go/identitytoolkit/logging/loggingpb;loggingpb'
    _globals['_REQUESTLOG']._serialized_start = 152
    _globals['_REQUESTLOG']._serialized_end = 458
    _globals['_REQUESTMETADATA']._serialized_start = 460
    _globals['_REQUESTMETADATA']._serialized_end = 532