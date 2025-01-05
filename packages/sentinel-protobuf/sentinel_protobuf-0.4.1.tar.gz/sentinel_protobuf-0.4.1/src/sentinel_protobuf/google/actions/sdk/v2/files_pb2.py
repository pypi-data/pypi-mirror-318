"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/files.proto')
_sym_db = _symbol_database.Default()
from .....google.actions.sdk.v2 import config_file_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_config__file__pb2
from .....google.actions.sdk.v2 import data_file_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_data__file__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/actions/sdk/v2/files.proto\x12\x15google.actions.sdk.v2\x1a\'google/actions/sdk/v2/config_file.proto\x1a%google/actions/sdk/v2/data_file.proto"\x88\x01\n\x05Files\x12:\n\x0cconfig_files\x18\x01 \x01(\x0b2".google.actions.sdk.v2.ConfigFilesH\x00\x126\n\ndata_files\x18\x02 \x01(\x0b2 .google.actions.sdk.v2.DataFilesH\x00B\x0b\n\tfile_typeBc\n\x19com.google.actions.sdk.v2B\nFilesProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.files_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\nFilesProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_FILES']._serialized_start = 141
    _globals['_FILES']._serialized_end = 277