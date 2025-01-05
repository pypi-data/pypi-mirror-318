"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/saasaccelerator/management/logs/v1/notification_service_payload.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nRgoogle/cloud/saasaccelerator/management/logs/v1/notification_service_payload.proto\x12/google.cloud.saasaccelerator.management.logs.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xa2\x03\n\x11NotificationStage\x12W\n\x05stage\x18\x01 \x01(\x0e2H.google.cloud.saasaccelerator.management.logs.v1.NotificationStage.Stage\x12.\n\nevent_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fnotification_id\x18\x03 \x01(\t\x12W\n\x05event\x18\x04 \x01(\x0e2H.google.cloud.saasaccelerator.management.logs.v1.NotificationStage.Event\x12\x0f\n\x07message\x18\x05 \x01(\t"G\n\x05Stage\x12\x15\n\x11STAGE_UNSPECIFIED\x10\x00\x12\x08\n\x04SENT\x10\x01\x12\x10\n\x0cSEND_FAILURE\x10\x02\x12\x0b\n\x07DROPPED\x10\x03"8\n\x05Event\x12\x15\n\x11EVENT_UNSPECIFIED\x10\x00\x12\x18\n\x14HEALTH_STATUS_CHANGE\x10\x01B\xa1\x01\n3com.google.cloud.saasaccelerator.management.logs.v1B\x1fNotificationServicePayloadProtoP\x01ZGcloud.google.com/go/saasaccelerator/management/logs/apiv1/logspb;logspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.saasaccelerator.management.logs.v1.notification_service_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n3com.google.cloud.saasaccelerator.management.logs.v1B\x1fNotificationServicePayloadProtoP\x01ZGcloud.google.com/go/saasaccelerator/management/logs/apiv1/logspb;logspb'
    _globals['_NOTIFICATIONSTAGE']._serialized_start = 169
    _globals['_NOTIFICATIONSTAGE']._serialized_end = 587
    _globals['_NOTIFICATIONSTAGE_STAGE']._serialized_start = 458
    _globals['_NOTIFICATIONSTAGE_STAGE']._serialized_end = 529
    _globals['_NOTIFICATIONSTAGE_EVENT']._serialized_start = 531
    _globals['_NOTIFICATIONSTAGE_EVENT']._serialized_end = 587