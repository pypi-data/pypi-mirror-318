"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/v1/mutation.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ....google.spanner.v1 import keys_pb2 as google_dot_spanner_dot_v1_dot_keys__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/spanner/v1/mutation.proto\x12\x11google.spanner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/spanner/v1/keys.proto"\xd5\x03\n\x08Mutation\x123\n\x06insert\x18\x01 \x01(\x0b2!.google.spanner.v1.Mutation.WriteH\x00\x123\n\x06update\x18\x02 \x01(\x0b2!.google.spanner.v1.Mutation.WriteH\x00\x12=\n\x10insert_or_update\x18\x03 \x01(\x0b2!.google.spanner.v1.Mutation.WriteH\x00\x124\n\x07replace\x18\x04 \x01(\x0b2!.google.spanner.v1.Mutation.WriteH\x00\x124\n\x06delete\x18\x05 \x01(\x0b2".google.spanner.v1.Mutation.DeleteH\x00\x1aX\n\x05Write\x12\x12\n\x05table\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0f\n\x07columns\x18\x02 \x03(\t\x12*\n\x06values\x18\x03 \x03(\x0b2\x1a.google.protobuf.ListValue\x1aM\n\x06Delete\x12\x12\n\x05table\x18\x01 \x01(\tB\x03\xe0A\x02\x12/\n\x07key_set\x18\x02 \x01(\x0b2\x19.google.spanner.v1.KeySetB\x03\xe0A\x02B\x0b\n\toperationB\xb0\x01\n\x15com.google.spanner.v1B\rMutationProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.mutation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.spanner.v1B\rMutationProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1'
    _globals['_MUTATION_WRITE'].fields_by_name['table']._loaded_options = None
    _globals['_MUTATION_WRITE'].fields_by_name['table']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATION_DELETE'].fields_by_name['table']._loaded_options = None
    _globals['_MUTATION_DELETE'].fields_by_name['table']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATION_DELETE'].fields_by_name['key_set']._loaded_options = None
    _globals['_MUTATION_DELETE'].fields_by_name['key_set']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATION']._serialized_start = 149
    _globals['_MUTATION']._serialized_end = 618
    _globals['_MUTATION_WRITE']._serialized_start = 438
    _globals['_MUTATION_WRITE']._serialized_end = 526
    _globals['_MUTATION_DELETE']._serialized_start = 528
    _globals['_MUTATION_DELETE']._serialized_end = 605