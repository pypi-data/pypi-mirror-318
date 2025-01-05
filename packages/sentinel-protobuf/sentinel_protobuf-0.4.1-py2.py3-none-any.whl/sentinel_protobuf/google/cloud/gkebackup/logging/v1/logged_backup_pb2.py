"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkebackup/logging/v1/logged_backup.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/gkebackup/logging/v1/logged_backup.proto\x12!google.cloud.gkebackup.logging.v1"\x92\x03\n\x0cLoggedBackup\x12K\n\x06labels\x18\x01 \x03(\x0b2;.google.cloud.gkebackup.logging.v1.LoggedBackup.LabelsEntry\x12\x18\n\x10delete_lock_days\x18\x02 \x01(\x05\x12\x13\n\x0bretain_days\x18\x03 \x01(\x05\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12D\n\x05state\x18\x05 \x01(\x0e25.google.cloud.gkebackup.logging.v1.LoggedBackup.State\x12\x14\n\x0cstate_reason\x18\x06 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"f\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0c\n\x08DELETING\x10\x05B\xe9\x01\n!google.cloud.gkebackup.logging.v1B\x11LoggedBackupProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.logging.v1.logged_backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!google.cloud.gkebackup.logging.v1B\x11LoggedBackupProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1'
    _globals['_LOGGEDBACKUP_LABELSENTRY']._loaded_options = None
    _globals['_LOGGEDBACKUP_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LOGGEDBACKUP']._serialized_start = 93
    _globals['_LOGGEDBACKUP']._serialized_end = 495
    _globals['_LOGGEDBACKUP_LABELSENTRY']._serialized_start = 346
    _globals['_LOGGEDBACKUP_LABELSENTRY']._serialized_end = 391
    _globals['_LOGGEDBACKUP_STATE']._serialized_start = 393
    _globals['_LOGGEDBACKUP_STATE']._serialized_end = 495