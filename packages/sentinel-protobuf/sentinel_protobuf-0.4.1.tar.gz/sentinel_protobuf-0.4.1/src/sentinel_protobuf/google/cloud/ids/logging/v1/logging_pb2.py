"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/ids/logging/v1/logging.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/ids/logging/v1/logging.proto\x12\x1bgoogle.cloud.ids.logging.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc9\x05\n\tThreatLog\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tthreat_id\x18\r \x01(\t\x12.\n\nalert_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12G\n\x0ealert_severity\x18\x13 \x01(\x0e2/.google.cloud.ids.logging.v1.ThreatLog.Severity\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x10\n\x08category\x18\x12 \x01(\t\x12\x19\n\x11source_ip_address\x18\x05 \x01(\t\x12\x13\n\x0bsource_port\x18\x06 \x01(\x05\x12\x1e\n\x16destination_ip_address\x18\x07 \x01(\t\x12\x18\n\x10destination_port\x18\x08 \x01(\x05\x12\x13\n\x0bip_protocol\x18\t \x01(\t\x12C\n\tdirection\x18\n \x01(\x0e20.google.cloud.ids.logging.v1.ThreatLog.Direction\x12\x12\n\nsession_id\x18\x0e \x01(\t\x12\x14\n\x0crepeat_count\x18\x0f \x01(\t\x12\x13\n\x0bapplication\x18\x10 \x01(\t\x12\x17\n\x0furi_or_filename\x18\x11 \x01(\t\x12\x0c\n\x04cves\x18\x14 \x03(\t\x12\x0f\n\x07details\x18\x0b \x01(\t\x12\x0f\n\x07network\x18\x0c \x01(\t"d\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x07\n\x03LOW\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x08\n\x04HIGH\x10\x04\x12\x0c\n\x08CRITICAL\x10\x05\x12\x11\n\rINFORMATIONAL\x10\x06"P\n\tDirection\x12\x17\n\x13DIRECTION_UNDEFINED\x10\x00\x12\x14\n\x10CLIENT_TO_SERVER\x10\x01\x12\x14\n\x10SERVER_TO_CLIENT\x10\x02"\xe8\x02\n\nTrafficLog\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0celapsed_time\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x19\n\x11source_ip_address\x18\x04 \x01(\t\x12\x13\n\x0bsource_port\x18\x05 \x01(\x05\x12\x1e\n\x16destination_ip_address\x18\x06 \x01(\t\x12\x18\n\x10destination_port\x18\x07 \x01(\x05\x12\x13\n\x0bip_protocol\x18\x08 \x01(\t\x12\x13\n\x0bapplication\x18\t \x01(\t\x12\x12\n\nsession_id\x18\x0c \x01(\t\x12\x14\n\x0crepeat_count\x18\r \x01(\t\x12\x13\n\x0btotal_bytes\x18\x0e \x01(\x03\x12\x15\n\rtotal_packets\x18\x0f \x01(\x03Bl\n\x1fcom.google.cloud.ids.logging.v1B\x0cLoggingProtoP\x01Z9cloud.google.com/go/ids/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.ids.logging.v1.logging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.ids.logging.v1B\x0cLoggingProtoP\x01Z9cloud.google.com/go/ids/logging/apiv1/loggingpb;loggingpb'
    _globals['_THREATLOG']._serialized_start = 140
    _globals['_THREATLOG']._serialized_end = 853
    _globals['_THREATLOG_SEVERITY']._serialized_start = 671
    _globals['_THREATLOG_SEVERITY']._serialized_end = 771
    _globals['_THREATLOG_DIRECTION']._serialized_start = 773
    _globals['_THREATLOG_DIRECTION']._serialized_end = 853
    _globals['_TRAFFICLOG']._serialized_start = 856
    _globals['_TRAFFICLOG']._serialized_end = 1216