"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1/project_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import project_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_project__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/discoveryengine/v1/project_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/discoveryengine/v1/project.proto\x1a#google/longrunning/operations.proto"\xa0\x01\n\x17ProvisionProjectRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Project\x12"\n\x15accept_data_use_terms\x18\x02 \x01(\x08B\x03\xe0A\x02\x12#\n\x16data_use_terms_version\x18\x03 \x01(\tB\x03\xe0A\x02"\x1a\n\x18ProvisionProjectMetadata2\xec\x02\n\x0eProjectService\x12\x85\x02\n\x10ProvisionProject\x128.google.cloud.discoveryengine.v1.ProvisionProjectRequest\x1a\x1d.google.longrunning.Operation"\x97\x01\xcaAc\n\'google.cloud.discoveryengine.v1.Project\x128google.cloud.discoveryengine.v1.ProvisionProjectMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02$"\x1f/v1/{name=projects/*}:provision:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x86\x02\n#com.google.cloud.discoveryengine.v1B\x13ProjectServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.project_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x13ProjectServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Project'
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['accept_data_use_terms']._loaded_options = None
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['accept_data_use_terms']._serialized_options = b'\xe0A\x02'
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['data_use_terms_version']._loaded_options = None
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['data_use_terms_version']._serialized_options = b'\xe0A\x02'
    _globals['_PROJECTSERVICE']._loaded_options = None
    _globals['_PROJECTSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PROJECTSERVICE'].methods_by_name['ProvisionProject']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['ProvisionProject']._serialized_options = b'\xcaAc\n\'google.cloud.discoveryengine.v1.Project\x128google.cloud.discoveryengine.v1.ProvisionProjectMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02$"\x1f/v1/{name=projects/*}:provision:\x01*'
    _globals['_PROVISIONPROJECTREQUEST']._serialized_start = 290
    _globals['_PROVISIONPROJECTREQUEST']._serialized_end = 450
    _globals['_PROVISIONPROJECTMETADATA']._serialized_start = 452
    _globals['_PROVISIONPROJECTMETADATA']._serialized_end = 478
    _globals['_PROJECTSERVICE']._serialized_start = 481
    _globals['_PROJECTSERVICE']._serialized_end = 845