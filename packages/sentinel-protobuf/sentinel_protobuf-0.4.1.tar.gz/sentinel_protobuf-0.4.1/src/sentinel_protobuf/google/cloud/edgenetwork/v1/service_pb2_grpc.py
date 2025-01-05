"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.edgenetwork.v1 import resources_pb2 as google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2
from .....google.cloud.edgenetwork.v1 import service_pb2 as google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/edgenetwork/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class EdgeNetworkStub(object):
    """EdgeNetwork API provides managed, highly available cloud dynamic network
    configuration service to the GEC customer to enable edge application and
    network function solutions. This allows the customers to easily define and
    configure the network setup and property to meet the workload requirement.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitializeZone = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/InitializeZone', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.InitializeZoneRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.InitializeZoneResponse.FromString, _registered_method=True)
        self.ListZones = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/ListZones', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListZonesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListZonesResponse.FromString, _registered_method=True)
        self.GetZone = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/GetZone', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetZoneRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Zone.FromString, _registered_method=True)
        self.ListNetworks = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/ListNetworks', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListNetworksRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListNetworksResponse.FromString, _registered_method=True)
        self.GetNetwork = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/GetNetwork', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetNetworkRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Network.FromString, _registered_method=True)
        self.DiagnoseNetwork = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/DiagnoseNetwork', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseNetworkRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseNetworkResponse.FromString, _registered_method=True)
        self.CreateNetwork = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/CreateNetwork', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateNetworkRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteNetwork = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteNetwork', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteNetworkRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListSubnets = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/ListSubnets', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListSubnetsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListSubnetsResponse.FromString, _registered_method=True)
        self.GetSubnet = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/GetSubnet', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetSubnetRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Subnet.FromString, _registered_method=True)
        self.CreateSubnet = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/CreateSubnet', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateSubnetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateSubnet = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/UpdateSubnet', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.UpdateSubnetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteSubnet = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteSubnet', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteSubnetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListInterconnects = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/ListInterconnects', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectsResponse.FromString, _registered_method=True)
        self.GetInterconnect = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/GetInterconnect', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetInterconnectRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Interconnect.FromString, _registered_method=True)
        self.DiagnoseInterconnect = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/DiagnoseInterconnect', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseInterconnectRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseInterconnectResponse.FromString, _registered_method=True)
        self.ListInterconnectAttachments = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/ListInterconnectAttachments', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectAttachmentsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectAttachmentsResponse.FromString, _registered_method=True)
        self.GetInterconnectAttachment = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/GetInterconnectAttachment', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetInterconnectAttachmentRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.InterconnectAttachment.FromString, _registered_method=True)
        self.CreateInterconnectAttachment = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/CreateInterconnectAttachment', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateInterconnectAttachmentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteInterconnectAttachment = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteInterconnectAttachment', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteInterconnectAttachmentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListRouters = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/ListRouters', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListRoutersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListRoutersResponse.FromString, _registered_method=True)
        self.GetRouter = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/GetRouter', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetRouterRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Router.FromString, _registered_method=True)
        self.DiagnoseRouter = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/DiagnoseRouter', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseRouterRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseRouterResponse.FromString, _registered_method=True)
        self.CreateRouter = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/CreateRouter', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateRouterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateRouter = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/UpdateRouter', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.UpdateRouterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteRouter = channel.unary_unary('/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteRouter', request_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteRouterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)

class EdgeNetworkServicer(object):
    """EdgeNetwork API provides managed, highly available cloud dynamic network
    configuration service to the GEC customer to enable edge application and
    network function solutions. This allows the customers to easily define and
    configure the network setup and property to meet the workload requirement.
    """

    def InitializeZone(self, request, context):
        """InitializeZone will initialize resources for a zone in a project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListZones(self, request, context):
        """Deprecated: not implemented.
        Lists Zones in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetZone(self, request, context):
        """Deprecated: not implemented.
        Gets details of a single Zone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNetworks(self, request, context):
        """Lists Networks in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNetwork(self, request, context):
        """Gets details of a single Network.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiagnoseNetwork(self, request, context):
        """Get the diagnostics of a single network resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNetwork(self, request, context):
        """Creates a new Network in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNetwork(self, request, context):
        """Deletes a single Network.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSubnets(self, request, context):
        """Lists Subnets in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSubnet(self, request, context):
        """Gets details of a single Subnet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSubnet(self, request, context):
        """Creates a new Subnet in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSubnet(self, request, context):
        """Updates the parameters of a single Subnet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSubnet(self, request, context):
        """Deletes a single Subnet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListInterconnects(self, request, context):
        """Lists Interconnects in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInterconnect(self, request, context):
        """Gets details of a single Interconnect.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiagnoseInterconnect(self, request, context):
        """Get the diagnostics of a single interconnect resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListInterconnectAttachments(self, request, context):
        """Lists InterconnectAttachments in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInterconnectAttachment(self, request, context):
        """Gets details of a single InterconnectAttachment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateInterconnectAttachment(self, request, context):
        """Creates a new InterconnectAttachment in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteInterconnectAttachment(self, request, context):
        """Deletes a single InterconnectAttachment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRouters(self, request, context):
        """Lists Routers in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRouter(self, request, context):
        """Gets details of a single Router.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiagnoseRouter(self, request, context):
        """Get the diagnostics of a single router resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRouter(self, request, context):
        """Creates a new Router in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRouter(self, request, context):
        """Updates the parameters of a single Router.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRouter(self, request, context):
        """Deletes a single Router.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_EdgeNetworkServicer_to_server(servicer, server):
    rpc_method_handlers = {'InitializeZone': grpc.unary_unary_rpc_method_handler(servicer.InitializeZone, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.InitializeZoneRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.InitializeZoneResponse.SerializeToString), 'ListZones': grpc.unary_unary_rpc_method_handler(servicer.ListZones, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListZonesRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListZonesResponse.SerializeToString), 'GetZone': grpc.unary_unary_rpc_method_handler(servicer.GetZone, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetZoneRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Zone.SerializeToString), 'ListNetworks': grpc.unary_unary_rpc_method_handler(servicer.ListNetworks, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListNetworksRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListNetworksResponse.SerializeToString), 'GetNetwork': grpc.unary_unary_rpc_method_handler(servicer.GetNetwork, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetNetworkRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Network.SerializeToString), 'DiagnoseNetwork': grpc.unary_unary_rpc_method_handler(servicer.DiagnoseNetwork, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseNetworkRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseNetworkResponse.SerializeToString), 'CreateNetwork': grpc.unary_unary_rpc_method_handler(servicer.CreateNetwork, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateNetworkRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteNetwork': grpc.unary_unary_rpc_method_handler(servicer.DeleteNetwork, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteNetworkRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListSubnets': grpc.unary_unary_rpc_method_handler(servicer.ListSubnets, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListSubnetsRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListSubnetsResponse.SerializeToString), 'GetSubnet': grpc.unary_unary_rpc_method_handler(servicer.GetSubnet, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetSubnetRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Subnet.SerializeToString), 'CreateSubnet': grpc.unary_unary_rpc_method_handler(servicer.CreateSubnet, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateSubnetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateSubnet': grpc.unary_unary_rpc_method_handler(servicer.UpdateSubnet, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.UpdateSubnetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteSubnet': grpc.unary_unary_rpc_method_handler(servicer.DeleteSubnet, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteSubnetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListInterconnects': grpc.unary_unary_rpc_method_handler(servicer.ListInterconnects, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectsRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectsResponse.SerializeToString), 'GetInterconnect': grpc.unary_unary_rpc_method_handler(servicer.GetInterconnect, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetInterconnectRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Interconnect.SerializeToString), 'DiagnoseInterconnect': grpc.unary_unary_rpc_method_handler(servicer.DiagnoseInterconnect, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseInterconnectRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseInterconnectResponse.SerializeToString), 'ListInterconnectAttachments': grpc.unary_unary_rpc_method_handler(servicer.ListInterconnectAttachments, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectAttachmentsRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectAttachmentsResponse.SerializeToString), 'GetInterconnectAttachment': grpc.unary_unary_rpc_method_handler(servicer.GetInterconnectAttachment, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetInterconnectAttachmentRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.InterconnectAttachment.SerializeToString), 'CreateInterconnectAttachment': grpc.unary_unary_rpc_method_handler(servicer.CreateInterconnectAttachment, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateInterconnectAttachmentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteInterconnectAttachment': grpc.unary_unary_rpc_method_handler(servicer.DeleteInterconnectAttachment, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteInterconnectAttachmentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListRouters': grpc.unary_unary_rpc_method_handler(servicer.ListRouters, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListRoutersRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListRoutersResponse.SerializeToString), 'GetRouter': grpc.unary_unary_rpc_method_handler(servicer.GetRouter, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetRouterRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Router.SerializeToString), 'DiagnoseRouter': grpc.unary_unary_rpc_method_handler(servicer.DiagnoseRouter, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseRouterRequest.FromString, response_serializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseRouterResponse.SerializeToString), 'CreateRouter': grpc.unary_unary_rpc_method_handler(servicer.CreateRouter, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateRouterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateRouter': grpc.unary_unary_rpc_method_handler(servicer.UpdateRouter, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.UpdateRouterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteRouter': grpc.unary_unary_rpc_method_handler(servicer.DeleteRouter, request_deserializer=google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteRouterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.edgenetwork.v1.EdgeNetwork', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.edgenetwork.v1.EdgeNetwork', rpc_method_handlers)

class EdgeNetwork(object):
    """EdgeNetwork API provides managed, highly available cloud dynamic network
    configuration service to the GEC customer to enable edge application and
    network function solutions. This allows the customers to easily define and
    configure the network setup and property to meet the workload requirement.
    """

    @staticmethod
    def InitializeZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/InitializeZone', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.InitializeZoneRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.InitializeZoneResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListZones(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/ListZones', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListZonesRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListZonesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/GetZone', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetZoneRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Zone.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListNetworks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/ListNetworks', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListNetworksRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListNetworksResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetNetwork(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/GetNetwork', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetNetworkRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Network.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DiagnoseNetwork(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/DiagnoseNetwork', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseNetworkRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseNetworkResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateNetwork(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/CreateNetwork', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateNetworkRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteNetwork(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteNetwork', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteNetworkRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSubnets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/ListSubnets', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListSubnetsRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListSubnetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetSubnet(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/GetSubnet', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetSubnetRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Subnet.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateSubnet(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/CreateSubnet', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateSubnetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateSubnet(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/UpdateSubnet', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.UpdateSubnetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteSubnet(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteSubnet', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteSubnetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListInterconnects(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/ListInterconnects', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectsRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetInterconnect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/GetInterconnect', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetInterconnectRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Interconnect.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DiagnoseInterconnect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/DiagnoseInterconnect', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseInterconnectRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseInterconnectResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListInterconnectAttachments(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/ListInterconnectAttachments', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectAttachmentsRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListInterconnectAttachmentsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetInterconnectAttachment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/GetInterconnectAttachment', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetInterconnectAttachmentRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.InterconnectAttachment.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateInterconnectAttachment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/CreateInterconnectAttachment', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateInterconnectAttachmentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteInterconnectAttachment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteInterconnectAttachment', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteInterconnectAttachmentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListRouters(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/ListRouters', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListRoutersRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.ListRoutersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetRouter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/GetRouter', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.GetRouterRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_resources__pb2.Router.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DiagnoseRouter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/DiagnoseRouter', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseRouterRequest.SerializeToString, google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DiagnoseRouterResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateRouter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/CreateRouter', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.CreateRouterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateRouter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/UpdateRouter', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.UpdateRouterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteRouter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteRouter', google_dot_cloud_dot_edgenetwork_dot_v1_dot_service__pb2.DeleteRouterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)