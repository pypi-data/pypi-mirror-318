"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/query_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.monitoring.v3 import metric_service_pb2 as google_dot_monitoring_dot_v3_dot_metric__service__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/monitoring/v3/query_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a)google/monitoring/v3/metric_service.proto2\xe1\x02\n\x0cQueryService\x12\xa4\x01\n\x0fQueryTimeSeries\x12,.google.monitoring.v3.QueryTimeSeriesRequest\x1a-.google.monitoring.v3.QueryTimeSeriesResponse"4\x88\x02\x01\x82\xd3\xe4\x93\x02+"&/v3/{name=projects/*}/timeSeries:query:\x01*\x1a\xa9\x01\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.readB\xcc\x01\n\x18com.google.monitoring.v3B\x11QueryServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.query_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x11QueryServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_QUERYSERVICE']._loaded_options = None
    _globals['_QUERYSERVICE']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read'
    _globals['_QUERYSERVICE'].methods_by_name['QueryTimeSeries']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryTimeSeries']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02+"&/v3/{name=projects/*}/timeSeries:query:\x01*'
    _globals['_QUERYSERVICE']._serialized_start = 165
    _globals['_QUERYSERVICE']._serialized_end = 518