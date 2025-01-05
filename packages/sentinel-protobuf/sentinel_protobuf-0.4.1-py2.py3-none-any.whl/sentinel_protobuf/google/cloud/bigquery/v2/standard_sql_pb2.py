"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/standard_sql.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/bigquery/v2/standard_sql.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"\xcb\x04\n\x13StandardSqlDataType\x12N\n\ttype_kind\x18\x01 \x01(\x0e26.google.cloud.bigquery.v2.StandardSqlDataType.TypeKindB\x03\xe0A\x02\x12K\n\x12array_element_type\x18\x02 \x01(\x0b2-.google.cloud.bigquery.v2.StandardSqlDataTypeH\x00\x12F\n\x0bstruct_type\x18\x03 \x01(\x0b2/.google.cloud.bigquery.v2.StandardSqlStructTypeH\x00\x12K\n\x12range_element_type\x18\x04 \x01(\x0b2-.google.cloud.bigquery.v2.StandardSqlDataTypeH\x00"\xf5\x01\n\x08TypeKind\x12\x19\n\x15TYPE_KIND_UNSPECIFIED\x10\x00\x12\t\n\x05INT64\x10\x02\x12\x08\n\x04BOOL\x10\x05\x12\x0b\n\x07FLOAT64\x10\x07\x12\n\n\x06STRING\x10\x08\x12\t\n\x05BYTES\x10\t\x12\r\n\tTIMESTAMP\x10\x13\x12\x08\n\x04DATE\x10\n\x12\x08\n\x04TIME\x10\x14\x12\x0c\n\x08DATETIME\x10\x15\x12\x0c\n\x08INTERVAL\x10\x1a\x12\r\n\tGEOGRAPHY\x10\x16\x12\x0b\n\x07NUMERIC\x10\x17\x12\x0e\n\nBIGNUMERIC\x10\x18\x12\x08\n\x04JSON\x10\x19\x12\t\n\x05ARRAY\x10\x10\x12\n\n\x06STRUCT\x10\x11\x12\t\n\x05RANGE\x10\x1dB\n\n\x08sub_type"g\n\x10StandardSqlField\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12@\n\x04type\x18\x02 \x01(\x0b2-.google.cloud.bigquery.v2.StandardSqlDataTypeB\x03\xe0A\x01"S\n\x15StandardSqlStructType\x12:\n\x06fields\x18\x01 \x03(\x0b2*.google.cloud.bigquery.v2.StandardSqlField"S\n\x14StandardSqlTableType\x12;\n\x07columns\x18\x01 \x03(\x0b2*.google.cloud.bigquery.v2.StandardSqlFieldBj\n\x1ccom.google.cloud.bigquery.v2B\x10StandardSqlProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.standard_sql_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x10StandardSqlProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_STANDARDSQLDATATYPE'].fields_by_name['type_kind']._loaded_options = None
    _globals['_STANDARDSQLDATATYPE'].fields_by_name['type_kind']._serialized_options = b'\xe0A\x02'
    _globals['_STANDARDSQLFIELD'].fields_by_name['name']._loaded_options = None
    _globals['_STANDARDSQLFIELD'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_STANDARDSQLFIELD'].fields_by_name['type']._loaded_options = None
    _globals['_STANDARDSQLFIELD'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_STANDARDSQLDATATYPE']._serialized_start = 107
    _globals['_STANDARDSQLDATATYPE']._serialized_end = 694
    _globals['_STANDARDSQLDATATYPE_TYPEKIND']._serialized_start = 437
    _globals['_STANDARDSQLDATATYPE_TYPEKIND']._serialized_end = 682
    _globals['_STANDARDSQLFIELD']._serialized_start = 696
    _globals['_STANDARDSQLFIELD']._serialized_end = 799
    _globals['_STANDARDSQLSTRUCTTYPE']._serialized_start = 801
    _globals['_STANDARDSQLSTRUCTTYPE']._serialized_end = 884
    _globals['_STANDARDSQLTABLETYPE']._serialized_start = 886
    _globals['_STANDARDSQLTABLETYPE']._serialized_end = 969