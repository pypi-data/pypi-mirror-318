"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/xychart.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.monitoring.dashboard.v1 import metrics_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_metrics__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/monitoring/dashboard/v1/xychart.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/monitoring/dashboard/v1/metrics.proto\x1a\x1egoogle/protobuf/duration.proto"\xcd\x08\n\x07XyChart\x12G\n\tdata_sets\x18\x01 \x03(\x0b2/.google.monitoring.dashboard.v1.XyChart.DataSetB\x03\xe0A\x02\x125\n\x12timeshift_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12=\n\nthresholds\x18\x05 \x03(\x0b2).google.monitoring.dashboard.v1.Threshold\x12<\n\x06x_axis\x18\x06 \x01(\x0b2,.google.monitoring.dashboard.v1.XyChart.Axis\x12<\n\x06y_axis\x18\x07 \x01(\x0b2,.google.monitoring.dashboard.v1.XyChart.Axis\x12=\n\x07y2_axis\x18\t \x01(\x0b2,.google.monitoring.dashboard.v1.XyChart.Axis\x12C\n\rchart_options\x18\x08 \x01(\x0b2,.google.monitoring.dashboard.v1.ChartOptions\x1a\xf0\x03\n\x07DataSet\x12O\n\x11time_series_query\x18\x01 \x01(\x0b2/.google.monitoring.dashboard.v1.TimeSeriesQueryB\x03\xe0A\x02\x12K\n\tplot_type\x18\x02 \x01(\x0e28.google.monitoring.dashboard.v1.XyChart.DataSet.PlotType\x12\x17\n\x0flegend_template\x18\x03 \x01(\t\x12<\n\x14min_alignment_period\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12T\n\x0btarget_axis\x18\x05 \x01(\x0e2:.google.monitoring.dashboard.v1.XyChart.DataSet.TargetAxisB\x03\xe0A\x01"_\n\x08PlotType\x12\x19\n\x15PLOT_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04LINE\x10\x01\x12\x10\n\x0cSTACKED_AREA\x10\x02\x12\x0f\n\x0bSTACKED_BAR\x10\x03\x12\x0b\n\x07HEATMAP\x10\x04"9\n\nTargetAxis\x12\x1b\n\x17TARGET_AXIS_UNSPECIFIED\x10\x00\x12\x06\n\x02Y1\x10\x01\x12\x06\n\x02Y2\x10\x02\x1a\x8f\x01\n\x04Axis\x12\r\n\x05label\x18\x01 \x01(\t\x12A\n\x05scale\x18\x02 \x01(\x0e22.google.monitoring.dashboard.v1.XyChart.Axis.Scale"5\n\x05Scale\x12\x15\n\x11SCALE_UNSPECIFIED\x10\x00\x12\n\n\x06LINEAR\x10\x01\x12\t\n\x05LOG10\x10\x02"\x8e\x01\n\x0cChartOptions\x12?\n\x04mode\x18\x01 \x01(\x0e21.google.monitoring.dashboard.v1.ChartOptions.Mode"=\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\t\n\x05COLOR\x10\x01\x12\t\n\x05X_RAY\x10\x02\x12\t\n\x05STATS\x10\x03B\xf5\x01\n"com.google.monitoring.dashboard.v1B\x0cXyChartProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.xychart_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x0cXyChartProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_XYCHART_DATASET'].fields_by_name['time_series_query']._loaded_options = None
    _globals['_XYCHART_DATASET'].fields_by_name['time_series_query']._serialized_options = b'\xe0A\x02'
    _globals['_XYCHART_DATASET'].fields_by_name['min_alignment_period']._loaded_options = None
    _globals['_XYCHART_DATASET'].fields_by_name['min_alignment_period']._serialized_options = b'\xe0A\x01'
    _globals['_XYCHART_DATASET'].fields_by_name['target_axis']._loaded_options = None
    _globals['_XYCHART_DATASET'].fields_by_name['target_axis']._serialized_options = b'\xe0A\x01'
    _globals['_XYCHART'].fields_by_name['data_sets']._loaded_options = None
    _globals['_XYCHART'].fields_by_name['data_sets']._serialized_options = b'\xe0A\x02'
    _globals['_XYCHART']._serialized_start = 192
    _globals['_XYCHART']._serialized_end = 1293
    _globals['_XYCHART_DATASET']._serialized_start = 651
    _globals['_XYCHART_DATASET']._serialized_end = 1147
    _globals['_XYCHART_DATASET_PLOTTYPE']._serialized_start = 993
    _globals['_XYCHART_DATASET_PLOTTYPE']._serialized_end = 1088
    _globals['_XYCHART_DATASET_TARGETAXIS']._serialized_start = 1090
    _globals['_XYCHART_DATASET_TARGETAXIS']._serialized_end = 1147
    _globals['_XYCHART_AXIS']._serialized_start = 1150
    _globals['_XYCHART_AXIS']._serialized_end = 1293
    _globals['_XYCHART_AXIS_SCALE']._serialized_start = 1240
    _globals['_XYCHART_AXIS_SCALE']._serialized_end = 1293
    _globals['_CHARTOPTIONS']._serialized_start = 1296
    _globals['_CHARTOPTIONS']._serialized_end = 1438
    _globals['_CHARTOPTIONS_MODE']._serialized_start = 1377
    _globals['_CHARTOPTIONS_MODE']._serialized_end = 1438