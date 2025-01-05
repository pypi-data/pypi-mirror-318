"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/stitcher/v1/cdn_keys.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/video/stitcher/v1/cdn_keys.proto\x12\x1egoogle.cloud.video.stitcher.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf5\x02\n\x06CdnKey\x12F\n\x0egoogle_cdn_key\x18\x05 \x01(\x0b2,.google.cloud.video.stitcher.v1.GoogleCdnKeyH\x00\x12F\n\x0eakamai_cdn_key\x18\x06 \x01(\x0b2,.google.cloud.video.stitcher.v1.AkamaiCdnKeyH\x00\x12D\n\rmedia_cdn_key\x18\x08 \x01(\x0b2+.google.cloud.video.stitcher.v1.MediaCdnKeyH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x04 \x01(\t:c\xeaA`\n#videostitcher.googleapis.com/CdnKey\x129projects/{project}/locations/{location}/cdnKeys/{cdn_key}B\x10\n\x0ecdn_key_config":\n\x0cGoogleCdnKey\x12\x18\n\x0bprivate_key\x18\x01 \x01(\x0cB\x03\xe0A\x04\x12\x10\n\x08key_name\x18\x02 \x01(\t"&\n\x0cAkamaiCdnKey\x12\x16\n\ttoken_key\x18\x01 \x01(\x0cB\x03\xe0A\x04"\xba\x01\n\x0bMediaCdnKey\x12\x18\n\x0bprivate_key\x18\x01 \x01(\x0cB\x03\xe0A\x04\x12\x10\n\x08key_name\x18\x02 \x01(\t\x12R\n\x0ctoken_config\x18\x03 \x01(\x0b27.google.cloud.video.stitcher.v1.MediaCdnKey.TokenConfigB\x03\xe0A\x01\x1a+\n\x0bTokenConfig\x12\x1c\n\x0fquery_parameter\x18\x01 \x01(\tB\x03\xe0A\x01Bt\n"com.google.cloud.video.stitcher.v1B\x0cCdnKeysProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.cdn_keys_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\x0cCdnKeysProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_CDNKEY']._loaded_options = None
    _globals['_CDNKEY']._serialized_options = b'\xeaA`\n#videostitcher.googleapis.com/CdnKey\x129projects/{project}/locations/{location}/cdnKeys/{cdn_key}'
    _globals['_GOOGLECDNKEY'].fields_by_name['private_key']._loaded_options = None
    _globals['_GOOGLECDNKEY'].fields_by_name['private_key']._serialized_options = b'\xe0A\x04'
    _globals['_AKAMAICDNKEY'].fields_by_name['token_key']._loaded_options = None
    _globals['_AKAMAICDNKEY'].fields_by_name['token_key']._serialized_options = b'\xe0A\x04'
    _globals['_MEDIACDNKEY_TOKENCONFIG'].fields_by_name['query_parameter']._loaded_options = None
    _globals['_MEDIACDNKEY_TOKENCONFIG'].fields_by_name['query_parameter']._serialized_options = b'\xe0A\x01'
    _globals['_MEDIACDNKEY'].fields_by_name['private_key']._loaded_options = None
    _globals['_MEDIACDNKEY'].fields_by_name['private_key']._serialized_options = b'\xe0A\x04'
    _globals['_MEDIACDNKEY'].fields_by_name['token_config']._loaded_options = None
    _globals['_MEDIACDNKEY'].fields_by_name['token_config']._serialized_options = b'\xe0A\x01'
    _globals['_CDNKEY']._serialized_start = 142
    _globals['_CDNKEY']._serialized_end = 515
    _globals['_GOOGLECDNKEY']._serialized_start = 517
    _globals['_GOOGLECDNKEY']._serialized_end = 575
    _globals['_AKAMAICDNKEY']._serialized_start = 577
    _globals['_AKAMAICDNKEY']._serialized_end = 615
    _globals['_MEDIACDNKEY']._serialized_start = 618
    _globals['_MEDIACDNKEY']._serialized_end = 804
    _globals['_MEDIACDNKEY_TOKENCONFIG']._serialized_start = 761
    _globals['_MEDIACDNKEY_TOKENCONFIG']._serialized_end = 804