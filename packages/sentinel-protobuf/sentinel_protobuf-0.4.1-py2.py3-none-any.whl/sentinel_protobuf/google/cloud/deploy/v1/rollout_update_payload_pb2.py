"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/deploy/v1/rollout_update_payload.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.deploy.v1 import log_enums_pb2 as google_dot_cloud_dot_deploy_dot_v1_dot_log__enums__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/deploy/v1/rollout_update_payload.proto\x12\x16google.cloud.deploy.v1\x1a&google/cloud/deploy/v1/log_enums.proto"\x97\x04\n\x12RolloutUpdateEvent\x12\x0f\n\x07message\x18\x06 \x01(\t\x12\x14\n\x0cpipeline_uid\x18\x01 \x01(\t\x12\x13\n\x0brelease_uid\x18\x02 \x01(\t\x12\x0f\n\x07release\x18\x08 \x01(\t\x12\x0f\n\x07rollout\x18\x03 \x01(\t\x12\x11\n\ttarget_id\x18\x04 \x01(\t\x12*\n\x04type\x18\x07 \x01(\x0e2\x1c.google.cloud.deploy.v1.Type\x12Y\n\x13rollout_update_type\x18\x05 \x01(\x0e2<.google.cloud.deploy.v1.RolloutUpdateEvent.RolloutUpdateType"\x88\x02\n\x11RolloutUpdateType\x12#\n\x1fROLLOUT_UPDATE_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x13\n\x0fPENDING_RELEASE\x10\x02\x12\x0f\n\x0bIN_PROGRESS\x10\x03\x12\x0e\n\nCANCELLING\x10\x04\x12\r\n\tCANCELLED\x10\x05\x12\n\n\x06HALTED\x10\x06\x12\r\n\tSUCCEEDED\x10\x07\x12\n\n\x06FAILED\x10\x08\x12\x15\n\x11APPROVAL_REQUIRED\x10\t\x12\x0c\n\x08APPROVED\x10\n\x12\x0c\n\x08REJECTED\x10\x0b\x12\x14\n\x10ADVANCE_REQUIRED\x10\x0c\x12\x0c\n\x08ADVANCED\x10\rBm\n\x1acom.google.cloud.deploy.v1B\x19RolloutUpdatePayloadProtoP\x01Z2cloud.google.com/go/deploy/apiv1/deploypb;deploypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.deploy.v1.rollout_update_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.deploy.v1B\x19RolloutUpdatePayloadProtoP\x01Z2cloud.google.com/go/deploy/apiv1/deploypb;deploypb'
    _globals['_ROLLOUTUPDATEEVENT']._serialized_start = 120
    _globals['_ROLLOUTUPDATEEVENT']._serialized_end = 655
    _globals['_ROLLOUTUPDATEEVENT_ROLLOUTUPDATETYPE']._serialized_start = 391
    _globals['_ROLLOUTUPDATEEVENT_ROLLOUTUPDATETYPE']._serialized_end = 655