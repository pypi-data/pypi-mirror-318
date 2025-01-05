"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/service_networking.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1/service_networking.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"D\n\x13PSCAutomationConfig\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07network\x18\x02 \x01(\tB\x03\xe0A\x02"\x86\x01\n\x1bPrivateServiceConnectConfig\x12+\n\x1eenable_private_service_connect\x18\x01 \x01(\x08B\x03\xe0A\x02\x12\x19\n\x11project_allowlist\x18\x02 \x03(\t\x12\x1f\n\x12service_attachment\x18\x05 \x01(\tB\x03\xe0A\x03"S\n\x15PscAutomatedEndpoints\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07network\x18\x02 \x01(\t\x12\x15\n\rmatch_address\x18\x03 \x01(\tB\xcd\x02\n\x1ecom.google.cloud.aiplatform.v1B\x16ServiceNetworkingProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAv\n(compute.googleapis.com/NetworkAttachment\x12Jprojects/{project}/regions/{region}/networkAttachments/{networkattachment}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.service_networking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x16ServiceNetworkingProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAv\n(compute.googleapis.com/NetworkAttachment\x12Jprojects/{project}/regions/{region}/networkAttachments/{networkattachment}'
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['project_id']._loaded_options = None
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['network']._loaded_options = None
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['network']._serialized_options = b'\xe0A\x02'
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['enable_private_service_connect']._loaded_options = None
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['enable_private_service_connect']._serialized_options = b'\xe0A\x02'
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['service_attachment']._loaded_options = None
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['service_attachment']._serialized_options = b'\xe0A\x03'
    _globals['_PSCAUTOMATIONCONFIG']._serialized_start = 143
    _globals['_PSCAUTOMATIONCONFIG']._serialized_end = 211
    _globals['_PRIVATESERVICECONNECTCONFIG']._serialized_start = 214
    _globals['_PRIVATESERVICECONNECTCONFIG']._serialized_end = 348
    _globals['_PSCAUTOMATEDENDPOINTS']._serialized_start = 350
    _globals['_PSCAUTOMATEDENDPOINTS']._serialized_end = 433