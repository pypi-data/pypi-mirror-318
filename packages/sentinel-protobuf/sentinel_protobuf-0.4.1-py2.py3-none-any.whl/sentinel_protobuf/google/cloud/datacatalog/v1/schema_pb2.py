"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1/schema.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/datacatalog/v1/schema.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto"D\n\x06Schema\x12:\n\x07columns\x18\x02 \x03(\x0b2).google.cloud.datacatalog.v1.ColumnSchema"\xd5\x07\n\x0cColumnSchema\x12\x13\n\x06column\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04mode\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rdefault_value\x18\x08 \x01(\tB\x03\xe0A\x01\x12\x1d\n\x10ordinal_position\x18\t \x01(\x05B\x03\xe0A\x01\x12Z\n\x15highest_indexing_type\x18\n \x01(\x0e26.google.cloud.datacatalog.v1.ColumnSchema.IndexingTypeB\x03\xe0A\x01\x12B\n\nsubcolumns\x18\x07 \x03(\x0b2).google.cloud.datacatalog.v1.ColumnSchemaB\x03\xe0A\x01\x12X\n\x12looker_column_spec\x18\x12 \x01(\x0b2:.google.cloud.datacatalog.v1.ColumnSchema.LookerColumnSpecH\x00\x12[\n\x12range_element_type\x18\x13 \x01(\x0b2:.google.cloud.datacatalog.v1.ColumnSchema.FieldElementTypeB\x03\xe0A\x01\x12\x14\n\x07gc_rule\x18\x0b \x01(\tB\x03\xe0A\x01\x1a\xf2\x01\n\x10LookerColumnSpec\x12Y\n\x04type\x18\x01 \x01(\x0e2K.google.cloud.datacatalog.v1.ColumnSchema.LookerColumnSpec.LookerColumnType"\x82\x01\n\x10LookerColumnType\x12"\n\x1eLOOKER_COLUMN_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tDIMENSION\x10\x01\x12\x13\n\x0fDIMENSION_GROUP\x10\x02\x12\n\n\x06FILTER\x10\x03\x12\x0b\n\x07MEASURE\x10\x04\x12\r\n\tPARAMETER\x10\x05\x1a%\n\x10FieldElementType\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x02"\x9c\x01\n\x0cIndexingType\x12\x1d\n\x19INDEXING_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12INDEXING_TYPE_NONE\x10\x01\x12\x1c\n\x18INDEXING_TYPE_NON_UNIQUE\x10\x02\x12\x18\n\x14INDEXING_TYPE_UNIQUE\x10\x03\x12\x1d\n\x19INDEXING_TYPE_PRIMARY_KEY\x10\x04B\r\n\x0bsystem_specB\xc3\x01\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_COLUMNSCHEMA_FIELDELEMENTTYPE'].fields_by_name['type']._loaded_options = None
    _globals['_COLUMNSCHEMA_FIELDELEMENTTYPE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_COLUMNSCHEMA'].fields_by_name['column']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['column']._serialized_options = b'\xe0A\x02'
    _globals['_COLUMNSCHEMA'].fields_by_name['type']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_COLUMNSCHEMA'].fields_by_name['description']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNSCHEMA'].fields_by_name['mode']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['mode']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNSCHEMA'].fields_by_name['default_value']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['default_value']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNSCHEMA'].fields_by_name['ordinal_position']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['ordinal_position']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNSCHEMA'].fields_by_name['highest_indexing_type']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['highest_indexing_type']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNSCHEMA'].fields_by_name['subcolumns']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['subcolumns']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNSCHEMA'].fields_by_name['range_element_type']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['range_element_type']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNSCHEMA'].fields_by_name['gc_rule']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['gc_rule']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA']._serialized_start = 106
    _globals['_SCHEMA']._serialized_end = 174
    _globals['_COLUMNSCHEMA']._serialized_start = 177
    _globals['_COLUMNSCHEMA']._serialized_end = 1158
    _globals['_COLUMNSCHEMA_LOOKERCOLUMNSPEC']._serialized_start = 703
    _globals['_COLUMNSCHEMA_LOOKERCOLUMNSPEC']._serialized_end = 945
    _globals['_COLUMNSCHEMA_LOOKERCOLUMNSPEC_LOOKERCOLUMNTYPE']._serialized_start = 815
    _globals['_COLUMNSCHEMA_LOOKERCOLUMNSPEC_LOOKERCOLUMNTYPE']._serialized_end = 945
    _globals['_COLUMNSCHEMA_FIELDELEMENTTYPE']._serialized_start = 947
    _globals['_COLUMNSCHEMA_FIELDELEMENTTYPE']._serialized_end = 984
    _globals['_COLUMNSCHEMA_INDEXINGTYPE']._serialized_start = 987
    _globals['_COLUMNSCHEMA_INDEXINGTYPE']._serialized_end = 1143