"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chat/logging/v1/chat_app_log_entry.proto')
_sym_db = _symbol_database.Default()
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/chat/logging/v1/chat_app_log_entry.proto\x12\x16google.chat.logging.v1\x1a\x17google/rpc/status.proto"e\n\x0fChatAppLogEntry\x12\x12\n\ndeployment\x18\x01 \x01(\t\x12!\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x12\x1b\n\x13deployment_function\x18\x03 \x01(\tBp\n\x1acom.google.chat.logging.v1B\x14ChatAppLogEntryProtoP\x01Z:cloud.google.com/go/chat/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.logging.v1.chat_app_log_entry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.chat.logging.v1B\x14ChatAppLogEntryProtoP\x01Z:cloud.google.com/go/chat/logging/apiv1/loggingpb;loggingpb'
    _globals['_CHATAPPLOGENTRY']._serialized_start = 100
    _globals['_CHATAPPLOGENTRY']._serialized_end = 201