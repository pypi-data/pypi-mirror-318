"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/stitcher/v1/fetch_options.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/video/stitcher/v1/fetch_options.proto\x12\x1egoogle.cloud.video.stitcher.v1"\x8a\x01\n\x0cFetchOptions\x12J\n\x07headers\x18\x01 \x03(\x0b29.google.cloud.video.stitcher.v1.FetchOptions.HeadersEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01By\n"com.google.cloud.video.stitcher.v1B\x11FetchOptionsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.fetch_options_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\x11FetchOptionsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_FETCHOPTIONS_HEADERSENTRY']._loaded_options = None
    _globals['_FETCHOPTIONS_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_FETCHOPTIONS']._serialized_start = 87
    _globals['_FETCHOPTIONS']._serialized_end = 225
    _globals['_FETCHOPTIONS_HEADERSENTRY']._serialized_start = 179
    _globals['_FETCHOPTIONS_HEADERSENTRY']._serialized_end = 225