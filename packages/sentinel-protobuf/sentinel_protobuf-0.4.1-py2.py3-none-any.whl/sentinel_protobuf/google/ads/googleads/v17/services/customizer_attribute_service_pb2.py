"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/services/customizer_attribute_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v17.resources import customizer_attribute_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_resources_dot_customizer__attribute__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/ads/googleads/v17/services/customizer_attribute_service.proto\x12!google.ads.googleads.v17.services\x1a:google/ads/googleads/v17/enums/response_content_type.proto\x1a=google/ads/googleads/v17/resources/customizer_attribute.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xb3\x02\n!MutateCustomizerAttributesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12X\n\noperations\x18\x02 \x03(\x0b2?.google.ads.googleads.v17.services.CustomizerAttributeOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v17.enums.ResponseContentTypeEnum.ResponseContentType"\xec\x01\n\x1cCustomizerAttributeOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12I\n\x06create\x18\x01 \x01(\x0b27.google.ads.googleads.v17.resources.CustomizerAttributeH\x00\x12C\n\x06remove\x18\x02 \x01(\tB1\xfaA.\n,googleads.googleapis.com/CustomizerAttributeH\x00B\x0b\n\toperation"\xac\x01\n"MutateCustomizerAttributesResponse\x12S\n\x07results\x18\x01 \x03(\x0b2B.google.ads.googleads.v17.services.MutateCustomizerAttributeResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\xc2\x01\n\x1fMutateCustomizerAttributeResult\x12H\n\rresource_name\x18\x01 \x01(\tB1\xfaA.\n,googleads.googleapis.com/CustomizerAttribute\x12U\n\x14customizer_attribute\x18\x02 \x01(\x0b27.google.ads.googleads.v17.resources.CustomizerAttribute2\xef\x02\n\x1aCustomizerAttributeService\x12\x89\x02\n\x1aMutateCustomizerAttributes\x12D.google.ads.googleads.v17.services.MutateCustomizerAttributesRequest\x1aE.google.ads.googleads.v17.services.MutateCustomizerAttributesResponse"^\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02?":/v17/customers/{customer_id=*}/customizerAttributes:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8b\x02\n%com.google.ads.googleads.v17.servicesB\x1fCustomizerAttributeServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.services.customizer_attribute_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v17.servicesB\x1fCustomizerAttributeServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Services'
    _globals['_MUTATECUSTOMIZERATTRIBUTESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMIZERATTRIBUTESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMIZERATTRIBUTESREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECUSTOMIZERATTRIBUTESREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMIZERATTRIBUTEOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CUSTOMIZERATTRIBUTEOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/CustomizerAttribute'
    _globals['_MUTATECUSTOMIZERATTRIBUTERESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMIZERATTRIBUTERESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/CustomizerAttribute'
    _globals['_CUSTOMIZERATTRIBUTESERVICE']._loaded_options = None
    _globals['_CUSTOMIZERATTRIBUTESERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMIZERATTRIBUTESERVICE'].methods_by_name['MutateCustomizerAttributes']._loaded_options = None
    _globals['_CUSTOMIZERATTRIBUTESERVICE'].methods_by_name['MutateCustomizerAttributes']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02?":/v17/customers/{customer_id=*}/customizerAttributes:mutate:\x01*'
    _globals['_MUTATECUSTOMIZERATTRIBUTESREQUEST']._serialized_start = 405
    _globals['_MUTATECUSTOMIZERATTRIBUTESREQUEST']._serialized_end = 712
    _globals['_CUSTOMIZERATTRIBUTEOPERATION']._serialized_start = 715
    _globals['_CUSTOMIZERATTRIBUTEOPERATION']._serialized_end = 951
    _globals['_MUTATECUSTOMIZERATTRIBUTESRESPONSE']._serialized_start = 954
    _globals['_MUTATECUSTOMIZERATTRIBUTESRESPONSE']._serialized_end = 1126
    _globals['_MUTATECUSTOMIZERATTRIBUTERESULT']._serialized_start = 1129
    _globals['_MUTATECUSTOMIZERATTRIBUTERESULT']._serialized_end = 1323
    _globals['_CUSTOMIZERATTRIBUTESERVICE']._serialized_start = 1326
    _globals['_CUSTOMIZERATTRIBUTESERVICE']._serialized_end = 1693