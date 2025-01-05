"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2alpha/analytics_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import export_config_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_export__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/retail/v2alpha/analytics_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/retail/v2alpha/export_config.proto\x1a#google/longrunning/operations.proto2\x97\x03\n\x10AnalyticsService\x12\xb7\x02\n\x16ExportAnalyticsMetrics\x12:.google.cloud.retail.v2alpha.ExportAnalyticsMetricsRequest\x1a\x1d.google.longrunning.Operation"\xc1\x01\xcaAh\n:google.cloud.retail.v2alpha.ExportAnalyticsMetricsResponse\x12*google.cloud.retail.v2alpha.ExportMetadata\x82\xd3\xe4\x93\x02P"K/v2alpha/{catalog=projects/*/locations/*/catalogs/*}:exportAnalyticsMetrics:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd9\x01\n\x1fcom.google.cloud.retail.v2alphaB\x15AnalyticsServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.analytics_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x15AnalyticsServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_ANALYTICSSERVICE']._loaded_options = None
    _globals['_ANALYTICSSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ANALYTICSSERVICE'].methods_by_name['ExportAnalyticsMetrics']._loaded_options = None
    _globals['_ANALYTICSSERVICE'].methods_by_name['ExportAnalyticsMetrics']._serialized_options = b'\xcaAh\n:google.cloud.retail.v2alpha.ExportAnalyticsMetricsResponse\x12*google.cloud.retail.v2alpha.ExportMetadata\x82\xd3\xe4\x93\x02P"K/v2alpha/{catalog=projects/*/locations/*/catalogs/*}:exportAnalyticsMetrics:\x01*'
    _globals['_ANALYTICSSERVICE']._serialized_start = 286
    _globals['_ANALYTICSSERVICE']._serialized_end = 693