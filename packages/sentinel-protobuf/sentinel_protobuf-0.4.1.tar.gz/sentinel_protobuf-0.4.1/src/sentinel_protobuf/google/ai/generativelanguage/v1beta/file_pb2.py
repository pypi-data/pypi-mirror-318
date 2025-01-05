"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ai/generativelanguage/v1beta/file.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ai/generativelanguage/v1beta/file.proto\x12#google.ai.generativelanguage.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x96\x05\n\x04File\x12Q\n\x0evideo_metadata\x18\x0c \x01(\x0b22.google.ai.generativelanguage.v1beta.VideoMetadataB\x03\xe0A\x03H\x00\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tmime_type\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x17\n\nsize_bytes\x18\x04 \x01(\x03B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x128\n\x0fexpiration_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bsha256_hash\x18\x08 \x01(\x0cB\x03\xe0A\x03\x12\x10\n\x03uri\x18\t \x01(\tB\x03\xe0A\x03\x12C\n\x05state\x18\n \x01(\x0e2/.google.ai.generativelanguage.v1beta.File.StateB\x03\xe0A\x03\x12&\n\x05error\x18\x0b \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\n\n\x06FAILED\x10\n:F\xeaAC\n&generativelanguage.googleapis.com/File\x12\x0cfiles/{file}*\x05files2\x04fileB\n\n\x08metadata"B\n\rVideoMetadata\x121\n\x0evideo_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x95\x01\n\'com.google.ai.generativelanguage.v1betaB\tFileProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta.file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ai.generativelanguage.v1betaB\tFileProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepb"
    _globals['_FILE'].fields_by_name['video_metadata']._loaded_options = None
    _globals['_FILE'].fields_by_name['video_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['name']._loaded_options = None
    _globals['_FILE'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x05'
    _globals['_FILE'].fields_by_name['display_name']._loaded_options = None
    _globals['_FILE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_FILE'].fields_by_name['mime_type']._loaded_options = None
    _globals['_FILE'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['size_bytes']._loaded_options = None
    _globals['_FILE'].fields_by_name['size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['create_time']._loaded_options = None
    _globals['_FILE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['update_time']._loaded_options = None
    _globals['_FILE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['expiration_time']._loaded_options = None
    _globals['_FILE'].fields_by_name['expiration_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['sha256_hash']._loaded_options = None
    _globals['_FILE'].fields_by_name['sha256_hash']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['uri']._loaded_options = None
    _globals['_FILE'].fields_by_name['uri']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['state']._loaded_options = None
    _globals['_FILE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_FILE'].fields_by_name['error']._loaded_options = None
    _globals['_FILE'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_FILE']._loaded_options = None
    _globals['_FILE']._serialized_options = b'\xeaAC\n&generativelanguage.googleapis.com/File\x12\x0cfiles/{file}*\x05files2\x04file'
    _globals['_FILE']._serialized_start = 238
    _globals['_FILE']._serialized_end = 900
    _globals['_FILE_STATE']._serialized_start = 746
    _globals['_FILE_STATE']._serialized_end = 816
    _globals['_VIDEOMETADATA']._serialized_start = 902
    _globals['_VIDEOMETADATA']._serialized_end = 968