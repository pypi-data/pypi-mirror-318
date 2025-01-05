"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/sensitiveaction/logging/v1/sensitive_action_payload.proto')
_sym_db = _symbol_database.Default()
from ......google.cloud.securitycenter.v1 import access_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_access__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/cloud/sensitiveaction/logging/v1/sensitive_action_payload.proto\x12\'google.cloud.sensitiveaction.logging.v1\x1a+google/cloud/securitycenter/v1/access.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa0\x03\n\x0fSensitiveAction\x12\x13\n\x0baction_type\x18\x01 \x01(\t\x12/\n\x0baction_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1a\n\x12affected_resources\x18\x03 \x03(\t\x12\\\n\x0esource_log_ids\x18\x04 \x03(\x0b2D.google.cloud.sensitiveaction.logging.v1.SensitiveAction.SourceLogId\x12\x16\n\x0elearn_more_uri\x18\x05 \x01(\t\x126\n\x06access\x18\x06 \x01(\x0b2&.google.cloud.securitycenter.v1.Access\x1a}\n\x0bSourceLogId\x12\x1a\n\x12resource_container\x18\x01 \x01(\t\x12,\n\x08log_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\tinsert_id\x18\x03 \x01(\t\x12\x11\n\tquery_uri\x18\x04 \x01(\tB\x95\x02\n+com.google.cloud.sensitiveaction.logging.v1B\x1bSensitiveActionPayloadProtoP\x01ZEcloud.google.com/go/sensitiveaction/logging/apiv1/loggingpb;loggingpb\xaa\x02\'Google.Cloud.SensitiveAction.Logging.V1\xca\x02\'Google\\Cloud\\SensitiveAction\\Logging\\V1\xea\x02+Google::Cloud::SensitiveAction::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sensitiveaction.logging.v1.sensitive_action_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.sensitiveaction.logging.v1B\x1bSensitiveActionPayloadProtoP\x01ZEcloud.google.com/go/sensitiveaction/logging/apiv1/loggingpb;loggingpb\xaa\x02'Google.Cloud.SensitiveAction.Logging.V1\xca\x02'Google\\Cloud\\SensitiveAction\\Logging\\V1\xea\x02+Google::Cloud::SensitiveAction::Logging::V1"
    _globals['_SENSITIVEACTION']._serialized_start = 194
    _globals['_SENSITIVEACTION']._serialized_end = 610
    _globals['_SENSITIVEACTION_SOURCELOGID']._serialized_start = 485
    _globals['_SENSITIVEACTION_SOURCELOGID']._serialized_end = 610