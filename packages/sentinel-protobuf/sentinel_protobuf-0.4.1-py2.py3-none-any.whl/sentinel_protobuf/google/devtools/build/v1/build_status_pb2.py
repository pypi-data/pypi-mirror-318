"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/build/v1/build_status.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/devtools/build/v1/build_status.proto\x12\x18google.devtools.build.v1\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xb5\x03\n\x0bBuildStatus\x12<\n\x06result\x18\x01 \x01(\x0e2,.google.devtools.build.v1.BuildStatus.Result\x12\x1b\n\x13final_invocation_id\x18\x03 \x01(\t\x129\n\x14build_tool_exit_code\x18\x04 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12\x15\n\rerror_message\x18\x05 \x01(\t\x12%\n\x07details\x18\x02 \x01(\x0b2\x14.google.protobuf.Any"\xd1\x01\n\x06Result\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x15\n\x11COMMAND_SUCCEEDED\x10\x01\x12\x12\n\x0eCOMMAND_FAILED\x10\x02\x12\x0e\n\nUSER_ERROR\x10\x03\x12\x10\n\x0cSYSTEM_ERROR\x10\x04\x12\x16\n\x12RESOURCE_EXHAUSTED\x10\x05\x12 \n\x1cINVOCATION_DEADLINE_EXCEEDED\x10\x06\x12\x1d\n\x19REQUEST_DEADLINE_EXCEEDED\x10\x08\x12\r\n\tCANCELLED\x10\x07B\x8c\x01\n\x1ccom.google.devtools.build.v1B\x10BuildStatusProtoP\x01Z=google.golang.org/genproto/googleapis/devtools/build/v1;build\xf8\x01\x01\xca\x02\x15Google\\Cloud\\Build\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.build.v1.build_status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.devtools.build.v1B\x10BuildStatusProtoP\x01Z=google.golang.org/genproto/googleapis/devtools/build/v1;build\xf8\x01\x01\xca\x02\x15Google\\Cloud\\Build\\V1'
    _globals['_BUILDSTATUS']._serialized_start = 133
    _globals['_BUILDSTATUS']._serialized_end = 570
    _globals['_BUILDSTATUS_RESULT']._serialized_start = 361
    _globals['_BUILDSTATUS_RESULT']._serialized_end = 570