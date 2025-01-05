"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networkservices/v1/tcp_route.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/networkservices/v1/tcp_route.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc0\x08\n\x08TcpRoute\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tself_link\x18\x0b \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x12G\n\x05rules\x18\x05 \x03(\x0b23.google.cloud.networkservices.v1.TcpRoute.RouteRuleB\x03\xe0A\x02\x12;\n\x06meshes\x18\x08 \x03(\tB+\xe0A\x01\xfaA%\n#networkservices.googleapis.com/Mesh\x12@\n\x08gateways\x18\t \x03(\tB.\xe0A\x01\xfaA(\n&networkservices.googleapis.com/Gateway\x12J\n\x06labels\x18\n \x03(\x0b25.google.cloud.networkservices.v1.TcpRoute.LabelsEntryB\x03\xe0A\x01\x1a\xa3\x01\n\tRouteRule\x12J\n\x07matches\x18\x01 \x03(\x0b24.google.cloud.networkservices.v1.TcpRoute.RouteMatchB\x03\xe0A\x01\x12J\n\x06action\x18\x02 \x01(\x0b25.google.cloud.networkservices.v1.TcpRoute.RouteActionB\x03\xe0A\x02\x1a5\n\nRouteMatch\x12\x14\n\x07address\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04port\x18\x02 \x01(\tB\x03\xe0A\x02\x1a\x87\x01\n\x0bRouteAction\x12U\n\x0cdestinations\x18\x01 \x03(\x0b2:.google.cloud.networkservices.v1.TcpRoute.RouteDestinationB\x03\xe0A\x01\x12!\n\x14original_destination\x18\x03 \x01(\x08B\x03\xe0A\x01\x1al\n\x10RouteDestination\x12C\n\x0cservice_name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%compute.googleapis.com/BackendService\x12\x13\n\x06weight\x18\x02 \x01(\x05B\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:k\xeaAh\n\'networkservices.googleapis.com/TcpRoute\x12=projects/{project}/locations/{location}/tcpRoutes/{tcp_route}"~\n\x14ListTcpRoutesRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'networkservices.googleapis.com/TcpRoute\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"o\n\x15ListTcpRoutesResponse\x12=\n\ntcp_routes\x18\x01 \x03(\x0b2).google.cloud.networkservices.v1.TcpRoute\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x12GetTcpRouteRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'networkservices.googleapis.com/TcpRoute"\xb6\x01\n\x15CreateTcpRouteRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'networkservices.googleapis.com/TcpRoute\x12\x19\n\x0ctcp_route_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\ttcp_route\x18\x03 \x01(\x0b2).google.cloud.networkservices.v1.TcpRouteB\x03\xe0A\x02"\x90\x01\n\x15UpdateTcpRouteRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12A\n\ttcp_route\x18\x02 \x01(\x0b2).google.cloud.networkservices.v1.TcpRouteB\x03\xe0A\x02"V\n\x15DeleteTcpRouteRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'networkservices.googleapis.com/TcpRouteB\xe3\x02\n#com.google.cloud.networkservices.v1B\rTcpRouteProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaAr\n%compute.googleapis.com/BackendService\x12Iprojects/{project}/locations/{location}/backendServices/{backend_service}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.tcp_route_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\rTcpRouteProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaAr\n%compute.googleapis.com/BackendService\x12Iprojects/{project}/locations/{location}/backendServices/{backend_service}'
    _globals['_TCPROUTE_ROUTERULE'].fields_by_name['matches']._loaded_options = None
    _globals['_TCPROUTE_ROUTERULE'].fields_by_name['matches']._serialized_options = b'\xe0A\x01'
    _globals['_TCPROUTE_ROUTERULE'].fields_by_name['action']._loaded_options = None
    _globals['_TCPROUTE_ROUTERULE'].fields_by_name['action']._serialized_options = b'\xe0A\x02'
    _globals['_TCPROUTE_ROUTEMATCH'].fields_by_name['address']._loaded_options = None
    _globals['_TCPROUTE_ROUTEMATCH'].fields_by_name['address']._serialized_options = b'\xe0A\x02'
    _globals['_TCPROUTE_ROUTEMATCH'].fields_by_name['port']._loaded_options = None
    _globals['_TCPROUTE_ROUTEMATCH'].fields_by_name['port']._serialized_options = b'\xe0A\x02'
    _globals['_TCPROUTE_ROUTEACTION'].fields_by_name['destinations']._loaded_options = None
    _globals['_TCPROUTE_ROUTEACTION'].fields_by_name['destinations']._serialized_options = b'\xe0A\x01'
    _globals['_TCPROUTE_ROUTEACTION'].fields_by_name['original_destination']._loaded_options = None
    _globals['_TCPROUTE_ROUTEACTION'].fields_by_name['original_destination']._serialized_options = b'\xe0A\x01'
    _globals['_TCPROUTE_ROUTEDESTINATION'].fields_by_name['service_name']._loaded_options = None
    _globals['_TCPROUTE_ROUTEDESTINATION'].fields_by_name['service_name']._serialized_options = b"\xe0A\x02\xfaA'\n%compute.googleapis.com/BackendService"
    _globals['_TCPROUTE_ROUTEDESTINATION'].fields_by_name['weight']._loaded_options = None
    _globals['_TCPROUTE_ROUTEDESTINATION'].fields_by_name['weight']._serialized_options = b'\xe0A\x01'
    _globals['_TCPROUTE_LABELSENTRY']._loaded_options = None
    _globals['_TCPROUTE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TCPROUTE'].fields_by_name['name']._loaded_options = None
    _globals['_TCPROUTE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_TCPROUTE'].fields_by_name['self_link']._loaded_options = None
    _globals['_TCPROUTE'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_TCPROUTE'].fields_by_name['create_time']._loaded_options = None
    _globals['_TCPROUTE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TCPROUTE'].fields_by_name['update_time']._loaded_options = None
    _globals['_TCPROUTE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TCPROUTE'].fields_by_name['description']._loaded_options = None
    _globals['_TCPROUTE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TCPROUTE'].fields_by_name['rules']._loaded_options = None
    _globals['_TCPROUTE'].fields_by_name['rules']._serialized_options = b'\xe0A\x02'
    _globals['_TCPROUTE'].fields_by_name['meshes']._loaded_options = None
    _globals['_TCPROUTE'].fields_by_name['meshes']._serialized_options = b'\xe0A\x01\xfaA%\n#networkservices.googleapis.com/Mesh'
    _globals['_TCPROUTE'].fields_by_name['gateways']._loaded_options = None
    _globals['_TCPROUTE'].fields_by_name['gateways']._serialized_options = b'\xe0A\x01\xfaA(\n&networkservices.googleapis.com/Gateway'
    _globals['_TCPROUTE'].fields_by_name['labels']._loaded_options = None
    _globals['_TCPROUTE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_TCPROUTE']._loaded_options = None
    _globals['_TCPROUTE']._serialized_options = b"\xeaAh\n'networkservices.googleapis.com/TcpRoute\x12=projects/{project}/locations/{location}/tcpRoutes/{tcp_route}"
    _globals['_LISTTCPROUTESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTCPROUTESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'networkservices.googleapis.com/TcpRoute"
    _globals['_GETTCPROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTCPROUTEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'networkservices.googleapis.com/TcpRoute"
    _globals['_CREATETCPROUTEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETCPROUTEREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'networkservices.googleapis.com/TcpRoute"
    _globals['_CREATETCPROUTEREQUEST'].fields_by_name['tcp_route_id']._loaded_options = None
    _globals['_CREATETCPROUTEREQUEST'].fields_by_name['tcp_route_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETCPROUTEREQUEST'].fields_by_name['tcp_route']._loaded_options = None
    _globals['_CREATETCPROUTEREQUEST'].fields_by_name['tcp_route']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETCPROUTEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETCPROUTEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATETCPROUTEREQUEST'].fields_by_name['tcp_route']._loaded_options = None
    _globals['_UPDATETCPROUTEREQUEST'].fields_by_name['tcp_route']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETCPROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETCPROUTEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'networkservices.googleapis.com/TcpRoute"
    _globals['_TCPROUTE']._serialized_start = 212
    _globals['_TCPROUTE']._serialized_end = 1300
    _globals['_TCPROUTE_ROUTERULE']._serialized_start = 678
    _globals['_TCPROUTE_ROUTERULE']._serialized_end = 841
    _globals['_TCPROUTE_ROUTEMATCH']._serialized_start = 843
    _globals['_TCPROUTE_ROUTEMATCH']._serialized_end = 896
    _globals['_TCPROUTE_ROUTEACTION']._serialized_start = 899
    _globals['_TCPROUTE_ROUTEACTION']._serialized_end = 1034
    _globals['_TCPROUTE_ROUTEDESTINATION']._serialized_start = 1036
    _globals['_TCPROUTE_ROUTEDESTINATION']._serialized_end = 1144
    _globals['_TCPROUTE_LABELSENTRY']._serialized_start = 1146
    _globals['_TCPROUTE_LABELSENTRY']._serialized_end = 1191
    _globals['_LISTTCPROUTESREQUEST']._serialized_start = 1302
    _globals['_LISTTCPROUTESREQUEST']._serialized_end = 1428
    _globals['_LISTTCPROUTESRESPONSE']._serialized_start = 1430
    _globals['_LISTTCPROUTESRESPONSE']._serialized_end = 1541
    _globals['_GETTCPROUTEREQUEST']._serialized_start = 1543
    _globals['_GETTCPROUTEREQUEST']._serialized_end = 1626
    _globals['_CREATETCPROUTEREQUEST']._serialized_start = 1629
    _globals['_CREATETCPROUTEREQUEST']._serialized_end = 1811
    _globals['_UPDATETCPROUTEREQUEST']._serialized_start = 1814
    _globals['_UPDATETCPROUTEREQUEST']._serialized_end = 1958
    _globals['_DELETETCPROUTEREQUEST']._serialized_start = 1960
    _globals['_DELETETCPROUTEREQUEST']._serialized_end = 2046