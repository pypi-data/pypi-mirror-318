"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2/translation_usability.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/bigquery/migration/v2/translation_usability.proto\x12"google.cloud.bigquery.migration.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf6\x01\n\x13GcsReportLogMessage\x12\x10\n\x08severity\x18\x01 \x01(\t\x12\x10\n\x08category\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t\x12\x10\n\x08filename\x18\x04 \x01(\t\x12\x1a\n\x12source_script_line\x18\x05 \x01(\x05\x12\x1c\n\x14source_script_column\x18\x06 \x01(\x05\x12\x0f\n\x07message\x18\x07 \x01(\t\x12\x16\n\x0escript_context\x18\x08 \x01(\t\x12\x0e\n\x06action\x18\t \x01(\t\x12\x0e\n\x06effect\x18\n \x01(\t\x12\x13\n\x0bobject_name\x18\x0b \x01(\tB\xd5\x01\n&com.google.cloud.bigquery.migration.v2B\x19TranslationUsabilityProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2.translation_usability_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.bigquery.migration.v2B\x19TranslationUsabilityProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2'
    _globals['_GCSREPORTLOGMESSAGE']._serialized_start = 163
    _globals['_GCSREPORTLOGMESSAGE']._serialized_end = 409