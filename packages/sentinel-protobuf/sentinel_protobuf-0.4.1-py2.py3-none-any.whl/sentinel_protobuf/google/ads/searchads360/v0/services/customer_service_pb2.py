"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/services/customer_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/searchads360/v0/services/customer_service.proto\x12#google.ads.searchads360.v0.services\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto" \n\x1eListAccessibleCustomersRequest"9\n\x1fListAccessibleCustomersResponse\x12\x16\n\x0eresource_names\x18\x01 \x03(\t2\xbb\x02\n\x0fCustomerService\x12\xd3\x01\n\x17ListAccessibleCustomers\x12C.google.ads.searchads360.v0.services.ListAccessibleCustomersRequest\x1aD.google.ads.searchads360.v0.services.ListAccessibleCustomersResponse"-\x82\xd3\xe4\x93\x02\'\x12%/v0/customers:listAccessibleCustomers\x1aR\xcaA\x1bsearchads360.googleapis.com\xd2A1https://www.googleapis.com/auth/doubleclicksearchB\x8e\x02\n\'com.google.ads.searchads360.v0.servicesB\x14CustomerServiceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/services;services\xa2\x02\x07GASA360\xaa\x02#Google.Ads.SearchAds360.V0.Services\xca\x02#Google\\Ads\\SearchAds360\\V0\\Services\xea\x02\'Google::Ads::SearchAds360::V0::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.services.customer_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ads.searchads360.v0.servicesB\x14CustomerServiceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/services;services\xa2\x02\x07GASA360\xaa\x02#Google.Ads.SearchAds360.V0.Services\xca\x02#Google\\Ads\\SearchAds360\\V0\\Services\xea\x02'Google::Ads::SearchAds360::V0::Services"
    _globals['_CUSTOMERSERVICE']._loaded_options = None
    _globals['_CUSTOMERSERVICE']._serialized_options = b'\xcaA\x1bsearchads360.googleapis.com\xd2A1https://www.googleapis.com/auth/doubleclicksearch'
    _globals['_CUSTOMERSERVICE'].methods_by_name['ListAccessibleCustomers']._loaded_options = None
    _globals['_CUSTOMERSERVICE'].methods_by_name['ListAccessibleCustomers']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/v0/customers:listAccessibleCustomers"
    _globals['_LISTACCESSIBLECUSTOMERSREQUEST']._serialized_start = 154
    _globals['_LISTACCESSIBLECUSTOMERSREQUEST']._serialized_end = 186
    _globals['_LISTACCESSIBLECUSTOMERSRESPONSE']._serialized_start = 188
    _globals['_LISTACCESSIBLECUSTOMERSRESPONSE']._serialized_end = 245
    _globals['_CUSTOMERSERVICE']._serialized_start = 248
    _globals['_CUSTOMERSERVICE']._serialized_end = 563