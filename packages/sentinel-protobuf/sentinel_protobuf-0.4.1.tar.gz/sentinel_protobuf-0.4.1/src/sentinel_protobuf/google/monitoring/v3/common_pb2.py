"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/common.proto')
_sym_db = _symbol_database.Default()
from ....google.api import distribution_pb2 as google_dot_api_dot_distribution__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/monitoring/v3/common.proto\x12\x14google.monitoring.v3\x1a\x1dgoogle/api/distribution.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xaa\x01\n\nTypedValue\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x126\n\x12distribution_value\x18\x05 \x01(\x0b2\x18.google.api.DistributionH\x00B\x07\n\x05value"l\n\x0cTimeInterval\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xad\x07\n\x0bAggregation\x123\n\x10alignment_period\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12E\n\x12per_series_aligner\x18\x02 \x01(\x0e2).google.monitoring.v3.Aggregation.Aligner\x12G\n\x14cross_series_reducer\x18\x04 \x01(\x0e2).google.monitoring.v3.Aggregation.Reducer\x12\x17\n\x0fgroup_by_fields\x18\x05 \x03(\t"\x8b\x03\n\x07Aligner\x12\x0e\n\nALIGN_NONE\x10\x00\x12\x0f\n\x0bALIGN_DELTA\x10\x01\x12\x0e\n\nALIGN_RATE\x10\x02\x12\x15\n\x11ALIGN_INTERPOLATE\x10\x03\x12\x14\n\x10ALIGN_NEXT_OLDER\x10\x04\x12\r\n\tALIGN_MIN\x10\n\x12\r\n\tALIGN_MAX\x10\x0b\x12\x0e\n\nALIGN_MEAN\x10\x0c\x12\x0f\n\x0bALIGN_COUNT\x10\r\x12\r\n\tALIGN_SUM\x10\x0e\x12\x10\n\x0cALIGN_STDDEV\x10\x0f\x12\x14\n\x10ALIGN_COUNT_TRUE\x10\x10\x12\x15\n\x11ALIGN_COUNT_FALSE\x10\x18\x12\x17\n\x13ALIGN_FRACTION_TRUE\x10\x11\x12\x17\n\x13ALIGN_PERCENTILE_99\x10\x12\x12\x17\n\x13ALIGN_PERCENTILE_95\x10\x13\x12\x17\n\x13ALIGN_PERCENTILE_50\x10\x14\x12\x17\n\x13ALIGN_PERCENTILE_05\x10\x15\x12\x18\n\x14ALIGN_PERCENT_CHANGE\x10\x17"\xb1\x02\n\x07Reducer\x12\x0f\n\x0bREDUCE_NONE\x10\x00\x12\x0f\n\x0bREDUCE_MEAN\x10\x01\x12\x0e\n\nREDUCE_MIN\x10\x02\x12\x0e\n\nREDUCE_MAX\x10\x03\x12\x0e\n\nREDUCE_SUM\x10\x04\x12\x11\n\rREDUCE_STDDEV\x10\x05\x12\x10\n\x0cREDUCE_COUNT\x10\x06\x12\x15\n\x11REDUCE_COUNT_TRUE\x10\x07\x12\x16\n\x12REDUCE_COUNT_FALSE\x10\x0f\x12\x18\n\x14REDUCE_FRACTION_TRUE\x10\x08\x12\x18\n\x14REDUCE_PERCENTILE_99\x10\t\x12\x18\n\x14REDUCE_PERCENTILE_95\x10\n\x12\x18\n\x14REDUCE_PERCENTILE_50\x10\x0b\x12\x18\n\x14REDUCE_PERCENTILE_05\x10\x0c*\x9e\x01\n\x0eComparisonType\x12\x1a\n\x16COMPARISON_UNSPECIFIED\x10\x00\x12\x11\n\rCOMPARISON_GT\x10\x01\x12\x11\n\rCOMPARISON_GE\x10\x02\x12\x11\n\rCOMPARISON_LT\x10\x03\x12\x11\n\rCOMPARISON_LE\x10\x04\x12\x11\n\rCOMPARISON_EQ\x10\x05\x12\x11\n\rCOMPARISON_NE\x10\x06*a\n\x0bServiceTier\x12\x1c\n\x18SERVICE_TIER_UNSPECIFIED\x10\x00\x12\x16\n\x12SERVICE_TIER_BASIC\x10\x01\x12\x18\n\x14SERVICE_TIER_PREMIUM\x10\x02\x1a\x02\x18\x01B\xcd\x01\n\x18com.google.monitoring.v3B\x0bCommonProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xa2\x02\x04GMON\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x0bCommonProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xa2\x02\x04GMON\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_SERVICETIER']._loaded_options = None
    _globals['_SERVICETIER']._serialized_options = b'\x18\x01'
    _globals['_COMPARISONTYPE']._serialized_start = 1383
    _globals['_COMPARISONTYPE']._serialized_end = 1541
    _globals['_SERVICETIER']._serialized_start = 1543
    _globals['_SERVICETIER']._serialized_end = 1640
    _globals['_TYPEDVALUE']._serialized_start = 156
    _globals['_TYPEDVALUE']._serialized_end = 326
    _globals['_TIMEINTERVAL']._serialized_start = 328
    _globals['_TIMEINTERVAL']._serialized_end = 436
    _globals['_AGGREGATION']._serialized_start = 439
    _globals['_AGGREGATION']._serialized_end = 1380
    _globals['_AGGREGATION_ALIGNER']._serialized_start = 677
    _globals['_AGGREGATION_ALIGNER']._serialized_end = 1072
    _globals['_AGGREGATION_REDUCER']._serialized_start = 1075
    _globals['_AGGREGATION_REDUCER']._serialized_end = 1380