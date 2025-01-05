"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.binaryauthorization.v1beta1 import resources_pb2 as google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2
from .....google.cloud.binaryauthorization.v1beta1 import service_pb2 as google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/binaryauthorization/v1beta1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class BinauthzManagementServiceV1Beta1Stub(object):
    """Customer-facing API for Cloud Binary Authorization.

    Google Cloud Management Service for Binary Authorization admission policies
    and attestation authorities.

    This API implements a REST model with the following objects:

    * [Policy][google.cloud.binaryauthorization.v1beta1.Policy]
    * [Attestor][google.cloud.binaryauthorization.v1beta1.Attestor]
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPolicy = channel.unary_unary('/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/GetPolicy', request_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.GetPolicyRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Policy.FromString, _registered_method=True)
        self.UpdatePolicy = channel.unary_unary('/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/UpdatePolicy', request_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.UpdatePolicyRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Policy.FromString, _registered_method=True)
        self.CreateAttestor = channel.unary_unary('/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/CreateAttestor', request_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.CreateAttestorRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Attestor.FromString, _registered_method=True)
        self.GetAttestor = channel.unary_unary('/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/GetAttestor', request_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.GetAttestorRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Attestor.FromString, _registered_method=True)
        self.UpdateAttestor = channel.unary_unary('/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/UpdateAttestor', request_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.UpdateAttestorRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Attestor.FromString, _registered_method=True)
        self.ListAttestors = channel.unary_unary('/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/ListAttestors', request_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.ListAttestorsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.ListAttestorsResponse.FromString, _registered_method=True)
        self.DeleteAttestor = channel.unary_unary('/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/DeleteAttestor', request_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.DeleteAttestorRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)

class BinauthzManagementServiceV1Beta1Servicer(object):
    """Customer-facing API for Cloud Binary Authorization.

    Google Cloud Management Service for Binary Authorization admission policies
    and attestation authorities.

    This API implements a REST model with the following objects:

    * [Policy][google.cloud.binaryauthorization.v1beta1.Policy]
    * [Attestor][google.cloud.binaryauthorization.v1beta1.Attestor]
    """

    def GetPolicy(self, request, context):
        """A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to
        a container image, before the project is allowed to deploy that
        image. There is at most one policy per project. All image admission
        requests are permitted if a project has no policy.

        Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default
        [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePolicy(self, request, context):
        """Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the
        new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race
        conditions with concurrent policy enforcement (or management!)
        requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT
        if the request is malformed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAttestor(self, request, context):
        """Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new
        [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist,
        INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the
        [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttestor(self, request, context):
        """Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor].
        Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAttestor(self, request, context):
        """Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor].
        Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAttestors(self, request, context):
        """Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor].
        Returns INVALID_ARGUMENT if the project does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAttestor(self, request, context):
        """Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the
        [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_BinauthzManagementServiceV1Beta1Servicer_to_server(servicer, server):
    rpc_method_handlers = {'GetPolicy': grpc.unary_unary_rpc_method_handler(servicer.GetPolicy, request_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.GetPolicyRequest.FromString, response_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Policy.SerializeToString), 'UpdatePolicy': grpc.unary_unary_rpc_method_handler(servicer.UpdatePolicy, request_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.UpdatePolicyRequest.FromString, response_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Policy.SerializeToString), 'CreateAttestor': grpc.unary_unary_rpc_method_handler(servicer.CreateAttestor, request_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.CreateAttestorRequest.FromString, response_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Attestor.SerializeToString), 'GetAttestor': grpc.unary_unary_rpc_method_handler(servicer.GetAttestor, request_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.GetAttestorRequest.FromString, response_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Attestor.SerializeToString), 'UpdateAttestor': grpc.unary_unary_rpc_method_handler(servicer.UpdateAttestor, request_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.UpdateAttestorRequest.FromString, response_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Attestor.SerializeToString), 'ListAttestors': grpc.unary_unary_rpc_method_handler(servicer.ListAttestors, request_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.ListAttestorsRequest.FromString, response_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.ListAttestorsResponse.SerializeToString), 'DeleteAttestor': grpc.unary_unary_rpc_method_handler(servicer.DeleteAttestor, request_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.DeleteAttestorRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1', rpc_method_handlers)

class BinauthzManagementServiceV1Beta1(object):
    """Customer-facing API for Cloud Binary Authorization.

    Google Cloud Management Service for Binary Authorization admission policies
    and attestation authorities.

    This API implements a REST model with the following objects:

    * [Policy][google.cloud.binaryauthorization.v1beta1.Policy]
    * [Attestor][google.cloud.binaryauthorization.v1beta1.Attestor]
    """

    @staticmethod
    def GetPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/GetPolicy', google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.GetPolicyRequest.SerializeToString, google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdatePolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/UpdatePolicy', google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.UpdatePolicyRequest.SerializeToString, google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateAttestor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/CreateAttestor', google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.CreateAttestorRequest.SerializeToString, google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Attestor.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetAttestor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/GetAttestor', google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.GetAttestorRequest.SerializeToString, google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Attestor.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateAttestor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/UpdateAttestor', google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.UpdateAttestorRequest.SerializeToString, google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Attestor.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListAttestors(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/ListAttestors', google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.ListAttestorsRequest.SerializeToString, google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.ListAttestorsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteAttestor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1/DeleteAttestor', google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.DeleteAttestorRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

class SystemPolicyV1Beta1Stub(object):
    """API for working with the system policy.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSystemPolicy = channel.unary_unary('/google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1/GetSystemPolicy', request_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.GetSystemPolicyRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Policy.FromString, _registered_method=True)

class SystemPolicyV1Beta1Servicer(object):
    """API for working with the system policy.
    """

    def GetSystemPolicy(self, request, context):
        """Gets the current system policy in the specified location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SystemPolicyV1Beta1Servicer_to_server(servicer, server):
    rpc_method_handlers = {'GetSystemPolicy': grpc.unary_unary_rpc_method_handler(servicer.GetSystemPolicy, request_deserializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.GetSystemPolicyRequest.FromString, response_serializer=google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Policy.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1', rpc_method_handlers)

class SystemPolicyV1Beta1(object):
    """API for working with the system policy.
    """

    @staticmethod
    def GetSystemPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1/GetSystemPolicy', google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_service__pb2.GetSystemPolicyRequest.SerializeToString, google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)