"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/stream/logging/v1/logging.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/stream/logging/v1/logging.proto\x12\x1egoogle.cloud.stream.logging.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xee\x01\n\x11OperationEventLog\x12F\n\nevent_type\x18\x01 \x01(\x0e22.google.cloud.stream.logging.v1.OperationEventType\x12.\n\nevent_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\toperation\x18\x03 \x01(\t\x12N\n\x13operation_artifacts\x18\x04 \x03(\x0b21.google.cloud.stream.logging.v1.OperationArtifact"@\n\x11OperationArtifact\x12\x15\n\rartifact_type\x18\x01 \x01(\t\x12\x14\n\x0cartifact_uri\x18\x02 \x01(\t"\x9b\x01\n\x0fSessionEventLog\x12D\n\nevent_type\x18\x01 \x01(\x0e20.google.cloud.stream.logging.v1.SessionEventType\x12.\n\nevent_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\nsession_id\x18\x03 \x01(\t*\x98\x05\n\x12OperationEventType\x12$\n OPERATION_EVENT_TYPE_UNSPECIFIED\x10\x00\x12*\n&OPERATION_EVENT_CREATE_CONTENT_STARTED\x10\x01\x12(\n$OPERATION_EVENT_CREATE_CONTENT_ENDED\x10\x02\x12)\n%OPERATION_EVENT_BUILD_CONTENT_STARTED\x10\x03\x12\'\n#OPERATION_EVENT_BUILD_CONTENT_ENDED\x10\x04\x12*\n&OPERATION_EVENT_UPDATE_CONTENT_STARTED\x10\x05\x12(\n$OPERATION_EVENT_UPDATE_CONTENT_ENDED\x10\x06\x12*\n&OPERATION_EVENT_DELETE_CONTENT_STARTED\x10\x07\x12(\n$OPERATION_EVENT_DELETE_CONTENT_ENDED\x10\x08\x12+\n\'OPERATION_EVENT_CREATE_INSTANCE_STARTED\x10\t\x12)\n%OPERATION_EVENT_CREATE_INSTANCE_ENDED\x10\n\x12+\n\'OPERATION_EVENT_UPDATE_INSTANCE_STARTED\x10\x0b\x12)\n%OPERATION_EVENT_UPDATE_INSTANCE_ENDED\x10\x0c\x12+\n\'OPERATION_EVENT_DELETE_INSTANCE_STARTED\x10\r\x12)\n%OPERATION_EVENT_DELETE_INSTANCE_ENDED\x10\x0e*\xe5\t\n\x10SessionEventType\x12"\n\x1eSESSION_EVENT_TYPE_UNSPECIFIED\x10\x00\x12/\n+SESSION_EVENT_SERVER_STREAMER_SHUTTING_DOWN\x10\x01\x12\'\n#SESSION_EVENT_SERVER_STREAMER_READY\x10\x02\x120\n,SESSION_EVENT_SERVER_STREAMER_BINARY_STARTED\x10\x03\x126\n2SESSION_EVENT_SERVER_STREAMER_READ_POD_IMAGE_NAMES\x10\x04\x123\n/SESSION_EVENT_SERVER_STREAMER_CONNECTED_TO_GAME\x10\x05\x125\n1SESSION_EVENT_SERVER_STREAMER_CONNECTED_TO_CLIENT\x10\x06\x12:\n6SESSION_EVENT_SERVER_STREAMER_DISCONNECTED_FROM_CLIENT\x10\x07\x12A\n=SESSION_EVENT_SERVER_STREAMER_RECEIVED_CREATE_SESSION_REQUEST\x10\x08\x12<\n8SESSION_EVENT_SERVER_STREAMER_GAME_MESSAGE_STREAM_CLOSED\x10\t\x12:\n6SESSION_EVENT_SERVER_STREAMER_GAME_FRAME_STREAM_CLOSED\x10\n\x12;\n7SESSION_EVENT_SERVER_STREAMER_GAME_MESSAGE_STREAM_ERROR\x10\x0b\x129\n5SESSION_EVENT_SERVER_STREAMER_GAME_AUDIO_STREAM_ERROR\x10\x0c\x12:\n6SESSION_EVENT_SERVER_STREAMER_GAME_AUDIO_STREAM_CLOSED\x10\r\x129\n5SESSION_EVENT_SERVER_STREAMER_GAME_FRAME_STREAM_ERROR\x10\x0e\x12A\n=SESSION_EVENT_SERVER_GAME_DISCONNECTING_AFTER_PAUSED_TOO_LONG\x10\x0f\x12C\n?SESSION_EVENT_SERVER_STREAMER_RECEIVED_EXPERIMENT_CONFIGURATION\x10\x10\x12:\n6SESSION_EVENT_SERVER_GAME_CONNECTED_TO_LOGGING_SERVICE\x10\x11\x12<\n8SESSION_EVENT_SERVER_STREAMER_DETERMINED_SESSION_OPTIONS\x10\x12\x12=\n9SESSION_EVENT_SERVER_STREAMER_KILLED_IN_MIDDLE_OF_SESSION\x10\x13\x124\n0SESSION_EVENT_SERVER_GAME_UPDATED_FRAME_PIPELINE\x10\x14\x12\x1e\n\x1aSESSION_EVENT_SERVER_ERROR\x10\x15Br\n"com.google.cloud.stream.logging.v1B\x0cLoggingProtoP\x01Z<cloud.google.com/go/stream/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.stream.logging.v1.logging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.stream.logging.v1B\x0cLoggingProtoP\x01Z<cloud.google.com/go/stream/logging/apiv1/loggingpb;loggingpb'
    _globals['_OPERATIONEVENTTYPE']._serialized_start = 579
    _globals['_OPERATIONEVENTTYPE']._serialized_end = 1243
    _globals['_SESSIONEVENTTYPE']._serialized_start = 1246
    _globals['_SESSIONEVENTTYPE']._serialized_end = 2499
    _globals['_OPERATIONEVENTLOG']._serialized_start = 114
    _globals['_OPERATIONEVENTLOG']._serialized_end = 352
    _globals['_OPERATIONARTIFACT']._serialized_start = 354
    _globals['_OPERATIONARTIFACT']._serialized_end = 418
    _globals['_SESSIONEVENTLOG']._serialized_start = 421
    _globals['_SESSIONEVENTLOG']._serialized_end = 576