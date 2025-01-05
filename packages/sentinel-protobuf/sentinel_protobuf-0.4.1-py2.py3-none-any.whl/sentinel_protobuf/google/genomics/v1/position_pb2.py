"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/position.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/genomics/v1/position.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto"L\n\x08Position\x12\x16\n\x0ereference_name\x18\x01 \x01(\t\x12\x10\n\x08position\x18\x02 \x01(\x03\x12\x16\n\x0ereverse_strand\x18\x03 \x01(\x08Bh\n\x16com.google.genomics.v1B\rPositionProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.position_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\rPositionProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_POSITION']._serialized_start = 87
    _globals['_POSITION']._serialized_end = 163