"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/backup_disaster_recovery.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/securitycenter/v1/backup_disaster_recovery.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x86\x02\n\x16BackupDisasterRecovery\x12\x17\n\x0fbackup_template\x18\x01 \x01(\t\x12\x10\n\x08policies\x18\x02 \x03(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x14\n\x0capplications\x18\x04 \x03(\t\x12\x14\n\x0cstorage_pool\x18\x05 \x01(\t\x12\x16\n\x0epolicy_options\x18\x06 \x03(\t\x12\x0f\n\x07profile\x18\x07 \x01(\t\x12\x11\n\tappliance\x18\x08 \x01(\t\x12\x13\n\x0bbackup_type\x18\t \x01(\t\x126\n\x12backup_create_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\xf5\x01\n"com.google.cloud.securitycenter.v1B\x1bBackupDisasterRecoveryProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.backup_disaster_recovery_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x1bBackupDisasterRecoveryProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_BACKUPDISASTERRECOVERY']._serialized_start = 131
    _globals['_BACKUPDISASTERRECOVERY']._serialized_end = 393