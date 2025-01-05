"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/bigtable/v2/feature_flags.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/bigtable/v2/feature_flags.proto\x12\x12google.bigtable.v2"\x9e\x02\n\x0cFeatureFlags\x12\x15\n\rreverse_scans\x18\x01 \x01(\x08\x12\x1e\n\x16mutate_rows_rate_limit\x18\x03 \x01(\x08\x12\x1f\n\x17mutate_rows_rate_limit2\x18\x05 \x01(\x08\x12"\n\x1alast_scanned_row_responses\x18\x04 \x01(\x08\x12\x16\n\x0erouting_cookie\x18\x06 \x01(\x08\x12\x12\n\nretry_info\x18\x07 \x01(\x08\x12#\n\x1bclient_side_metrics_enabled\x18\x08 \x01(\x08\x12 \n\x18traffic_director_enabled\x18\t \x01(\x08\x12\x1f\n\x17direct_access_requested\x18\n \x01(\x08B\xbb\x01\n\x16com.google.bigtable.v2B\x11FeatureFlagsProtoP\x01Z8cloud.google.com/go/bigtable/apiv2/bigtablepb;bigtablepb\xaa\x02\x18Google.Cloud.Bigtable.V2\xca\x02\x18Google\\Cloud\\Bigtable\\V2\xea\x02\x1bGoogle::Cloud::Bigtable::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.bigtable.v2.feature_flags_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.bigtable.v2B\x11FeatureFlagsProtoP\x01Z8cloud.google.com/go/bigtable/apiv2/bigtablepb;bigtablepb\xaa\x02\x18Google.Cloud.Bigtable.V2\xca\x02\x18Google\\Cloud\\Bigtable\\V2\xea\x02\x1bGoogle::Cloud::Bigtable::V2'
    _globals['_FEATUREFLAGS']._serialized_start = 63
    _globals['_FEATUREFLAGS']._serialized_end = 349