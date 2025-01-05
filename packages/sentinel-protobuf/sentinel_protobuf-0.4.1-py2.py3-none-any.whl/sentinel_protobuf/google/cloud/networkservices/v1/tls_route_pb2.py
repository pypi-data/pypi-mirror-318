"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networkservices/v1/tls_route.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/networkservices/v1/tls_route.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa2\x07\n\x08TlsRoute\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tself_link\x18\x08 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x12G\n\x05rules\x18\x05 \x03(\x0b23.google.cloud.networkservices.v1.TlsRoute.RouteRuleB\x03\xe0A\x02\x12;\n\x06meshes\x18\x06 \x03(\tB+\xe0A\x01\xfaA%\n#networkservices.googleapis.com/Mesh\x12@\n\x08gateways\x18\x07 \x03(\tB.\xe0A\x01\xfaA(\n&networkservices.googleapis.com/Gateway\x1a\xa3\x01\n\tRouteRule\x12J\n\x07matches\x18\x01 \x03(\x0b24.google.cloud.networkservices.v1.TlsRoute.RouteMatchB\x03\xe0A\x02\x12J\n\x06action\x18\x02 \x01(\x0b25.google.cloud.networkservices.v1.TlsRoute.RouteActionB\x03\xe0A\x02\x1a6\n\nRouteMatch\x12\x15\n\x08sni_host\x18\x01 \x03(\tB\x03\xe0A\x01\x12\x11\n\x04alpn\x18\x02 \x03(\tB\x03\xe0A\x01\x1ad\n\x0bRouteAction\x12U\n\x0cdestinations\x18\x01 \x03(\x0b2:.google.cloud.networkservices.v1.TlsRoute.RouteDestinationB\x03\xe0A\x02\x1al\n\x10RouteDestination\x12C\n\x0cservice_name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%compute.googleapis.com/BackendService\x12\x13\n\x06weight\x18\x02 \x01(\x05B\x03\xe0A\x01:k\xeaAh\n\'networkservices.googleapis.com/TlsRoute\x12=projects/{project}/locations/{location}/tlsRoutes/{tls_route}"~\n\x14ListTlsRoutesRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'networkservices.googleapis.com/TlsRoute\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"o\n\x15ListTlsRoutesResponse\x12=\n\ntls_routes\x18\x01 \x03(\x0b2).google.cloud.networkservices.v1.TlsRoute\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x12GetTlsRouteRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'networkservices.googleapis.com/TlsRoute"\xb6\x01\n\x15CreateTlsRouteRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'networkservices.googleapis.com/TlsRoute\x12\x19\n\x0ctls_route_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\ttls_route\x18\x03 \x01(\x0b2).google.cloud.networkservices.v1.TlsRouteB\x03\xe0A\x02"\x90\x01\n\x15UpdateTlsRouteRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12A\n\ttls_route\x18\x02 \x01(\x0b2).google.cloud.networkservices.v1.TlsRouteB\x03\xe0A\x02"V\n\x15DeleteTlsRouteRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'networkservices.googleapis.com/TlsRouteB\xee\x01\n#com.google.cloud.networkservices.v1B\rTlsRouteProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.tls_route_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\rTlsRouteProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1'
    _globals['_TLSROUTE_ROUTERULE'].fields_by_name['matches']._loaded_options = None
    _globals['_TLSROUTE_ROUTERULE'].fields_by_name['matches']._serialized_options = b'\xe0A\x02'
    _globals['_TLSROUTE_ROUTERULE'].fields_by_name['action']._loaded_options = None
    _globals['_TLSROUTE_ROUTERULE'].fields_by_name['action']._serialized_options = b'\xe0A\x02'
    _globals['_TLSROUTE_ROUTEMATCH'].fields_by_name['sni_host']._loaded_options = None
    _globals['_TLSROUTE_ROUTEMATCH'].fields_by_name['sni_host']._serialized_options = b'\xe0A\x01'
    _globals['_TLSROUTE_ROUTEMATCH'].fields_by_name['alpn']._loaded_options = None
    _globals['_TLSROUTE_ROUTEMATCH'].fields_by_name['alpn']._serialized_options = b'\xe0A\x01'
    _globals['_TLSROUTE_ROUTEACTION'].fields_by_name['destinations']._loaded_options = None
    _globals['_TLSROUTE_ROUTEACTION'].fields_by_name['destinations']._serialized_options = b'\xe0A\x02'
    _globals['_TLSROUTE_ROUTEDESTINATION'].fields_by_name['service_name']._loaded_options = None
    _globals['_TLSROUTE_ROUTEDESTINATION'].fields_by_name['service_name']._serialized_options = b"\xe0A\x02\xfaA'\n%compute.googleapis.com/BackendService"
    _globals['_TLSROUTE_ROUTEDESTINATION'].fields_by_name['weight']._loaded_options = None
    _globals['_TLSROUTE_ROUTEDESTINATION'].fields_by_name['weight']._serialized_options = b'\xe0A\x01'
    _globals['_TLSROUTE'].fields_by_name['name']._loaded_options = None
    _globals['_TLSROUTE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_TLSROUTE'].fields_by_name['self_link']._loaded_options = None
    _globals['_TLSROUTE'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_TLSROUTE'].fields_by_name['create_time']._loaded_options = None
    _globals['_TLSROUTE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TLSROUTE'].fields_by_name['update_time']._loaded_options = None
    _globals['_TLSROUTE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TLSROUTE'].fields_by_name['description']._loaded_options = None
    _globals['_TLSROUTE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TLSROUTE'].fields_by_name['rules']._loaded_options = None
    _globals['_TLSROUTE'].fields_by_name['rules']._serialized_options = b'\xe0A\x02'
    _globals['_TLSROUTE'].fields_by_name['meshes']._loaded_options = None
    _globals['_TLSROUTE'].fields_by_name['meshes']._serialized_options = b'\xe0A\x01\xfaA%\n#networkservices.googleapis.com/Mesh'
    _globals['_TLSROUTE'].fields_by_name['gateways']._loaded_options = None
    _globals['_TLSROUTE'].fields_by_name['gateways']._serialized_options = b'\xe0A\x01\xfaA(\n&networkservices.googleapis.com/Gateway'
    _globals['_TLSROUTE']._loaded_options = None
    _globals['_TLSROUTE']._serialized_options = b"\xeaAh\n'networkservices.googleapis.com/TlsRoute\x12=projects/{project}/locations/{location}/tlsRoutes/{tls_route}"
    _globals['_LISTTLSROUTESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTLSROUTESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'networkservices.googleapis.com/TlsRoute"
    _globals['_GETTLSROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTLSROUTEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'networkservices.googleapis.com/TlsRoute"
    _globals['_CREATETLSROUTEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETLSROUTEREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'networkservices.googleapis.com/TlsRoute"
    _globals['_CREATETLSROUTEREQUEST'].fields_by_name['tls_route_id']._loaded_options = None
    _globals['_CREATETLSROUTEREQUEST'].fields_by_name['tls_route_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETLSROUTEREQUEST'].fields_by_name['tls_route']._loaded_options = None
    _globals['_CREATETLSROUTEREQUEST'].fields_by_name['tls_route']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETLSROUTEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETLSROUTEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATETLSROUTEREQUEST'].fields_by_name['tls_route']._loaded_options = None
    _globals['_UPDATETLSROUTEREQUEST'].fields_by_name['tls_route']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETLSROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETLSROUTEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'networkservices.googleapis.com/TlsRoute"
    _globals['_TLSROUTE']._serialized_start = 212
    _globals['_TLSROUTE']._serialized_end = 1142
    _globals['_TLSROUTE_ROUTERULE']._serialized_start = 602
    _globals['_TLSROUTE_ROUTERULE']._serialized_end = 765
    _globals['_TLSROUTE_ROUTEMATCH']._serialized_start = 767
    _globals['_TLSROUTE_ROUTEMATCH']._serialized_end = 821
    _globals['_TLSROUTE_ROUTEACTION']._serialized_start = 823
    _globals['_TLSROUTE_ROUTEACTION']._serialized_end = 923
    _globals['_TLSROUTE_ROUTEDESTINATION']._serialized_start = 925
    _globals['_TLSROUTE_ROUTEDESTINATION']._serialized_end = 1033
    _globals['_LISTTLSROUTESREQUEST']._serialized_start = 1144
    _globals['_LISTTLSROUTESREQUEST']._serialized_end = 1270
    _globals['_LISTTLSROUTESRESPONSE']._serialized_start = 1272
    _globals['_LISTTLSROUTESRESPONSE']._serialized_end = 1383
    _globals['_GETTLSROUTEREQUEST']._serialized_start = 1385
    _globals['_GETTLSROUTEREQUEST']._serialized_end = 1468
    _globals['_CREATETLSROUTEREQUEST']._serialized_start = 1471
    _globals['_CREATETLSROUTEREQUEST']._serialized_end = 1653
    _globals['_UPDATETLSROUTEREQUEST']._serialized_start = 1656
    _globals['_UPDATETLSROUTEREQUEST']._serialized_end = 1800
    _globals['_DELETETLSROUTEREQUEST']._serialized_start = 1802
    _globals['_DELETETLSROUTEREQUEST']._serialized_end = 1888