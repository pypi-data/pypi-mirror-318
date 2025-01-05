"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/v1/keys.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgoogle/spanner/v1/keys.proto\x12\x11google.spanner.v1\x1a\x1cgoogle/protobuf/struct.proto"\xf4\x01\n\x08KeyRange\x122\n\x0cstart_closed\x18\x01 \x01(\x0b2\x1a.google.protobuf.ListValueH\x00\x120\n\nstart_open\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValueH\x00\x120\n\nend_closed\x18\x03 \x01(\x0b2\x1a.google.protobuf.ListValueH\x01\x12.\n\x08end_open\x18\x04 \x01(\x0b2\x1a.google.protobuf.ListValueH\x01B\x10\n\x0estart_key_typeB\x0e\n\x0cend_key_type"l\n\x06KeySet\x12(\n\x04keys\x18\x01 \x03(\x0b2\x1a.google.protobuf.ListValue\x12+\n\x06ranges\x18\x02 \x03(\x0b2\x1b.google.spanner.v1.KeyRange\x12\x0b\n\x03all\x18\x03 \x01(\x08B\xac\x01\n\x15com.google.spanner.v1B\tKeysProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.keys_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.spanner.v1B\tKeysProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1'
    _globals['_KEYRANGE']._serialized_start = 82
    _globals['_KEYRANGE']._serialized_end = 326
    _globals['_KEYSET']._serialized_start = 328
    _globals['_KEYSET']._serialized_end = 436