"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/metastore/logging/v1/log_streams.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/metastore/logging/v1/log_streams.proto\x12!google.cloud.metastore.logging.v1"#\n\x10RequestsLogEntry\x12\x0f\n\x07message\x18\x01 \x01(\t")\n\x16SystemActivityLogEntry\x12\x0f\n\x07message\x18\x01 \x01(\tBw\n!google.cloud.metastore.logging.v1B\x0fLogStreamsProtoP\x01Z?cloud.google.com/go/metastore/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.metastore.logging.v1.log_streams_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!google.cloud.metastore.logging.v1B\x0fLogStreamsProtoP\x01Z?cloud.google.com/go/metastore/logging/apiv1/loggingpb;loggingpb'
    _globals['_REQUESTSLOGENTRY']._serialized_start = 90
    _globals['_REQUESTSLOGENTRY']._serialized_end = 125
    _globals['_SYSTEMACTIVITYLOGENTRY']._serialized_start = 127
    _globals['_SYSTEMACTIVITYLOGENTRY']._serialized_end = 168