"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/clouddebugger/v2/data.proto')
_sym_db = _symbol_database.Default()
from .....google.devtools.source.v1 import source_context_pb2 as google_dot_devtools_dot_source_dot_v1_dot_source__context__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/devtools/clouddebugger/v2/data.proto\x12 google.devtools.clouddebugger.v2\x1a.google/devtools/source/v1/source_context.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"3\n\rFormatMessage\x12\x0e\n\x06format\x18\x01 \x01(\t\x12\x12\n\nparameters\x18\x02 \x03(\t"\xe4\x02\n\rStatusMessage\x12\x10\n\x08is_error\x18\x01 \x01(\x08\x12L\n\trefers_to\x18\x02 \x01(\x0e29.google.devtools.clouddebugger.v2.StatusMessage.Reference\x12D\n\x0bdescription\x18\x03 \x01(\x0b2/.google.devtools.clouddebugger.v2.FormatMessage"\xac\x01\n\tReference\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x1e\n\x1aBREAKPOINT_SOURCE_LOCATION\x10\x03\x12\x18\n\x14BREAKPOINT_CONDITION\x10\x04\x12\x19\n\x15BREAKPOINT_EXPRESSION\x10\x07\x12\x12\n\x0eBREAKPOINT_AGE\x10\x08\x12\x11\n\rVARIABLE_NAME\x10\x05\x12\x12\n\x0eVARIABLE_VALUE\x10\x06"<\n\x0eSourceLocation\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04line\x18\x02 \x01(\x05\x12\x0e\n\x06column\x18\x03 \x01(\x05"\xe9\x01\n\x08Variable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12;\n\x07members\x18\x03 \x03(\x0b2*.google.devtools.clouddebugger.v2.Variable\x124\n\x0fvar_table_index\x18\x04 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12?\n\x06status\x18\x05 \x01(\x0b2/.google.devtools.clouddebugger.v2.StatusMessage"\xdd\x01\n\nStackFrame\x12\x10\n\x08function\x18\x01 \x01(\t\x12B\n\x08location\x18\x02 \x01(\x0b20.google.devtools.clouddebugger.v2.SourceLocation\x12=\n\targuments\x18\x03 \x03(\x0b2*.google.devtools.clouddebugger.v2.Variable\x12:\n\x06locals\x18\x04 \x03(\x0b2*.google.devtools.clouddebugger.v2.Variable"\x97\x07\n\nBreakpoint\x12\n\n\x02id\x18\x01 \x01(\t\x12C\n\x06action\x18\r \x01(\x0e23.google.devtools.clouddebugger.v2.Breakpoint.Action\x12B\n\x08location\x18\x02 \x01(\x0b20.google.devtools.clouddebugger.v2.SourceLocation\x12\x11\n\tcondition\x18\x03 \x01(\t\x12\x13\n\x0bexpressions\x18\x04 \x03(\t\x12\x1a\n\x12log_message_format\x18\x0e \x01(\t\x12H\n\tlog_level\x18\x0f \x01(\x0e25.google.devtools.clouddebugger.v2.Breakpoint.LogLevel\x12\x16\n\x0eis_final_state\x18\x05 \x01(\x08\x12/\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nfinal_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\nuser_email\x18\x10 \x01(\t\x12?\n\x06status\x18\n \x01(\x0b2/.google.devtools.clouddebugger.v2.StatusMessage\x12B\n\x0cstack_frames\x18\x07 \x03(\x0b2,.google.devtools.clouddebugger.v2.StackFrame\x12I\n\x15evaluated_expressions\x18\x08 \x03(\x0b2*.google.devtools.clouddebugger.v2.Variable\x12B\n\x0evariable_table\x18\t \x03(\x0b2*.google.devtools.clouddebugger.v2.Variable\x12H\n\x06labels\x18\x11 \x03(\x0b28.google.devtools.clouddebugger.v2.Breakpoint.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x1e\n\x06Action\x12\x0b\n\x07CAPTURE\x10\x00\x12\x07\n\x03LOG\x10\x01",\n\x08LogLevel\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05ERROR\x10\x02"\xdf\x03\n\x08Debuggee\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x12\n\nuniquifier\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\x13\n\x0bis_inactive\x18\x05 \x01(\x08\x12\x15\n\ragent_version\x18\x06 \x01(\t\x12\x13\n\x0bis_disabled\x18\x07 \x01(\x08\x12?\n\x06status\x18\x08 \x01(\x0b2/.google.devtools.clouddebugger.v2.StatusMessage\x12A\n\x0fsource_contexts\x18\t \x03(\x0b2(.google.devtools.source.v1.SourceContext\x12Q\n\x13ext_source_contexts\x18\r \x03(\x0b20.google.devtools.source.v1.ExtendedSourceContextB\x02\x18\x01\x12F\n\x06labels\x18\x0b \x03(\x0b26.google.devtools.clouddebugger.v2.Debuggee.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\xc4\x01\n$com.google.devtools.clouddebugger.v2B\tDataProtoP\x01Z8cloud.google.com/go/debugger/apiv2/debuggerpb;debuggerpb\xf8\x01\x01\xaa\x02\x18Google.Cloud.Debugger.V2\xca\x02\x18Google\\Cloud\\Debugger\\V2\xea\x02\x1bGoogle::Cloud::Debugger::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.clouddebugger.v2.data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.devtools.clouddebugger.v2B\tDataProtoP\x01Z8cloud.google.com/go/debugger/apiv2/debuggerpb;debuggerpb\xf8\x01\x01\xaa\x02\x18Google.Cloud.Debugger.V2\xca\x02\x18Google\\Cloud\\Debugger\\V2\xea\x02\x1bGoogle::Cloud::Debugger::V2'
    _globals['_BREAKPOINT_LABELSENTRY']._loaded_options = None
    _globals['_BREAKPOINT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DEBUGGEE_LABELSENTRY']._loaded_options = None
    _globals['_DEBUGGEE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DEBUGGEE'].fields_by_name['ext_source_contexts']._loaded_options = None
    _globals['_DEBUGGEE'].fields_by_name['ext_source_contexts']._serialized_options = b'\x18\x01'
    _globals['_FORMATMESSAGE']._serialized_start = 194
    _globals['_FORMATMESSAGE']._serialized_end = 245
    _globals['_STATUSMESSAGE']._serialized_start = 248
    _globals['_STATUSMESSAGE']._serialized_end = 604
    _globals['_STATUSMESSAGE_REFERENCE']._serialized_start = 432
    _globals['_STATUSMESSAGE_REFERENCE']._serialized_end = 604
    _globals['_SOURCELOCATION']._serialized_start = 606
    _globals['_SOURCELOCATION']._serialized_end = 666
    _globals['_VARIABLE']._serialized_start = 669
    _globals['_VARIABLE']._serialized_end = 902
    _globals['_STACKFRAME']._serialized_start = 905
    _globals['_STACKFRAME']._serialized_end = 1126
    _globals['_BREAKPOINT']._serialized_start = 1129
    _globals['_BREAKPOINT']._serialized_end = 2048
    _globals['_BREAKPOINT_LABELSENTRY']._serialized_start = 1925
    _globals['_BREAKPOINT_LABELSENTRY']._serialized_end = 1970
    _globals['_BREAKPOINT_ACTION']._serialized_start = 1972
    _globals['_BREAKPOINT_ACTION']._serialized_end = 2002
    _globals['_BREAKPOINT_LOGLEVEL']._serialized_start = 2004
    _globals['_BREAKPOINT_LOGLEVEL']._serialized_end = 2048
    _globals['_DEBUGGEE']._serialized_start = 2051
    _globals['_DEBUGGEE']._serialized_end = 2530
    _globals['_DEBUGGEE_LABELSENTRY']._serialized_start = 1925
    _globals['_DEBUGGEE_LABELSENTRY']._serialized_end = 1970