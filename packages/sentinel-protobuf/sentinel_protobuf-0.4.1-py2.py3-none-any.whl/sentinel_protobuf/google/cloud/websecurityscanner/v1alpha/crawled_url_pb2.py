"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1alpha/crawled_url.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/websecurityscanner/v1alpha/crawled_url.proto\x12\'google.cloud.websecurityscanner.v1alpha"<\n\nCrawledUrl\x12\x13\n\x0bhttp_method\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04body\x18\x03 \x01(\tB\x9d\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x0fCrawledUrlProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1alpha.crawled_url_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.cloud.websecurityscanner.v1alphaB\x0fCrawledUrlProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpb'
    _globals['_CRAWLEDURL']._serialized_start = 102
    _globals['_CRAWLEDURL']._serialized_end = 162