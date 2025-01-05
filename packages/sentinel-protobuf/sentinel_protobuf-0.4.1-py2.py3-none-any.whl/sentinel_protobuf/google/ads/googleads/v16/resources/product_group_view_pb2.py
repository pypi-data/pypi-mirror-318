"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/product_group_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v16/resources/product_group_view.proto\x12"google.ads.googleads.v16.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd3\x01\n\x10ProductGroupView\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0A\x03\xfaA+\n)googleads.googleapis.com/ProductGroupView:u\xeaAr\n)googleads.googleapis.com/ProductGroupView\x12Ecustomers/{customer_id}/productGroupViews/{adgroup_id}~{criterion_id}B\x87\x02\n&com.google.ads.googleads.v16.resourcesB\x15ProductGroupViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.product_group_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB\x15ProductGroupViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_PRODUCTGROUPVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_PRODUCTGROUPVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA+\n)googleads.googleapis.com/ProductGroupView'
    _globals['_PRODUCTGROUPVIEW']._loaded_options = None
    _globals['_PRODUCTGROUPVIEW']._serialized_options = b'\xeaAr\n)googleads.googleapis.com/ProductGroupView\x12Ecustomers/{customer_id}/productGroupViews/{adgroup_id}~{criterion_id}'
    _globals['_PRODUCTGROUPVIEW']._serialized_start = 160
    _globals['_PRODUCTGROUPVIEW']._serialized_end = 371