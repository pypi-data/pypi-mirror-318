"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/v1/type.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgoogle/spanner/v1/type.proto\x12\x11google.spanner.v1\x1a\x1fgoogle/api/field_behavior.proto"\xf7\x01\n\x04Type\x12.\n\x04code\x18\x01 \x01(\x0e2\x1b.google.spanner.v1.TypeCodeB\x03\xe0A\x02\x123\n\x12array_element_type\x18\x02 \x01(\x0b2\x17.google.spanner.v1.Type\x122\n\x0bstruct_type\x18\x03 \x01(\x0b2\x1d.google.spanner.v1.StructType\x12>\n\x0ftype_annotation\x18\x04 \x01(\x0e2%.google.spanner.v1.TypeAnnotationCode\x12\x16\n\x0eproto_type_fqn\x18\x05 \x01(\t"\x7f\n\nStructType\x123\n\x06fields\x18\x01 \x03(\x0b2#.google.spanner.v1.StructType.Field\x1a<\n\x05Field\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04type\x18\x02 \x01(\x0b2\x17.google.spanner.v1.Type*\xdf\x01\n\x08TypeCode\x12\x19\n\x15TYPE_CODE_UNSPECIFIED\x10\x00\x12\x08\n\x04BOOL\x10\x01\x12\t\n\x05INT64\x10\x02\x12\x0b\n\x07FLOAT64\x10\x03\x12\x0b\n\x07FLOAT32\x10\x0f\x12\r\n\tTIMESTAMP\x10\x04\x12\x08\n\x04DATE\x10\x05\x12\n\n\x06STRING\x10\x06\x12\t\n\x05BYTES\x10\x07\x12\t\n\x05ARRAY\x10\x08\x12\n\n\x06STRUCT\x10\t\x12\x0b\n\x07NUMERIC\x10\n\x12\x08\n\x04JSON\x10\x0b\x12\t\n\x05PROTO\x10\r\x12\x08\n\x04ENUM\x10\x0e\x12\x0c\n\x08INTERVAL\x10\x10\x12\x08\n\x04UUID\x10\x11*d\n\x12TypeAnnotationCode\x12$\n TYPE_ANNOTATION_CODE_UNSPECIFIED\x10\x00\x12\x0e\n\nPG_NUMERIC\x10\x02\x12\x0c\n\x08PG_JSONB\x10\x03\x12\n\n\x06PG_OID\x10\x04B\xac\x01\n\x15com.google.spanner.v1B\tTypeProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.spanner.v1B\tTypeProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1'
    _globals['_TYPE'].fields_by_name['code']._loaded_options = None
    _globals['_TYPE'].fields_by_name['code']._serialized_options = b'\xe0A\x02'
    _globals['_TYPECODE']._serialized_start = 464
    _globals['_TYPECODE']._serialized_end = 687
    _globals['_TYPEANNOTATIONCODE']._serialized_start = 689
    _globals['_TYPEANNOTATIONCODE']._serialized_end = 789
    _globals['_TYPE']._serialized_start = 85
    _globals['_TYPE']._serialized_end = 332
    _globals['_STRUCTTYPE']._serialized_start = 334
    _globals['_STRUCTTYPE']._serialized_end = 461
    _globals['_STRUCTTYPE_FIELD']._serialized_start = 401
    _globals['_STRUCTTYPE_FIELD']._serialized_end = 461