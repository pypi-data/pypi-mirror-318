"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2/translation_details.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/bigquery/migration/v2/translation_details.proto\x12"google.cloud.bigquery.migration.v2\x1a\x1fgoogle/api/field_behavior.proto"\x8e\x02\n\x12TranslationDetails\x12V\n\x15source_target_mapping\x18\x01 \x03(\x0b27.google.cloud.bigquery.migration.v2.SourceTargetMapping\x12\x17\n\x0ftarget_base_uri\x18\x02 \x01(\t\x12Q\n\x12source_environment\x18\x03 \x01(\x0b25.google.cloud.bigquery.migration.v2.SourceEnvironment\x12\x1e\n\x16target_return_literals\x18\x04 \x03(\t\x12\x14\n\x0ctarget_types\x18\x05 \x03(\t"\x9f\x01\n\x13SourceTargetMapping\x12C\n\x0bsource_spec\x18\x01 \x01(\x0b2..google.cloud.bigquery.migration.v2.SourceSpec\x12C\n\x0btarget_spec\x18\x02 \x01(\x0b2..google.cloud.bigquery.migration.v2.TargetSpec"\x81\x01\n\nSourceSpec\x12\x12\n\x08base_uri\x18\x01 \x01(\tH\x00\x12>\n\x07literal\x18\x02 \x01(\x0b2+.google.cloud.bigquery.migration.v2.LiteralH\x00\x12\x15\n\x08encoding\x18\x03 \x01(\tB\x03\xe0A\x01B\x08\n\x06source"#\n\nTargetSpec\x12\x15\n\rrelative_path\x18\x01 \x01(\t"h\n\x07Literal\x12\x18\n\x0eliteral_string\x18\x02 \x01(\tH\x00\x12\x17\n\rliteral_bytes\x18\x03 \x01(\x0cH\x00\x12\x1a\n\rrelative_path\x18\x01 \x01(\tB\x03\xe0A\x02B\x0e\n\x0cliteral_data"n\n\x11SourceEnvironment\x12\x18\n\x10default_database\x18\x01 \x01(\t\x12\x1a\n\x12schema_search_path\x18\x02 \x03(\t\x12#\n\x16metadata_store_dataset\x18\x03 \x01(\tB\x03\xe0A\x01B\xd3\x01\n&com.google.cloud.bigquery.migration.v2B\x17TranslationDetailsProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2.translation_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.bigquery.migration.v2B\x17TranslationDetailsProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2'
    _globals['_SOURCESPEC'].fields_by_name['encoding']._loaded_options = None
    _globals['_SOURCESPEC'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_LITERAL'].fields_by_name['relative_path']._loaded_options = None
    _globals['_LITERAL'].fields_by_name['relative_path']._serialized_options = b'\xe0A\x02'
    _globals['_SOURCEENVIRONMENT'].fields_by_name['metadata_store_dataset']._loaded_options = None
    _globals['_SOURCEENVIRONMENT'].fields_by_name['metadata_store_dataset']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSLATIONDETAILS']._serialized_start = 134
    _globals['_TRANSLATIONDETAILS']._serialized_end = 404
    _globals['_SOURCETARGETMAPPING']._serialized_start = 407
    _globals['_SOURCETARGETMAPPING']._serialized_end = 566
    _globals['_SOURCESPEC']._serialized_start = 569
    _globals['_SOURCESPEC']._serialized_end = 698
    _globals['_TARGETSPEC']._serialized_start = 700
    _globals['_TARGETSPEC']._serialized_end = 735
    _globals['_LITERAL']._serialized_start = 737
    _globals['_LITERAL']._serialized_end = 841
    _globals['_SOURCEENVIRONMENT']._serialized_start = 843
    _globals['_SOURCEENVIRONMENT']._serialized_end = 953