"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1beta1/schema.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/datacatalog/v1beta1/schema.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1fgoogle/api/field_behavior.proto"N\n\x06Schema\x12D\n\x07columns\x18\x02 \x03(\x0b2..google.cloud.datacatalog.v1beta1.ColumnSchemaB\x03\xe0A\x02"\xac\x01\n\x0cColumnSchema\x12\x13\n\x06column\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04mode\x18\x03 \x01(\tB\x03\xe0A\x01\x12G\n\nsubcolumns\x18\x07 \x03(\x0b2..google.cloud.datacatalog.v1beta1.ColumnSchemaB\x03\xe0A\x01B\xdc\x01\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1beta1.schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1'
    _globals['_SCHEMA'].fields_by_name['columns']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['columns']._serialized_options = b'\xe0A\x02'
    _globals['_COLUMNSCHEMA'].fields_by_name['column']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['column']._serialized_options = b'\xe0A\x02'
    _globals['_COLUMNSCHEMA'].fields_by_name['type']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_COLUMNSCHEMA'].fields_by_name['description']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNSCHEMA'].fields_by_name['mode']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['mode']._serialized_options = b'\xe0A\x01'
    _globals['_COLUMNSCHEMA'].fields_by_name['subcolumns']._loaded_options = None
    _globals['_COLUMNSCHEMA'].fields_by_name['subcolumns']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA']._serialized_start = 116
    _globals['_SCHEMA']._serialized_end = 194
    _globals['_COLUMNSCHEMA']._serialized_start = 197
    _globals['_COLUMNSCHEMA']._serialized_end = 369