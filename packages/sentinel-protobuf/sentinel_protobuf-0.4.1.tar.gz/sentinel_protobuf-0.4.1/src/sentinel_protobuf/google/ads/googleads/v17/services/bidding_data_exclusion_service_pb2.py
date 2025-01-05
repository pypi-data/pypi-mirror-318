"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/services/bidding_data_exclusion_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v17.resources import bidding_data_exclusion_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_resources_dot_bidding__data__exclusion__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/ads/googleads/v17/services/bidding_data_exclusion_service.proto\x12!google.ads.googleads.v17.services\x1a:google/ads/googleads/v17/enums/response_content_type.proto\x1a?google/ads/googleads/v17/resources/bidding_data_exclusion.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xb5\x02\n"MutateBiddingDataExclusionsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12Y\n\noperations\x18\x02 \x03(\x0b2@.google.ads.googleads.v17.services.BiddingDataExclusionOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v17.enums.ResponseContentTypeEnum.ResponseContentType"\xbb\x02\n\x1dBiddingDataExclusionOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12J\n\x06create\x18\x01 \x01(\x0b28.google.ads.googleads.v17.resources.BiddingDataExclusionH\x00\x12J\n\x06update\x18\x02 \x01(\x0b28.google.ads.googleads.v17.resources.BiddingDataExclusionH\x00\x12D\n\x06remove\x18\x03 \x01(\tB2\xfaA/\n-googleads.googleapis.com/BiddingDataExclusionH\x00B\x0b\n\toperation"\xaf\x01\n#MutateBiddingDataExclusionsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12U\n\x07results\x18\x02 \x03(\x0b2D.google.ads.googleads.v17.services.MutateBiddingDataExclusionsResult"\xc8\x01\n!MutateBiddingDataExclusionsResult\x12I\n\rresource_name\x18\x01 \x01(\tB2\xfaA/\n-googleads.googleapis.com/BiddingDataExclusion\x12X\n\x16bidding_data_exclusion\x18\x02 \x01(\x0b28.google.ads.googleads.v17.resources.BiddingDataExclusion2\xf4\x02\n\x1bBiddingDataExclusionService\x12\x8d\x02\n\x1bMutateBiddingDataExclusions\x12E.google.ads.googleads.v17.services.MutateBiddingDataExclusionsRequest\x1aF.google.ads.googleads.v17.services.MutateBiddingDataExclusionsResponse"_\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02@";/v17/customers/{customer_id=*}/biddingDataExclusions:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8c\x02\n%com.google.ads.googleads.v17.servicesB BiddingDataExclusionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.services.bidding_data_exclusion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v17.servicesB BiddingDataExclusionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Services'
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_BIDDINGDATAEXCLUSIONOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSIONOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/BiddingDataExclusion'
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/BiddingDataExclusion'
    _globals['_BIDDINGDATAEXCLUSIONSERVICE']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_BIDDINGDATAEXCLUSIONSERVICE'].methods_by_name['MutateBiddingDataExclusions']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSIONSERVICE'].methods_by_name['MutateBiddingDataExclusions']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02@";/v17/customers/{customer_id=*}/biddingDataExclusions:mutate:\x01*'
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSREQUEST']._serialized_start = 409
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSREQUEST']._serialized_end = 718
    _globals['_BIDDINGDATAEXCLUSIONOPERATION']._serialized_start = 721
    _globals['_BIDDINGDATAEXCLUSIONOPERATION']._serialized_end = 1036
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSRESPONSE']._serialized_start = 1039
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSRESPONSE']._serialized_end = 1214
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSRESULT']._serialized_start = 1217
    _globals['_MUTATEBIDDINGDATAEXCLUSIONSRESULT']._serialized_end = 1417
    _globals['_BIDDINGDATAEXCLUSIONSERVICE']._serialized_start = 1420
    _globals['_BIDDINGDATAEXCLUSIONSERVICE']._serialized_end = 1792