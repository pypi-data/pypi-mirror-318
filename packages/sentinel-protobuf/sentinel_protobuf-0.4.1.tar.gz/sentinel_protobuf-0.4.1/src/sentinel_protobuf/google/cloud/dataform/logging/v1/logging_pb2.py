"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataform/logging/v1/logging.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/dataform/logging/v1/logging.proto\x12 google.cloud.dataform.logging.v1\x1a\x1fgoogle/api/field_behavior.proto"\xda\x02\n$WorkflowInvocationCompletionLogEntry\x12#\n\x16workflow_invocation_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12workflow_config_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11release_config_id\x18\x03 \x01(\tB\x03\xe0A\x01\x12q\n\x0eterminal_state\x18\x04 \x01(\x0e2T.google.cloud.dataform.logging.v1.WorkflowInvocationCompletionLogEntry.TerminalStateB\x03\xe0A\x02"Y\n\rTerminalState\x12\x1e\n\x1aTERMINAL_STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\r\n\tCANCELLED\x10\x02\x12\n\n\x06FAILED\x10\x03Bv\n$com.google.cloud.dataform.logging.v1B\x0cLoggingProtoP\x01Z>cloud.google.com/go/dataform/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataform.logging.v1.logging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.dataform.logging.v1B\x0cLoggingProtoP\x01Z>cloud.google.com/go/dataform/logging/apiv1/loggingpb;loggingpb'
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY'].fields_by_name['workflow_invocation_id']._loaded_options = None
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY'].fields_by_name['workflow_invocation_id']._serialized_options = b'\xe0A\x02'
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY'].fields_by_name['workflow_config_id']._loaded_options = None
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY'].fields_by_name['workflow_config_id']._serialized_options = b'\xe0A\x01'
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY'].fields_by_name['release_config_id']._loaded_options = None
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY'].fields_by_name['release_config_id']._serialized_options = b'\xe0A\x01'
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY'].fields_by_name['terminal_state']._loaded_options = None
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY'].fields_by_name['terminal_state']._serialized_options = b'\xe0A\x02'
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY']._serialized_start = 118
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY']._serialized_end = 464
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY_TERMINALSTATE']._serialized_start = 375
    _globals['_WORKFLOWINVOCATIONCOMPLETIONLOGENTRY_TERMINALSTATE']._serialized_end = 464