"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/bigtable/admin/v2/table.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.bigtable.admin.v2 import types_pb2 as google_dot_bigtable_dot_admin_dot_v2_dot_types__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/bigtable/admin/v2/table.proto\x12\x18google.bigtable.admin.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/bigtable/admin/v2/types.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x9b\x01\n\x0bRestoreInfo\x12@\n\x0bsource_type\x18\x01 \x01(\x0e2+.google.bigtable.admin.v2.RestoreSourceType\x12;\n\x0bbackup_info\x18\x02 \x01(\x0b2$.google.bigtable.admin.v2.BackupInfoH\x00B\r\n\x0bsource_info"I\n\x12ChangeStreamConfig\x123\n\x10retention_period\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"\xd6\x0b\n\x05Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\x0ecluster_states\x18\x02 \x03(\x0b22.google.bigtable.admin.v2.Table.ClusterStatesEntryB\x03\xe0A\x03\x12L\n\x0fcolumn_families\x18\x03 \x03(\x0b23.google.bigtable.admin.v2.Table.ColumnFamiliesEntry\x12N\n\x0bgranularity\x18\x04 \x01(\x0e24.google.bigtable.admin.v2.Table.TimestampGranularityB\x03\xe0A\x05\x12@\n\x0crestore_info\x18\x06 \x01(\x0b2%.google.bigtable.admin.v2.RestoreInfoB\x03\xe0A\x03\x12J\n\x14change_stream_config\x18\x08 \x01(\x0b2,.google.bigtable.admin.v2.ChangeStreamConfig\x12\x1b\n\x13deletion_protection\x18\t \x01(\x08\x12X\n\x17automated_backup_policy\x18\r \x01(\x0b25.google.bigtable.admin.v2.Table.AutomatedBackupPolicyH\x00\x1a\xc6\x02\n\x0cClusterState\x12]\n\x11replication_state\x18\x01 \x01(\x0e2=.google.bigtable.admin.v2.Table.ClusterState.ReplicationStateB\x03\xe0A\x03\x12F\n\x0fencryption_info\x18\x02 \x03(\x0b2(.google.bigtable.admin.v2.EncryptionInfoB\x03\xe0A\x03"\x8e\x01\n\x10ReplicationState\x12\x13\n\x0fSTATE_NOT_KNOWN\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x17\n\x13PLANNED_MAINTENANCE\x10\x02\x12\x19\n\x15UNPLANNED_MAINTENANCE\x10\x03\x12\t\n\x05READY\x10\x04\x12\x14\n\x10READY_OPTIMIZING\x10\x05\x1a\x84\x01\n\x15AutomatedBackupPolicy\x128\n\x10retention_period\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x121\n\tfrequency\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x1ab\n\x12ClusterStatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b2,.google.bigtable.admin.v2.Table.ClusterState:\x028\x01\x1a]\n\x13ColumnFamiliesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.google.bigtable.admin.v2.ColumnFamily:\x028\x01"I\n\x14TimestampGranularity\x12%\n!TIMESTAMP_GRANULARITY_UNSPECIFIED\x10\x00\x12\n\n\x06MILLIS\x10\x01"q\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\r\n\tNAME_ONLY\x10\x01\x12\x0f\n\x0bSCHEMA_VIEW\x10\x02\x12\x14\n\x10REPLICATION_VIEW\x10\x03\x12\x13\n\x0fENCRYPTION_VIEW\x10\x05\x12\x08\n\x04FULL\x10\x04:_\xeaA\\\n"bigtableadmin.googleapis.com/Table\x126projects/{project}/instances/{instance}/tables/{table}B\x19\n\x17automated_backup_config"\xe3\x05\n\x0eAuthorizedView\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12J\n\x0bsubset_view\x18\x02 \x01(\x0b23.google.bigtable.admin.v2.AuthorizedView.SubsetViewH\x00\x12\x0c\n\x04etag\x18\x03 \x01(\t\x12\x1b\n\x13deletion_protection\x18\x04 \x01(\x08\x1a?\n\rFamilySubsets\x12\x12\n\nqualifiers\x18\x01 \x03(\x0c\x12\x1a\n\x12qualifier_prefixes\x18\x02 \x03(\x0c\x1a\xf0\x01\n\nSubsetView\x12\x14\n\x0crow_prefixes\x18\x01 \x03(\x0c\x12^\n\x0efamily_subsets\x18\x02 \x03(\x0b2F.google.bigtable.admin.v2.AuthorizedView.SubsetView.FamilySubsetsEntry\x1al\n\x12FamilySubsetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12E\n\x05value\x18\x02 \x01(\x0b26.google.bigtable.admin.v2.AuthorizedView.FamilySubsets:\x028\x01"Q\n\x0cResponseView\x12\x1d\n\x19RESPONSE_VIEW_UNSPECIFIED\x10\x00\x12\r\n\tNAME_ONLY\x10\x01\x12\t\n\x05BASIC\x10\x02\x12\x08\n\x04FULL\x10\x03:\xac\x01\xeaA\xa8\x01\n+bigtableadmin.googleapis.com/AuthorizedView\x12Xprojects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}*\x0fauthorizedViews2\x0eauthorizedViewB\x11\n\x0fauthorized_view"u\n\x0cColumnFamily\x121\n\x07gc_rule\x18\x01 \x01(\x0b2 .google.bigtable.admin.v2.GcRule\x122\n\nvalue_type\x18\x03 \x01(\x0b2\x1e.google.bigtable.admin.v2.Type"\xd5\x02\n\x06GcRule\x12\x1a\n\x10max_num_versions\x18\x01 \x01(\x05H\x00\x12,\n\x07max_age\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x12E\n\x0cintersection\x18\x03 \x01(\x0b2-.google.bigtable.admin.v2.GcRule.IntersectionH\x00\x127\n\x05union\x18\x04 \x01(\x0b2&.google.bigtable.admin.v2.GcRule.UnionH\x00\x1a?\n\x0cIntersection\x12/\n\x05rules\x18\x01 \x03(\x0b2 .google.bigtable.admin.v2.GcRule\x1a8\n\x05Union\x12/\n\x05rules\x18\x01 \x03(\x0b2 .google.bigtable.admin.v2.GcRuleB\x06\n\x04rule"\xd9\x02\n\x0eEncryptionInfo\x12U\n\x0fencryption_type\x18\x03 \x01(\x0e27.google.bigtable.admin.v2.EncryptionInfo.EncryptionTypeB\x03\xe0A\x03\x122\n\x11encryption_status\x18\x04 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12I\n\x0fkms_key_version\x18\x02 \x01(\tB0\xe0A\x03\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion"q\n\x0eEncryptionType\x12\x1f\n\x1bENCRYPTION_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19GOOGLE_DEFAULT_ENCRYPTION\x10\x01\x12\x1f\n\x1bCUSTOMER_MANAGED_ENCRYPTION\x10\x02"\xe0\x03\n\x08Snapshot\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x0csource_table\x18\x02 \x01(\x0b2\x1f.google.bigtable.admin.v2.TableB\x03\xe0A\x03\x12\x1c\n\x0fdata_size_bytes\x18\x03 \x01(\x03B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12/\n\x0bdelete_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12<\n\x05state\x18\x06 \x01(\x0e2(.google.bigtable.admin.v2.Snapshot.StateB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x07 \x01(\t"5\n\x05State\x12\x13\n\x0fSTATE_NOT_KNOWN\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0c\n\x08CREATING\x10\x02:{\xeaAx\n%bigtableadmin.googleapis.com/Snapshot\x12Oprojects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}"\xf9\x05\n\x06Backup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1c\n\x0csource_table\x18\x02 \x01(\tB\x06\xe0A\x05\xe0A\x02\x12\x1a\n\rsource_backup\x18\n \x01(\tB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x123\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x17\n\nsize_bytes\x18\x06 \x01(\x03B\x03\xe0A\x03\x12:\n\x05state\x18\x07 \x01(\x0e2&.google.bigtable.admin.v2.Backup.StateB\x03\xe0A\x03\x12F\n\x0fencryption_info\x18\t \x01(\x0b2(.google.bigtable.admin.v2.EncryptionInfoB\x03\xe0A\x03\x12@\n\x0bbackup_type\x18\x0b \x01(\x0e2+.google.bigtable.admin.v2.Backup.BackupType\x128\n\x14hot_to_standard_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.Timestamp"7\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02"@\n\nBackupType\x12\x1b\n\x17BACKUP_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x07\n\x03HOT\x10\x02:u\xeaAr\n#bigtableadmin.googleapis.com/Backup\x12Kprojects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup}"\xc0\x01\n\nBackupInfo\x12\x13\n\x06backup\x18\x01 \x01(\tB\x03\xe0A\x03\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x19\n\x0csource_table\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rsource_backup\x18\n \x01(\tB\x03\xe0A\x03*D\n\x11RestoreSourceType\x12#\n\x1fRESTORE_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06BACKUP\x10\x01B\xf7\x02\n\x1ccom.google.bigtable.admin.v2B\nTableProtoP\x01Z8cloud.google.com/go/bigtable/admin/apiv2/adminpb;adminpb\xaa\x02\x1eGoogle.Cloud.Bigtable.Admin.V2\xca\x02\x1eGoogle\\Cloud\\Bigtable\\Admin\\V2\xea\x02"Google::Cloud::Bigtable::Admin::V2\xeaA\xa6\x01\n(cloudkms.googleapis.com/CryptoKeyVersion\x12zprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.bigtable.admin.v2.table_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.bigtable.admin.v2B\nTableProtoP\x01Z8cloud.google.com/go/bigtable/admin/apiv2/adminpb;adminpb\xaa\x02\x1eGoogle.Cloud.Bigtable.Admin.V2\xca\x02\x1eGoogle\\Cloud\\Bigtable\\Admin\\V2\xea\x02"Google::Cloud::Bigtable::Admin::V2\xeaA\xa6\x01\n(cloudkms.googleapis.com/CryptoKeyVersion\x12zprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}'
    _globals['_TABLE_CLUSTERSTATE'].fields_by_name['replication_state']._loaded_options = None
    _globals['_TABLE_CLUSTERSTATE'].fields_by_name['replication_state']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE_CLUSTERSTATE'].fields_by_name['encryption_info']._loaded_options = None
    _globals['_TABLE_CLUSTERSTATE'].fields_by_name['encryption_info']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE_AUTOMATEDBACKUPPOLICY'].fields_by_name['retention_period']._loaded_options = None
    _globals['_TABLE_AUTOMATEDBACKUPPOLICY'].fields_by_name['retention_period']._serialized_options = b'\xe0A\x02'
    _globals['_TABLE_AUTOMATEDBACKUPPOLICY'].fields_by_name['frequency']._loaded_options = None
    _globals['_TABLE_AUTOMATEDBACKUPPOLICY'].fields_by_name['frequency']._serialized_options = b'\xe0A\x02'
    _globals['_TABLE_CLUSTERSTATESENTRY']._loaded_options = None
    _globals['_TABLE_CLUSTERSTATESENTRY']._serialized_options = b'8\x01'
    _globals['_TABLE_COLUMNFAMILIESENTRY']._loaded_options = None
    _globals['_TABLE_COLUMNFAMILIESENTRY']._serialized_options = b'8\x01'
    _globals['_TABLE'].fields_by_name['cluster_states']._loaded_options = None
    _globals['_TABLE'].fields_by_name['cluster_states']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['granularity']._loaded_options = None
    _globals['_TABLE'].fields_by_name['granularity']._serialized_options = b'\xe0A\x05'
    _globals['_TABLE'].fields_by_name['restore_info']._loaded_options = None
    _globals['_TABLE'].fields_by_name['restore_info']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE']._loaded_options = None
    _globals['_TABLE']._serialized_options = b'\xeaA\\\n"bigtableadmin.googleapis.com/Table\x126projects/{project}/instances/{instance}/tables/{table}'
    _globals['_AUTHORIZEDVIEW_SUBSETVIEW_FAMILYSUBSETSENTRY']._loaded_options = None
    _globals['_AUTHORIZEDVIEW_SUBSETVIEW_FAMILYSUBSETSENTRY']._serialized_options = b'8\x01'
    _globals['_AUTHORIZEDVIEW'].fields_by_name['name']._loaded_options = None
    _globals['_AUTHORIZEDVIEW'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_AUTHORIZEDVIEW']._loaded_options = None
    _globals['_AUTHORIZEDVIEW']._serialized_options = b'\xeaA\xa8\x01\n+bigtableadmin.googleapis.com/AuthorizedView\x12Xprojects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}*\x0fauthorizedViews2\x0eauthorizedView'
    _globals['_ENCRYPTIONINFO'].fields_by_name['encryption_type']._loaded_options = None
    _globals['_ENCRYPTIONINFO'].fields_by_name['encryption_type']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONINFO'].fields_by_name['encryption_status']._loaded_options = None
    _globals['_ENCRYPTIONINFO'].fields_by_name['encryption_status']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONINFO'].fields_by_name['kms_key_version']._loaded_options = None
    _globals['_ENCRYPTIONINFO'].fields_by_name['kms_key_version']._serialized_options = b'\xe0A\x03\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion'
    _globals['_SNAPSHOT'].fields_by_name['source_table']._loaded_options = None
    _globals['_SNAPSHOT'].fields_by_name['source_table']._serialized_options = b'\xe0A\x03'
    _globals['_SNAPSHOT'].fields_by_name['data_size_bytes']._loaded_options = None
    _globals['_SNAPSHOT'].fields_by_name['data_size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_SNAPSHOT'].fields_by_name['create_time']._loaded_options = None
    _globals['_SNAPSHOT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SNAPSHOT'].fields_by_name['state']._loaded_options = None
    _globals['_SNAPSHOT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SNAPSHOT']._loaded_options = None
    _globals['_SNAPSHOT']._serialized_options = b'\xeaAx\n%bigtableadmin.googleapis.com/Snapshot\x12Oprojects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}'
    _globals['_BACKUP'].fields_by_name['source_table']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['source_table']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_BACKUP'].fields_by_name['source_backup']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['source_backup']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['expire_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUP'].fields_by_name['start_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['end_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['size_bytes']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['encryption_info']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['encryption_info']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP']._loaded_options = None
    _globals['_BACKUP']._serialized_options = b'\xeaAr\n#bigtableadmin.googleapis.com/Backup\x12Kprojects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup}'
    _globals['_BACKUPINFO'].fields_by_name['backup']._loaded_options = None
    _globals['_BACKUPINFO'].fields_by_name['backup']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPINFO'].fields_by_name['start_time']._loaded_options = None
    _globals['_BACKUPINFO'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPINFO'].fields_by_name['end_time']._loaded_options = None
    _globals['_BACKUPINFO'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPINFO'].fields_by_name['source_table']._loaded_options = None
    _globals['_BACKUPINFO'].fields_by_name['source_table']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPINFO'].fields_by_name['source_backup']._loaded_options = None
    _globals['_BACKUPINFO'].fields_by_name['source_backup']._serialized_options = b'\xe0A\x03'
    _globals['_RESTORESOURCETYPE']._serialized_start = 4979
    _globals['_RESTORESOURCETYPE']._serialized_end = 5047
    _globals['_RESTOREINFO']._serialized_start = 255
    _globals['_RESTOREINFO']._serialized_end = 410
    _globals['_CHANGESTREAMCONFIG']._serialized_start = 412
    _globals['_CHANGESTREAMCONFIG']._serialized_end = 485
    _globals['_TABLE']._serialized_start = 488
    _globals['_TABLE']._serialized_end = 1982
    _globals['_TABLE_CLUSTERSTATE']._serialized_start = 1012
    _globals['_TABLE_CLUSTERSTATE']._serialized_end = 1338
    _globals['_TABLE_CLUSTERSTATE_REPLICATIONSTATE']._serialized_start = 1196
    _globals['_TABLE_CLUSTERSTATE_REPLICATIONSTATE']._serialized_end = 1338
    _globals['_TABLE_AUTOMATEDBACKUPPOLICY']._serialized_start = 1341
    _globals['_TABLE_AUTOMATEDBACKUPPOLICY']._serialized_end = 1473
    _globals['_TABLE_CLUSTERSTATESENTRY']._serialized_start = 1475
    _globals['_TABLE_CLUSTERSTATESENTRY']._serialized_end = 1573
    _globals['_TABLE_COLUMNFAMILIESENTRY']._serialized_start = 1575
    _globals['_TABLE_COLUMNFAMILIESENTRY']._serialized_end = 1668
    _globals['_TABLE_TIMESTAMPGRANULARITY']._serialized_start = 1670
    _globals['_TABLE_TIMESTAMPGRANULARITY']._serialized_end = 1743
    _globals['_TABLE_VIEW']._serialized_start = 1745
    _globals['_TABLE_VIEW']._serialized_end = 1858
    _globals['_AUTHORIZEDVIEW']._serialized_start = 1985
    _globals['_AUTHORIZEDVIEW']._serialized_end = 2724
    _globals['_AUTHORIZEDVIEW_FAMILYSUBSETS']._serialized_start = 2141
    _globals['_AUTHORIZEDVIEW_FAMILYSUBSETS']._serialized_end = 2204
    _globals['_AUTHORIZEDVIEW_SUBSETVIEW']._serialized_start = 2207
    _globals['_AUTHORIZEDVIEW_SUBSETVIEW']._serialized_end = 2447
    _globals['_AUTHORIZEDVIEW_SUBSETVIEW_FAMILYSUBSETSENTRY']._serialized_start = 2339
    _globals['_AUTHORIZEDVIEW_SUBSETVIEW_FAMILYSUBSETSENTRY']._serialized_end = 2447
    _globals['_AUTHORIZEDVIEW_RESPONSEVIEW']._serialized_start = 2449
    _globals['_AUTHORIZEDVIEW_RESPONSEVIEW']._serialized_end = 2530
    _globals['_COLUMNFAMILY']._serialized_start = 2726
    _globals['_COLUMNFAMILY']._serialized_end = 2843
    _globals['_GCRULE']._serialized_start = 2846
    _globals['_GCRULE']._serialized_end = 3187
    _globals['_GCRULE_INTERSECTION']._serialized_start = 3058
    _globals['_GCRULE_INTERSECTION']._serialized_end = 3121
    _globals['_GCRULE_UNION']._serialized_start = 3123
    _globals['_GCRULE_UNION']._serialized_end = 3179
    _globals['_ENCRYPTIONINFO']._serialized_start = 3190
    _globals['_ENCRYPTIONINFO']._serialized_end = 3535
    _globals['_ENCRYPTIONINFO_ENCRYPTIONTYPE']._serialized_start = 3422
    _globals['_ENCRYPTIONINFO_ENCRYPTIONTYPE']._serialized_end = 3535
    _globals['_SNAPSHOT']._serialized_start = 3538
    _globals['_SNAPSHOT']._serialized_end = 4018
    _globals['_SNAPSHOT_STATE']._serialized_start = 3840
    _globals['_SNAPSHOT_STATE']._serialized_end = 3893
    _globals['_BACKUP']._serialized_start = 4021
    _globals['_BACKUP']._serialized_end = 4782
    _globals['_BACKUP_STATE']._serialized_start = 4542
    _globals['_BACKUP_STATE']._serialized_end = 4597
    _globals['_BACKUP_BACKUPTYPE']._serialized_start = 4599
    _globals['_BACKUP_BACKUPTYPE']._serialized_end = 4663
    _globals['_BACKUPINFO']._serialized_start = 4785
    _globals['_BACKUPINFO']._serialized_end = 4977