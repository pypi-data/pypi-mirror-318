"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/shareable_preview_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v18/services/shareable_preview_service.proto\x12!google.ads.googleads.v18.services\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/rpc/status.proto"\x92\x01\n GenerateShareablePreviewsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12T\n\x12shareable_previews\x18\x02 \x03(\x0b23.google.ads.googleads.v18.services.ShareablePreviewB\x03\xe0A\x02"p\n\x10ShareablePreview\x12\\\n\x16asset_group_identifier\x18\x01 \x01(\x0b27.google.ads.googleads.v18.services.AssetGroupIdentifierB\x03\xe0A\x02"3\n\x14AssetGroupIdentifier\x12\x1b\n\x0easset_group_id\x18\x01 \x01(\x03B\x03\xe0A\x02"r\n!GenerateShareablePreviewsResponse\x12M\n\tresponses\x18\x01 \x03(\x0b2:.google.ads.googleads.v18.services.ShareablePreviewOrError"\xad\x02\n\x17ShareablePreviewOrError\x12W\n\x16asset_group_identifier\x18\x03 \x01(\x0b27.google.ads.googleads.v18.services.AssetGroupIdentifier\x12]\n\x18shareable_preview_result\x18\x01 \x01(\x0b29.google.ads.googleads.v18.services.ShareablePreviewResultH\x00\x123\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusH\x00B%\n#generate_shareable_preview_response"U\n\x16ShareablePreviewResult\x12\x1d\n\x15shareable_preview_url\x18\x01 \x01(\t\x12\x1c\n\x14expiration_date_time\x18\x02 \x01(\t2\xef\x02\n\x17ShareablePreviewService\x12\x8c\x02\n\x19GenerateShareablePreviews\x12C.google.ads.googleads.v18.services.GenerateShareablePreviewsRequest\x1aD.google.ads.googleads.v18.services.GenerateShareablePreviewsResponse"d\xdaA\x1ecustomer_id,shareable_previews\x82\xd3\xe4\x93\x02="8/v18/customers/{customer_id=*}:generateShareablePreviews:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x88\x02\n%com.google.ads.googleads.v18.servicesB\x1cShareablePreviewServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.shareable_preview_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB\x1cShareablePreviewServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_GENERATESHAREABLEPREVIEWSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATESHAREABLEPREVIEWSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATESHAREABLEPREVIEWSREQUEST'].fields_by_name['shareable_previews']._loaded_options = None
    _globals['_GENERATESHAREABLEPREVIEWSREQUEST'].fields_by_name['shareable_previews']._serialized_options = b'\xe0A\x02'
    _globals['_SHAREABLEPREVIEW'].fields_by_name['asset_group_identifier']._loaded_options = None
    _globals['_SHAREABLEPREVIEW'].fields_by_name['asset_group_identifier']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETGROUPIDENTIFIER'].fields_by_name['asset_group_id']._loaded_options = None
    _globals['_ASSETGROUPIDENTIFIER'].fields_by_name['asset_group_id']._serialized_options = b'\xe0A\x02'
    _globals['_SHAREABLEPREVIEWSERVICE']._loaded_options = None
    _globals['_SHAREABLEPREVIEWSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_SHAREABLEPREVIEWSERVICE'].methods_by_name['GenerateShareablePreviews']._loaded_options = None
    _globals['_SHAREABLEPREVIEWSERVICE'].methods_by_name['GenerateShareablePreviews']._serialized_options = b'\xdaA\x1ecustomer_id,shareable_previews\x82\xd3\xe4\x93\x02="8/v18/customers/{customer_id=*}:generateShareablePreviews:\x01*'
    _globals['_GENERATESHAREABLEPREVIEWSREQUEST']._serialized_start = 218
    _globals['_GENERATESHAREABLEPREVIEWSREQUEST']._serialized_end = 364
    _globals['_SHAREABLEPREVIEW']._serialized_start = 366
    _globals['_SHAREABLEPREVIEW']._serialized_end = 478
    _globals['_ASSETGROUPIDENTIFIER']._serialized_start = 480
    _globals['_ASSETGROUPIDENTIFIER']._serialized_end = 531
    _globals['_GENERATESHAREABLEPREVIEWSRESPONSE']._serialized_start = 533
    _globals['_GENERATESHAREABLEPREVIEWSRESPONSE']._serialized_end = 647
    _globals['_SHAREABLEPREVIEWORERROR']._serialized_start = 650
    _globals['_SHAREABLEPREVIEWORERROR']._serialized_end = 951
    _globals['_SHAREABLEPREVIEWRESULT']._serialized_start = 953
    _globals['_SHAREABLEPREVIEWRESULT']._serialized_end = 1038
    _globals['_SHAREABLEPREVIEWSERVICE']._serialized_start = 1041
    _globals['_SHAREABLEPREVIEWSERVICE']._serialized_end = 1408