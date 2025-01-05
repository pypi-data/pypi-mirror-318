"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/backupdr/logging/v1/eventlog.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/backupdr/logging/v1/eventlog.proto\x12 google.cloud.backupdr.logging.v1"\xb4\x01\n\x05Event\x12\x12\n\nevent_time\x18\x01 \x01(\t\x12\r\n\x05srcid\x18\x02 \x01(\x03\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x10\n\x08event_id\x18\x04 \x01(\x05\x12\x11\n\tcomponent\x18\x05 \x01(\t\x12\x16\n\x0eappliance_name\x18\x06 \x01(\x03\x12\x10\n\x08app_name\x18\x07 \x01(\t\x12\x10\n\x08app_type\x18\x08 \x01(\t\x12\x10\n\x08job_name\x18\t \x01(\tB@Z>cloud.google.com/go/backupdr/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.backupdr.logging.v1.eventlog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z>cloud.google.com/go/backupdr/logging/apiv1/loggingpb;loggingpb'
    _globals['_EVENT']._serialized_start = 86
    _globals['_EVENT']._serialized_end = 266