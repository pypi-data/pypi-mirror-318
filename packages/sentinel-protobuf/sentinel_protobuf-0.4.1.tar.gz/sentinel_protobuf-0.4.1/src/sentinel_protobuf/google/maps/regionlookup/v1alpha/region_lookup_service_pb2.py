"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/regionlookup/v1alpha/region_lookup_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.maps.regionlookup.v1alpha import region_identifier_pb2 as google_dot_maps_dot_regionlookup_dot_v1alpha_dot_region__identifier__pb2
from .....google.maps.regionlookup.v1alpha import region_match_pb2 as google_dot_maps_dot_regionlookup_dot_v1alpha_dot_region__match__pb2
from .....google.maps.regionlookup.v1alpha import region_search_values_pb2 as google_dot_maps_dot_regionlookup_dot_v1alpha_dot_region__search__values__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/maps/regionlookup/v1alpha/region_lookup_service.proto\x12 google.maps.regionlookup.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a8google/maps/regionlookup/v1alpha/region_identifier.proto\x1a3google/maps/regionlookup/v1alpha/region_match.proto\x1a;google/maps/regionlookup/v1alpha/region_search_values.proto"\x85\x01\n\x13LookupRegionRequest\x12G\n\x0bidentifiers\x18\x01 \x03(\x0b22.google.maps.regionlookup.v1alpha.RegionIdentifier\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"o\n\x14LookupRegionResponse\x12>\n\x07matches\x18\x01 \x03(\x0b2-.google.maps.regionlookup.v1alpha.RegionMatch\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x88\x01\n\x13SearchRegionRequest\x12J\n\rsearch_values\x18\x01 \x03(\x0b23.google.maps.regionlookup.v1alpha.RegionSearchValue\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"o\n\x14SearchRegionResponse\x12>\n\x07matches\x18\x01 \x03(\x0b2-.google.maps.regionlookup.v1alpha.RegionMatch\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xf2\x02\n\x0cRegionLookup\x12\x9f\x01\n\x0cLookupRegion\x125.google.maps.regionlookup.v1alpha.LookupRegionRequest\x1a6.google.maps.regionlookup.v1alpha.LookupRegionResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/v1alpha:lookupRegion:\x01*\x12\x9f\x01\n\x0cSearchRegion\x125.google.maps.regionlookup.v1alpha.SearchRegionRequest\x1a6.google.maps.regionlookup.v1alpha.SearchRegionResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/v1alpha:searchRegion:\x01*\x1a\x1e\xcaA\x1bregionlookup.googleapis.comB\xe4\x01\n$com.google.maps.regionlookup.v1alphaB\x18RegionLookupServiceProtoP\x01ZNcloud.google.com/go/maps/regionlookup/apiv1alpha/regionlookuppb;regionlookuppb\xf8\x01\x01\xa2\x02\x06MRLV1A\xaa\x02 Google.Maps.RegionLookup.V1Alpha\xca\x02 Google\\Maps\\RegionLookup\\V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.regionlookup.v1alpha.region_lookup_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.maps.regionlookup.v1alphaB\x18RegionLookupServiceProtoP\x01ZNcloud.google.com/go/maps/regionlookup/apiv1alpha/regionlookuppb;regionlookuppb\xf8\x01\x01\xa2\x02\x06MRLV1A\xaa\x02 Google.Maps.RegionLookup.V1Alpha\xca\x02 Google\\Maps\\RegionLookup\\V1alpha'
    _globals['_REGIONLOOKUP']._loaded_options = None
    _globals['_REGIONLOOKUP']._serialized_options = b'\xcaA\x1bregionlookup.googleapis.com'
    _globals['_REGIONLOOKUP'].methods_by_name['LookupRegion']._loaded_options = None
    _globals['_REGIONLOOKUP'].methods_by_name['LookupRegion']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/v1alpha:lookupRegion:\x01*'
    _globals['_REGIONLOOKUP'].methods_by_name['SearchRegion']._loaded_options = None
    _globals['_REGIONLOOKUP'].methods_by_name['SearchRegion']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/v1alpha:searchRegion:\x01*'
    _globals['_LOOKUPREGIONREQUEST']._serialized_start = 326
    _globals['_LOOKUPREGIONREQUEST']._serialized_end = 459
    _globals['_LOOKUPREGIONRESPONSE']._serialized_start = 461
    _globals['_LOOKUPREGIONRESPONSE']._serialized_end = 572
    _globals['_SEARCHREGIONREQUEST']._serialized_start = 575
    _globals['_SEARCHREGIONREQUEST']._serialized_end = 711
    _globals['_SEARCHREGIONRESPONSE']._serialized_start = 713
    _globals['_SEARCHREGIONRESPONSE']._serialized_end = 824
    _globals['_REGIONLOOKUP']._serialized_start = 827
    _globals['_REGIONLOOKUP']._serialized_end = 1197