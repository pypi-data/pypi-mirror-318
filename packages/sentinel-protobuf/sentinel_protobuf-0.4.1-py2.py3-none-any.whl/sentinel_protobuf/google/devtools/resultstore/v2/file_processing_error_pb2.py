"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/file_processing_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/devtools/resultstore/v2/file_processing_error.proto\x12\x1egoogle.devtools.resultstore.v2"}\n\x14FileProcessingErrors\x12\x10\n\x08file_uid\x18\x01 \x01(\t\x12S\n\x16file_processing_errors\x18\x03 \x03(\x0b23.google.devtools.resultstore.v2.FileProcessingError"m\n\x13FileProcessingError\x12E\n\x04type\x18\x01 \x01(\x0e27.google.devtools.resultstore.v2.FileProcessingErrorType\x12\x0f\n\x07message\x18\x02 \x01(\t*\xe9\x01\n\x17FileProcessingErrorType\x12*\n&FILE_PROCESSING_ERROR_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12GENERIC_READ_ERROR\x10\x01\x12\x17\n\x13GENERIC_PARSE_ERROR\x10\x02\x12\x12\n\x0eFILE_TOO_LARGE\x10\x03\x12\x14\n\x10OUTPUT_TOO_LARGE\x10\x04\x12\x11\n\rACCESS_DENIED\x10\x05\x12\x15\n\x11DEADLINE_EXCEEDED\x10\x06\x12\r\n\tNOT_FOUND\x10\x07\x12\x0e\n\nFILE_EMPTY\x10\x08B\x8b\x01\n"com.google.devtools.resultstore.v2B\x18FileProcessingErrorProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.file_processing_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x18FileProcessingErrorProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_FILEPROCESSINGERRORTYPE']._serialized_start = 333
    _globals['_FILEPROCESSINGERRORTYPE']._serialized_end = 566
    _globals['_FILEPROCESSINGERRORS']._serialized_start = 94
    _globals['_FILEPROCESSINGERRORS']._serialized_end = 219
    _globals['_FILEPROCESSINGERROR']._serialized_start = 221
    _globals['_FILEPROCESSINGERROR']._serialized_end = 330