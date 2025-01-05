"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/dashboards_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.monitoring.dashboard.v1 import dashboard_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_dashboard__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/monitoring/dashboard/v1/dashboards_service.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/monitoring/dashboard/v1/dashboard.proto\x1a\x1bgoogle/protobuf/empty.proto"\xb7\x01\n\x16CreateDashboardRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12A\n\tdashboard\x18\x02 \x01(\x0b2).google.monitoring.dashboard.v1.DashboardB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"\x88\x01\n\x15ListDashboardsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"p\n\x16ListDashboardsResponse\x12=\n\ndashboards\x18\x01 \x03(\x0b2).google.monitoring.dashboard.v1.Dashboard\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"P\n\x13GetDashboardRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#monitoring.googleapis.com/Dashboard"S\n\x16DeleteDashboardRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#monitoring.googleapis.com/Dashboard"r\n\x16UpdateDashboardRequest\x12A\n\tdashboard\x18\x01 \x01(\x0b2).google.monitoring.dashboard.v1.DashboardB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x082\xdb\x08\n\x11DashboardsService\x12\xbe\x01\n\x0fCreateDashboard\x126.google.monitoring.dashboard.v1.CreateDashboardRequest\x1a).google.monitoring.dashboard.v1.Dashboard"H\xdaA\x10parent,dashboard\x82\xd3\xe4\x93\x02/""/v1/{parent=projects/*}/dashboards:\tdashboard\x12\xb4\x01\n\x0eListDashboards\x125.google.monitoring.dashboard.v1.ListDashboardsRequest\x1a6.google.monitoring.dashboard.v1.ListDashboardsResponse"3\xdaA\x06parent\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=projects/*}/dashboards\x12\xa1\x01\n\x0cGetDashboard\x123.google.monitoring.dashboard.v1.GetDashboardRequest\x1a).google.monitoring.dashboard.v1.Dashboard"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=projects/*/dashboards/*}\x12\x94\x01\n\x0fDeleteDashboard\x126.google.monitoring.dashboard.v1.DeleteDashboardRequest\x1a\x16.google.protobuf.Empty"1\xdaA\x04name\x82\xd3\xe4\x93\x02$*"/v1/{name=projects/*/dashboards/*}\x12\xb5\x01\n\x0fUpdateDashboard\x126.google.monitoring.dashboard.v1.UpdateDashboardRequest\x1a).google.monitoring.dashboard.v1.Dashboard"?\x82\xd3\xe4\x93\x0292,/v1/{dashboard.name=projects/*/dashboards/*}:\tdashboard\x1a\xda\x01\xcaA\x19monitoring.googleapis.com\xd2A\xba\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read,https://www.googleapis.com/auth/monitoring.writeB\xff\x01\n"com.google.monitoring.dashboard.v1B\x16DashboardsServiceProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.dashboards_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x16DashboardsServiceProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['dashboard']._loaded_options = None
    _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['dashboard']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETDASHBOARDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDASHBOARDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#monitoring.googleapis.com/Dashboard'
    _globals['_DELETEDASHBOARDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDASHBOARDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#monitoring.googleapis.com/Dashboard'
    _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['dashboard']._loaded_options = None
    _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['dashboard']._serialized_options = b'\xe0A\x02'
    _globals['_DASHBOARDSSERVICE']._loaded_options = None
    _globals['_DASHBOARDSSERVICE']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\xba\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read,https://www.googleapis.com/auth/monitoring.write'
    _globals['_DASHBOARDSSERVICE'].methods_by_name['CreateDashboard']._loaded_options = None
    _globals['_DASHBOARDSSERVICE'].methods_by_name['CreateDashboard']._serialized_options = b'\xdaA\x10parent,dashboard\x82\xd3\xe4\x93\x02/""/v1/{parent=projects/*}/dashboards:\tdashboard'
    _globals['_DASHBOARDSSERVICE'].methods_by_name['ListDashboards']._loaded_options = None
    _globals['_DASHBOARDSSERVICE'].methods_by_name['ListDashboards']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=projects/*}/dashboards'
    _globals['_DASHBOARDSSERVICE'].methods_by_name['GetDashboard']._loaded_options = None
    _globals['_DASHBOARDSSERVICE'].methods_by_name['GetDashboard']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=projects/*/dashboards/*}'
    _globals['_DASHBOARDSSERVICE'].methods_by_name['DeleteDashboard']._loaded_options = None
    _globals['_DASHBOARDSSERVICE'].methods_by_name['DeleteDashboard']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$*"/v1/{name=projects/*/dashboards/*}'
    _globals['_DASHBOARDSSERVICE'].methods_by_name['UpdateDashboard']._loaded_options = None
    _globals['_DASHBOARDSSERVICE'].methods_by_name['UpdateDashboard']._serialized_options = b'\x82\xd3\xe4\x93\x0292,/v1/{dashboard.name=projects/*/dashboards/*}:\tdashboard'
    _globals['_CREATEDASHBOARDREQUEST']._serialized_start = 284
    _globals['_CREATEDASHBOARDREQUEST']._serialized_end = 467
    _globals['_LISTDASHBOARDSREQUEST']._serialized_start = 470
    _globals['_LISTDASHBOARDSREQUEST']._serialized_end = 606
    _globals['_LISTDASHBOARDSRESPONSE']._serialized_start = 608
    _globals['_LISTDASHBOARDSRESPONSE']._serialized_end = 720
    _globals['_GETDASHBOARDREQUEST']._serialized_start = 722
    _globals['_GETDASHBOARDREQUEST']._serialized_end = 802
    _globals['_DELETEDASHBOARDREQUEST']._serialized_start = 804
    _globals['_DELETEDASHBOARDREQUEST']._serialized_end = 887
    _globals['_UPDATEDASHBOARDREQUEST']._serialized_start = 889
    _globals['_UPDATEDASHBOARDREQUEST']._serialized_end = 1003
    _globals['_DASHBOARDSSERVICE']._serialized_start = 1006
    _globals['_DASHBOARDSSERVICE']._serialized_end = 2121