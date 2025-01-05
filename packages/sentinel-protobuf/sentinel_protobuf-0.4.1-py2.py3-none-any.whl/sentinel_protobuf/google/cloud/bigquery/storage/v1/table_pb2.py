"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1/table.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/bigquery/storage/v1/table.proto\x12 google.cloud.bigquery.storage.v1\x1a\x1fgoogle/api/field_behavior.proto"Q\n\x0bTableSchema\x12B\n\x06fields\x18\x01 \x03(\x0b22.google.cloud.bigquery.storage.v1.TableFieldSchema"\xfd\x06\n\x10TableFieldSchema\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12J\n\x04type\x18\x02 \x01(\x0e27.google.cloud.bigquery.storage.v1.TableFieldSchema.TypeB\x03\xe0A\x02\x12J\n\x04mode\x18\x03 \x01(\x0e27.google.cloud.bigquery.storage.v1.TableFieldSchema.ModeB\x03\xe0A\x01\x12G\n\x06fields\x18\x04 \x03(\x0b22.google.cloud.bigquery.storage.v1.TableFieldSchemaB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x17\n\nmax_length\x18\x07 \x01(\x03B\x03\xe0A\x01\x12\x16\n\tprecision\x18\x08 \x01(\x03B\x03\xe0A\x01\x12\x12\n\x05scale\x18\t \x01(\x03B\x03\xe0A\x01\x12%\n\x18default_value_expression\x18\n \x01(\tB\x03\xe0A\x01\x12d\n\x12range_element_type\x18\x0b \x01(\x0b2C.google.cloud.bigquery.storage.v1.TableFieldSchema.FieldElementTypeB\x03\xe0A\x01\x1a^\n\x10FieldElementType\x12J\n\x04type\x18\x01 \x01(\x0e27.google.cloud.bigquery.storage.v1.TableFieldSchema.TypeB\x03\xe0A\x02"\xe0\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\t\n\x05INT64\x10\x02\x12\n\n\x06DOUBLE\x10\x03\x12\n\n\x06STRUCT\x10\x04\x12\t\n\x05BYTES\x10\x05\x12\x08\n\x04BOOL\x10\x06\x12\r\n\tTIMESTAMP\x10\x07\x12\x08\n\x04DATE\x10\x08\x12\x08\n\x04TIME\x10\t\x12\x0c\n\x08DATETIME\x10\n\x12\r\n\tGEOGRAPHY\x10\x0b\x12\x0b\n\x07NUMERIC\x10\x0c\x12\x0e\n\nBIGNUMERIC\x10\r\x12\x0c\n\x08INTERVAL\x10\x0e\x12\x08\n\x04JSON\x10\x0f\x12\t\n\x05RANGE\x10\x10"F\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08NULLABLE\x10\x01\x12\x0c\n\x08REQUIRED\x10\x02\x12\x0c\n\x08REPEATED\x10\x03B\xba\x01\n$com.google.cloud.bigquery.storage.v1B\nTableProtoP\x01Z>cloud.google.com/go/bigquery/storage/apiv1/storagepb;storagepb\xaa\x02 Google.Cloud.BigQuery.Storage.V1\xca\x02 Google\\Cloud\\BigQuery\\Storage\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1.table_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.bigquery.storage.v1B\nTableProtoP\x01Z>cloud.google.com/go/bigquery/storage/apiv1/storagepb;storagepb\xaa\x02 Google.Cloud.BigQuery.Storage.V1\xca\x02 Google\\Cloud\\BigQuery\\Storage\\V1'
    _globals['_TABLEFIELDSCHEMA_FIELDELEMENTTYPE'].fields_by_name['type']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA_FIELDELEMENTTYPE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['name']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['type']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['mode']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['mode']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['fields']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['fields']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['description']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['max_length']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['max_length']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['precision']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['precision']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['scale']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['scale']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['default_value_expression']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['default_value_expression']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['range_element_type']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['range_element_type']._serialized_options = b'\xe0A\x01'
    _globals['_TABLESCHEMA']._serialized_start = 115
    _globals['_TABLESCHEMA']._serialized_end = 196
    _globals['_TABLEFIELDSCHEMA']._serialized_start = 199
    _globals['_TABLEFIELDSCHEMA']._serialized_end = 1092
    _globals['_TABLEFIELDSCHEMA_FIELDELEMENTTYPE']._serialized_start = 699
    _globals['_TABLEFIELDSCHEMA_FIELDELEMENTTYPE']._serialized_end = 793
    _globals['_TABLEFIELDSCHEMA_TYPE']._serialized_start = 796
    _globals['_TABLEFIELDSCHEMA_TYPE']._serialized_end = 1020
    _globals['_TABLEFIELDSCHEMA_MODE']._serialized_start = 1022
    _globals['_TABLEFIELDSCHEMA_MODE']._serialized_end = 1092