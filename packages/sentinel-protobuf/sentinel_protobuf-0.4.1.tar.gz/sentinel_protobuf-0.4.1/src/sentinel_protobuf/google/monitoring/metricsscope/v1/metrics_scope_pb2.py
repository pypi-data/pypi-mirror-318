"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/metricsscope/v1/metrics_scope.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/monitoring/metricsscope/v1/metrics_scope.proto\x12!google.monitoring.metricsscope.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbf\x02\n\x0cMetricsScope\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12T\n\x12monitored_projects\x18\x04 \x03(\x0b23.google.monitoring.metricsscope.v1.MonitoredProjectB\x03\xe0A\x03:Z\xeaAW\n&monitoring.googleapis.com/MetricsScope\x12-locations/global/metricsScope/{metrics_scope}"\xcf\x01\n\x10MonitoredProject\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:r\xeaAo\n*monitoring.googleapis.com/MonitoredProject\x12Alocations/global/metricsScopes/{metrics_scope}/projects/{project}B\x8f\x02\n%com.google.monitoring.metricsscope.v1B\x11MetricsScopeProtoP\x01ZOcloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb;metricsscopepb\xaa\x02\'Google.Cloud.Monitoring.MetricsScope.V1\xca\x02\'Google\\Cloud\\Monitoring\\MetricsScope\\V1\xea\x02+Google::Cloud::Monitoring::MetricsScope::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.metricsscope.v1.metrics_scope_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n%com.google.monitoring.metricsscope.v1B\x11MetricsScopeProtoP\x01ZOcloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb;metricsscopepb\xaa\x02'Google.Cloud.Monitoring.MetricsScope.V1\xca\x02'Google\\Cloud\\Monitoring\\MetricsScope\\V1\xea\x02+Google::Cloud::Monitoring::MetricsScope::V1"
    _globals['_METRICSSCOPE'].fields_by_name['name']._loaded_options = None
    _globals['_METRICSSCOPE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_METRICSSCOPE'].fields_by_name['create_time']._loaded_options = None
    _globals['_METRICSSCOPE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_METRICSSCOPE'].fields_by_name['update_time']._loaded_options = None
    _globals['_METRICSSCOPE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_METRICSSCOPE'].fields_by_name['monitored_projects']._loaded_options = None
    _globals['_METRICSSCOPE'].fields_by_name['monitored_projects']._serialized_options = b'\xe0A\x03'
    _globals['_METRICSSCOPE']._loaded_options = None
    _globals['_METRICSSCOPE']._serialized_options = b'\xeaAW\n&monitoring.googleapis.com/MetricsScope\x12-locations/global/metricsScope/{metrics_scope}'
    _globals['_MONITOREDPROJECT'].fields_by_name['name']._loaded_options = None
    _globals['_MONITOREDPROJECT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_MONITOREDPROJECT'].fields_by_name['create_time']._loaded_options = None
    _globals['_MONITOREDPROJECT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MONITOREDPROJECT']._loaded_options = None
    _globals['_MONITOREDPROJECT']._serialized_options = b'\xeaAo\n*monitoring.googleapis.com/MonitoredProject\x12Alocations/global/metricsScopes/{metrics_scope}/projects/{project}'
    _globals['_METRICSSCOPE']._serialized_start = 186
    _globals['_METRICSSCOPE']._serialized_end = 505
    _globals['_MONITOREDPROJECT']._serialized_start = 508
    _globals['_MONITOREDPROJECT']._serialized_end = 715