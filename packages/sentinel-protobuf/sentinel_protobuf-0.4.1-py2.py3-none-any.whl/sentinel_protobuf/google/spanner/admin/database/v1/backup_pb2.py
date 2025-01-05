"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/admin/database/v1/backup.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.spanner.admin.database.v1 import common_pb2 as google_dot_spanner_dot_admin_dot_database_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/spanner/admin/database/v1/backup.proto\x12 google.spanner.admin.database.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-google/spanner/admin/database/v1/common.proto"\x90\t\n\x06Backup\x126\n\x08database\x18\x02 \x01(\tB$\xfaA!\n\x1fspanner.googleapis.com/Database\x120\n\x0cversion_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x17\n\nsize_bytes\x18\x05 \x01(\x03B\x03\xe0A\x03\x12 \n\x13freeable_size_bytes\x18\x0f \x01(\x03B\x03\xe0A\x03\x12!\n\x14exclusive_size_bytes\x18\x10 \x01(\x03B\x03\xe0A\x03\x12B\n\x05state\x18\x06 \x01(\x0e2..google.spanner.admin.database.v1.Backup.StateB\x03\xe0A\x03\x12F\n\x15referencing_databases\x18\x07 \x03(\tB\'\xe0A\x03\xfaA!\n\x1fspanner.googleapis.com/Database\x12N\n\x0fencryption_info\x18\x08 \x01(\x0b20.google.spanner.admin.database.v1.EncryptionInfoB\x03\xe0A\x03\x12U\n\x16encryption_information\x18\r \x03(\x0b20.google.spanner.admin.database.v1.EncryptionInfoB\x03\xe0A\x03\x12P\n\x10database_dialect\x18\n \x01(\x0e21.google.spanner.admin.database.v1.DatabaseDialectB\x03\xe0A\x03\x12B\n\x13referencing_backups\x18\x0b \x03(\tB%\xe0A\x03\xfaA\x1f\n\x1dspanner.googleapis.com/Backup\x128\n\x0fmax_expire_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x10backup_schedules\x18\x0e \x03(\tB-\xe0A\x03\xfaA\'\n%spanner.googleapis.com/BackupSchedule\x12(\n\x1bincremental_backup_chain_id\x18\x11 \x01(\tB\x03\xe0A\x03\x12<\n\x13oldest_version_time\x18\x12 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"7\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02:\\\xeaAY\n\x1dspanner.googleapis.com/Backup\x128projects/{project}/instances/{instance}/backups/{backup}"\x85\x02\n\x13CreateBackupRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance\x12\x16\n\tbackup_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12=\n\x06backup\x18\x03 \x01(\x0b2(.google.spanner.admin.database.v1.BackupB\x03\xe0A\x02\x12^\n\x11encryption_config\x18\x04 \x01(\x0b2>.google.spanner.admin.database.v1.CreateBackupEncryptionConfigB\x03\xe0A\x01"\xf8\x01\n\x14CreateBackupMetadata\x120\n\x04name\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dspanner.googleapis.com/Backup\x126\n\x08database\x18\x02 \x01(\tB$\xfaA!\n\x1fspanner.googleapis.com/Database\x12E\n\x08progress\x18\x03 \x01(\x0b23.google.spanner.admin.database.v1.OperationProgress\x12/\n\x0bcancel_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xb6\x02\n\x11CopyBackupRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance\x12\x16\n\tbackup_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12<\n\rsource_backup\x18\x03 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dspanner.googleapis.com/Backup\x124\n\x0bexpire_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12\\\n\x11encryption_config\x18\x05 \x01(\x0b2<.google.spanner.admin.database.v1.CopyBackupEncryptionConfigB\x03\xe0A\x01"\xf9\x01\n\x12CopyBackupMetadata\x120\n\x04name\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dspanner.googleapis.com/Backup\x129\n\rsource_backup\x18\x02 \x01(\tB"\xfaA\x1f\n\x1dspanner.googleapis.com/Backup\x12E\n\x08progress\x18\x03 \x01(\x0b23.google.spanner.admin.database.v1.OperationProgress\x12/\n\x0bcancel_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x8a\x01\n\x13UpdateBackupRequest\x12=\n\x06backup\x18\x01 \x01(\x0b2(.google.spanner.admin.database.v1.BackupB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"G\n\x10GetBackupRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dspanner.googleapis.com/Backup"J\n\x13DeleteBackupRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dspanner.googleapis.com/Backup"\x84\x01\n\x12ListBackupsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"i\n\x13ListBackupsResponse\x129\n\x07backups\x18\x01 \x03(\x0b2(.google.spanner.admin.database.v1.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8d\x01\n\x1bListBackupOperationsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"j\n\x1cListBackupOperationsResponse\x121\n\noperations\x18\x01 \x03(\x0b2\x1d.google.longrunning.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xe2\x01\n\nBackupInfo\x122\n\x06backup\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dspanner.googleapis.com/Backup\x120\n\x0cversion_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12=\n\x0fsource_database\x18\x03 \x01(\tB$\xfaA!\n\x1fspanner.googleapis.com/Database"\x9f\x03\n\x1cCreateBackupEncryptionConfig\x12k\n\x0fencryption_type\x18\x01 \x01(\x0e2M.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.EncryptionTypeB\x03\xe0A\x02\x12?\n\x0ckms_key_name\x18\x02 \x01(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12@\n\rkms_key_names\x18\x03 \x03(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey"\x8e\x01\n\x0eEncryptionType\x12\x1f\n\x1bENCRYPTION_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17USE_DATABASE_ENCRYPTION\x10\x01\x12\x1d\n\x19GOOGLE_DEFAULT_ENCRYPTION\x10\x02\x12\x1f\n\x1bCUSTOMER_MANAGED_ENCRYPTION\x10\x03"\xab\x03\n\x1aCopyBackupEncryptionConfig\x12i\n\x0fencryption_type\x18\x01 \x01(\x0e2K.google.spanner.admin.database.v1.CopyBackupEncryptionConfig.EncryptionTypeB\x03\xe0A\x02\x12?\n\x0ckms_key_name\x18\x02 \x01(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12@\n\rkms_key_names\x18\x03 \x03(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey"\x9e\x01\n\x0eEncryptionType\x12\x1f\n\x1bENCRYPTION_TYPE_UNSPECIFIED\x10\x00\x12+\n\'USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION\x10\x01\x12\x1d\n\x19GOOGLE_DEFAULT_ENCRYPTION\x10\x02\x12\x1f\n\x1bCUSTOMER_MANAGED_ENCRYPTION\x10\x03"\x10\n\x0eFullBackupSpec"\x17\n\x15IncrementalBackupSpecB\xfd\x01\n$com.google.spanner.admin.database.v1B\x0bBackupProtoP\x01ZFcloud.google.com/go/spanner/admin/database/apiv1/databasepb;databasepb\xaa\x02&Google.Cloud.Spanner.Admin.Database.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Database\\V1\xea\x02+Google::Cloud::Spanner::Admin::Database::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.admin.database.v1.backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.spanner.admin.database.v1B\x0bBackupProtoP\x01ZFcloud.google.com/go/spanner/admin/database/apiv1/databasepb;databasepb\xaa\x02&Google.Cloud.Spanner.Admin.Database.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Database\\V1\xea\x02+Google::Cloud::Spanner::Admin::Database::V1'
    _globals['_BACKUP'].fields_by_name['database']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['database']._serialized_options = b'\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_BACKUP'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['size_bytes']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['freeable_size_bytes']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['freeable_size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['exclusive_size_bytes']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['exclusive_size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['referencing_databases']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['referencing_databases']._serialized_options = b'\xe0A\x03\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_BACKUP'].fields_by_name['encryption_info']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['encryption_info']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['encryption_information']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['encryption_information']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['database_dialect']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['database_dialect']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['referencing_backups']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['referencing_backups']._serialized_options = b'\xe0A\x03\xfaA\x1f\n\x1dspanner.googleapis.com/Backup'
    _globals['_BACKUP'].fields_by_name['max_expire_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['max_expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['backup_schedules']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['backup_schedules']._serialized_options = b"\xe0A\x03\xfaA'\n%spanner.googleapis.com/BackupSchedule"
    _globals['_BACKUP'].fields_by_name['incremental_backup_chain_id']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['incremental_backup_chain_id']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['oldest_version_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['oldest_version_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP']._loaded_options = None
    _globals['_BACKUP']._serialized_options = b'\xeaAY\n\x1dspanner.googleapis.com/Backup\x128projects/{project}/instances/{instance}/backups/{backup}'
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance'
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['backup_id']._loaded_options = None
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['backup_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['backup']._loaded_options = None
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['backup']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['encryption_config']._loaded_options = None
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['encryption_config']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEBACKUPMETADATA'].fields_by_name['name']._loaded_options = None
    _globals['_CREATEBACKUPMETADATA'].fields_by_name['name']._serialized_options = b'\xfaA\x1f\n\x1dspanner.googleapis.com/Backup'
    _globals['_CREATEBACKUPMETADATA'].fields_by_name['database']._loaded_options = None
    _globals['_CREATEBACKUPMETADATA'].fields_by_name['database']._serialized_options = b'\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_COPYBACKUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_COPYBACKUPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance'
    _globals['_COPYBACKUPREQUEST'].fields_by_name['backup_id']._loaded_options = None
    _globals['_COPYBACKUPREQUEST'].fields_by_name['backup_id']._serialized_options = b'\xe0A\x02'
    _globals['_COPYBACKUPREQUEST'].fields_by_name['source_backup']._loaded_options = None
    _globals['_COPYBACKUPREQUEST'].fields_by_name['source_backup']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dspanner.googleapis.com/Backup'
    _globals['_COPYBACKUPREQUEST'].fields_by_name['expire_time']._loaded_options = None
    _globals['_COPYBACKUPREQUEST'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x02'
    _globals['_COPYBACKUPREQUEST'].fields_by_name['encryption_config']._loaded_options = None
    _globals['_COPYBACKUPREQUEST'].fields_by_name['encryption_config']._serialized_options = b'\xe0A\x01'
    _globals['_COPYBACKUPMETADATA'].fields_by_name['name']._loaded_options = None
    _globals['_COPYBACKUPMETADATA'].fields_by_name['name']._serialized_options = b'\xfaA\x1f\n\x1dspanner.googleapis.com/Backup'
    _globals['_COPYBACKUPMETADATA'].fields_by_name['source_backup']._loaded_options = None
    _globals['_COPYBACKUPMETADATA'].fields_by_name['source_backup']._serialized_options = b'\xfaA\x1f\n\x1dspanner.googleapis.com/Backup'
    _globals['_UPDATEBACKUPREQUEST'].fields_by_name['backup']._loaded_options = None
    _globals['_UPDATEBACKUPREQUEST'].fields_by_name['backup']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBACKUPREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBACKUPREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETBACKUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dspanner.googleapis.com/Backup'
    _globals['_DELETEBACKUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dspanner.googleapis.com/Backup'
    _globals['_LISTBACKUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance'
    _globals['_LISTBACKUPOPERATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPOPERATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance'
    _globals['_BACKUPINFO'].fields_by_name['backup']._loaded_options = None
    _globals['_BACKUPINFO'].fields_by_name['backup']._serialized_options = b'\xfaA\x1f\n\x1dspanner.googleapis.com/Backup'
    _globals['_BACKUPINFO'].fields_by_name['source_database']._loaded_options = None
    _globals['_BACKUPINFO'].fields_by_name['source_database']._serialized_options = b'\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_CREATEBACKUPENCRYPTIONCONFIG'].fields_by_name['encryption_type']._loaded_options = None
    _globals['_CREATEBACKUPENCRYPTIONCONFIG'].fields_by_name['encryption_type']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPENCRYPTIONCONFIG'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_CREATEBACKUPENCRYPTIONCONFIG'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_CREATEBACKUPENCRYPTIONCONFIG'].fields_by_name['kms_key_names']._loaded_options = None
    _globals['_CREATEBACKUPENCRYPTIONCONFIG'].fields_by_name['kms_key_names']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_COPYBACKUPENCRYPTIONCONFIG'].fields_by_name['encryption_type']._loaded_options = None
    _globals['_COPYBACKUPENCRYPTIONCONFIG'].fields_by_name['encryption_type']._serialized_options = b'\xe0A\x02'
    _globals['_COPYBACKUPENCRYPTIONCONFIG'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_COPYBACKUPENCRYPTIONCONFIG'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_COPYBACKUPENCRYPTIONCONFIG'].fields_by_name['kms_key_names']._loaded_options = None
    _globals['_COPYBACKUPENCRYPTIONCONFIG'].fields_by_name['kms_key_names']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_BACKUP']._serialized_start = 295
    _globals['_BACKUP']._serialized_end = 1463
    _globals['_BACKUP_STATE']._serialized_start = 1314
    _globals['_BACKUP_STATE']._serialized_end = 1369
    _globals['_CREATEBACKUPREQUEST']._serialized_start = 1466
    _globals['_CREATEBACKUPREQUEST']._serialized_end = 1727
    _globals['_CREATEBACKUPMETADATA']._serialized_start = 1730
    _globals['_CREATEBACKUPMETADATA']._serialized_end = 1978
    _globals['_COPYBACKUPREQUEST']._serialized_start = 1981
    _globals['_COPYBACKUPREQUEST']._serialized_end = 2291
    _globals['_COPYBACKUPMETADATA']._serialized_start = 2294
    _globals['_COPYBACKUPMETADATA']._serialized_end = 2543
    _globals['_UPDATEBACKUPREQUEST']._serialized_start = 2546
    _globals['_UPDATEBACKUPREQUEST']._serialized_end = 2684
    _globals['_GETBACKUPREQUEST']._serialized_start = 2686
    _globals['_GETBACKUPREQUEST']._serialized_end = 2757
    _globals['_DELETEBACKUPREQUEST']._serialized_start = 2759
    _globals['_DELETEBACKUPREQUEST']._serialized_end = 2833
    _globals['_LISTBACKUPSREQUEST']._serialized_start = 2836
    _globals['_LISTBACKUPSREQUEST']._serialized_end = 2968
    _globals['_LISTBACKUPSRESPONSE']._serialized_start = 2970
    _globals['_LISTBACKUPSRESPONSE']._serialized_end = 3075
    _globals['_LISTBACKUPOPERATIONSREQUEST']._serialized_start = 3078
    _globals['_LISTBACKUPOPERATIONSREQUEST']._serialized_end = 3219
    _globals['_LISTBACKUPOPERATIONSRESPONSE']._serialized_start = 3221
    _globals['_LISTBACKUPOPERATIONSRESPONSE']._serialized_end = 3327
    _globals['_BACKUPINFO']._serialized_start = 3330
    _globals['_BACKUPINFO']._serialized_end = 3556
    _globals['_CREATEBACKUPENCRYPTIONCONFIG']._serialized_start = 3559
    _globals['_CREATEBACKUPENCRYPTIONCONFIG']._serialized_end = 3974
    _globals['_CREATEBACKUPENCRYPTIONCONFIG_ENCRYPTIONTYPE']._serialized_start = 3832
    _globals['_CREATEBACKUPENCRYPTIONCONFIG_ENCRYPTIONTYPE']._serialized_end = 3974
    _globals['_COPYBACKUPENCRYPTIONCONFIG']._serialized_start = 3977
    _globals['_COPYBACKUPENCRYPTIONCONFIG']._serialized_end = 4404
    _globals['_COPYBACKUPENCRYPTIONCONFIG_ENCRYPTIONTYPE']._serialized_start = 4246
    _globals['_COPYBACKUPENCRYPTIONCONFIG_ENCRYPTIONTYPE']._serialized_end = 4404
    _globals['_FULLBACKUPSPEC']._serialized_start = 4406
    _globals['_FULLBACKUPSPEC']._serialized_end = 4422
    _globals['_INCREMENTALBACKUPSPEC']._serialized_start = 4424
    _globals['_INCREMENTALBACKUPSPEC']._serialized_end = 4447