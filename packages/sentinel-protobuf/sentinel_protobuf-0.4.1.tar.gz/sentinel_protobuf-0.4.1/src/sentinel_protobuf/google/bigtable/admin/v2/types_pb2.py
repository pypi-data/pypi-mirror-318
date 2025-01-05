"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/bigtable/admin/v2/types.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/bigtable/admin/v2/types.proto\x12\x18google.bigtable.admin.v2\x1a\x1fgoogle/api/field_behavior.proto"\x9a\x12\n\x04Type\x12:\n\nbytes_type\x18\x01 \x01(\x0b2$.google.bigtable.admin.v2.Type.BytesH\x00\x12<\n\x0bstring_type\x18\x02 \x01(\x0b2%.google.bigtable.admin.v2.Type.StringH\x00\x12:\n\nint64_type\x18\x05 \x01(\x0b2$.google.bigtable.admin.v2.Type.Int64H\x00\x12>\n\x0cfloat32_type\x18\x0c \x01(\x0b2&.google.bigtable.admin.v2.Type.Float32H\x00\x12>\n\x0cfloat64_type\x18\t \x01(\x0b2&.google.bigtable.admin.v2.Type.Float64H\x00\x128\n\tbool_type\x18\x08 \x01(\x0b2#.google.bigtable.admin.v2.Type.BoolH\x00\x12B\n\x0etimestamp_type\x18\n \x01(\x0b2(.google.bigtable.admin.v2.Type.TimestampH\x00\x128\n\tdate_type\x18\x0b \x01(\x0b2#.google.bigtable.admin.v2.Type.DateH\x00\x12B\n\x0eaggregate_type\x18\x06 \x01(\x0b2(.google.bigtable.admin.v2.Type.AggregateH\x00\x12<\n\x0bstruct_type\x18\x07 \x01(\x0b2%.google.bigtable.admin.v2.Type.StructH\x00\x12:\n\narray_type\x18\x03 \x01(\x0b2$.google.bigtable.admin.v2.Type.ArrayH\x00\x126\n\x08map_type\x18\x04 \x01(\x0b2".google.bigtable.admin.v2.Type.MapH\x00\x1a\xa9\x01\n\x05Bytes\x12?\n\x08encoding\x18\x01 \x01(\x0b2-.google.bigtable.admin.v2.Type.Bytes.Encoding\x1a_\n\x08Encoding\x12@\n\x03raw\x18\x01 \x01(\x0b21.google.bigtable.admin.v2.Type.Bytes.Encoding.RawH\x00\x1a\x05\n\x03RawB\n\n\x08encoding\x1a\x9f\x02\n\x06String\x12@\n\x08encoding\x18\x01 \x01(\x0b2..google.bigtable.admin.v2.Type.String.Encoding\x1a\xd2\x01\n\x08Encoding\x12N\n\x08utf8_raw\x18\x01 \x01(\x0b26.google.bigtable.admin.v2.Type.String.Encoding.Utf8RawB\x02\x18\x01H\x00\x12N\n\nutf8_bytes\x18\x02 \x01(\x0b28.google.bigtable.admin.v2.Type.String.Encoding.Utf8BytesH\x00\x1a\r\n\x07Utf8Raw:\x02\x18\x01\x1a\x0b\n\tUtf8BytesB\n\n\x08encoding\x1a\x87\x02\n\x05Int64\x12?\n\x08encoding\x18\x01 \x01(\x0b2-.google.bigtable.admin.v2.Type.Int64.Encoding\x1a\xbc\x01\n\x08Encoding\x12X\n\x10big_endian_bytes\x18\x01 \x01(\x0b2<.google.bigtable.admin.v2.Type.Int64.Encoding.BigEndianBytesH\x00\x1aJ\n\x0eBigEndianBytes\x128\n\nbytes_type\x18\x01 \x01(\x0b2$.google.bigtable.admin.v2.Type.BytesB\n\n\x08encoding\x1a\x06\n\x04Bool\x1a\t\n\x07Float32\x1a\t\n\x07Float64\x1a\x0b\n\tTimestamp\x1a\x06\n\x04Date\x1a\x90\x01\n\x06Struct\x12;\n\x06fields\x18\x01 \x03(\x0b2+.google.bigtable.admin.v2.Type.Struct.Field\x1aI\n\x05Field\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12,\n\x04type\x18\x02 \x01(\x0b2\x1e.google.bigtable.admin.v2.Type\x1a=\n\x05Array\x124\n\x0celement_type\x18\x01 \x01(\x0b2\x1e.google.bigtable.admin.v2.Type\x1ak\n\x03Map\x120\n\x08key_type\x18\x01 \x01(\x0b2\x1e.google.bigtable.admin.v2.Type\x122\n\nvalue_type\x18\x02 \x01(\x0b2\x1e.google.bigtable.admin.v2.Type\x1a\xdb\x03\n\tAggregate\x122\n\ninput_type\x18\x01 \x01(\x0b2\x1e.google.bigtable.admin.v2.Type\x127\n\nstate_type\x18\x02 \x01(\x0b2\x1e.google.bigtable.admin.v2.TypeB\x03\xe0A\x03\x12;\n\x03sum\x18\x04 \x01(\x0b2,.google.bigtable.admin.v2.Type.Aggregate.SumH\x00\x12e\n\x12hllpp_unique_count\x18\x05 \x01(\x0b2G.google.bigtable.admin.v2.Type.Aggregate.HyperLogLogPlusPlusUniqueCountH\x00\x12;\n\x03max\x18\x06 \x01(\x0b2,.google.bigtable.admin.v2.Type.Aggregate.MaxH\x00\x12;\n\x03min\x18\x07 \x01(\x0b2,.google.bigtable.admin.v2.Type.Aggregate.MinH\x00\x1a\x05\n\x03Sum\x1a\x05\n\x03Max\x1a\x05\n\x03Min\x1a \n\x1eHyperLogLogPlusPlusUniqueCountB\x0c\n\naggregatorB\x06\n\x04kindB\xcd\x01\n\x1ccom.google.bigtable.admin.v2B\nTypesProtoP\x01Z8cloud.google.com/go/bigtable/admin/apiv2/adminpb;adminpb\xaa\x02\x1eGoogle.Cloud.Bigtable.Admin.V2\xca\x02\x1eGoogle\\Cloud\\Bigtable\\Admin\\V2\xea\x02"Google::Cloud::Bigtable::Admin::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.bigtable.admin.v2.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.bigtable.admin.v2B\nTypesProtoP\x01Z8cloud.google.com/go/bigtable/admin/apiv2/adminpb;adminpb\xaa\x02\x1eGoogle.Cloud.Bigtable.Admin.V2\xca\x02\x1eGoogle\\Cloud\\Bigtable\\Admin\\V2\xea\x02"Google::Cloud::Bigtable::Admin::V2'
    _globals['_TYPE_STRING_ENCODING_UTF8RAW']._loaded_options = None
    _globals['_TYPE_STRING_ENCODING_UTF8RAW']._serialized_options = b'\x18\x01'
    _globals['_TYPE_STRING_ENCODING'].fields_by_name['utf8_raw']._loaded_options = None
    _globals['_TYPE_STRING_ENCODING'].fields_by_name['utf8_raw']._serialized_options = b'\x18\x01'
    _globals['_TYPE_AGGREGATE'].fields_by_name['state_type']._loaded_options = None
    _globals['_TYPE_AGGREGATE'].fields_by_name['state_type']._serialized_options = b'\xe0A\x03'
    _globals['_TYPE']._serialized_start = 100
    _globals['_TYPE']._serialized_end = 2430
    _globals['_TYPE_BYTES']._serialized_start = 849
    _globals['_TYPE_BYTES']._serialized_end = 1018
    _globals['_TYPE_BYTES_ENCODING']._serialized_start = 923
    _globals['_TYPE_BYTES_ENCODING']._serialized_end = 1018
    _globals['_TYPE_BYTES_ENCODING_RAW']._serialized_start = 1001
    _globals['_TYPE_BYTES_ENCODING_RAW']._serialized_end = 1006
    _globals['_TYPE_STRING']._serialized_start = 1021
    _globals['_TYPE_STRING']._serialized_end = 1308
    _globals['_TYPE_STRING_ENCODING']._serialized_start = 1098
    _globals['_TYPE_STRING_ENCODING']._serialized_end = 1308
    _globals['_TYPE_STRING_ENCODING_UTF8RAW']._serialized_start = 1270
    _globals['_TYPE_STRING_ENCODING_UTF8RAW']._serialized_end = 1283
    _globals['_TYPE_STRING_ENCODING_UTF8BYTES']._serialized_start = 1285
    _globals['_TYPE_STRING_ENCODING_UTF8BYTES']._serialized_end = 1296
    _globals['_TYPE_INT64']._serialized_start = 1311
    _globals['_TYPE_INT64']._serialized_end = 1574
    _globals['_TYPE_INT64_ENCODING']._serialized_start = 1386
    _globals['_TYPE_INT64_ENCODING']._serialized_end = 1574
    _globals['_TYPE_INT64_ENCODING_BIGENDIANBYTES']._serialized_start = 1488
    _globals['_TYPE_INT64_ENCODING_BIGENDIANBYTES']._serialized_end = 1562
    _globals['_TYPE_BOOL']._serialized_start = 1576
    _globals['_TYPE_BOOL']._serialized_end = 1582
    _globals['_TYPE_FLOAT32']._serialized_start = 1584
    _globals['_TYPE_FLOAT32']._serialized_end = 1593
    _globals['_TYPE_FLOAT64']._serialized_start = 1595
    _globals['_TYPE_FLOAT64']._serialized_end = 1604
    _globals['_TYPE_TIMESTAMP']._serialized_start = 1606
    _globals['_TYPE_TIMESTAMP']._serialized_end = 1617
    _globals['_TYPE_DATE']._serialized_start = 1619
    _globals['_TYPE_DATE']._serialized_end = 1625
    _globals['_TYPE_STRUCT']._serialized_start = 1628
    _globals['_TYPE_STRUCT']._serialized_end = 1772
    _globals['_TYPE_STRUCT_FIELD']._serialized_start = 1699
    _globals['_TYPE_STRUCT_FIELD']._serialized_end = 1772
    _globals['_TYPE_ARRAY']._serialized_start = 1774
    _globals['_TYPE_ARRAY']._serialized_end = 1835
    _globals['_TYPE_MAP']._serialized_start = 1837
    _globals['_TYPE_MAP']._serialized_end = 1944
    _globals['_TYPE_AGGREGATE']._serialized_start = 1947
    _globals['_TYPE_AGGREGATE']._serialized_end = 2422
    _globals['_TYPE_AGGREGATE_SUM']._serialized_start = 2355
    _globals['_TYPE_AGGREGATE_SUM']._serialized_end = 2360
    _globals['_TYPE_AGGREGATE_MAX']._serialized_start = 2362
    _globals['_TYPE_AGGREGATE_MAX']._serialized_end = 2367
    _globals['_TYPE_AGGREGATE_MIN']._serialized_start = 2369
    _globals['_TYPE_AGGREGATE_MIN']._serialized_end = 2374
    _globals['_TYPE_AGGREGATE_HYPERLOGLOGPLUSPLUSUNIQUECOUNT']._serialized_start = 2376
    _globals['_TYPE_AGGREGATE_HYPERLOGLOGPLUSPLUSUNIQUECOUNT']._serialized_end = 2408