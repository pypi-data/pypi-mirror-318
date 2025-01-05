"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/asset_group_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.resources import asset_group_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_resources_dot_asset__group__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v18/services/asset_group_service.proto\x12!google.ads.googleads.v18.services\x1a4google/ads/googleads/v18/resources/asset_group.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\x9c\x01\n\x18MutateAssetGroupsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12O\n\noperations\x18\x02 \x03(\x0b26.google.ads.googleads.v18.services.AssetGroupOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\x93\x02\n\x13AssetGroupOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12@\n\x06create\x18\x01 \x01(\x0b2..google.ads.googleads.v18.resources.AssetGroupH\x00\x12@\n\x06update\x18\x02 \x01(\x0b2..google.ads.googleads.v18.resources.AssetGroupH\x00\x12:\n\x06remove\x18\x03 \x01(\tB(\xfaA%\n#googleads.googleapis.com/AssetGroupH\x00B\x0b\n\toperation"\x9a\x01\n\x19MutateAssetGroupsResponse\x12J\n\x07results\x18\x01 \x03(\x0b29.google.ads.googleads.v18.services.MutateAssetGroupResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"Y\n\x16MutateAssetGroupResult\x12?\n\rresource_name\x18\x01 \x01(\tB(\xfaA%\n#googleads.googleapis.com/AssetGroup2\xc2\x02\n\x11AssetGroupService\x12\xe5\x01\n\x11MutateAssetGroups\x12;.google.ads.googleads.v18.services.MutateAssetGroupsRequest\x1a<.google.ads.googleads.v18.services.MutateAssetGroupsResponse"U\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x026"1/v18/customers/{customer_id=*}/assetGroups:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x82\x02\n%com.google.ads.googleads.v18.servicesB\x16AssetGroupServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.asset_group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB\x16AssetGroupServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_MUTATEASSETGROUPSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEASSETGROUPSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEASSETGROUPSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEASSETGROUPSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETGROUPOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ASSETGROUPOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_MUTATEASSETGROUPRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEASSETGROUPRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_ASSETGROUPSERVICE']._loaded_options = None
    _globals['_ASSETGROUPSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ASSETGROUPSERVICE'].methods_by_name['MutateAssetGroups']._loaded_options = None
    _globals['_ASSETGROUPSERVICE'].methods_by_name['MutateAssetGroups']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x026"1/v18/customers/{customer_id=*}/assetGroups:mutate:\x01*'
    _globals['_MUTATEASSETGROUPSREQUEST']._serialized_start = 327
    _globals['_MUTATEASSETGROUPSREQUEST']._serialized_end = 483
    _globals['_ASSETGROUPOPERATION']._serialized_start = 486
    _globals['_ASSETGROUPOPERATION']._serialized_end = 761
    _globals['_MUTATEASSETGROUPSRESPONSE']._serialized_start = 764
    _globals['_MUTATEASSETGROUPSRESPONSE']._serialized_end = 918
    _globals['_MUTATEASSETGROUPRESULT']._serialized_start = 920
    _globals['_MUTATEASSETGROUPRESULT']._serialized_end = 1009
    _globals['_ASSETGROUPSERVICE']._serialized_start = 1012
    _globals['_ASSETGROUPSERVICE']._serialized_end = 1334