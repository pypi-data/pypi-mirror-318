"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkebackup/logging/v1/logged_backup_plan.proto')
_sym_db = _symbol_database.Default()
from ......google.cloud.gkebackup.logging.v1 import logged_common_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/gkebackup/logging/v1/logged_backup_plan.proto\x12!google.cloud.gkebackup.logging.v1\x1a5google/cloud/gkebackup/logging/v1/logged_common.proto"\xe5\x07\n\x10LoggedBackupPlan\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12\x0f\n\x07cluster\x18\x02 \x01(\t\x12]\n\x10retention_policy\x18\x03 \x01(\x0b2C.google.cloud.gkebackup.logging.v1.LoggedBackupPlan.RetentionPolicy\x12O\n\x06labels\x18\x04 \x03(\x0b2?.google.cloud.gkebackup.logging.v1.LoggedBackupPlan.LabelsEntry\x12U\n\x0fbackup_schedule\x18\x05 \x01(\x0b2<.google.cloud.gkebackup.logging.v1.LoggedBackupPlan.Schedule\x12\x13\n\x0bdeactivated\x18\x06 \x01(\x08\x12W\n\rbackup_config\x18\x07 \x01(\x0b2@.google.cloud.gkebackup.logging.v1.LoggedBackupPlan.BackupConfig\x12\x16\n\x0erpo_risk_level\x18\x08 \x01(\x05\x1a^\n\x0fRetentionPolicy\x12\x1f\n\x17backup_delete_lock_days\x18\x01 \x01(\x05\x12\x1a\n\x12backup_retain_days\x18\x02 \x01(\x05\x12\x0e\n\x06locked\x18\x03 \x01(\x08\x1a1\n\x08Schedule\x12\x15\n\rcron_schedule\x18\x01 \x01(\t\x12\x0e\n\x06paused\x18\x02 \x01(\x08\x1a\xdb\x02\n\x0cBackupConfig\x12\x18\n\x0eall_namespaces\x18\x01 \x01(\x08H\x00\x12L\n\x13selected_namespaces\x18\x02 \x01(\x0b2-.google.cloud.gkebackup.logging.v1.NamespacesH\x00\x12S\n\x15selected_applications\x18\x03 \x01(\x0b22.google.cloud.gkebackup.logging.v1.NamespacedNamesH\x00\x12\x1b\n\x13include_volume_data\x18\x04 \x01(\x08\x12\x17\n\x0finclude_secrets\x18\x05 \x01(\x08\x12H\n\x0eencryption_key\x18\x06 \x01(\x0b20.google.cloud.gkebackup.logging.v1.EncryptionKeyB\x0e\n\x0cbackup_scope\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\xed\x01\n!google.cloud.gkebackup.logging.v1B\x15LoggedBackupPlanProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.logging.v1.logged_backup_plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!google.cloud.gkebackup.logging.v1B\x15LoggedBackupPlanProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1'
    _globals['_LOGGEDBACKUPPLAN_LABELSENTRY']._loaded_options = None
    _globals['_LOGGEDBACKUPPLAN_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LOGGEDBACKUPPLAN']._serialized_start = 153
    _globals['_LOGGEDBACKUPPLAN']._serialized_end = 1150
    _globals['_LOGGEDBACKUPPLAN_RETENTIONPOLICY']._serialized_start = 608
    _globals['_LOGGEDBACKUPPLAN_RETENTIONPOLICY']._serialized_end = 702
    _globals['_LOGGEDBACKUPPLAN_SCHEDULE']._serialized_start = 704
    _globals['_LOGGEDBACKUPPLAN_SCHEDULE']._serialized_end = 753
    _globals['_LOGGEDBACKUPPLAN_BACKUPCONFIG']._serialized_start = 756
    _globals['_LOGGEDBACKUPPLAN_BACKUPCONFIG']._serialized_end = 1103
    _globals['_LOGGEDBACKUPPLAN_LABELSENTRY']._serialized_start = 1105
    _globals['_LOGGEDBACKUPPLAN_LABELSENTRY']._serialized_end = 1150