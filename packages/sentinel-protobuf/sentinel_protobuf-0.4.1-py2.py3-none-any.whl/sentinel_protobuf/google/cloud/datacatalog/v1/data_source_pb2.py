"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1/data_source.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/datacatalog/v1/data_source.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto"\x9c\x02\n\nDataSource\x12@\n\x07service\x18\x01 \x01(\x0e2/.google.cloud.datacatalog.v1.DataSource.Service\x12\x10\n\x08resource\x18\x02 \x01(\t\x12\x19\n\x0csource_entry\x18\x03 \x01(\tB\x03\xe0A\x03\x12L\n\x12storage_properties\x18\x04 \x01(\x0b2..google.cloud.datacatalog.v1.StoragePropertiesH\x00"C\n\x07Service\x12\x17\n\x13SERVICE_UNSPECIFIED\x10\x00\x12\x11\n\rCLOUD_STORAGE\x10\x01\x12\x0c\n\x08BIGQUERY\x10\x02B\x0c\n\nproperties"<\n\x11StorageProperties\x12\x14\n\x0cfile_pattern\x18\x01 \x03(\t\x12\x11\n\tfile_type\x18\x02 \x01(\tB\xd4\x01\n\x1fcom.google.cloud.datacatalog.v1B\x0fDataSourceProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.data_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1B\x0fDataSourceProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_DATASOURCE'].fields_by_name['source_entry']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['source_entry']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCE']._serialized_start = 112
    _globals['_DATASOURCE']._serialized_end = 396
    _globals['_DATASOURCE_SERVICE']._serialized_start = 315
    _globals['_DATASOURCE_SERVICE']._serialized_end = 382
    _globals['_STORAGEPROPERTIES']._serialized_start = 398
    _globals['_STORAGEPROPERTIES']._serialized_end = 458