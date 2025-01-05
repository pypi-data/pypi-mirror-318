"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/download_metadata.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/devtools/resultstore/v2/download_metadata.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xda\x02\n\x10DownloadMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12C\n\rupload_status\x18\x02 \x01(\x0e2,.google.devtools.resultstore.v2.UploadStatus\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x121\n\rfinalize_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x122\n\x0eimmutable_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp:[\xeaAX\n+resultstore.googleapis.com/DownloadMetadata\x12)invocations/{invocation}/downloadMetadataB\x88\x01\n"com.google.devtools.resultstore.v2B\x15DownloadMetadataProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.download_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x15DownloadMetadataProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_DOWNLOADMETADATA']._loaded_options = None
    _globals['_DOWNLOADMETADATA']._serialized_options = b'\xeaAX\n+resultstore.googleapis.com/DownloadMetadata\x12)invocations/{invocation}/downloadMetadata'
    _globals['_DOWNLOADMETADATA']._serialized_start = 196
    _globals['_DOWNLOADMETADATA']._serialized_end = 542