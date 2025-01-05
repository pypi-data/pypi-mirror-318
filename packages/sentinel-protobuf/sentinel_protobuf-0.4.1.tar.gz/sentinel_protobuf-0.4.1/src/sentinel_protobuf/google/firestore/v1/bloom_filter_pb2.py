"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1/bloom_filter.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/firestore/v1/bloom_filter.proto\x12\x13google.firestore.v1".\n\x0bBitSequence\x12\x0e\n\x06bitmap\x18\x01 \x01(\x0c\x12\x0f\n\x07padding\x18\x02 \x01(\x05"Q\n\x0bBloomFilter\x12.\n\x04bits\x18\x01 \x01(\x0b2 .google.firestore.v1.BitSequence\x12\x12\n\nhash_count\x18\x02 \x01(\x05B\xc8\x01\n\x17com.google.firestore.v1B\x10BloomFilterProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1.bloom_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.firestore.v1B\x10BloomFilterProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1'
    _globals['_BITSEQUENCE']._serialized_start = 63
    _globals['_BITSEQUENCE']._serialized_end = 109
    _globals['_BLOOMFILTER']._serialized_start = 111
    _globals['_BLOOMFILTER']._serialized_end = 192