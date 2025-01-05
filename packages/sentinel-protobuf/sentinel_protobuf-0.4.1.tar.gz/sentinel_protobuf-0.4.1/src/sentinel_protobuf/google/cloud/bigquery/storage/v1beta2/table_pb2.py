"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1beta2/table.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/bigquery/storage/v1beta2/table.proto\x12%google.cloud.bigquery.storage.v1beta2\x1a\x1fgoogle/api/field_behavior.proto"V\n\x0bTableSchema\x12G\n\x06fields\x18\x01 \x03(\x0b27.google.cloud.bigquery.storage.v1beta2.TableFieldSchema"\xcf\x04\n\x10TableFieldSchema\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12O\n\x04type\x18\x02 \x01(\x0e2<.google.cloud.bigquery.storage.v1beta2.TableFieldSchema.TypeB\x03\xe0A\x02\x12O\n\x04mode\x18\x03 \x01(\x0e2<.google.cloud.bigquery.storage.v1beta2.TableFieldSchema.ModeB\x03\xe0A\x01\x12L\n\x06fields\x18\x04 \x03(\x0b27.google.cloud.bigquery.storage.v1beta2.TableFieldSchemaB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x01"\xd5\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\t\n\x05INT64\x10\x02\x12\n\n\x06DOUBLE\x10\x03\x12\n\n\x06STRUCT\x10\x04\x12\t\n\x05BYTES\x10\x05\x12\x08\n\x04BOOL\x10\x06\x12\r\n\tTIMESTAMP\x10\x07\x12\x08\n\x04DATE\x10\x08\x12\x08\n\x04TIME\x10\t\x12\x0c\n\x08DATETIME\x10\n\x12\r\n\tGEOGRAPHY\x10\x0b\x12\x0b\n\x07NUMERIC\x10\x0c\x12\x0e\n\nBIGNUMERIC\x10\r\x12\x0c\n\x08INTERVAL\x10\x0e\x12\x08\n\x04JSON\x10\x0f"F\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08NULLABLE\x10\x01\x12\x0c\n\x08REQUIRED\x10\x02\x12\x0c\n\x08REPEATED\x10\x03B~\n)com.google.cloud.bigquery.storage.v1beta2B\nTableProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1beta2/storagepb;storagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1beta2.table_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1beta2B\nTableProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1beta2/storagepb;storagepb'
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
    _globals['_TABLESCHEMA']._serialized_start = 125
    _globals['_TABLESCHEMA']._serialized_end = 211
    _globals['_TABLEFIELDSCHEMA']._serialized_start = 214
    _globals['_TABLEFIELDSCHEMA']._serialized_end = 805
    _globals['_TABLEFIELDSCHEMA_TYPE']._serialized_start = 520
    _globals['_TABLEFIELDSCHEMA_TYPE']._serialized_end = 733
    _globals['_TABLEFIELDSCHEMA_MODE']._serialized_start = 735
    _globals['_TABLEFIELDSCHEMA_MODE']._serialized_end = 805