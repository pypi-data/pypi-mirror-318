"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/analytics/cloud/bigquery_export_platform_log.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/analytics/cloud/bigquery_export_platform_log.proto\x12\x16google.analytics.cloud"\xcd\x01\n\x0fExportStatusLog\x12\x13\n\x0bexport_date\x18\x01 \x01(\t\x12>\n\x06status\x18\x02 \x01(\x0e2..google.analytics.cloud.ExportStatusLog.Status\x12\x13\n\x0bevent_count\x18\x03 \x01(\x03\x12\x0f\n\x07message\x18\x04 \x01(\t"?\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08COMPLETE\x10\x01\x12\x0e\n\nINCOMPLETE\x10\x02\x12\n\n\x06FAILED\x10\x03BVZ;google.golang.org/genproto/googleapis/analytics/cloud;cloud\xaa\x02\x16Google.Analytics.Cloudb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.analytics.cloud.bigquery_export_platform_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z;google.golang.org/genproto/googleapis/analytics/cloud;cloud\xaa\x02\x16Google.Analytics.Cloud'
    _globals['_EXPORTSTATUSLOG']._serialized_start = 86
    _globals['_EXPORTSTATUSLOG']._serialized_end = 291
    _globals['_EXPORTSTATUSLOG_STATUS']._serialized_start = 228
    _globals['_EXPORTSTATUSLOG_STATUS']._serialized_end = 291