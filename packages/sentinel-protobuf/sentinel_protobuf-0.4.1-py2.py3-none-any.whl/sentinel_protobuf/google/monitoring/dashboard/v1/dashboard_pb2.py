"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/dashboard.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.monitoring.dashboard.v1 import dashboard_filter_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_dashboard__filter__pb2
from .....google.monitoring.dashboard.v1 import layouts_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_layouts__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/monitoring/dashboard/v1/dashboard.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/monitoring/dashboard/v1/dashboard_filter.proto\x1a,google/monitoring/dashboard/v1/layouts.proto"\xfa\x04\n\tDashboard\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04etag\x18\x04 \x01(\t\x12A\n\x0bgrid_layout\x18\x05 \x01(\x0b2*.google.monitoring.dashboard.v1.GridLayoutH\x00\x12E\n\rmosaic_layout\x18\x06 \x01(\x0b2,.google.monitoring.dashboard.v1.MosaicLayoutH\x00\x12?\n\nrow_layout\x18\x08 \x01(\x0b2).google.monitoring.dashboard.v1.RowLayoutH\x00\x12E\n\rcolumn_layout\x18\t \x01(\x0b2,.google.monitoring.dashboard.v1.ColumnLayoutH\x00\x12J\n\x11dashboard_filters\x18\x0b \x03(\x0b2/.google.monitoring.dashboard.v1.DashboardFilter\x12E\n\x06labels\x18\x0c \x03(\x0b25.google.monitoring.dashboard.v1.Dashboard.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:S\xeaAP\n#monitoring.googleapis.com/Dashboard\x12)projects/{project}/dashboards/{dashboard}B\x08\n\x06layoutB\xf8\x01\n"com.google.monitoring.dashboard.v1B\x0fDashboardsProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.dashboard_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x0fDashboardsProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_DASHBOARD_LABELSENTRY']._loaded_options = None
    _globals['_DASHBOARD_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DASHBOARD'].fields_by_name['name']._loaded_options = None
    _globals['_DASHBOARD'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_DASHBOARD'].fields_by_name['display_name']._loaded_options = None
    _globals['_DASHBOARD'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DASHBOARD']._loaded_options = None
    _globals['_DASHBOARD']._serialized_options = b'\xeaAP\n#monitoring.googleapis.com/Dashboard\x12)projects/{project}/dashboards/{dashboard}'
    _globals['_DASHBOARD']._serialized_start = 244
    _globals['_DASHBOARD']._serialized_end = 878
    _globals['_DASHBOARD_LABELSENTRY']._serialized_start = 738
    _globals['_DASHBOARD_LABELSENTRY']._serialized_end = 783