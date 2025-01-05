"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ai/generativelanguage/v1/content.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/ai/generativelanguage/v1/content.proto\x12\x1fgoogle.ai.generativelanguage.v1\x1a\x1fgoogle/api/field_behavior.proto"R\n\x07Content\x124\n\x05parts\x18\x01 \x03(\x0b2%.google.ai.generativelanguage.v1.Part\x12\x11\n\x04role\x18\x02 \x01(\tB\x03\xe0A\x01"\\\n\x04Part\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12<\n\x0binline_data\x18\x03 \x01(\x0b2%.google.ai.generativelanguage.v1.BlobH\x00B\x06\n\x04data"\'\n\x04Blob\x12\x11\n\tmime_type\x18\x01 \x01(\t\x12\x0c\n\x04data\x18\x02 \x01(\x0cB\x90\x01\n#com.google.ai.generativelanguage.v1B\x0cContentProtoP\x01ZYcloud.google.com/go/ai/generativelanguage/apiv1/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1.content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ai.generativelanguage.v1B\x0cContentProtoP\x01ZYcloud.google.com/go/ai/generativelanguage/apiv1/generativelanguagepb;generativelanguagepb'
    _globals['_CONTENT'].fields_by_name['role']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['role']._serialized_options = b'\xe0A\x01'
    _globals['_CONTENT']._serialized_start = 115
    _globals['_CONTENT']._serialized_end = 197
    _globals['_PART']._serialized_start = 199
    _globals['_PART']._serialized_end = 291
    _globals['_BLOB']._serialized_start = 293
    _globals['_BLOB']._serialized_end = 332