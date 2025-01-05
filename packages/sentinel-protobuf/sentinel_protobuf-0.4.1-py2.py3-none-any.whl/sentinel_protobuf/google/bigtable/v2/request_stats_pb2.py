"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/bigtable/v2/request_stats.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/bigtable/v2/request_stats.proto\x12\x12google.bigtable.v2\x1a\x1egoogle/protobuf/duration.proto"\x82\x01\n\x12ReadIterationStats\x12\x17\n\x0frows_seen_count\x18\x01 \x01(\x03\x12\x1b\n\x13rows_returned_count\x18\x02 \x01(\x03\x12\x18\n\x10cells_seen_count\x18\x03 \x01(\x03\x12\x1c\n\x14cells_returned_count\x18\x04 \x01(\x03"Q\n\x13RequestLatencyStats\x12:\n\x17frontend_server_latency\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"\xa1\x01\n\x11FullReadStatsView\x12D\n\x14read_iteration_stats\x18\x01 \x01(\x0b2&.google.bigtable.v2.ReadIterationStats\x12F\n\x15request_latency_stats\x18\x02 \x01(\x0b2\'.google.bigtable.v2.RequestLatencyStats"c\n\x0cRequestStats\x12E\n\x14full_read_stats_view\x18\x01 \x01(\x0b2%.google.bigtable.v2.FullReadStatsViewH\x00B\x0c\n\nstats_viewB\xbb\x01\n\x16com.google.bigtable.v2B\x11RequestStatsProtoP\x01Z8cloud.google.com/go/bigtable/apiv2/bigtablepb;bigtablepb\xaa\x02\x18Google.Cloud.Bigtable.V2\xca\x02\x18Google\\Cloud\\Bigtable\\V2\xea\x02\x1bGoogle::Cloud::Bigtable::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.bigtable.v2.request_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.bigtable.v2B\x11RequestStatsProtoP\x01Z8cloud.google.com/go/bigtable/apiv2/bigtablepb;bigtablepb\xaa\x02\x18Google.Cloud.Bigtable.V2\xca\x02\x18Google\\Cloud\\Bigtable\\V2\xea\x02\x1bGoogle::Cloud::Bigtable::V2'
    _globals['_READITERATIONSTATS']._serialized_start = 95
    _globals['_READITERATIONSTATS']._serialized_end = 225
    _globals['_REQUESTLATENCYSTATS']._serialized_start = 227
    _globals['_REQUESTLATENCYSTATS']._serialized_end = 308
    _globals['_FULLREADSTATSVIEW']._serialized_start = 311
    _globals['_FULLREADSTATSVIEW']._serialized_end = 472
    _globals['_REQUESTSTATS']._serialized_start = 474
    _globals['_REQUESTSTATS']._serialized_end = 573