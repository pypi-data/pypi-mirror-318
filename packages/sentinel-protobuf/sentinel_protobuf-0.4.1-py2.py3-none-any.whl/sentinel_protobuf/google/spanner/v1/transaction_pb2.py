"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/v1/transaction.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/spanner/v1/transaction.proto\x12\x11google.spanner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xce\x06\n\x12TransactionOptions\x12E\n\nread_write\x18\x01 \x01(\x0b2/.google.spanner.v1.TransactionOptions.ReadWriteH\x00\x12O\n\x0fpartitioned_dml\x18\x03 \x01(\x0b24.google.spanner.v1.TransactionOptions.PartitionedDmlH\x00\x12C\n\tread_only\x18\x02 \x01(\x0b2..google.spanner.v1.TransactionOptions.ReadOnlyH\x00\x12\'\n\x1fexclude_txn_from_change_streams\x18\x05 \x01(\x08\x1a\xec\x01\n\tReadWrite\x12T\n\x0eread_lock_mode\x18\x01 \x01(\x0e2<.google.spanner.v1.TransactionOptions.ReadWrite.ReadLockMode\x128\n+multiplexed_session_previous_transaction_id\x18\x02 \x01(\x0cB\x03\xe0A\x01"O\n\x0cReadLockMode\x12\x1e\n\x1aREAD_LOCK_MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPESSIMISTIC\x10\x01\x12\x0e\n\nOPTIMISTIC\x10\x02\x1a\x10\n\x0ePartitionedDml\x1a\xa8\x02\n\x08ReadOnly\x12\x10\n\x06strong\x18\x01 \x01(\x08H\x00\x128\n\x12min_read_timestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x122\n\rmax_staleness\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x124\n\x0eread_timestamp\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x124\n\x0fexact_staleness\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x12\x1d\n\x15return_read_timestamp\x18\x06 \x01(\x08B\x11\n\x0ftimestamp_boundB\x06\n\x04mode"\x9b\x01\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\x0c\x122\n\x0eread_timestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12L\n\x0fprecommit_token\x18\x03 \x01(\x0b23.google.spanner.v1.MultiplexedSessionPrecommitToken"\xa4\x01\n\x13TransactionSelector\x12;\n\nsingle_use\x18\x01 \x01(\x0b2%.google.spanner.v1.TransactionOptionsH\x00\x12\x0c\n\x02id\x18\x02 \x01(\x0cH\x00\x126\n\x05begin\x18\x03 \x01(\x0b2%.google.spanner.v1.TransactionOptionsH\x00B\n\n\x08selector"L\n MultiplexedSessionPrecommitToken\x12\x17\n\x0fprecommit_token\x18\x01 \x01(\x0c\x12\x0f\n\x07seq_num\x18\x02 \x01(\x05B\xb3\x01\n\x15com.google.spanner.v1B\x10TransactionProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.transaction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.spanner.v1B\x10TransactionProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1'
    _globals['_TRANSACTIONOPTIONS_READWRITE'].fields_by_name['multiplexed_session_previous_transaction_id']._loaded_options = None
    _globals['_TRANSACTIONOPTIONS_READWRITE'].fields_by_name['multiplexed_session_previous_transaction_id']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSACTIONOPTIONS']._serialized_start = 157
    _globals['_TRANSACTIONOPTIONS']._serialized_end = 1003
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_start = 442
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_end = 678
    _globals['_TRANSACTIONOPTIONS_READWRITE_READLOCKMODE']._serialized_start = 599
    _globals['_TRANSACTIONOPTIONS_READWRITE_READLOCKMODE']._serialized_end = 678
    _globals['_TRANSACTIONOPTIONS_PARTITIONEDDML']._serialized_start = 680
    _globals['_TRANSACTIONOPTIONS_PARTITIONEDDML']._serialized_end = 696
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_start = 699
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_end = 995
    _globals['_TRANSACTION']._serialized_start = 1006
    _globals['_TRANSACTION']._serialized_end = 1161
    _globals['_TRANSACTIONSELECTOR']._serialized_start = 1164
    _globals['_TRANSACTIONSELECTOR']._serialized_end = 1328
    _globals['_MULTIPLEXEDSESSIONPRECOMMITTOKEN']._serialized_start = 1330
    _globals['_MULTIPLEXEDSESSIONPRECOMMITTOKEN']._serialized_end = 1406