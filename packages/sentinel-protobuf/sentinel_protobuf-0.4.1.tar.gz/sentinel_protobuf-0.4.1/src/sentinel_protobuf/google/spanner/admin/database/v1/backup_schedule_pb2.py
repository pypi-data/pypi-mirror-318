"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/admin/database/v1/backup_schedule.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.spanner.admin.database.v1 import backup_pb2 as google_dot_spanner_dot_admin_dot_database_dot_v1_dot_backup__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/spanner/admin/database/v1/backup_schedule.proto\x12 google.spanner.admin.database.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-google/spanner/admin/database/v1/backup.proto"i\n\x12BackupScheduleSpec\x12B\n\tcron_spec\x18\x01 \x01(\x0b2-.google.spanner.admin.database.v1.CrontabSpecH\x00B\x0f\n\rschedule_spec"\xa4\x05\n\x0eBackupSchedule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12G\n\x04spec\x18\x06 \x01(\x0b24.google.spanner.admin.database.v1.BackupScheduleSpecB\x03\xe0A\x01\x12:\n\x12retention_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12^\n\x11encryption_config\x18\x04 \x01(\x0b2>.google.spanner.admin.database.v1.CreateBackupEncryptionConfigB\x03\xe0A\x01\x12L\n\x10full_backup_spec\x18\x07 \x01(\x0b20.google.spanner.admin.database.v1.FullBackupSpecH\x00\x12Z\n\x17incremental_backup_spec\x18\x08 \x01(\x0b27.google.spanner.admin.database.v1.IncrementalBackupSpecH\x00\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\xa5\x01\xeaA\xa1\x01\n%spanner.googleapis.com/BackupSchedule\x12Wprojects/{project}/instances/{instance}/databases/{database}/backupSchedules/{schedule}*\x0fbackupSchedules2\x0ebackupScheduleB\x12\n\x10backup_type_spec"q\n\x0bCrontabSpec\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\ttime_zone\x18\x02 \x01(\tB\x03\xe0A\x03\x127\n\x0fcreation_window\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03"\xc7\x01\n\x1bCreateBackupScheduleRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database\x12\x1f\n\x12backup_schedule_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12N\n\x0fbackup_schedule\x18\x03 \x01(\x0b20.google.spanner.admin.database.v1.BackupScheduleB\x03\xe0A\x02"W\n\x18GetBackupScheduleRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%spanner.googleapis.com/BackupSchedule"Z\n\x1bDeleteBackupScheduleRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%spanner.googleapis.com/BackupSchedule"\x86\x01\n\x1aListBackupSchedulesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"\x82\x01\n\x1bListBackupSchedulesResponse\x12J\n\x10backup_schedules\x18\x01 \x03(\x0b20.google.spanner.admin.database.v1.BackupSchedule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa3\x01\n\x1bUpdateBackupScheduleRequest\x12N\n\x0fbackup_schedule\x18\x01 \x01(\x0b20.google.spanner.admin.database.v1.BackupScheduleB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02B\x85\x02\n$com.google.spanner.admin.database.v1B\x13BackupScheduleProtoP\x01ZFcloud.google.com/go/spanner/admin/database/apiv1/databasepb;databasepb\xaa\x02&Google.Cloud.Spanner.Admin.Database.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Database\\V1\xea\x02+Google::Cloud::Spanner::Admin::Database::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.admin.database.v1.backup_schedule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.spanner.admin.database.v1B\x13BackupScheduleProtoP\x01ZFcloud.google.com/go/spanner/admin/database/apiv1/databasepb;databasepb\xaa\x02&Google.Cloud.Spanner.Admin.Database.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Database\\V1\xea\x02+Google::Cloud::Spanner::Admin::Database::V1'
    _globals['_BACKUPSCHEDULE'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPSCHEDULE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_BACKUPSCHEDULE'].fields_by_name['spec']._loaded_options = None
    _globals['_BACKUPSCHEDULE'].fields_by_name['spec']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPSCHEDULE'].fields_by_name['retention_duration']._loaded_options = None
    _globals['_BACKUPSCHEDULE'].fields_by_name['retention_duration']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPSCHEDULE'].fields_by_name['encryption_config']._loaded_options = None
    _globals['_BACKUPSCHEDULE'].fields_by_name['encryption_config']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPSCHEDULE'].fields_by_name['update_time']._loaded_options = None
    _globals['_BACKUPSCHEDULE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPSCHEDULE']._loaded_options = None
    _globals['_BACKUPSCHEDULE']._serialized_options = b'\xeaA\xa1\x01\n%spanner.googleapis.com/BackupSchedule\x12Wprojects/{project}/instances/{instance}/databases/{database}/backupSchedules/{schedule}*\x0fbackupSchedules2\x0ebackupSchedule'
    _globals['_CRONTABSPEC'].fields_by_name['text']._loaded_options = None
    _globals['_CRONTABSPEC'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_CRONTABSPEC'].fields_by_name['time_zone']._loaded_options = None
    _globals['_CRONTABSPEC'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x03'
    _globals['_CRONTABSPEC'].fields_by_name['creation_window']._loaded_options = None
    _globals['_CRONTABSPEC'].fields_by_name['creation_window']._serialized_options = b'\xe0A\x03'
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule_id']._loaded_options = None
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule']._loaded_options = None
    _globals['_CREATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule']._serialized_options = b'\xe0A\x02'
    _globals['_GETBACKUPSCHEDULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPSCHEDULEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%spanner.googleapis.com/BackupSchedule"
    _globals['_DELETEBACKUPSCHEDULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPSCHEDULEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%spanner.googleapis.com/BackupSchedule"
    _globals['_LISTBACKUPSCHEDULESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPSCHEDULESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_LISTBACKUPSCHEDULESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTBACKUPSCHEDULESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBACKUPSCHEDULESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTBACKUPSCHEDULESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule']._loaded_options = None
    _globals['_UPDATEBACKUPSCHEDULEREQUEST'].fields_by_name['backup_schedule']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBACKUPSCHEDULEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBACKUPSCHEDULEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPSCHEDULESPEC']._serialized_start = 298
    _globals['_BACKUPSCHEDULESPEC']._serialized_end = 403
    _globals['_BACKUPSCHEDULE']._serialized_start = 406
    _globals['_BACKUPSCHEDULE']._serialized_end = 1082
    _globals['_CRONTABSPEC']._serialized_start = 1084
    _globals['_CRONTABSPEC']._serialized_end = 1197
    _globals['_CREATEBACKUPSCHEDULEREQUEST']._serialized_start = 1200
    _globals['_CREATEBACKUPSCHEDULEREQUEST']._serialized_end = 1399
    _globals['_GETBACKUPSCHEDULEREQUEST']._serialized_start = 1401
    _globals['_GETBACKUPSCHEDULEREQUEST']._serialized_end = 1488
    _globals['_DELETEBACKUPSCHEDULEREQUEST']._serialized_start = 1490
    _globals['_DELETEBACKUPSCHEDULEREQUEST']._serialized_end = 1580
    _globals['_LISTBACKUPSCHEDULESREQUEST']._serialized_start = 1583
    _globals['_LISTBACKUPSCHEDULESREQUEST']._serialized_end = 1717
    _globals['_LISTBACKUPSCHEDULESRESPONSE']._serialized_start = 1720
    _globals['_LISTBACKUPSCHEDULESRESPONSE']._serialized_end = 1850
    _globals['_UPDATEBACKUPSCHEDULEREQUEST']._serialized_start = 1853
    _globals['_UPDATEBACKUPSCHEDULEREQUEST']._serialized_end = 2016