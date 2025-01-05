"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1/health_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/visionai/v1/health_service.proto\x12\x18google.cloud.visionai.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto"K\n\x12HealthCheckRequest\x125\n\x07cluster\x18\x01 \x01(\tB$\xfaA!\n\x1fvisionai.googleapis.com/Cluster"s\n\x13HealthCheckResponse\x12\x0f\n\x07healthy\x18\x01 \x01(\x08\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12;\n\x0ccluster_info\x18\x03 \x01(\x0b2%.google.cloud.visionai.v1.ClusterInfo"=\n\x0bClusterInfo\x12\x15\n\rstreams_count\x18\x01 \x01(\x05\x12\x17\n\x0fprocesses_count\x18\x02 \x01(\x052\x93\x02\n\x12HealthCheckService\x12\xaf\x01\n\x0bHealthCheck\x12,.google.cloud.visionai.v1.HealthCheckRequest\x1a-.google.cloud.visionai.v1.HealthCheckResponse"C\x82\xd3\xe4\x93\x02=\x12;/v1/{cluster=projects/*/locations/*/clusters/*}:healthCheck\x1aK\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc7\x01\n\x1ccom.google.cloud.visionai.v1B\x17HealthCheckServiceProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1.health_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.visionai.v1B\x17HealthCheckServiceProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1'
    _globals['_HEALTHCHECKREQUEST'].fields_by_name['cluster']._loaded_options = None
    _globals['_HEALTHCHECKREQUEST'].fields_by_name['cluster']._serialized_options = b'\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_HEALTHCHECKSERVICE']._loaded_options = None
    _globals['_HEALTHCHECKSERVICE']._serialized_options = b'\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_HEALTHCHECKSERVICE'].methods_by_name['HealthCheck']._loaded_options = None
    _globals['_HEALTHCHECKSERVICE'].methods_by_name['HealthCheck']._serialized_options = b'\x82\xd3\xe4\x93\x02=\x12;/v1/{cluster=projects/*/locations/*/clusters/*}:healthCheck'
    _globals['_HEALTHCHECKREQUEST']._serialized_start = 157
    _globals['_HEALTHCHECKREQUEST']._serialized_end = 232
    _globals['_HEALTHCHECKRESPONSE']._serialized_start = 234
    _globals['_HEALTHCHECKRESPONSE']._serialized_end = 349
    _globals['_CLUSTERINFO']._serialized_start = 351
    _globals['_CLUSTERINFO']._serialized_end = 412
    _globals['_HEALTHCHECKSERVICE']._serialized_start = 415
    _globals['_HEALTHCHECKSERVICE']._serialized_end = 690