"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/edgecontainer/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.edgecontainer.v1 import resources_pb2 as google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/edgecontainer/v1/service.proto\x12\x1dgoogle.cloud.edgecontainer.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/edgecontainer/v1/resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x88\x03\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t\x12\x16\n\x0estatus_message\x18\x05 \x01(\t\x12\x1e\n\x16requested_cancellation\x18\x06 \x01(\x08\x12\x13\n\x0bapi_version\x18\x07 \x01(\t\x12\x10\n\x08warnings\x18\x08 \x03(\t\x12T\n\rstatus_reason\x18\t \x01(\x0e2=.google.cloud.edgecontainer.v1.OperationMetadata.StatusReason"A\n\x0cStatusReason\x12\x1d\n\x19STATUS_REASON_UNSPECIFIED\x10\x00\x12\x12\n\x0eUPGRADE_PAUSED\x10\x01"\x9c\x01\n\x13ListClustersRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$edgecontainer.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"~\n\x14ListClustersResponse\x128\n\x08clusters\x18\x01 \x03(\x0b2&.google.cloud.edgecontainer.v1.Cluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"O\n\x11GetClusterRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster"\xbf\x01\n\x14CreateClusterRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$edgecontainer.googleapis.com/Cluster\x12\x17\n\ncluster_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12<\n\x07cluster\x18\x03 \x01(\x0b2&.google.cloud.edgecontainer.v1.ClusterB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x04 \x01(\t"\x94\x01\n\x14UpdateClusterRequest\x12/\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMask\x127\n\x07cluster\x18\x02 \x01(\x0b2&.google.cloud.edgecontainer.v1.Cluster\x12\x12\n\nrequest_id\x18\x03 \x01(\t"\x8c\x02\n\x15UpgradeClusterRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster\x12\x1b\n\x0etarget_version\x18\x02 \x01(\tB\x03\xe0A\x02\x12O\n\x08schedule\x18\x03 \x01(\x0e2=.google.cloud.edgecontainer.v1.UpgradeClusterRequest.Schedule\x12\x12\n\nrequest_id\x18\x04 \x01(\t"5\n\x08Schedule\x12\x18\n\x14SCHEDULE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIMMEDIATELY\x10\x01"f\n\x14DeleteClusterRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster\x12\x12\n\nrequest_id\x18\x02 \x01(\t"[\n\x1aGenerateAccessTokenRequest\x12=\n\x07cluster\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster"n\n\x1bGenerateAccessTokenResponse\x12\x19\n\x0caccess_token\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"a\n GenerateOfflineCredentialRequest\x12=\n\x07cluster\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster"\xa9\x01\n!GenerateOfflineCredentialResponse\x12\x1f\n\x12client_certificate\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x17\n\nclient_key\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07user_id\x18\x03 \x01(\tB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x9e\x01\n\x14ListNodePoolsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%edgecontainer.googleapis.com/NodePool\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x82\x01\n\x15ListNodePoolsResponse\x12;\n\nnode_pools\x18\x01 \x03(\x0b2\'.google.cloud.edgecontainer.v1.NodePool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"Q\n\x12GetNodePoolRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%edgecontainer.googleapis.com/NodePool"\xc6\x01\n\x15CreateNodePoolRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%edgecontainer.googleapis.com/NodePool\x12\x19\n\x0cnode_pool_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12?\n\tnode_pool\x18\x03 \x01(\x0b2\'.google.cloud.edgecontainer.v1.NodePoolB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x04 \x01(\t"\x98\x01\n\x15UpdateNodePoolRequest\x12/\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12:\n\tnode_pool\x18\x02 \x01(\x0b2\'.google.cloud.edgecontainer.v1.NodePool\x12\x12\n\nrequest_id\x18\x03 \x01(\t"h\n\x15DeleteNodePoolRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%edgecontainer.googleapis.com/NodePool\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\x9c\x01\n\x13ListMachinesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$edgecontainer.googleapis.com/Machine\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"~\n\x14ListMachinesResponse\x128\n\x08machines\x18\x01 \x03(\x0b2&.google.cloud.edgecontainer.v1.Machine\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"O\n\x11GetMachineRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Machine"\xa8\x01\n\x19ListVpnConnectionsRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*edgecontainer.googleapis.com/VpnConnection\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x91\x01\n\x1aListVpnConnectionsResponse\x12E\n\x0fvpn_connections\x18\x01 \x03(\x0b2,.google.cloud.edgecontainer.v1.VpnConnection\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"[\n\x17GetVpnConnectionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*edgecontainer.googleapis.com/VpnConnection"\xdf\x01\n\x1aCreateVpnConnectionRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*edgecontainer.googleapis.com/VpnConnection\x12\x1e\n\x11vpn_connection_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12I\n\x0evpn_connection\x18\x03 \x01(\x0b2,.google.cloud.edgecontainer.v1.VpnConnectionB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x04 \x01(\t"r\n\x1aDeleteVpnConnectionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*edgecontainer.googleapis.com/VpnConnection\x12\x12\n\nrequest_id\x18\x02 \x01(\t"Q\n\x16GetServerConfigRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location2\xfb!\n\rEdgeContainer\x12\xb6\x01\n\x0cListClusters\x122.google.cloud.edgecontainer.v1.ListClustersRequest\x1a3.google.cloud.edgecontainer.v1.ListClustersResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/clusters\x12\xa3\x01\n\nGetCluster\x120.google.cloud.edgecontainer.v1.GetClusterRequest\x1a&.google.cloud.edgecontainer.v1.Cluster";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/clusters/*}\x12\xdd\x01\n\rCreateCluster\x123.google.cloud.edgecontainer.v1.CreateClusterRequest\x1a\x1d.google.longrunning.Operation"x\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x19parent,cluster,cluster_id\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/clusters:\x07cluster\x12\xdf\x01\n\rUpdateCluster\x123.google.cloud.edgecontainer.v1.UpdateClusterRequest\x1a\x1d.google.longrunning.Operation"z\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x13cluster,update_mask\x82\xd3\xe4\x93\x02?24/v1/{cluster.name=projects/*/locations/*/clusters/*}:\x07cluster\x12\xe4\x01\n\x0eUpgradeCluster\x124.google.cloud.edgecontainer.v1.UpgradeClusterRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x1cname,target_version,schedule\x82\xd3\xe4\x93\x029"4/v1/{name=projects/*/locations/*/clusters/*}:upgrade:\x01*\x12\xcd\x01\n\rDeleteCluster\x123.google.cloud.edgecontainer.v1.DeleteClusterRequest\x1a\x1d.google.longrunning.Operation"h\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/clusters/*}\x12\xe3\x01\n\x13GenerateAccessToken\x129.google.cloud.edgecontainer.v1.GenerateAccessTokenRequest\x1a:.google.cloud.edgecontainer.v1.GenerateAccessTokenResponse"U\xdaA\x07cluster\x82\xd3\xe4\x93\x02E\x12C/v1/{cluster=projects/*/locations/*/clusters/*}:generateAccessToken\x12\xfb\x01\n\x19GenerateOfflineCredential\x12?.google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest\x1a@.google.cloud.edgecontainer.v1.GenerateOfflineCredentialResponse"[\xdaA\x07cluster\x82\xd3\xe4\x93\x02K\x12I/v1/{cluster=projects/*/locations/*/clusters/*}:generateOfflineCredential\x12\xc5\x01\n\rListNodePools\x123.google.cloud.edgecontainer.v1.ListNodePoolsRequest\x1a4.google.cloud.edgecontainer.v1.ListNodePoolsResponse"I\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/clusters/*}/nodePools\x12\xb2\x01\n\x0bGetNodePool\x121.google.cloud.edgecontainer.v1.GetNodePoolRequest\x1a\'.google.cloud.edgecontainer.v1.NodePool"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}\x12\xf3\x01\n\x0eCreateNodePool\x124.google.cloud.edgecontainer.v1.CreateNodePoolRequest\x1a\x1d.google.longrunning.Operation"\x8b\x01\xcaA\x1d\n\x08NodePool\x12\x11OperationMetadata\xdaA\x1dparent,node_pool,node_pool_id\x82\xd3\xe4\x93\x02E"8/v1/{parent=projects/*/locations/*/clusters/*}/nodePools:\tnode_pool\x12\xf5\x01\n\x0eUpdateNodePool\x124.google.cloud.edgecontainer.v1.UpdateNodePoolRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaA\x1d\n\x08NodePool\x12\x11OperationMetadata\xdaA\x15node_pool,update_mask\x82\xd3\xe4\x93\x02O2B/v1/{node_pool.name=projects/*/locations/*/clusters/*/nodePools/*}:\tnode_pool\x12\xdb\x01\n\x0eDeleteNodePool\x124.google.cloud.edgecontainer.v1.DeleteNodePoolRequest\x1a\x1d.google.longrunning.Operation"t\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}\x12\xb6\x01\n\x0cListMachines\x122.google.cloud.edgecontainer.v1.ListMachinesRequest\x1a3.google.cloud.edgecontainer.v1.ListMachinesResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/machines\x12\xa3\x01\n\nGetMachine\x120.google.cloud.edgecontainer.v1.GetMachineRequest\x1a&.google.cloud.edgecontainer.v1.Machine";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/machines/*}\x12\xce\x01\n\x12ListVpnConnections\x128.google.cloud.edgecontainer.v1.ListVpnConnectionsRequest\x1a9.google.cloud.edgecontainer.v1.ListVpnConnectionsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/vpnConnections\x12\xbb\x01\n\x10GetVpnConnection\x126.google.cloud.edgecontainer.v1.GetVpnConnectionRequest\x1a,.google.cloud.edgecontainer.v1.VpnConnection"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/vpnConnections/*}\x12\x8b\x02\n\x13CreateVpnConnection\x129.google.cloud.edgecontainer.v1.CreateVpnConnectionRequest\x1a\x1d.google.longrunning.Operation"\x99\x01\xcaA"\n\rVpnConnection\x12\x11OperationMetadata\xdaA\'parent,vpn_connection,vpn_connection_id\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/vpnConnections:\x0evpn_connection\x12\xdf\x01\n\x13DeleteVpnConnection\x129.google.cloud.edgecontainer.v1.DeleteVpnConnectionRequest\x1a\x1d.google.longrunning.Operation"n\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/vpnConnections/*}\x12\xb4\x01\n\x0fGetServerConfig\x125.google.cloud.edgecontainer.v1.GetServerConfigRequest\x1a+.google.cloud.edgecontainer.v1.ServerConfig"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*}/serverConfig\x1aP\xcaA\x1cedgecontainer.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdf\x01\n!com.google.cloud.edgecontainer.v1B\x0cServiceProtoP\x01ZGcloud.google.com/go/edgecontainer/apiv1/edgecontainerpb;edgecontainerpb\xaa\x02\x1dGoogle.Cloud.EdgeContainer.V1\xca\x02\x1dGoogle\\Cloud\\EdgeContainer\\V1\xea\x02 Google::Cloud::EdgeContainer::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.edgecontainer.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.edgecontainer.v1B\x0cServiceProtoP\x01ZGcloud.google.com/go/edgecontainer/apiv1/edgecontainerpb;edgecontainerpb\xaa\x02\x1dGoogle.Cloud.EdgeContainer.V1\xca\x02\x1dGoogle\\Cloud\\EdgeContainer\\V1\xea\x02 Google::Cloud::EdgeContainer::V1'
    _globals['_LISTCLUSTERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCLUSTERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$edgecontainer.googleapis.com/Cluster'
    _globals['_GETCLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster'
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$edgecontainer.googleapis.com/Cluster'
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['cluster']._loaded_options = None
    _globals['_CREATECLUSTERREQUEST'].fields_by_name['cluster']._serialized_options = b'\xe0A\x02'
    _globals['_UPGRADECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPGRADECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster'
    _globals['_UPGRADECLUSTERREQUEST'].fields_by_name['target_version']._loaded_options = None
    _globals['_UPGRADECLUSTERREQUEST'].fields_by_name['target_version']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster'
    _globals['_GENERATEACCESSTOKENREQUEST'].fields_by_name['cluster']._loaded_options = None
    _globals['_GENERATEACCESSTOKENREQUEST'].fields_by_name['cluster']._serialized_options = b'\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster'
    _globals['_GENERATEACCESSTOKENRESPONSE'].fields_by_name['access_token']._loaded_options = None
    _globals['_GENERATEACCESSTOKENRESPONSE'].fields_by_name['access_token']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATEACCESSTOKENRESPONSE'].fields_by_name['expire_time']._loaded_options = None
    _globals['_GENERATEACCESSTOKENRESPONSE'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATEOFFLINECREDENTIALREQUEST'].fields_by_name['cluster']._loaded_options = None
    _globals['_GENERATEOFFLINECREDENTIALREQUEST'].fields_by_name['cluster']._serialized_options = b'\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Cluster'
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE'].fields_by_name['client_certificate']._loaded_options = None
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE'].fields_by_name['client_certificate']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE'].fields_by_name['client_key']._loaded_options = None
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE'].fields_by_name['client_key']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE'].fields_by_name['user_id']._loaded_options = None
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE'].fields_by_name['user_id']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE'].fields_by_name['expire_time']._loaded_options = None
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_LISTNODEPOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNODEPOOLSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%edgecontainer.googleapis.com/NodePool"
    _globals['_GETNODEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNODEPOOLREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%edgecontainer.googleapis.com/NodePool"
    _globals['_CREATENODEPOOLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATENODEPOOLREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%edgecontainer.googleapis.com/NodePool"
    _globals['_CREATENODEPOOLREQUEST'].fields_by_name['node_pool_id']._loaded_options = None
    _globals['_CREATENODEPOOLREQUEST'].fields_by_name['node_pool_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATENODEPOOLREQUEST'].fields_by_name['node_pool']._loaded_options = None
    _globals['_CREATENODEPOOLREQUEST'].fields_by_name['node_pool']._serialized_options = b'\xe0A\x02'
    _globals['_DELETENODEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETENODEPOOLREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%edgecontainer.googleapis.com/NodePool"
    _globals['_LISTMACHINESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMACHINESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$edgecontainer.googleapis.com/Machine'
    _globals['_GETMACHINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMACHINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$edgecontainer.googleapis.com/Machine'
    _globals['_LISTVPNCONNECTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTVPNCONNECTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*edgecontainer.googleapis.com/VpnConnection'
    _globals['_GETVPNCONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETVPNCONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*edgecontainer.googleapis.com/VpnConnection'
    _globals['_CREATEVPNCONNECTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEVPNCONNECTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*edgecontainer.googleapis.com/VpnConnection'
    _globals['_CREATEVPNCONNECTIONREQUEST'].fields_by_name['vpn_connection_id']._loaded_options = None
    _globals['_CREATEVPNCONNECTIONREQUEST'].fields_by_name['vpn_connection_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEVPNCONNECTIONREQUEST'].fields_by_name['vpn_connection']._loaded_options = None
    _globals['_CREATEVPNCONNECTIONREQUEST'].fields_by_name['vpn_connection']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEVPNCONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEVPNCONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*edgecontainer.googleapis.com/VpnConnection'
    _globals['_GETSERVERCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVERCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_EDGECONTAINER']._loaded_options = None
    _globals['_EDGECONTAINER']._serialized_options = b'\xcaA\x1cedgecontainer.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_EDGECONTAINER'].methods_by_name['ListClusters']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['ListClusters']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/clusters'
    _globals['_EDGECONTAINER'].methods_by_name['GetCluster']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['GetCluster']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/clusters/*}'
    _globals['_EDGECONTAINER'].methods_by_name['CreateCluster']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['CreateCluster']._serialized_options = b'\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x19parent,cluster,cluster_id\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/clusters:\x07cluster'
    _globals['_EDGECONTAINER'].methods_by_name['UpdateCluster']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['UpdateCluster']._serialized_options = b'\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x13cluster,update_mask\x82\xd3\xe4\x93\x02?24/v1/{cluster.name=projects/*/locations/*/clusters/*}:\x07cluster'
    _globals['_EDGECONTAINER'].methods_by_name['UpgradeCluster']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['UpgradeCluster']._serialized_options = b'\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x1cname,target_version,schedule\x82\xd3\xe4\x93\x029"4/v1/{name=projects/*/locations/*/clusters/*}:upgrade:\x01*'
    _globals['_EDGECONTAINER'].methods_by_name['DeleteCluster']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['DeleteCluster']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/clusters/*}'
    _globals['_EDGECONTAINER'].methods_by_name['GenerateAccessToken']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['GenerateAccessToken']._serialized_options = b'\xdaA\x07cluster\x82\xd3\xe4\x93\x02E\x12C/v1/{cluster=projects/*/locations/*/clusters/*}:generateAccessToken'
    _globals['_EDGECONTAINER'].methods_by_name['GenerateOfflineCredential']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['GenerateOfflineCredential']._serialized_options = b'\xdaA\x07cluster\x82\xd3\xe4\x93\x02K\x12I/v1/{cluster=projects/*/locations/*/clusters/*}:generateOfflineCredential'
    _globals['_EDGECONTAINER'].methods_by_name['ListNodePools']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['ListNodePools']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/clusters/*}/nodePools'
    _globals['_EDGECONTAINER'].methods_by_name['GetNodePool']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['GetNodePool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}'
    _globals['_EDGECONTAINER'].methods_by_name['CreateNodePool']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['CreateNodePool']._serialized_options = b'\xcaA\x1d\n\x08NodePool\x12\x11OperationMetadata\xdaA\x1dparent,node_pool,node_pool_id\x82\xd3\xe4\x93\x02E"8/v1/{parent=projects/*/locations/*/clusters/*}/nodePools:\tnode_pool'
    _globals['_EDGECONTAINER'].methods_by_name['UpdateNodePool']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['UpdateNodePool']._serialized_options = b'\xcaA\x1d\n\x08NodePool\x12\x11OperationMetadata\xdaA\x15node_pool,update_mask\x82\xd3\xe4\x93\x02O2B/v1/{node_pool.name=projects/*/locations/*/clusters/*/nodePools/*}:\tnode_pool'
    _globals['_EDGECONTAINER'].methods_by_name['DeleteNodePool']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['DeleteNodePool']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}'
    _globals['_EDGECONTAINER'].methods_by_name['ListMachines']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['ListMachines']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/machines'
    _globals['_EDGECONTAINER'].methods_by_name['GetMachine']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['GetMachine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/machines/*}'
    _globals['_EDGECONTAINER'].methods_by_name['ListVpnConnections']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['ListVpnConnections']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/vpnConnections'
    _globals['_EDGECONTAINER'].methods_by_name['GetVpnConnection']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['GetVpnConnection']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/vpnConnections/*}'
    _globals['_EDGECONTAINER'].methods_by_name['CreateVpnConnection']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['CreateVpnConnection']._serialized_options = b'\xcaA"\n\rVpnConnection\x12\x11OperationMetadata\xdaA\'parent,vpn_connection,vpn_connection_id\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/vpnConnections:\x0evpn_connection'
    _globals['_EDGECONTAINER'].methods_by_name['DeleteVpnConnection']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['DeleteVpnConnection']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/vpnConnections/*}'
    _globals['_EDGECONTAINER'].methods_by_name['GetServerConfig']._loaded_options = None
    _globals['_EDGECONTAINER'].methods_by_name['GetServerConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*}/serverConfig'
    _globals['_OPERATIONMETADATA']._serialized_start = 374
    _globals['_OPERATIONMETADATA']._serialized_end = 766
    _globals['_OPERATIONMETADATA_STATUSREASON']._serialized_start = 701
    _globals['_OPERATIONMETADATA_STATUSREASON']._serialized_end = 766
    _globals['_LISTCLUSTERSREQUEST']._serialized_start = 769
    _globals['_LISTCLUSTERSREQUEST']._serialized_end = 925
    _globals['_LISTCLUSTERSRESPONSE']._serialized_start = 927
    _globals['_LISTCLUSTERSRESPONSE']._serialized_end = 1053
    _globals['_GETCLUSTERREQUEST']._serialized_start = 1055
    _globals['_GETCLUSTERREQUEST']._serialized_end = 1134
    _globals['_CREATECLUSTERREQUEST']._serialized_start = 1137
    _globals['_CREATECLUSTERREQUEST']._serialized_end = 1328
    _globals['_UPDATECLUSTERREQUEST']._serialized_start = 1331
    _globals['_UPDATECLUSTERREQUEST']._serialized_end = 1479
    _globals['_UPGRADECLUSTERREQUEST']._serialized_start = 1482
    _globals['_UPGRADECLUSTERREQUEST']._serialized_end = 1750
    _globals['_UPGRADECLUSTERREQUEST_SCHEDULE']._serialized_start = 1697
    _globals['_UPGRADECLUSTERREQUEST_SCHEDULE']._serialized_end = 1750
    _globals['_DELETECLUSTERREQUEST']._serialized_start = 1752
    _globals['_DELETECLUSTERREQUEST']._serialized_end = 1854
    _globals['_GENERATEACCESSTOKENREQUEST']._serialized_start = 1856
    _globals['_GENERATEACCESSTOKENREQUEST']._serialized_end = 1947
    _globals['_GENERATEACCESSTOKENRESPONSE']._serialized_start = 1949
    _globals['_GENERATEACCESSTOKENRESPONSE']._serialized_end = 2059
    _globals['_GENERATEOFFLINECREDENTIALREQUEST']._serialized_start = 2061
    _globals['_GENERATEOFFLINECREDENTIALREQUEST']._serialized_end = 2158
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE']._serialized_start = 2161
    _globals['_GENERATEOFFLINECREDENTIALRESPONSE']._serialized_end = 2330
    _globals['_LISTNODEPOOLSREQUEST']._serialized_start = 2333
    _globals['_LISTNODEPOOLSREQUEST']._serialized_end = 2491
    _globals['_LISTNODEPOOLSRESPONSE']._serialized_start = 2494
    _globals['_LISTNODEPOOLSRESPONSE']._serialized_end = 2624
    _globals['_GETNODEPOOLREQUEST']._serialized_start = 2626
    _globals['_GETNODEPOOLREQUEST']._serialized_end = 2707
    _globals['_CREATENODEPOOLREQUEST']._serialized_start = 2710
    _globals['_CREATENODEPOOLREQUEST']._serialized_end = 2908
    _globals['_UPDATENODEPOOLREQUEST']._serialized_start = 2911
    _globals['_UPDATENODEPOOLREQUEST']._serialized_end = 3063
    _globals['_DELETENODEPOOLREQUEST']._serialized_start = 3065
    _globals['_DELETENODEPOOLREQUEST']._serialized_end = 3169
    _globals['_LISTMACHINESREQUEST']._serialized_start = 3172
    _globals['_LISTMACHINESREQUEST']._serialized_end = 3328
    _globals['_LISTMACHINESRESPONSE']._serialized_start = 3330
    _globals['_LISTMACHINESRESPONSE']._serialized_end = 3456
    _globals['_GETMACHINEREQUEST']._serialized_start = 3458
    _globals['_GETMACHINEREQUEST']._serialized_end = 3537
    _globals['_LISTVPNCONNECTIONSREQUEST']._serialized_start = 3540
    _globals['_LISTVPNCONNECTIONSREQUEST']._serialized_end = 3708
    _globals['_LISTVPNCONNECTIONSRESPONSE']._serialized_start = 3711
    _globals['_LISTVPNCONNECTIONSRESPONSE']._serialized_end = 3856
    _globals['_GETVPNCONNECTIONREQUEST']._serialized_start = 3858
    _globals['_GETVPNCONNECTIONREQUEST']._serialized_end = 3949
    _globals['_CREATEVPNCONNECTIONREQUEST']._serialized_start = 3952
    _globals['_CREATEVPNCONNECTIONREQUEST']._serialized_end = 4175
    _globals['_DELETEVPNCONNECTIONREQUEST']._serialized_start = 4177
    _globals['_DELETEVPNCONNECTIONREQUEST']._serialized_end = 4291
    _globals['_GETSERVERCONFIGREQUEST']._serialized_start = 4293
    _globals['_GETSERVERCONFIGREQUEST']._serialized_end = 4374
    _globals['_EDGECONTAINER']._serialized_start = 4377
    _globals['_EDGECONTAINER']._serialized_end = 8724