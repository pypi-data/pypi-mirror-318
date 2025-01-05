"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/healthcare/logging/annotation.proto')
_sym_db = _symbol_database.Default()
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/healthcare/logging/annotation.proto\x12\x1fgoogle.cloud.healthcare.logging\x1a\x17google/rpc/status.proto"M\n\x18ImportAnnotationLogEntry\x12\x0e\n\x06source\x18\x01 \x01(\t\x12!\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"k\n\x18ExportAnnotationLogEntry\x12\x13\n\x0bdestination\x18\x01 \x01(\t\x12\x17\n\x0fannotation_name\x18\x02 \x01(\t\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.Status"\x92\x01\n\x1aEvaluateAnnotationLogEntry\x12\x13\n\x0bdestination\x18\x01 \x01(\t\x12\x1c\n\x14eval_annotation_name\x18\x02 \x01(\t\x12\x1e\n\x16golden_annotation_name\x18\x03 \x01(\t\x12!\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.StatusBa\n#com.google.cloud.healthcare.loggingZ:cloud.google.com/go/healthcare/logging/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.healthcare.logging.annotation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.healthcare.loggingZ:cloud.google.com/go/healthcare/logging/loggingpb;loggingpb'
    _globals['_IMPORTANNOTATIONLOGENTRY']._serialized_start = 110
    _globals['_IMPORTANNOTATIONLOGENTRY']._serialized_end = 187
    _globals['_EXPORTANNOTATIONLOGENTRY']._serialized_start = 189
    _globals['_EXPORTANNOTATIONLOGENTRY']._serialized_end = 296
    _globals['_EVALUATEANNOTATIONLOGENTRY']._serialized_start = 299
    _globals['_EVALUATEANNOTATIONLOGENTRY']._serialized_end = 445