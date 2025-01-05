"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/table.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.monitoring.dashboard.v1 import metrics_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_metrics__pb2
from .....google.monitoring.dashboard.v1 import table_display_options_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_table__display__options__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/monitoring/dashboard/v1/table.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/monitoring/dashboard/v1/metrics.proto\x1a:google/monitoring/dashboard/v1/table_display_options.proto\x1a\x1egoogle/protobuf/duration.proto"\xd2\x05\n\x0fTimeSeriesTable\x12T\n\tdata_sets\x18\x01 \x03(\x0b2<.google.monitoring.dashboard.v1.TimeSeriesTable.TableDataSetB\x03\xe0A\x02\x12f\n\x14metric_visualization\x18\x02 \x01(\x0e2C.google.monitoring.dashboard.v1.TimeSeriesTable.MetricVisualizationB\x03\xe0A\x01\x12\\\n\x0fcolumn_settings\x18\x04 \x03(\x0b2>.google.monitoring.dashboard.v1.TimeSeriesTable.ColumnSettingsB\x03\xe0A\x01\x1a\x93\x02\n\x0cTableDataSet\x12O\n\x11time_series_query\x18\x01 \x01(\x0b2/.google.monitoring.dashboard.v1.TimeSeriesQueryB\x03\xe0A\x02\x12\x1b\n\x0etable_template\x18\x02 \x01(\tB\x03\xe0A\x01\x12<\n\x14min_alignment_period\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12W\n\x15table_display_options\x18\x04 \x01(\x0b23.google.monitoring.dashboard.v1.TableDisplayOptionsB\x03\xe0A\x01\x1a;\n\x0eColumnSettings\x12\x13\n\x06column\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07visible\x18\x02 \x01(\x08B\x03\xe0A\x02"P\n\x13MetricVisualization\x12$\n METRIC_VISUALIZATION_UNSPECIFIED\x10\x00\x12\n\n\x06NUMBER\x10\x01\x12\x07\n\x03BAR\x10\x02B\xf3\x01\n"com.google.monitoring.dashboard.v1B\nTableProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.table_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\nTableProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_TIMESERIESTABLE_TABLEDATASET'].fields_by_name['time_series_query']._loaded_options = None
    _globals['_TIMESERIESTABLE_TABLEDATASET'].fields_by_name['time_series_query']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIESTABLE_TABLEDATASET'].fields_by_name['table_template']._loaded_options = None
    _globals['_TIMESERIESTABLE_TABLEDATASET'].fields_by_name['table_template']._serialized_options = b'\xe0A\x01'
    _globals['_TIMESERIESTABLE_TABLEDATASET'].fields_by_name['min_alignment_period']._loaded_options = None
    _globals['_TIMESERIESTABLE_TABLEDATASET'].fields_by_name['min_alignment_period']._serialized_options = b'\xe0A\x01'
    _globals['_TIMESERIESTABLE_TABLEDATASET'].fields_by_name['table_display_options']._loaded_options = None
    _globals['_TIMESERIESTABLE_TABLEDATASET'].fields_by_name['table_display_options']._serialized_options = b'\xe0A\x01'
    _globals['_TIMESERIESTABLE_COLUMNSETTINGS'].fields_by_name['column']._loaded_options = None
    _globals['_TIMESERIESTABLE_COLUMNSETTINGS'].fields_by_name['column']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIESTABLE_COLUMNSETTINGS'].fields_by_name['visible']._loaded_options = None
    _globals['_TIMESERIESTABLE_COLUMNSETTINGS'].fields_by_name['visible']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIESTABLE'].fields_by_name['data_sets']._loaded_options = None
    _globals['_TIMESERIESTABLE'].fields_by_name['data_sets']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIESTABLE'].fields_by_name['metric_visualization']._loaded_options = None
    _globals['_TIMESERIESTABLE'].fields_by_name['metric_visualization']._serialized_options = b'\xe0A\x01'
    _globals['_TIMESERIESTABLE'].fields_by_name['column_settings']._loaded_options = None
    _globals['_TIMESERIESTABLE'].fields_by_name['column_settings']._serialized_options = b'\xe0A\x01'
    _globals['_TIMESERIESTABLE']._serialized_start = 250
    _globals['_TIMESERIESTABLE']._serialized_end = 972
    _globals['_TIMESERIESTABLE_TABLEDATASET']._serialized_start = 554
    _globals['_TIMESERIESTABLE_TABLEDATASET']._serialized_end = 829
    _globals['_TIMESERIESTABLE_COLUMNSETTINGS']._serialized_start = 831
    _globals['_TIMESERIESTABLE_COLUMNSETTINGS']._serialized_end = 890
    _globals['_TIMESERIESTABLE_METRICVISUALIZATION']._serialized_start = 892
    _globals['_TIMESERIESTABLE_METRICVISUALIZATION']._serialized_end = 972