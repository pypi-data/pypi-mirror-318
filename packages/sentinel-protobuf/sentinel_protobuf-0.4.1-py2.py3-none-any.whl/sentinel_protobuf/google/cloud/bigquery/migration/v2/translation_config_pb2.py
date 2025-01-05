"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2/translation_config.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/bigquery/migration/v2/translation_config.proto\x12"google.cloud.bigquery.migration.v2\x1a\x1fgoogle/api/field_behavior.proto"\xe0\x03\n\x18TranslationConfigDetails\x12\x19\n\x0fgcs_source_path\x18\x01 \x01(\tH\x00\x12\x19\n\x0fgcs_target_path\x18\x02 \x01(\tH\x01\x12V\n\x11name_mapping_list\x18\x05 \x01(\x0b29.google.cloud.bigquery.migration.v2.ObjectNameMappingListH\x02\x12C\n\x0esource_dialect\x18\x03 \x01(\x0b2+.google.cloud.bigquery.migration.v2.Dialect\x12C\n\x0etarget_dialect\x18\x04 \x01(\x0b2+.google.cloud.bigquery.migration.v2.Dialect\x12A\n\nsource_env\x18\x06 \x01(\x0b2-.google.cloud.bigquery.migration.v2.SourceEnv\x12\x16\n\x0erequest_source\x18\x08 \x01(\t\x12\x14\n\x0ctarget_types\x18\t \x03(\tB\x11\n\x0fsource_locationB\x11\n\x0ftarget_locationB\x15\n\x13output_name_mapping"\xeb\n\n\x07Dialect\x12O\n\x10bigquery_dialect\x18\x01 \x01(\x0b23.google.cloud.bigquery.migration.v2.BigQueryDialectH\x00\x12K\n\x0ehiveql_dialect\x18\x02 \x01(\x0b21.google.cloud.bigquery.migration.v2.HiveQLDialectH\x00\x12O\n\x10redshift_dialect\x18\x03 \x01(\x0b23.google.cloud.bigquery.migration.v2.RedshiftDialectH\x00\x12O\n\x10teradata_dialect\x18\x04 \x01(\x0b23.google.cloud.bigquery.migration.v2.TeradataDialectH\x00\x12K\n\x0eoracle_dialect\x18\x05 \x01(\x0b21.google.cloud.bigquery.migration.v2.OracleDialectH\x00\x12O\n\x10sparksql_dialect\x18\x06 \x01(\x0b23.google.cloud.bigquery.migration.v2.SparkSQLDialectH\x00\x12Q\n\x11snowflake_dialect\x18\x07 \x01(\x0b24.google.cloud.bigquery.migration.v2.SnowflakeDialectH\x00\x12M\n\x0fnetezza_dialect\x18\x08 \x01(\x0b22.google.cloud.bigquery.migration.v2.NetezzaDialectH\x00\x12X\n\x15azure_synapse_dialect\x18\t \x01(\x0b27.google.cloud.bigquery.migration.v2.AzureSynapseDialectH\x00\x12M\n\x0fvertica_dialect\x18\n \x01(\x0b22.google.cloud.bigquery.migration.v2.VerticaDialectH\x00\x12R\n\x12sql_server_dialect\x18\x0b \x01(\x0b24.google.cloud.bigquery.migration.v2.SQLServerDialectH\x00\x12S\n\x12postgresql_dialect\x18\x0c \x01(\x0b25.google.cloud.bigquery.migration.v2.PostgresqlDialectH\x00\x12K\n\x0epresto_dialect\x18\r \x01(\x0b21.google.cloud.bigquery.migration.v2.PrestoDialectH\x00\x12I\n\rmysql_dialect\x18\x0e \x01(\x0b20.google.cloud.bigquery.migration.v2.MySQLDialectH\x00\x12E\n\x0bdb2_dialect\x18\x0f \x01(\x0b2..google.cloud.bigquery.migration.v2.DB2DialectH\x00\x12K\n\x0esqlite_dialect\x18\x10 \x01(\x0b21.google.cloud.bigquery.migration.v2.SQLiteDialectH\x00\x12Q\n\x11greenplum_dialect\x18\x11 \x01(\x0b24.google.cloud.bigquery.migration.v2.GreenplumDialectH\x00B\x0f\n\rdialect_value"\x11\n\x0fBigQueryDialect"\x0f\n\rHiveQLDialect"\x11\n\x0fRedshiftDialect"\x8a\x01\n\x0fTeradataDialect\x12F\n\x04mode\x18\x01 \x01(\x0e28.google.cloud.bigquery.migration.v2.TeradataDialect.Mode"/\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03SQL\x10\x01\x12\x08\n\x04BTEQ\x10\x02"\x0f\n\rOracleDialect"\x11\n\x0fSparkSQLDialect"\x12\n\x10SnowflakeDialect"\x10\n\x0eNetezzaDialect"\x15\n\x13AzureSynapseDialect"\x10\n\x0eVerticaDialect"\x12\n\x10SQLServerDialect"\x13\n\x11PostgresqlDialect"\x0f\n\rPrestoDialect"\x0e\n\x0cMySQLDialect"\x0c\n\nDB2Dialect"\x0f\n\rSQLiteDialect"\x12\n\x10GreenplumDialect"`\n\x15ObjectNameMappingList\x12G\n\x08name_map\x18\x01 \x03(\x0b25.google.cloud.bigquery.migration.v2.ObjectNameMapping"\x9d\x01\n\x11ObjectNameMapping\x12B\n\x06source\x18\x01 \x01(\x0b22.google.cloud.bigquery.migration.v2.NameMappingKey\x12D\n\x06target\x18\x02 \x01(\x0b24.google.cloud.bigquery.migration.v2.NameMappingValue"\xab\x02\n\x0eNameMappingKey\x12E\n\x04type\x18\x01 \x01(\x0e27.google.cloud.bigquery.migration.v2.NameMappingKey.Type\x12\x10\n\x08database\x18\x02 \x01(\t\x12\x0e\n\x06schema\x18\x03 \x01(\t\x12\x10\n\x08relation\x18\x04 \x01(\t\x12\x11\n\tattribute\x18\x05 \x01(\t"\x8a\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DATABASE\x10\x01\x12\n\n\x06SCHEMA\x10\x02\x12\x0c\n\x08RELATION\x10\x03\x12\r\n\tATTRIBUTE\x10\x04\x12\x12\n\x0eRELATION_ALIAS\x10\x05\x12\x13\n\x0fATTRIBUTE_ALIAS\x10\x06\x12\x0c\n\x08FUNCTION\x10\x07"Y\n\x10NameMappingValue\x12\x10\n\x08database\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x10\n\x08relation\x18\x03 \x01(\t\x12\x11\n\tattribute\x18\x04 \x01(\t"f\n\tSourceEnv\x12\x18\n\x10default_database\x18\x01 \x01(\t\x12\x1a\n\x12schema_search_path\x18\x02 \x03(\t\x12#\n\x16metadata_store_dataset\x18\x03 \x01(\tB\x03\xe0A\x01B\xd2\x01\n&com.google.cloud.bigquery.migration.v2B\x16TranslationConfigProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2.translation_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.bigquery.migration.v2B\x16TranslationConfigProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2'
    _globals['_SOURCEENV'].fields_by_name['metadata_store_dataset']._loaded_options = None
    _globals['_SOURCEENV'].fields_by_name['metadata_store_dataset']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSLATIONCONFIGDETAILS']._serialized_start = 133
    _globals['_TRANSLATIONCONFIGDETAILS']._serialized_end = 613
    _globals['_DIALECT']._serialized_start = 616
    _globals['_DIALECT']._serialized_end = 2003
    _globals['_BIGQUERYDIALECT']._serialized_start = 2005
    _globals['_BIGQUERYDIALECT']._serialized_end = 2022
    _globals['_HIVEQLDIALECT']._serialized_start = 2024
    _globals['_HIVEQLDIALECT']._serialized_end = 2039
    _globals['_REDSHIFTDIALECT']._serialized_start = 2041
    _globals['_REDSHIFTDIALECT']._serialized_end = 2058
    _globals['_TERADATADIALECT']._serialized_start = 2061
    _globals['_TERADATADIALECT']._serialized_end = 2199
    _globals['_TERADATADIALECT_MODE']._serialized_start = 2152
    _globals['_TERADATADIALECT_MODE']._serialized_end = 2199
    _globals['_ORACLEDIALECT']._serialized_start = 2201
    _globals['_ORACLEDIALECT']._serialized_end = 2216
    _globals['_SPARKSQLDIALECT']._serialized_start = 2218
    _globals['_SPARKSQLDIALECT']._serialized_end = 2235
    _globals['_SNOWFLAKEDIALECT']._serialized_start = 2237
    _globals['_SNOWFLAKEDIALECT']._serialized_end = 2255
    _globals['_NETEZZADIALECT']._serialized_start = 2257
    _globals['_NETEZZADIALECT']._serialized_end = 2273
    _globals['_AZURESYNAPSEDIALECT']._serialized_start = 2275
    _globals['_AZURESYNAPSEDIALECT']._serialized_end = 2296
    _globals['_VERTICADIALECT']._serialized_start = 2298
    _globals['_VERTICADIALECT']._serialized_end = 2314
    _globals['_SQLSERVERDIALECT']._serialized_start = 2316
    _globals['_SQLSERVERDIALECT']._serialized_end = 2334
    _globals['_POSTGRESQLDIALECT']._serialized_start = 2336
    _globals['_POSTGRESQLDIALECT']._serialized_end = 2355
    _globals['_PRESTODIALECT']._serialized_start = 2357
    _globals['_PRESTODIALECT']._serialized_end = 2372
    _globals['_MYSQLDIALECT']._serialized_start = 2374
    _globals['_MYSQLDIALECT']._serialized_end = 2388
    _globals['_DB2DIALECT']._serialized_start = 2390
    _globals['_DB2DIALECT']._serialized_end = 2402
    _globals['_SQLITEDIALECT']._serialized_start = 2404
    _globals['_SQLITEDIALECT']._serialized_end = 2419
    _globals['_GREENPLUMDIALECT']._serialized_start = 2421
    _globals['_GREENPLUMDIALECT']._serialized_end = 2439
    _globals['_OBJECTNAMEMAPPINGLIST']._serialized_start = 2441
    _globals['_OBJECTNAMEMAPPINGLIST']._serialized_end = 2537
    _globals['_OBJECTNAMEMAPPING']._serialized_start = 2540
    _globals['_OBJECTNAMEMAPPING']._serialized_end = 2697
    _globals['_NAMEMAPPINGKEY']._serialized_start = 2700
    _globals['_NAMEMAPPINGKEY']._serialized_end = 2999
    _globals['_NAMEMAPPINGKEY_TYPE']._serialized_start = 2861
    _globals['_NAMEMAPPINGKEY_TYPE']._serialized_end = 2999
    _globals['_NAMEMAPPINGVALUE']._serialized_start = 3001
    _globals['_NAMEMAPPINGVALUE']._serialized_end = 3090
    _globals['_SOURCEENV']._serialized_start = 3092
    _globals['_SOURCEENV']._serialized_end = 3194