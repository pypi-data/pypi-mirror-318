"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/piechart.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.monitoring.dashboard.v1 import metrics_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_metrics__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/monitoring/dashboard/v1/piechart.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/monitoring/dashboard/v1/metrics.proto\x1a\x1egoogle/protobuf/duration.proto"\xcf\x03\n\x08PieChart\x12P\n\tdata_sets\x18\x01 \x03(\x0b28.google.monitoring.dashboard.v1.PieChart.PieChartDataSetB\x03\xe0A\x02\x12N\n\nchart_type\x18\x02 \x01(\x0e25.google.monitoring.dashboard.v1.PieChart.PieChartTypeB\x03\xe0A\x02\x12\x18\n\x0bshow_labels\x18\x04 \x01(\x08B\x03\xe0A\x01\x1a\xc2\x01\n\x0fPieChartDataSet\x12O\n\x11time_series_query\x18\x01 \x01(\x0b2/.google.monitoring.dashboard.v1.TimeSeriesQueryB\x03\xe0A\x02\x12 \n\x13slice_name_template\x18\x02 \x01(\tB\x03\xe0A\x01\x12<\n\x14min_alignment_period\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01"B\n\x0cPieChartType\x12\x1e\n\x1aPIE_CHART_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03PIE\x10\x01\x12\t\n\x05DONUT\x10\x02B\xf6\x01\n"com.google.monitoring.dashboard.v1B\rPieChartProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.piechart_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\rPieChartProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_PIECHART_PIECHARTDATASET'].fields_by_name['time_series_query']._loaded_options = None
    _globals['_PIECHART_PIECHARTDATASET'].fields_by_name['time_series_query']._serialized_options = b'\xe0A\x02'
    _globals['_PIECHART_PIECHARTDATASET'].fields_by_name['slice_name_template']._loaded_options = None
    _globals['_PIECHART_PIECHARTDATASET'].fields_by_name['slice_name_template']._serialized_options = b'\xe0A\x01'
    _globals['_PIECHART_PIECHARTDATASET'].fields_by_name['min_alignment_period']._loaded_options = None
    _globals['_PIECHART_PIECHARTDATASET'].fields_by_name['min_alignment_period']._serialized_options = b'\xe0A\x01'
    _globals['_PIECHART'].fields_by_name['data_sets']._loaded_options = None
    _globals['_PIECHART'].fields_by_name['data_sets']._serialized_options = b'\xe0A\x02'
    _globals['_PIECHART'].fields_by_name['chart_type']._loaded_options = None
    _globals['_PIECHART'].fields_by_name['chart_type']._serialized_options = b'\xe0A\x02'
    _globals['_PIECHART'].fields_by_name['show_labels']._loaded_options = None
    _globals['_PIECHART'].fields_by_name['show_labels']._serialized_options = b'\xe0A\x01'
    _globals['_PIECHART']._serialized_start = 193
    _globals['_PIECHART']._serialized_end = 656
    _globals['_PIECHART_PIECHARTDATASET']._serialized_start = 394
    _globals['_PIECHART_PIECHARTDATASET']._serialized_end = 588
    _globals['_PIECHART_PIECHARTTYPE']._serialized_start = 590
    _globals['_PIECHART_PIECHARTTYPE']._serialized_end = 656