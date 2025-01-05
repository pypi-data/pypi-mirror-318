"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.dataplex.v1 import analyze_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_analyze__pb2
from .....google.cloud.dataplex.v1 import resources_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2
from .....google.cloud.dataplex.v1 import service_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2
from .....google.cloud.dataplex.v1 import tasks_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_tasks__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/dataplex/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class DataplexServiceStub(object):
    """Dataplex service provides data lakes as a service. The primary resources
    offered by this service are Lakes, Zones and Assets which collectively allow
    a data administrator to organize, manage, secure and catalog data across
    their organization located across cloud projects in a variety of storage
    systems including Cloud Storage and BigQuery.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateLake = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/CreateLake', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateLakeRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateLake = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/UpdateLake', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateLakeRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteLake = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/DeleteLake', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteLakeRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListLakes = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListLakes', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListLakesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListLakesResponse.FromString, _registered_method=True)
        self.GetLake = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/GetLake', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetLakeRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2.Lake.FromString, _registered_method=True)
        self.ListLakeActions = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListLakeActions', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListLakeActionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListActionsResponse.FromString, _registered_method=True)
        self.CreateZone = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/CreateZone', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateZoneRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateZone = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/UpdateZone', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateZoneRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteZone = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/DeleteZone', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteZoneRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListZones = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListZones', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListZonesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListZonesResponse.FromString, _registered_method=True)
        self.GetZone = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/GetZone', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetZoneRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2.Zone.FromString, _registered_method=True)
        self.ListZoneActions = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListZoneActions', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListZoneActionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListActionsResponse.FromString, _registered_method=True)
        self.CreateAsset = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/CreateAsset', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateAssetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateAsset = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/UpdateAsset', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateAssetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteAsset = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/DeleteAsset', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteAssetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListAssets = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListAssets', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListAssetsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListAssetsResponse.FromString, _registered_method=True)
        self.GetAsset = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/GetAsset', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetAssetRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2.Asset.FromString, _registered_method=True)
        self.ListAssetActions = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListAssetActions', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListAssetActionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListActionsResponse.FromString, _registered_method=True)
        self.CreateTask = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/CreateTask', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateTaskRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateTask = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/UpdateTask', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateTaskRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteTask = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/DeleteTask', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteTaskRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListTasks = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListTasks', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListTasksRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListTasksResponse.FromString, _registered_method=True)
        self.GetTask = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/GetTask', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetTaskRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_tasks__pb2.Task.FromString, _registered_method=True)
        self.ListJobs = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListJobs', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListJobsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListJobsResponse.FromString, _registered_method=True)
        self.RunTask = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/RunTask', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.RunTaskRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.RunTaskResponse.FromString, _registered_method=True)
        self.GetJob = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/GetJob', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetJobRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_tasks__pb2.Job.FromString, _registered_method=True)
        self.CancelJob = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/CancelJob', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CancelJobRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.CreateEnvironment = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/CreateEnvironment', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateEnvironmentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateEnvironment = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/UpdateEnvironment', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateEnvironmentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteEnvironment = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/DeleteEnvironment', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteEnvironmentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListEnvironments = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListEnvironments', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListEnvironmentsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListEnvironmentsResponse.FromString, _registered_method=True)
        self.GetEnvironment = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/GetEnvironment', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetEnvironmentRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_analyze__pb2.Environment.FromString, _registered_method=True)
        self.ListSessions = channel.unary_unary('/google.cloud.dataplex.v1.DataplexService/ListSessions', request_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListSessionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListSessionsResponse.FromString, _registered_method=True)

class DataplexServiceServicer(object):
    """Dataplex service provides data lakes as a service. The primary resources
    offered by this service are Lakes, Zones and Assets which collectively allow
    a data administrator to organize, manage, secure and catalog data across
    their organization located across cloud projects in a variety of storage
    systems including Cloud Storage and BigQuery.
    """

    def CreateLake(self, request, context):
        """Creates a lake resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateLake(self, request, context):
        """Updates a lake resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteLake(self, request, context):
        """Deletes a lake resource. All zones within the lake must be deleted before
        the lake can be deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLakes(self, request, context):
        """Lists lake resources in a project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLake(self, request, context):
        """Retrieves a lake resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLakeActions(self, request, context):
        """Lists action resources in a lake.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateZone(self, request, context):
        """Creates a zone resource within a lake.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateZone(self, request, context):
        """Updates a zone resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteZone(self, request, context):
        """Deletes a zone resource. All assets within a zone must be deleted before
        the zone can be deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListZones(self, request, context):
        """Lists zone resources in a lake.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetZone(self, request, context):
        """Retrieves a zone resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListZoneActions(self, request, context):
        """Lists action resources in a zone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAsset(self, request, context):
        """Creates an asset resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAsset(self, request, context):
        """Updates an asset resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAsset(self, request, context):
        """Deletes an asset resource. The referenced storage resource is detached
        (default) or deleted based on the associated Lifecycle policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAssets(self, request, context):
        """Lists asset resources in a zone.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAsset(self, request, context):
        """Retrieves an asset resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAssetActions(self, request, context):
        """Lists action resources in an asset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTask(self, request, context):
        """Creates a task resource within a lake.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Update the task resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """Delete the task resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTasks(self, request, context):
        """Lists tasks under the given lake.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Get task resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListJobs(self, request, context):
        """Lists Jobs under the given task.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunTask(self, request, context):
        """Run an on demand execution of a Task.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJob(self, request, context):
        """Get job resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelJob(self, request, context):
        """Cancel jobs running for the task resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEnvironment(self, request, context):
        """Create an environment resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEnvironment(self, request, context):
        """Update the environment resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEnvironment(self, request, context):
        """Delete the environment resource. All the child resources must have been
        deleted before environment deletion can be initiated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEnvironments(self, request, context):
        """Lists environments under the given lake.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEnvironment(self, request, context):
        """Get environment resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSessions(self, request, context):
        """Lists session resources in an environment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DataplexServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateLake': grpc.unary_unary_rpc_method_handler(servicer.CreateLake, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateLakeRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateLake': grpc.unary_unary_rpc_method_handler(servicer.UpdateLake, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateLakeRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteLake': grpc.unary_unary_rpc_method_handler(servicer.DeleteLake, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteLakeRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListLakes': grpc.unary_unary_rpc_method_handler(servicer.ListLakes, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListLakesRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListLakesResponse.SerializeToString), 'GetLake': grpc.unary_unary_rpc_method_handler(servicer.GetLake, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetLakeRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2.Lake.SerializeToString), 'ListLakeActions': grpc.unary_unary_rpc_method_handler(servicer.ListLakeActions, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListLakeActionsRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListActionsResponse.SerializeToString), 'CreateZone': grpc.unary_unary_rpc_method_handler(servicer.CreateZone, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateZoneRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateZone': grpc.unary_unary_rpc_method_handler(servicer.UpdateZone, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateZoneRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteZone': grpc.unary_unary_rpc_method_handler(servicer.DeleteZone, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteZoneRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListZones': grpc.unary_unary_rpc_method_handler(servicer.ListZones, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListZonesRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListZonesResponse.SerializeToString), 'GetZone': grpc.unary_unary_rpc_method_handler(servicer.GetZone, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetZoneRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2.Zone.SerializeToString), 'ListZoneActions': grpc.unary_unary_rpc_method_handler(servicer.ListZoneActions, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListZoneActionsRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListActionsResponse.SerializeToString), 'CreateAsset': grpc.unary_unary_rpc_method_handler(servicer.CreateAsset, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateAssetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateAsset': grpc.unary_unary_rpc_method_handler(servicer.UpdateAsset, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateAssetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteAsset': grpc.unary_unary_rpc_method_handler(servicer.DeleteAsset, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteAssetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListAssets': grpc.unary_unary_rpc_method_handler(servicer.ListAssets, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListAssetsRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListAssetsResponse.SerializeToString), 'GetAsset': grpc.unary_unary_rpc_method_handler(servicer.GetAsset, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetAssetRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2.Asset.SerializeToString), 'ListAssetActions': grpc.unary_unary_rpc_method_handler(servicer.ListAssetActions, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListAssetActionsRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListActionsResponse.SerializeToString), 'CreateTask': grpc.unary_unary_rpc_method_handler(servicer.CreateTask, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateTaskRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateTask': grpc.unary_unary_rpc_method_handler(servicer.UpdateTask, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateTaskRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteTask': grpc.unary_unary_rpc_method_handler(servicer.DeleteTask, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteTaskRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListTasks': grpc.unary_unary_rpc_method_handler(servicer.ListTasks, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListTasksRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListTasksResponse.SerializeToString), 'GetTask': grpc.unary_unary_rpc_method_handler(servicer.GetTask, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetTaskRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_tasks__pb2.Task.SerializeToString), 'ListJobs': grpc.unary_unary_rpc_method_handler(servicer.ListJobs, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListJobsRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListJobsResponse.SerializeToString), 'RunTask': grpc.unary_unary_rpc_method_handler(servicer.RunTask, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.RunTaskRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.RunTaskResponse.SerializeToString), 'GetJob': grpc.unary_unary_rpc_method_handler(servicer.GetJob, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetJobRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_tasks__pb2.Job.SerializeToString), 'CancelJob': grpc.unary_unary_rpc_method_handler(servicer.CancelJob, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CancelJobRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'CreateEnvironment': grpc.unary_unary_rpc_method_handler(servicer.CreateEnvironment, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateEnvironmentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateEnvironment': grpc.unary_unary_rpc_method_handler(servicer.UpdateEnvironment, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateEnvironmentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteEnvironment': grpc.unary_unary_rpc_method_handler(servicer.DeleteEnvironment, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteEnvironmentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListEnvironments': grpc.unary_unary_rpc_method_handler(servicer.ListEnvironments, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListEnvironmentsRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListEnvironmentsResponse.SerializeToString), 'GetEnvironment': grpc.unary_unary_rpc_method_handler(servicer.GetEnvironment, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetEnvironmentRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_analyze__pb2.Environment.SerializeToString), 'ListSessions': grpc.unary_unary_rpc_method_handler(servicer.ListSessions, request_deserializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListSessionsRequest.FromString, response_serializer=google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListSessionsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.dataplex.v1.DataplexService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.dataplex.v1.DataplexService', rpc_method_handlers)

class DataplexService(object):
    """Dataplex service provides data lakes as a service. The primary resources
    offered by this service are Lakes, Zones and Assets which collectively allow
    a data administrator to organize, manage, secure and catalog data across
    their organization located across cloud projects in a variety of storage
    systems including Cloud Storage and BigQuery.
    """

    @staticmethod
    def CreateLake(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/CreateLake', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateLakeRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateLake(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/UpdateLake', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateLakeRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteLake(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/DeleteLake', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteLakeRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListLakes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListLakes', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListLakesRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListLakesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetLake(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/GetLake', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetLakeRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2.Lake.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListLakeActions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListLakeActions', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListLakeActionsRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListActionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/CreateZone', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateZoneRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/UpdateZone', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateZoneRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/DeleteZone', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteZoneRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListZones(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListZones', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListZonesRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListZonesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetZone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/GetZone', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetZoneRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2.Zone.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListZoneActions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListZoneActions', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListZoneActionsRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListActionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/CreateAsset', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateAssetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/UpdateAsset', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateAssetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/DeleteAsset', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteAssetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListAssets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListAssets', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListAssetsRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListAssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/GetAsset', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetAssetRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2.Asset.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListAssetActions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListAssetActions', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListAssetActionsRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListActionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/CreateTask', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateTaskRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/UpdateTask', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateTaskRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/DeleteTask', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteTaskRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListTasks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListTasks', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListTasksRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListTasksResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/GetTask', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetTaskRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_tasks__pb2.Task.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListJobs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListJobs', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListJobsRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListJobsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RunTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/RunTask', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.RunTaskRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.RunTaskResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetJob(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/GetJob', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetJobRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_tasks__pb2.Job.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CancelJob(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/CancelJob', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CancelJobRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateEnvironment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/CreateEnvironment', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.CreateEnvironmentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateEnvironment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/UpdateEnvironment', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.UpdateEnvironmentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteEnvironment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/DeleteEnvironment', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.DeleteEnvironmentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListEnvironments(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListEnvironments', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListEnvironmentsRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListEnvironmentsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetEnvironment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/GetEnvironment', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.GetEnvironmentRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_analyze__pb2.Environment.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dataplex.v1.DataplexService/ListSessions', google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListSessionsRequest.SerializeToString, google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2.ListSessionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)