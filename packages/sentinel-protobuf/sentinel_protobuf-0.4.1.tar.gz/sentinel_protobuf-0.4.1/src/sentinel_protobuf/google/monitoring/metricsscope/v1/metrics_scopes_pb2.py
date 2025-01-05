"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/metricsscope/v1/metrics_scopes.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from .....google.monitoring.metricsscope.v1 import metrics_scope_pb2 as google_dot_monitoring_dot_metricsscope_dot_v1_dot_metrics__scope__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/monitoring/metricsscope/v1/metrics_scopes.proto\x12!google.monitoring.metricsscope.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a5google/monitoring/metricsscope/v1/metrics_scope.proto\x1a\x1fgoogle/protobuf/timestamp.proto"V\n\x16GetMetricsScopeRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&monitoring.googleapis.com/MetricsScope"W\n*ListMetricsScopesByMonitoredProjectRequest\x12)\n\x1cmonitored_resource_container\x18\x01 \x01(\tB\x03\xe0A\x02"v\n+ListMetricsScopesByMonitoredProjectResponse\x12G\n\x0emetrics_scopes\x18\x01 \x03(\x0b2/.google.monitoring.metricsscope.v1.MetricsScope"\xb4\x01\n\x1dCreateMonitoredProjectRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&monitoring.googleapis.com/MetricsScope\x12S\n\x11monitored_project\x18\x02 \x01(\x0b23.google.monitoring.metricsscope.v1.MonitoredProjectB\x03\xe0A\x02"a\n\x1dDeleteMonitoredProjectRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*monitoring.googleapis.com/MonitoredProject"\x93\x02\n\x11OperationMetadata\x12I\n\x05state\x18\x01 \x01(\x0e2:.google.monitoring.metricsscope.v1.OperationMetadata.State\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"Q\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07CREATED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04DONE\x10\x03\x12\r\n\tCANCELLED\x10\x042\xc2\t\n\rMetricsScopes\x12\xb9\x01\n\x0fGetMetricsScope\x129.google.monitoring.metricsscope.v1.GetMetricsScopeRequest\x1a/.google.monitoring.metricsscope.v1.MetricsScope":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=locations/global/metricsScopes/*}\x12\x94\x02\n#ListMetricsScopesByMonitoredProject\x12M.google.monitoring.metricsscope.v1.ListMetricsScopesByMonitoredProjectRequest\x1aN.google.monitoring.metricsscope.v1.ListMetricsScopesByMonitoredProjectResponse"N\x82\xd3\xe4\x93\x02H\x12F/v1/locations/global/metricsScopes:listMetricsScopesByMonitoredProject\x12\x90\x02\n\x16CreateMonitoredProject\x12@.google.monitoring.metricsscope.v1.CreateMonitoredProjectRequest\x1a\x1d.google.longrunning.Operation"\x94\x01\xcaA%\n\x10MonitoredProject\x12\x11OperationMetadata\xdaA\x18parent,monitored_project\x82\xd3\xe4\x93\x02K"6/v1/{parent=locations/global/metricsScopes/*}/projects:\x11monitored_project\x12\xed\x01\n\x16DeleteMonitoredProject\x12@.google.monitoring.metricsscope.v1.DeleteMonitoredProjectRequest\x1a\x1d.google.longrunning.Operation"r\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=locations/global/metricsScopes/*/projects/*}\x1a\xda\x01\xcaA\x19monitoring.googleapis.com\xd2A\xba\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read,https://www.googleapis.com/auth/monitoring.writeB\x90\x02\n%com.google.monitoring.metricsscope.v1B\x12MetricsScopesProtoP\x01ZOcloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb;metricsscopepb\xaa\x02\'Google.Cloud.Monitoring.MetricsScope.V1\xca\x02\'Google\\Cloud\\Monitoring\\MetricsScope\\V1\xea\x02+Google::Cloud::Monitoring::MetricsScope::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.metricsscope.v1.metrics_scopes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n%com.google.monitoring.metricsscope.v1B\x12MetricsScopesProtoP\x01ZOcloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb;metricsscopepb\xaa\x02'Google.Cloud.Monitoring.MetricsScope.V1\xca\x02'Google\\Cloud\\Monitoring\\MetricsScope\\V1\xea\x02+Google::Cloud::Monitoring::MetricsScope::V1"
    _globals['_GETMETRICSSCOPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMETRICSSCOPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&monitoring.googleapis.com/MetricsScope'
    _globals['_LISTMETRICSSCOPESBYMONITOREDPROJECTREQUEST'].fields_by_name['monitored_resource_container']._loaded_options = None
    _globals['_LISTMETRICSSCOPESBYMONITOREDPROJECTREQUEST'].fields_by_name['monitored_resource_container']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMONITOREDPROJECTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMONITOREDPROJECTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\n&monitoring.googleapis.com/MetricsScope'
    _globals['_CREATEMONITOREDPROJECTREQUEST'].fields_by_name['monitored_project']._loaded_options = None
    _globals['_CREATEMONITOREDPROJECTREQUEST'].fields_by_name['monitored_project']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEMONITOREDPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMONITOREDPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*monitoring.googleapis.com/MonitoredProject'
    _globals['_METRICSSCOPES']._loaded_options = None
    _globals['_METRICSSCOPES']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\xba\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read,https://www.googleapis.com/auth/monitoring.write'
    _globals['_METRICSSCOPES'].methods_by_name['GetMetricsScope']._loaded_options = None
    _globals['_METRICSSCOPES'].methods_by_name['GetMetricsScope']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=locations/global/metricsScopes/*}'
    _globals['_METRICSSCOPES'].methods_by_name['ListMetricsScopesByMonitoredProject']._loaded_options = None
    _globals['_METRICSSCOPES'].methods_by_name['ListMetricsScopesByMonitoredProject']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/v1/locations/global/metricsScopes:listMetricsScopesByMonitoredProject'
    _globals['_METRICSSCOPES'].methods_by_name['CreateMonitoredProject']._loaded_options = None
    _globals['_METRICSSCOPES'].methods_by_name['CreateMonitoredProject']._serialized_options = b'\xcaA%\n\x10MonitoredProject\x12\x11OperationMetadata\xdaA\x18parent,monitored_project\x82\xd3\xe4\x93\x02K"6/v1/{parent=locations/global/metricsScopes/*}/projects:\x11monitored_project'
    _globals['_METRICSSCOPES'].methods_by_name['DeleteMonitoredProject']._loaded_options = None
    _globals['_METRICSSCOPES'].methods_by_name['DeleteMonitoredProject']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=locations/global/metricsScopes/*/projects/*}'
    _globals['_GETMETRICSSCOPEREQUEST']._serialized_start = 333
    _globals['_GETMETRICSSCOPEREQUEST']._serialized_end = 419
    _globals['_LISTMETRICSSCOPESBYMONITOREDPROJECTREQUEST']._serialized_start = 421
    _globals['_LISTMETRICSSCOPESBYMONITOREDPROJECTREQUEST']._serialized_end = 508
    _globals['_LISTMETRICSSCOPESBYMONITOREDPROJECTRESPONSE']._serialized_start = 510
    _globals['_LISTMETRICSSCOPESBYMONITOREDPROJECTRESPONSE']._serialized_end = 628
    _globals['_CREATEMONITOREDPROJECTREQUEST']._serialized_start = 631
    _globals['_CREATEMONITOREDPROJECTREQUEST']._serialized_end = 811
    _globals['_DELETEMONITOREDPROJECTREQUEST']._serialized_start = 813
    _globals['_DELETEMONITOREDPROJECTREQUEST']._serialized_end = 910
    _globals['_OPERATIONMETADATA']._serialized_start = 913
    _globals['_OPERATIONMETADATA']._serialized_end = 1188
    _globals['_OPERATIONMETADATA_STATE']._serialized_start = 1107
    _globals['_OPERATIONMETADATA_STATE']._serialized_end = 1188
    _globals['_METRICSSCOPES']._serialized_start = 1191
    _globals['_METRICSSCOPES']._serialized_end = 2409