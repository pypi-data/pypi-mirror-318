"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/v1/commit_response.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.spanner.v1 import transaction_pb2 as google_dot_spanner_dot_v1_dot_transaction__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/spanner/v1/commit_response.proto\x12\x11google.spanner.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a#google/spanner/v1/transaction.proto"\x9d\x02\n\x0eCommitResponse\x124\n\x10commit_timestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12C\n\x0ccommit_stats\x18\x02 \x01(\x0b2-.google.spanner.v1.CommitResponse.CommitStats\x12N\n\x0fprecommit_token\x18\x04 \x01(\x0b23.google.spanner.v1.MultiplexedSessionPrecommitTokenH\x00\x1a%\n\x0bCommitStats\x12\x16\n\x0emutation_count\x18\x01 \x01(\x03B\x19\n\x17MultiplexedSessionRetryB\xb6\x01\n\x15com.google.spanner.v1B\x13CommitResponseProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.commit_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.spanner.v1B\x13CommitResponseProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1'
    _globals['_COMMITRESPONSE']._serialized_start = 133
    _globals['_COMMITRESPONSE']._serialized_end = 418
    _globals['_COMMITRESPONSE_COMMITSTATS']._serialized_start = 354
    _globals['_COMMITRESPONSE_COMMITSTATS']._serialized_end = 391