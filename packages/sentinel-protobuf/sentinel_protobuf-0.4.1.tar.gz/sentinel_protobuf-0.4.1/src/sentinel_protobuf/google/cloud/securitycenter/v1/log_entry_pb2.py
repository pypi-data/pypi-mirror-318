"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/log_entry.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/securitycenter/v1/log_entry.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/protobuf/timestamp.proto"i\n\x08LogEntry\x12P\n\x13cloud_logging_entry\x18\x01 \x01(\x0b21.google.cloud.securitycenter.v1.CloudLoggingEntryH\x00B\x0b\n\tlog_entry"\x81\x01\n\x11CloudLoggingEntry\x12\x11\n\tinsert_id\x18\x01 \x01(\t\x12\x0e\n\x06log_id\x18\x02 \x01(\t\x12\x1a\n\x12resource_container\x18\x03 \x01(\t\x12-\n\ttimestamp\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\xe7\x01\n"com.google.cloud.securitycenter.v1B\rLogEntryProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.log_entry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\rLogEntryProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_LOGENTRY']._serialized_start = 115
    _globals['_LOGENTRY']._serialized_end = 220
    _globals['_CLOUDLOGGINGENTRY']._serialized_start = 223
    _globals['_CLOUDLOGGINGENTRY']._serialized_end = 352