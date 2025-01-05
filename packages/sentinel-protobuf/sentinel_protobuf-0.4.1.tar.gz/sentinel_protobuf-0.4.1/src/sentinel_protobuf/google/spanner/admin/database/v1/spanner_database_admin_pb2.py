"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/admin/database/v1/spanner_database_admin.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from ......google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.spanner.admin.database.v1 import backup_pb2 as google_dot_spanner_dot_admin_dot_database_dot_v1_dot_backup__pb2
from ......google.spanner.admin.database.v1 import backup_schedule_pb2 as google_dot_spanner_dot_admin_dot_database_dot_v1_dot_backup__schedule__pb2
from ......google.spanner.admin.database.v1 import common_pb2 as google_dot_spanner_dot_admin_dot_database_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/spanner/admin/database/v1/spanner_database_admin.proto\x12 google.spanner.admin.database.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-google/spanner/admin/database/v1/backup.proto\x1a6google/spanner/admin/database/v1/backup_schedule.proto\x1a-google/spanner/admin/database/v1/common.proto"\xab\x01\n\x0bRestoreInfo\x12H\n\x0bsource_type\x18\x01 \x01(\x0e23.google.spanner.admin.database.v1.RestoreSourceType\x12C\n\x0bbackup_info\x18\x02 \x01(\x0b2,.google.spanner.admin.database.v1.BackupInfoH\x00B\r\n\x0bsource_info"\xca\x06\n\x08Database\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12D\n\x05state\x18\x02 \x01(\x0e20.google.spanner.admin.database.v1.Database.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x0crestore_info\x18\x04 \x01(\x0b2-.google.spanner.admin.database.v1.RestoreInfoB\x03\xe0A\x03\x12R\n\x11encryption_config\x18\x05 \x01(\x0b22.google.spanner.admin.database.v1.EncryptionConfigB\x03\xe0A\x03\x12N\n\x0fencryption_info\x18\x08 \x03(\x0b20.google.spanner.admin.database.v1.EncryptionInfoB\x03\xe0A\x03\x12%\n\x18version_retention_period\x18\x06 \x01(\tB\x03\xe0A\x03\x12>\n\x15earliest_version_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1b\n\x0edefault_leader\x18\t \x01(\tB\x03\xe0A\x03\x12P\n\x10database_dialect\x18\n \x01(\x0e21.google.spanner.admin.database.v1.DatabaseDialectB\x03\xe0A\x03\x12\x1e\n\x16enable_drop_protection\x18\x0b \x01(\x08\x12\x18\n\x0breconciling\x18\x0c \x01(\x08B\x03\xe0A\x03"M\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x14\n\x10READY_OPTIMIZING\x10\x03:b\xeaA_\n\x1fspanner.googleapis.com/Database\x12<projects/{project}/instances/{instance}/databases/{database}"v\n\x14ListDatabasesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"o\n\x15ListDatabasesResponse\x12=\n\tdatabases\x18\x01 \x03(\x0b2*.google.spanner.admin.database.v1.Database\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xd4\x02\n\x15CreateDatabaseRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance\x12\x1d\n\x10create_statement\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10extra_statements\x18\x03 \x03(\tB\x03\xe0A\x01\x12R\n\x11encryption_config\x18\x04 \x01(\x0b22.google.spanner.admin.database.v1.EncryptionConfigB\x03\xe0A\x01\x12P\n\x10database_dialect\x18\x05 \x01(\x0e21.google.spanner.admin.database.v1.DatabaseDialectB\x03\xe0A\x01\x12\x1e\n\x11proto_descriptors\x18\x06 \x01(\x0cB\x03\xe0A\x01"P\n\x16CreateDatabaseMetadata\x126\n\x08database\x18\x01 \x01(\tB$\xfaA!\n\x1fspanner.googleapis.com/Database"K\n\x12GetDatabaseRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database"\x90\x01\n\x15UpdateDatabaseRequest\x12A\n\x08database\x18\x01 \x01(\x0b2*.google.spanner.admin.database.v1.DatabaseB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xda\x01\n\x16UpdateDatabaseMetadata\x12H\n\x07request\x18\x01 \x01(\x0b27.google.spanner.admin.database.v1.UpdateDatabaseRequest\x12E\n\x08progress\x18\x02 \x01(\x0b23.google.spanner.admin.database.v1.OperationProgress\x12/\n\x0bcancel_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xa4\x01\n\x18UpdateDatabaseDdlRequest\x129\n\x08database\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database\x12\x17\n\nstatements\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x14\n\x0coperation_id\x18\x03 \x01(\t\x12\x1e\n\x11proto_descriptors\x18\x04 \x01(\x0cB\x03\xe0A\x01"S\n\x16DdlStatementActionInfo\x12\x0e\n\x06action\x18\x01 \x01(\t\x12\x13\n\x0bentity_type\x18\x02 \x01(\t\x12\x14\n\x0centity_names\x18\x03 \x03(\t"\xc8\x02\n\x19UpdateDatabaseDdlMetadata\x126\n\x08database\x18\x01 \x01(\tB$\xfaA!\n\x1fspanner.googleapis.com/Database\x12\x12\n\nstatements\x18\x02 \x03(\t\x125\n\x11commit_timestamps\x18\x03 \x03(\x0b2\x1a.google.protobuf.Timestamp\x12\x16\n\tthrottled\x18\x04 \x01(\x08B\x03\xe0A\x03\x12E\n\x08progress\x18\x05 \x03(\x0b23.google.spanner.admin.database.v1.OperationProgress\x12I\n\x07actions\x18\x06 \x03(\x0b28.google.spanner.admin.database.v1.DdlStatementActionInfo"P\n\x13DropDatabaseRequest\x129\n\x08database\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database"R\n\x15GetDatabaseDdlRequest\x129\n\x08database\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database"G\n\x16GetDatabaseDdlResponse\x12\x12\n\nstatements\x18\x01 \x03(\t\x12\x19\n\x11proto_descriptors\x18\x02 \x01(\x0c"\x8f\x01\n\x1dListDatabaseOperationsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"l\n\x1eListDatabaseOperationsResponse\x121\n\noperations\x18\x01 \x03(\x0b2\x1d.google.longrunning.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8e\x02\n\x16RestoreDatabaseRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance\x12\x18\n\x0bdatabase_id\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x06backup\x18\x03 \x01(\tB"\xfaA\x1f\n\x1dspanner.googleapis.com/BackupH\x00\x12a\n\x11encryption_config\x18\x04 \x01(\x0b2A.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfigB\x03\xe0A\x01B\x08\n\x06source"\xb5\x03\n\x1fRestoreDatabaseEncryptionConfig\x12n\n\x0fencryption_type\x18\x01 \x01(\x0e2P.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.EncryptionTypeB\x03\xe0A\x02\x12?\n\x0ckms_key_name\x18\x02 \x01(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12@\n\rkms_key_names\x18\x03 \x03(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey"\x9e\x01\n\x0eEncryptionType\x12\x1f\n\x1bENCRYPTION_TYPE_UNSPECIFIED\x10\x00\x12+\n\'USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION\x10\x01\x12\x1d\n\x19GOOGLE_DEFAULT_ENCRYPTION\x10\x02\x12\x1f\n\x1bCUSTOMER_MANAGED_ENCRYPTION\x10\x03"\x8d\x03\n\x17RestoreDatabaseMetadata\x122\n\x04name\x18\x01 \x01(\tB$\xfaA!\n\x1fspanner.googleapis.com/Database\x12H\n\x0bsource_type\x18\x02 \x01(\x0e23.google.spanner.admin.database.v1.RestoreSourceType\x12C\n\x0bbackup_info\x18\x03 \x01(\x0b2,.google.spanner.admin.database.v1.BackupInfoH\x00\x12E\n\x08progress\x18\x04 \x01(\x0b23.google.spanner.admin.database.v1.OperationProgress\x12/\n\x0bcancel_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12(\n optimize_database_operation_name\x18\x06 \x01(\tB\r\n\x0bsource_info"\x9d\x01\n OptimizeRestoredDatabaseMetadata\x122\n\x04name\x18\x01 \x01(\tB$\xfaA!\n\x1fspanner.googleapis.com/Database\x12E\n\x08progress\x18\x02 \x01(\x0b23.google.spanner.admin.database.v1.OperationProgress"\x9e\x01\n\x0cDatabaseRole\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02:{\xeaAx\n#spanner.googleapis.com/DatabaseRole\x12Qprojects/{project}/instances/{instance}/databases/{database}/databaseRoles/{role}"z\n\x18ListDatabaseRolesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"|\n\x19ListDatabaseRolesResponse\x12F\n\x0edatabase_roles\x18\x01 \x03(\x0b2..google.spanner.admin.database.v1.DatabaseRole\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*5\n\x11RestoreSourceType\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06BACKUP\x10\x012\x981\n\rDatabaseAdmin\x12\xc0\x01\n\rListDatabases\x126.google.spanner.admin.database.v1.ListDatabasesRequest\x1a7.google.spanner.admin.database.v1.ListDatabasesResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/instances/*}/databases\x12\xa4\x02\n\x0eCreateDatabase\x127.google.spanner.admin.database.v1.CreateDatabaseRequest\x1a\x1d.google.longrunning.Operation"\xb9\x01\xcaAd\n)google.spanner.admin.database.v1.Database\x127google.spanner.admin.database.v1.CreateDatabaseMetadata\xdaA\x17parent,create_statement\x82\xd3\xe4\x93\x022"-/v1/{parent=projects/*/instances/*}/databases:\x01*\x12\xad\x01\n\x0bGetDatabase\x124.google.spanner.admin.database.v1.GetDatabaseRequest\x1a*.google.spanner.admin.database.v1.Database"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/instances/*/databases/*}\x12\xef\x01\n\x0eUpdateDatabase\x127.google.spanner.admin.database.v1.UpdateDatabaseRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA"\n\x08Database\x12\x16UpdateDatabaseMetadata\xdaA\x14database,update_mask\x82\xd3\xe4\x93\x02B26/v1/{database.name=projects/*/instances/*/databases/*}:\x08database\x12\x9d\x02\n\x11UpdateDatabaseDdl\x12:.google.spanner.admin.database.v1.UpdateDatabaseDdlRequest\x1a\x1d.google.longrunning.Operation"\xac\x01\xcaAS\n\x15google.protobuf.Empty\x12:google.spanner.admin.database.v1.UpdateDatabaseDdlMetadata\xdaA\x13database,statements\x82\xd3\xe4\x93\x02:25/v1/{database=projects/*/instances/*/databases/*}/ddl:\x01*\x12\xa3\x01\n\x0cDropDatabase\x125.google.spanner.admin.database.v1.DropDatabaseRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x08database\x82\xd3\xe4\x93\x023*1/v1/{database=projects/*/instances/*/databases/*}\x12\xcd\x01\n\x0eGetDatabaseDdl\x127.google.spanner.admin.database.v1.GetDatabaseDdlRequest\x1a8.google.spanner.admin.database.v1.GetDatabaseDdlResponse"H\xdaA\x08database\x82\xd3\xe4\x93\x027\x125/v1/{database=projects/*/instances/*/databases/*}/ddl\x12\xc2\x02\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xf6\x01\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02\xdd\x01">/v1/{resource=projects/*/instances/*/databases/*}:setIamPolicy:\x01*ZA"</v1/{resource=projects/*/instances/*/backups/*}:setIamPolicy:\x01*ZU"P/v1/{resource=projects/*/instances/*/databases/*/backupSchedules/*}:setIamPolicy:\x01*\x12\xbb\x02\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xef\x01\xdaA\x08resource\x82\xd3\xe4\x93\x02\xdd\x01">/v1/{resource=projects/*/instances/*/databases/*}:getIamPolicy:\x01*ZA"</v1/{resource=projects/*/instances/*/backups/*}:getIamPolicy:\x01*ZU"P/v1/{resource=projects/*/instances/*/databases/*/backupSchedules/*}:getIamPolicy:\x01*\x12\xd4\x03\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\xe8\x02\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02\xca\x02"D/v1/{resource=projects/*/instances/*/databases/*}:testIamPermissions:\x01*ZG"B/v1/{resource=projects/*/instances/*/backups/*}:testIamPermissions:\x01*Z["V/v1/{resource=projects/*/instances/*/databases/*/backupSchedules/*}:testIamPermissions:\x01*ZY"T/v1/{resource=projects/*/instances/*/databases/*/databaseRoles/*}:testIamPermissions:\x01*\x12\x9f\x02\n\x0cCreateBackup\x125.google.spanner.admin.database.v1.CreateBackupRequest\x1a\x1d.google.longrunning.Operation"\xb8\x01\xcaA`\n\'google.spanner.admin.database.v1.Backup\x125google.spanner.admin.database.v1.CreateBackupMetadata\xdaA\x17parent,backup,backup_id\x82\xd3\xe4\x93\x025"+/v1/{parent=projects/*/instances/*}/backups:\x06backup\x12\xac\x02\n\nCopyBackup\x123.google.spanner.admin.database.v1.CopyBackupRequest\x1a\x1d.google.longrunning.Operation"\xc9\x01\xcaA^\n\'google.spanner.admin.database.v1.Backup\x123google.spanner.admin.database.v1.CopyBackupMetadata\xdaA*parent,backup_id,source_backup,expire_time\x82\xd3\xe4\x93\x025"0/v1/{parent=projects/*/instances/*}/backups:copy:\x01*\x12\xa5\x01\n\tGetBackup\x122.google.spanner.admin.database.v1.GetBackupRequest\x1a(.google.spanner.admin.database.v1.Backup":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/instances/*/backups/*}\x12\xc8\x01\n\x0cUpdateBackup\x125.google.spanner.admin.database.v1.UpdateBackupRequest\x1a(.google.spanner.admin.database.v1.Backup"W\xdaA\x12backup,update_mask\x82\xd3\xe4\x93\x02<22/v1/{backup.name=projects/*/instances/*/backups/*}:\x06backup\x12\x99\x01\n\x0cDeleteBackup\x125.google.spanner.admin.database.v1.DeleteBackupRequest\x1a\x16.google.protobuf.Empty":\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1/{name=projects/*/instances/*/backups/*}\x12\xb8\x01\n\x0bListBackups\x124.google.spanner.admin.database.v1.ListBackupsRequest\x1a5.google.spanner.admin.database.v1.ListBackupsResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/instances/*}/backups\x12\xb1\x02\n\x0fRestoreDatabase\x128.google.spanner.admin.database.v1.RestoreDatabaseRequest\x1a\x1d.google.longrunning.Operation"\xc4\x01\xcaAe\n)google.spanner.admin.database.v1.Database\x128google.spanner.admin.database.v1.RestoreDatabaseMetadata\xdaA\x19parent,database_id,backup\x82\xd3\xe4\x93\x02:"5/v1/{parent=projects/*/instances/*}/databases:restore:\x01*\x12\xe4\x01\n\x16ListDatabaseOperations\x12?.google.spanner.admin.database.v1.ListDatabaseOperationsRequest\x1a@.google.spanner.admin.database.v1.ListDatabaseOperationsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/instances/*}/databaseOperations\x12\xdc\x01\n\x14ListBackupOperations\x12=.google.spanner.admin.database.v1.ListBackupOperationsRequest\x1a>.google.spanner.admin.database.v1.ListBackupOperationsResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/instances/*}/backupOperations\x12\xdc\x01\n\x11ListDatabaseRoles\x12:.google.spanner.admin.database.v1.ListDatabaseRolesRequest\x1a;.google.spanner.admin.database.v1.ListDatabaseRolesResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/instances/*/databases/*}/databaseRoles\x12\x8e\x02\n\x14CreateBackupSchedule\x12=.google.spanner.admin.database.v1.CreateBackupScheduleRequest\x1a0.google.spanner.admin.database.v1.BackupSchedule"\x84\x01\xdaA)parent,backup_schedule,backup_schedule_id\x82\xd3\xe4\x93\x02R"?/v1/{parent=projects/*/instances/*/databases/*}/backupSchedules:\x0fbackup_schedule\x12\xd1\x01\n\x11GetBackupSchedule\x12:.google.spanner.admin.database.v1.GetBackupScheduleRequest\x1a0.google.spanner.admin.database.v1.BackupSchedule"N\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1/{name=projects/*/instances/*/databases/*/backupSchedules/*}\x12\x90\x02\n\x14UpdateBackupSchedule\x12=.google.spanner.admin.database.v1.UpdateBackupScheduleRequest\x1a0.google.spanner.admin.database.v1.BackupSchedule"\x86\x01\xdaA\x1bbackup_schedule,update_mask\x82\xd3\xe4\x93\x02b2O/v1/{backup_schedule.name=projects/*/instances/*/databases/*/backupSchedules/*}:\x0fbackup_schedule\x12\xbd\x01\n\x14DeleteBackupSchedule\x12=.google.spanner.admin.database.v1.DeleteBackupScheduleRequest\x1a\x16.google.protobuf.Empty"N\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/v1/{name=projects/*/instances/*/databases/*/backupSchedules/*}\x12\xe4\x01\n\x13ListBackupSchedules\x12<.google.spanner.admin.database.v1.ListBackupSchedulesRequest\x1a=.google.spanner.admin.database.v1.ListBackupSchedulesResponse"P\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/v1/{parent=projects/*/instances/*/databases/*}/backupSchedules\x1ax\xcaA\x16spanner.googleapis.com\xd2A\\https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/spanner.adminB\xd8\x02\n$com.google.spanner.admin.database.v1B\x19SpannerDatabaseAdminProtoP\x01ZFcloud.google.com/go/spanner/admin/database/apiv1/databasepb;databasepb\xaa\x02&Google.Cloud.Spanner.Admin.Database.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Database\\V1\xea\x02+Google::Cloud::Spanner::Admin::Database::V1\xeaAJ\n\x1fspanner.googleapis.com/Instance\x12\'projects/{project}/instances/{instance}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.admin.database.v1.spanner_database_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n$com.google.spanner.admin.database.v1B\x19SpannerDatabaseAdminProtoP\x01ZFcloud.google.com/go/spanner/admin/database/apiv1/databasepb;databasepb\xaa\x02&Google.Cloud.Spanner.Admin.Database.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Database\\V1\xea\x02+Google::Cloud::Spanner::Admin::Database::V1\xeaAJ\n\x1fspanner.googleapis.com/Instance\x12'projects/{project}/instances/{instance}"
    _globals['_DATABASE'].fields_by_name['name']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_DATABASE'].fields_by_name['state']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['restore_info']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['restore_info']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['encryption_config']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['encryption_config']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['encryption_info']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['encryption_info']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['version_retention_period']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['version_retention_period']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['earliest_version_time']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['earliest_version_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['default_leader']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['default_leader']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['database_dialect']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['database_dialect']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE'].fields_by_name['reconciling']._loaded_options = None
    _globals['_DATABASE'].fields_by_name['reconciling']._serialized_options = b'\xe0A\x03'
    _globals['_DATABASE']._loaded_options = None
    _globals['_DATABASE']._serialized_options = b'\xeaA_\n\x1fspanner.googleapis.com/Database\x12<projects/{project}/instances/{instance}/databases/{database}'
    _globals['_LISTDATABASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATABASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['create_statement']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['create_statement']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['extra_statements']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['extra_statements']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['encryption_config']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['encryption_config']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database_dialect']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database_dialect']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['proto_descriptors']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['proto_descriptors']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEDATABASEMETADATA'].fields_by_name['database']._loaded_options = None
    _globals['_CREATEDATABASEMETADATA'].fields_by_name['database']._serialized_options = b'\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_GETDATABASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATABASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_UPDATEDATABASEREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_UPDATEDATABASEREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATABASEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATABASEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATABASEDDLREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_UPDATEDATABASEDDLREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_UPDATEDATABASEDDLREQUEST'].fields_by_name['statements']._loaded_options = None
    _globals['_UPDATEDATABASEDDLREQUEST'].fields_by_name['statements']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATABASEDDLREQUEST'].fields_by_name['proto_descriptors']._loaded_options = None
    _globals['_UPDATEDATABASEDDLREQUEST'].fields_by_name['proto_descriptors']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDATABASEDDLMETADATA'].fields_by_name['database']._loaded_options = None
    _globals['_UPDATEDATABASEDDLMETADATA'].fields_by_name['database']._serialized_options = b'\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_UPDATEDATABASEDDLMETADATA'].fields_by_name['throttled']._loaded_options = None
    _globals['_UPDATEDATABASEDDLMETADATA'].fields_by_name['throttled']._serialized_options = b'\xe0A\x03'
    _globals['_DROPDATABASEREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_DROPDATABASEREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_GETDATABASEDDLREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_GETDATABASEDDLREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_LISTDATABASEOPERATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATABASEOPERATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance'
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Instance'
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['database_id']._loaded_options = None
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['database_id']._serialized_options = b'\xe0A\x02'
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['backup']._loaded_options = None
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['backup']._serialized_options = b'\xfaA\x1f\n\x1dspanner.googleapis.com/Backup'
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['encryption_config']._loaded_options = None
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['encryption_config']._serialized_options = b'\xe0A\x01'
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG'].fields_by_name['encryption_type']._loaded_options = None
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG'].fields_by_name['encryption_type']._serialized_options = b'\xe0A\x02'
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG'].fields_by_name['kms_key_names']._loaded_options = None
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG'].fields_by_name['kms_key_names']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_RESTOREDATABASEMETADATA'].fields_by_name['name']._loaded_options = None
    _globals['_RESTOREDATABASEMETADATA'].fields_by_name['name']._serialized_options = b'\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_OPTIMIZERESTOREDDATABASEMETADATA'].fields_by_name['name']._loaded_options = None
    _globals['_OPTIMIZERESTOREDDATABASEMETADATA'].fields_by_name['name']._serialized_options = b'\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_DATABASEROLE'].fields_by_name['name']._loaded_options = None
    _globals['_DATABASEROLE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_DATABASEROLE']._loaded_options = None
    _globals['_DATABASEROLE']._serialized_options = b'\xeaAx\n#spanner.googleapis.com/DatabaseRole\x12Qprojects/{project}/instances/{instance}/databases/{database}/databaseRoles/{role}'
    _globals['_LISTDATABASEROLESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATABASEROLESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_DATABASEADMIN']._loaded_options = None
    _globals['_DATABASEADMIN']._serialized_options = b'\xcaA\x16spanner.googleapis.com\xd2A\\https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/spanner.admin'
    _globals['_DATABASEADMIN'].methods_by_name['ListDatabases']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['ListDatabases']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/instances/*}/databases'
    _globals['_DATABASEADMIN'].methods_by_name['CreateDatabase']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['CreateDatabase']._serialized_options = b'\xcaAd\n)google.spanner.admin.database.v1.Database\x127google.spanner.admin.database.v1.CreateDatabaseMetadata\xdaA\x17parent,create_statement\x82\xd3\xe4\x93\x022"-/v1/{parent=projects/*/instances/*}/databases:\x01*'
    _globals['_DATABASEADMIN'].methods_by_name['GetDatabase']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['GetDatabase']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/instances/*/databases/*}'
    _globals['_DATABASEADMIN'].methods_by_name['UpdateDatabase']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['UpdateDatabase']._serialized_options = b'\xcaA"\n\x08Database\x12\x16UpdateDatabaseMetadata\xdaA\x14database,update_mask\x82\xd3\xe4\x93\x02B26/v1/{database.name=projects/*/instances/*/databases/*}:\x08database'
    _globals['_DATABASEADMIN'].methods_by_name['UpdateDatabaseDdl']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['UpdateDatabaseDdl']._serialized_options = b'\xcaAS\n\x15google.protobuf.Empty\x12:google.spanner.admin.database.v1.UpdateDatabaseDdlMetadata\xdaA\x13database,statements\x82\xd3\xe4\x93\x02:25/v1/{database=projects/*/instances/*/databases/*}/ddl:\x01*'
    _globals['_DATABASEADMIN'].methods_by_name['DropDatabase']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['DropDatabase']._serialized_options = b'\xdaA\x08database\x82\xd3\xe4\x93\x023*1/v1/{database=projects/*/instances/*/databases/*}'
    _globals['_DATABASEADMIN'].methods_by_name['GetDatabaseDdl']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['GetDatabaseDdl']._serialized_options = b'\xdaA\x08database\x82\xd3\xe4\x93\x027\x125/v1/{database=projects/*/instances/*/databases/*}/ddl'
    _globals['_DATABASEADMIN'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02\xdd\x01">/v1/{resource=projects/*/instances/*/databases/*}:setIamPolicy:\x01*ZA"</v1/{resource=projects/*/instances/*/backups/*}:setIamPolicy:\x01*ZU"P/v1/{resource=projects/*/instances/*/databases/*/backupSchedules/*}:setIamPolicy:\x01*'
    _globals['_DATABASEADMIN'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02\xdd\x01">/v1/{resource=projects/*/instances/*/databases/*}:getIamPolicy:\x01*ZA"</v1/{resource=projects/*/instances/*/backups/*}:getIamPolicy:\x01*ZU"P/v1/{resource=projects/*/instances/*/databases/*/backupSchedules/*}:getIamPolicy:\x01*'
    _globals['_DATABASEADMIN'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02\xca\x02"D/v1/{resource=projects/*/instances/*/databases/*}:testIamPermissions:\x01*ZG"B/v1/{resource=projects/*/instances/*/backups/*}:testIamPermissions:\x01*Z["V/v1/{resource=projects/*/instances/*/databases/*/backupSchedules/*}:testIamPermissions:\x01*ZY"T/v1/{resource=projects/*/instances/*/databases/*/databaseRoles/*}:testIamPermissions:\x01*'
    _globals['_DATABASEADMIN'].methods_by_name['CreateBackup']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['CreateBackup']._serialized_options = b'\xcaA`\n\'google.spanner.admin.database.v1.Backup\x125google.spanner.admin.database.v1.CreateBackupMetadata\xdaA\x17parent,backup,backup_id\x82\xd3\xe4\x93\x025"+/v1/{parent=projects/*/instances/*}/backups:\x06backup'
    _globals['_DATABASEADMIN'].methods_by_name['CopyBackup']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['CopyBackup']._serialized_options = b'\xcaA^\n\'google.spanner.admin.database.v1.Backup\x123google.spanner.admin.database.v1.CopyBackupMetadata\xdaA*parent,backup_id,source_backup,expire_time\x82\xd3\xe4\x93\x025"0/v1/{parent=projects/*/instances/*}/backups:copy:\x01*'
    _globals['_DATABASEADMIN'].methods_by_name['GetBackup']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['GetBackup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/instances/*/backups/*}'
    _globals['_DATABASEADMIN'].methods_by_name['UpdateBackup']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['UpdateBackup']._serialized_options = b'\xdaA\x12backup,update_mask\x82\xd3\xe4\x93\x02<22/v1/{backup.name=projects/*/instances/*/backups/*}:\x06backup'
    _globals['_DATABASEADMIN'].methods_by_name['DeleteBackup']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['DeleteBackup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1/{name=projects/*/instances/*/backups/*}'
    _globals['_DATABASEADMIN'].methods_by_name['ListBackups']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['ListBackups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/instances/*}/backups'
    _globals['_DATABASEADMIN'].methods_by_name['RestoreDatabase']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['RestoreDatabase']._serialized_options = b'\xcaAe\n)google.spanner.admin.database.v1.Database\x128google.spanner.admin.database.v1.RestoreDatabaseMetadata\xdaA\x19parent,database_id,backup\x82\xd3\xe4\x93\x02:"5/v1/{parent=projects/*/instances/*}/databases:restore:\x01*'
    _globals['_DATABASEADMIN'].methods_by_name['ListDatabaseOperations']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['ListDatabaseOperations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/instances/*}/databaseOperations'
    _globals['_DATABASEADMIN'].methods_by_name['ListBackupOperations']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['ListBackupOperations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/instances/*}/backupOperations'
    _globals['_DATABASEADMIN'].methods_by_name['ListDatabaseRoles']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['ListDatabaseRoles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/instances/*/databases/*}/databaseRoles'
    _globals['_DATABASEADMIN'].methods_by_name['CreateBackupSchedule']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['CreateBackupSchedule']._serialized_options = b'\xdaA)parent,backup_schedule,backup_schedule_id\x82\xd3\xe4\x93\x02R"?/v1/{parent=projects/*/instances/*/databases/*}/backupSchedules:\x0fbackup_schedule'
    _globals['_DATABASEADMIN'].methods_by_name['GetBackupSchedule']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['GetBackupSchedule']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1/{name=projects/*/instances/*/databases/*/backupSchedules/*}'
    _globals['_DATABASEADMIN'].methods_by_name['UpdateBackupSchedule']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['UpdateBackupSchedule']._serialized_options = b'\xdaA\x1bbackup_schedule,update_mask\x82\xd3\xe4\x93\x02b2O/v1/{backup_schedule.name=projects/*/instances/*/databases/*/backupSchedules/*}:\x0fbackup_schedule'
    _globals['_DATABASEADMIN'].methods_by_name['DeleteBackupSchedule']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['DeleteBackupSchedule']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/v1/{name=projects/*/instances/*/databases/*/backupSchedules/*}'
    _globals['_DATABASEADMIN'].methods_by_name['ListBackupSchedules']._loaded_options = None
    _globals['_DATABASEADMIN'].methods_by_name['ListBackupSchedules']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/v1/{parent=projects/*/instances/*/databases/*}/backupSchedules'
    _globals['_RESTORESOURCETYPE']._serialized_start = 5441
    _globals['_RESTORESOURCETYPE']._serialized_end = 5494
    _globals['_RESTOREINFO']._serialized_start = 558
    _globals['_RESTOREINFO']._serialized_end = 729
    _globals['_DATABASE']._serialized_start = 732
    _globals['_DATABASE']._serialized_end = 1574
    _globals['_DATABASE_STATE']._serialized_start = 1397
    _globals['_DATABASE_STATE']._serialized_end = 1474
    _globals['_LISTDATABASESREQUEST']._serialized_start = 1576
    _globals['_LISTDATABASESREQUEST']._serialized_end = 1694
    _globals['_LISTDATABASESRESPONSE']._serialized_start = 1696
    _globals['_LISTDATABASESRESPONSE']._serialized_end = 1807
    _globals['_CREATEDATABASEREQUEST']._serialized_start = 1810
    _globals['_CREATEDATABASEREQUEST']._serialized_end = 2150
    _globals['_CREATEDATABASEMETADATA']._serialized_start = 2152
    _globals['_CREATEDATABASEMETADATA']._serialized_end = 2232
    _globals['_GETDATABASEREQUEST']._serialized_start = 2234
    _globals['_GETDATABASEREQUEST']._serialized_end = 2309
    _globals['_UPDATEDATABASEREQUEST']._serialized_start = 2312
    _globals['_UPDATEDATABASEREQUEST']._serialized_end = 2456
    _globals['_UPDATEDATABASEMETADATA']._serialized_start = 2459
    _globals['_UPDATEDATABASEMETADATA']._serialized_end = 2677
    _globals['_UPDATEDATABASEDDLREQUEST']._serialized_start = 2680
    _globals['_UPDATEDATABASEDDLREQUEST']._serialized_end = 2844
    _globals['_DDLSTATEMENTACTIONINFO']._serialized_start = 2846
    _globals['_DDLSTATEMENTACTIONINFO']._serialized_end = 2929
    _globals['_UPDATEDATABASEDDLMETADATA']._serialized_start = 2932
    _globals['_UPDATEDATABASEDDLMETADATA']._serialized_end = 3260
    _globals['_DROPDATABASEREQUEST']._serialized_start = 3262
    _globals['_DROPDATABASEREQUEST']._serialized_end = 3342
    _globals['_GETDATABASEDDLREQUEST']._serialized_start = 3344
    _globals['_GETDATABASEDDLREQUEST']._serialized_end = 3426
    _globals['_GETDATABASEDDLRESPONSE']._serialized_start = 3428
    _globals['_GETDATABASEDDLRESPONSE']._serialized_end = 3499
    _globals['_LISTDATABASEOPERATIONSREQUEST']._serialized_start = 3502
    _globals['_LISTDATABASEOPERATIONSREQUEST']._serialized_end = 3645
    _globals['_LISTDATABASEOPERATIONSRESPONSE']._serialized_start = 3647
    _globals['_LISTDATABASEOPERATIONSRESPONSE']._serialized_end = 3755
    _globals['_RESTOREDATABASEREQUEST']._serialized_start = 3758
    _globals['_RESTOREDATABASEREQUEST']._serialized_end = 4028
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG']._serialized_start = 4031
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG']._serialized_end = 4468
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG_ENCRYPTIONTYPE']._serialized_start = 4310
    _globals['_RESTOREDATABASEENCRYPTIONCONFIG_ENCRYPTIONTYPE']._serialized_end = 4468
    _globals['_RESTOREDATABASEMETADATA']._serialized_start = 4471
    _globals['_RESTOREDATABASEMETADATA']._serialized_end = 4868
    _globals['_OPTIMIZERESTOREDDATABASEMETADATA']._serialized_start = 4871
    _globals['_OPTIMIZERESTOREDDATABASEMETADATA']._serialized_end = 5028
    _globals['_DATABASEROLE']._serialized_start = 5031
    _globals['_DATABASEROLE']._serialized_end = 5189
    _globals['_LISTDATABASEROLESREQUEST']._serialized_start = 5191
    _globals['_LISTDATABASEROLESREQUEST']._serialized_end = 5313
    _globals['_LISTDATABASEROLESRESPONSE']._serialized_start = 5315
    _globals['_LISTDATABASEROLESRESPONSE']._serialized_end = 5439
    _globals['_DATABASEADMIN']._serialized_start = 5497
    _globals['_DATABASEADMIN']._serialized_end = 11793