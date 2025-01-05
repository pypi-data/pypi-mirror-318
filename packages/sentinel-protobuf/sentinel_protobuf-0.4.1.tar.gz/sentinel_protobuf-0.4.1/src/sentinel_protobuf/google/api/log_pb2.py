"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/log.proto')
_sym_db = _symbol_database.Default()
from ...google.api import label_pb2 as google_dot_api_dot_label__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14google/api/log.proto\x12\ngoogle.api\x1a\x16google/api/label.proto"u\n\rLogDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x06labels\x18\x02 \x03(\x0b2\x1b.google.api.LabelDescriptor\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\tBj\n\x0ecom.google.apiB\x08LogProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x08LogProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPI'
    _globals['_LOGDESCRIPTOR']._serialized_start = 60
    _globals['_LOGDESCRIPTOR']._serialized_end = 177