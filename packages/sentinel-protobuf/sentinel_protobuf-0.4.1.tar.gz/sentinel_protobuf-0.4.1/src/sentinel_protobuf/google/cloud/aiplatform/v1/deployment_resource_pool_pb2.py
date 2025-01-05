"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/deployment_resource_pool.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_machine__resources__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1/deployment_resource_pool.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a2google/cloud/aiplatform/v1/machine_resources.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x81\x04\n\x16DeploymentResourcePool\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12P\n\x13dedicated_resources\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1.DedicatedResourcesB\x03\xe0A\x02\x12C\n\x0fencryption_spec\x18\x05 \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpec\x12\x17\n\x0fservice_account\x18\x06 \x01(\t\x12!\n\x19disable_container_logging\x18\x07 \x01(\x08\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x08 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\t \x01(\x08B\x03\xe0A\x03:\x92\x01\xeaA\x8e\x01\n0aiplatform.googleapis.com/DeploymentResourcePool\x12Zprojects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}B\xd9\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1bDeploymentResourcePoolProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.deployment_resource_pool_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1bDeploymentResourcePoolProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['name']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['dedicated_resources']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['dedicated_resources']._serialized_options = b'\xe0A\x02'
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['create_time']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOL'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYMENTRESOURCEPOOL']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOL']._serialized_options = b'\xeaA\x8e\x01\n0aiplatform.googleapis.com/DeploymentResourcePool\x12Zprojects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}'
    _globals['_DEPLOYMENTRESOURCEPOOL']._serialized_start = 285
    _globals['_DEPLOYMENTRESOURCEPOOL']._serialized_end = 798