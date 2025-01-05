"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/deploy/v1/automation_payload.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.deploy.v1 import log_enums_pb2 as google_dot_cloud_dot_deploy_dot_v1_dot_log__enums__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/deploy/v1/automation_payload.proto\x12\x16google.cloud.deploy.v1\x1a&google/cloud/deploy/v1/log_enums.proto"x\n\x0fAutomationEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x12\n\nautomation\x18\x02 \x01(\t\x12\x14\n\x0cpipeline_uid\x18\x03 \x01(\t\x12*\n\x04type\x18\x04 \x01(\x0e2\x1c.google.cloud.deploy.v1.TypeBj\n\x1acom.google.cloud.deploy.v1B\x16AutomationPayloadProtoP\x01Z2cloud.google.com/go/deploy/apiv1/deploypb;deploypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.deploy.v1.automation_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.deploy.v1B\x16AutomationPayloadProtoP\x01Z2cloud.google.com/go/deploy/apiv1/deploypb;deploypb'
    _globals['_AUTOMATIONEVENT']._serialized_start = 115
    _globals['_AUTOMATIONEVENT']._serialized_end = 235