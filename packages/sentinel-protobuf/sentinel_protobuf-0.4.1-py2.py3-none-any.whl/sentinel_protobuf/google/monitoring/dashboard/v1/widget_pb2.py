"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/widget.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.monitoring.dashboard.v1 import alertchart_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_alertchart__pb2
from .....google.monitoring.dashboard.v1 import collapsible_group_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_collapsible__group__pb2
from .....google.monitoring.dashboard.v1 import error_reporting_panel_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_error__reporting__panel__pb2
from .....google.monitoring.dashboard.v1 import incident_list_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_incident__list__pb2
from .....google.monitoring.dashboard.v1 import logs_panel_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_logs__panel__pb2
from .....google.monitoring.dashboard.v1 import piechart_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_piechart__pb2
from .....google.monitoring.dashboard.v1 import scorecard_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_scorecard__pb2
from .....google.monitoring.dashboard.v1 import section_header_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_section__header__pb2
from .....google.monitoring.dashboard.v1 import single_view_group_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_single__view__group__pb2
from .....google.monitoring.dashboard.v1 import table_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_table__pb2
from .....google.monitoring.dashboard.v1 import text_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_text__pb2
from .....google.monitoring.dashboard.v1 import xychart_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_xychart__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/monitoring/dashboard/v1/widget.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a/google/monitoring/dashboard/v1/alertchart.proto\x1a6google/monitoring/dashboard/v1/collapsible_group.proto\x1a:google/monitoring/dashboard/v1/error_reporting_panel.proto\x1a2google/monitoring/dashboard/v1/incident_list.proto\x1a/google/monitoring/dashboard/v1/logs_panel.proto\x1a-google/monitoring/dashboard/v1/piechart.proto\x1a.google/monitoring/dashboard/v1/scorecard.proto\x1a3google/monitoring/dashboard/v1/section_header.proto\x1a6google/monitoring/dashboard/v1/single_view_group.proto\x1a*google/monitoring/dashboard/v1/table.proto\x1a)google/monitoring/dashboard/v1/text.proto\x1a,google/monitoring/dashboard/v1/xychart.proto\x1a\x1bgoogle/protobuf/empty.proto"\xa8\x07\n\x06Widget\x12\x12\n\x05title\x18\x01 \x01(\tB\x03\xe0A\x01\x12;\n\x08xy_chart\x18\x02 \x01(\x0b2\'.google.monitoring.dashboard.v1.XyChartH\x00\x12>\n\tscorecard\x18\x03 \x01(\x0b2).google.monitoring.dashboard.v1.ScorecardH\x00\x124\n\x04text\x18\x04 \x01(\x0b2$.google.monitoring.dashboard.v1.TextH\x00\x12\'\n\x05blank\x18\x05 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12A\n\x0balert_chart\x18\x07 \x01(\x0b2*.google.monitoring.dashboard.v1.AlertChartH\x00\x12L\n\x11time_series_table\x18\x08 \x01(\x0b2/.google.monitoring.dashboard.v1.TimeSeriesTableH\x00\x12M\n\x11collapsible_group\x18\t \x01(\x0b20.google.monitoring.dashboard.v1.CollapsibleGroupH\x00\x12?\n\nlogs_panel\x18\n \x01(\x0b2).google.monitoring.dashboard.v1.LogsPanelH\x00\x12E\n\rincident_list\x18\x0c \x01(\x0b2,.google.monitoring.dashboard.v1.IncidentListH\x00\x12=\n\tpie_chart\x18\x0e \x01(\x0b2(.google.monitoring.dashboard.v1.PieChartH\x00\x12T\n\x15error_reporting_panel\x18\x13 \x01(\x0b23.google.monitoring.dashboard.v1.ErrorReportingPanelH\x00\x12G\n\x0esection_header\x18\x15 \x01(\x0b2-.google.monitoring.dashboard.v1.SectionHeaderH\x00\x12L\n\x11single_view_group\x18\x16 \x01(\x0b2/.google.monitoring.dashboard.v1.SingleViewGroupH\x00\x12\x0f\n\x02id\x18\x11 \x01(\tB\x03\xe0A\x01B\t\n\x07contentB\xf4\x01\n"com.google.monitoring.dashboard.v1B\x0bWidgetProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.widget_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x0bWidgetProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_WIDGET'].fields_by_name['title']._loaded_options = None
    _globals['_WIDGET'].fields_by_name['title']._serialized_options = b'\xe0A\x01'
    _globals['_WIDGET'].fields_by_name['id']._loaded_options = None
    _globals['_WIDGET'].fields_by_name['id']._serialized_options = b'\xe0A\x01'
    _globals['_WIDGET']._serialized_start = 745
    _globals['_WIDGET']._serialized_end = 1681