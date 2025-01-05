"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2alpha/translation_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/bigquery/migration/v2alpha/translation_service.proto\x12\'google.cloud.bigquery.migration.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xbc\x02\n\x15TranslateQueryRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12w\n\x0esource_dialect\x18\x02 \x01(\x0e2Z.google.cloud.bigquery.migration.v2alpha.TranslateQueryRequest.SqlTranslationSourceDialectB\x03\xe0A\x02\x12\x12\n\x05query\x18\x03 \x01(\tB\x03\xe0A\x02"[\n\x1bSqlTranslationSourceDialect\x12.\n*SQL_TRANSLATION_SOURCE_DIALECT_UNSPECIFIED\x10\x00\x12\x0c\n\x08TERADATA\x10\x01"\xf3\x01\n\x16TranslateQueryResponse\x12\x1f\n\x0ftranslation_job\x18\x04 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x18\n\x10translated_query\x18\x01 \x01(\t\x12L\n\x06errors\x18\x02 \x03(\x0b2<.google.cloud.bigquery.migration.v2alpha.SqlTranslationError\x12P\n\x08warnings\x18\x03 \x03(\x0b2>.google.cloud.bigquery.migration.v2alpha.SqlTranslationWarning"I\n\x19SqlTranslationErrorDetail\x12\x0b\n\x03row\x18\x01 \x01(\x03\x12\x0e\n\x06column\x18\x02 \x01(\x03\x12\x0f\n\x07message\x18\x03 \x01(\t"\xd3\x02\n\x13SqlTranslationError\x12h\n\nerror_type\x18\x01 \x01(\x0e2T.google.cloud.bigquery.migration.v2alpha.SqlTranslationError.SqlTranslationErrorType\x12X\n\x0cerror_detail\x18\x02 \x01(\x0b2B.google.cloud.bigquery.migration.v2alpha.SqlTranslationErrorDetail"x\n\x17SqlTranslationErrorType\x12*\n&SQL_TRANSLATION_ERROR_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSQL_PARSE_ERROR\x10\x01\x12\x1c\n\x18UNSUPPORTED_SQL_FUNCTION\x10\x02"s\n\x15SqlTranslationWarning\x12Z\n\x0ewarning_detail\x18\x01 \x01(\x0b2B.google.cloud.bigquery.migration.v2alpha.SqlTranslationErrorDetail2\xe3\x02\n\x15SqlTranslationService\x12\xf3\x01\n\x0eTranslateQuery\x12>.google.cloud.bigquery.migration.v2alpha.TranslateQueryRequest\x1a?.google.cloud.bigquery.migration.v2alpha.TranslateQueryResponse"`\xdaA\x1bparent,source_dialect,query\x82\xd3\xe4\x93\x02<"7/v2alpha/{parent=projects/*/locations/*}:translateQuery:\x01*\x1aT\xcaA bigquerymigration.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe7\x01\n+com.google.cloud.bigquery.migration.v2alphaB\x17TranslationServiceProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02\'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02\'Google\\Cloud\\BigQuery\\Migration\\V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2alpha.translation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.bigquery.migration.v2alphaB\x17TranslationServiceProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02'Google\\Cloud\\BigQuery\\Migration\\V2alpha"
    _globals['_TRANSLATEQUERYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_TRANSLATEQUERYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_TRANSLATEQUERYREQUEST'].fields_by_name['source_dialect']._loaded_options = None
    _globals['_TRANSLATEQUERYREQUEST'].fields_by_name['source_dialect']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATEQUERYREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_TRANSLATEQUERYREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATEQUERYRESPONSE'].fields_by_name['translation_job']._loaded_options = None
    _globals['_TRANSLATEQUERYRESPONSE'].fields_by_name['translation_job']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_SQLTRANSLATIONSERVICE']._loaded_options = None
    _globals['_SQLTRANSLATIONSERVICE']._serialized_options = b'\xcaA bigquerymigration.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SQLTRANSLATIONSERVICE'].methods_by_name['TranslateQuery']._loaded_options = None
    _globals['_SQLTRANSLATIONSERVICE'].methods_by_name['TranslateQuery']._serialized_options = b'\xdaA\x1bparent,source_dialect,query\x82\xd3\xe4\x93\x02<"7/v2alpha/{parent=projects/*/locations/*}:translateQuery:\x01*'
    _globals['_TRANSLATEQUERYREQUEST']._serialized_start = 226
    _globals['_TRANSLATEQUERYREQUEST']._serialized_end = 542
    _globals['_TRANSLATEQUERYREQUEST_SQLTRANSLATIONSOURCEDIALECT']._serialized_start = 451
    _globals['_TRANSLATEQUERYREQUEST_SQLTRANSLATIONSOURCEDIALECT']._serialized_end = 542
    _globals['_TRANSLATEQUERYRESPONSE']._serialized_start = 545
    _globals['_TRANSLATEQUERYRESPONSE']._serialized_end = 788
    _globals['_SQLTRANSLATIONERRORDETAIL']._serialized_start = 790
    _globals['_SQLTRANSLATIONERRORDETAIL']._serialized_end = 863
    _globals['_SQLTRANSLATIONERROR']._serialized_start = 866
    _globals['_SQLTRANSLATIONERROR']._serialized_end = 1205
    _globals['_SQLTRANSLATIONERROR_SQLTRANSLATIONERRORTYPE']._serialized_start = 1085
    _globals['_SQLTRANSLATIONERROR_SQLTRANSLATIONERRORTYPE']._serialized_end = 1205
    _globals['_SQLTRANSLATIONWARNING']._serialized_start = 1207
    _globals['_SQLTRANSLATIONWARNING']._serialized_end = 1322
    _globals['_SQLTRANSLATIONSERVICE']._serialized_start = 1325
    _globals['_SQLTRANSLATIONSERVICE']._serialized_end = 1680