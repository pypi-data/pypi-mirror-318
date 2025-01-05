"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/external_catalog_dataset_options.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/bigquery/v2/external_catalog_dataset_options.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"\xdf\x01\n\x1dExternalCatalogDatasetOptions\x12`\n\nparameters\x18\x01 \x03(\x0b2G.google.cloud.bigquery.v2.ExternalCatalogDatasetOptions.ParametersEntryB\x03\xe0A\x01\x12)\n\x1cdefault_storage_location_uri\x18\x02 \x01(\tB\x03\xe0A\x01\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B~\n\x1ccom.google.cloud.bigquery.v2B"ExternalCatalogDatasetOptionsProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.external_catalog_dataset_options_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B"ExternalCatalogDatasetOptionsProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_EXTERNALCATALOGDATASETOPTIONS_PARAMETERSENTRY']._loaded_options = None
    _globals['_EXTERNALCATALOGDATASETOPTIONS_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_EXTERNALCATALOGDATASETOPTIONS'].fields_by_name['parameters']._loaded_options = None
    _globals['_EXTERNALCATALOGDATASETOPTIONS'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALCATALOGDATASETOPTIONS'].fields_by_name['default_storage_location_uri']._loaded_options = None
    _globals['_EXTERNALCATALOGDATASETOPTIONS'].fields_by_name['default_storage_location_uri']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALCATALOGDATASETOPTIONS']._serialized_start = 127
    _globals['_EXTERNALCATALOGDATASETOPTIONS']._serialized_end = 350
    _globals['_EXTERNALCATALOGDATASETOPTIONS_PARAMETERSENTRY']._serialized_start = 301
    _globals['_EXTERNALCATALOGDATASETOPTIONS_PARAMETERSENTRY']._serialized_end = 350