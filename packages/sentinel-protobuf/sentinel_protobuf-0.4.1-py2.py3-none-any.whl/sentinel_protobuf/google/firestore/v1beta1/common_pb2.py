"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1beta1/common.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/firestore/v1beta1/common.proto\x12\x18google.firestore.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"#\n\x0cDocumentMask\x12\x13\n\x0bfield_paths\x18\x01 \x03(\t"e\n\x0cPrecondition\x12\x10\n\x06exists\x18\x01 \x01(\x08H\x00\x121\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x10\n\x0econdition_type"\xb3\x02\n\x12TransactionOptions\x12J\n\tread_only\x18\x02 \x01(\x0b25.google.firestore.v1beta1.TransactionOptions.ReadOnlyH\x00\x12L\n\nread_write\x18\x03 \x01(\x0b26.google.firestore.v1beta1.TransactionOptions.ReadWriteH\x00\x1a&\n\tReadWrite\x12\x19\n\x11retry_transaction\x18\x01 \x01(\x0c\x1aS\n\x08ReadOnly\x12/\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x16\n\x14consistency_selectorB\x06\n\x04modeB\xdc\x01\n\x1ccom.google.firestore.v1beta1B\x0bCommonProtoP\x01Z@cloud.google.com/go/firestore/apiv1beta1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1\xea\x02!Google::Cloud::Firestore::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1beta1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.firestore.v1beta1B\x0bCommonProtoP\x01Z@cloud.google.com/go/firestore/apiv1beta1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1\xea\x02!Google::Cloud::Firestore::V1beta1'
    _globals['_DOCUMENTMASK']._serialized_start = 100
    _globals['_DOCUMENTMASK']._serialized_end = 135
    _globals['_PRECONDITION']._serialized_start = 137
    _globals['_PRECONDITION']._serialized_end = 238
    _globals['_TRANSACTIONOPTIONS']._serialized_start = 241
    _globals['_TRANSACTIONOPTIONS']._serialized_end = 548
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_start = 417
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_end = 455
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_start = 457
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_end = 540