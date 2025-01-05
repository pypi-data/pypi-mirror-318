"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.edgecontainer.v1 import resources_pb2 as google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2
from .....google.cloud.edgecontainer.v1 import service_pb2 as google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/edgecontainer/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class EdgeContainerStub(object):
    """EdgeContainer API provides management of Kubernetes Clusters on Google Edge
    Cloud deployments.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListClusters = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/ListClusters', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListClustersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListClustersResponse.FromString, _registered_method=True)
        self.GetCluster = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/GetCluster', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetClusterRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.Cluster.FromString, _registered_method=True)
        self.CreateCluster = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/CreateCluster', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.CreateClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateCluster = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/UpdateCluster', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.UpdateClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpgradeCluster = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/UpgradeCluster', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.UpgradeClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteCluster = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/DeleteCluster', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.DeleteClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.GenerateAccessToken = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/GenerateAccessToken', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateAccessTokenRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateAccessTokenResponse.FromString, _registered_method=True)
        self.GenerateOfflineCredential = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/GenerateOfflineCredential', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateOfflineCredentialRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateOfflineCredentialResponse.FromString, _registered_method=True)
        self.ListNodePools = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/ListNodePools', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListNodePoolsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListNodePoolsResponse.FromString, _registered_method=True)
        self.GetNodePool = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/GetNodePool', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetNodePoolRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.NodePool.FromString, _registered_method=True)
        self.CreateNodePool = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/CreateNodePool', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.CreateNodePoolRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateNodePool = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/UpdateNodePool', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.UpdateNodePoolRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteNodePool = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/DeleteNodePool', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.DeleteNodePoolRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListMachines = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/ListMachines', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListMachinesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListMachinesResponse.FromString, _registered_method=True)
        self.GetMachine = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/GetMachine', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetMachineRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.Machine.FromString, _registered_method=True)
        self.ListVpnConnections = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/ListVpnConnections', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListVpnConnectionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListVpnConnectionsResponse.FromString, _registered_method=True)
        self.GetVpnConnection = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/GetVpnConnection', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetVpnConnectionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.VpnConnection.FromString, _registered_method=True)
        self.CreateVpnConnection = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/CreateVpnConnection', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.CreateVpnConnectionRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteVpnConnection = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/DeleteVpnConnection', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.DeleteVpnConnectionRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.GetServerConfig = channel.unary_unary('/google.cloud.edgecontainer.v1.EdgeContainer/GetServerConfig', request_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetServerConfigRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.ServerConfig.FromString, _registered_method=True)

class EdgeContainerServicer(object):
    """EdgeContainer API provides management of Kubernetes Clusters on Google Edge
    Cloud deployments.
    """

    def ListClusters(self, request, context):
        """Lists Clusters in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCluster(self, request, context):
        """Gets details of a single Cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCluster(self, request, context):
        """Creates a new Cluster in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCluster(self, request, context):
        """Updates the parameters of a single Cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpgradeCluster(self, request, context):
        """Upgrades a single cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCluster(self, request, context):
        """Deletes a single Cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateAccessToken(self, request, context):
        """Generates an access token for a Cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateOfflineCredential(self, request, context):
        """Generates an offline credential for a Cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNodePools(self, request, context):
        """Lists NodePools in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNodePool(self, request, context):
        """Gets details of a single NodePool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNodePool(self, request, context):
        """Creates a new NodePool in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNodePool(self, request, context):
        """Updates the parameters of a single NodePool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNodePool(self, request, context):
        """Deletes a single NodePool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMachines(self, request, context):
        """Lists Machines in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMachine(self, request, context):
        """Gets details of a single Machine.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListVpnConnections(self, request, context):
        """Lists VPN connections in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVpnConnection(self, request, context):
        """Gets details of a single VPN connection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateVpnConnection(self, request, context):
        """Creates a new VPN connection in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVpnConnection(self, request, context):
        """Deletes a single VPN connection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerConfig(self, request, context):
        """Gets the server config.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_EdgeContainerServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListClusters': grpc.unary_unary_rpc_method_handler(servicer.ListClusters, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListClustersRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListClustersResponse.SerializeToString), 'GetCluster': grpc.unary_unary_rpc_method_handler(servicer.GetCluster, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetClusterRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.Cluster.SerializeToString), 'CreateCluster': grpc.unary_unary_rpc_method_handler(servicer.CreateCluster, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.CreateClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateCluster': grpc.unary_unary_rpc_method_handler(servicer.UpdateCluster, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.UpdateClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpgradeCluster': grpc.unary_unary_rpc_method_handler(servicer.UpgradeCluster, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.UpgradeClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteCluster': grpc.unary_unary_rpc_method_handler(servicer.DeleteCluster, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.DeleteClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'GenerateAccessToken': grpc.unary_unary_rpc_method_handler(servicer.GenerateAccessToken, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateAccessTokenRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateAccessTokenResponse.SerializeToString), 'GenerateOfflineCredential': grpc.unary_unary_rpc_method_handler(servicer.GenerateOfflineCredential, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateOfflineCredentialRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateOfflineCredentialResponse.SerializeToString), 'ListNodePools': grpc.unary_unary_rpc_method_handler(servicer.ListNodePools, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListNodePoolsRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListNodePoolsResponse.SerializeToString), 'GetNodePool': grpc.unary_unary_rpc_method_handler(servicer.GetNodePool, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetNodePoolRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.NodePool.SerializeToString), 'CreateNodePool': grpc.unary_unary_rpc_method_handler(servicer.CreateNodePool, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.CreateNodePoolRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateNodePool': grpc.unary_unary_rpc_method_handler(servicer.UpdateNodePool, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.UpdateNodePoolRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteNodePool': grpc.unary_unary_rpc_method_handler(servicer.DeleteNodePool, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.DeleteNodePoolRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListMachines': grpc.unary_unary_rpc_method_handler(servicer.ListMachines, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListMachinesRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListMachinesResponse.SerializeToString), 'GetMachine': grpc.unary_unary_rpc_method_handler(servicer.GetMachine, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetMachineRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.Machine.SerializeToString), 'ListVpnConnections': grpc.unary_unary_rpc_method_handler(servicer.ListVpnConnections, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListVpnConnectionsRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListVpnConnectionsResponse.SerializeToString), 'GetVpnConnection': grpc.unary_unary_rpc_method_handler(servicer.GetVpnConnection, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetVpnConnectionRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.VpnConnection.SerializeToString), 'CreateVpnConnection': grpc.unary_unary_rpc_method_handler(servicer.CreateVpnConnection, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.CreateVpnConnectionRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteVpnConnection': grpc.unary_unary_rpc_method_handler(servicer.DeleteVpnConnection, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.DeleteVpnConnectionRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'GetServerConfig': grpc.unary_unary_rpc_method_handler(servicer.GetServerConfig, request_deserializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetServerConfigRequest.FromString, response_serializer=google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.ServerConfig.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.edgecontainer.v1.EdgeContainer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.edgecontainer.v1.EdgeContainer', rpc_method_handlers)

class EdgeContainer(object):
    """EdgeContainer API provides management of Kubernetes Clusters on Google Edge
    Cloud deployments.
    """

    @staticmethod
    def ListClusters(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/ListClusters', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListClustersRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListClustersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/GetCluster', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetClusterRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.Cluster.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/CreateCluster', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.CreateClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/UpdateCluster', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.UpdateClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpgradeCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/UpgradeCluster', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.UpgradeClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/DeleteCluster', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.DeleteClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GenerateAccessToken(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/GenerateAccessToken', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateAccessTokenRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateAccessTokenResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GenerateOfflineCredential(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/GenerateOfflineCredential', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateOfflineCredentialRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GenerateOfflineCredentialResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListNodePools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/ListNodePools', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListNodePoolsRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListNodePoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetNodePool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/GetNodePool', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetNodePoolRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.NodePool.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateNodePool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/CreateNodePool', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.CreateNodePoolRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateNodePool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/UpdateNodePool', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.UpdateNodePoolRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteNodePool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/DeleteNodePool', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.DeleteNodePoolRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListMachines(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/ListMachines', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListMachinesRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListMachinesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetMachine(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/GetMachine', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetMachineRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.Machine.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListVpnConnections(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/ListVpnConnections', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListVpnConnectionsRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.ListVpnConnectionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetVpnConnection(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/GetVpnConnection', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetVpnConnectionRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.VpnConnection.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateVpnConnection(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/CreateVpnConnection', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.CreateVpnConnectionRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteVpnConnection(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/DeleteVpnConnection', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.DeleteVpnConnectionRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetServerConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgecontainer.v1.EdgeContainer/GetServerConfig', google_dot_cloud_dot_edgecontainer_dot_v1_dot_service__pb2.GetServerConfigRequest.SerializeToString, google_dot_cloud_dot_edgecontainer_dot_v1_dot_resources__pb2.ServerConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)