"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkebackup/v1/volume.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkebackup.v1 import common_pb2 as google_dot_cloud_dot_gkebackup_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/gkebackup/v1/volume.proto\x12\x19google.cloud.gkebackup.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/gkebackup/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa8\x07\n\x0cVolumeBackup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\nsource_pvc\x18\x05 \x01(\x0b2).google.cloud.gkebackup.v1.NamespacedNameB\x03\xe0A\x03\x12!\n\x14volume_backup_handle\x18\x06 \x01(\tB\x03\xe0A\x03\x12O\n\x06format\x18\x07 \x01(\x0e2:.google.cloud.gkebackup.v1.VolumeBackup.VolumeBackupFormatB\x03\xe0A\x03\x12\x1a\n\rstorage_bytes\x18\x08 \x01(\x03B\x03\xe0A\x03\x12\x1c\n\x0fdisk_size_bytes\x18\t \x01(\x03B\x03\xe0A\x03\x126\n\rcomplete_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\x05state\x18\x0b \x01(\x0e2-.google.cloud.gkebackup.v1.VolumeBackup.StateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\x0c \x01(\tB\x03\xe0A\x03\x12\x11\n\x04etag\x18\r \x01(\tB\x03\xe0A\x03"S\n\x12VolumeBackupFormat\x12$\n VOLUME_BACKUP_FORMAT_UNSPECIFIED\x10\x00\x12\x17\n\x13GCE_PERSISTENT_DISK\x10\x01"v\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x10\n\x0cSNAPSHOTTING\x10\x02\x12\r\n\tUPLOADING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\n\n\x06FAILED\x10\x05\x12\x0c\n\x08DELETING\x10\x06:\x9d\x01\xeaA\x99\x01\n%gkebackup.googleapis.com/VolumeBackup\x12pprojects/{project}/locations/{location}/backupPlans/{backup_plan}/backups/{backup}/volumeBackups/{volume_backup}"\xe7\x06\n\rVolumeRestore\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\rvolume_backup\x18\x05 \x01(\tB\x03\xe0A\x03\x12B\n\ntarget_pvc\x18\x06 \x01(\x0b2).google.cloud.gkebackup.v1.NamespacedNameB\x03\xe0A\x03\x12\x1a\n\rvolume_handle\x18\x07 \x01(\tB\x03\xe0A\x03\x12M\n\x0bvolume_type\x18\x08 \x01(\x0e23.google.cloud.gkebackup.v1.VolumeRestore.VolumeTypeB\x03\xe0A\x03\x126\n\rcomplete_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\x05state\x18\n \x01(\x0e2..google.cloud.gkebackup.v1.VolumeRestore.StateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\x0b \x01(\tB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x0c \x01(\tB\x03\xe0A\x03"B\n\nVolumeType\x12\x1b\n\x17VOLUME_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13GCE_PERSISTENT_DISK\x10\x01"d\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\r\n\tRESTORING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0c\n\x08DELETING\x10\x05:\xa4\x01\xeaA\xa0\x01\n&gkebackup.googleapis.com/VolumeRestore\x12vprojects/{project}/locations/{location}/restorePlans/{restore_plan}/restores/{restore}/volumeRestores/{volume_restore}B\xc2\x01\n\x1dcom.google.cloud.gkebackup.v1B\x0bVolumeProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.v1.volume_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.gkebackup.v1B\x0bVolumeProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1'
    _globals['_VOLUMEBACKUP'].fields_by_name['name']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['uid']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['create_time']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['update_time']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['source_pvc']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['source_pvc']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['volume_backup_handle']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['volume_backup_handle']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['format']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['format']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['storage_bytes']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['storage_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['disk_size_bytes']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['disk_size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['complete_time']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['complete_time']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['state']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['state_message']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP'].fields_by_name['etag']._loaded_options = None
    _globals['_VOLUMEBACKUP'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMEBACKUP']._loaded_options = None
    _globals['_VOLUMEBACKUP']._serialized_options = b'\xeaA\x99\x01\n%gkebackup.googleapis.com/VolumeBackup\x12pprojects/{project}/locations/{location}/backupPlans/{backup_plan}/backups/{backup}/volumeBackups/{volume_backup}'
    _globals['_VOLUMERESTORE'].fields_by_name['name']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['uid']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['create_time']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['update_time']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['volume_backup']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['volume_backup']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['target_pvc']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['target_pvc']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['volume_handle']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['volume_handle']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['volume_type']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['volume_type']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['complete_time']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['complete_time']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['state']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['state_message']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE'].fields_by_name['etag']._loaded_options = None
    _globals['_VOLUMERESTORE'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMERESTORE']._loaded_options = None
    _globals['_VOLUMERESTORE']._serialized_options = b'\xeaA\xa0\x01\n&gkebackup.googleapis.com/VolumeRestore\x12vprojects/{project}/locations/{location}/restorePlans/{restore_plan}/restores/{restore}/volumeRestores/{volume_restore}'
    _globals['_VOLUMEBACKUP']._serialized_start = 203
    _globals['_VOLUMEBACKUP']._serialized_end = 1139
    _globals['_VOLUMEBACKUP_VOLUMEBACKUPFORMAT']._serialized_start = 776
    _globals['_VOLUMEBACKUP_VOLUMEBACKUPFORMAT']._serialized_end = 859
    _globals['_VOLUMEBACKUP_STATE']._serialized_start = 861
    _globals['_VOLUMEBACKUP_STATE']._serialized_end = 979
    _globals['_VOLUMERESTORE']._serialized_start = 1142
    _globals['_VOLUMERESTORE']._serialized_end = 2013
    _globals['_VOLUMERESTORE_VOLUMETYPE']._serialized_start = 1678
    _globals['_VOLUMERESTORE_VOLUMETYPE']._serialized_end = 1744
    _globals['_VOLUMERESTORE_STATE']._serialized_start = 1746
    _globals['_VOLUMERESTORE_STATE']._serialized_end = 1846