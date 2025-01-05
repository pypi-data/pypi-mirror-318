"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/network.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/baremetalsolution/v2/network.proto\x12!google.cloud.baremetalsolution.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xa8\x07\n\x07Network\x12\x11\n\x04name\x18\x05 \x01(\tB\x03\xe0A\x03\x12\n\n\x02id\x18\n \x01(\t\x12=\n\x04type\x18\x02 \x01(\x0e2/.google.cloud.baremetalsolution.v2.Network.Type\x12\x12\n\nip_address\x18\x03 \x01(\t\x12\x13\n\x0bmac_address\x18\x04 \x03(\t\x12?\n\x05state\x18\x06 \x01(\x0e20.google.cloud.baremetalsolution.v2.Network.State\x12\x0f\n\x07vlan_id\x18\x07 \x01(\t\x12\x0c\n\x04cidr\x18\x08 \x01(\t\x123\n\x03vrf\x18\t \x01(\x0b2&.google.cloud.baremetalsolution.v2.VRF\x12F\n\x06labels\x18\x0b \x03(\x0b26.google.cloud.baremetalsolution.v2.Network.LabelsEntry\x12\x15\n\rservices_cidr\x18\x0c \x01(\t\x12R\n\x0creservations\x18\r \x03(\x0b2<.google.cloud.baremetalsolution.v2.NetworkAddressReservation\x12\x10\n\x03pod\x18\x0e \x01(\tB\x03\xe0A\x03\x12O\n\x0cmount_points\x18\x0f \x03(\x0b24.google.cloud.baremetalsolution.v2.NetworkMountPointB\x03\xe0A\x04\x12\x1c\n\x14jumbo_frames_enabled\x18\x10 \x01(\x08\x12\x17\n\ngateway_ip\x18\x11 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"5\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CLIENT\x10\x01\x12\x0b\n\x07PRIVATE\x10\x02"c\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0f\n\x0bPROVISIONED\x10\x02\x12\x12\n\x0eDEPROVISIONING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04:i\xeaAf\n(baremetalsolution.googleapis.com/Network\x12:projects/{project}/locations/{location}/networks/{network}"U\n\x19NetworkAddressReservation\x12\x15\n\rstart_address\x18\x01 \x01(\t\x12\x13\n\x0bend_address\x18\x02 \x01(\t\x12\x0c\n\x04note\x18\x03 \x01(\t"\xe5\x04\n\x03VRF\x12\x0c\n\x04name\x18\x01 \x01(\t\x12;\n\x05state\x18\x05 \x01(\x0e2,.google.cloud.baremetalsolution.v2.VRF.State\x12D\n\nqos_policy\x18\x06 \x01(\x0b20.google.cloud.baremetalsolution.v2.VRF.QosPolicy\x12O\n\x10vlan_attachments\x18\x07 \x03(\x0b25.google.cloud.baremetalsolution.v2.VRF.VlanAttachment\x1a#\n\tQosPolicy\x12\x16\n\x0ebandwidth_gbps\x18\x01 \x01(\x01\x1a\x93\x02\n\x0eVlanAttachment\x12\x14\n\x0cpeer_vlan_id\x18\x01 \x01(\x03\x12\x0f\n\x07peer_ip\x18\x02 \x01(\t\x12\x11\n\trouter_ip\x18\x03 \x01(\t\x12\x18\n\x0bpairing_key\x18\x04 \x01(\tB\x03\xe0A\x04\x12D\n\nqos_policy\x18\x05 \x01(\x0b20.google.cloud.baremetalsolution.v2.VRF.QosPolicy\x12\x0f\n\x02id\x18\x06 \x01(\tB\x03\xe0A\x05\x12V\n\x17interconnect_attachment\x18\x07 \x01(\tB5\xe0A\x01\xfaA/\n-compute.googleapis.com/InterconnectAttachment"A\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0f\n\x0bPROVISIONED\x10\x02"\xdb\x02\n\x10LogicalInterface\x12o\n\x1alogical_network_interfaces\x18\x01 \x03(\x0b2K.google.cloud.baremetalsolution.v2.LogicalInterface.LogicalNetworkInterface\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1b\n\x0finterface_index\x18\x03 \x01(\x05B\x02\x18\x01\x1a\xaa\x01\n\x17LogicalNetworkInterface\x12\x0f\n\x07network\x18\x01 \x01(\t\x12\x12\n\nip_address\x18\x02 \x01(\t\x12\x17\n\x0fdefault_gateway\x18\x03 \x01(\x08\x12E\n\x0cnetwork_type\x18\x04 \x01(\x0e2/.google.cloud.baremetalsolution.v2.Network.Type\x12\n\n\x02id\x18\x05 \x01(\t"S\n\x11GetNetworkRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(baremetalsolution.googleapis.com/Network"\x87\x01\n\x13ListNetworksRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"\x82\x01\n\x14ListNetworksResponse\x12<\n\x08networks\x18\x01 \x03(\x0b2*.google.cloud.baremetalsolution.v2.Network\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x89\x01\n\x14UpdateNetworkRequest\x12@\n\x07network\x18\x01 \x01(\x0b2*.google.cloud.baremetalsolution.v2.NetworkB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"]\n\x0cNetworkUsage\x12;\n\x07network\x18\x01 \x01(\x0b2*.google.cloud.baremetalsolution.v2.Network\x12\x10\n\x08used_ips\x18\x02 \x03(\t"V\n\x17ListNetworkUsageRequest\x12;\n\x08location\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location"]\n\x18ListNetworkUsageResponse\x12A\n\x08networks\x18\x01 \x03(\x0b2/.google.cloud.baremetalsolution.v2.NetworkUsage"\x9d\x01\n\x11NetworkMountPoint\x12@\n\x08instance\x18\x01 \x01(\tB.\xfaA+\n)baremetalsolution.googleapis.com/Instance\x12\x19\n\x11logical_interface\x18\x02 \x01(\t\x12\x17\n\x0fdefault_gateway\x18\x03 \x01(\x08\x12\x12\n\nip_address\x18\x04 \x01(\t"s\n\x14RenameNetworkRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(baremetalsolution.googleapis.com/Network\x12\x1b\n\x0enew_network_id\x18\x02 \x01(\tB\x03\xe0A\x02B\x85\x03\n%com.google.cloud.baremetalsolution.v2B\x0cNetworkProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2\xeaA\x86\x01\n-compute.googleapis.com/InterconnectAttachment\x12Uprojects/{project}/regions/{region}/interconnectAttachments/{interconnect_attachment}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.network_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\x0cNetworkProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2\xeaA\x86\x01\n-compute.googleapis.com/InterconnectAttachment\x12Uprojects/{project}/regions/{region}/interconnectAttachments/{interconnect_attachment}'
    _globals['_NETWORK_LABELSENTRY']._loaded_options = None
    _globals['_NETWORK_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NETWORK'].fields_by_name['name']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORK'].fields_by_name['pod']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['pod']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORK'].fields_by_name['mount_points']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['mount_points']._serialized_options = b'\xe0A\x04'
    _globals['_NETWORK'].fields_by_name['gateway_ip']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['gateway_ip']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORK']._loaded_options = None
    _globals['_NETWORK']._serialized_options = b'\xeaAf\n(baremetalsolution.googleapis.com/Network\x12:projects/{project}/locations/{location}/networks/{network}'
    _globals['_VRF_VLANATTACHMENT'].fields_by_name['pairing_key']._loaded_options = None
    _globals['_VRF_VLANATTACHMENT'].fields_by_name['pairing_key']._serialized_options = b'\xe0A\x04'
    _globals['_VRF_VLANATTACHMENT'].fields_by_name['id']._loaded_options = None
    _globals['_VRF_VLANATTACHMENT'].fields_by_name['id']._serialized_options = b'\xe0A\x05'
    _globals['_VRF_VLANATTACHMENT'].fields_by_name['interconnect_attachment']._loaded_options = None
    _globals['_VRF_VLANATTACHMENT'].fields_by_name['interconnect_attachment']._serialized_options = b'\xe0A\x01\xfaA/\n-compute.googleapis.com/InterconnectAttachment'
    _globals['_LOGICALINTERFACE'].fields_by_name['interface_index']._loaded_options = None
    _globals['_LOGICALINTERFACE'].fields_by_name['interface_index']._serialized_options = b'\x18\x01'
    _globals['_GETNETWORKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNETWORKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(baremetalsolution.googleapis.com/Network'
    _globals['_LISTNETWORKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNETWORKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATENETWORKREQUEST'].fields_by_name['network']._loaded_options = None
    _globals['_UPDATENETWORKREQUEST'].fields_by_name['network']._serialized_options = b'\xe0A\x02'
    _globals['_LISTNETWORKUSAGEREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_LISTNETWORKUSAGEREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_NETWORKMOUNTPOINT'].fields_by_name['instance']._loaded_options = None
    _globals['_NETWORKMOUNTPOINT'].fields_by_name['instance']._serialized_options = b'\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_RENAMENETWORKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENAMENETWORKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(baremetalsolution.googleapis.com/Network'
    _globals['_RENAMENETWORKREQUEST'].fields_by_name['new_network_id']._loaded_options = None
    _globals['_RENAMENETWORKREQUEST'].fields_by_name['new_network_id']._serialized_options = b'\xe0A\x02'
    _globals['_NETWORK']._serialized_start = 181
    _globals['_NETWORK']._serialized_end = 1117
    _globals['_NETWORK_LABELSENTRY']._serialized_start = 809
    _globals['_NETWORK_LABELSENTRY']._serialized_end = 854
    _globals['_NETWORK_TYPE']._serialized_start = 856
    _globals['_NETWORK_TYPE']._serialized_end = 909
    _globals['_NETWORK_STATE']._serialized_start = 911
    _globals['_NETWORK_STATE']._serialized_end = 1010
    _globals['_NETWORKADDRESSRESERVATION']._serialized_start = 1119
    _globals['_NETWORKADDRESSRESERVATION']._serialized_end = 1204
    _globals['_VRF']._serialized_start = 1207
    _globals['_VRF']._serialized_end = 1820
    _globals['_VRF_QOSPOLICY']._serialized_start = 1440
    _globals['_VRF_QOSPOLICY']._serialized_end = 1475
    _globals['_VRF_VLANATTACHMENT']._serialized_start = 1478
    _globals['_VRF_VLANATTACHMENT']._serialized_end = 1753
    _globals['_VRF_STATE']._serialized_start = 911
    _globals['_VRF_STATE']._serialized_end = 976
    _globals['_LOGICALINTERFACE']._serialized_start = 1823
    _globals['_LOGICALINTERFACE']._serialized_end = 2170
    _globals['_LOGICALINTERFACE_LOGICALNETWORKINTERFACE']._serialized_start = 2000
    _globals['_LOGICALINTERFACE_LOGICALNETWORKINTERFACE']._serialized_end = 2170
    _globals['_GETNETWORKREQUEST']._serialized_start = 2172
    _globals['_GETNETWORKREQUEST']._serialized_end = 2255
    _globals['_LISTNETWORKSREQUEST']._serialized_start = 2258
    _globals['_LISTNETWORKSREQUEST']._serialized_end = 2393
    _globals['_LISTNETWORKSRESPONSE']._serialized_start = 2396
    _globals['_LISTNETWORKSRESPONSE']._serialized_end = 2526
    _globals['_UPDATENETWORKREQUEST']._serialized_start = 2529
    _globals['_UPDATENETWORKREQUEST']._serialized_end = 2666
    _globals['_NETWORKUSAGE']._serialized_start = 2668
    _globals['_NETWORKUSAGE']._serialized_end = 2761
    _globals['_LISTNETWORKUSAGEREQUEST']._serialized_start = 2763
    _globals['_LISTNETWORKUSAGEREQUEST']._serialized_end = 2849
    _globals['_LISTNETWORKUSAGERESPONSE']._serialized_start = 2851
    _globals['_LISTNETWORKUSAGERESPONSE']._serialized_end = 2944
    _globals['_NETWORKMOUNTPOINT']._serialized_start = 2947
    _globals['_NETWORKMOUNTPOINT']._serialized_end = 3104
    _globals['_RENAMENETWORKREQUEST']._serialized_start = 3106
    _globals['_RENAMENETWORKREQUEST']._serialized_end = 3221