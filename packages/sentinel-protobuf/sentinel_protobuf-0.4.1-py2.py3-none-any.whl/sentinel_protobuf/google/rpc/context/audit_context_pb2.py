"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/rpc/context/audit_context.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/rpc/context/audit_context.proto\x12\x12google.rpc.context\x1a\x1cgoogle/protobuf/struct.proto"\xc7\x01\n\x0cAuditContext\x12\x11\n\taudit_log\x18\x01 \x01(\x0c\x121\n\x10scrubbed_request\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x122\n\x11scrubbed_response\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct\x12$\n\x1cscrubbed_response_item_count\x18\x04 \x01(\x05\x12\x17\n\x0ftarget_resource\x18\x05 \x01(\tBh\n\x16com.google.rpc.contextB\x11AuditContextProtoP\x01Z9google.golang.org/genproto/googleapis/rpc/context;contextb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.rpc.context.audit_context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.rpc.contextB\x11AuditContextProtoP\x01Z9google.golang.org/genproto/googleapis/rpc/context;context'
    _globals['_AUDITCONTEXT']._serialized_start = 93
    _globals['_AUDITCONTEXT']._serialized_end = 292