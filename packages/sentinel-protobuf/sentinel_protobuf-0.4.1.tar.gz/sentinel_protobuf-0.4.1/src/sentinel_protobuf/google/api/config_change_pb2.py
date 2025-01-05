"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/config_change.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egoogle/api/config_change.proto\x12\ngoogle.api"\x97\x01\n\x0cConfigChange\x12\x0f\n\x07element\x18\x01 \x01(\t\x12\x11\n\told_value\x18\x02 \x01(\t\x12\x11\n\tnew_value\x18\x03 \x01(\t\x12+\n\x0bchange_type\x18\x04 \x01(\x0e2\x16.google.api.ChangeType\x12#\n\x07advices\x18\x05 \x03(\x0b2\x12.google.api.Advice"\x1d\n\x06Advice\x12\x13\n\x0bdescription\x18\x02 \x01(\t*O\n\nChangeType\x12\x1b\n\x17CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ADDED\x10\x01\x12\x0b\n\x07REMOVED\x10\x02\x12\x0c\n\x08MODIFIED\x10\x03Bq\n\x0ecom.google.apiB\x11ConfigChangeProtoP\x01ZCgoogle.golang.org/genproto/googleapis/api/configchange;configchange\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.config_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x11ConfigChangeProtoP\x01ZCgoogle.golang.org/genproto/googleapis/api/configchange;configchange\xa2\x02\x04GAPI'
    _globals['_CHANGETYPE']._serialized_start = 231
    _globals['_CHANGETYPE']._serialized_end = 310
    _globals['_CONFIGCHANGE']._serialized_start = 47
    _globals['_CONFIGCHANGE']._serialized_end = 198
    _globals['_ADVICE']._serialized_start = 200
    _globals['_ADVICE']._serialized_end = 229