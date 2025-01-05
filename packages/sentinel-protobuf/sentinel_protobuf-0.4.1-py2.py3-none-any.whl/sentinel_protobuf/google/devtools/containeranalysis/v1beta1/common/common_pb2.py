"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/common/common.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/devtools/containeranalysis/v1beta1/common/common.proto\x12\x0fgrafeas.v1beta1"(\n\nRelatedUrl\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t"5\n\tSignature\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x15\n\rpublic_key_id\x18\x02 \x01(\t*\x8b\x01\n\x08NoteKind\x12\x19\n\x15NOTE_KIND_UNSPECIFIED\x10\x00\x12\x11\n\rVULNERABILITY\x10\x01\x12\t\n\x05BUILD\x10\x02\x12\t\n\x05IMAGE\x10\x03\x12\x0b\n\x07PACKAGE\x10\x04\x12\x0e\n\nDEPLOYMENT\x10\x05\x12\r\n\tDISCOVERY\x10\x06\x12\x0f\n\x0bATTESTATION\x10\x07B}\n\x19io.grafeas.v1beta1.commonP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.common.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19io.grafeas.v1beta1.commonP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_NOTEKIND']._serialized_start = 180
    _globals['_NOTEKIND']._serialized_end = 319
    _globals['_RELATEDURL']._serialized_start = 82
    _globals['_RELATEDURL']._serialized_end = 122
    _globals['_SIGNATURE']._serialized_start = 124
    _globals['_SIGNATURE']._serialized_end = 177