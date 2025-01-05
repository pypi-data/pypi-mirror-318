"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1/common.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/firestore/v1/common.proto\x12\x13google.firestore.v1\x1a\x1fgoogle/protobuf/timestamp.proto"#\n\x0cDocumentMask\x12\x13\n\x0bfield_paths\x18\x01 \x03(\t"e\n\x0cPrecondition\x12\x10\n\x06exists\x18\x01 \x01(\x08H\x00\x121\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x10\n\x0econdition_type"\xa9\x02\n\x12TransactionOptions\x12E\n\tread_only\x18\x02 \x01(\x0b20.google.firestore.v1.TransactionOptions.ReadOnlyH\x00\x12G\n\nread_write\x18\x03 \x01(\x0b21.google.firestore.v1.TransactionOptions.ReadWriteH\x00\x1a&\n\tReadWrite\x12\x19\n\x11retry_transaction\x18\x01 \x01(\x0c\x1aS\n\x08ReadOnly\x12/\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x16\n\x14consistency_selectorB\x06\n\x04modeB\xc3\x01\n\x17com.google.firestore.v1B\x0bCommonProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.firestore.v1B\x0bCommonProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1'
    _globals['_DOCUMENTMASK']._serialized_start = 90
    _globals['_DOCUMENTMASK']._serialized_end = 125
    _globals['_PRECONDITION']._serialized_start = 127
    _globals['_PRECONDITION']._serialized_end = 228
    _globals['_TRANSACTIONOPTIONS']._serialized_start = 231
    _globals['_TRANSACTIONOPTIONS']._serialized_end = 528
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_start = 397
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_end = 435
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_start = 437
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_end = 520