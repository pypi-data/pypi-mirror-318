"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/scorecard.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.monitoring.dashboard.v1 import metrics_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_metrics__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/monitoring/dashboard/v1/scorecard.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/monitoring/dashboard/v1/metrics.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto"\xc9\x04\n\tScorecard\x12O\n\x11time_series_query\x18\x01 \x01(\x0b2/.google.monitoring.dashboard.v1.TimeSeriesQueryB\x03\xe0A\x02\x12I\n\ngauge_view\x18\x04 \x01(\x0b23.google.monitoring.dashboard.v1.Scorecard.GaugeViewH\x00\x12T\n\x10spark_chart_view\x18\x05 \x01(\x0b28.google.monitoring.dashboard.v1.Scorecard.SparkChartViewH\x00\x12,\n\nblank_view\x18\x07 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12=\n\nthresholds\x18\x06 \x03(\x0b2).google.monitoring.dashboard.v1.Threshold\x1a5\n\tGaugeView\x12\x13\n\x0blower_bound\x18\x01 \x01(\x01\x12\x13\n\x0bupper_bound\x18\x02 \x01(\x01\x1a\x98\x01\n\x0eSparkChartView\x12M\n\x10spark_chart_type\x18\x01 \x01(\x0e2..google.monitoring.dashboard.v1.SparkChartTypeB\x03\xe0A\x02\x127\n\x14min_alignment_period\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x0b\n\tdata_viewB\xf7\x01\n"com.google.monitoring.dashboard.v1B\x0eScorecardProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.scorecard_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x0eScorecardProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_SCORECARD_SPARKCHARTVIEW'].fields_by_name['spark_chart_type']._loaded_options = None
    _globals['_SCORECARD_SPARKCHARTVIEW'].fields_by_name['spark_chart_type']._serialized_options = b'\xe0A\x02'
    _globals['_SCORECARD'].fields_by_name['time_series_query']._loaded_options = None
    _globals['_SCORECARD'].fields_by_name['time_series_query']._serialized_options = b'\xe0A\x02'
    _globals['_SCORECARD']._serialized_start = 223
    _globals['_SCORECARD']._serialized_end = 808
    _globals['_SCORECARD_GAUGEVIEW']._serialized_start = 587
    _globals['_SCORECARD_GAUGEVIEW']._serialized_end = 640
    _globals['_SCORECARD_SPARKCHARTVIEW']._serialized_start = 643
    _globals['_SCORECARD_SPARKCHARTVIEW']._serialized_end = 795