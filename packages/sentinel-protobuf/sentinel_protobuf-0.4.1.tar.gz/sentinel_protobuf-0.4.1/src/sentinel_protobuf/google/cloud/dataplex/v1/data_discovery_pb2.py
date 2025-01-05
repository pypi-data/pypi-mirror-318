"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataplex/v1/data_discovery.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/dataplex/v1/data_discovery.proto\x12\x18google.cloud.dataplex.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xee\x07\n\x11DataDiscoverySpec\x12m\n\x1abigquery_publishing_config\x18\x01 \x01(\x0b2D.google.cloud.dataplex.v1.DataDiscoverySpec.BigQueryPublishingConfigB\x03\xe0A\x01\x12S\n\x0estorage_config\x18d \x01(\x0b29.google.cloud.dataplex.v1.DataDiscoverySpec.StorageConfigH\x00\x1a\x91\x02\n\x18BigQueryPublishingConfig\x12g\n\ntable_type\x18\x02 \x01(\x0e2N.google.cloud.dataplex.v1.DataDiscoverySpec.BigQueryPublishingConfig.TableTypeB\x03\xe0A\x01\x12H\n\nconnection\x18\x03 \x01(\tB4\xe0A\x01\xfaA.\n,bigqueryconnection.googleapis.com/Connection"B\n\tTableType\x12\x1a\n\x16TABLE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08EXTERNAL\x10\x01\x12\x0b\n\x07BIGLAKE\x10\x02\x1a\xed\x03\n\rStorageConfig\x12\x1d\n\x10include_patterns\x18\x01 \x03(\tB\x03\xe0A\x01\x12\x1d\n\x10exclude_patterns\x18\x02 \x03(\tB\x03\xe0A\x01\x12^\n\x0bcsv_options\x18\x03 \x01(\x0b2D.google.cloud.dataplex.v1.DataDiscoverySpec.StorageConfig.CsvOptionsB\x03\xe0A\x01\x12`\n\x0cjson_options\x18\x04 \x01(\x0b2E.google.cloud.dataplex.v1.DataDiscoverySpec.StorageConfig.JsonOptionsB\x03\xe0A\x01\x1a\x8f\x01\n\nCsvOptions\x12\x18\n\x0bheader_rows\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x16\n\tdelimiter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08encoding\x18\x03 \x01(\tB\x03\xe0A\x01\x12$\n\x17type_inference_disabled\x18\x04 \x01(\x08B\x03\xe0A\x01\x12\x12\n\x05quote\x18\x05 \x01(\tB\x03\xe0A\x01\x1aJ\n\x0bJsonOptions\x12\x15\n\x08encoding\x18\x01 \x01(\tB\x03\xe0A\x01\x12$\n\x17type_inference_disabled\x18\x02 \x01(\x08B\x03\xe0A\x01B\x11\n\x0fresource_config"\xc9\x01\n\x13DataDiscoveryResult\x12b\n\x13bigquery_publishing\x18\x01 \x01(\x0b2@.google.cloud.dataplex.v1.DataDiscoveryResult.BigQueryPublishingB\x03\xe0A\x03\x1aN\n\x12BigQueryPublishing\x128\n\x07dataset\x18\x01 \x01(\tB\'\xe0A\x03\xfaA!\n\x1fbigquery.googleapis.com/DatasetB\xac\x02\n\x1ccom.google.cloud.dataplex.v1B\x12DataDiscoveryProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb\xeaAH\n\x1fbigquery.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}\xeaAp\n,bigqueryconnection.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.data_discovery_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\x12DataDiscoveryProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb\xeaAH\n\x1fbigquery.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}\xeaAp\n,bigqueryconnection.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}'
    _globals['_DATADISCOVERYSPEC_BIGQUERYPUBLISHINGCONFIG'].fields_by_name['table_type']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_BIGQUERYPUBLISHINGCONFIG'].fields_by_name['table_type']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_BIGQUERYPUBLISHINGCONFIG'].fields_by_name['connection']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_BIGQUERYPUBLISHINGCONFIG'].fields_by_name['connection']._serialized_options = b'\xe0A\x01\xfaA.\n,bigqueryconnection.googleapis.com/Connection'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['header_rows']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['header_rows']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['delimiter']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['delimiter']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['encoding']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['type_inference_disabled']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['type_inference_disabled']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['quote']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS'].fields_by_name['quote']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_JSONOPTIONS'].fields_by_name['encoding']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_JSONOPTIONS'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_JSONOPTIONS'].fields_by_name['type_inference_disabled']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_JSONOPTIONS'].fields_by_name['type_inference_disabled']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG'].fields_by_name['include_patterns']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG'].fields_by_name['include_patterns']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG'].fields_by_name['exclude_patterns']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG'].fields_by_name['exclude_patterns']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG'].fields_by_name['csv_options']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG'].fields_by_name['csv_options']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG'].fields_by_name['json_options']._loaded_options = None
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG'].fields_by_name['json_options']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYSPEC'].fields_by_name['bigquery_publishing_config']._loaded_options = None
    _globals['_DATADISCOVERYSPEC'].fields_by_name['bigquery_publishing_config']._serialized_options = b'\xe0A\x01'
    _globals['_DATADISCOVERYRESULT_BIGQUERYPUBLISHING'].fields_by_name['dataset']._loaded_options = None
    _globals['_DATADISCOVERYRESULT_BIGQUERYPUBLISHING'].fields_by_name['dataset']._serialized_options = b'\xe0A\x03\xfaA!\n\x1fbigquery.googleapis.com/Dataset'
    _globals['_DATADISCOVERYRESULT'].fields_by_name['bigquery_publishing']._loaded_options = None
    _globals['_DATADISCOVERYRESULT'].fields_by_name['bigquery_publishing']._serialized_options = b'\xe0A\x03'
    _globals['_DATADISCOVERYSPEC']._serialized_start = 136
    _globals['_DATADISCOVERYSPEC']._serialized_end = 1142
    _globals['_DATADISCOVERYSPEC_BIGQUERYPUBLISHINGCONFIG']._serialized_start = 354
    _globals['_DATADISCOVERYSPEC_BIGQUERYPUBLISHINGCONFIG']._serialized_end = 627
    _globals['_DATADISCOVERYSPEC_BIGQUERYPUBLISHINGCONFIG_TABLETYPE']._serialized_start = 561
    _globals['_DATADISCOVERYSPEC_BIGQUERYPUBLISHINGCONFIG_TABLETYPE']._serialized_end = 627
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG']._serialized_start = 630
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG']._serialized_end = 1123
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS']._serialized_start = 904
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_CSVOPTIONS']._serialized_end = 1047
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_JSONOPTIONS']._serialized_start = 1049
    _globals['_DATADISCOVERYSPEC_STORAGECONFIG_JSONOPTIONS']._serialized_end = 1123
    _globals['_DATADISCOVERYRESULT']._serialized_start = 1145
    _globals['_DATADISCOVERYRESULT']._serialized_end = 1346
    _globals['_DATADISCOVERYRESULT_BIGQUERYPUBLISHING']._serialized_start = 1268
    _globals['_DATADISCOVERYRESULT_BIGQUERYPUBLISHING']._serialized_end = 1346