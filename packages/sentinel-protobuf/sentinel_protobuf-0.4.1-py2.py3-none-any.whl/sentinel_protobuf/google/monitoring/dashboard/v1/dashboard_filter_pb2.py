"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/dashboard_filter.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/monitoring/dashboard/v1/dashboard_filter.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto"\xcf\x02\n\x0fDashboardFilter\x12\x16\n\tlabel_key\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x11template_variable\x18\x03 \x01(\t\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x12O\n\x0bfilter_type\x18\x05 \x01(\x0e2:.google.monitoring.dashboard.v1.DashboardFilter.FilterType"\x8e\x01\n\nFilterType\x12\x1b\n\x17FILTER_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eRESOURCE_LABEL\x10\x01\x12\x10\n\x0cMETRIC_LABEL\x10\x02\x12\x17\n\x13USER_METADATA_LABEL\x10\x03\x12\x19\n\x15SYSTEM_METADATA_LABEL\x10\x04\x12\t\n\x05GROUP\x10\x05B\x0f\n\rdefault_valueB\xfd\x01\n"com.google.monitoring.dashboard.v1B\x14DashboardFilterProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.dashboard_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x14DashboardFilterProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_DASHBOARDFILTER'].fields_by_name['label_key']._loaded_options = None
    _globals['_DASHBOARDFILTER'].fields_by_name['label_key']._serialized_options = b'\xe0A\x02'
    _globals['_DASHBOARDFILTER']._serialized_start = 123
    _globals['_DASHBOARDFILTER']._serialized_end = 458
    _globals['_DASHBOARDFILTER_FILTERTYPE']._serialized_start = 299
    _globals['_DASHBOARDFILTER_FILTERTYPE']._serialized_end = 441