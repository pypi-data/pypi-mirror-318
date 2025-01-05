"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/activity/v2/common.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/apps/drive/activity/v2/common.proto\x12\x1dgoogle.apps.drive.activity.v2\x1a\x1fgoogle/protobuf/timestamp.proto"i\n\tTimeRange\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"%\n\x05Group\x12\r\n\x05email\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t")\n\x06Domain\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tlegacy_id\x18\x03 \x01(\tB\xc0\x01\n!com.google.apps.drive.activity.v2B\x0bCommonProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.activity.v2.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.apps.drive.activity.v2B\x0bCommonProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2'
    _globals['_TIMERANGE']._serialized_start = 110
    _globals['_TIMERANGE']._serialized_end = 215
    _globals['_GROUP']._serialized_start = 217
    _globals['_GROUP']._serialized_end = 254
    _globals['_DOMAIN']._serialized_start = 256
    _globals['_DOMAIN']._serialized_end = 297