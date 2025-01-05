"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/services/custom_audience_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.resources import custom_audience_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_resources_dot_custom__audience__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v17/services/custom_audience_service.proto\x12!google.ads.googleads.v17.services\x1a8google/ads/googleads/v17/resources/custom_audience.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xa4\x01\n\x1cMutateCustomAudiencesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12S\n\noperations\x18\x02 \x03(\x0b2:.google.ads.googleads.v17.services.CustomAudienceOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"\xa3\x02\n\x17CustomAudienceOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12D\n\x06create\x18\x01 \x01(\x0b22.google.ads.googleads.v17.resources.CustomAudienceH\x00\x12D\n\x06update\x18\x02 \x01(\x0b22.google.ads.googleads.v17.resources.CustomAudienceH\x00\x12>\n\x06remove\x18\x03 \x01(\tB,\xfaA)\n\'googleads.googleapis.com/CustomAudienceH\x00B\x0b\n\toperation"o\n\x1dMutateCustomAudiencesResponse\x12N\n\x07results\x18\x01 \x03(\x0b2=.google.ads.googleads.v17.services.MutateCustomAudienceResult"a\n\x1aMutateCustomAudienceResult\x12C\n\rresource_name\x18\x01 \x01(\tB,\xfaA)\n\'googleads.googleapis.com/CustomAudience2\xd6\x02\n\x15CustomAudienceService\x12\xf5\x01\n\x15MutateCustomAudiences\x12?.google.ads.googleads.v17.services.MutateCustomAudiencesRequest\x1a@.google.ads.googleads.v17.services.MutateCustomAudiencesResponse"Y\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02:"5/v17/customers/{customer_id=*}/customAudiences:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x86\x02\n%com.google.ads.googleads.v17.servicesB\x1aCustomAudienceServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.services.custom_audience_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v17.servicesB\x1aCustomAudienceServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Services'
    _globals['_MUTATECUSTOMAUDIENCESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMAUDIENCESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMAUDIENCESREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECUSTOMAUDIENCESREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMAUDIENCEOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CUSTOMAUDIENCEOPERATION'].fields_by_name['remove']._serialized_options = b"\xfaA)\n'googleads.googleapis.com/CustomAudience"
    _globals['_MUTATECUSTOMAUDIENCERESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMAUDIENCERESULT'].fields_by_name['resource_name']._serialized_options = b"\xfaA)\n'googleads.googleapis.com/CustomAudience"
    _globals['_CUSTOMAUDIENCESERVICE']._loaded_options = None
    _globals['_CUSTOMAUDIENCESERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMAUDIENCESERVICE'].methods_by_name['MutateCustomAudiences']._loaded_options = None
    _globals['_CUSTOMAUDIENCESERVICE'].methods_by_name['MutateCustomAudiences']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02:"5/v17/customers/{customer_id=*}/customAudiences:mutate:\x01*'
    _globals['_MUTATECUSTOMAUDIENCESREQUEST']._serialized_start = 310
    _globals['_MUTATECUSTOMAUDIENCESREQUEST']._serialized_end = 474
    _globals['_CUSTOMAUDIENCEOPERATION']._serialized_start = 477
    _globals['_CUSTOMAUDIENCEOPERATION']._serialized_end = 768
    _globals['_MUTATECUSTOMAUDIENCESRESPONSE']._serialized_start = 770
    _globals['_MUTATECUSTOMAUDIENCESRESPONSE']._serialized_end = 881
    _globals['_MUTATECUSTOMAUDIENCERESULT']._serialized_start = 883
    _globals['_MUTATECUSTOMAUDIENCERESULT']._serialized_end = 980
    _globals['_CUSTOMAUDIENCESERVICE']._serialized_start = 983
    _globals['_CUSTOMAUDIENCESERVICE']._serialized_end = 1325