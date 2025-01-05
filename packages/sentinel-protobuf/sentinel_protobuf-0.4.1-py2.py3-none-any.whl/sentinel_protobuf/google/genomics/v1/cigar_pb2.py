"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/cigar.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egoogle/genomics/v1/cigar.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto"\xaf\x02\n\tCigarUnit\x12:\n\toperation\x18\x01 \x01(\x0e2\'.google.genomics.v1.CigarUnit.Operation\x12\x18\n\x10operation_length\x18\x02 \x01(\x03\x12\x1a\n\x12reference_sequence\x18\x03 \x01(\t"\xaf\x01\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x13\n\x0fALIGNMENT_MATCH\x10\x01\x12\n\n\x06INSERT\x10\x02\x12\n\n\x06DELETE\x10\x03\x12\x08\n\x04SKIP\x10\x04\x12\r\n\tCLIP_SOFT\x10\x05\x12\r\n\tCLIP_HARD\x10\x06\x12\x07\n\x03PAD\x10\x07\x12\x12\n\x0eSEQUENCE_MATCH\x10\x08\x12\x15\n\x11SEQUENCE_MISMATCH\x10\tBe\n\x16com.google.genomics.v1B\nCigarProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.cigar_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\nCigarProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_CIGARUNIT']._serialized_start = 85
    _globals['_CIGARUNIT']._serialized_end = 388
    _globals['_CIGARUNIT_OPERATION']._serialized_start = 213
    _globals['_CIGARUNIT_OPERATION']._serialized_end = 388