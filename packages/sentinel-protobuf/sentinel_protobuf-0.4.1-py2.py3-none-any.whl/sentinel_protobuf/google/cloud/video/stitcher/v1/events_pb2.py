"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/stitcher/v1/events.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/video/stitcher/v1/events.proto\x12\x1egoogle.cloud.video.stitcher.v1\x1a\x1egoogle/protobuf/duration.proto"\x8e\x04\n\x05Event\x12=\n\x04type\x18\x01 \x01(\x0e2/.google.cloud.video.stitcher.v1.Event.EventType\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12)\n\x06offset\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration"\x81\x03\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rCREATIVE_VIEW\x10\x01\x12\t\n\x05START\x10\x02\x12\x0f\n\x0bBREAK_START\x10\x03\x12\r\n\tBREAK_END\x10\x04\x12\x0e\n\nIMPRESSION\x10\x05\x12\x12\n\x0eFIRST_QUARTILE\x10\x06\x12\x0c\n\x08MIDPOINT\x10\x07\x12\x12\n\x0eTHIRD_QUARTILE\x10\x08\x12\x0c\n\x08COMPLETE\x10\t\x12\x0c\n\x08PROGRESS\x10\n\x12\x08\n\x04MUTE\x10\x0b\x12\n\n\x06UNMUTE\x10\x0c\x12\t\n\x05PAUSE\x10\r\x12\t\n\x05CLICK\x10\x0e\x12\x11\n\rCLICK_THROUGH\x10\x0f\x12\n\n\x06REWIND\x10\x10\x12\n\n\x06RESUME\x10\x11\x12\t\n\x05ERROR\x10\x12\x12\n\n\x06EXPAND\x10\x15\x12\x0c\n\x08COLLAPSE\x10\x16\x12\t\n\x05CLOSE\x10\x18\x12\x10\n\x0cCLOSE_LINEAR\x10\x19\x12\x08\n\x04SKIP\x10\x1a\x12\x15\n\x11ACCEPT_INVITATION\x10\x1b"v\n\rProgressEvent\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x125\n\x06events\x18\x02 \x03(\x0b2%.google.cloud.video.stitcher.v1.EventBs\n"com.google.cloud.video.stitcher.v1B\x0bEventsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\x0bEventsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_EVENT']._serialized_start = 112
    _globals['_EVENT']._serialized_end = 638
    _globals['_EVENT_EVENTTYPE']._serialized_start = 253
    _globals['_EVENT_EVENTTYPE']._serialized_end = 638
    _globals['_PROGRESSEVENT']._serialized_start = 640
    _globals['_PROGRESSEVENT']._serialized_end = 758