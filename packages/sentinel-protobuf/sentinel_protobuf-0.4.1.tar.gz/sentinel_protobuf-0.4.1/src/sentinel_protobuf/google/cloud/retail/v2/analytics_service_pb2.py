"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2/analytics_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2 import export_config_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_export__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/retail/v2/analytics_service.proto\x12\x16google.cloud.retail.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/retail/v2/export_config.proto\x1a#google/longrunning/operations.proto2\x83\x03\n\x10AnalyticsService\x12\xa3\x02\n\x16ExportAnalyticsMetrics\x125.google.cloud.retail.v2.ExportAnalyticsMetricsRequest\x1a\x1d.google.longrunning.Operation"\xb2\x01\xcaA^\n5google.cloud.retail.v2.ExportAnalyticsMetricsResponse\x12%google.cloud.retail.v2.ExportMetadata\x82\xd3\xe4\x93\x02K"F/v2/{catalog=projects/*/locations/*/catalogs/*}:exportAnalyticsMetrics:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc0\x01\n\x1acom.google.cloud.retail.v2B\x15AnalyticsServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.analytics_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x15AnalyticsServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
    _globals['_ANALYTICSSERVICE']._loaded_options = None
    _globals['_ANALYTICSSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ANALYTICSSERVICE'].methods_by_name['ExportAnalyticsMetrics']._loaded_options = None
    _globals['_ANALYTICSSERVICE'].methods_by_name['ExportAnalyticsMetrics']._serialized_options = b'\xcaA^\n5google.cloud.retail.v2.ExportAnalyticsMetricsResponse\x12%google.cloud.retail.v2.ExportMetadata\x82\xd3\xe4\x93\x02K"F/v2/{catalog=projects/*/locations/*/catalogs/*}:exportAnalyticsMetrics:\x01*'
    _globals['_ANALYTICSSERVICE']._serialized_start = 271
    _globals['_ANALYTICSSERVICE']._serialized_end = 658