"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkebackup/logging/v1/logged_restore.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/gkebackup/logging/v1/logged_restore.proto\x12!google.cloud.gkebackup.logging.v1"\xf6\x02\n\rLoggedRestore\x12\x0e\n\x06backup\x18\x01 \x01(\t\x12L\n\x06labels\x18\x02 \x03(\x0b2<.google.cloud.gkebackup.logging.v1.LoggedRestore.LabelsEntry\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12E\n\x05state\x18\x04 \x01(\x0e26.google.cloud.gkebackup.logging.v1.LoggedRestore.State\x12\x14\n\x0cstate_reason\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"f\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0c\n\x08DELETING\x10\x05B\xea\x01\n!google.cloud.gkebackup.logging.v1B\x12LoggedRestoreProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.logging.v1.logged_restore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!google.cloud.gkebackup.logging.v1B\x12LoggedRestoreProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1'
    _globals['_LOGGEDRESTORE_LABELSENTRY']._loaded_options = None
    _globals['_LOGGEDRESTORE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LOGGEDRESTORE']._serialized_start = 94
    _globals['_LOGGEDRESTORE']._serialized_end = 468
    _globals['_LOGGEDRESTORE_LABELSENTRY']._serialized_start = 319
    _globals['_LOGGEDRESTORE_LABELSENTRY']._serialized_end = 364
    _globals['_LOGGEDRESTORE_STATE']._serialized_start = 366
    _globals['_LOGGEDRESTORE_STATE']._serialized_end = 468