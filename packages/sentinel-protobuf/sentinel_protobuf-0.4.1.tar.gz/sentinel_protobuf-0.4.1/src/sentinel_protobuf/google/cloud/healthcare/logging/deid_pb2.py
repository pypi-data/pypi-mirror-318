"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/healthcare/logging/deid.proto')
_sym_db = _symbol_database.Default()
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/healthcare/logging/deid.proto\x12\x1fgoogle.cloud.healthcare.logging\x1a\x17google/rpc/status.proto"N\n\x12DeidentifyLogEntry\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12!\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusBa\n#com.google.cloud.healthcare.loggingZ:cloud.google.com/go/healthcare/logging/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.healthcare.logging.deid_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.healthcare.loggingZ:cloud.google.com/go/healthcare/logging/loggingpb;loggingpb'
    _globals['_DEIDENTIFYLOGENTRY']._serialized_start = 104
    _globals['_DEIDENTIFYLOGENTRY']._serialized_end = 182