"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/upload_metadata.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/devtools/resultstore/v2/upload_metadata.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x19google/api/resource.proto"\xa5\x01\n\x0eUploadMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cresume_token\x18\x02 \x01(\t\x12\x16\n\x0euploader_state\x18\x03 \x01(\x0c:W\xeaAT\n)resultstore.googleapis.com/UploadMetadata\x12\'invocations/{invocation}/uploadMetadataB\x86\x01\n"com.google.devtools.resultstore.v2B\x13UploadMetadataProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.upload_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x13UploadMetadataProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_UPLOADMETADATA']._loaded_options = None
    _globals['_UPLOADMETADATA']._serialized_options = b"\xeaAT\n)resultstore.googleapis.com/UploadMetadata\x12'invocations/{invocation}/uploadMetadata"
    _globals['_UPLOADMETADATA']._serialized_start = 116
    _globals['_UPLOADMETADATA']._serialized_end = 281