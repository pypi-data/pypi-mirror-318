"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/readgroupset.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.genomics.v1 import readgroup_pb2 as google_dot_genomics_dot_v1_dot_readgroup__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/genomics/v1/readgroupset.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a"google/genomics/v1/readgroup.proto\x1a\x1cgoogle/protobuf/struct.proto"\x9f\x02\n\x0cReadGroupSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x18\n\x10reference_set_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08filename\x18\x05 \x01(\t\x122\n\x0bread_groups\x18\x06 \x03(\x0b2\x1d.google.genomics.v1.ReadGroup\x128\n\x04info\x18\x07 \x03(\x0b2*.google.genomics.v1.ReadGroupSet.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01Bl\n\x16com.google.genomics.v1B\x11ReadGroupSetProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.readgroupset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\x11ReadGroupSetProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_READGROUPSET_INFOENTRY']._loaded_options = None
    _globals['_READGROUPSET_INFOENTRY']._serialized_options = b'8\x01'
    _globals['_READGROUPSET']._serialized_start = 158
    _globals['_READGROUPSET']._serialized_end = 445
    _globals['_READGROUPSET_INFOENTRY']._serialized_start = 374
    _globals['_READGROUPSET_INFOENTRY']._serialized_end = 445