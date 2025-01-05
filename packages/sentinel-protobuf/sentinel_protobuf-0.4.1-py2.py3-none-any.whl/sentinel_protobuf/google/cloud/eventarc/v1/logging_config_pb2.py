"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/v1/logging_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/eventarc/v1/logging_config.proto\x12\x18google.cloud.eventarc.v1\x1a\x1fgoogle/api/field_behavior.proto"\xf8\x01\n\rLoggingConfig\x12N\n\x0clog_severity\x18\x01 \x01(\x0e23.google.cloud.eventarc.v1.LoggingConfig.LogSeverityB\x03\xe0A\x01"\x96\x01\n\x0bLogSeverity\x12\x1c\n\x18LOG_SEVERITY_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\t\n\x05DEBUG\x10\x02\x12\x08\n\x04INFO\x10\x03\x12\n\n\x06NOTICE\x10\x04\x12\x0b\n\x07WARNING\x10\x05\x12\t\n\x05ERROR\x10\x06\x12\x0c\n\x08CRITICAL\x10\x07\x12\t\n\x05ALERT\x10\x08\x12\r\n\tEMERGENCY\x10\tB\xc2\x01\n\x1ccom.google.cloud.eventarc.v1B\x12LoggingConfigProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.v1.logging_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.eventarc.v1B\x12LoggingConfigProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1'
    _globals['_LOGGINGCONFIG'].fields_by_name['log_severity']._loaded_options = None
    _globals['_LOGGINGCONFIG'].fields_by_name['log_severity']._serialized_options = b'\xe0A\x01'
    _globals['_LOGGINGCONFIG']._serialized_start = 109
    _globals['_LOGGINGCONFIG']._serialized_end = 357
    _globals['_LOGGINGCONFIG_LOGSEVERITY']._serialized_start = 207
    _globals['_LOGGINGCONFIG_LOGSEVERITY']._serialized_end = 357