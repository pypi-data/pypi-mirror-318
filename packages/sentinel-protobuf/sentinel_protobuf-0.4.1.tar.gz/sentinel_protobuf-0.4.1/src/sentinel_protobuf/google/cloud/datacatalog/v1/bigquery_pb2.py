"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1/bigquery.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/datacatalog/v1/bigquery.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto"\xb4\x02\n\x16BigQueryConnectionSpec\x12[\n\x0fconnection_type\x18\x01 \x01(\x0e2B.google.cloud.datacatalog.v1.BigQueryConnectionSpec.ConnectionType\x12P\n\tcloud_sql\x18\x02 \x01(\x0b2;.google.cloud.datacatalog.v1.CloudSqlBigQueryConnectionSpecH\x00\x12\x16\n\x0ehas_credential\x18\x03 \x01(\x08"@\n\x0eConnectionType\x12\x1f\n\x1bCONNECTION_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tCLOUD_SQL\x10\x01B\x11\n\x0fconnection_spec"\xe7\x01\n\x1eCloudSqlBigQueryConnectionSpec\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x10\n\x08database\x18\x02 \x01(\t\x12V\n\x04type\x18\x03 \x01(\x0e2H.google.cloud.datacatalog.v1.CloudSqlBigQueryConnectionSpec.DatabaseType"F\n\x0cDatabaseType\x12\x1d\n\x19DATABASE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08POSTGRES\x10\x01\x12\t\n\x05MYSQL\x10\x02"1\n\x13BigQueryRoutineSpec\x12\x1a\n\x12imported_libraries\x18\x01 \x03(\tB\xd2\x01\n\x1fcom.google.cloud.datacatalog.v1B\rBigQueryProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.bigquery_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1B\rBigQueryProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_BIGQUERYCONNECTIONSPEC']._serialized_start = 109
    _globals['_BIGQUERYCONNECTIONSPEC']._serialized_end = 417
    _globals['_BIGQUERYCONNECTIONSPEC_CONNECTIONTYPE']._serialized_start = 334
    _globals['_BIGQUERYCONNECTIONSPEC_CONNECTIONTYPE']._serialized_end = 398
    _globals['_CLOUDSQLBIGQUERYCONNECTIONSPEC']._serialized_start = 420
    _globals['_CLOUDSQLBIGQUERYCONNECTIONSPEC']._serialized_end = 651
    _globals['_CLOUDSQLBIGQUERYCONNECTIONSPEC_DATABASETYPE']._serialized_start = 581
    _globals['_CLOUDSQLBIGQUERYCONNECTIONSPEC_DATABASETYPE']._serialized_end = 651
    _globals['_BIGQUERYROUTINESPEC']._serialized_start = 653
    _globals['_BIGQUERYROUTINESPEC']._serialized_end = 702