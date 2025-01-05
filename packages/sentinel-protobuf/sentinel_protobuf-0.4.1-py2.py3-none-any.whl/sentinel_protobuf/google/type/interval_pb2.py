"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/type/interval.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1agoogle/type/interval.proto\x12\x0bgoogle.type\x1a\x1fgoogle/protobuf/timestamp.proto"h\n\x08Interval\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampBi\n\x0fcom.google.typeB\rIntervalProtoP\x01Z<google.golang.org/genproto/googleapis/type/interval;interval\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.type.interval_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0fcom.google.typeB\rIntervalProtoP\x01Z<google.golang.org/genproto/googleapis/type/interval;interval\xf8\x01\x01\xa2\x02\x03GTP'
    _globals['_INTERVAL']._serialized_start = 76
    _globals['_INTERVAL']._serialized_end = 180