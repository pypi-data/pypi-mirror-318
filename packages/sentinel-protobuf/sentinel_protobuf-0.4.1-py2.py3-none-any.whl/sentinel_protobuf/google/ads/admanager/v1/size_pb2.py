"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/size.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import size_type_enum_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_size__type__enum__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/ads/admanager/v1/size.proto\x12\x17google.ads.admanager.v1\x1a,google/ads/admanager/v1/size_type_enum.proto\x1a\x1fgoogle/api/field_behavior.proto"w\n\x04Size\x12\x12\n\x05width\x18\x01 \x01(\x05B\x03\xe0A\x02\x12\x13\n\x06height\x18\x02 \x01(\x05B\x03\xe0A\x02\x12F\n\tsize_type\x18\x03 \x01(\x0e2..google.ads.admanager.v1.SizeTypeEnum.SizeTypeB\x03\xe0A\x02B\xbd\x01\n\x1bcom.google.ads.admanager.v1B\tSizeProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.size_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\tSizeProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_SIZE'].fields_by_name['width']._loaded_options = None
    _globals['_SIZE'].fields_by_name['width']._serialized_options = b'\xe0A\x02'
    _globals['_SIZE'].fields_by_name['height']._loaded_options = None
    _globals['_SIZE'].fields_by_name['height']._serialized_options = b'\xe0A\x02'
    _globals['_SIZE'].fields_by_name['size_type']._loaded_options = None
    _globals['_SIZE'].fields_by_name['size_type']._serialized_options = b'\xe0A\x02'
    _globals['_SIZE']._serialized_start = 142
    _globals['_SIZE']._serialized_end = 261