"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/secretmanager/logging/v1/secret_event.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/secretmanager/logging/v1/secret_event.proto\x12%google.cloud.secretmanager.logging.v1"\xd9\x02\n\x0bSecretEvent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12J\n\x04type\x18\x02 \x01(\x0e2<.google.cloud.secretmanager.logging.v1.SecretEvent.EventType\x12\x13\n\x0blog_message\x18\x03 \x01(\t"\xda\x01\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12EXPIRES_IN_30_DAYS\x10\x01\x12\x15\n\x11EXPIRES_IN_7_DAYS\x10\x02\x12\x14\n\x10EXPIRES_IN_1_DAY\x10\x03\x12\x16\n\x12EXPIRES_IN_6_HOURS\x10\x04\x12\x15\n\x11EXPIRES_IN_1_HOUR\x10\x05\x12\x0b\n\x07EXPIRED\x10\x06\x12\x13\n\x0fTOPIC_NOT_FOUND\x10\x07\x12\x1b\n\x17TOPIC_PERMISSION_DENIED\x10\x08B\x80\x02\n)com.google.cloud.secretmanager.logging.v1B\x10SecretEventProtoP\x01ZCcloud.google.com/go/secretmanager/logging/apiv1/loggingpb;loggingpb\xaa\x02%Google.Cloud.SecretManager.Logging.V1\xca\x02%Google\\Cloud\\SecretManager\\Logging\\V1\xea\x02)Google::Cloud::SecretManager::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.secretmanager.logging.v1.secret_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.secretmanager.logging.v1B\x10SecretEventProtoP\x01ZCcloud.google.com/go/secretmanager/logging/apiv1/loggingpb;loggingpb\xaa\x02%Google.Cloud.SecretManager.Logging.V1\xca\x02%Google\\Cloud\\SecretManager\\Logging\\V1\xea\x02)Google::Cloud::SecretManager::Logging::V1'
    _globals['_SECRETEVENT']._serialized_start = 100
    _globals['_SECRETEVENT']._serialized_end = 445
    _globals['_SECRETEVENT_EVENTTYPE']._serialized_start = 227
    _globals['_SECRETEVENT_EVENTTYPE']._serialized_end = 445