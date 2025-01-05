"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/workflows/type/executions_system.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/workflows/type/executions_system.proto\x12\x1bgoogle.cloud.workflows.type\x1a\x1fgoogle/protobuf/timestamp.proto"\xc8\x04\n\x13ExecutionsSystemLog\x12\x0f\n\x07message\x18\x01 \x01(\t\x121\n\ractivity_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12E\n\x05state\x18\x03 \x01(\x0e26.google.cloud.workflows.type.ExecutionsSystemLog.State\x12G\n\x05start\x18\x04 \x01(\x0b26.google.cloud.workflows.type.ExecutionsSystemLog.StartH\x00\x12K\n\x07success\x18\x05 \x01(\x0b28.google.cloud.workflows.type.ExecutionsSystemLog.SuccessH\x00\x12K\n\x07failure\x18\x06 \x01(\x0b28.google.cloud.workflows.type.ExecutionsSystemLog.FailureH\x00\x1a\x19\n\x05Start\x12\x10\n\x08argument\x18\x02 \x01(\t\x1a\x19\n\x07Success\x12\x0e\n\x06result\x18\x02 \x01(\t\x1a,\n\x07Failure\x12\x11\n\texception\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06FAILED\x10\x03\x12\r\n\tCANCELLED\x10\x04B\t\n\x07detailsB2Z0cloud.google.com/go/workflows/type/typepb;typepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.workflows.type.executions_system_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z0cloud.google.com/go/workflows/type/typepb;typepb'
    _globals['_EXECUTIONSSYSTEMLOG']._serialized_start = 118
    _globals['_EXECUTIONSSYSTEMLOG']._serialized_end = 702
    _globals['_EXECUTIONSSYSTEMLOG_START']._serialized_start = 507
    _globals['_EXECUTIONSSYSTEMLOG_START']._serialized_end = 532
    _globals['_EXECUTIONSSYSTEMLOG_SUCCESS']._serialized_start = 534
    _globals['_EXECUTIONSSYSTEMLOG_SUCCESS']._serialized_end = 559
    _globals['_EXECUTIONSSYSTEMLOG_FAILURE']._serialized_start = 561
    _globals['_EXECUTIONSSYSTEMLOG_FAILURE']._serialized_end = 605
    _globals['_EXECUTIONSSYSTEMLOG_STATE']._serialized_start = 607
    _globals['_EXECUTIONSSYSTEMLOG_STATE']._serialized_end = 691