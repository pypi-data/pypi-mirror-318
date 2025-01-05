"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2/translation_suggestion.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/bigquery/migration/v2/translation_suggestion.proto\x12"google.cloud.bigquery.migration.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x88\x02\n\x17TranslationReportRecord\x12V\n\x08severity\x18\x01 \x01(\x0e2D.google.cloud.bigquery.migration.v2.TranslationReportRecord.Severity\x12\x13\n\x0bscript_line\x18\x02 \x01(\x05\x12\x15\n\rscript_column\x18\x03 \x01(\x05\x12\x10\n\x08category\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t"F\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x03B\xd6\x01\n&com.google.cloud.bigquery.migration.v2B\x1aTranslationSuggestionProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2.translation_suggestion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.bigquery.migration.v2B\x1aTranslationSuggestionProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2'
    _globals['_TRANSLATIONREPORTRECORD']._serialized_start = 164
    _globals['_TRANSLATIONREPORTRECORD']._serialized_end = 428
    _globals['_TRANSLATIONREPORTRECORD_SEVERITY']._serialized_start = 358
    _globals['_TRANSLATIONREPORTRECORD_SEVERITY']._serialized_end = 428