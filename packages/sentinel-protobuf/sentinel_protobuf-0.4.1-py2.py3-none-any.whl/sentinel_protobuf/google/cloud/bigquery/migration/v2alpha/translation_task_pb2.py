"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2alpha/translation_task.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/bigquery/migration/v2alpha/translation_task.proto\x12\'google.cloud.bigquery.migration.v2alpha"A\n\x16TranslationFileMapping\x12\x12\n\ninput_path\x18\x01 \x01(\t\x12\x13\n\x0boutput_path\x18\x02 \x01(\t"\xfa\x08\n\x16TranslationTaskDetails\x12T\n\x10teradata_options\x18\n \x01(\x0b28.google.cloud.bigquery.migration.v2alpha.TeradataOptionsH\x00\x12L\n\x0cbteq_options\x18\x0b \x01(\x0b24.google.cloud.bigquery.migration.v2alpha.BteqOptionsH\x00\x12\x12\n\ninput_path\x18\x01 \x01(\t\x12\x13\n\x0boutput_path\x18\x02 \x01(\t\x12S\n\nfile_paths\x18\x0c \x03(\x0b2?.google.cloud.bigquery.migration.v2alpha.TranslationFileMapping\x12\x13\n\x0bschema_path\x18\x03 \x01(\t\x12c\n\rfile_encoding\x18\x04 \x01(\x0e2L.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.FileEncoding\x12X\n\x13identifier_settings\x18\x05 \x01(\x0b2;.google.cloud.bigquery.migration.v2alpha.IdentifierSettings\x12o\n\x11special_token_map\x18\x06 \x03(\x0b2T.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.SpecialTokenMapEntry\x12?\n\x06filter\x18\x07 \x01(\x0b2/.google.cloud.bigquery.migration.v2alpha.Filter\x12#\n\x1btranslation_exception_table\x18\r \x01(\t\x1a\x81\x01\n\x14SpecialTokenMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12X\n\x05value\x18\x02 \x01(\x0e2I.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType:\x028\x01"~\n\x0cFileEncoding\x12\x1d\n\x19FILE_ENCODING_UNSPECIFIED\x10\x00\x12\t\n\x05UTF_8\x10\x01\x12\x0e\n\nISO_8859_1\x10\x02\x12\x0c\n\x08US_ASCII\x10\x03\x12\n\n\x06UTF_16\x10\x04\x12\x0c\n\x08UTF_16LE\x10\x05\x12\x0c\n\x08UTF_16BE\x10\x06"{\n\tTokenType\x12\x1a\n\x16TOKEN_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\t\n\x05INT64\x10\x02\x12\x0b\n\x07NUMERIC\x10\x03\x12\x08\n\x04BOOL\x10\x04\x12\x0b\n\x07FLOAT64\x10\x05\x12\x08\n\x04DATE\x10\x06\x12\r\n\tTIMESTAMP\x10\x07B\x12\n\x10language_options"/\n\x06Filter\x12%\n\x1dinput_file_exclusion_prefixes\x18\x01 \x03(\t"\xa8\x03\n\x12IdentifierSettings\x12j\n\x16output_identifier_case\x18\x01 \x01(\x0e2J.google.cloud.bigquery.migration.v2alpha.IdentifierSettings.IdentifierCase\x12r\n\x17identifier_rewrite_mode\x18\x02 \x01(\x0e2Q.google.cloud.bigquery.migration.v2alpha.IdentifierSettings.IdentifierRewriteMode"U\n\x0eIdentifierCase\x12\x1f\n\x1bIDENTIFIER_CASE_UNSPECIFIED\x10\x00\x12\x0c\n\x08ORIGINAL\x10\x01\x12\t\n\x05UPPER\x10\x02\x12\t\n\x05LOWER\x10\x03"[\n\x15IdentifierRewriteMode\x12\'\n#IDENTIFIER_REWRITE_MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x0f\n\x0bREWRITE_ALL\x10\x02"\x11\n\x0fTeradataOptions"\xa2\x02\n\x0bBteqOptions\x12R\n\x0fproject_dataset\x18\x01 \x01(\x0b29.google.cloud.bigquery.migration.v2alpha.DatasetReference\x12\x18\n\x10default_path_uri\x18\x02 \x01(\t\x12j\n\x14file_replacement_map\x18\x03 \x03(\x0b2L.google.cloud.bigquery.migration.v2alpha.BteqOptions.FileReplacementMapEntry\x1a9\n\x17FileReplacementMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01":\n\x10DatasetReference\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\tB\xe4\x01\n+com.google.cloud.bigquery.migration.v2alphaB\x14TranslationTaskProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02\'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02\'Google\\Cloud\\BigQuery\\Migration\\V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2alpha.translation_task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.bigquery.migration.v2alphaB\x14TranslationTaskProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02'Google\\Cloud\\BigQuery\\Migration\\V2alpha"
    _globals['_TRANSLATIONTASKDETAILS_SPECIALTOKENMAPENTRY']._loaded_options = None
    _globals['_TRANSLATIONTASKDETAILS_SPECIALTOKENMAPENTRY']._serialized_options = b'8\x01'
    _globals['_BTEQOPTIONS_FILEREPLACEMENTMAPENTRY']._loaded_options = None
    _globals['_BTEQOPTIONS_FILEREPLACEMENTMAPENTRY']._serialized_options = b'8\x01'
    _globals['_TRANSLATIONFILEMAPPING']._serialized_start = 107
    _globals['_TRANSLATIONFILEMAPPING']._serialized_end = 172
    _globals['_TRANSLATIONTASKDETAILS']._serialized_start = 175
    _globals['_TRANSLATIONTASKDETAILS']._serialized_end = 1321
    _globals['_TRANSLATIONTASKDETAILS_SPECIALTOKENMAPENTRY']._serialized_start = 919
    _globals['_TRANSLATIONTASKDETAILS_SPECIALTOKENMAPENTRY']._serialized_end = 1048
    _globals['_TRANSLATIONTASKDETAILS_FILEENCODING']._serialized_start = 1050
    _globals['_TRANSLATIONTASKDETAILS_FILEENCODING']._serialized_end = 1176
    _globals['_TRANSLATIONTASKDETAILS_TOKENTYPE']._serialized_start = 1178
    _globals['_TRANSLATIONTASKDETAILS_TOKENTYPE']._serialized_end = 1301
    _globals['_FILTER']._serialized_start = 1323
    _globals['_FILTER']._serialized_end = 1370
    _globals['_IDENTIFIERSETTINGS']._serialized_start = 1373
    _globals['_IDENTIFIERSETTINGS']._serialized_end = 1797
    _globals['_IDENTIFIERSETTINGS_IDENTIFIERCASE']._serialized_start = 1619
    _globals['_IDENTIFIERSETTINGS_IDENTIFIERCASE']._serialized_end = 1704
    _globals['_IDENTIFIERSETTINGS_IDENTIFIERREWRITEMODE']._serialized_start = 1706
    _globals['_IDENTIFIERSETTINGS_IDENTIFIERREWRITEMODE']._serialized_end = 1797
    _globals['_TERADATAOPTIONS']._serialized_start = 1799
    _globals['_TERADATAOPTIONS']._serialized_end = 1816
    _globals['_BTEQOPTIONS']._serialized_start = 1819
    _globals['_BTEQOPTIONS']._serialized_end = 2109
    _globals['_BTEQOPTIONS_FILEREPLACEMENTMAPENTRY']._serialized_start = 2052
    _globals['_BTEQOPTIONS_FILEREPLACEMENTMAPENTRY']._serialized_end = 2109
    _globals['_DATASETREFERENCE']._serialized_start = 2111
    _globals['_DATASETREFERENCE']._serialized_end = 2169