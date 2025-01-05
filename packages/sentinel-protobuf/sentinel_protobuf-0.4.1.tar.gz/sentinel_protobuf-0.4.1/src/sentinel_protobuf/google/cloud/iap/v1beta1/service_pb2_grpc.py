"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/iap/v1beta1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class IdentityAwareProxyAdminV1Beta1Stub(object):
    """APIs for Identity-Aware Proxy Admin configurations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetIamPolicy = channel.unary_unary('/google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1/SetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.GetIamPolicy = channel.unary_unary('/google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1/GetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.TestIamPermissions = channel.unary_unary('/google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1/TestIamPermissions', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, _registered_method=True)

class IdentityAwareProxyAdminV1Beta1Servicer(object):
    """APIs for Identity-Aware Proxy Admin configurations.
    """

    def SetIamPolicy(self, request, context):
        """Sets the access control policy for an Identity-Aware Proxy protected
        resource. Replaces any existing policy.
        More information about managing access via IAP can be found at:
        https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIamPolicy(self, request, context):
        """Gets the access control policy for an Identity-Aware Proxy protected
        resource.
        More information about managing access via IAP can be found at:
        https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestIamPermissions(self, request, context):
        """Returns permissions that a caller has on the Identity-Aware Proxy protected
        resource. If the resource does not exist or the caller does not have
        Identity-Aware Proxy permissions a [google.rpc.Code.PERMISSION_DENIED]
        will be returned.
        More information about managing access via IAP can be found at:
        https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_IdentityAwareProxyAdminV1Beta1Servicer_to_server(servicer, server):
    rpc_method_handlers = {'SetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.SetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'GetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.GetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'TestIamPermissions': grpc.unary_unary_rpc_method_handler(servicer.TestIamPermissions, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1', rpc_method_handlers)

class IdentityAwareProxyAdminV1Beta1(object):
    """APIs for Identity-Aware Proxy Admin configurations.
    """

    @staticmethod
    def SetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1/SetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1/GetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def TestIamPermissions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1/TestIamPermissions', google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)