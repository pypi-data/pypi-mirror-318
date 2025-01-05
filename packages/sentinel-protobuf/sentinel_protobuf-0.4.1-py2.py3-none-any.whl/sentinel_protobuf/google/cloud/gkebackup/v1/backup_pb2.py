"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkebackup/v1/backup.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkebackup.v1 import common_pb2 as google_dot_cloud_dot_gkebackup_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/gkebackup/v1/backup.proto\x12\x19google.cloud.gkebackup.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/gkebackup/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x86\x0e\n\x06Backup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06manual\x18\x05 \x01(\x08B\x03\xe0A\x03\x12B\n\x06labels\x18\x06 \x03(\x0b2-.google.cloud.gkebackup.v1.Backup.LabelsEntryB\x03\xe0A\x01\x12\x1d\n\x10delete_lock_days\x18\x07 \x01(\x05B\x03\xe0A\x01\x12@\n\x17delete_lock_expire_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bretain_days\x18\t \x01(\x05B\x03\xe0A\x01\x12;\n\x12retain_expire_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x0eencryption_key\x18\x0b \x01(\x0b2(.google.cloud.gkebackup.v1.EncryptionKeyB\x03\xe0A\x03\x12\x1d\n\x0eall_namespaces\x18\x0c \x01(\x08B\x03\xe0A\x03H\x00\x12I\n\x13selected_namespaces\x18\r \x01(\x0b2%.google.cloud.gkebackup.v1.NamespacesB\x03\xe0A\x03H\x00\x12P\n\x15selected_applications\x18\x0e \x01(\x0b2*.google.cloud.gkebackup.v1.NamespacedNamesB\x03\xe0A\x03H\x00\x12!\n\x14contains_volume_data\x18\x0f \x01(\x08B\x03\xe0A\x03\x12\x1d\n\x10contains_secrets\x18\x10 \x01(\x08B\x03\xe0A\x03\x12P\n\x10cluster_metadata\x18\x11 \x01(\x0b21.google.cloud.gkebackup.v1.Backup.ClusterMetadataB\x03\xe0A\x03\x12;\n\x05state\x18\x12 \x01(\x0e2\'.google.cloud.gkebackup.v1.Backup.StateB\x03\xe0A\x03\x12\x19\n\x0cstate_reason\x18\x13 \x01(\tB\x03\xe0A\x03\x126\n\rcomplete_time\x18\x14 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1b\n\x0eresource_count\x18\x15 \x01(\x05B\x03\xe0A\x03\x12\x19\n\x0cvolume_count\x18\x16 \x01(\x05B\x03\xe0A\x03\x12\x17\n\nsize_bytes\x18\x17 \x01(\x03B\x03\xe0A\x03\x12\x11\n\x04etag\x18\x18 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x19 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpod_count\x18\x1a \x01(\x05B\x03\xe0A\x03\x12%\n\x18config_backup_size_bytes\x18\x1b \x01(\x03B\x03\xe0A\x03\x12\x1c\n\x0fpermissive_mode\x18\x1c \x01(\x08B\x03\xe0A\x03\x1a\xb6\x02\n\x0fClusterMetadata\x12\x14\n\x07cluster\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bk8s_version\x18\x02 \x01(\tB\x03\xe0A\x03\x12j\n\x13backup_crd_versions\x18\x03 \x03(\x0b2H.google.cloud.gkebackup.v1.Backup.ClusterMetadata.BackupCrdVersionsEntryB\x03\xe0A\x03\x12\x1a\n\x0bgke_version\x18\x04 \x01(\tB\x03\xe0A\x03H\x00\x12\x1d\n\x0eanthos_version\x18\x05 \x01(\tB\x03\xe0A\x03H\x00\x1a8\n\x16BackupCrdVersionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x12\n\x10platform_version\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"f\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0c\n\x08DELETING\x10\x05:x\xeaAu\n\x1fgkebackup.googleapis.com/Backup\x12Rprojects/{project}/locations/{location}/backupPlans/{backup_plan}/backups/{backup}B\x0e\n\x0cbackup_scopeB\xc2\x01\n\x1dcom.google.cloud.gkebackup.v1B\x0bBackupProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.v1.backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.gkebackup.v1B\x0bBackupProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1'
    _globals['_BACKUP_CLUSTERMETADATA_BACKUPCRDVERSIONSENTRY']._loaded_options = None
    _globals['_BACKUP_CLUSTERMETADATA_BACKUPCRDVERSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['cluster']._loaded_options = None
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['cluster']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['k8s_version']._loaded_options = None
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['k8s_version']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['backup_crd_versions']._loaded_options = None
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['backup_crd_versions']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['gke_version']._loaded_options = None
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['gke_version']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['anthos_version']._loaded_options = None
    _globals['_BACKUP_CLUSTERMETADATA'].fields_by_name['anthos_version']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP_LABELSENTRY']._loaded_options = None
    _globals['_BACKUP_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKUP'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['uid']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['update_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['manual']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['manual']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['labels']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUP'].fields_by_name['delete_lock_days']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['delete_lock_days']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUP'].fields_by_name['delete_lock_expire_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['delete_lock_expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['retain_days']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['retain_days']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUP'].fields_by_name['retain_expire_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['retain_expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['encryption_key']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['encryption_key']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['all_namespaces']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['all_namespaces']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['selected_namespaces']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['selected_namespaces']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['selected_applications']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['selected_applications']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['contains_volume_data']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['contains_volume_data']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['contains_secrets']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['contains_secrets']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['cluster_metadata']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['cluster_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['state_reason']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['state_reason']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['complete_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['complete_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['resource_count']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['resource_count']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['volume_count']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['volume_count']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['size_bytes']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['etag']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['description']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUP'].fields_by_name['pod_count']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['pod_count']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['config_backup_size_bytes']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['config_backup_size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['permissive_mode']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['permissive_mode']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP']._loaded_options = None
    _globals['_BACKUP']._serialized_options = b'\xeaAu\n\x1fgkebackup.googleapis.com/Backup\x12Rprojects/{project}/locations/{location}/backupPlans/{backup_plan}/backups/{backup}'
    _globals['_BACKUP']._serialized_start = 203
    _globals['_BACKUP']._serialized_end = 2001
    _globals['_BACKUP_CLUSTERMETADATA']._serialized_start = 1402
    _globals['_BACKUP_CLUSTERMETADATA']._serialized_end = 1712
    _globals['_BACKUP_CLUSTERMETADATA_BACKUPCRDVERSIONSENTRY']._serialized_start = 1636
    _globals['_BACKUP_CLUSTERMETADATA_BACKUPCRDVERSIONSENTRY']._serialized_end = 1692
    _globals['_BACKUP_LABELSENTRY']._serialized_start = 1714
    _globals['_BACKUP_LABELSENTRY']._serialized_end = 1759
    _globals['_BACKUP_STATE']._serialized_start = 1761
    _globals['_BACKUP_STATE']._serialized_end = 1863