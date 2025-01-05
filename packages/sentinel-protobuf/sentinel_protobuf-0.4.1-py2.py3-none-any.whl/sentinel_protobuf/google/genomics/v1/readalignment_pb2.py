"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/readalignment.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.genomics.v1 import cigar_pb2 as google_dot_genomics_dot_v1_dot_cigar__pb2
from ....google.genomics.v1 import position_pb2 as google_dot_genomics_dot_v1_dot_position__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/genomics/v1/readalignment.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/genomics/v1/cigar.proto\x1a!google/genomics/v1/position.proto\x1a\x1cgoogle/protobuf/struct.proto"\x88\x01\n\x0fLinearAlignment\x12.\n\x08position\x18\x01 \x01(\x0b2\x1c.google.genomics.v1.Position\x12\x17\n\x0fmapping_quality\x18\x02 \x01(\x05\x12,\n\x05cigar\x18\x03 \x03(\x0b2\x1d.google.genomics.v1.CigarUnit"\xd9\x04\n\x04Read\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rread_group_id\x18\x02 \x01(\t\x12\x19\n\x11read_group_set_id\x18\x03 \x01(\t\x12\x15\n\rfragment_name\x18\x04 \x01(\t\x12\x18\n\x10proper_placement\x18\x05 \x01(\x08\x12\x1a\n\x12duplicate_fragment\x18\x06 \x01(\x08\x12\x17\n\x0ffragment_length\x18\x07 \x01(\x05\x12\x13\n\x0bread_number\x18\x08 \x01(\x05\x12\x14\n\x0cnumber_reads\x18\t \x01(\x05\x12$\n\x1cfailed_vendor_quality_checks\x18\n \x01(\x08\x126\n\talignment\x18\x0b \x01(\x0b2#.google.genomics.v1.LinearAlignment\x12\x1b\n\x13secondary_alignment\x18\x0c \x01(\x08\x12\x1f\n\x17supplementary_alignment\x18\r \x01(\x08\x12\x18\n\x10aligned_sequence\x18\x0e \x01(\t\x12\x17\n\x0faligned_quality\x18\x0f \x03(\x05\x128\n\x12next_mate_position\x18\x10 \x01(\x0b2\x1c.google.genomics.v1.Position\x120\n\x04info\x18\x11 \x03(\x0b2".google.genomics.v1.Read.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01Bm\n\x16com.google.genomics.v1B\x12ReadAlignmentProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.readalignment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\x12ReadAlignmentProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_READ_INFOENTRY']._loaded_options = None
    _globals['_READ_INFOENTRY']._serialized_options = b'8\x01'
    _globals['_LINEARALIGNMENT']._serialized_start = 190
    _globals['_LINEARALIGNMENT']._serialized_end = 326
    _globals['_READ']._serialized_start = 329
    _globals['_READ']._serialized_end = 930
    _globals['_READ_INFOENTRY']._serialized_start = 859
    _globals['_READ_INFOENTRY']._serialized_end = 930