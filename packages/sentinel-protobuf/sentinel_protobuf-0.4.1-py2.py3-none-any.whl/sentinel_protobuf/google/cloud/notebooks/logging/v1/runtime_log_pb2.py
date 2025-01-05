"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/logging/v1/runtime_log.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/notebooks/logging/v1/runtime_log.proto\x12!google.cloud.notebooks.logging.v1\x1a\x1fgoogle/api/field_behavior.proto"\xa9\x02\n\x0cRuntimeEvent\x12L\n\x04type\x18\x01 \x01(\x0e29.google.cloud.notebooks.logging.v1.RuntimeEvent.EventTypeB\x03\xe0A\x02\x12R\n\x07details\x18\x02 \x03(\x0b2<.google.cloud.notebooks.logging.v1.RuntimeEvent.DetailsEntryB\x03\xe0A\x01\x1a.\n\x0cDetailsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"G\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aRUNTIME_STATE_CHANGE_EVENT\x10\x01B\x9f\x01\n%com.google.cloud.notebooks.logging.v1B\x0fRuntimeLogProtoP\x01Z?cloud.google.com/go/notebooks/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.Notebooks.Logging.V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.logging.v1.runtime_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.notebooks.logging.v1B\x0fRuntimeLogProtoP\x01Z?cloud.google.com/go/notebooks/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.Notebooks.Logging.V1'
    _globals['_RUNTIMEEVENT_DETAILSENTRY']._loaded_options = None
    _globals['_RUNTIMEEVENT_DETAILSENTRY']._serialized_options = b'8\x01'
    _globals['_RUNTIMEEVENT'].fields_by_name['type']._loaded_options = None
    _globals['_RUNTIMEEVENT'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_RUNTIMEEVENT'].fields_by_name['details']._loaded_options = None
    _globals['_RUNTIMEEVENT'].fields_by_name['details']._serialized_options = b'\xe0A\x01'
    _globals['_RUNTIMEEVENT']._serialized_start = 124
    _globals['_RUNTIMEEVENT']._serialized_end = 421
    _globals['_RUNTIMEEVENT_DETAILSENTRY']._serialized_start = 302
    _globals['_RUNTIMEEVENT_DETAILSENTRY']._serialized_end = 348
    _globals['_RUNTIMEEVENT_EVENTTYPE']._serialized_start = 350
    _globals['_RUNTIMEEVENT_EVENTTYPE']._serialized_end = 421