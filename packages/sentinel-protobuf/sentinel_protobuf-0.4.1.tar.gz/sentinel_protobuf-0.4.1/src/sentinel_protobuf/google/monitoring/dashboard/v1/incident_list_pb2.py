"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/incident_list.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/monitoring/dashboard/v1/incident_list.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/api/monitored_resource.proto"j\n\x0cIncidentList\x12?\n\x13monitored_resources\x18\x01 \x03(\x0b2\x1d.google.api.MonitoredResourceB\x03\xe0A\x01\x12\x19\n\x0cpolicy_names\x18\x02 \x03(\tB\x03\xe0A\x01B\xfa\x01\n"com.google.monitoring.dashboard.v1B\x11IncidentListProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.incident_list_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x11IncidentListProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_INCIDENTLIST'].fields_by_name['monitored_resources']._loaded_options = None
    _globals['_INCIDENTLIST'].fields_by_name['monitored_resources']._serialized_options = b'\xe0A\x01'
    _globals['_INCIDENTLIST'].fields_by_name['policy_names']._loaded_options = None
    _globals['_INCIDENTLIST'].fields_by_name['policy_names']._serialized_options = b'\xe0A\x01'
    _globals['_INCIDENTLIST']._serialized_start = 156
    _globals['_INCIDENTLIST']._serialized_end = 262