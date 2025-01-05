"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/feature_monitoring_stats.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1/feature_monitoring_stats.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xef\x01\n\x13FeatureStatsAnomaly\x12\r\n\x05score\x18\x01 \x01(\x01\x12\x11\n\tstats_uri\x18\x03 \x01(\t\x12\x13\n\x0banomaly_uri\x18\x04 \x01(\t\x12\x1e\n\x16distribution_deviation\x18\x05 \x01(\x01\x12#\n\x1banomaly_detection_threshold\x18\t \x01(\x01\x12.\n\nstart_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\xd9\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1bFeatureMonitoringStatsProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.feature_monitoring_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1bFeatureMonitoringStatsProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_FEATURESTATSANOMALY']._serialized_start = 123
    _globals['_FEATURESTATSANOMALY']._serialized_end = 362