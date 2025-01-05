"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/deployed_model_ref.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1/deployed_model_ref.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"p\n\x10DeployedModelRef\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x05\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12\x1e\n\x11deployed_model_id\x18\x02 \x01(\tB\x03\xe0A\x05B\xd4\x01\n\x1ecom.google.cloud.aiplatform.v1B\x16DeployedModelNameProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.deployed_model_ref_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x16DeployedModelNameProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_DEPLOYEDMODELREF'].fields_by_name['endpoint']._loaded_options = None
    _globals['_DEPLOYEDMODELREF'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x05\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_DEPLOYEDMODELREF'].fields_by_name['deployed_model_id']._loaded_options = None
    _globals['_DEPLOYEDMODELREF'].fields_by_name['deployed_model_id']._serialized_options = b'\xe0A\x05'
    _globals['_DEPLOYEDMODELREF']._serialized_start = 143
    _globals['_DEPLOYEDMODELREF']._serialized_end = 255