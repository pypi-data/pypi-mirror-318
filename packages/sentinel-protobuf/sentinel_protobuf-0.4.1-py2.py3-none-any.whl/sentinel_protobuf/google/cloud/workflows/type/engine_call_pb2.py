"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/workflows/type/engine_call.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/workflows/type/engine_call.proto\x12\x1bgoogle.cloud.workflows.type\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9c\t\n\rEngineCallLog\x12\x14\n\x0cexecution_id\x18\x01 \x01(\t\x121\n\ractivity_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12?\n\x05state\x18\x03 \x01(\x0e20.google.cloud.workflows.type.EngineCallLog.State\x12\x0c\n\x04step\x18\x04 \x01(\t\x12\x0e\n\x06callee\x18\x05 \x01(\t\x12A\n\x05begun\x18\x06 \x01(\x0b20.google.cloud.workflows.type.EngineCallLog.BegunH\x00\x12I\n\tsucceeded\x18\x07 \x01(\x0b24.google.cloud.workflows.type.EngineCallLog.SucceededH\x00\x12V\n\x10exception_raised\x18\x08 \x01(\x0b2:.google.cloud.workflows.type.EngineCallLog.ExceptionRaisedH\x00\x12X\n\x11exception_handled\x18\t \x01(\x0b2;.google.cloud.workflows.type.EngineCallLog.ExceptionHandledH\x00\x1a\x1b\n\x07CallArg\x12\x10\n\x08argument\x18\x01 \x01(\t\x1a\xe8\x01\n\x05Begun\x12@\n\x04args\x18\x01 \x03(\x0b22.google.cloud.workflows.type.EngineCallLog.CallArg\x12S\n\nnamed_args\x18\x02 \x03(\x0b2?.google.cloud.workflows.type.EngineCallLog.Begun.NamedArgsEntry\x1aH\n\x0eNamedArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01\x1aR\n\tSucceeded\x123\n\x0fcall_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08response\x18\x02 \x01(\t\x1ai\n\x0fExceptionRaised\x123\n\x0fcall_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\texception\x18\x02 \x01(\t\x12\x0e\n\x06origin\x18\x03 \x01(\t\x1aj\n\x10ExceptionHandled\x123\n\x0fcall_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\texception\x18\x02 \x01(\t\x12\x0e\n\x06origin\x18\x03 \x01(\t"e\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05BEGUN\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\x14\n\x10EXCEPTION_RAISED\x10\x03\x12\x15\n\x11EXCEPTION_HANDLED\x10\x04B\t\n\x07detailsBf\n\x1fcom.google.cloud.workflows.typeB\x0fEngineCallProtoP\x01Z0cloud.google.com/go/workflows/type/typepb;typepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.workflows.type.engine_call_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.workflows.typeB\x0fEngineCallProtoP\x01Z0cloud.google.com/go/workflows/type/typepb;typepb'
    _globals['_ENGINECALLLOG_BEGUN_NAMEDARGSENTRY']._loaded_options = None
    _globals['_ENGINECALLLOG_BEGUN_NAMEDARGSENTRY']._serialized_options = b'8\x01'
    _globals['_ENGINECALLLOG']._serialized_start = 142
    _globals['_ENGINECALLLOG']._serialized_end = 1322
    _globals['_ENGINECALLLOG_CALLARG']._serialized_start = 647
    _globals['_ENGINECALLLOG_CALLARG']._serialized_end = 674
    _globals['_ENGINECALLLOG_BEGUN']._serialized_start = 677
    _globals['_ENGINECALLLOG_BEGUN']._serialized_end = 909
    _globals['_ENGINECALLLOG_BEGUN_NAMEDARGSENTRY']._serialized_start = 837
    _globals['_ENGINECALLLOG_BEGUN_NAMEDARGSENTRY']._serialized_end = 909
    _globals['_ENGINECALLLOG_SUCCEEDED']._serialized_start = 911
    _globals['_ENGINECALLLOG_SUCCEEDED']._serialized_end = 993
    _globals['_ENGINECALLLOG_EXCEPTIONRAISED']._serialized_start = 995
    _globals['_ENGINECALLLOG_EXCEPTIONRAISED']._serialized_end = 1100
    _globals['_ENGINECALLLOG_EXCEPTIONHANDLED']._serialized_start = 1102
    _globals['_ENGINECALLLOG_EXCEPTIONHANDLED']._serialized_end = 1208
    _globals['_ENGINECALLLOG_STATE']._serialized_start = 1210
    _globals['_ENGINECALLLOG_STATE']._serialized_end = 1311