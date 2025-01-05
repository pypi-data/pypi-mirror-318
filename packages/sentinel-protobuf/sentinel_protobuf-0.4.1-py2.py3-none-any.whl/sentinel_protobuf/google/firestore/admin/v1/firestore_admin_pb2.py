"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1/firestore_admin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.firestore.admin.v1 import backup_pb2 as google_dot_firestore_dot_admin_dot_v1_dot_backup__pb2
from .....google.firestore.admin.v1 import database_pb2 as google_dot_firestore_dot_admin_dot_v1_dot_database__pb2
from .....google.firestore.admin.v1 import field_pb2 as google_dot_firestore_dot_admin_dot_v1_dot_field__pb2
from .....google.firestore.admin.v1 import index_pb2 as google_dot_firestore_dot_admin_dot_v1_dot_index__pb2
from .....google.firestore.admin.v1 import operation_pb2 as google_dot_firestore_dot_admin_dot_v1_dot_operation__pb2
from .....google.firestore.admin.v1 import schedule_pb2 as google_dot_firestore_dot_admin_dot_v1_dot_schedule__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/firestore/admin/v1/firestore_admin.proto\x12\x19google.firestore.admin.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/firestore/admin/v1/backup.proto\x1a(google/firestore/admin/v1/database.proto\x1a%google/firestore/admin/v1/field.proto\x1a%google/firestore/admin/v1/index.proto\x1a)google/firestore/admin/v1/operation.proto\x1a(google/firestore/admin/v1/schedule.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"g\n\x14ListDatabasesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!firestore.googleapis.com/Database\x12\x14\n\x0cshow_deleted\x18\x04 \x01(\x08"\xa8\x01\n\x15CreateDatabaseRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!firestore.googleapis.com/Database\x12:\n\x08database\x18\x02 \x01(\x0b2#.google.firestore.admin.v1.DatabaseB\x03\xe0A\x02\x12\x18\n\x0bdatabase_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x18\n\x16CreateDatabaseMetadata"d\n\x15ListDatabasesResponse\x126\n\tdatabases\x18\x01 \x03(\x0b2#.google.firestore.admin.v1.Database\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"M\n\x12GetDatabaseRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database"\x84\x01\n\x15UpdateDatabaseRequest\x12:\n\x08database\x18\x01 \x01(\x0b2#.google.firestore.admin.v1.DatabaseB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x18\n\x16UpdateDatabaseMetadata"^\n\x15DeleteDatabaseRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database\x12\x0c\n\x04etag\x18\x03 \x01(\t"\x18\n\x16DeleteDatabaseMetadata"\xa1\x01\n\x1bCreateBackupScheduleRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database\x12G\n\x0fbackup_schedule\x18\x02 \x01(\x0b2).google.firestore.admin.v1.BackupScheduleB\x03\xe0A\x02"Y\n\x18GetBackupScheduleRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'firestore.googleapis.com/BackupSchedule"\x97\x01\n\x1bUpdateBackupScheduleRequest\x12G\n\x0fbackup_schedule\x18\x01 \x01(\x0b2).google.firestore.admin.v1.BackupScheduleB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"W\n\x1aListBackupSchedulesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database"b\n\x1bListBackupSchedulesResponse\x12C\n\x10backup_schedules\x18\x01 \x03(\x0b2).google.firestore.admin.v1.BackupSchedule"\\\n\x1bDeleteBackupScheduleRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'firestore.googleapis.com/BackupSchedule"\x8c\x01\n\x12CreateIndexRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(firestore.googleapis.com/CollectionGroup\x124\n\x05index\x18\x02 \x01(\x0b2 .google.firestore.admin.v1.IndexB\x03\xe0A\x02"\x8d\x01\n\x12ListIndexesRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(firestore.googleapis.com/CollectionGroup\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"a\n\x13ListIndexesResponse\x121\n\x07indexes\x18\x01 \x03(\x0b2 .google.firestore.admin.v1.Index\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"G\n\x0fGetIndexRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1efirestore.googleapis.com/Index"J\n\x12DeleteIndexRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1efirestore.googleapis.com/Index"{\n\x12UpdateFieldRequest\x124\n\x05field\x18\x01 \x01(\x0b2 .google.firestore.admin.v1.FieldB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"G\n\x0fGetFieldRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1efirestore.googleapis.com/Field"\x8c\x01\n\x11ListFieldsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(firestore.googleapis.com/CollectionGroup\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"_\n\x12ListFieldsResponse\x120\n\x06fields\x18\x01 \x03(\x0b2 .google.firestore.admin.v1.Field\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xce\x01\n\x16ExportDocumentsRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database\x12\x16\n\x0ecollection_ids\x18\x02 \x03(\t\x12\x19\n\x11output_uri_prefix\x18\x03 \x01(\t\x12\x15\n\rnamespace_ids\x18\x04 \x03(\t\x121\n\rsnapshot_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x9a\x01\n\x16ImportDocumentsRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database\x12\x16\n\x0ecollection_ids\x18\x02 \x03(\t\x12\x18\n\x10input_uri_prefix\x18\x03 \x01(\t\x12\x15\n\rnamespace_ids\x18\x04 \x03(\t"\x8e\x01\n\x1aBulkDeleteDocumentsRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database\x12\x1b\n\x0ecollection_ids\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x1a\n\rnamespace_ids\x18\x03 \x03(\tB\x03\xe0A\x01"\x1d\n\x1bBulkDeleteDocumentsResponse"I\n\x10GetBackupRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1ffirestore.googleapis.com/Backup"O\n\x12ListBackupsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!firestore.googleapis.com/Location"^\n\x13ListBackupsResponse\x122\n\x07backups\x18\x01 \x03(\x0b2!.google.firestore.admin.v1.Backup\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"L\n\x13DeleteBackupRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1ffirestore.googleapis.com/Backup"\xfc\x01\n\x16RestoreDatabaseRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!firestore.googleapis.com/Database\x12\x18\n\x0bdatabase_id\x18\x02 \x01(\tB\x03\xe0A\x02\x127\n\x06backup\x18\x03 \x01(\tB\'\xe0A\x02\xfaA!\n\x1ffirestore.googleapis.com/Backup\x12T\n\x11encryption_config\x18\t \x01(\x0b24.google.firestore.admin.v1.Database.EncryptionConfigB\x03\xe0A\x012\xcb%\n\x0eFirestoreAdmin\x12\xdb\x01\n\x0bCreateIndex\x12-.google.firestore.admin.v1.CreateIndexRequest\x1a\x1d.google.longrunning.Operation"~\xcaA\x1f\n\x05Index\x12\x16IndexOperationMetadata\xdaA\x0cparent,index\x82\xd3\xe4\x93\x02G">/v1/{parent=projects/*/databases/*/collectionGroups/*}/indexes:\x05index\x12\xbd\x01\n\x0bListIndexes\x12-.google.firestore.admin.v1.ListIndexesRequest\x1a..google.firestore.admin.v1.ListIndexesResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1/{parent=projects/*/databases/*/collectionGroups/*}/indexes\x12\xa7\x01\n\x08GetIndex\x12*.google.firestore.admin.v1.GetIndexRequest\x1a .google.firestore.admin.v1.Index"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/databases/*/collectionGroups/*/indexes/*}\x12\xa3\x01\n\x0bDeleteIndex\x12-.google.firestore.admin.v1.DeleteIndexRequest\x1a\x16.google.protobuf.Empty"M\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1/{name=projects/*/databases/*/collectionGroups/*/indexes/*}\x12\xa6\x01\n\x08GetField\x12*.google.firestore.admin.v1.GetFieldRequest\x1a .google.firestore.admin.v1.Field"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/databases/*/collectionGroups/*/fields/*}\x12\xd9\x01\n\x0bUpdateField\x12-.google.firestore.admin.v1.UpdateFieldRequest\x1a\x1d.google.longrunning.Operation"|\xcaA\x1f\n\x05Field\x12\x16FieldOperationMetadata\xdaA\x05field\x82\xd3\xe4\x93\x02L2C/v1/{field.name=projects/*/databases/*/collectionGroups/*/fields/*}:\x05field\x12\xb9\x01\n\nListFields\x12,.google.firestore.admin.v1.ListFieldsRequest\x1a-.google.firestore.admin.v1.ListFieldsResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/databases/*/collectionGroups/*}/fields\x12\xdd\x01\n\x0fExportDocuments\x121.google.firestore.admin.v1.ExportDocumentsRequest\x1a\x1d.google.longrunning.Operation"x\xcaA2\n\x17ExportDocumentsResponse\x12\x17ExportDocumentsMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/databases/*}:exportDocuments:\x01*\x12\xdb\x01\n\x0fImportDocuments\x121.google.firestore.admin.v1.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation"v\xcaA0\n\x15google.protobuf.Empty\x12\x17ImportDocumentsMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/databases/*}:importDocuments:\x01*\x12\xf2\x01\n\x13BulkDeleteDocuments\x125.google.firestore.admin.v1.BulkDeleteDocumentsRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA:\n\x1bBulkDeleteDocumentsResponse\x12\x1bBulkDeleteDocumentsMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/databases/*}:bulkDeleteDocuments:\x01*\x12\xd9\x01\n\x0eCreateDatabase\x120.google.firestore.admin.v1.CreateDatabaseRequest\x1a\x1d.google.longrunning.Operation"v\xcaA"\n\x08Database\x12\x16CreateDatabaseMetadata\xdaA\x1bparent,database,database_id\x82\xd3\xe4\x93\x02-"!/v1/{parent=projects/*}/databases:\x08database\x12\x93\x01\n\x0bGetDatabase\x12-.google.firestore.admin.v1.GetDatabaseRequest\x1a#.google.firestore.admin.v1.Database"0\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1/{name=projects/*/databases/*}\x12\xa6\x01\n\rListDatabases\x12/.google.firestore.admin.v1.ListDatabasesRequest\x1a0.google.firestore.admin.v1.ListDatabasesResponse"2\xdaA\x06parent\x82\xd3\xe4\x93\x02#\x12!/v1/{parent=projects/*}/databases\x12\xdb\x01\n\x0eUpdateDatabase\x120.google.firestore.admin.v1.UpdateDatabaseRequest\x1a\x1d.google.longrunning.Operation"x\xcaA"\n\x08Database\x12\x16UpdateDatabaseMetadata\xdaA\x14database,update_mask\x82\xd3\xe4\x93\x0262*/v1/{database.name=projects/*/databases/*}:\x08database\x12\xb8\x01\n\x0eDeleteDatabase\x120.google.firestore.admin.v1.DeleteDatabaseRequest\x1a\x1d.google.longrunning.Operation"U\xcaA"\n\x08Database\x12\x16DeleteDatabaseMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02#*!/v1/{name=projects/*/databases/*}\x12\x97\x01\n\tGetBackup\x12+.google.firestore.admin.v1.GetBackupRequest\x1a!.google.firestore.admin.v1.Backup":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/backups/*}\x12\xaa\x01\n\x0bListBackups\x12-.google.firestore.admin.v1.ListBackupsRequest\x1a..google.firestore.admin.v1.ListBackupsResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/locations/*}/backups\x12\x92\x01\n\x0cDeleteBackup\x12..google.firestore.admin.v1.DeleteBackupRequest\x1a\x16.google.protobuf.Empty":\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1/{name=projects/*/locations/*/backups/*}\x12\xbf\x01\n\x0fRestoreDatabase\x121.google.firestore.admin.v1.RestoreDatabaseRequest\x1a\x1d.google.longrunning.Operation"Z\xcaA#\n\x08Database\x12\x17RestoreDatabaseMetadata\x82\xd3\xe4\x93\x02.")/v1/{parent=projects/*}/databases:restore:\x01*\x12\xe0\x01\n\x14CreateBackupSchedule\x126.google.firestore.admin.v1.CreateBackupScheduleRequest\x1a).google.firestore.admin.v1.BackupSchedule"e\xdaA\x16parent,backup_schedule\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/databases/*}/backupSchedules:\x0fbackup_schedule\x12\xb7\x01\n\x11GetBackupSchedule\x123.google.firestore.admin.v1.GetBackupScheduleRequest\x1a).google.firestore.admin.v1.BackupSchedule"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/databases/*/backupSchedules/*}\x12\xca\x01\n\x13ListBackupSchedules\x125.google.firestore.admin.v1.ListBackupSchedulesRequest\x1a6.google.firestore.admin.v1.ListBackupSchedulesResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/databases/*}/backupSchedules\x12\xf5\x01\n\x14UpdateBackupSchedule\x126.google.firestore.admin.v1.UpdateBackupScheduleRequest\x1a).google.firestore.admin.v1.BackupSchedule"z\xdaA\x1bbackup_schedule,update_mask\x82\xd3\xe4\x93\x02V2C/v1/{backup_schedule.name=projects/*/databases/*/backupSchedules/*}:\x0fbackup_schedule\x12\xaa\x01\n\x14DeleteBackupSchedule\x126.google.firestore.admin.v1.DeleteBackupScheduleRequest\x1a\x16.google.protobuf.Empty"B\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/databases/*/backupSchedules/*}\x1av\xcaA\x18firestore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastoreB\xa5\x03\n\x1dcom.google.firestore.admin.v1B\x13FirestoreAdminProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1\xeaAL\n!firestore.googleapis.com/Location\x12\'projects/{project}/locations/{location}\xeaAq\n(firestore.googleapis.com/CollectionGroup\x12Eprojects/{project}/databases/{database}/collectionGroups/{collection}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1.firestore_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n\x1dcom.google.firestore.admin.v1B\x13FirestoreAdminProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1\xeaAL\n!firestore.googleapis.com/Location\x12'projects/{project}/locations/{location}\xeaAq\n(firestore.googleapis.com/CollectionGroup\x12Eprojects/{project}/databases/{database}/collectionGroups/{collection}"
    _globals['_LISTDATABASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATABASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!firestore.googleapis.com/Database'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!firestore.googleapis.com/Database'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database_id']._loaded_options = None
    _globals['_CREATEDATABASEREQUEST'].fields_by_name['database_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATABASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATABASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_UPDATEDATABASEREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_UPDATEDATABASEREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATABASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATABASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule']._loaded_options = None
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule']._serialized_options = b'\xe0A\x02'
    _globals['_GETBACKUPSCHEDULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPSCHEDULEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'firestore.googleapis.com/BackupSchedule"
    _globals['_UPDATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule']._loaded_options = None
    _globals['_UPDATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule']._serialized_options = b'\xe0A\x02'
    _globals['_LISTBACKUPSCHEDULESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPSCHEDULESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_DELETEBACKUPSCHEDULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPSCHEDULEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'firestore.googleapis.com/BackupSchedule"
    _globals['_CREATEINDEXREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINDEXREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(firestore.googleapis.com/CollectionGroup'
    _globals['_CREATEINDEXREQUEST'].fields_by_name['index']._loaded_options = None
    _globals['_CREATEINDEXREQUEST'].fields_by_name['index']._serialized_options = b'\xe0A\x02'
    _globals['_LISTINDEXESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINDEXESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(firestore.googleapis.com/CollectionGroup'
    _globals['_GETINDEXREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINDEXREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1efirestore.googleapis.com/Index'
    _globals['_DELETEINDEXREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINDEXREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1efirestore.googleapis.com/Index'
    _globals['_UPDATEFIELDREQUEST'].fields_by_name['field']._loaded_options = None
    _globals['_UPDATEFIELDREQUEST'].fields_by_name['field']._serialized_options = b'\xe0A\x02'
    _globals['_GETFIELDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFIELDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1efirestore.googleapis.com/Field'
    _globals['_LISTFIELDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFIELDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(firestore.googleapis.com/CollectionGroup'
    _globals['_EXPORTDOCUMENTSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTDOCUMENTSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_BULKDELETEDOCUMENTSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_BULKDELETEDOCUMENTSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_BULKDELETEDOCUMENTSREQUEST'].fields_by_name['collection_ids']._loaded_options = None
    _globals['_BULKDELETEDOCUMENTSREQUEST'].fields_by_name['collection_ids']._serialized_options = b'\xe0A\x01'
    _globals['_BULKDELETEDOCUMENTSREQUEST'].fields_by_name['namespace_ids']._loaded_options = None
    _globals['_BULKDELETEDOCUMENTSREQUEST'].fields_by_name['namespace_ids']._serialized_options = b'\xe0A\x01'
    _globals['_GETBACKUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1ffirestore.googleapis.com/Backup'
    _globals['_LISTBACKUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!firestore.googleapis.com/Location'
    _globals['_DELETEBACKUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1ffirestore.googleapis.com/Backup'
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!firestore.googleapis.com/Database'
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['database_id']._loaded_options = None
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['database_id']._serialized_options = b'\xe0A\x02'
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['backup']._loaded_options = None
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['backup']._serialized_options = b'\xe0A\x02\xfaA!\n\x1ffirestore.googleapis.com/Backup'
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['encryption_config']._loaded_options = None
    _globals['_RESTOREDATABASEREQUEST'].fields_by_name['encryption_config']._serialized_options = b'\xe0A\x01'
    _globals['_FIRESTOREADMIN']._loaded_options = None
    _globals['_FIRESTOREADMIN']._serialized_options = b'\xcaA\x18firestore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastore'
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateIndex']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateIndex']._serialized_options = b'\xcaA\x1f\n\x05Index\x12\x16IndexOperationMetadata\xdaA\x0cparent,index\x82\xd3\xe4\x93\x02G">/v1/{parent=projects/*/databases/*/collectionGroups/*}/indexes:\x05index'
    _globals['_FIRESTOREADMIN'].methods_by_name['ListIndexes']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ListIndexes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1/{parent=projects/*/databases/*/collectionGroups/*}/indexes'
    _globals['_FIRESTOREADMIN'].methods_by_name['GetIndex']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['GetIndex']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/databases/*/collectionGroups/*/indexes/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteIndex']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteIndex']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1/{name=projects/*/databases/*/collectionGroups/*/indexes/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['GetField']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['GetField']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/databases/*/collectionGroups/*/fields/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['UpdateField']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['UpdateField']._serialized_options = b'\xcaA\x1f\n\x05Field\x12\x16FieldOperationMetadata\xdaA\x05field\x82\xd3\xe4\x93\x02L2C/v1/{field.name=projects/*/databases/*/collectionGroups/*/fields/*}:\x05field'
    _globals['_FIRESTOREADMIN'].methods_by_name['ListFields']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ListFields']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/databases/*/collectionGroups/*}/fields'
    _globals['_FIRESTOREADMIN'].methods_by_name['ExportDocuments']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ExportDocuments']._serialized_options = b'\xcaA2\n\x17ExportDocumentsResponse\x12\x17ExportDocumentsMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/databases/*}:exportDocuments:\x01*'
    _globals['_FIRESTOREADMIN'].methods_by_name['ImportDocuments']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ImportDocuments']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17ImportDocumentsMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/databases/*}:importDocuments:\x01*'
    _globals['_FIRESTOREADMIN'].methods_by_name['BulkDeleteDocuments']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['BulkDeleteDocuments']._serialized_options = b'\xcaA:\n\x1bBulkDeleteDocumentsResponse\x12\x1bBulkDeleteDocumentsMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/databases/*}:bulkDeleteDocuments:\x01*'
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateDatabase']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateDatabase']._serialized_options = b'\xcaA"\n\x08Database\x12\x16CreateDatabaseMetadata\xdaA\x1bparent,database,database_id\x82\xd3\xe4\x93\x02-"!/v1/{parent=projects/*}/databases:\x08database'
    _globals['_FIRESTOREADMIN'].methods_by_name['GetDatabase']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['GetDatabase']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1/{name=projects/*/databases/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['ListDatabases']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ListDatabases']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02#\x12!/v1/{parent=projects/*}/databases'
    _globals['_FIRESTOREADMIN'].methods_by_name['UpdateDatabase']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['UpdateDatabase']._serialized_options = b'\xcaA"\n\x08Database\x12\x16UpdateDatabaseMetadata\xdaA\x14database,update_mask\x82\xd3\xe4\x93\x0262*/v1/{database.name=projects/*/databases/*}:\x08database'
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteDatabase']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteDatabase']._serialized_options = b'\xcaA"\n\x08Database\x12\x16DeleteDatabaseMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02#*!/v1/{name=projects/*/databases/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['GetBackup']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['GetBackup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/backups/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['ListBackups']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ListBackups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/locations/*}/backups'
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteBackup']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteBackup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1/{name=projects/*/locations/*/backups/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['RestoreDatabase']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['RestoreDatabase']._serialized_options = b'\xcaA#\n\x08Database\x12\x17RestoreDatabaseMetadata\x82\xd3\xe4\x93\x02.")/v1/{parent=projects/*}/databases:restore:\x01*'
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateBackupSchedule']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateBackupSchedule']._serialized_options = b'\xdaA\x16parent,backup_schedule\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/databases/*}/backupSchedules:\x0fbackup_schedule'
    _globals['_FIRESTOREADMIN'].methods_by_name['GetBackupSchedule']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['GetBackupSchedule']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/databases/*/backupSchedules/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['ListBackupSchedules']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ListBackupSchedules']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/databases/*}/backupSchedules'
    _globals['_FIRESTOREADMIN'].methods_by_name['UpdateBackupSchedule']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['UpdateBackupSchedule']._serialized_options = b'\xdaA\x1bbackup_schedule,update_mask\x82\xd3\xe4\x93\x02V2C/v1/{backup_schedule.name=projects/*/databases/*/backupSchedules/*}:\x0fbackup_schedule'
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteBackupSchedule']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteBackupSchedule']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/databases/*/backupSchedules/*}'
    _globals['_LISTDATABASESREQUEST']._serialized_start = 571
    _globals['_LISTDATABASESREQUEST']._serialized_end = 674
    _globals['_CREATEDATABASEREQUEST']._serialized_start = 677
    _globals['_CREATEDATABASEREQUEST']._serialized_end = 845
    _globals['_CREATEDATABASEMETADATA']._serialized_start = 847
    _globals['_CREATEDATABASEMETADATA']._serialized_end = 871
    _globals['_LISTDATABASESRESPONSE']._serialized_start = 873
    _globals['_LISTDATABASESRESPONSE']._serialized_end = 973
    _globals['_GETDATABASEREQUEST']._serialized_start = 975
    _globals['_GETDATABASEREQUEST']._serialized_end = 1052
    _globals['_UPDATEDATABASEREQUEST']._serialized_start = 1055
    _globals['_UPDATEDATABASEREQUEST']._serialized_end = 1187
    _globals['_UPDATEDATABASEMETADATA']._serialized_start = 1189
    _globals['_UPDATEDATABASEMETADATA']._serialized_end = 1213
    _globals['_DELETEDATABASEREQUEST']._serialized_start = 1215
    _globals['_DELETEDATABASEREQUEST']._serialized_end = 1309
    _globals['_DELETEDATABASEMETADATA']._serialized_start = 1311
    _globals['_DELETEDATABASEMETADATA']._serialized_end = 1335
    _globals['_CREATEBACKUPSCHEDULEREQUEST']._serialized_start = 1338
    _globals['_CREATEBACKUPSCHEDULEREQUEST']._serialized_end = 1499
    _globals['_GETBACKUPSCHEDULEREQUEST']._serialized_start = 1501
    _globals['_GETBACKUPSCHEDULEREQUEST']._serialized_end = 1590
    _globals['_UPDATEBACKUPSCHEDULEREQUEST']._serialized_start = 1593
    _globals['_UPDATEBACKUPSCHEDULEREQUEST']._serialized_end = 1744
    _globals['_LISTBACKUPSCHEDULESREQUEST']._serialized_start = 1746
    _globals['_LISTBACKUPSCHEDULESREQUEST']._serialized_end = 1833
    _globals['_LISTBACKUPSCHEDULESRESPONSE']._serialized_start = 1835
    _globals['_LISTBACKUPSCHEDULESRESPONSE']._serialized_end = 1933
    _globals['_DELETEBACKUPSCHEDULEREQUEST']._serialized_start = 1935
    _globals['_DELETEBACKUPSCHEDULEREQUEST']._serialized_end = 2027
    _globals['_CREATEINDEXREQUEST']._serialized_start = 2030
    _globals['_CREATEINDEXREQUEST']._serialized_end = 2170
    _globals['_LISTINDEXESREQUEST']._serialized_start = 2173
    _globals['_LISTINDEXESREQUEST']._serialized_end = 2314
    _globals['_LISTINDEXESRESPONSE']._serialized_start = 2316
    _globals['_LISTINDEXESRESPONSE']._serialized_end = 2413
    _globals['_GETINDEXREQUEST']._serialized_start = 2415
    _globals['_GETINDEXREQUEST']._serialized_end = 2486
    _globals['_DELETEINDEXREQUEST']._serialized_start = 2488
    _globals['_DELETEINDEXREQUEST']._serialized_end = 2562
    _globals['_UPDATEFIELDREQUEST']._serialized_start = 2564
    _globals['_UPDATEFIELDREQUEST']._serialized_end = 2687
    _globals['_GETFIELDREQUEST']._serialized_start = 2689
    _globals['_GETFIELDREQUEST']._serialized_end = 2760
    _globals['_LISTFIELDSREQUEST']._serialized_start = 2763
    _globals['_LISTFIELDSREQUEST']._serialized_end = 2903
    _globals['_LISTFIELDSRESPONSE']._serialized_start = 2905
    _globals['_LISTFIELDSRESPONSE']._serialized_end = 3000
    _globals['_EXPORTDOCUMENTSREQUEST']._serialized_start = 3003
    _globals['_EXPORTDOCUMENTSREQUEST']._serialized_end = 3209
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_start = 3212
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_end = 3366
    _globals['_BULKDELETEDOCUMENTSREQUEST']._serialized_start = 3369
    _globals['_BULKDELETEDOCUMENTSREQUEST']._serialized_end = 3511
    _globals['_BULKDELETEDOCUMENTSRESPONSE']._serialized_start = 3513
    _globals['_BULKDELETEDOCUMENTSRESPONSE']._serialized_end = 3542
    _globals['_GETBACKUPREQUEST']._serialized_start = 3544
    _globals['_GETBACKUPREQUEST']._serialized_end = 3617
    _globals['_LISTBACKUPSREQUEST']._serialized_start = 3619
    _globals['_LISTBACKUPSREQUEST']._serialized_end = 3698
    _globals['_LISTBACKUPSRESPONSE']._serialized_start = 3700
    _globals['_LISTBACKUPSRESPONSE']._serialized_end = 3794
    _globals['_DELETEBACKUPREQUEST']._serialized_start = 3796
    _globals['_DELETEBACKUPREQUEST']._serialized_end = 3872
    _globals['_RESTOREDATABASEREQUEST']._serialized_start = 3875
    _globals['_RESTOREDATABASEREQUEST']._serialized_end = 4127
    _globals['_FIRESTOREADMIN']._serialized_start = 4130
    _globals['_FIRESTOREADMIN']._serialized_end = 8941