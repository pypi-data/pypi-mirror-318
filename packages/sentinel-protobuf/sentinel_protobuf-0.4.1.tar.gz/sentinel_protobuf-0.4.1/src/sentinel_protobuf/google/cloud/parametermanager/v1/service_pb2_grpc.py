"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.parametermanager.v1 import service_pb2 as google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/parametermanager/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class ParameterManagerStub(object):
    """Service describing handlers for resources
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListParameters = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/ListParameters', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParametersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParametersResponse.FromString, _registered_method=True)
        self.GetParameter = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/GetParameter', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.GetParameterRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.Parameter.FromString, _registered_method=True)
        self.CreateParameter = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/CreateParameter', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.CreateParameterRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.Parameter.FromString, _registered_method=True)
        self.UpdateParameter = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/UpdateParameter', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.UpdateParameterRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.Parameter.FromString, _registered_method=True)
        self.DeleteParameter = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/DeleteParameter', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.DeleteParameterRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.ListParameterVersions = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/ListParameterVersions', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParameterVersionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParameterVersionsResponse.FromString, _registered_method=True)
        self.GetParameterVersion = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/GetParameterVersion', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.GetParameterVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ParameterVersion.FromString, _registered_method=True)
        self.RenderParameterVersion = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/RenderParameterVersion', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.RenderParameterVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.RenderParameterVersionResponse.FromString, _registered_method=True)
        self.CreateParameterVersion = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/CreateParameterVersion', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.CreateParameterVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ParameterVersion.FromString, _registered_method=True)
        self.UpdateParameterVersion = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/UpdateParameterVersion', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.UpdateParameterVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ParameterVersion.FromString, _registered_method=True)
        self.DeleteParameterVersion = channel.unary_unary('/google.cloud.parametermanager.v1.ParameterManager/DeleteParameterVersion', request_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.DeleteParameterVersionRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)

class ParameterManagerServicer(object):
    """Service describing handlers for resources
    """

    def ListParameters(self, request, context):
        """Lists Parameters in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParameter(self, request, context):
        """Gets details of a single Parameter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateParameter(self, request, context):
        """Creates a new Parameter in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateParameter(self, request, context):
        """Updates a single Parameter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteParameter(self, request, context):
        """Deletes a single Parameter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListParameterVersions(self, request, context):
        """Lists ParameterVersions in a given project, location, and parameter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParameterVersion(self, request, context):
        """Gets details of a single ParameterVersion.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RenderParameterVersion(self, request, context):
        """Gets rendered version of a ParameterVersion.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateParameterVersion(self, request, context):
        """Creates a new ParameterVersion in a given project, location, and parameter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateParameterVersion(self, request, context):
        """Updates a single ParameterVersion.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteParameterVersion(self, request, context):
        """Deletes a single ParameterVersion.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ParameterManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListParameters': grpc.unary_unary_rpc_method_handler(servicer.ListParameters, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParametersRequest.FromString, response_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParametersResponse.SerializeToString), 'GetParameter': grpc.unary_unary_rpc_method_handler(servicer.GetParameter, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.GetParameterRequest.FromString, response_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.Parameter.SerializeToString), 'CreateParameter': grpc.unary_unary_rpc_method_handler(servicer.CreateParameter, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.CreateParameterRequest.FromString, response_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.Parameter.SerializeToString), 'UpdateParameter': grpc.unary_unary_rpc_method_handler(servicer.UpdateParameter, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.UpdateParameterRequest.FromString, response_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.Parameter.SerializeToString), 'DeleteParameter': grpc.unary_unary_rpc_method_handler(servicer.DeleteParameter, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.DeleteParameterRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ListParameterVersions': grpc.unary_unary_rpc_method_handler(servicer.ListParameterVersions, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParameterVersionsRequest.FromString, response_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParameterVersionsResponse.SerializeToString), 'GetParameterVersion': grpc.unary_unary_rpc_method_handler(servicer.GetParameterVersion, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.GetParameterVersionRequest.FromString, response_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ParameterVersion.SerializeToString), 'RenderParameterVersion': grpc.unary_unary_rpc_method_handler(servicer.RenderParameterVersion, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.RenderParameterVersionRequest.FromString, response_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.RenderParameterVersionResponse.SerializeToString), 'CreateParameterVersion': grpc.unary_unary_rpc_method_handler(servicer.CreateParameterVersion, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.CreateParameterVersionRequest.FromString, response_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ParameterVersion.SerializeToString), 'UpdateParameterVersion': grpc.unary_unary_rpc_method_handler(servicer.UpdateParameterVersion, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.UpdateParameterVersionRequest.FromString, response_serializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ParameterVersion.SerializeToString), 'DeleteParameterVersion': grpc.unary_unary_rpc_method_handler(servicer.DeleteParameterVersion, request_deserializer=google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.DeleteParameterVersionRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.parametermanager.v1.ParameterManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.parametermanager.v1.ParameterManager', rpc_method_handlers)

class ParameterManager(object):
    """Service describing handlers for resources
    """

    @staticmethod
    def ListParameters(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/ListParameters', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParametersRequest.SerializeToString, google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParametersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetParameter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/GetParameter', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.GetParameterRequest.SerializeToString, google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.Parameter.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateParameter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/CreateParameter', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.CreateParameterRequest.SerializeToString, google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.Parameter.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateParameter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/UpdateParameter', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.UpdateParameterRequest.SerializeToString, google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.Parameter.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteParameter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/DeleteParameter', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.DeleteParameterRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListParameterVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/ListParameterVersions', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParameterVersionsRequest.SerializeToString, google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ListParameterVersionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetParameterVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/GetParameterVersion', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.GetParameterVersionRequest.SerializeToString, google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ParameterVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RenderParameterVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/RenderParameterVersion', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.RenderParameterVersionRequest.SerializeToString, google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.RenderParameterVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateParameterVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/CreateParameterVersion', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.CreateParameterVersionRequest.SerializeToString, google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ParameterVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateParameterVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/UpdateParameterVersion', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.UpdateParameterVersionRequest.SerializeToString, google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.ParameterVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteParameterVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.parametermanager.v1.ParameterManager/DeleteParameterVersion', google_dot_cloud_dot_parametermanager_dot_v1_dot_service__pb2.DeleteParameterVersionRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)