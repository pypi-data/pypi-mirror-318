"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/admanager_error.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/ads/admanager/v1/admanager_error.proto\x12\x17google.ads.admanager.v1\x1a\x19google/protobuf/any.proto"\x96\x01\n\x0eAdManagerError\x12\x12\n\nerror_code\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nfield_path\x18\x03 \x01(\t\x12\x0f\n\x07trigger\x18\x04 \x01(\t\x12\x13\n\x0bstack_trace\x18\x05 \x01(\t\x12%\n\x07details\x18\x06 \x03(\x0b2\x14.google.protobuf.AnyB\xc7\x01\n\x1bcom.google.ads.admanager.v1B\x13AdManagerErrorProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.admanager_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x13AdManagerErrorProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_ADMANAGERERROR']._serialized_start = 102
    _globals['_ADMANAGERERROR']._serialized_end = 252