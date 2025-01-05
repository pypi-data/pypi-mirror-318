"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.confidentialcomputing.v1 import service_pb2 as google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/confidentialcomputing/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class ConfidentialComputingStub(object):
    """Service describing handlers for resources
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateChallenge = channel.unary_unary('/google.cloud.confidentialcomputing.v1.ConfidentialComputing/CreateChallenge', request_serializer=google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.CreateChallengeRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.Challenge.FromString, _registered_method=True)
        self.VerifyAttestation = channel.unary_unary('/google.cloud.confidentialcomputing.v1.ConfidentialComputing/VerifyAttestation', request_serializer=google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.VerifyAttestationRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.VerifyAttestationResponse.FromString, _registered_method=True)

class ConfidentialComputingServicer(object):
    """Service describing handlers for resources
    """

    def CreateChallenge(self, request, context):
        """Creates a new Challenge in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyAttestation(self, request, context):
        """Verifies the provided attestation info, returning a signed OIDC token.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ConfidentialComputingServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateChallenge': grpc.unary_unary_rpc_method_handler(servicer.CreateChallenge, request_deserializer=google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.CreateChallengeRequest.FromString, response_serializer=google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.Challenge.SerializeToString), 'VerifyAttestation': grpc.unary_unary_rpc_method_handler(servicer.VerifyAttestation, request_deserializer=google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.VerifyAttestationRequest.FromString, response_serializer=google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.VerifyAttestationResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.confidentialcomputing.v1.ConfidentialComputing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.confidentialcomputing.v1.ConfidentialComputing', rpc_method_handlers)

class ConfidentialComputing(object):
    """Service describing handlers for resources
    """

    @staticmethod
    def CreateChallenge(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.confidentialcomputing.v1.ConfidentialComputing/CreateChallenge', google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.CreateChallengeRequest.SerializeToString, google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.Challenge.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def VerifyAttestation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.confidentialcomputing.v1.ConfidentialComputing/VerifyAttestation', google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.VerifyAttestationRequest.SerializeToString, google_dot_cloud_dot_confidentialcomputing_dot_v1_dot_service__pb2.VerifyAttestationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)