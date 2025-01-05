"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networkconnectivity/v1alpha1/hub.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/networkconnectivity/v1alpha1/hub.proto\x12)google.cloud.networkconnectivity.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x87\x04\n\x03Hub\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12J\n\x06labels\x18\x04 \x03(\x0b2:.google.cloud.networkconnectivity.v1alpha1.Hub.LabelsEntry\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12@\n\x06spokes\x18\x06 \x03(\tB0\xe0A\x03\xfaA*\n(networkconnectivity.googleapis.com/Spoke\x12\x16\n\tunique_id\x18\x08 \x01(\tB\x03\xe0A\x03\x12D\n\x05state\x18\t \x01(\x0e20.google.cloud.networkconnectivity.v1alpha1.StateB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:[\xeaAX\n&networkconnectivity.googleapis.com/Hub\x12.projects/{project}/locations/global/hubs/{hub}"\x9c\x06\n\x05Spoke\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12L\n\x06labels\x18\x04 \x03(\x0b2<.google.cloud.networkconnectivity.v1alpha1.Spoke.LabelsEntry\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x128\n\x03hub\x18\x06 \x01(\tB+\xfaA(\n&networkconnectivity.googleapis.com/Hub\x12A\n\x12linked_vpn_tunnels\x18\x0c \x03(\tB%\xfaA"\n compute.googleapis.com/VpnTunnel\x12[\n\x1flinked_interconnect_attachments\x18\r \x03(\tB2\xfaA/\n-compute.googleapis.com/InterconnectAttachment\x12m\n!linked_router_appliance_instances\x18\x0e \x03(\x0b2B.google.cloud.networkconnectivity.v1alpha1.RouterApplianceInstance\x12\x16\n\tunique_id\x18\x0b \x01(\tB\x03\xe0A\x03\x12D\n\x05state\x18\x0f \x01(\x0e20.google.cloud.networkconnectivity.v1alpha1.StateB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:e\xeaAb\n(networkconnectivity.googleapis.com/Spoke\x126projects/{project}/locations/{location}/spokes/{spoke}"\x95\x01\n\x0fListHubsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"~\n\x10ListHubsResponse\x12<\n\x04hubs\x18\x01 \x03(\x0b2..google.cloud.networkconnectivity.v1alpha1.Hub\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"M\n\rGetHubRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&networkconnectivity.googleapis.com/Hub"\xbd\x01\n\x10CreateHubRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06hub_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12@\n\x03hub\x18\x03 \x01(\x0b2..google.cloud.networkconnectivity.v1alpha1.HubB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa3\x01\n\x10UpdateHubRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12@\n\x03hub\x18\x02 \x01(\x0b2..google.cloud.networkconnectivity.v1alpha1.HubB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"i\n\x10DeleteHubRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&networkconnectivity.googleapis.com/Hub\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x97\x01\n\x11ListSpokesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x84\x01\n\x12ListSpokesResponse\x12@\n\x06spokes\x18\x01 \x03(\x0b20.google.cloud.networkconnectivity.v1alpha1.Spoke\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"Q\n\x0fGetSpokeRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(networkconnectivity.googleapis.com/Spoke"\xc5\x01\n\x12CreateSpokeRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x15\n\x08spoke_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12D\n\x05spoke\x18\x03 \x01(\x0b20.google.cloud.networkconnectivity.v1alpha1.SpokeB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa9\x01\n\x12UpdateSpokeRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12D\n\x05spoke\x18\x02 \x01(\x0b20.google.cloud.networkconnectivity.v1alpha1.SpokeB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"m\n\x12DeleteSpokeRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(networkconnectivity.googleapis.com/Spoke\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x8b\x01\n\x17RouterApplianceInstance\x12=\n\x0fvirtual_machine\x18\x01 \x01(\tB$\xfaA!\n\x1fcompute.googleapis.com/Instance\x12\x12\n\nip_address\x18\x03 \x01(\t\x12\x1d\n\x11network_interface\x18\x02 \x01(\tB\x02\x18\x01*F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08DELETING\x10\x032\xad\x11\n\nHubService\x12\xc9\x01\n\x08ListHubs\x12:.google.cloud.networkconnectivity.v1alpha1.ListHubsRequest\x1a;.google.cloud.networkconnectivity.v1alpha1.ListHubsResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1alpha1/{parent=projects/*/locations/global}/hubs\x12\xb6\x01\n\x06GetHub\x128.google.cloud.networkconnectivity.v1alpha1.GetHubRequest\x1a..google.cloud.networkconnectivity.v1alpha1.Hub"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1alpha1/{name=projects/*/locations/global/hubs/*}\x12\xd8\x01\n\tCreateHub\x12;.google.cloud.networkconnectivity.v1alpha1.CreateHubRequest\x1a\x1d.google.longrunning.Operation"o\xcaA\x18\n\x03Hub\x12\x11OperationMetadata\xdaA\x11parent,hub,hub_id\x82\xd3\xe4\x93\x02:"3/v1alpha1/{parent=projects/*/locations/global}/hubs:\x03hub\x12\xda\x01\n\tUpdateHub\x12;.google.cloud.networkconnectivity.v1alpha1.UpdateHubRequest\x1a\x1d.google.longrunning.Operation"q\xcaA\x18\n\x03Hub\x12\x11OperationMetadata\xdaA\x0fhub,update_mask\x82\xd3\xe4\x93\x02>27/v1alpha1/{hub.name=projects/*/locations/global/hubs/*}:\x03hub\x12\xd8\x01\n\tDeleteHub\x12;.google.cloud.networkconnectivity.v1alpha1.DeleteHubRequest\x1a\x1d.google.longrunning.Operation"o\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1alpha1/{name=projects/*/locations/global/hubs/*}\x12\xcc\x01\n\nListSpokes\x12<.google.cloud.networkconnectivity.v1alpha1.ListSpokesRequest\x1a=.google.cloud.networkconnectivity.v1alpha1.ListSpokesResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1alpha1/{parent=projects/*/locations/*}/spokes\x12\xb9\x01\n\x08GetSpoke\x12:.google.cloud.networkconnectivity.v1alpha1.GetSpokeRequest\x1a0.google.cloud.networkconnectivity.v1alpha1.Spoke"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1alpha1/{name=projects/*/locations/*/spokes/*}\x12\xe1\x01\n\x0bCreateSpoke\x12=.google.cloud.networkconnectivity.v1alpha1.CreateSpokeRequest\x1a\x1d.google.longrunning.Operation"t\xcaA\x1a\n\x05Spoke\x12\x11OperationMetadata\xdaA\x15parent,spoke,spoke_id\x82\xd3\xe4\x93\x029"0/v1alpha1/{parent=projects/*/locations/*}/spokes:\x05spoke\x12\xe3\x01\n\x0bUpdateSpoke\x12=.google.cloud.networkconnectivity.v1alpha1.UpdateSpokeRequest\x1a\x1d.google.longrunning.Operation"v\xcaA\x1a\n\x05Spoke\x12\x11OperationMetadata\xdaA\x11spoke,update_mask\x82\xd3\xe4\x93\x02?26/v1alpha1/{spoke.name=projects/*/locations/*/spokes/*}:\x05spoke\x12\xd9\x01\n\x0bDeleteSpoke\x12=.google.cloud.networkconnectivity.v1alpha1.DeleteSpokeRequest\x1a\x1d.google.longrunning.Operation"l\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1alpha1/{name=projects/*/locations/*/spokes/*}\x1aV\xcaA"networkconnectivity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdd\x04\n-com.google.cloud.networkconnectivity.v1alpha1B\x08HubProtoP\x01Z_cloud.google.com/go/networkconnectivity/apiv1alpha1/networkconnectivitypb;networkconnectivitypb\xaa\x02)Google.Cloud.NetworkConnectivity.V1Alpha1\xca\x02)Google\\Cloud\\NetworkConnectivity\\V1alpha1\xea\x02,Google::Cloud::NetworkConnectivity::V1alpha1\xeaA`\n compute.googleapis.com/VpnTunnel\x12<projects/{project}/regions/{region}/vpnTunnels/{resource_id}\xeaAz\n-compute.googleapis.com/InterconnectAttachment\x12Iprojects/{project}/regions/{region}/interconnectAttachments/{resource_id}\xeaAW\n\x1fcompute.googleapis.com/Instance\x124projects/{project}/zones/{zone}/instances/{instance}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkconnectivity.v1alpha1.hub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.networkconnectivity.v1alpha1B\x08HubProtoP\x01Z_cloud.google.com/go/networkconnectivity/apiv1alpha1/networkconnectivitypb;networkconnectivitypb\xaa\x02)Google.Cloud.NetworkConnectivity.V1Alpha1\xca\x02)Google\\Cloud\\NetworkConnectivity\\V1alpha1\xea\x02,Google::Cloud::NetworkConnectivity::V1alpha1\xeaA`\n compute.googleapis.com/VpnTunnel\x12<projects/{project}/regions/{region}/vpnTunnels/{resource_id}\xeaAz\n-compute.googleapis.com/InterconnectAttachment\x12Iprojects/{project}/regions/{region}/interconnectAttachments/{resource_id}\xeaAW\n\x1fcompute.googleapis.com/Instance\x124projects/{project}/zones/{zone}/instances/{instance}'
    _globals['_HUB_LABELSENTRY']._loaded_options = None
    _globals['_HUB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_HUB'].fields_by_name['name']._loaded_options = None
    _globals['_HUB'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_HUB'].fields_by_name['spokes']._loaded_options = None
    _globals['_HUB'].fields_by_name['spokes']._serialized_options = b'\xe0A\x03\xfaA*\n(networkconnectivity.googleapis.com/Spoke'
    _globals['_HUB'].fields_by_name['unique_id']._loaded_options = None
    _globals['_HUB'].fields_by_name['unique_id']._serialized_options = b'\xe0A\x03'
    _globals['_HUB'].fields_by_name['state']._loaded_options = None
    _globals['_HUB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_HUB']._loaded_options = None
    _globals['_HUB']._serialized_options = b'\xeaAX\n&networkconnectivity.googleapis.com/Hub\x12.projects/{project}/locations/global/hubs/{hub}'
    _globals['_SPOKE_LABELSENTRY']._loaded_options = None
    _globals['_SPOKE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SPOKE'].fields_by_name['name']._loaded_options = None
    _globals['_SPOKE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SPOKE'].fields_by_name['hub']._loaded_options = None
    _globals['_SPOKE'].fields_by_name['hub']._serialized_options = b'\xfaA(\n&networkconnectivity.googleapis.com/Hub'
    _globals['_SPOKE'].fields_by_name['linked_vpn_tunnels']._loaded_options = None
    _globals['_SPOKE'].fields_by_name['linked_vpn_tunnels']._serialized_options = b'\xfaA"\n compute.googleapis.com/VpnTunnel'
    _globals['_SPOKE'].fields_by_name['linked_interconnect_attachments']._loaded_options = None
    _globals['_SPOKE'].fields_by_name['linked_interconnect_attachments']._serialized_options = b'\xfaA/\n-compute.googleapis.com/InterconnectAttachment'
    _globals['_SPOKE'].fields_by_name['unique_id']._loaded_options = None
    _globals['_SPOKE'].fields_by_name['unique_id']._serialized_options = b'\xe0A\x03'
    _globals['_SPOKE'].fields_by_name['state']._loaded_options = None
    _globals['_SPOKE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SPOKE']._loaded_options = None
    _globals['_SPOKE']._serialized_options = b'\xeaAb\n(networkconnectivity.googleapis.com/Spoke\x126projects/{project}/locations/{location}/spokes/{spoke}'
    _globals['_LISTHUBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTHUBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETHUBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETHUBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&networkconnectivity.googleapis.com/Hub'
    _globals['_CREATEHUBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEHUBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEHUBREQUEST'].fields_by_name['hub_id']._loaded_options = None
    _globals['_CREATEHUBREQUEST'].fields_by_name['hub_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEHUBREQUEST'].fields_by_name['hub']._loaded_options = None
    _globals['_CREATEHUBREQUEST'].fields_by_name['hub']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEHUBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEHUBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEHUBREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEHUBREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEHUBREQUEST'].fields_by_name['hub']._loaded_options = None
    _globals['_UPDATEHUBREQUEST'].fields_by_name['hub']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEHUBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEHUBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEHUBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEHUBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&networkconnectivity.googleapis.com/Hub'
    _globals['_DELETEHUBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEHUBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSPOKESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSPOKESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETSPOKEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSPOKEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(networkconnectivity.googleapis.com/Spoke'
    _globals['_CREATESPOKEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESPOKEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATESPOKEREQUEST'].fields_by_name['spoke_id']._loaded_options = None
    _globals['_CREATESPOKEREQUEST'].fields_by_name['spoke_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATESPOKEREQUEST'].fields_by_name['spoke']._loaded_options = None
    _globals['_CREATESPOKEREQUEST'].fields_by_name['spoke']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESPOKEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATESPOKEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESPOKEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESPOKEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESPOKEREQUEST'].fields_by_name['spoke']._loaded_options = None
    _globals['_UPDATESPOKEREQUEST'].fields_by_name['spoke']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESPOKEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATESPOKEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESPOKEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESPOKEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(networkconnectivity.googleapis.com/Spoke'
    _globals['_DELETESPOKEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETESPOKEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTERAPPLIANCEINSTANCE'].fields_by_name['virtual_machine']._loaded_options = None
    _globals['_ROUTERAPPLIANCEINSTANCE'].fields_by_name['virtual_machine']._serialized_options = b'\xfaA!\n\x1fcompute.googleapis.com/Instance'
    _globals['_ROUTERAPPLIANCEINSTANCE'].fields_by_name['network_interface']._loaded_options = None
    _globals['_ROUTERAPPLIANCEINSTANCE'].fields_by_name['network_interface']._serialized_options = b'\x18\x01'
    _globals['_HUBSERVICE']._loaded_options = None
    _globals['_HUBSERVICE']._serialized_options = b'\xcaA"networkconnectivity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_HUBSERVICE'].methods_by_name['ListHubs']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['ListHubs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1alpha1/{parent=projects/*/locations/global}/hubs'
    _globals['_HUBSERVICE'].methods_by_name['GetHub']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['GetHub']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1alpha1/{name=projects/*/locations/global/hubs/*}'
    _globals['_HUBSERVICE'].methods_by_name['CreateHub']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['CreateHub']._serialized_options = b'\xcaA\x18\n\x03Hub\x12\x11OperationMetadata\xdaA\x11parent,hub,hub_id\x82\xd3\xe4\x93\x02:"3/v1alpha1/{parent=projects/*/locations/global}/hubs:\x03hub'
    _globals['_HUBSERVICE'].methods_by_name['UpdateHub']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['UpdateHub']._serialized_options = b'\xcaA\x18\n\x03Hub\x12\x11OperationMetadata\xdaA\x0fhub,update_mask\x82\xd3\xe4\x93\x02>27/v1alpha1/{hub.name=projects/*/locations/global/hubs/*}:\x03hub'
    _globals['_HUBSERVICE'].methods_by_name['DeleteHub']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['DeleteHub']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1alpha1/{name=projects/*/locations/global/hubs/*}'
    _globals['_HUBSERVICE'].methods_by_name['ListSpokes']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['ListSpokes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1alpha1/{parent=projects/*/locations/*}/spokes'
    _globals['_HUBSERVICE'].methods_by_name['GetSpoke']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['GetSpoke']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1alpha1/{name=projects/*/locations/*/spokes/*}'
    _globals['_HUBSERVICE'].methods_by_name['CreateSpoke']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['CreateSpoke']._serialized_options = b'\xcaA\x1a\n\x05Spoke\x12\x11OperationMetadata\xdaA\x15parent,spoke,spoke_id\x82\xd3\xe4\x93\x029"0/v1alpha1/{parent=projects/*/locations/*}/spokes:\x05spoke'
    _globals['_HUBSERVICE'].methods_by_name['UpdateSpoke']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['UpdateSpoke']._serialized_options = b'\xcaA\x1a\n\x05Spoke\x12\x11OperationMetadata\xdaA\x11spoke,update_mask\x82\xd3\xe4\x93\x02?26/v1alpha1/{spoke.name=projects/*/locations/*/spokes/*}:\x05spoke'
    _globals['_HUBSERVICE'].methods_by_name['DeleteSpoke']._loaded_options = None
    _globals['_HUBSERVICE'].methods_by_name['DeleteSpoke']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1alpha1/{name=projects/*/locations/*/spokes/*}'
    _globals['_STATE']._serialized_start = 3459
    _globals['_STATE']._serialized_end = 3529
    _globals['_HUB']._serialized_start = 318
    _globals['_HUB']._serialized_end = 837
    _globals['_HUB_LABELSENTRY']._serialized_start = 699
    _globals['_HUB_LABELSENTRY']._serialized_end = 744
    _globals['_SPOKE']._serialized_start = 840
    _globals['_SPOKE']._serialized_end = 1636
    _globals['_SPOKE_LABELSENTRY']._serialized_start = 699
    _globals['_SPOKE_LABELSENTRY']._serialized_end = 744
    _globals['_LISTHUBSREQUEST']._serialized_start = 1639
    _globals['_LISTHUBSREQUEST']._serialized_end = 1788
    _globals['_LISTHUBSRESPONSE']._serialized_start = 1790
    _globals['_LISTHUBSRESPONSE']._serialized_end = 1916
    _globals['_GETHUBREQUEST']._serialized_start = 1918
    _globals['_GETHUBREQUEST']._serialized_end = 1995
    _globals['_CREATEHUBREQUEST']._serialized_start = 1998
    _globals['_CREATEHUBREQUEST']._serialized_end = 2187
    _globals['_UPDATEHUBREQUEST']._serialized_start = 2190
    _globals['_UPDATEHUBREQUEST']._serialized_end = 2353
    _globals['_DELETEHUBREQUEST']._serialized_start = 2355
    _globals['_DELETEHUBREQUEST']._serialized_end = 2460
    _globals['_LISTSPOKESREQUEST']._serialized_start = 2463
    _globals['_LISTSPOKESREQUEST']._serialized_end = 2614
    _globals['_LISTSPOKESRESPONSE']._serialized_start = 2617
    _globals['_LISTSPOKESRESPONSE']._serialized_end = 2749
    _globals['_GETSPOKEREQUEST']._serialized_start = 2751
    _globals['_GETSPOKEREQUEST']._serialized_end = 2832
    _globals['_CREATESPOKEREQUEST']._serialized_start = 2835
    _globals['_CREATESPOKEREQUEST']._serialized_end = 3032
    _globals['_UPDATESPOKEREQUEST']._serialized_start = 3035
    _globals['_UPDATESPOKEREQUEST']._serialized_end = 3204
    _globals['_DELETESPOKEREQUEST']._serialized_start = 3206
    _globals['_DELETESPOKEREQUEST']._serialized_end = 3315
    _globals['_ROUTERAPPLIANCEINSTANCE']._serialized_start = 3318
    _globals['_ROUTERAPPLIANCEINSTANCE']._serialized_end = 3457
    _globals['_HUBSERVICE']._serialized_start = 3532
    _globals['_HUBSERVICE']._serialized_end = 5753