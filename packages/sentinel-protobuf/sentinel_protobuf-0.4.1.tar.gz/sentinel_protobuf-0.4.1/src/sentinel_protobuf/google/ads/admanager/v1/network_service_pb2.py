"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/network_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import network_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_network__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/ads/admanager/v1/network_service.proto\x12\x17google.ads.admanager.v1\x1a.google/ads/admanager/v1/network_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"K\n\x11GetNetworkRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network"\x15\n\x13ListNetworksRequest"J\n\x14ListNetworksResponse\x122\n\x08networks\x18\x01 \x03(\x0b2 .google.ads.admanager.v1.Network2\xb4\x02\n\x0eNetworkService\x12\x80\x01\n\nGetNetwork\x12*.google.ads.admanager.v1.GetNetworkRequest\x1a .google.ads.admanager.v1.Network"$\xdaA\x04name\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=networks/*}\x12\x81\x01\n\x0cListNetworks\x12,.google.ads.admanager.v1.ListNetworksRequest\x1a-.google.ads.admanager.v1.ListNetworksResponse"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/networks\x1a\x1b\xcaA\x18admanager.googleapis.comB\xc7\x01\n\x1bcom.google.ads.admanager.v1B\x13NetworkServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.network_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x13NetworkServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETNETWORKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNETWORKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_NETWORKSERVICE']._loaded_options = None
    _globals['_NETWORKSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com'
    _globals['_NETWORKSERVICE'].methods_by_name['GetNetwork']._loaded_options = None
    _globals['_NETWORKSERVICE'].methods_by_name['GetNetwork']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=networks/*}'
    _globals['_NETWORKSERVICE'].methods_by_name['ListNetworks']._loaded_options = None
    _globals['_NETWORKSERVICE'].methods_by_name['ListNetworks']._serialized_options = b'\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/networks'
    _globals['_GETNETWORKREQUEST']._serialized_start = 237
    _globals['_GETNETWORKREQUEST']._serialized_end = 312
    _globals['_LISTNETWORKSREQUEST']._serialized_start = 314
    _globals['_LISTNETWORKSREQUEST']._serialized_end = 335
    _globals['_LISTNETWORKSRESPONSE']._serialized_start = 337
    _globals['_LISTNETWORKSRESPONSE']._serialized_end = 411
    _globals['_NETWORKSERVICE']._serialized_start = 414
    _globals['_NETWORKSERVICE']._serialized_end = 722