"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/usage.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16google/api/usage.proto\x12\ngoogle.api"j\n\x05Usage\x12\x14\n\x0crequirements\x18\x01 \x03(\t\x12$\n\x05rules\x18\x06 \x03(\x0b2\x15.google.api.UsageRule\x12%\n\x1dproducer_notification_channel\x18\x07 \x01(\t"]\n\tUsageRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12 \n\x18allow_unregistered_calls\x18\x02 \x01(\x08\x12\x1c\n\x14skip_service_control\x18\x03 \x01(\x08Bl\n\x0ecom.google.apiB\nUsageProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.usage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\nUsageProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPI'
    _globals['_USAGE']._serialized_start = 38
    _globals['_USAGE']._serialized_end = 144
    _globals['_USAGERULE']._serialized_start = 146
    _globals['_USAGERULE']._serialized_end = 239