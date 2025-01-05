"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/resultstore_file_download.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/devtools/resultstore/v2/resultstore_file_download.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto"]\n\x0eGetFileRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x13\n\x0bread_offset\x18\x02 \x01(\x03\x12\x12\n\nread_limit\x18\x03 \x01(\x03\x12\x15\n\rarchive_entry\x18\x04 \x01(\t"\x1f\n\x0fGetFileResponse\x12\x0c\n\x04data\x18\x01 \x01(\x0c"a\n\x12GetFileTailRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x13\n\x0bread_offset\x18\x02 \x01(\x03\x12\x12\n\nread_limit\x18\x03 \x01(\x03\x12\x15\n\rarchive_entry\x18\x04 \x01(\t"#\n\x13GetFileTailResponse\x12\x0c\n\x04data\x18\x01 \x01(\x0c2\x8a\x03\n\x17ResultStoreFileDownload\x12\x86\x01\n\x07GetFile\x12..google.devtools.resultstore.v2.GetFileRequest\x1a/.google.devtools.resultstore.v2.GetFileResponse"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v2/{uri=file/*}0\x01\x12\x95\x01\n\x0bGetFileTail\x122.google.devtools.resultstore.v2.GetFileTailRequest\x1a3.google.devtools.resultstore.v2.GetFileTailResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v2/{uri=file/tail/*}\x1aN\xcaA\x1aresultstore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8f\x01\n"com.google.devtools.resultstore.v2B\x1cResultStoreFileDownloadProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.resultstore_file_download_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x1cResultStoreFileDownloadProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_RESULTSTOREFILEDOWNLOAD']._loaded_options = None
    _globals['_RESULTSTOREFILEDOWNLOAD']._serialized_options = b'\xcaA\x1aresultstore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_RESULTSTOREFILEDOWNLOAD'].methods_by_name['GetFile']._loaded_options = None
    _globals['_RESULTSTOREFILEDOWNLOAD'].methods_by_name['GetFile']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12\x12\x10/v2/{uri=file/*}'
    _globals['_RESULTSTOREFILEDOWNLOAD'].methods_by_name['GetFileTail']._loaded_options = None
    _globals['_RESULTSTOREFILEDOWNLOAD'].methods_by_name['GetFileTail']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/v2/{uri=file/tail/*}'
    _globals['_GETFILEREQUEST']._serialized_start = 153
    _globals['_GETFILEREQUEST']._serialized_end = 246
    _globals['_GETFILERESPONSE']._serialized_start = 248
    _globals['_GETFILERESPONSE']._serialized_end = 279
    _globals['_GETFILETAILREQUEST']._serialized_start = 281
    _globals['_GETFILETAILREQUEST']._serialized_end = 378
    _globals['_GETFILETAILRESPONSE']._serialized_start = 380
    _globals['_GETFILETAILRESPONSE']._serialized_end = 415
    _globals['_RESULTSTOREFILEDOWNLOAD']._serialized_start = 418
    _globals['_RESULTSTOREFILEDOWNLOAD']._serialized_end = 812