"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/metastore/logging/v1/scheduled_backups_log.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/metastore/logging/v1/scheduled_backups_log.proto\x12!google.cloud.metastore.logging.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x82\x03\n\x17ScheduledBackupLogEntry\x12\x11\n\tbackup_id\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12T\n\x05state\x18\x05 \x01(\x0e2@.google.cloud.metastore.logging.v1.ScheduledBackupLogEntry.StateB\x03\xe0A\x03\x12\x19\n\x11backup_size_bytes\x18\x06 \x01(\x03\x12\x17\n\x0fbackup_location\x18\x07 \x01(\t\x12\x0f\n\x07message\x18\x08 \x01(\t"J\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06FAILED\x10\x03B\x80\x01\n!google.cloud.metastore.logging.v1B\x18ScheduledBackupsLogProtoP\x01Z?cloud.google.com/go/metastore/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.metastore.logging.v1.scheduled_backups_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!google.cloud.metastore.logging.v1B\x18ScheduledBackupsLogProtoP\x01Z?cloud.google.com/go/metastore/logging/apiv1/loggingpb;loggingpb'
    _globals['_SCHEDULEDBACKUPLOGENTRY'].fields_by_name['state']._loaded_options = None
    _globals['_SCHEDULEDBACKUPLOGENTRY'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULEDBACKUPLOGENTRY']._serialized_start = 167
    _globals['_SCHEDULEDBACKUPLOGENTRY']._serialized_end = 553
    _globals['_SCHEDULEDBACKUPLOGENTRY_STATE']._serialized_start = 479
    _globals['_SCHEDULEDBACKUPLOGENTRY_STATE']._serialized_end = 553