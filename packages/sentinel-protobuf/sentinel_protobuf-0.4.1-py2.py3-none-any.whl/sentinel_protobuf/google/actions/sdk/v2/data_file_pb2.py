"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/data_file.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/actions/sdk/v2/data_file.proto\x12\x15google.actions.sdk.v2"@\n\tDataFiles\x123\n\ndata_files\x18\x01 \x03(\x0b2\x1f.google.actions.sdk.v2.DataFile"D\n\x08DataFile\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x14\n\x0ccontent_type\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0cBf\n\x19com.google.actions.sdk.v2B\rDataFileProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.data_file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\rDataFileProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_DATAFILES']._serialized_start = 64
    _globals['_DATAFILES']._serialized_end = 128
    _globals['_DATAFILE']._serialized_start = 130
    _globals['_DATAFILE']._serialized_end = 198