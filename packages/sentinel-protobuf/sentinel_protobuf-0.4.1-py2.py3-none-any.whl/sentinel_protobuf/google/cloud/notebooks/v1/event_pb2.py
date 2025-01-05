"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/v1/event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/notebooks/v1/event.proto\x12\x19google.cloud.notebooks.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc6\x02\n\x05Event\x12/\n\x0breport_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x128\n\x04type\x18\x02 \x01(\x0e2*.google.cloud.notebooks.v1.Event.EventType\x12C\n\x07details\x18\x03 \x03(\x0b2-.google.cloud.notebooks.v1.Event.DetailsEntryB\x03\xe0A\x01\x1a.\n\x0cDetailsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"]\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\r\n\tHEARTBEAT\x10\x02\x12\n\n\x06HEALTH\x10\x03\x12\x0f\n\x0bMAINTENANCE\x10\x04Bj\n\x1dcom.google.cloud.notebooks.v1B\nEventProtoP\x01Z;cloud.google.com/go/notebooks/apiv1/notebookspb;notebookspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v1.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.notebooks.v1B\nEventProtoP\x01Z;cloud.google.com/go/notebooks/apiv1/notebookspb;notebookspb'
    _globals['_EVENT_DETAILSENTRY']._loaded_options = None
    _globals['_EVENT_DETAILSENTRY']._serialized_options = b'8\x01'
    _globals['_EVENT'].fields_by_name['details']._loaded_options = None
    _globals['_EVENT'].fields_by_name['details']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT']._serialized_start = 135
    _globals['_EVENT']._serialized_end = 461
    _globals['_EVENT_DETAILSENTRY']._serialized_start = 320
    _globals['_EVENT_DETAILSENTRY']._serialized_end = 366
    _globals['_EVENT_EVENTTYPE']._serialized_start = 368
    _globals['_EVENT_EVENTTYPE']._serialized_end = 461