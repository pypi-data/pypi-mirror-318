"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/bigtable/v2/data.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.bigtable.v2 import types_pb2 as google_dot_bigtable_dot_v2_dot_types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dgoogle/bigtable/v2/data.proto\x12\x12google.bigtable.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/bigtable/v2/types.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto"@\n\x03Row\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12,\n\x08families\x18\x02 \x03(\x0b2\x1a.google.bigtable.v2.Family"C\n\x06Family\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x07columns\x18\x02 \x03(\x0b2\x1a.google.bigtable.v2.Column"D\n\x06Column\x12\x11\n\tqualifier\x18\x01 \x01(\x0c\x12\'\n\x05cells\x18\x02 \x03(\x0b2\x18.google.bigtable.v2.Cell"?\n\x04Cell\x12\x18\n\x10timestamp_micros\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0e\n\x06labels\x18\x03 \x03(\t"\xf4\x02\n\x05Value\x12&\n\x04type\x18\x07 \x01(\x0b2\x18.google.bigtable.v2.Type\x12\x13\n\traw_value\x18\x08 \x01(\x0cH\x00\x12\x1e\n\x14raw_timestamp_micros\x18\t \x01(\x03H\x00\x12\x15\n\x0bbytes_value\x18\x02 \x01(\x0cH\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x13\n\tint_value\x18\x06 \x01(\x03H\x00\x12\x14\n\nbool_value\x18\n \x01(\x08H\x00\x12\x15\n\x0bfloat_value\x18\x0b \x01(\x01H\x00\x125\n\x0ftimestamp_value\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12\'\n\ndate_value\x18\r \x01(\x0b2\x11.google.type.DateH\x00\x125\n\x0barray_value\x18\x04 \x01(\x0b2\x1e.google.bigtable.v2.ArrayValueH\x00B\x06\n\x04kind"7\n\nArrayValue\x12)\n\x06values\x18\x01 \x03(\x0b2\x19.google.bigtable.v2.Value"\x8a\x01\n\x08RowRange\x12\x1a\n\x10start_key_closed\x18\x01 \x01(\x0cH\x00\x12\x18\n\x0estart_key_open\x18\x02 \x01(\x0cH\x00\x12\x16\n\x0cend_key_open\x18\x03 \x01(\x0cH\x01\x12\x18\n\x0eend_key_closed\x18\x04 \x01(\x0cH\x01B\x0b\n\tstart_keyB\t\n\x07end_key"L\n\x06RowSet\x12\x10\n\x08row_keys\x18\x01 \x03(\x0c\x120\n\nrow_ranges\x18\x02 \x03(\x0b2\x1c.google.bigtable.v2.RowRange"\xc6\x01\n\x0bColumnRange\x12\x13\n\x0bfamily_name\x18\x01 \x01(\t\x12 \n\x16start_qualifier_closed\x18\x02 \x01(\x0cH\x00\x12\x1e\n\x14start_qualifier_open\x18\x03 \x01(\x0cH\x00\x12\x1e\n\x14end_qualifier_closed\x18\x04 \x01(\x0cH\x01\x12\x1c\n\x12end_qualifier_open\x18\x05 \x01(\x0cH\x01B\x11\n\x0fstart_qualifierB\x0f\n\rend_qualifier"N\n\x0eTimestampRange\x12\x1e\n\x16start_timestamp_micros\x18\x01 \x01(\x03\x12\x1c\n\x14end_timestamp_micros\x18\x02 \x01(\x03"\x98\x01\n\nValueRange\x12\x1c\n\x12start_value_closed\x18\x01 \x01(\x0cH\x00\x12\x1a\n\x10start_value_open\x18\x02 \x01(\x0cH\x00\x12\x1a\n\x10end_value_closed\x18\x03 \x01(\x0cH\x01\x12\x18\n\x0eend_value_open\x18\x04 \x01(\x0cH\x01B\r\n\x0bstart_valueB\x0b\n\tend_value"\xdf\x08\n\tRowFilter\x124\n\x05chain\x18\x01 \x01(\x0b2#.google.bigtable.v2.RowFilter.ChainH\x00\x12>\n\ninterleave\x18\x02 \x01(\x0b2(.google.bigtable.v2.RowFilter.InterleaveH\x00\x12<\n\tcondition\x18\x03 \x01(\x0b2\'.google.bigtable.v2.RowFilter.ConditionH\x00\x12\x0e\n\x04sink\x18\x10 \x01(\x08H\x00\x12\x19\n\x0fpass_all_filter\x18\x11 \x01(\x08H\x00\x12\x1a\n\x10block_all_filter\x18\x12 \x01(\x08H\x00\x12\x1e\n\x14row_key_regex_filter\x18\x04 \x01(\x0cH\x00\x12\x1b\n\x11row_sample_filter\x18\x0e \x01(\x01H\x00\x12"\n\x18family_name_regex_filter\x18\x05 \x01(\tH\x00\x12\'\n\x1dcolumn_qualifier_regex_filter\x18\x06 \x01(\x0cH\x00\x12>\n\x13column_range_filter\x18\x07 \x01(\x0b2\x1f.google.bigtable.v2.ColumnRangeH\x00\x12D\n\x16timestamp_range_filter\x18\x08 \x01(\x0b2".google.bigtable.v2.TimestampRangeH\x00\x12\x1c\n\x12value_regex_filter\x18\t \x01(\x0cH\x00\x12<\n\x12value_range_filter\x18\x0f \x01(\x0b2\x1e.google.bigtable.v2.ValueRangeH\x00\x12%\n\x1bcells_per_row_offset_filter\x18\n \x01(\x05H\x00\x12$\n\x1acells_per_row_limit_filter\x18\x0b \x01(\x05H\x00\x12\'\n\x1dcells_per_column_limit_filter\x18\x0c \x01(\x05H\x00\x12!\n\x17strip_value_transformer\x18\r \x01(\x08H\x00\x12!\n\x17apply_label_transformer\x18\x13 \x01(\tH\x00\x1a7\n\x05Chain\x12.\n\x07filters\x18\x01 \x03(\x0b2\x1d.google.bigtable.v2.RowFilter\x1a<\n\nInterleave\x12.\n\x07filters\x18\x01 \x03(\x0b2\x1d.google.bigtable.v2.RowFilter\x1a\xad\x01\n\tCondition\x127\n\x10predicate_filter\x18\x01 \x01(\x0b2\x1d.google.bigtable.v2.RowFilter\x122\n\x0btrue_filter\x18\x02 \x01(\x0b2\x1d.google.bigtable.v2.RowFilter\x123\n\x0cfalse_filter\x18\x03 \x01(\x0b2\x1d.google.bigtable.v2.RowFilterB\x08\n\x06filter"\xad\x08\n\x08Mutation\x128\n\x08set_cell\x18\x01 \x01(\x0b2$.google.bigtable.v2.Mutation.SetCellH\x00\x12=\n\x0badd_to_cell\x18\x05 \x01(\x0b2&.google.bigtable.v2.Mutation.AddToCellH\x00\x12A\n\rmerge_to_cell\x18\x06 \x01(\x0b2(.google.bigtable.v2.Mutation.MergeToCellH\x00\x12K\n\x12delete_from_column\x18\x02 \x01(\x0b2-.google.bigtable.v2.Mutation.DeleteFromColumnH\x00\x12K\n\x12delete_from_family\x18\x03 \x01(\x0b2-.google.bigtable.v2.Mutation.DeleteFromFamilyH\x00\x12E\n\x0fdelete_from_row\x18\x04 \x01(\x0b2*.google.bigtable.v2.Mutation.DeleteFromRowH\x00\x1aa\n\x07SetCell\x12\x13\n\x0bfamily_name\x18\x01 \x01(\t\x12\x18\n\x10column_qualifier\x18\x02 \x01(\x0c\x12\x18\n\x10timestamp_micros\x18\x03 \x01(\x03\x12\r\n\x05value\x18\x04 \x01(\x0c\x1a\xad\x01\n\tAddToCell\x12\x13\n\x0bfamily_name\x18\x01 \x01(\t\x123\n\x10column_qualifier\x18\x02 \x01(\x0b2\x19.google.bigtable.v2.Value\x12,\n\ttimestamp\x18\x03 \x01(\x0b2\x19.google.bigtable.v2.Value\x12(\n\x05input\x18\x04 \x01(\x0b2\x19.google.bigtable.v2.Value\x1a\xaf\x01\n\x0bMergeToCell\x12\x13\n\x0bfamily_name\x18\x01 \x01(\t\x123\n\x10column_qualifier\x18\x02 \x01(\x0b2\x19.google.bigtable.v2.Value\x12,\n\ttimestamp\x18\x03 \x01(\x0b2\x19.google.bigtable.v2.Value\x12(\n\x05input\x18\x04 \x01(\x0b2\x19.google.bigtable.v2.Value\x1ay\n\x10DeleteFromColumn\x12\x13\n\x0bfamily_name\x18\x01 \x01(\t\x12\x18\n\x10column_qualifier\x18\x02 \x01(\x0c\x126\n\ntime_range\x18\x03 \x01(\x0b2".google.bigtable.v2.TimestampRange\x1a\'\n\x10DeleteFromFamily\x12\x13\n\x0bfamily_name\x18\x01 \x01(\t\x1a\x0f\n\rDeleteFromRowB\n\n\x08mutation"\x80\x01\n\x13ReadModifyWriteRule\x12\x13\n\x0bfamily_name\x18\x01 \x01(\t\x12\x18\n\x10column_qualifier\x18\x02 \x01(\x0c\x12\x16\n\x0cappend_value\x18\x03 \x01(\x0cH\x00\x12\x1a\n\x10increment_amount\x18\x04 \x01(\x03H\x00B\x06\n\x04rule"B\n\x0fStreamPartition\x12/\n\trow_range\x18\x01 \x01(\x0b2\x1c.google.bigtable.v2.RowRange"W\n\x18StreamContinuationTokens\x12;\n\x06tokens\x18\x01 \x03(\x0b2+.google.bigtable.v2.StreamContinuationToken"`\n\x17StreamContinuationToken\x126\n\tpartition\x18\x01 \x01(\x0b2#.google.bigtable.v2.StreamPartition\x12\r\n\x05token\x18\x02 \x01(\t"\r\n\x0bProtoFormat"F\n\x0eColumnMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x04type\x18\x02 \x01(\x0b2\x18.google.bigtable.v2.Type"B\n\x0bProtoSchema\x123\n\x07columns\x18\x01 \x03(\x0b2".google.bigtable.v2.ColumnMetadata"V\n\x11ResultSetMetadata\x127\n\x0cproto_schema\x18\x01 \x01(\x0b2\x1f.google.bigtable.v2.ProtoSchemaH\x00B\x08\n\x06schema"6\n\tProtoRows\x12)\n\x06values\x18\x02 \x03(\x0b2\x19.google.bigtable.v2.Value"$\n\x0eProtoRowsBatch\x12\x12\n\nbatch_data\x18\x01 \x01(\x0c"\x96\x01\n\x10PartialResultSet\x12>\n\x10proto_rows_batch\x18\x03 \x01(\x0b2".google.bigtable.v2.ProtoRowsBatchH\x00\x12\x14\n\x0cresume_token\x18\x05 \x01(\x0c\x12\x1c\n\x14estimated_batch_size\x18\x04 \x01(\x05B\x0e\n\x0cpartial_rowsB\xb3\x01\n\x16com.google.bigtable.v2B\tDataProtoP\x01Z8cloud.google.com/go/bigtable/apiv2/bigtablepb;bigtablepb\xaa\x02\x18Google.Cloud.Bigtable.V2\xca\x02\x18Google\\Cloud\\Bigtable\\V2\xea\x02\x1bGoogle::Cloud::Bigtable::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.bigtable.v2.data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.bigtable.v2B\tDataProtoP\x01Z8cloud.google.com/go/bigtable/apiv2/bigtablepb;bigtablepb\xaa\x02\x18Google.Cloud.Bigtable.V2\xca\x02\x18Google\\Cloud\\Bigtable\\V2\xea\x02\x1bGoogle::Cloud::Bigtable::V2'
    _globals['_ROW']._serialized_start = 175
    _globals['_ROW']._serialized_end = 239
    _globals['_FAMILY']._serialized_start = 241
    _globals['_FAMILY']._serialized_end = 308
    _globals['_COLUMN']._serialized_start = 310
    _globals['_COLUMN']._serialized_end = 378
    _globals['_CELL']._serialized_start = 380
    _globals['_CELL']._serialized_end = 443
    _globals['_VALUE']._serialized_start = 446
    _globals['_VALUE']._serialized_end = 818
    _globals['_ARRAYVALUE']._serialized_start = 820
    _globals['_ARRAYVALUE']._serialized_end = 875
    _globals['_ROWRANGE']._serialized_start = 878
    _globals['_ROWRANGE']._serialized_end = 1016
    _globals['_ROWSET']._serialized_start = 1018
    _globals['_ROWSET']._serialized_end = 1094
    _globals['_COLUMNRANGE']._serialized_start = 1097
    _globals['_COLUMNRANGE']._serialized_end = 1295
    _globals['_TIMESTAMPRANGE']._serialized_start = 1297
    _globals['_TIMESTAMPRANGE']._serialized_end = 1375
    _globals['_VALUERANGE']._serialized_start = 1378
    _globals['_VALUERANGE']._serialized_end = 1530
    _globals['_ROWFILTER']._serialized_start = 1533
    _globals['_ROWFILTER']._serialized_end = 2652
    _globals['_ROWFILTER_CHAIN']._serialized_start = 2349
    _globals['_ROWFILTER_CHAIN']._serialized_end = 2404
    _globals['_ROWFILTER_INTERLEAVE']._serialized_start = 2406
    _globals['_ROWFILTER_INTERLEAVE']._serialized_end = 2466
    _globals['_ROWFILTER_CONDITION']._serialized_start = 2469
    _globals['_ROWFILTER_CONDITION']._serialized_end = 2642
    _globals['_MUTATION']._serialized_start = 2655
    _globals['_MUTATION']._serialized_end = 3724
    _globals['_MUTATION_SETCELL']._serialized_start = 3080
    _globals['_MUTATION_SETCELL']._serialized_end = 3177
    _globals['_MUTATION_ADDTOCELL']._serialized_start = 3180
    _globals['_MUTATION_ADDTOCELL']._serialized_end = 3353
    _globals['_MUTATION_MERGETOCELL']._serialized_start = 3356
    _globals['_MUTATION_MERGETOCELL']._serialized_end = 3531
    _globals['_MUTATION_DELETEFROMCOLUMN']._serialized_start = 3533
    _globals['_MUTATION_DELETEFROMCOLUMN']._serialized_end = 3654
    _globals['_MUTATION_DELETEFROMFAMILY']._serialized_start = 3656
    _globals['_MUTATION_DELETEFROMFAMILY']._serialized_end = 3695
    _globals['_MUTATION_DELETEFROMROW']._serialized_start = 3697
    _globals['_MUTATION_DELETEFROMROW']._serialized_end = 3712
    _globals['_READMODIFYWRITERULE']._serialized_start = 3727
    _globals['_READMODIFYWRITERULE']._serialized_end = 3855
    _globals['_STREAMPARTITION']._serialized_start = 3857
    _globals['_STREAMPARTITION']._serialized_end = 3923
    _globals['_STREAMCONTINUATIONTOKENS']._serialized_start = 3925
    _globals['_STREAMCONTINUATIONTOKENS']._serialized_end = 4012
    _globals['_STREAMCONTINUATIONTOKEN']._serialized_start = 4014
    _globals['_STREAMCONTINUATIONTOKEN']._serialized_end = 4110
    _globals['_PROTOFORMAT']._serialized_start = 4112
    _globals['_PROTOFORMAT']._serialized_end = 4125
    _globals['_COLUMNMETADATA']._serialized_start = 4127
    _globals['_COLUMNMETADATA']._serialized_end = 4197
    _globals['_PROTOSCHEMA']._serialized_start = 4199
    _globals['_PROTOSCHEMA']._serialized_end = 4265
    _globals['_RESULTSETMETADATA']._serialized_start = 4267
    _globals['_RESULTSETMETADATA']._serialized_end = 4353
    _globals['_PROTOROWS']._serialized_start = 4355
    _globals['_PROTOROWS']._serialized_end = 4409
    _globals['_PROTOROWSBATCH']._serialized_start = 4411
    _globals['_PROTOROWSBATCH']._serialized_end = 4447
    _globals['_PARTIALRESULTSET']._serialized_start = 4450
    _globals['_PARTIALRESULTSET']._serialized_end = 4600