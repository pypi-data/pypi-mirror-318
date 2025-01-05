"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.gdchardwaremanagement.v1alpha import resources_pb2 as google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2
from .....google.cloud.gdchardwaremanagement.v1alpha import service_pb2 as google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/gdchardwaremanagement/v1alpha/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class GDCHardwareManagementStub(object):
    """The GDC Hardware Management service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListOrders = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListOrders', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListOrdersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListOrdersResponse.FromString, _registered_method=True)
        self.GetOrder = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetOrder', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetOrderRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Order.FromString, _registered_method=True)
        self.CreateOrder = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateOrder', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateOrderRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateOrder = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateOrder', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateOrderRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteOrder = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteOrder', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteOrderRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.SubmitOrder = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/SubmitOrder', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.SubmitOrderRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListSites = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListSites', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSitesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSitesResponse.FromString, _registered_method=True)
        self.GetSite = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetSite', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetSiteRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Site.FromString, _registered_method=True)
        self.CreateSite = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateSite', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateSiteRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateSite = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateSite', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateSiteRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteSite = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteSite', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteSiteRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListHardwareGroups = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListHardwareGroups', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareGroupsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareGroupsResponse.FromString, _registered_method=True)
        self.GetHardwareGroup = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetHardwareGroup', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetHardwareGroupRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.HardwareGroup.FromString, _registered_method=True)
        self.CreateHardwareGroup = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateHardwareGroup', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateHardwareGroupRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateHardwareGroup = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateHardwareGroup', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateHardwareGroupRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteHardwareGroup = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteHardwareGroup', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteHardwareGroupRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListHardware = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListHardware', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareResponse.FromString, _registered_method=True)
        self.GetHardware = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetHardware', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetHardwareRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Hardware.FromString, _registered_method=True)
        self.CreateHardware = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateHardware', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateHardwareRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateHardware = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateHardware', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateHardwareRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteHardware = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteHardware', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteHardwareRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListComments = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListComments', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListCommentsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListCommentsResponse.FromString, _registered_method=True)
        self.GetComment = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetComment', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetCommentRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Comment.FromString, _registered_method=True)
        self.CreateComment = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateComment', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateCommentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.RecordActionOnComment = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/RecordActionOnComment', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.RecordActionOnCommentRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Comment.FromString, _registered_method=True)
        self.ListChangeLogEntries = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListChangeLogEntries', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListChangeLogEntriesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListChangeLogEntriesResponse.FromString, _registered_method=True)
        self.GetChangeLogEntry = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetChangeLogEntry', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetChangeLogEntryRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.ChangeLogEntry.FromString, _registered_method=True)
        self.ListSkus = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListSkus', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSkusRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSkusResponse.FromString, _registered_method=True)
        self.GetSku = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetSku', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetSkuRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Sku.FromString, _registered_method=True)
        self.ListZones = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListZones', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListZonesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListZonesResponse.FromString, _registered_method=True)
        self.GetZone = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetZone', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetZoneRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Zone.FromString, _registered_method=True)
        self.CreateZone = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateZone', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateZoneRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateZone = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateZone', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateZoneRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteZone = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteZone', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteZoneRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.SignalZoneState = channel.unary_unary('/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/SignalZoneState', request_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.SignalZoneStateRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)

class GDCHardwareManagementServicer(object):
    """The GDC Hardware Management service.
    """

    def ListOrders(self, request, context):
        """Lists orders in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrder(self, request, context):
        """Gets details of an order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOrder(self, request, context):
        """Creates a new order in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOrder(self, request, context):
        """Updates the parameters of an order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOrder(self, request, context):
        """Deletes an order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitOrder(self, request, context):
        """Submits an order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSites(self, request, context):
        """Lists sites in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSite(self, request, context):
        """Gets details of a site.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSite(self, request, context):
        """Creates a new site in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSite(self, request, context):
        """Updates the parameters of a site.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSite(self, request, context):
        """Deletes a site.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListHardwareGroups(self, request, context):
        """Lists hardware groups in a given order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHardwareGroup(self, request, context):
        """Gets details of a hardware group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateHardwareGroup(self, request, context):
        """Creates a new hardware group in a given order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateHardwareGroup(self, request, context):
        """Updates the parameters of a hardware group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteHardwareGroup(self, request, context):
        """Deletes a hardware group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListHardware(self, request, context):
        """Lists hardware in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHardware(self, request, context):
        """Gets hardware details.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateHardware(self, request, context):
        """Creates new hardware in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateHardware(self, request, context):
        """Updates hardware parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteHardware(self, request, context):
        """Deletes hardware.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListComments(self, request, context):
        """Lists the comments on an order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetComment(self, request, context):
        """Gets the content of a comment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateComment(self, request, context):
        """Creates a new comment on an order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordActionOnComment(self, request, context):
        """Record Action on a Comment. If the Action specified in the request is READ,
        the viewed time in the comment is set to the time the request was received.
        If the comment is already marked as read, subsequent calls will be ignored.
        If the Action is UNREAD, the viewed time is cleared from the comment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListChangeLogEntries(self, request, context):
        """Lists the changes made to an order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChangeLogEntry(self, request, context):
        """Gets details of a change to an order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSkus(self, request, context):
        """Lists SKUs for a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSku(self, request, context):
        """Gets details of an SKU.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListZones(self, request, context):
        """Lists zones in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetZone(self, request, context):
        """Gets details of a zone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateZone(self, request, context):
        """Creates a new zone in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateZone(self, request, context):
        """Updates the parameters of a zone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteZone(self, request, context):
        """Deletes a zone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignalZoneState(self, request, context):
        """Signals the state of a zone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_GDCHardwareManagementServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListOrders': grpc.unary_unary_rpc_method_handler(servicer.ListOrders, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListOrdersRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListOrdersResponse.SerializeToString), 'GetOrder': grpc.unary_unary_rpc_method_handler(servicer.GetOrder, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetOrderRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Order.SerializeToString), 'CreateOrder': grpc.unary_unary_rpc_method_handler(servicer.CreateOrder, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateOrderRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateOrder': grpc.unary_unary_rpc_method_handler(servicer.UpdateOrder, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateOrderRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteOrder': grpc.unary_unary_rpc_method_handler(servicer.DeleteOrder, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteOrderRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'SubmitOrder': grpc.unary_unary_rpc_method_handler(servicer.SubmitOrder, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.SubmitOrderRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListSites': grpc.unary_unary_rpc_method_handler(servicer.ListSites, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSitesRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSitesResponse.SerializeToString), 'GetSite': grpc.unary_unary_rpc_method_handler(servicer.GetSite, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetSiteRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Site.SerializeToString), 'CreateSite': grpc.unary_unary_rpc_method_handler(servicer.CreateSite, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateSiteRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateSite': grpc.unary_unary_rpc_method_handler(servicer.UpdateSite, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateSiteRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteSite': grpc.unary_unary_rpc_method_handler(servicer.DeleteSite, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteSiteRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListHardwareGroups': grpc.unary_unary_rpc_method_handler(servicer.ListHardwareGroups, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareGroupsRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareGroupsResponse.SerializeToString), 'GetHardwareGroup': grpc.unary_unary_rpc_method_handler(servicer.GetHardwareGroup, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetHardwareGroupRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.HardwareGroup.SerializeToString), 'CreateHardwareGroup': grpc.unary_unary_rpc_method_handler(servicer.CreateHardwareGroup, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateHardwareGroupRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateHardwareGroup': grpc.unary_unary_rpc_method_handler(servicer.UpdateHardwareGroup, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateHardwareGroupRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteHardwareGroup': grpc.unary_unary_rpc_method_handler(servicer.DeleteHardwareGroup, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteHardwareGroupRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListHardware': grpc.unary_unary_rpc_method_handler(servicer.ListHardware, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareResponse.SerializeToString), 'GetHardware': grpc.unary_unary_rpc_method_handler(servicer.GetHardware, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetHardwareRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Hardware.SerializeToString), 'CreateHardware': grpc.unary_unary_rpc_method_handler(servicer.CreateHardware, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateHardwareRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateHardware': grpc.unary_unary_rpc_method_handler(servicer.UpdateHardware, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateHardwareRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteHardware': grpc.unary_unary_rpc_method_handler(servicer.DeleteHardware, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteHardwareRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListComments': grpc.unary_unary_rpc_method_handler(servicer.ListComments, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListCommentsRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListCommentsResponse.SerializeToString), 'GetComment': grpc.unary_unary_rpc_method_handler(servicer.GetComment, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetCommentRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Comment.SerializeToString), 'CreateComment': grpc.unary_unary_rpc_method_handler(servicer.CreateComment, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateCommentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'RecordActionOnComment': grpc.unary_unary_rpc_method_handler(servicer.RecordActionOnComment, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.RecordActionOnCommentRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Comment.SerializeToString), 'ListChangeLogEntries': grpc.unary_unary_rpc_method_handler(servicer.ListChangeLogEntries, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListChangeLogEntriesRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListChangeLogEntriesResponse.SerializeToString), 'GetChangeLogEntry': grpc.unary_unary_rpc_method_handler(servicer.GetChangeLogEntry, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetChangeLogEntryRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.ChangeLogEntry.SerializeToString), 'ListSkus': grpc.unary_unary_rpc_method_handler(servicer.ListSkus, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSkusRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSkusResponse.SerializeToString), 'GetSku': grpc.unary_unary_rpc_method_handler(servicer.GetSku, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetSkuRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Sku.SerializeToString), 'ListZones': grpc.unary_unary_rpc_method_handler(servicer.ListZones, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListZonesRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListZonesResponse.SerializeToString), 'GetZone': grpc.unary_unary_rpc_method_handler(servicer.GetZone, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetZoneRequest.FromString, response_serializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Zone.SerializeToString), 'CreateZone': grpc.unary_unary_rpc_method_handler(servicer.CreateZone, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateZoneRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateZone': grpc.unary_unary_rpc_method_handler(servicer.UpdateZone, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateZoneRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteZone': grpc.unary_unary_rpc_method_handler(servicer.DeleteZone, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteZoneRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'SignalZoneState': grpc.unary_unary_rpc_method_handler(servicer.SignalZoneState, request_deserializer=google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.SignalZoneStateRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement', rpc_method_handlers)

class GDCHardwareManagement(object):
    """The GDC Hardware Management service.
    """

    @staticmethod
    def ListOrders(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListOrders', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListOrdersRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListOrdersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetOrder(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetOrder', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetOrderRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Order.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateOrder(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateOrder', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateOrderRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateOrder(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateOrder', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateOrderRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteOrder(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteOrder', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteOrderRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SubmitOrder(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/SubmitOrder', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.SubmitOrderRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSites(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListSites', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSitesRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSitesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetSite(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetSite', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetSiteRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Site.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateSite(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateSite', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateSiteRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateSite(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateSite', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateSiteRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteSite(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteSite', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteSiteRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListHardwareGroups(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListHardwareGroups', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareGroupsRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareGroupsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetHardwareGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetHardwareGroup', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetHardwareGroupRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.HardwareGroup.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateHardwareGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateHardwareGroup', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateHardwareGroupRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateHardwareGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateHardwareGroup', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateHardwareGroupRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteHardwareGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteHardwareGroup', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteHardwareGroupRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListHardware(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListHardware', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListHardwareResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetHardware(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetHardware', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetHardwareRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Hardware.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateHardware(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateHardware', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateHardwareRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateHardware(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateHardware', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateHardwareRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteHardware(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteHardware', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteHardwareRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListComments(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListComments', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListCommentsRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListCommentsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetComment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetComment', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetCommentRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Comment.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateComment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateComment', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateCommentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RecordActionOnComment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/RecordActionOnComment', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.RecordActionOnCommentRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Comment.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListChangeLogEntries(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListChangeLogEntries', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListChangeLogEntriesRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListChangeLogEntriesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetChangeLogEntry(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetChangeLogEntry', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetChangeLogEntryRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.ChangeLogEntry.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSkus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListSkus', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSkusRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListSkusResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetSku(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetSku', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetSkuRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Sku.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListZones(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListZones', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListZonesRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.ListZonesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetZone', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.GetZoneRequest.SerializeToString, google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_resources__pb2.Zone.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateZone', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.CreateZoneRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateZone', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.UpdateZoneRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteZone', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.DeleteZoneRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SignalZoneState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/SignalZoneState', google_dot_cloud_dot_gdchardwaremanagement_dot_v1alpha_dot_service__pb2.SignalZoneStateRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)