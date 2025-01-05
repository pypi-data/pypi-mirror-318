"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/services/custom_column_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.resources import custom_column_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_resources_dot_custom__column__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/searchads360/v0/services/custom_column_service.proto\x12#google.ads.searchads360.v0.services\x1a8google/ads/searchads360/v0/resources/custom_column.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"a\n\x16GetCustomColumnRequest\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(searchads360.googleapis.com/CustomColumn"4\n\x18ListCustomColumnsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02"g\n\x19ListCustomColumnsResponse\x12J\n\x0ecustom_columns\x18\x01 \x03(\x0b22.google.ads.searchads360.v0.resources.CustomColumn2\x8f\x04\n\x13CustomColumnService\x12\xcb\x01\n\x0fGetCustomColumn\x12;.google.ads.searchads360.v0.services.GetCustomColumnRequest\x1a2.google.ads.searchads360.v0.resources.CustomColumn"G\xdaA\rresource_name\x82\xd3\xe4\x93\x021\x12//v0/{resource_name=customers/*/customColumns/*}\x12\xd5\x01\n\x11ListCustomColumns\x12=.google.ads.searchads360.v0.services.ListCustomColumnsRequest\x1a>.google.ads.searchads360.v0.services.ListCustomColumnsResponse"A\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x02-\x12+/v0/customers/{customer_id=*}/customColumns\x1aR\xcaA\x1bsearchads360.googleapis.com\xd2A1https://www.googleapis.com/auth/doubleclicksearchB\x92\x02\n\'com.google.ads.searchads360.v0.servicesB\x18CustomColumnServiceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/services;services\xa2\x02\x07GASA360\xaa\x02#Google.Ads.SearchAds360.V0.Services\xca\x02#Google\\Ads\\SearchAds360\\V0\\Services\xea\x02\'Google::Ads::SearchAds360::V0::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.services.custom_column_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ads.searchads360.v0.servicesB\x18CustomColumnServiceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/services;services\xa2\x02\x07GASA360\xaa\x02#Google.Ads.SearchAds360.V0.Services\xca\x02#Google\\Ads\\SearchAds360\\V0\\Services\xea\x02'Google::Ads::SearchAds360::V0::Services"
    _globals['_GETCUSTOMCOLUMNREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_GETCUSTOMCOLUMNREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA*\n(searchads360.googleapis.com/CustomColumn'
    _globals['_LISTCUSTOMCOLUMNSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_LISTCUSTOMCOLUMNSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMCOLUMNSERVICE']._loaded_options = None
    _globals['_CUSTOMCOLUMNSERVICE']._serialized_options = b'\xcaA\x1bsearchads360.googleapis.com\xd2A1https://www.googleapis.com/auth/doubleclicksearch'
    _globals['_CUSTOMCOLUMNSERVICE'].methods_by_name['GetCustomColumn']._loaded_options = None
    _globals['_CUSTOMCOLUMNSERVICE'].methods_by_name['GetCustomColumn']._serialized_options = b'\xdaA\rresource_name\x82\xd3\xe4\x93\x021\x12//v0/{resource_name=customers/*/customColumns/*}'
    _globals['_CUSTOMCOLUMNSERVICE'].methods_by_name['ListCustomColumns']._loaded_options = None
    _globals['_CUSTOMCOLUMNSERVICE'].methods_by_name['ListCustomColumns']._serialized_options = b'\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x02-\x12+/v0/customers/{customer_id=*}/customColumns'
    _globals['_GETCUSTOMCOLUMNREQUEST']._serialized_start = 277
    _globals['_GETCUSTOMCOLUMNREQUEST']._serialized_end = 374
    _globals['_LISTCUSTOMCOLUMNSREQUEST']._serialized_start = 376
    _globals['_LISTCUSTOMCOLUMNSREQUEST']._serialized_end = 428
    _globals['_LISTCUSTOMCOLUMNSRESPONSE']._serialized_start = 430
    _globals['_LISTCUSTOMCOLUMNSRESPONSE']._serialized_end = 533
    _globals['_CUSTOMCOLUMNSERVICE']._serialized_start = 536
    _globals['_CUSTOMCOLUMNSERVICE']._serialized_end = 1063