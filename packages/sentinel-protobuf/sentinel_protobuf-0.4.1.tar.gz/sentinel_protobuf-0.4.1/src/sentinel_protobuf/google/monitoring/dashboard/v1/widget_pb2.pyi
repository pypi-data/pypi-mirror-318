from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.monitoring.dashboard.v1 import alertchart_pb2 as _alertchart_pb2
from google.monitoring.dashboard.v1 import collapsible_group_pb2 as _collapsible_group_pb2
from google.monitoring.dashboard.v1 import error_reporting_panel_pb2 as _error_reporting_panel_pb2
from google.monitoring.dashboard.v1 import incident_list_pb2 as _incident_list_pb2
from google.monitoring.dashboard.v1 import logs_panel_pb2 as _logs_panel_pb2
from google.monitoring.dashboard.v1 import piechart_pb2 as _piechart_pb2
from google.monitoring.dashboard.v1 import scorecard_pb2 as _scorecard_pb2
from google.monitoring.dashboard.v1 import section_header_pb2 as _section_header_pb2
from google.monitoring.dashboard.v1 import single_view_group_pb2 as _single_view_group_pb2
from google.monitoring.dashboard.v1 import table_pb2 as _table_pb2
from google.monitoring.dashboard.v1 import text_pb2 as _text_pb2
from google.monitoring.dashboard.v1 import xychart_pb2 as _xychart_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Widget(_message.Message):
    __slots__ = ('title', 'xy_chart', 'scorecard', 'text', 'blank', 'alert_chart', 'time_series_table', 'collapsible_group', 'logs_panel', 'incident_list', 'pie_chart', 'error_reporting_panel', 'section_header', 'single_view_group', 'id')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    XY_CHART_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BLANK_FIELD_NUMBER: _ClassVar[int]
    ALERT_CHART_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_TABLE_FIELD_NUMBER: _ClassVar[int]
    COLLAPSIBLE_GROUP_FIELD_NUMBER: _ClassVar[int]
    LOGS_PANEL_FIELD_NUMBER: _ClassVar[int]
    INCIDENT_LIST_FIELD_NUMBER: _ClassVar[int]
    PIE_CHART_FIELD_NUMBER: _ClassVar[int]
    ERROR_REPORTING_PANEL_FIELD_NUMBER: _ClassVar[int]
    SECTION_HEADER_FIELD_NUMBER: _ClassVar[int]
    SINGLE_VIEW_GROUP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    xy_chart: _xychart_pb2.XyChart
    scorecard: _scorecard_pb2.Scorecard
    text: _text_pb2.Text
    blank: _empty_pb2.Empty
    alert_chart: _alertchart_pb2.AlertChart
    time_series_table: _table_pb2.TimeSeriesTable
    collapsible_group: _collapsible_group_pb2.CollapsibleGroup
    logs_panel: _logs_panel_pb2.LogsPanel
    incident_list: _incident_list_pb2.IncidentList
    pie_chart: _piechart_pb2.PieChart
    error_reporting_panel: _error_reporting_panel_pb2.ErrorReportingPanel
    section_header: _section_header_pb2.SectionHeader
    single_view_group: _single_view_group_pb2.SingleViewGroup
    id: str

    def __init__(self, title: _Optional[str]=..., xy_chart: _Optional[_Union[_xychart_pb2.XyChart, _Mapping]]=..., scorecard: _Optional[_Union[_scorecard_pb2.Scorecard, _Mapping]]=..., text: _Optional[_Union[_text_pb2.Text, _Mapping]]=..., blank: _Optional[_Union[_empty_pb2.Empty, _Mapping]]=..., alert_chart: _Optional[_Union[_alertchart_pb2.AlertChart, _Mapping]]=..., time_series_table: _Optional[_Union[_table_pb2.TimeSeriesTable, _Mapping]]=..., collapsible_group: _Optional[_Union[_collapsible_group_pb2.CollapsibleGroup, _Mapping]]=..., logs_panel: _Optional[_Union[_logs_panel_pb2.LogsPanel, _Mapping]]=..., incident_list: _Optional[_Union[_incident_list_pb2.IncidentList, _Mapping]]=..., pie_chart: _Optional[_Union[_piechart_pb2.PieChart, _Mapping]]=..., error_reporting_panel: _Optional[_Union[_error_reporting_panel_pb2.ErrorReportingPanel, _Mapping]]=..., section_header: _Optional[_Union[_section_header_pb2.SectionHeader, _Mapping]]=..., single_view_group: _Optional[_Union[_single_view_group_pb2.SingleViewGroup, _Mapping]]=..., id: _Optional[str]=...) -> None:
        ...