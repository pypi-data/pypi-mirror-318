"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.notebooks.v1beta1 import environment_pb2 as google_dot_cloud_dot_notebooks_dot_v1beta1_dot_environment__pb2
from .....google.cloud.notebooks.v1beta1 import instance_pb2 as google_dot_cloud_dot_notebooks_dot_v1beta1_dot_instance__pb2
from .....google.cloud.notebooks.v1beta1 import service_pb2 as google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/notebooks/v1beta1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class NotebookServiceStub(object):
    """API v1beta1 service for Cloud AI Platform Notebooks.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListInstances = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/ListInstances', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListInstancesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListInstancesResponse.FromString, _registered_method=True)
        self.GetInstance = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/GetInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.GetInstanceRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_instance__pb2.Instance.FromString, _registered_method=True)
        self.CreateInstance = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/CreateInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.CreateInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.RegisterInstance = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/RegisterInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.RegisterInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.SetInstanceAccelerator = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/SetInstanceAccelerator', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.SetInstanceAcceleratorRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.SetInstanceMachineType = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/SetInstanceMachineType', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.SetInstanceMachineTypeRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.SetInstanceLabels = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/SetInstanceLabels', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.SetInstanceLabelsRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteInstance = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/DeleteInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.DeleteInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.StartInstance = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/StartInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.StartInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.StopInstance = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/StopInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.StopInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ResetInstance = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/ResetInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ResetInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ReportInstanceInfo = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/ReportInstanceInfo', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ReportInstanceInfoRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.IsInstanceUpgradeable = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/IsInstanceUpgradeable', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.IsInstanceUpgradeableRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.IsInstanceUpgradeableResponse.FromString, _registered_method=True)
        self.UpgradeInstance = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/UpgradeInstance', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.UpgradeInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpgradeInstanceInternal = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/UpgradeInstanceInternal', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.UpgradeInstanceInternalRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListEnvironments = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/ListEnvironments', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListEnvironmentsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListEnvironmentsResponse.FromString, _registered_method=True)
        self.GetEnvironment = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/GetEnvironment', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.GetEnvironmentRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_environment__pb2.Environment.FromString, _registered_method=True)
        self.CreateEnvironment = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/CreateEnvironment', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.CreateEnvironmentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteEnvironment = channel.unary_unary('/google.cloud.notebooks.v1beta1.NotebookService/DeleteEnvironment', request_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.DeleteEnvironmentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)

class NotebookServiceServicer(object):
    """API v1beta1 service for Cloud AI Platform Notebooks.
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

    def RegisterInstance(self, request, context):
        """Registers an existing legacy notebook instance to the Notebooks API server.
        Legacy instances are instances created with the legacy Compute Engine
        calls. They are not manageable by the Notebooks API out of the box. This
        call makes these instances manageable by the Notebooks API.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetInstanceAccelerator(self, request, context):
        """Updates the guest accelerators of a single Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetInstanceMachineType(self, request, context):
        """Updates the machine type of a single Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetInstanceLabels(self, request, context):
        """Updates the labels of an Instance.
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

    def ReportInstanceInfo(self, request, context):
        """Allows notebook instances to
        report their latest instance information to the Notebooks
        API server. The server will merge the reported information to
        the instance metadata store. Do not use this method directly.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsInstanceUpgradeable(self, request, context):
        """Check if a notebook instance is upgradable.
        Deprecated. Please consider using v1.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpgradeInstance(self, request, context):
        """Upgrades a notebook instance to the latest version.
        Deprecated. Please consider using v1.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpgradeInstanceInternal(self, request, context):
        """Allows notebook instances to
        call this endpoint to upgrade themselves. Do not use this method directly.
        Deprecated. Please consider using v1.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEnvironments(self, request, context):
        """Lists environments in a project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEnvironment(self, request, context):
        """Gets details of a single Environment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEnvironment(self, request, context):
        """Creates a new Environment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEnvironment(self, request, context):
        """Deletes a single Environment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_NotebookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListInstances': grpc.unary_unary_rpc_method_handler(servicer.ListInstances, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListInstancesRequest.FromString, response_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListInstancesResponse.SerializeToString), 'GetInstance': grpc.unary_unary_rpc_method_handler(servicer.GetInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.GetInstanceRequest.FromString, response_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_instance__pb2.Instance.SerializeToString), 'CreateInstance': grpc.unary_unary_rpc_method_handler(servicer.CreateInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.CreateInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'RegisterInstance': grpc.unary_unary_rpc_method_handler(servicer.RegisterInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.RegisterInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'SetInstanceAccelerator': grpc.unary_unary_rpc_method_handler(servicer.SetInstanceAccelerator, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.SetInstanceAcceleratorRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'SetInstanceMachineType': grpc.unary_unary_rpc_method_handler(servicer.SetInstanceMachineType, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.SetInstanceMachineTypeRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'SetInstanceLabels': grpc.unary_unary_rpc_method_handler(servicer.SetInstanceLabels, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.SetInstanceLabelsRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteInstance': grpc.unary_unary_rpc_method_handler(servicer.DeleteInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.DeleteInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'StartInstance': grpc.unary_unary_rpc_method_handler(servicer.StartInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.StartInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'StopInstance': grpc.unary_unary_rpc_method_handler(servicer.StopInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.StopInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ResetInstance': grpc.unary_unary_rpc_method_handler(servicer.ResetInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ResetInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ReportInstanceInfo': grpc.unary_unary_rpc_method_handler(servicer.ReportInstanceInfo, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ReportInstanceInfoRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'IsInstanceUpgradeable': grpc.unary_unary_rpc_method_handler(servicer.IsInstanceUpgradeable, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.IsInstanceUpgradeableRequest.FromString, response_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.IsInstanceUpgradeableResponse.SerializeToString), 'UpgradeInstance': grpc.unary_unary_rpc_method_handler(servicer.UpgradeInstance, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.UpgradeInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpgradeInstanceInternal': grpc.unary_unary_rpc_method_handler(servicer.UpgradeInstanceInternal, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.UpgradeInstanceInternalRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListEnvironments': grpc.unary_unary_rpc_method_handler(servicer.ListEnvironments, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListEnvironmentsRequest.FromString, response_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListEnvironmentsResponse.SerializeToString), 'GetEnvironment': grpc.unary_unary_rpc_method_handler(servicer.GetEnvironment, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.GetEnvironmentRequest.FromString, response_serializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_environment__pb2.Environment.SerializeToString), 'CreateEnvironment': grpc.unary_unary_rpc_method_handler(servicer.CreateEnvironment, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.CreateEnvironmentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteEnvironment': grpc.unary_unary_rpc_method_handler(servicer.DeleteEnvironment, request_deserializer=google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.DeleteEnvironmentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.notebooks.v1beta1.NotebookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.notebooks.v1beta1.NotebookService', rpc_method_handlers)

class NotebookService(object):
    """API v1beta1 service for Cloud AI Platform Notebooks.
    """

    @staticmethod
    def ListInstances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/ListInstances', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListInstancesRequest.SerializeToString, google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListInstancesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/GetInstance', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.GetInstanceRequest.SerializeToString, google_dot_cloud_dot_notebooks_dot_v1beta1_dot_instance__pb2.Instance.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/CreateInstance', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.CreateInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RegisterInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/RegisterInstance', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.RegisterInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetInstanceAccelerator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/SetInstanceAccelerator', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.SetInstanceAcceleratorRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetInstanceMachineType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/SetInstanceMachineType', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.SetInstanceMachineTypeRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetInstanceLabels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/SetInstanceLabels', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.SetInstanceLabelsRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/DeleteInstance', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.DeleteInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def StartInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/StartInstance', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.StartInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def StopInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/StopInstance', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.StopInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ResetInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/ResetInstance', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ResetInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ReportInstanceInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/ReportInstanceInfo', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ReportInstanceInfoRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def IsInstanceUpgradeable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/IsInstanceUpgradeable', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.IsInstanceUpgradeableRequest.SerializeToString, google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.IsInstanceUpgradeableResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpgradeInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/UpgradeInstance', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.UpgradeInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpgradeInstanceInternal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/UpgradeInstanceInternal', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.UpgradeInstanceInternalRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListEnvironments(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/ListEnvironments', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListEnvironmentsRequest.SerializeToString, google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.ListEnvironmentsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetEnvironment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/GetEnvironment', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.GetEnvironmentRequest.SerializeToString, google_dot_cloud_dot_notebooks_dot_v1beta1_dot_environment__pb2.Environment.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateEnvironment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/CreateEnvironment', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.CreateEnvironmentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteEnvironment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.notebooks.v1beta1.NotebookService/DeleteEnvironment', google_dot_cloud_dot_notebooks_dot_v1beta1_dot_service__pb2.DeleteEnvironmentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)