"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/beyondcorp/appgateways/v1/app_gateways_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/beyondcorp/appgateways/v1/app_gateways_service.proto\x12&google.cloud.beyondcorp.appgateways.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb3\x01\n\x16ListAppGatewaysRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$beyondcorp.googleapis.com/AppGateway\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x91\x01\n\x17ListAppGatewaysResponse\x12H\n\x0capp_gateways\x18\x01 \x03(\x0b22.google.cloud.beyondcorp.appgateways.v1.AppGateway\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"R\n\x14GetAppGatewayRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$beyondcorp.googleapis.com/AppGateway"\xf7\x01\n\x17CreateAppGatewayRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$beyondcorp.googleapis.com/AppGateway\x12\x1b\n\x0eapp_gateway_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12L\n\x0bapp_gateway\x18\x03 \x01(\x0b22.google.cloud.beyondcorp.appgateways.v1.AppGatewayB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x05 \x01(\x08B\x03\xe0A\x01"\x8a\x01\n\x17DeleteAppGatewayRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$beyondcorp.googleapis.com/AppGateway\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\xaa\x08\n\nAppGateway\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12S\n\x06labels\x18\x04 \x03(\x0b2>.google.cloud.beyondcorp.appgateways.v1.AppGateway.LabelsEntryB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x10\n\x03uid\x18\x06 \x01(\tB\x03\xe0A\x03\x12J\n\x04type\x18\x07 \x01(\x0e27.google.cloud.beyondcorp.appgateways.v1.AppGateway.TypeB\x03\xe0A\x02\x12L\n\x05state\x18\x08 \x01(\x0e28.google.cloud.beyondcorp.appgateways.v1.AppGateway.StateB\x03\xe0A\x03\x12\x10\n\x03uri\x18\t \x01(\tB\x03\xe0A\x03\x12j\n\x15allocated_connections\x18\n \x03(\x0b2F.google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnectionB\x03\xe0A\x03\x12S\n\thost_type\x18\x0b \x01(\x0e2;.google.cloud.beyondcorp.appgateways.v1.AppGateway.HostTypeB\x03\xe0A\x02\x1aF\n\x13AllocatedConnection\x12\x14\n\x07psc_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cingress_port\x18\x02 \x01(\x05B\x03\xe0A\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"+\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\r\n\tTCP_PROXY\x10\x01"_\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0b\n\x07CREATED\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\x08\n\x04DOWN\x10\x05";\n\x08HostType\x12\x19\n\x15HOST_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10GCP_REGIONAL_MIG\x10\x01:l\xeaAi\n$beyondcorp.googleapis.com/AppGateway\x12Aprojects/{project}/locations/{location}/appGateways/{app_gateway}"\x8a\x02\n\x1bAppGatewayOperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xf6\x07\n\x12AppGatewaysService\x12\xd4\x01\n\x0fListAppGateways\x12>.google.cloud.beyondcorp.appgateways.v1.ListAppGatewaysRequest\x1a?.google.cloud.beyondcorp.appgateways.v1.ListAppGatewaysResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/appGateways\x12\xc1\x01\n\rGetAppGateway\x12<.google.cloud.beyondcorp.appgateways.v1.GetAppGatewayRequest\x1a2.google.cloud.beyondcorp.appgateways.v1.AppGateway">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/appGateways/*}\x12\x89\x02\n\x10CreateAppGateway\x12?.google.cloud.beyondcorp.appgateways.v1.CreateAppGatewayRequest\x1a\x1d.google.longrunning.Operation"\x94\x01\xcaA)\n\nAppGateway\x12\x1bAppGatewayOperationMetadata\xdaA!parent,app_gateway,app_gateway_id\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/appGateways:\x0bapp_gateway\x12\xe9\x01\n\x10DeleteAppGateway\x12?.google.cloud.beyondcorp.appgateways.v1.DeleteAppGatewayRequest\x1a\x1d.google.longrunning.Operation"u\xcaA4\n\x15google.protobuf.Empty\x12\x1bAppGatewayOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/appGateways/*}\x1aM\xcaA\x19beyondcorp.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x94\x02\n*com.google.cloud.beyondcorp.appgateways.v1B\x17AppGatewaysServiceProtoP\x01ZLcloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb;appgatewayspb\xaa\x02&Google.Cloud.BeyondCorp.AppGateways.V1\xca\x02&Google\\Cloud\\BeyondCorp\\AppGateways\\V1\xea\x02*Google::Cloud::BeyondCorp::AppGateways::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.beyondcorp.appgateways.v1.app_gateways_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.beyondcorp.appgateways.v1B\x17AppGatewaysServiceProtoP\x01ZLcloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb;appgatewayspb\xaa\x02&Google.Cloud.BeyondCorp.AppGateways.V1\xca\x02&Google\\Cloud\\BeyondCorp\\AppGateways\\V1\xea\x02*Google::Cloud::BeyondCorp::AppGateways::V1'
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$beyondcorp.googleapis.com/AppGateway'
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTAPPGATEWAYSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETAPPGATEWAYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAPPGATEWAYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$beyondcorp.googleapis.com/AppGateway'
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$beyondcorp.googleapis.com/AppGateway'
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['app_gateway_id']._loaded_options = None
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['app_gateway_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['app_gateway']._loaded_options = None
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['app_gateway']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATEAPPGATEWAYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEAPPGATEWAYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAPPGATEWAYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$beyondcorp.googleapis.com/AppGateway'
    _globals['_DELETEAPPGATEWAYREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEAPPGATEWAYREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEAPPGATEWAYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETEAPPGATEWAYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_APPGATEWAY_ALLOCATEDCONNECTION'].fields_by_name['psc_uri']._loaded_options = None
    _globals['_APPGATEWAY_ALLOCATEDCONNECTION'].fields_by_name['psc_uri']._serialized_options = b'\xe0A\x02'
    _globals['_APPGATEWAY_ALLOCATEDCONNECTION'].fields_by_name['ingress_port']._loaded_options = None
    _globals['_APPGATEWAY_ALLOCATEDCONNECTION'].fields_by_name['ingress_port']._serialized_options = b'\xe0A\x02'
    _globals['_APPGATEWAY_LABELSENTRY']._loaded_options = None
    _globals['_APPGATEWAY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_APPGATEWAY'].fields_by_name['name']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_APPGATEWAY'].fields_by_name['create_time']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAY'].fields_by_name['update_time']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAY'].fields_by_name['labels']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_APPGATEWAY'].fields_by_name['display_name']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_APPGATEWAY'].fields_by_name['uid']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAY'].fields_by_name['type']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_APPGATEWAY'].fields_by_name['state']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAY'].fields_by_name['uri']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['uri']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAY'].fields_by_name['allocated_connections']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['allocated_connections']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAY'].fields_by_name['host_type']._loaded_options = None
    _globals['_APPGATEWAY'].fields_by_name['host_type']._serialized_options = b'\xe0A\x02'
    _globals['_APPGATEWAY']._loaded_options = None
    _globals['_APPGATEWAY']._serialized_options = b'\xeaAi\n$beyondcorp.googleapis.com/AppGateway\x12Aprojects/{project}/locations/{location}/appGateways/{app_gateway}'
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_APPGATEWAYOPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_APPGATEWAYSSERVICE']._loaded_options = None
    _globals['_APPGATEWAYSSERVICE']._serialized_options = b'\xcaA\x19beyondcorp.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_APPGATEWAYSSERVICE'].methods_by_name['ListAppGateways']._loaded_options = None
    _globals['_APPGATEWAYSSERVICE'].methods_by_name['ListAppGateways']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/appGateways'
    _globals['_APPGATEWAYSSERVICE'].methods_by_name['GetAppGateway']._loaded_options = None
    _globals['_APPGATEWAYSSERVICE'].methods_by_name['GetAppGateway']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/appGateways/*}'
    _globals['_APPGATEWAYSSERVICE'].methods_by_name['CreateAppGateway']._loaded_options = None
    _globals['_APPGATEWAYSSERVICE'].methods_by_name['CreateAppGateway']._serialized_options = b'\xcaA)\n\nAppGateway\x12\x1bAppGatewayOperationMetadata\xdaA!parent,app_gateway,app_gateway_id\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/appGateways:\x0bapp_gateway'
    _globals['_APPGATEWAYSSERVICE'].methods_by_name['DeleteAppGateway']._loaded_options = None
    _globals['_APPGATEWAYSSERVICE'].methods_by_name['DeleteAppGateway']._serialized_options = b'\xcaA4\n\x15google.protobuf.Empty\x12\x1bAppGatewayOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/appGateways/*}'
    _globals['_LISTAPPGATEWAYSREQUEST']._serialized_start = 295
    _globals['_LISTAPPGATEWAYSREQUEST']._serialized_end = 474
    _globals['_LISTAPPGATEWAYSRESPONSE']._serialized_start = 477
    _globals['_LISTAPPGATEWAYSRESPONSE']._serialized_end = 622
    _globals['_GETAPPGATEWAYREQUEST']._serialized_start = 624
    _globals['_GETAPPGATEWAYREQUEST']._serialized_end = 706
    _globals['_CREATEAPPGATEWAYREQUEST']._serialized_start = 709
    _globals['_CREATEAPPGATEWAYREQUEST']._serialized_end = 956
    _globals['_DELETEAPPGATEWAYREQUEST']._serialized_start = 959
    _globals['_DELETEAPPGATEWAYREQUEST']._serialized_end = 1097
    _globals['_APPGATEWAY']._serialized_start = 1100
    _globals['_APPGATEWAY']._serialized_end = 2166
    _globals['_APPGATEWAY_ALLOCATEDCONNECTION']._serialized_start = 1736
    _globals['_APPGATEWAY_ALLOCATEDCONNECTION']._serialized_end = 1806
    _globals['_APPGATEWAY_LABELSENTRY']._serialized_start = 1808
    _globals['_APPGATEWAY_LABELSENTRY']._serialized_end = 1853
    _globals['_APPGATEWAY_TYPE']._serialized_start = 1855
    _globals['_APPGATEWAY_TYPE']._serialized_end = 1898
    _globals['_APPGATEWAY_STATE']._serialized_start = 1900
    _globals['_APPGATEWAY_STATE']._serialized_end = 1995
    _globals['_APPGATEWAY_HOSTTYPE']._serialized_start = 1997
    _globals['_APPGATEWAY_HOSTTYPE']._serialized_end = 2056
    _globals['_APPGATEWAYOPERATIONMETADATA']._serialized_start = 2169
    _globals['_APPGATEWAYOPERATIONMETADATA']._serialized_end = 2435
    _globals['_APPGATEWAYSSERVICE']._serialized_start = 2438
    _globals['_APPGATEWAYSSERVICE']._serialized_end = 3452