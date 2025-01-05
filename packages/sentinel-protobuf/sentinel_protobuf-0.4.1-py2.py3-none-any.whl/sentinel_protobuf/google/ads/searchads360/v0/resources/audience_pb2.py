"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/resources/audience.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/searchads360/v0/resources/audience.proto\x12$google.ads.searchads360.v0.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe4\x01\n\x08Audience\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Audience\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x11\n\x04name\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x05 \x01(\t:Z\xeaAW\n$searchads360.googleapis.com/Audience\x12/customers/{customer_id}/audiences/{audience_id}B\x8d\x02\n(com.google.ads.searchads360.v0.resourcesB\rAudienceProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.audience_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\rAudienceProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_AUDIENCE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Audience'
    _globals['_AUDIENCE'].fields_by_name['id']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCE'].fields_by_name['name']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCE']._loaded_options = None
    _globals['_AUDIENCE']._serialized_options = b'\xeaAW\n$searchads360.googleapis.com/Audience\x12/customers/{customer_id}/audiences/{audience_id}'
    _globals['_AUDIENCE']._serialized_start = 154
    _globals['_AUDIENCE']._serialized_end = 382