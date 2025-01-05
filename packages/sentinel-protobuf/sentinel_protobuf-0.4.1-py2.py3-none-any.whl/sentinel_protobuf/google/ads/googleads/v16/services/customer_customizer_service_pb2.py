"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/services/customer_customizer_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v16.resources import customer_customizer_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_resources_dot_customer__customizer__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v16/services/customer_customizer_service.proto\x12!google.ads.googleads.v16.services\x1a:google/ads/googleads/v16/enums/response_content_type.proto\x1a<google/ads/googleads/v16/resources/customer_customizer.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xb1\x02\n MutateCustomerCustomizersRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12W\n\noperations\x18\x02 \x03(\x0b2>.google.ads.googleads.v16.services.CustomerCustomizerOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v16.enums.ResponseContentTypeEnum.ResponseContentType"\xb8\x01\n\x1bCustomerCustomizerOperation\x12H\n\x06create\x18\x01 \x01(\x0b26.google.ads.googleads.v16.resources.CustomerCustomizerH\x00\x12B\n\x06remove\x18\x02 \x01(\tB0\xfaA-\n+googleads.googleapis.com/CustomerCustomizerH\x00B\x0b\n\toperation"\xaa\x01\n!MutateCustomerCustomizersResponse\x12R\n\x07results\x18\x01 \x03(\x0b2A.google.ads.googleads.v16.services.MutateCustomerCustomizerResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\xbe\x01\n\x1eMutateCustomerCustomizerResult\x12G\n\rresource_name\x18\x01 \x01(\tB0\xfaA-\n+googleads.googleapis.com/CustomerCustomizer\x12S\n\x13customer_customizer\x18\x02 \x01(\x0b26.google.ads.googleads.v16.resources.CustomerCustomizer2\xea\x02\n\x19CustomerCustomizerService\x12\x85\x02\n\x19MutateCustomerCustomizers\x12C.google.ads.googleads.v16.services.MutateCustomerCustomizersRequest\x1aD.google.ads.googleads.v16.services.MutateCustomerCustomizersResponse"]\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02>"9/v16/customers/{customer_id=*}/CustomerCustomizers:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8a\x02\n%com.google.ads.googleads.v16.servicesB\x1eCustomerCustomizerServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v16/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V16.Services\xca\x02!Google\\Ads\\GoogleAds\\V16\\Services\xea\x02%Google::Ads::GoogleAds::V16::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.services.customer_customizer_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v16.servicesB\x1eCustomerCustomizerServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v16/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V16.Services\xca\x02!Google\\Ads\\GoogleAds\\V16\\Services\xea\x02%Google::Ads::GoogleAds::V16::Services'
    _globals['_MUTATECUSTOMERCUSTOMIZERSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMERCUSTOMIZERSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMERCUSTOMIZERSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECUSTOMERCUSTOMIZERSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMERCUSTOMIZEROPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CUSTOMERCUSTOMIZEROPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA-\n+googleads.googleapis.com/CustomerCustomizer'
    _globals['_MUTATECUSTOMERCUSTOMIZERRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMERCUSTOMIZERRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA-\n+googleads.googleapis.com/CustomerCustomizer'
    _globals['_CUSTOMERCUSTOMIZERSERVICE']._loaded_options = None
    _globals['_CUSTOMERCUSTOMIZERSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMERCUSTOMIZERSERVICE'].methods_by_name['MutateCustomerCustomizers']._loaded_options = None
    _globals['_CUSTOMERCUSTOMIZERSERVICE'].methods_by_name['MutateCustomerCustomizers']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02>"9/v16/customers/{customer_id=*}/CustomerCustomizers:mutate:\x01*'
    _globals['_MUTATECUSTOMERCUSTOMIZERSREQUEST']._serialized_start = 369
    _globals['_MUTATECUSTOMERCUSTOMIZERSREQUEST']._serialized_end = 674
    _globals['_CUSTOMERCUSTOMIZEROPERATION']._serialized_start = 677
    _globals['_CUSTOMERCUSTOMIZEROPERATION']._serialized_end = 861
    _globals['_MUTATECUSTOMERCUSTOMIZERSRESPONSE']._serialized_start = 864
    _globals['_MUTATECUSTOMERCUSTOMIZERSRESPONSE']._serialized_end = 1034
    _globals['_MUTATECUSTOMERCUSTOMIZERRESULT']._serialized_start = 1037
    _globals['_MUTATECUSTOMERCUSTOMIZERRESULT']._serialized_end = 1227
    _globals['_CUSTOMERCUSTOMIZERSERVICE']._serialized_start = 1230
    _globals['_CUSTOMERCUSTOMIZERSERVICE']._serialized_end = 1592