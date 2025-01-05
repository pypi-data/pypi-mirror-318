"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/beyondcorp/clientconnectorservices/v1/client_connector_services_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nZgoogle/cloud/beyondcorp/clientconnectorservices/v1/client_connector_services_service.proto\x122google.cloud.beyondcorp.clientconnectorservices.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdc\x0b\n\x16ClientConnectorService\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x01\x12h\n\x07ingress\x18\x06 \x01(\x0b2R.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorService.IngressB\x03\xe0A\x02\x12f\n\x06egress\x18\x07 \x01(\x0b2Q.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorService.EgressB\x03\xe0A\x02\x12d\n\x05state\x18\x08 \x01(\x0e2P.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorService.StateB\x03\xe0A\x03\x1a\xb5\x04\n\x07Ingress\x12k\n\x06config\x18\x01 \x01(\x0b2Y.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorService.Ingress.ConfigH\x00\x1a\xaa\x03\n\x06Config\x12\x8f\x01\n\x12transport_protocol\x18\x01 \x01(\x0e2k.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorService.Ingress.Config.TransportProtocolB\x06\xe0A\x02\xe0A\x05\x12\x8b\x01\n\x12destination_routes\x18\x02 \x03(\x0b2j.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorService.Ingress.Config.DestinationRouteB\x03\xe0A\x02\x1a>\n\x10DestinationRoute\x12\x14\n\x07address\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07netmask\x18\x02 \x01(\tB\x03\xe0A\x02"@\n\x11TransportProtocol\x12"\n\x1eTRANSPORT_PROTOCOL_UNSPECIFIED\x10\x00\x12\x07\n\x03TCP\x10\x01B\x10\n\x0eingress_config\x1a\xb6\x01\n\x06Egress\x12q\n\npeered_vpc\x18\x01 \x01(\x0b2[.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorService.Egress.PeeredVpcH\x00\x1a%\n\tPeeredVpc\x12\x18\n\x0bnetwork_vpc\x18\x01 \x01(\tB\x03\xe0A\x02B\x12\n\x10destination_type"j\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0c\n\x08UPDATING\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0b\n\x07RUNNING\x10\x04\x12\x08\n\x04DOWN\x10\x05\x12\t\n\x05ERROR\x10\x06:\x92\x01\xeaA\x8e\x01\n0beyondcorp.googleapis.com/ClientConnectorService\x12Zprojects/{project}/locations/{location}/clientConnectorServices/{client_connector_service}"\xcb\x01\n"ListClientConnectorServicesRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120beyondcorp.googleapis.com/ClientConnectorService\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\xc2\x01\n#ListClientConnectorServicesResponse\x12m\n\x19client_connector_services\x18\x01 \x03(\x0b2J.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorService\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"j\n GetClientConnectorServiceRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0beyondcorp.googleapis.com/ClientConnectorService"\xc1\x02\n#CreateClientConnectorServiceRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120beyondcorp.googleapis.com/ClientConnectorService\x12(\n\x1bclient_connector_service_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12q\n\x18client_connector_service\x18\x03 \x01(\x0b2J.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorServiceB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x05 \x01(\x08B\x03\xe0A\x01"\x9f\x02\n#UpdateClientConnectorServiceRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12q\n\x18client_connector_service\x18\x02 \x01(\x0b2J.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorServiceB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rallow_missing\x18\x05 \x01(\x08B\x03\xe0A\x01"\xa2\x01\n#DeleteClientConnectorServiceRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0beyondcorp.googleapis.com/ClientConnectorService\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\x96\x02\n\'ClientConnectorServiceOperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xbb\r\n\x1eClientConnectorServicesService\x12\x9c\x02\n\x1bListClientConnectorServices\x12V.google.cloud.beyondcorp.clientconnectorservices.v1.ListClientConnectorServicesRequest\x1aW.google.cloud.beyondcorp.clientconnectorservices.v1.ListClientConnectorServicesResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=projects/*/locations/*}/clientConnectorServices\x12\x89\x02\n\x19GetClientConnectorService\x12T.google.cloud.beyondcorp.clientconnectorservices.v1.GetClientConnectorServiceRequest\x1aJ.google.cloud.beyondcorp.clientconnectorservices.v1.ClientConnectorService"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/{name=projects/*/locations/*/clientConnectorServices/*}\x12\xf8\x02\n\x1cCreateClientConnectorService\x12W.google.cloud.beyondcorp.clientconnectorservices.v1.CreateClientConnectorServiceRequest\x1a\x1d.google.longrunning.Operation"\xdf\x01\xcaAA\n\x16ClientConnectorService\x12\'ClientConnectorServiceOperationMetadata\xdaA;parent,client_connector_service,client_connector_service_id\x82\xd3\xe4\x93\x02W";/v1/{parent=projects/*/locations/*}/clientConnectorServices:\x18client_connector_service\x12\xfa\x02\n\x1cUpdateClientConnectorService\x12W.google.cloud.beyondcorp.clientconnectorservices.v1.UpdateClientConnectorServiceRequest\x1a\x1d.google.longrunning.Operation"\xe1\x01\xcaAA\n\x16ClientConnectorService\x12\'ClientConnectorServiceOperationMetadata\xdaA$client_connector_service,update_mask\x82\xd3\xe4\x93\x02p2T/v1/{client_connector_service.name=projects/*/locations/*/clientConnectorServices/*}:\x18client_connector_service\x12\xa6\x02\n\x1cDeleteClientConnectorService\x12W.google.cloud.beyondcorp.clientconnectorservices.v1.DeleteClientConnectorServiceRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaA@\n\x15google.protobuf.Empty\x12\'ClientConnectorServiceOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1/{name=projects/*/locations/*/clientConnectorServices/*}\x1aM\xcaA\x19beyondcorp.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf4\x02\n6com.google.cloud.beyondcorp.clientconnectorservices.v1B#ClientConnectorServicesServiceProtoP\x01Zpcloud.google.com/go/beyondcorp/clientconnectorservices/apiv1/clientconnectorservicespb;clientconnectorservicespb\xaa\x022Google.Cloud.BeyondCorp.ClientConnectorServices.V1\xca\x022Google\\Cloud\\BeyondCorp\\ClientConnectorServices\\V1\xea\x026Google::Cloud::BeyondCorp::ClientConnectorServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.beyondcorp.clientconnectorservices.v1.client_connector_services_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n6com.google.cloud.beyondcorp.clientconnectorservices.v1B#ClientConnectorServicesServiceProtoP\x01Zpcloud.google.com/go/beyondcorp/clientconnectorservices/apiv1/clientconnectorservicespb;clientconnectorservicespb\xaa\x022Google.Cloud.BeyondCorp.ClientConnectorServices.V1\xca\x022Google\\Cloud\\BeyondCorp\\ClientConnectorServices\\V1\xea\x026Google::Cloud::BeyondCorp::ClientConnectorServices::V1'
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG_DESTINATIONROUTE'].fields_by_name['address']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG_DESTINATIONROUTE'].fields_by_name['address']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG_DESTINATIONROUTE'].fields_by_name['netmask']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG_DESTINATIONROUTE'].fields_by_name['netmask']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG'].fields_by_name['transport_protocol']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG'].fields_by_name['transport_protocol']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG'].fields_by_name['destination_routes']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG'].fields_by_name['destination_routes']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTCONNECTORSERVICE_EGRESS_PEEREDVPC'].fields_by_name['network_vpc']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE_EGRESS_PEEREDVPC'].fields_by_name['network_vpc']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['name']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['update_time']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['display_name']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['ingress']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['ingress']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['egress']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['egress']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['state']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICE']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICE']._serialized_options = b'\xeaA\x8e\x01\n0beyondcorp.googleapis.com/ClientConnectorService\x12Zprojects/{project}/locations/{location}/clientConnectorServices/{client_connector_service}'
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120beyondcorp.googleapis.com/ClientConnectorService'
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETCLIENTCONNECTORSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCLIENTCONNECTORSERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0beyondcorp.googleapis.com/ClientConnectorService'
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120beyondcorp.googleapis.com/ClientConnectorService'
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['client_connector_service_id']._loaded_options = None
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['client_connector_service_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['client_connector_service']._loaded_options = None
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['client_connector_service']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['client_connector_service']._loaded_options = None
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['client_connector_service']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['allow_missing']._loaded_options = None
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0beyondcorp.googleapis.com/ClientConnectorService'
    _globals['_DELETECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETECLIENTCONNECTORSERVICEREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTCONNECTORSERVICESSERVICE']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICESSERVICE']._serialized_options = b'\xcaA\x19beyondcorp.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['ListClientConnectorServices']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['ListClientConnectorServices']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=projects/*/locations/*}/clientConnectorServices'
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['GetClientConnectorService']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['GetClientConnectorService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/{name=projects/*/locations/*/clientConnectorServices/*}'
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['CreateClientConnectorService']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['CreateClientConnectorService']._serialized_options = b'\xcaAA\n\x16ClientConnectorService\x12\'ClientConnectorServiceOperationMetadata\xdaA;parent,client_connector_service,client_connector_service_id\x82\xd3\xe4\x93\x02W";/v1/{parent=projects/*/locations/*}/clientConnectorServices:\x18client_connector_service'
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['UpdateClientConnectorService']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['UpdateClientConnectorService']._serialized_options = b"\xcaAA\n\x16ClientConnectorService\x12'ClientConnectorServiceOperationMetadata\xdaA$client_connector_service,update_mask\x82\xd3\xe4\x93\x02p2T/v1/{client_connector_service.name=projects/*/locations/*/clientConnectorServices/*}:\x18client_connector_service"
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['DeleteClientConnectorService']._loaded_options = None
    _globals['_CLIENTCONNECTORSERVICESSERVICE'].methods_by_name['DeleteClientConnectorService']._serialized_options = b"\xcaA@\n\x15google.protobuf.Empty\x12'ClientConnectorServiceOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1/{name=projects/*/locations/*/clientConnectorServices/*}"
    _globals['_CLIENTCONNECTORSERVICE']._serialized_start = 366
    _globals['_CLIENTCONNECTORSERVICE']._serialized_end = 1866
    _globals['_CLIENTCONNECTORSERVICE_INGRESS']._serialized_start = 859
    _globals['_CLIENTCONNECTORSERVICE_INGRESS']._serialized_end = 1424
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG']._serialized_start = 980
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG']._serialized_end = 1406
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG_DESTINATIONROUTE']._serialized_start = 1278
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG_DESTINATIONROUTE']._serialized_end = 1340
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG_TRANSPORTPROTOCOL']._serialized_start = 1342
    _globals['_CLIENTCONNECTORSERVICE_INGRESS_CONFIG_TRANSPORTPROTOCOL']._serialized_end = 1406
    _globals['_CLIENTCONNECTORSERVICE_EGRESS']._serialized_start = 1427
    _globals['_CLIENTCONNECTORSERVICE_EGRESS']._serialized_end = 1609
    _globals['_CLIENTCONNECTORSERVICE_EGRESS_PEEREDVPC']._serialized_start = 1552
    _globals['_CLIENTCONNECTORSERVICE_EGRESS_PEEREDVPC']._serialized_end = 1589
    _globals['_CLIENTCONNECTORSERVICE_STATE']._serialized_start = 1611
    _globals['_CLIENTCONNECTORSERVICE_STATE']._serialized_end = 1717
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST']._serialized_start = 1869
    _globals['_LISTCLIENTCONNECTORSERVICESREQUEST']._serialized_end = 2072
    _globals['_LISTCLIENTCONNECTORSERVICESRESPONSE']._serialized_start = 2075
    _globals['_LISTCLIENTCONNECTORSERVICESRESPONSE']._serialized_end = 2269
    _globals['_GETCLIENTCONNECTORSERVICEREQUEST']._serialized_start = 2271
    _globals['_GETCLIENTCONNECTORSERVICEREQUEST']._serialized_end = 2377
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST']._serialized_start = 2380
    _globals['_CREATECLIENTCONNECTORSERVICEREQUEST']._serialized_end = 2701
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST']._serialized_start = 2704
    _globals['_UPDATECLIENTCONNECTORSERVICEREQUEST']._serialized_end = 2991
    _globals['_DELETECLIENTCONNECTORSERVICEREQUEST']._serialized_start = 2994
    _globals['_DELETECLIENTCONNECTORSERVICEREQUEST']._serialized_end = 3156
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA']._serialized_start = 3159
    _globals['_CLIENTCONNECTORSERVICEOPERATIONMETADATA']._serialized_end = 3437
    _globals['_CLIENTCONNECTORSERVICESSERVICE']._serialized_start = 3440
    _globals['_CLIENTCONNECTORSERVICESSERVICE']._serialized_end = 5163