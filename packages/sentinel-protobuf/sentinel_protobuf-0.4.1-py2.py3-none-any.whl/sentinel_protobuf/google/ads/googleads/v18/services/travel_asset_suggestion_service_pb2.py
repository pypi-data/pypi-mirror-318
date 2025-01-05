"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/travel_asset_suggestion_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v18.enums import call_to_action_type_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_call__to__action__type__pb2
from ......google.ads.googleads.v18.enums import hotel_asset_suggestion_status_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_hotel__asset__suggestion__status__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/ads/googleads/v18/services/travel_asset_suggestion_service.proto\x12!google.ads.googleads.v18.services\x1a5google/ads/googleads/v18/enums/asset_field_type.proto\x1a8google/ads/googleads/v18/enums/call_to_action_type.proto\x1aBgoogle/ads/googleads/v18/enums/hotel_asset_suggestion_status.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"g\n\x1aSuggestTravelAssetsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0flanguage_option\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\tplace_ids\x18\x04 \x03(\t"w\n\x1bSuggestTravelAssetsResponse\x12X\n\x17hotel_asset_suggestions\x18\x01 \x03(\x0b27.google.ads.googleads.v18.services.HotelAssetSuggestion"\xab\x03\n\x14HotelAssetSuggestion\x12\x10\n\x08place_id\x18\x01 \x01(\t\x12\x11\n\tfinal_url\x18\x02 \x01(\t\x12\x12\n\nhotel_name\x18\x03 \x01(\t\x12]\n\x0ecall_to_action\x18\x04 \x01(\x0e2E.google.ads.googleads.v18.enums.CallToActionTypeEnum.CallToActionType\x12F\n\x0btext_assets\x18\x05 \x03(\x0b21.google.ads.googleads.v18.services.HotelTextAsset\x12H\n\x0cimage_assets\x18\x06 \x03(\x0b22.google.ads.googleads.v18.services.HotelImageAsset\x12i\n\x06status\x18\x07 \x01(\x0e2Y.google.ads.googleads.v18.enums.HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus"{\n\x0eHotelTextAsset\x12\x0c\n\x04text\x18\x01 \x01(\t\x12[\n\x10asset_field_type\x18\x02 \x01(\x0e2A.google.ads.googleads.v18.enums.AssetFieldTypeEnum.AssetFieldType"{\n\x0fHotelImageAsset\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12[\n\x10asset_field_type\x18\x02 \x01(\x0e2A.google.ads.googleads.v18.enums.AssetFieldTypeEnum.AssetFieldType2\xd9\x02\n\x1cTravelAssetSuggestionService\x12\xf1\x01\n\x13SuggestTravelAssets\x12=.google.ads.googleads.v18.services.SuggestTravelAssetsRequest\x1a>.google.ads.googleads.v18.services.SuggestTravelAssetsResponse"[\xdaA\x1bcustomer_id,language_option\x82\xd3\xe4\x93\x027"2/v18/customers/{customer_id=*}:suggestTravelAssets:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8d\x02\n%com.google.ads.googleads.v18.servicesB!TravelAssetSuggestionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.travel_asset_suggestion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB!TravelAssetSuggestionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_SUGGESTTRAVELASSETSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_SUGGESTTRAVELASSETSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTTRAVELASSETSREQUEST'].fields_by_name['language_option']._loaded_options = None
    _globals['_SUGGESTTRAVELASSETSREQUEST'].fields_by_name['language_option']._serialized_options = b'\xe0A\x02'
    _globals['_TRAVELASSETSUGGESTIONSERVICE']._loaded_options = None
    _globals['_TRAVELASSETSUGGESTIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_TRAVELASSETSUGGESTIONSERVICE'].methods_by_name['SuggestTravelAssets']._loaded_options = None
    _globals['_TRAVELASSETSUGGESTIONSERVICE'].methods_by_name['SuggestTravelAssets']._serialized_options = b'\xdaA\x1bcustomer_id,language_option\x82\xd3\xe4\x93\x027"2/v18/customers/{customer_id=*}:suggestTravelAssets:\x01*'
    _globals['_SUGGESTTRAVELASSETSREQUEST']._serialized_start = 379
    _globals['_SUGGESTTRAVELASSETSREQUEST']._serialized_end = 482
    _globals['_SUGGESTTRAVELASSETSRESPONSE']._serialized_start = 484
    _globals['_SUGGESTTRAVELASSETSRESPONSE']._serialized_end = 603
    _globals['_HOTELASSETSUGGESTION']._serialized_start = 606
    _globals['_HOTELASSETSUGGESTION']._serialized_end = 1033
    _globals['_HOTELTEXTASSET']._serialized_start = 1035
    _globals['_HOTELTEXTASSET']._serialized_end = 1158
    _globals['_HOTELIMAGEASSET']._serialized_start = 1160
    _globals['_HOTELIMAGEASSET']._serialized_end = 1283
    _globals['_TRAVELASSETSUGGESTIONSERVICE']._serialized_start = 1286
    _globals['_TRAVELASSETSUGGESTIONSERVICE']._serialized_end = 1631