"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkebackup/v1/backup_plan.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkebackup.v1 import common_pb2 as google_dot_cloud_dot_gkebackup_dot_v1_dot_common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
from .....google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from .....google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/gkebackup/v1/backup_plan.proto\x12\x19google.cloud.gkebackup.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/gkebackup/v1/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x1bgoogle/type/timeofday.proto"\xd4\r\n\nBackupPlan\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x12<\n\x07cluster\x18\x06 \x01(\tB+\xe0A\x05\xe0A\x02\xfaA"\n container.googleapis.com/Cluster\x12T\n\x10retention_policy\x18\x07 \x01(\x0b25.google.cloud.gkebackup.v1.BackupPlan.RetentionPolicyB\x03\xe0A\x01\x12F\n\x06labels\x18\x08 \x03(\x0b21.google.cloud.gkebackup.v1.BackupPlan.LabelsEntryB\x03\xe0A\x01\x12L\n\x0fbackup_schedule\x18\t \x01(\x0b2..google.cloud.gkebackup.v1.BackupPlan.ScheduleB\x03\xe0A\x01\x12\x11\n\x04etag\x18\n \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdeactivated\x18\x0b \x01(\x08B\x03\xe0A\x01\x12N\n\rbackup_config\x18\x0c \x01(\x0b22.google.cloud.gkebackup.v1.BackupPlan.BackupConfigB\x03\xe0A\x01\x12 \n\x13protected_pod_count\x18\r \x01(\x05B\x03\xe0A\x03\x12?\n\x05state\x18\x0e \x01(\x0e2+.google.cloud.gkebackup.v1.BackupPlan.StateB\x03\xe0A\x03\x12\x19\n\x0cstate_reason\x18\x0f \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0erpo_risk_level\x18\x10 \x01(\x05B\x03\xe0A\x03\x12\x1c\n\x0frpo_risk_reason\x18\x11 \x01(\tB\x03\xe0A\x03\x1am\n\x0fRetentionPolicy\x12$\n\x17backup_delete_lock_days\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x1f\n\x12backup_retain_days\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x13\n\x06locked\x18\x03 \x01(\x08B\x03\xe0A\x01\x1a\xbf\x01\n\x08Schedule\x12\x1a\n\rcron_schedule\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06paused\x18\x02 \x01(\x08B\x03\xe0A\x01\x12=\n\nrpo_config\x18\x03 \x01(\x0b2$.google.cloud.gkebackup.v1.RpoConfigB\x03\xe0A\x01\x12C\n\x1anext_scheduled_backup_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a\xf0\x02\n\x0cBackupConfig\x12\x18\n\x0eall_namespaces\x18\x01 \x01(\x08H\x00\x12D\n\x13selected_namespaces\x18\x02 \x01(\x0b2%.google.cloud.gkebackup.v1.NamespacesH\x00\x12K\n\x15selected_applications\x18\x03 \x01(\x0b2*.google.cloud.gkebackup.v1.NamespacedNamesH\x00\x12 \n\x13include_volume_data\x18\x04 \x01(\x08B\x03\xe0A\x01\x12\x1c\n\x0finclude_secrets\x18\x05 \x01(\x08B\x03\xe0A\x01\x12E\n\x0eencryption_key\x18\x06 \x01(\x0b2(.google.cloud.gkebackup.v1.EncryptionKeyB\x03\xe0A\x01\x12\x1c\n\x0fpermissive_mode\x18\x07 \x01(\x08B\x03\xe0A\x01B\x0e\n\x0cbackup_scope\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"{\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x13\n\x0fCLUSTER_PENDING\x10\x01\x12\x10\n\x0cPROVISIONING\x10\x02\x12\t\n\x05READY\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0f\n\x0bDEACTIVATED\x10\x05\x12\x0c\n\x08DELETING\x10\x06:k\xeaAh\n#gkebackup.googleapis.com/BackupPlan\x12Aprojects/{project}/locations/{location}/backupPlans/{backup_plan}"x\n\tRpoConfig\x12\x1f\n\x12target_rpo_minutes\x18\x01 \x01(\x05B\x03\xe0A\x02\x12J\n\x11exclusion_windows\x18\x02 \x03(\x0b2*.google.cloud.gkebackup.v1.ExclusionWindowB\x03\xe0A\x01"\xde\x02\n\x0fExclusionWindow\x12/\n\nstart_time\x18\x01 \x01(\x0b2\x16.google.type.TimeOfDayB\x03\xe0A\x02\x120\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x123\n\x16single_occurrence_date\x18\x03 \x01(\x0b2\x11.google.type.DateH\x00\x12\x0f\n\x05daily\x18\x04 \x01(\x08H\x00\x12P\n\x0cdays_of_week\x18\x05 \x01(\x0b28.google.cloud.gkebackup.v1.ExclusionWindow.DayOfWeekListH\x00\x1aB\n\rDayOfWeekList\x121\n\x0cdays_of_week\x18\x01 \x03(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x01B\x0c\n\nrecurrenceB\xc6\x01\n\x1dcom.google.cloud.gkebackup.v1B\x0fBackupPlanProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.v1.backup_plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.gkebackup.v1B\x0fBackupPlanProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1'
    _globals['_BACKUPPLAN_RETENTIONPOLICY'].fields_by_name['backup_delete_lock_days']._loaded_options = None
    _globals['_BACKUPPLAN_RETENTIONPOLICY'].fields_by_name['backup_delete_lock_days']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_RETENTIONPOLICY'].fields_by_name['backup_retain_days']._loaded_options = None
    _globals['_BACKUPPLAN_RETENTIONPOLICY'].fields_by_name['backup_retain_days']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_RETENTIONPOLICY'].fields_by_name['locked']._loaded_options = None
    _globals['_BACKUPPLAN_RETENTIONPOLICY'].fields_by_name['locked']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_SCHEDULE'].fields_by_name['cron_schedule']._loaded_options = None
    _globals['_BACKUPPLAN_SCHEDULE'].fields_by_name['cron_schedule']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_SCHEDULE'].fields_by_name['paused']._loaded_options = None
    _globals['_BACKUPPLAN_SCHEDULE'].fields_by_name['paused']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_SCHEDULE'].fields_by_name['rpo_config']._loaded_options = None
    _globals['_BACKUPPLAN_SCHEDULE'].fields_by_name['rpo_config']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_SCHEDULE'].fields_by_name['next_scheduled_backup_time']._loaded_options = None
    _globals['_BACKUPPLAN_SCHEDULE'].fields_by_name['next_scheduled_backup_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN_BACKUPCONFIG'].fields_by_name['include_volume_data']._loaded_options = None
    _globals['_BACKUPPLAN_BACKUPCONFIG'].fields_by_name['include_volume_data']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_BACKUPCONFIG'].fields_by_name['include_secrets']._loaded_options = None
    _globals['_BACKUPPLAN_BACKUPCONFIG'].fields_by_name['include_secrets']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_BACKUPCONFIG'].fields_by_name['encryption_key']._loaded_options = None
    _globals['_BACKUPPLAN_BACKUPCONFIG'].fields_by_name['encryption_key']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_BACKUPCONFIG'].fields_by_name['permissive_mode']._loaded_options = None
    _globals['_BACKUPPLAN_BACKUPCONFIG'].fields_by_name['permissive_mode']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN_LABELSENTRY']._loaded_options = None
    _globals['_BACKUPPLAN_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKUPPLAN'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['uid']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['update_time']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['description']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN'].fields_by_name['cluster']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['cluster']._serialized_options = b'\xe0A\x05\xe0A\x02\xfaA"\n container.googleapis.com/Cluster'
    _globals['_BACKUPPLAN'].fields_by_name['retention_policy']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['retention_policy']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN'].fields_by_name['labels']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN'].fields_by_name['backup_schedule']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['backup_schedule']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN'].fields_by_name['etag']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['deactivated']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['deactivated']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN'].fields_by_name['backup_config']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['backup_config']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN'].fields_by_name['protected_pod_count']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['protected_pod_count']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['state_reason']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['state_reason']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['rpo_risk_level']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['rpo_risk_level']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['rpo_risk_reason']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['rpo_risk_reason']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN']._loaded_options = None
    _globals['_BACKUPPLAN']._serialized_options = b'\xeaAh\n#gkebackup.googleapis.com/BackupPlan\x12Aprojects/{project}/locations/{location}/backupPlans/{backup_plan}'
    _globals['_RPOCONFIG'].fields_by_name['target_rpo_minutes']._loaded_options = None
    _globals['_RPOCONFIG'].fields_by_name['target_rpo_minutes']._serialized_options = b'\xe0A\x02'
    _globals['_RPOCONFIG'].fields_by_name['exclusion_windows']._loaded_options = None
    _globals['_RPOCONFIG'].fields_by_name['exclusion_windows']._serialized_options = b'\xe0A\x01'
    _globals['_EXCLUSIONWINDOW_DAYOFWEEKLIST'].fields_by_name['days_of_week']._loaded_options = None
    _globals['_EXCLUSIONWINDOW_DAYOFWEEKLIST'].fields_by_name['days_of_week']._serialized_options = b'\xe0A\x01'
    _globals['_EXCLUSIONWINDOW'].fields_by_name['start_time']._loaded_options = None
    _globals['_EXCLUSIONWINDOW'].fields_by_name['start_time']._serialized_options = b'\xe0A\x02'
    _globals['_EXCLUSIONWINDOW'].fields_by_name['duration']._loaded_options = None
    _globals['_EXCLUSIONWINDOW'].fields_by_name['duration']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPPLAN']._serialized_start = 322
    _globals['_BACKUPPLAN']._serialized_end = 2070
    _globals['_BACKUPPLAN_RETENTIONPOLICY']._serialized_start = 1115
    _globals['_BACKUPPLAN_RETENTIONPOLICY']._serialized_end = 1224
    _globals['_BACKUPPLAN_SCHEDULE']._serialized_start = 1227
    _globals['_BACKUPPLAN_SCHEDULE']._serialized_end = 1418
    _globals['_BACKUPPLAN_BACKUPCONFIG']._serialized_start = 1421
    _globals['_BACKUPPLAN_BACKUPCONFIG']._serialized_end = 1789
    _globals['_BACKUPPLAN_LABELSENTRY']._serialized_start = 1791
    _globals['_BACKUPPLAN_LABELSENTRY']._serialized_end = 1836
    _globals['_BACKUPPLAN_STATE']._serialized_start = 1838
    _globals['_BACKUPPLAN_STATE']._serialized_end = 1961
    _globals['_RPOCONFIG']._serialized_start = 2072
    _globals['_RPOCONFIG']._serialized_end = 2192
    _globals['_EXCLUSIONWINDOW']._serialized_start = 2195
    _globals['_EXCLUSIONWINDOW']._serialized_end = 2545
    _globals['_EXCLUSIONWINDOW_DAYOFWEEKLIST']._serialized_start = 2465
    _globals['_EXCLUSIONWINDOW_DAYOFWEEKLIST']._serialized_end = 2531