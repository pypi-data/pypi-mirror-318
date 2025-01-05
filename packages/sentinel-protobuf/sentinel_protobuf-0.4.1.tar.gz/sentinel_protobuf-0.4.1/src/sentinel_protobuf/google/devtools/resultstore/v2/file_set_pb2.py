"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/file_set.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.resultstore.v2 import file_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/devtools/resultstore/v2/file_set.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x19google/api/resource.proto\x1a)google/devtools/resultstore/v2/file.proto"\xa0\x02\n\x07FileSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x126\n\x02id\x18\x02 \x01(\x0b2*.google.devtools.resultstore.v2.FileSet.Id\x12\x11\n\tfile_sets\x18\x03 \x03(\t\x123\n\x05files\x18\x04 \x03(\x0b2$.google.devtools.resultstore.v2.File\x1a0\n\x02Id\x12\x15\n\rinvocation_id\x18\x01 \x01(\t\x12\x13\n\x0bfile_set_id\x18\x02 \x01(\t:U\xeaAR\n"resultstore.googleapis.com/FileSet\x12,invocations/{invocation}/fileSets/{file_set}B\x7f\n"com.google.devtools.resultstore.v2B\x0cFileSetProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.file_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x0cFileSetProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_FILESET']._loaded_options = None
    _globals['_FILESET']._serialized_options = b'\xeaAR\n"resultstore.googleapis.com/FileSet\x12,invocations/{invocation}/fileSets/{file_set}'
    _globals['_FILESET']._serialized_start = 152
    _globals['_FILESET']._serialized_end = 440
    _globals['_FILESET_ID']._serialized_start = 305
    _globals['_FILESET_ID']._serialized_end = 353