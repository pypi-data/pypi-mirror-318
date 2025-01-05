"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/type/date_range.proto')
_sym_db = _symbol_database.Default()
from ....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/actions/type/date_range.proto\x12\x13google.actions.type\x1a\x16google/type/date.proto"M\n\tDateRange\x12 \n\x05start\x18\x01 \x01(\x0b2\x11.google.type.Date\x12\x1e\n\x03end\x18\x02 \x01(\x0b2\x11.google.type.DateBu\n\x17com.google.actions.typeB\x0eDateRangeProtoP\x01Z@google.golang.org/genproto/googleapis/type/date_range;date_range\xa2\x02\x05AOGTPb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.type.date_range_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.actions.typeB\x0eDateRangeProtoP\x01Z@google.golang.org/genproto/googleapis/type/date_range;date_range\xa2\x02\x05AOGTP'
    _globals['_DATERANGE']._serialized_start = 85
    _globals['_DATERANGE']._serialized_end = 162