"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networkconnectivity/v1/policy_based_routing.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networkconnectivity.v1 import common_pb2 as google_dot_cloud_dot_networkconnectivity_dot_v1_dot_common__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/networkconnectivity/v1/policy_based_routing.proto\x12#google.cloud.networkconnectivity.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/networkconnectivity/v1/common.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd1\x0e\n\x10PolicyBasedRoute\x12d\n\x0fvirtual_machine\x18\x12 \x01(\x0b2D.google.cloud.networkconnectivity.v1.PolicyBasedRoute.VirtualMachineB\x03\xe0A\x01H\x00\x12t\n\x17interconnect_attachment\x18\t \x01(\x0b2L.google.cloud.networkconnectivity.v1.PolicyBasedRoute.InterconnectAttachmentB\x03\xe0A\x01H\x00\x12\x1e\n\x0fnext_hop_ilb_ip\x18\x0c \x01(\tB\x03\xe0A\x01H\x01\x12g\n\x15next_hop_other_routes\x18\x15 \x01(\x0e2A.google.cloud.networkconnectivity.v1.PolicyBasedRoute.OtherRoutesB\x03\xe0A\x01H\x01\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Q\n\x06labels\x18\x04 \x03(\x0b2A.google.cloud.networkconnectivity.v1.PolicyBasedRoute.LabelsEntry\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x127\n\x07network\x18\x06 \x01(\tB&\xe0A\x02\xfaA \n\x1ecompute.googleapis.com/Network\x12Q\n\x06filter\x18\n \x01(\x0b2<.google.cloud.networkconnectivity.v1.PolicyBasedRoute.FilterB\x03\xe0A\x02\x12\x15\n\x08priority\x18\x0b \x01(\x05B\x03\xe0A\x01\x12U\n\x08warnings\x18\x0e \x03(\x0b2>.google.cloud.networkconnectivity.v1.PolicyBasedRoute.WarningsB\x03\xe0A\x03\x12\x16\n\tself_link\x18\x0f \x01(\tB\x03\xe0A\x03\x12\x11\n\x04kind\x18\x10 \x01(\tB\x03\xe0A\x03\x1a#\n\x0eVirtualMachine\x12\x11\n\x04tags\x18\x01 \x03(\tB\x03\xe0A\x01\x1a-\n\x16InterconnectAttachment\x12\x13\n\x06region\x18\x01 \x01(\tB\x03\xe0A\x01\x1a\xff\x01\n\x06Filter\x12\x18\n\x0bip_protocol\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x16\n\tsrc_range\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x17\n\ndest_range\x18\x03 \x01(\tB\x03\xe0A\x01\x12k\n\x10protocol_version\x18\x06 \x01(\x0e2L.google.cloud.networkconnectivity.v1.PolicyBasedRoute.Filter.ProtocolVersionB\x03\xe0A\x02"=\n\x0fProtocolVersion\x12 \n\x1cPROTOCOL_VERSION_UNSPECIFIED\x10\x00\x12\x08\n\x04IPV4\x10\x01\x1a\xe1\x02\n\x08Warnings\x12V\n\x04code\x18\x01 \x01(\x0e2C.google.cloud.networkconnectivity.v1.PolicyBasedRoute.Warnings.CodeB\x03\xe0A\x03\x12[\n\x04data\x18\x02 \x03(\x0b2H.google.cloud.networkconnectivity.v1.PolicyBasedRoute.Warnings.DataEntryB\x03\xe0A\x03\x12\x1c\n\x0fwarning_message\x18\x03 \x01(\tB\x03\xe0A\x03\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"U\n\x04Code\x12\x17\n\x13WARNING_UNSPECIFIED\x10\x00\x12\x17\n\x13RESOURCE_NOT_ACTIVE\x10\x01\x12\x1b\n\x17RESOURCE_BEING_MODIFIED\x10\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"@\n\x0bOtherRoutes\x12\x1c\n\x18OTHER_ROUTES_UNSPECIFIED\x10\x00\x12\x13\n\x0fDEFAULT_ROUTING\x10\x01:\x85\x01\xeaA\x81\x01\n3networkconnectivity.googleapis.com/PolicyBasedRoute\x12Jprojects/{project}/locations/global/PolicyBasedRoutes/{policy_based_route}B\x08\n\x06targetB\n\n\x08next_hop"\xa2\x01\n\x1cListPolicyBasedRoutesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\xa1\x01\n\x1dListPolicyBasedRoutesResponse\x12R\n\x13policy_based_routes\x18\x01 \x03(\x0b25.google.cloud.networkconnectivity.v1.PolicyBasedRoute\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"g\n\x1aGetPolicyBasedRouteRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3networkconnectivity.googleapis.com/PolicyBasedRoute"\xef\x01\n\x1dCreatePolicyBasedRouteRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12"\n\x15policy_based_route_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12V\n\x12policy_based_route\x18\x03 \x01(\x0b25.google.cloud.networkconnectivity.v1.PolicyBasedRouteB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x1dDeletePolicyBasedRouteRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3networkconnectivity.googleapis.com/PolicyBasedRoute\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x012\xe3\x08\n\x19PolicyBasedRoutingService\x12\xeb\x01\n\x15ListPolicyBasedRoutes\x12A.google.cloud.networkconnectivity.v1.ListPolicyBasedRoutesRequest\x1aB.google.cloud.networkconnectivity.v1.ListPolicyBasedRoutesResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/global}/policyBasedRoutes\x12\xd8\x01\n\x13GetPolicyBasedRoute\x12?.google.cloud.networkconnectivity.v1.GetPolicyBasedRouteRequest\x1a5.google.cloud.networkconnectivity.v1.PolicyBasedRoute"I\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/global/policyBasedRoutes/*}\x12\xae\x02\n\x16CreatePolicyBasedRoute\x12B.google.cloud.networkconnectivity.v1.CreatePolicyBasedRouteRequest\x1a\x1d.google.longrunning.Operation"\xb0\x01\xcaA%\n\x10PolicyBasedRoute\x12\x11OperationMetadata\xdaA/parent,policy_based_route,policy_based_route_id\x82\xd3\xe4\x93\x02P":/v1/{parent=projects/*/locations/global}/policyBasedRoutes:\x12policy_based_route\x12\xf3\x01\n\x16DeletePolicyBasedRoute\x12B.google.cloud.networkconnectivity.v1.DeletePolicyBasedRouteRequest\x1a\x1d.google.longrunning.Operation"v\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v1/{name=projects/*/locations/global/policyBasedRoutes/*}\x1aV\xcaA"networkconnectivity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x94\x02\n\'com.google.cloud.networkconnectivity.v1B\x17PolicyBasedRoutingProtoP\x01ZYcloud.google.com/go/networkconnectivity/apiv1/networkconnectivitypb;networkconnectivitypb\xaa\x02#Google.Cloud.NetworkConnectivity.V1\xca\x02#Google\\Cloud\\NetworkConnectivity\\V1\xea\x02&Google::Cloud::NetworkConnectivity::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkconnectivity.v1.policy_based_routing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.networkconnectivity.v1B\x17PolicyBasedRoutingProtoP\x01ZYcloud.google.com/go/networkconnectivity/apiv1/networkconnectivitypb;networkconnectivitypb\xaa\x02#Google.Cloud.NetworkConnectivity.V1\xca\x02#Google\\Cloud\\NetworkConnectivity\\V1\xea\x02&Google::Cloud::NetworkConnectivity::V1"
    _globals['_POLICYBASEDROUTE_VIRTUALMACHINE'].fields_by_name['tags']._loaded_options = None
    _globals['_POLICYBASEDROUTE_VIRTUALMACHINE'].fields_by_name['tags']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE_INTERCONNECTATTACHMENT'].fields_by_name['region']._loaded_options = None
    _globals['_POLICYBASEDROUTE_INTERCONNECTATTACHMENT'].fields_by_name['region']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE_FILTER'].fields_by_name['ip_protocol']._loaded_options = None
    _globals['_POLICYBASEDROUTE_FILTER'].fields_by_name['ip_protocol']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE_FILTER'].fields_by_name['src_range']._loaded_options = None
    _globals['_POLICYBASEDROUTE_FILTER'].fields_by_name['src_range']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE_FILTER'].fields_by_name['dest_range']._loaded_options = None
    _globals['_POLICYBASEDROUTE_FILTER'].fields_by_name['dest_range']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE_FILTER'].fields_by_name['protocol_version']._loaded_options = None
    _globals['_POLICYBASEDROUTE_FILTER'].fields_by_name['protocol_version']._serialized_options = b'\xe0A\x02'
    _globals['_POLICYBASEDROUTE_WARNINGS_DATAENTRY']._loaded_options = None
    _globals['_POLICYBASEDROUTE_WARNINGS_DATAENTRY']._serialized_options = b'8\x01'
    _globals['_POLICYBASEDROUTE_WARNINGS'].fields_by_name['code']._loaded_options = None
    _globals['_POLICYBASEDROUTE_WARNINGS'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBASEDROUTE_WARNINGS'].fields_by_name['data']._loaded_options = None
    _globals['_POLICYBASEDROUTE_WARNINGS'].fields_by_name['data']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBASEDROUTE_WARNINGS'].fields_by_name['warning_message']._loaded_options = None
    _globals['_POLICYBASEDROUTE_WARNINGS'].fields_by_name['warning_message']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBASEDROUTE_LABELSENTRY']._loaded_options = None
    _globals['_POLICYBASEDROUTE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_POLICYBASEDROUTE'].fields_by_name['virtual_machine']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['virtual_machine']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE'].fields_by_name['interconnect_attachment']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['interconnect_attachment']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE'].fields_by_name['next_hop_ilb_ip']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['next_hop_ilb_ip']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE'].fields_by_name['next_hop_other_routes']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['next_hop_other_routes']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE'].fields_by_name['name']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_POLICYBASEDROUTE'].fields_by_name['create_time']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBASEDROUTE'].fields_by_name['update_time']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBASEDROUTE'].fields_by_name['description']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE'].fields_by_name['network']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['network']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_POLICYBASEDROUTE'].fields_by_name['filter']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_POLICYBASEDROUTE'].fields_by_name['priority']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['priority']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTE'].fields_by_name['warnings']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['warnings']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBASEDROUTE'].fields_by_name['self_link']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBASEDROUTE'].fields_by_name['kind']._loaded_options = None
    _globals['_POLICYBASEDROUTE'].fields_by_name['kind']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYBASEDROUTE']._loaded_options = None
    _globals['_POLICYBASEDROUTE']._serialized_options = b'\xeaA\x81\x01\n3networkconnectivity.googleapis.com/PolicyBasedRoute\x12Jprojects/{project}/locations/global/PolicyBasedRoutes/{policy_based_route}'
    _globals['_LISTPOLICYBASEDROUTESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPOLICYBASEDROUTESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETPOLICYBASEDROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPOLICYBASEDROUTEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3networkconnectivity.googleapis.com/PolicyBasedRoute'
    _globals['_CREATEPOLICYBASEDROUTEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPOLICYBASEDROUTEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEPOLICYBASEDROUTEREQUEST'].fields_by_name['policy_based_route_id']._loaded_options = None
    _globals['_CREATEPOLICYBASEDROUTEREQUEST'].fields_by_name['policy_based_route_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPOLICYBASEDROUTEREQUEST'].fields_by_name['policy_based_route']._loaded_options = None
    _globals['_CREATEPOLICYBASEDROUTEREQUEST'].fields_by_name['policy_based_route']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPOLICYBASEDROUTEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEPOLICYBASEDROUTEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPOLICYBASEDROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPOLICYBASEDROUTEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3networkconnectivity.googleapis.com/PolicyBasedRoute'
    _globals['_DELETEPOLICYBASEDROUTEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEPOLICYBASEDROUTEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBASEDROUTINGSERVICE']._loaded_options = None
    _globals['_POLICYBASEDROUTINGSERVICE']._serialized_options = b'\xcaA"networkconnectivity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_POLICYBASEDROUTINGSERVICE'].methods_by_name['ListPolicyBasedRoutes']._loaded_options = None
    _globals['_POLICYBASEDROUTINGSERVICE'].methods_by_name['ListPolicyBasedRoutes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/global}/policyBasedRoutes'
    _globals['_POLICYBASEDROUTINGSERVICE'].methods_by_name['GetPolicyBasedRoute']._loaded_options = None
    _globals['_POLICYBASEDROUTINGSERVICE'].methods_by_name['GetPolicyBasedRoute']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/global/policyBasedRoutes/*}'
    _globals['_POLICYBASEDROUTINGSERVICE'].methods_by_name['CreatePolicyBasedRoute']._loaded_options = None
    _globals['_POLICYBASEDROUTINGSERVICE'].methods_by_name['CreatePolicyBasedRoute']._serialized_options = b'\xcaA%\n\x10PolicyBasedRoute\x12\x11OperationMetadata\xdaA/parent,policy_based_route,policy_based_route_id\x82\xd3\xe4\x93\x02P":/v1/{parent=projects/*/locations/global}/policyBasedRoutes:\x12policy_based_route'
    _globals['_POLICYBASEDROUTINGSERVICE'].methods_by_name['DeletePolicyBasedRoute']._loaded_options = None
    _globals['_POLICYBASEDROUTINGSERVICE'].methods_by_name['DeletePolicyBasedRoute']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v1/{name=projects/*/locations/global/policyBasedRoutes/*}'
    _globals['_POLICYBASEDROUTE']._serialized_start = 368
    _globals['_POLICYBASEDROUTE']._serialized_end = 2241
    _globals['_POLICYBASEDROUTE_VIRTUALMACHINE']._serialized_start = 1274
    _globals['_POLICYBASEDROUTE_VIRTUALMACHINE']._serialized_end = 1309
    _globals['_POLICYBASEDROUTE_INTERCONNECTATTACHMENT']._serialized_start = 1311
    _globals['_POLICYBASEDROUTE_INTERCONNECTATTACHMENT']._serialized_end = 1356
    _globals['_POLICYBASEDROUTE_FILTER']._serialized_start = 1359
    _globals['_POLICYBASEDROUTE_FILTER']._serialized_end = 1614
    _globals['_POLICYBASEDROUTE_FILTER_PROTOCOLVERSION']._serialized_start = 1553
    _globals['_POLICYBASEDROUTE_FILTER_PROTOCOLVERSION']._serialized_end = 1614
    _globals['_POLICYBASEDROUTE_WARNINGS']._serialized_start = 1617
    _globals['_POLICYBASEDROUTE_WARNINGS']._serialized_end = 1970
    _globals['_POLICYBASEDROUTE_WARNINGS_DATAENTRY']._serialized_start = 1840
    _globals['_POLICYBASEDROUTE_WARNINGS_DATAENTRY']._serialized_end = 1883
    _globals['_POLICYBASEDROUTE_WARNINGS_CODE']._serialized_start = 1885
    _globals['_POLICYBASEDROUTE_WARNINGS_CODE']._serialized_end = 1970
    _globals['_POLICYBASEDROUTE_LABELSENTRY']._serialized_start = 1972
    _globals['_POLICYBASEDROUTE_LABELSENTRY']._serialized_end = 2017
    _globals['_POLICYBASEDROUTE_OTHERROUTES']._serialized_start = 2019
    _globals['_POLICYBASEDROUTE_OTHERROUTES']._serialized_end = 2083
    _globals['_LISTPOLICYBASEDROUTESREQUEST']._serialized_start = 2244
    _globals['_LISTPOLICYBASEDROUTESREQUEST']._serialized_end = 2406
    _globals['_LISTPOLICYBASEDROUTESRESPONSE']._serialized_start = 2409
    _globals['_LISTPOLICYBASEDROUTESRESPONSE']._serialized_end = 2570
    _globals['_GETPOLICYBASEDROUTEREQUEST']._serialized_start = 2572
    _globals['_GETPOLICYBASEDROUTEREQUEST']._serialized_end = 2675
    _globals['_CREATEPOLICYBASEDROUTEREQUEST']._serialized_start = 2678
    _globals['_CREATEPOLICYBASEDROUTEREQUEST']._serialized_end = 2917
    _globals['_DELETEPOLICYBASEDROUTEREQUEST']._serialized_start = 2920
    _globals['_DELETEPOLICYBASEDROUTEREQUEST']._serialized_end = 3051
    _globals['_POLICYBASEDROUTINGSERVICE']._serialized_start = 3054
    _globals['_POLICYBASEDROUTINGSERVICE']._serialized_end = 4177