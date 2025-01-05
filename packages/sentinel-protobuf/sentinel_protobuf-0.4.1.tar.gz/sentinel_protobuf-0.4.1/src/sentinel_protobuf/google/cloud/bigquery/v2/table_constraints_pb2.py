"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/table_constraints.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.bigquery.v2 import table_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__reference__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/bigquery/v2/table_constraints.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/cloud/bigquery/v2/table_reference.proto""\n\nPrimaryKey\x12\x14\n\x07columns\x18\x01 \x03(\tB\x03\xe0A\x02"R\n\x0fColumnReference\x12\x1f\n\x12referencing_column\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11referenced_column\x18\x02 \x01(\tB\x03\xe0A\x02"\xb3\x01\n\nForeignKey\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12G\n\x10referenced_table\x18\x02 \x01(\x0b2(.google.cloud.bigquery.v2.TableReferenceB\x03\xe0A\x02\x12I\n\x11column_references\x18\x03 \x03(\x0b2).google.cloud.bigquery.v2.ColumnReferenceB\x03\xe0A\x02"\x93\x01\n\x10TableConstraints\x12>\n\x0bprimary_key\x18\x01 \x01(\x0b2$.google.cloud.bigquery.v2.PrimaryKeyB\x03\xe0A\x01\x12?\n\x0cforeign_keys\x18\x02 \x03(\x0b2$.google.cloud.bigquery.v2.ForeignKeyB\x03\xe0A\x01Bo\n\x1ccom.google.cloud.bigquery.v2B\x15TableConstraintsProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.table_constraints_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x15TableConstraintsProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_PRIMARYKEY'].fields_by_name['columns']._loaded_options = None
    _globals['_PRIMARYKEY'].fields_by_name['columns']._serialized_options = b'\xe0A\x02'
    _globals['_COLUMNREFERENCE'].fields_by_name['referencing_column']._loaded_options = None
    _globals['_COLUMNREFERENCE'].fields_by_name['referencing_column']._serialized_options = b'\xe0A\x02'
    _globals['_COLUMNREFERENCE'].fields_by_name['referenced_column']._loaded_options = None
    _globals['_COLUMNREFERENCE'].fields_by_name['referenced_column']._serialized_options = b'\xe0A\x02'
    _globals['_FOREIGNKEY'].fields_by_name['name']._loaded_options = None
    _globals['_FOREIGNKEY'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_FOREIGNKEY'].fields_by_name['referenced_table']._loaded_options = None
    _globals['_FOREIGNKEY'].fields_by_name['referenced_table']._serialized_options = b'\xe0A\x02'
    _globals['_FOREIGNKEY'].fields_by_name['column_references']._loaded_options = None
    _globals['_FOREIGNKEY'].fields_by_name['column_references']._serialized_options = b'\xe0A\x02'
    _globals['_TABLECONSTRAINTS'].fields_by_name['primary_key']._loaded_options = None
    _globals['_TABLECONSTRAINTS'].fields_by_name['primary_key']._serialized_options = b'\xe0A\x01'
    _globals['_TABLECONSTRAINTS'].fields_by_name['foreign_keys']._loaded_options = None
    _globals['_TABLECONSTRAINTS'].fields_by_name['foreign_keys']._serialized_options = b'\xe0A\x01'
    _globals['_PRIMARYKEY']._serialized_start = 159
    _globals['_PRIMARYKEY']._serialized_end = 193
    _globals['_COLUMNREFERENCE']._serialized_start = 195
    _globals['_COLUMNREFERENCE']._serialized_end = 277
    _globals['_FOREIGNKEY']._serialized_start = 280
    _globals['_FOREIGNKEY']._serialized_end = 459
    _globals['_TABLECONSTRAINTS']._serialized_start = 462
    _globals['_TABLECONSTRAINTS']._serialized_end = 609