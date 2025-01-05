"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.notebooks.v2 import instance_pb2 as google_dot_cloud_dot_notebooks_dot_v2_dot_instance__pb2
from .....google.cloud.notebooks.v2 import service_pb2 as google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/notebooks/v2/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class NotebookServiceStub(object):
    """API v2 service for Workbench Notebooks Instances.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListInstances = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/ListInstances', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.ListInstancesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.ListInstancesResponse.FromString, _registered_method=True)
        self.GetInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/GetInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.GetInstanceRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_instance__pb2.Instance.FromString, _registered_method=True)
        self.CreateInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/CreateInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.CreateInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/UpdateInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.UpdateInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/DeleteInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.DeleteInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.StartInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/StartInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.StartInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.StopInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/StopInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.StopInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ResetInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/ResetInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.ResetInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CheckInstanceUpgradability = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/CheckInstanceUpgradability', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.CheckInstanceUpgradabilityRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.CheckInstanceUpgradabilityResponse.FromString, _registered_method=True)
        self.UpgradeInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/UpgradeInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.UpgradeInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.RollbackInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/RollbackInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.RollbackInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DiagnoseInstance = channel.unary_unary('/google.cloud.notebooks.v2.NotebookService/DiagnoseInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.DiagnoseInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)

class NotebookServiceServicer(object):
    """API v2 service for Workbench Notebooks Instances.
    """

    def ListInstances(self, request, context):
        """Lists instances in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstance(self, request, context):
        """Gets details of a single Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateInstance(self, request, context):
        """Creates a new Instance in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateInstance(self, request, context):
        """UpdateInstance updates an Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteInstance(self, request, context):
        """Deletes a single Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartInstance(self, request, context):
        """Starts a notebook instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopInstance(self, request, context):
        """Stops a notebook instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetInstance(self, request, context):
        """Resets a notebook instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckInstanceUpgradability(self, request, context):
        """Checks whether a notebook instance is upgradable.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpgradeInstance(self, request, context):
        """Upgrades a notebook instance to the latest version.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RollbackInstance(self, request, context):
        """Rollbacks a notebook instance to the previous version.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiagnoseInstance(self, request, context):
        """Creates a Diagnostic File and runs Diagnostic Tool given an Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_NotebookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListInstances': grpc.unary_unary_rpc_method_handler(servicer.ListInstances, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.ListInstancesRequest.FromString, response_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.ListInstancesResponse.SerializeToString), 'GetInstance': grpc.unary_unary_rpc_method_handler(servicer.GetInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.GetInstanceRequest.FromString, response_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_instance__pb2.Instance.SerializeToString), 'CreateInstance': grpc.unary_unary_rpc_method_handler(servicer.CreateInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.CreateInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateInstance': grpc.unary_unary_rpc_method_handler(servicer.UpdateInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.UpdateInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteInstance': grpc.unary_unary_rpc_method_handler(servicer.DeleteInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.DeleteInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'StartInstance': grpc.unary_unary_rpc_method_handler(servicer.StartInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.StartInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'StopInstance': grpc.unary_unary_rpc_method_handler(servicer.StopInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.StopInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ResetInstance': grpc.unary_unary_rpc_method_handler(servicer.ResetInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.ResetInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CheckInstanceUpgradability': grpc.unary_unary_rpc_method_handler(servicer.CheckInstanceUpgradability, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.CheckInstanceUpgradabilityRequest.FromString, response_serializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.CheckInstanceUpgradabilityResponse.SerializeToString), 'UpgradeInstance': grpc.unary_unary_rpc_method_handler(servicer.UpgradeInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.UpgradeInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'RollbackInstance': grpc.unary_unary_rpc_method_handler(servicer.RollbackInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.RollbackInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DiagnoseInstance': grpc.unary_unary_rpc_method_handler(servicer.DiagnoseInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.DiagnoseInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.notebooks.v2.NotebookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.notebooks.v2.NotebookService', rpc_method_handlers)

class NotebookService(object):
    """API v2 service for Workbench Notebooks Instances.
    """

    @staticmethod
    def ListInstances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/ListInstances', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.ListInstancesRequest.SerializeToString, google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.ListInstancesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/GetInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.GetInstanceRequest.SerializeToString, google_dot_cloud_dot_notebooks_dot_v2_dot_instance__pb2.Instance.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/CreateInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.CreateInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/UpdateInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.UpdateInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/DeleteInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.DeleteInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def StartInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/StartInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.StartInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def StopInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/StopInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.StopInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ResetInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/ResetInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.ResetInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CheckInstanceUpgradability(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/CheckInstanceUpgradability', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.CheckInstanceUpgradabilityRequest.SerializeToString, google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.CheckInstanceUpgradabilityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpgradeInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/UpgradeInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.UpgradeInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RollbackInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/RollbackInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.RollbackInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DiagnoseInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v2.NotebookService/DiagnoseInstance', google_dot_cloud_dot_notebooks_dot_v2_dot_service__pb2.DiagnoseInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)