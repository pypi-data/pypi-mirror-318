"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/readgroup.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/genomics/v1/readgroup.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xe4\x04\n\tReadGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\x11\n\tsample_id\x18\x05 \x01(\t\x12<\n\nexperiment\x18\x06 \x01(\x0b2(.google.genomics.v1.ReadGroup.Experiment\x12\x1d\n\x15predicted_insert_size\x18\x07 \x01(\x05\x127\n\x08programs\x18\n \x03(\x0b2%.google.genomics.v1.ReadGroup.Program\x12\x18\n\x10reference_set_id\x18\x0b \x01(\t\x125\n\x04info\x18\x0c \x03(\x0b2\'.google.genomics.v1.ReadGroup.InfoEntry\x1al\n\nExperiment\x12\x12\n\nlibrary_id\x18\x01 \x01(\t\x12\x15\n\rplatform_unit\x18\x02 \x01(\t\x12\x19\n\x11sequencing_center\x18\x03 \x01(\t\x12\x18\n\x10instrument_model\x18\x04 \x01(\t\x1ac\n\x07Program\x12\x14\n\x0ccommand_line\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x17\n\x0fprev_program_id\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01Bi\n\x16com.google.genomics.v1B\x0eReadGroupProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.readgroup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\x0eReadGroupProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_READGROUP_INFOENTRY']._loaded_options = None
    _globals['_READGROUP_INFOENTRY']._serialized_options = b'8\x01'
    _globals['_READGROUP']._serialized_start = 119
    _globals['_READGROUP']._serialized_end = 731
    _globals['_READGROUP_EXPERIMENT']._serialized_start = 449
    _globals['_READGROUP_EXPERIMENT']._serialized_end = 557
    _globals['_READGROUP_PROGRAM']._serialized_start = 559
    _globals['_READGROUP_PROGRAM']._serialized_end = 658
    _globals['_READGROUP_INFOENTRY']._serialized_start = 660
    _globals['_READGROUP_INFOENTRY']._serialized_end = 731