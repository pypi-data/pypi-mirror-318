"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/beyondcorp/clientgateways/v1/client_gateways_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/cloud/beyondcorp/clientgateways/v1/client_gateways_service.proto\x12)google.cloud.beyondcorp.clientgateways.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfd\x03\n\rClientGateway\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12R\n\x05state\x18\x04 \x01(\x0e2>.google.cloud.beyondcorp.clientgateways.v1.ClientGateway.StateB\x03\xe0A\x03\x12\x0f\n\x02id\x18\x05 \x01(\tB\x03\xe0A\x03\x12%\n\x18client_connector_service\x18\x06 \x01(\tB\x03\xe0A\x03"j\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0c\n\x08UPDATING\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0b\n\x07RUNNING\x10\x04\x12\x08\n\x04DOWN\x10\x05\x12\t\n\x05ERROR\x10\x06:u\xeaAr\n\'beyondcorp.googleapis.com/ClientGateway\x12Gprojects/{project}/locations/{location}/clientGateways/{client_gateway}"\xb9\x01\n\x19ListClientGatewaysRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'beyondcorp.googleapis.com/ClientGateway\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x9d\x01\n\x1aListClientGatewaysResponse\x12Q\n\x0fclient_gateways\x18\x01 \x03(\x0b28.google.cloud.beyondcorp.clientgateways.v1.ClientGateway\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"X\n\x17GetClientGatewayRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'beyondcorp.googleapis.com/ClientGateway"\x89\x02\n\x1aCreateClientGatewayRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'beyondcorp.googleapis.com/ClientGateway\x12\x1e\n\x11client_gateway_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12U\n\x0eclient_gateway\x18\x03 \x01(\x0b28.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x05 \x01(\x08B\x03\xe0A\x01"\x90\x01\n\x1aDeleteClientGatewayRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'beyondcorp.googleapis.com/ClientGateway\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\x8d\x02\n\x1eClientGatewayOperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xc7\x08\n\x15ClientGatewaysService\x12\xe6\x01\n\x12ListClientGateways\x12D.google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysRequest\x1aE.google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/clientGateways\x12\xd3\x01\n\x10GetClientGateway\x12B.google.cloud.beyondcorp.clientgateways.v1.GetClientGatewayRequest\x1a8.google.cloud.beyondcorp.clientgateways.v1.ClientGateway"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/clientGateways/*}\x12\xa4\x02\n\x13CreateClientGateway\x12E.google.cloud.beyondcorp.clientgateways.v1.CreateClientGatewayRequest\x1a\x1d.google.longrunning.Operation"\xa6\x01\xcaA/\n\rClientGateway\x12\x1eClientGatewayOperationMetadata\xdaA\'parent,client_gateway,client_gateway_id\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/clientGateways:\x0eclient_gateway\x12\xf8\x01\n\x13DeleteClientGateway\x12E.google.cloud.beyondcorp.clientgateways.v1.DeleteClientGatewayRequest\x1a\x1d.google.longrunning.Operation"{\xcaA7\n\x15google.protobuf.Empty\x12\x1eClientGatewayOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/clientGateways/*}\x1aM\xcaA\x19beyondcorp.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xac\x02\n-com.google.cloud.beyondcorp.clientgateways.v1B\x1aClientGatewaysServiceProtoP\x01ZUcloud.google.com/go/beyondcorp/clientgateways/apiv1/clientgatewayspb;clientgatewayspb\xaa\x02)Google.Cloud.BeyondCorp.ClientGateways.V1\xca\x02)Google\\Cloud\\BeyondCorp\\ClientGateways\\V1\xea\x02-Google::Cloud::BeyondCorp::ClientGateways::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.beyondcorp.clientgateways.v1.client_gateways_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.beyondcorp.clientgateways.v1B\x1aClientGatewaysServiceProtoP\x01ZUcloud.google.com/go/beyondcorp/clientgateways/apiv1/clientgatewayspb;clientgatewayspb\xaa\x02)Google.Cloud.BeyondCorp.ClientGateways.V1\xca\x02)Google\\Cloud\\BeyondCorp\\ClientGateways\\V1\xea\x02-Google::Cloud::BeyondCorp::ClientGateways::V1'
    _globals['_CLIENTGATEWAY'].fields_by_name['name']._loaded_options = None
    _globals['_CLIENTGATEWAY'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTGATEWAY'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLIENTGATEWAY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAY'].fields_by_name['update_time']._loaded_options = None
    _globals['_CLIENTGATEWAY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAY'].fields_by_name['state']._loaded_options = None
    _globals['_CLIENTGATEWAY'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAY'].fields_by_name['id']._loaded_options = None
    _globals['_CLIENTGATEWAY'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAY'].fields_by_name['client_connector_service']._loaded_options = None
    _globals['_CLIENTGATEWAY'].fields_by_name['client_connector_service']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAY']._loaded_options = None
    _globals['_CLIENTGATEWAY']._serialized_options = b"\xeaAr\n'beyondcorp.googleapis.com/ClientGateway\x12Gprojects/{project}/locations/{location}/clientGateways/{client_gateway}"
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'beyondcorp.googleapis.com/ClientGateway"
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTCLIENTGATEWAYSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETCLIENTGATEWAYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCLIENTGATEWAYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'beyondcorp.googleapis.com/ClientGateway"
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'beyondcorp.googleapis.com/ClientGateway"
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['client_gateway_id']._loaded_options = None
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['client_gateway_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['client_gateway']._loaded_options = None
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['client_gateway']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATECLIENTGATEWAYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECLIENTGATEWAYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECLIENTGATEWAYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'beyondcorp.googleapis.com/ClientGateway"
    _globals['_DELETECLIENTGATEWAYREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETECLIENTGATEWAYREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECLIENTGATEWAYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETECLIENTGATEWAYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_CLIENTGATEWAYOPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTGATEWAYSSERVICE']._loaded_options = None
    _globals['_CLIENTGATEWAYSSERVICE']._serialized_options = b'\xcaA\x19beyondcorp.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLIENTGATEWAYSSERVICE'].methods_by_name['ListClientGateways']._loaded_options = None
    _globals['_CLIENTGATEWAYSSERVICE'].methods_by_name['ListClientGateways']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/clientGateways'
    _globals['_CLIENTGATEWAYSSERVICE'].methods_by_name['GetClientGateway']._loaded_options = None
    _globals['_CLIENTGATEWAYSSERVICE'].methods_by_name['GetClientGateway']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/clientGateways/*}'
    _globals['_CLIENTGATEWAYSSERVICE'].methods_by_name['CreateClientGateway']._loaded_options = None
    _globals['_CLIENTGATEWAYSSERVICE'].methods_by_name['CreateClientGateway']._serialized_options = b'\xcaA/\n\rClientGateway\x12\x1eClientGatewayOperationMetadata\xdaA\'parent,client_gateway,client_gateway_id\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/clientGateways:\x0eclient_gateway'
    _globals['_CLIENTGATEWAYSSERVICE'].methods_by_name['DeleteClientGateway']._loaded_options = None
    _globals['_CLIENTGATEWAYSSERVICE'].methods_by_name['DeleteClientGateway']._serialized_options = b'\xcaA7\n\x15google.protobuf.Empty\x12\x1eClientGatewayOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/clientGateways/*}'
    _globals['_CLIENTGATEWAY']._serialized_start = 304
    _globals['_CLIENTGATEWAY']._serialized_end = 813
    _globals['_CLIENTGATEWAY_STATE']._serialized_start = 588
    _globals['_CLIENTGATEWAY_STATE']._serialized_end = 694
    _globals['_LISTCLIENTGATEWAYSREQUEST']._serialized_start = 816
    _globals['_LISTCLIENTGATEWAYSREQUEST']._serialized_end = 1001
    _globals['_LISTCLIENTGATEWAYSRESPONSE']._serialized_start = 1004
    _globals['_LISTCLIENTGATEWAYSRESPONSE']._serialized_end = 1161
    _globals['_GETCLIENTGATEWAYREQUEST']._serialized_start = 1163
    _globals['_GETCLIENTGATEWAYREQUEST']._serialized_end = 1251
    _globals['_CREATECLIENTGATEWAYREQUEST']._serialized_start = 1254
    _globals['_CREATECLIENTGATEWAYREQUEST']._serialized_end = 1519
    _globals['_DELETECLIENTGATEWAYREQUEST']._serialized_start = 1522
    _globals['_DELETECLIENTGATEWAYREQUEST']._serialized_end = 1666
    _globals['_CLIENTGATEWAYOPERATIONMETADATA']._serialized_start = 1669
    _globals['_CLIENTGATEWAYOPERATIONMETADATA']._serialized_end = 1938
    _globals['_CLIENTGATEWAYSSERVICE']._serialized_start = 1941
    _globals['_CLIENTGATEWAYSSERVICE']._serialized_end = 3036