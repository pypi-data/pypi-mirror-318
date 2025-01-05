"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ......google.cloud.security.publicca.v1 import resources_pb2 as google_dot_cloud_dot_security_dot_publicca_dot_v1_dot_resources__pb2
from ......google.cloud.security.publicca.v1 import service_pb2 as google_dot_cloud_dot_security_dot_publicca_dot_v1_dot_service__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/security/publicca/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class PublicCertificateAuthorityServiceStub(object):
    """Manages the resources required for ACME [external account
    binding](https://tools.ietf.org/html/rfc8555#section-7.3.4) for
    the public certificate authority service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateExternalAccountKey = channel.unary_unary('/google.cloud.security.publicca.v1.PublicCertificateAuthorityService/CreateExternalAccountKey', request_serializer=google_dot_cloud_dot_security_dot_publicca_dot_v1_dot_service__pb2.CreateExternalAccountKeyRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_publicca_dot_v1_dot_resources__pb2.ExternalAccountKey.FromString, _registered_method=True)

class PublicCertificateAuthorityServiceServicer(object):
    """Manages the resources required for ACME [external account
    binding](https://tools.ietf.org/html/rfc8555#section-7.3.4) for
    the public certificate authority service.
    """

    def CreateExternalAccountKey(self, request, context):
        """Creates a new
        [ExternalAccountKey][google.cloud.security.publicca.v1.ExternalAccountKey]
        bound to the project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_PublicCertificateAuthorityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateExternalAccountKey': grpc.unary_unary_rpc_method_handler(servicer.CreateExternalAccountKey, request_deserializer=google_dot_cloud_dot_security_dot_publicca_dot_v1_dot_service__pb2.CreateExternalAccountKeyRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_publicca_dot_v1_dot_resources__pb2.ExternalAccountKey.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.security.publicca.v1.PublicCertificateAuthorityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.security.publicca.v1.PublicCertificateAuthorityService', rpc_method_handlers)

class PublicCertificateAuthorityService(object):
    """Manages the resources required for ACME [external account
    binding](https://tools.ietf.org/html/rfc8555#section-7.3.4) for
    the public certificate authority service.
    """

    @staticmethod
    def CreateExternalAccountKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.publicca.v1.PublicCertificateAuthorityService/CreateExternalAccountKey', google_dot_cloud_dot_security_dot_publicca_dot_v1_dot_service__pb2.CreateExternalAccountKeyRequest.SerializeToString, google_dot_cloud_dot_security_dot_publicca_dot_v1_dot_resources__pb2.ExternalAccountKey.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)