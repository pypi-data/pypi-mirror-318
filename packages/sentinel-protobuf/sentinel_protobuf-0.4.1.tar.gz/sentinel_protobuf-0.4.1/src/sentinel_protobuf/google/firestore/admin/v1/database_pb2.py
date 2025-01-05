"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1/database.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/firestore/admin/v1/database.proto\x12\x19google.firestore.admin.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdc\x13\n\x08Database\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x03uid\x18\x03 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x0blocation_id\x18\t \x01(\t\x12>\n\x04type\x18\n \x01(\x0e20.google.firestore.admin.v1.Database.DatabaseType\x12M\n\x10concurrency_mode\x18\x0f \x01(\x0e23.google.firestore.admin.v1.Database.ConcurrencyMode\x12@\n\x18version_retention_period\x18\x11 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03\x12>\n\x15earliest_version_time\x18\x12 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12l\n!point_in_time_recovery_enablement\x18\x15 \x01(\x0e2A.google.firestore.admin.v1.Database.PointInTimeRecoveryEnablement\x12a\n\x1bapp_engine_integration_mode\x18\x13 \x01(\x0e2<.google.firestore.admin.v1.Database.AppEngineIntegrationMode\x12\x17\n\nkey_prefix\x18\x14 \x01(\tB\x03\xe0A\x03\x12Z\n\x17delete_protection_state\x18\x16 \x01(\x0e29.google.firestore.admin.v1.Database.DeleteProtectionState\x12H\n\x0bcmek_config\x18\x17 \x01(\x0b2..google.firestore.admin.v1.Database.CmekConfigB\x03\xe0A\x01\x12\x18\n\x0bprevious_id\x18\x19 \x01(\tB\x03\xe0A\x03\x12H\n\x0bsource_info\x18\x1a \x01(\x0b2..google.firestore.admin.v1.Database.SourceInfoB\x03\xe0A\x03\x12\x0c\n\x04etag\x18c \x01(\t\x1aH\n\nCmekConfig\x12\x19\n\x0ckms_key_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12active_key_version\x18\x02 \x03(\tB\x03\xe0A\x03\x1a\xe7\x01\n\nSourceInfo\x12M\n\x06backup\x18\x01 \x01(\x0b2;.google.firestore.admin.v1.Database.SourceInfo.BackupSourceH\x00\x12:\n\toperation\x18\x03 \x01(\tB\'\xfaA$\n"firestore.googleapis.com/Operation\x1aD\n\x0cBackupSource\x124\n\x06backup\x18\x01 \x01(\tB$\xfaA!\n\x1ffirestore.googleapis.com/BackupB\x08\n\x06source\x1a\x88\x04\n\x10EncryptionConfig\x12x\n\x19google_default_encryption\x18\x01 \x01(\x0b2S.google.firestore.admin.v1.Database.EncryptionConfig.GoogleDefaultEncryptionOptionsH\x00\x12m\n\x15use_source_encryption\x18\x02 \x01(\x0b2L.google.firestore.admin.v1.Database.EncryptionConfig.SourceEncryptionOptionsH\x00\x12|\n\x1bcustomer_managed_encryption\x18\x03 \x01(\x0b2U.google.firestore.admin.v1.Database.EncryptionConfig.CustomerManagedEncryptionOptionsH\x00\x1a \n\x1eGoogleDefaultEncryptionOptions\x1a\x19\n\x17SourceEncryptionOptions\x1a=\n CustomerManagedEncryptionOptions\x12\x19\n\x0ckms_key_name\x18\x01 \x01(\tB\x03\xe0A\x02B\x11\n\x0fencryption_type"W\n\x0cDatabaseType\x12\x1d\n\x19DATABASE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10FIRESTORE_NATIVE\x10\x01\x12\x12\n\x0eDATASTORE_MODE\x10\x02"w\n\x0fConcurrencyMode\x12 \n\x1cCONCURRENCY_MODE_UNSPECIFIED\x10\x00\x12\x0e\n\nOPTIMISTIC\x10\x01\x12\x0f\n\x0bPESSIMISTIC\x10\x02\x12!\n\x1dOPTIMISTIC_WITH_ENTITY_GROUPS\x10\x03"\x9b\x01\n\x1dPointInTimeRecoveryEnablement\x121\n-POINT_IN_TIME_RECOVERY_ENABLEMENT_UNSPECIFIED\x10\x00\x12"\n\x1ePOINT_IN_TIME_RECOVERY_ENABLED\x10\x01\x12#\n\x1fPOINT_IN_TIME_RECOVERY_DISABLED\x10\x02"b\n\x18AppEngineIntegrationMode\x12+\n\'APP_ENGINE_INTEGRATION_MODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02"\x7f\n\x15DeleteProtectionState\x12\'\n#DELETE_PROTECTION_STATE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aDELETE_PROTECTION_DISABLED\x10\x01\x12\x1d\n\x19DELETE_PROTECTION_ENABLED\x10\x02:R\xeaAO\n!firestore.googleapis.com/Database\x12\'projects/{project}/databases/{database}R\x01\x01B\xc3\x02\n\x1dcom.google.firestore.admin.v1B\rDatabaseProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1\xeaAd\n"firestore.googleapis.com/Operation\x12>projects/{project}/databases/{database}/operations/{operation}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1.database_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.firestore.admin.v1B\rDatabaseProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1\xeaAd\n"firestore.googleapis.com/Operation\x12>projects/{project}/databases/{database}/operations/{operation}'
    _globals['_DATABASE_CMEKCONFIG'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_DATABASE_CMEKCONFIG'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x02'
    _globals['_DATABASE_CMEKCONFIG'].fields_by_name['active_key_version']._loaded_options = None
    _globals['_DATABASE_CMEKCONFIG'].fields_by_name['active_key_version']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE_SOURCEINFO_BACKUPSOURCE'].fields_by_name['backup']._loaded_options = None
    _globals['_DATABASE_SOURCEINFO_BACKUPSOURCE'].fields_by_name['backup']._serialized_options = b'\xfaA!\n\x1ffirestore.googleapis.com/Backup'
    _globals['_DATABASE_SOURCEINFO'].fields_by_name['operation']._loaded_options = None
    _globals['_DATABASE_SOURCEINFO'].fields_by_name['operation']._serialized_options = b'\xfaA$\n"firestore.googleapis.com/Operation'
    _globals['_DATABASE_ENCRYPTIONCONFIG_CUSTOMERMANAGEDENCRYPTIONOPTIONS'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_DATABASE_ENCRYPTIONCONFIG_CUSTOMERMANAGEDENCRYPTIONOPTIONS'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x02'
    _globals['_DATABASE'].fields_by_name['uid']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['delete_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['version_retention_period']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['version_retention_period']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['earliest_version_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['earliest_version_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['key_prefix']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['key_prefix']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['cmek_config']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['cmek_config']._serialized_options = b'\xe0A\x01'
    _globals['_DATABASE'].fields_by_name['previous_id']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['previous_id']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['source_info']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['source_info']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE']._loaded_options = None
    _globals['_DATABASE']._serialized_options = b"\xeaAO\n!firestore.googleapis.com/Database\x12'projects/{project}/databases/{database}R\x01\x01"
    _globals['_DATABASE']._serialized_start = 197
    _globals['_DATABASE']._serialized_end = 2721
    _globals['_DATABASE_CMEKCONFIG']._serialized_start = 1211
    _globals['_DATABASE_CMEKCONFIG']._serialized_end = 1283
    _globals['_DATABASE_SOURCEINFO']._serialized_start = 1286
    _globals['_DATABASE_SOURCEINFO']._serialized_end = 1517
    _globals['_DATABASE_SOURCEINFO_BACKUPSOURCE']._serialized_start = 1439
    _globals['_DATABASE_SOURCEINFO_BACKUPSOURCE']._serialized_end = 1507
    _globals['_DATABASE_ENCRYPTIONCONFIG']._serialized_start = 1520
    _globals['_DATABASE_ENCRYPTIONCONFIG']._serialized_end = 2040
    _globals['_DATABASE_ENCRYPTIONCONFIG_GOOGLEDEFAULTENCRYPTIONOPTIONS']._serialized_start = 1899
    _globals['_DATABASE_ENCRYPTIONCONFIG_GOOGLEDEFAULTENCRYPTIONOPTIONS']._serialized_end = 1931
    _globals['_DATABASE_ENCRYPTIONCONFIG_SOURCEENCRYPTIONOPTIONS']._serialized_start = 1933
    _globals['_DATABASE_ENCRYPTIONCONFIG_SOURCEENCRYPTIONOPTIONS']._serialized_end = 1958
    _globals['_DATABASE_ENCRYPTIONCONFIG_CUSTOMERMANAGEDENCRYPTIONOPTIONS']._serialized_start = 1960
    _globals['_DATABASE_ENCRYPTIONCONFIG_CUSTOMERMANAGEDENCRYPTIONOPTIONS']._serialized_end = 2021
    _globals['_DATABASE_DATABASETYPE']._serialized_start = 2042
    _globals['_DATABASE_DATABASETYPE']._serialized_end = 2129
    _globals['_DATABASE_CONCURRENCYMODE']._serialized_start = 2131
    _globals['_DATABASE_CONCURRENCYMODE']._serialized_end = 2250
    _globals['_DATABASE_POINTINTIMERECOVERYENABLEMENT']._serialized_start = 2253
    _globals['_DATABASE_POINTINTIMERECOVERYENABLEMENT']._serialized_end = 2408
    _globals['_DATABASE_APPENGINEINTEGRATIONMODE']._serialized_start = 2410
    _globals['_DATABASE_APPENGINEINTEGRATIONMODE']._serialized_end = 2508
    _globals['_DATABASE_DELETEPROTECTIONSTATE']._serialized_start = 2510
    _globals['_DATABASE_DELETEPROTECTIONSTATE']._serialized_end = 2637