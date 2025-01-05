"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/customer_sk_ad_network_conversion_value_schema_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.resources import customer_sk_ad_network_conversion_value_schema_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_resources_dot_customer__sk__ad__network__conversion__value__schema__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n^google/ads/googleads/v18/services/customer_sk_ad_network_conversion_value_schema_service.proto\x12!google.ads.googleads.v18.services\x1aWgoogle/ads/googleads/v18/resources/customer_sk_ad_network_conversion_value_schema.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\x91\x01\n1CustomerSkAdNetworkConversionValueSchemaOperation\x12\\\n\x06update\x18\x01 \x01(\x0b2L.google.ads.googleads.v18.resources.CustomerSkAdNetworkConversionValueSchema"\xea\x01\n5MutateCustomerSkAdNetworkConversionValueSchemaRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12g\n\toperation\x18\x02 \x01(\x0b2T.google.ads.googleads.v18.services.CustomerSkAdNetworkConversionValueSchemaOperation\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08\x12\x1c\n\x0fenable_warnings\x18\x04 \x01(\x08B\x03\xe0A\x01"\xa5\x01\n4MutateCustomerSkAdNetworkConversionValueSchemaResult\x12]\n\rresource_name\x18\x01 \x01(\tBF\xfaAC\nAgoogleads.googleapis.com/CustomerSkAdNetworkConversionValueSchema\x12\x0e\n\x06app_id\x18\x02 \x01(\t"\xc6\x01\n6MutateCustomerSkAdNetworkConversionValueSchemaResponse\x12g\n\x06result\x18\x01 \x01(\x0b2W.google.ads.googleads.v18.services.MutateCustomerSkAdNetworkConversionValueSchemaResult\x12#\n\x07warning\x18\x02 \x01(\x0b2\x12.google.rpc.Status2\xbc\x03\n/CustomerSkAdNetworkConversionValueSchemaService\x12\xc1\x02\n.MutateCustomerSkAdNetworkConversionValueSchema\x12X.google.ads.googleads.v18.services.MutateCustomerSkAdNetworkConversionValueSchemaRequest\x1aY.google.ads.googleads.v18.services.MutateCustomerSkAdNetworkConversionValueSchemaResponse"Z\x82\xd3\xe4\x93\x02T"O/v18/customers/{customer_id=*}/customerSkAdNetworkConversionValueSchemas:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\xa0\x02\n%com.google.ads.googleads.v18.servicesB4CustomerSkAdNetworkConversionValueSchemaServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.customer_sk_ad_network_conversion_value_schema_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB4CustomerSkAdNetworkConversionValueSchemaServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMAREQUEST'].fields_by_name['enable_warnings']._loaded_options = None
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMAREQUEST'].fields_by_name['enable_warnings']._serialized_options = b'\xe0A\x01'
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMARESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMARESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaAC\nAgoogleads.googleapis.com/CustomerSkAdNetworkConversionValueSchema'
    _globals['_CUSTOMERSKADNETWORKCONVERSIONVALUESCHEMASERVICE']._loaded_options = None
    _globals['_CUSTOMERSKADNETWORKCONVERSIONVALUESCHEMASERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMERSKADNETWORKCONVERSIONVALUESCHEMASERVICE'].methods_by_name['MutateCustomerSkAdNetworkConversionValueSchema']._loaded_options = None
    _globals['_CUSTOMERSKADNETWORKCONVERSIONVALUESCHEMASERVICE'].methods_by_name['MutateCustomerSkAdNetworkConversionValueSchema']._serialized_options = b'\x82\xd3\xe4\x93\x02T"O/v18/customers/{customer_id=*}/customerSkAdNetworkConversionValueSchemas:mutate:\x01*'
    _globals['_CUSTOMERSKADNETWORKCONVERSIONVALUESCHEMAOPERATION']._serialized_start = 363
    _globals['_CUSTOMERSKADNETWORKCONVERSIONVALUESCHEMAOPERATION']._serialized_end = 508
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMAREQUEST']._serialized_start = 511
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMAREQUEST']._serialized_end = 745
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMARESULT']._serialized_start = 748
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMARESULT']._serialized_end = 913
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMARESPONSE']._serialized_start = 916
    _globals['_MUTATECUSTOMERSKADNETWORKCONVERSIONVALUESCHEMARESPONSE']._serialized_end = 1114
    _globals['_CUSTOMERSKADNETWORKCONVERSIONVALUESCHEMASERVICE']._serialized_start = 1117
    _globals['_CUSTOMERSKADNETWORKCONVERSIONVALUESCHEMASERVICE']._serialized_end = 1561