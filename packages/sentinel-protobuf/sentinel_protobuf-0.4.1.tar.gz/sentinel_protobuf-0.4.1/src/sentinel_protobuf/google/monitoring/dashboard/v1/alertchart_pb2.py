"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/alertchart.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/monitoring/dashboard/v1/alertchart.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"|\n\nAlertChart\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02:[\xeaAX\n%monitoring.googleapis.com/AlertPolicy\x12/projects/{project}/alertPolicies/{alert_policy}B\xf8\x01\n"com.google.monitoring.dashboard.v1B\x0fAlertChartProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.alertchart_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x0fAlertChartProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_ALERTCHART'].fields_by_name['name']._loaded_options = None
    _globals['_ALERTCHART'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTCHART']._loaded_options = None
    _globals['_ALERTCHART']._serialized_options = b'\xeaAX\n%monitoring.googleapis.com/AlertPolicy\x12/projects/{project}/alertPolicies/{alert_policy}'
    _globals['_ALERTCHART']._serialized_start = 143
    _globals['_ALERTCHART']._serialized_end = 267