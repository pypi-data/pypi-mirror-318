"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/metrics.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.monitoring.dashboard.v1 import common_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/monitoring/dashboard/v1/metrics.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/monitoring/dashboard/v1/common.proto"\xc2\x02\n\x0fTimeSeriesQuery\x12N\n\x12time_series_filter\x18\x01 \x01(\x0b20.google.monitoring.dashboard.v1.TimeSeriesFilterH\x00\x12Y\n\x18time_series_filter_ratio\x18\x02 \x01(\x0b25.google.monitoring.dashboard.v1.TimeSeriesFilterRatioH\x00\x12$\n\x1atime_series_query_language\x18\x03 \x01(\tH\x00\x12\x1a\n\x10prometheus_query\x18\x06 \x01(\tH\x00\x12\x15\n\runit_override\x18\x05 \x01(\t\x12!\n\x14output_full_duration\x18\x07 \x01(\x08B\x03\xe0A\x01B\x08\n\x06source"\x8a\x03\n\x10TimeSeriesFilter\x12\x13\n\x06filter\x18\x01 \x01(\tB\x03\xe0A\x02\x12@\n\x0baggregation\x18\x02 \x01(\x0b2+.google.monitoring.dashboard.v1.Aggregation\x12J\n\x15secondary_aggregation\x18\x03 \x01(\x0b2+.google.monitoring.dashboard.v1.Aggregation\x12W\n\x17pick_time_series_filter\x18\x04 \x01(\x0b24.google.monitoring.dashboard.v1.PickTimeSeriesFilterH\x00\x12i\n\x1estatistical_time_series_filter\x18\x05 \x01(\x0b2;.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilterB\x02\x18\x01H\x00B\x0f\n\routput_filter"\xc6\x04\n\x15TimeSeriesFilterRatio\x12R\n\tnumerator\x18\x01 \x01(\x0b2?.google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart\x12T\n\x0bdenominator\x18\x02 \x01(\x0b2?.google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart\x12J\n\x15secondary_aggregation\x18\x03 \x01(\x0b2+.google.monitoring.dashboard.v1.Aggregation\x12W\n\x17pick_time_series_filter\x18\x04 \x01(\x0b24.google.monitoring.dashboard.v1.PickTimeSeriesFilterH\x00\x12i\n\x1estatistical_time_series_filter\x18\x05 \x01(\x0b2;.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilterB\x02\x18\x01H\x00\x1ab\n\tRatioPart\x12\x13\n\x06filter\x18\x01 \x01(\tB\x03\xe0A\x02\x12@\n\x0baggregation\x18\x02 \x01(\x0b2+.google.monitoring.dashboard.v1.AggregationB\x0f\n\routput_filter"\xaa\x03\n\tThreshold\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12>\n\x05color\x18\x03 \x01(\x0e2/.google.monitoring.dashboard.v1.Threshold.Color\x12F\n\tdirection\x18\x04 \x01(\x0e23.google.monitoring.dashboard.v1.Threshold.Direction\x12I\n\x0btarget_axis\x18\x05 \x01(\x0e24.google.monitoring.dashboard.v1.Threshold.TargetAxis"3\n\x05Color\x12\x15\n\x11COLOR_UNSPECIFIED\x10\x00\x12\n\n\x06YELLOW\x10\x04\x12\x07\n\x03RED\x10\x06"<\n\tDirection\x12\x19\n\x15DIRECTION_UNSPECIFIED\x10\x00\x12\t\n\x05ABOVE\x10\x01\x12\t\n\x05BELOW\x10\x02"9\n\nTargetAxis\x12\x1b\n\x17TARGET_AXIS_UNSPECIFIED\x10\x00\x12\x06\n\x02Y1\x10\x01\x12\x06\n\x02Y2\x10\x02*Q\n\x0eSparkChartType\x12 \n\x1cSPARK_CHART_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nSPARK_LINE\x10\x01\x12\r\n\tSPARK_BAR\x10\x02B\xf5\x01\n"com.google.monitoring.dashboard.v1B\x0cMetricsProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.metrics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x0cMetricsProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_TIMESERIESQUERY'].fields_by_name['output_full_duration']._loaded_options = None
    _globals['_TIMESERIESQUERY'].fields_by_name['output_full_duration']._serialized_options = b'\xe0A\x01'
    _globals['_TIMESERIESFILTER'].fields_by_name['filter']._loaded_options = None
    _globals['_TIMESERIESFILTER'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIESFILTER'].fields_by_name['statistical_time_series_filter']._loaded_options = None
    _globals['_TIMESERIESFILTER'].fields_by_name['statistical_time_series_filter']._serialized_options = b'\x18\x01'
    _globals['_TIMESERIESFILTERRATIO_RATIOPART'].fields_by_name['filter']._loaded_options = None
    _globals['_TIMESERIESFILTERRATIO_RATIOPART'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIESFILTERRATIO'].fields_by_name['statistical_time_series_filter']._loaded_options = None
    _globals['_TIMESERIESFILTERRATIO'].fields_by_name['statistical_time_series_filter']._serialized_options = b'\x18\x01'
    _globals['_SPARKCHARTTYPE']._serialized_start = 1894
    _globals['_SPARKCHARTTYPE']._serialized_end = 1975
    _globals['_TIMESERIESQUERY']._serialized_start = 159
    _globals['_TIMESERIESQUERY']._serialized_end = 481
    _globals['_TIMESERIESFILTER']._serialized_start = 484
    _globals['_TIMESERIESFILTER']._serialized_end = 878
    _globals['_TIMESERIESFILTERRATIO']._serialized_start = 881
    _globals['_TIMESERIESFILTERRATIO']._serialized_end = 1463
    _globals['_TIMESERIESFILTERRATIO_RATIOPART']._serialized_start = 1348
    _globals['_TIMESERIESFILTERRATIO_RATIOPART']._serialized_end = 1446
    _globals['_THRESHOLD']._serialized_start = 1466
    _globals['_THRESHOLD']._serialized_end = 1892
    _globals['_THRESHOLD_COLOR']._serialized_start = 1720
    _globals['_THRESHOLD_COLOR']._serialized_end = 1771
    _globals['_THRESHOLD_DIRECTION']._serialized_start = 1773
    _globals['_THRESHOLD_DIRECTION']._serialized_end = 1833
    _globals['_THRESHOLD_TARGETAXIS']._serialized_start = 1835
    _globals['_THRESHOLD_TARGETAXIS']._serialized_end = 1892