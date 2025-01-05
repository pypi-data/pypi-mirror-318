"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/common.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/monitoring/dashboard/v1/common.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1agoogle/type/interval.proto"\xc1\x07\n\x0bAggregation\x123\n\x10alignment_period\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12O\n\x12per_series_aligner\x18\x02 \x01(\x0e23.google.monitoring.dashboard.v1.Aggregation.Aligner\x12Q\n\x14cross_series_reducer\x18\x04 \x01(\x0e23.google.monitoring.dashboard.v1.Aggregation.Reducer\x12\x17\n\x0fgroup_by_fields\x18\x05 \x03(\t"\x8b\x03\n\x07Aligner\x12\x0e\n\nALIGN_NONE\x10\x00\x12\x0f\n\x0bALIGN_DELTA\x10\x01\x12\x0e\n\nALIGN_RATE\x10\x02\x12\x15\n\x11ALIGN_INTERPOLATE\x10\x03\x12\x14\n\x10ALIGN_NEXT_OLDER\x10\x04\x12\r\n\tALIGN_MIN\x10\n\x12\r\n\tALIGN_MAX\x10\x0b\x12\x0e\n\nALIGN_MEAN\x10\x0c\x12\x0f\n\x0bALIGN_COUNT\x10\r\x12\r\n\tALIGN_SUM\x10\x0e\x12\x10\n\x0cALIGN_STDDEV\x10\x0f\x12\x14\n\x10ALIGN_COUNT_TRUE\x10\x10\x12\x15\n\x11ALIGN_COUNT_FALSE\x10\x18\x12\x17\n\x13ALIGN_FRACTION_TRUE\x10\x11\x12\x17\n\x13ALIGN_PERCENTILE_99\x10\x12\x12\x17\n\x13ALIGN_PERCENTILE_95\x10\x13\x12\x17\n\x13ALIGN_PERCENTILE_50\x10\x14\x12\x17\n\x13ALIGN_PERCENTILE_05\x10\x15\x12\x18\n\x14ALIGN_PERCENT_CHANGE\x10\x17"\xb1\x02\n\x07Reducer\x12\x0f\n\x0bREDUCE_NONE\x10\x00\x12\x0f\n\x0bREDUCE_MEAN\x10\x01\x12\x0e\n\nREDUCE_MIN\x10\x02\x12\x0e\n\nREDUCE_MAX\x10\x03\x12\x0e\n\nREDUCE_SUM\x10\x04\x12\x11\n\rREDUCE_STDDEV\x10\x05\x12\x10\n\x0cREDUCE_COUNT\x10\x06\x12\x15\n\x11REDUCE_COUNT_TRUE\x10\x07\x12\x16\n\x12REDUCE_COUNT_FALSE\x10\x0f\x12\x18\n\x14REDUCE_FRACTION_TRUE\x10\x08\x12\x18\n\x14REDUCE_PERCENTILE_99\x10\t\x12\x18\n\x14REDUCE_PERCENTILE_95\x10\n\x12\x18\n\x14REDUCE_PERCENTILE_50\x10\x0b\x12\x18\n\x14REDUCE_PERCENTILE_05\x10\x0c"\xb3\x03\n\x14PickTimeSeriesFilter\x12S\n\x0eranking_method\x18\x01 \x01(\x0e2;.google.monitoring.dashboard.v1.PickTimeSeriesFilter.Method\x12\x17\n\x0fnum_time_series\x18\x02 \x01(\x05\x12Q\n\tdirection\x18\x03 \x01(\x0e2>.google.monitoring.dashboard.v1.PickTimeSeriesFilter.Direction\x12\'\n\x08interval\x18\x04 \x01(\x0b2\x15.google.type.Interval"t\n\x06Method\x12\x16\n\x12METHOD_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMETHOD_MEAN\x10\x01\x12\x0e\n\nMETHOD_MAX\x10\x02\x12\x0e\n\nMETHOD_MIN\x10\x03\x12\x0e\n\nMETHOD_SUM\x10\x04\x12\x11\n\rMETHOD_LATEST\x10\x05";\n\tDirection\x12\x19\n\x15DIRECTION_UNSPECIFIED\x10\x00\x12\x07\n\x03TOP\x10\x01\x12\n\n\x06BOTTOM\x10\x02"\xd0\x01\n\x1bStatisticalTimeSeriesFilter\x12Z\n\x0eranking_method\x18\x01 \x01(\x0e2B.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter.Method\x12\x17\n\x0fnum_time_series\x18\x02 \x01(\x05"<\n\x06Method\x12\x16\n\x12METHOD_UNSPECIFIED\x10\x00\x12\x1a\n\x16METHOD_CLUSTER_OUTLIER\x10\x01B\xf4\x01\n"com.google.monitoring.dashboard.v1B\x0bCommonProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x0bCommonProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_AGGREGATION']._serialized_start = 140
    _globals['_AGGREGATION']._serialized_end = 1101
    _globals['_AGGREGATION_ALIGNER']._serialized_start = 398
    _globals['_AGGREGATION_ALIGNER']._serialized_end = 793
    _globals['_AGGREGATION_REDUCER']._serialized_start = 796
    _globals['_AGGREGATION_REDUCER']._serialized_end = 1101
    _globals['_PICKTIMESERIESFILTER']._serialized_start = 1104
    _globals['_PICKTIMESERIESFILTER']._serialized_end = 1539
    _globals['_PICKTIMESERIESFILTER_METHOD']._serialized_start = 1362
    _globals['_PICKTIMESERIESFILTER_METHOD']._serialized_end = 1478
    _globals['_PICKTIMESERIESFILTER_DIRECTION']._serialized_start = 1480
    _globals['_PICKTIMESERIESFILTER_DIRECTION']._serialized_end = 1539
    _globals['_STATISTICALTIMESERIESFILTER']._serialized_start = 1542
    _globals['_STATISTICALTIMESERIESFILTER']._serialized_end = 1750
    _globals['_STATISTICALTIMESERIESFILTER_METHOD']._serialized_start = 1690
    _globals['_STATISTICALTIMESERIESFILTER_METHOD']._serialized_end = 1750