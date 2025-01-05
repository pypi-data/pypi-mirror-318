"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ......google.cloud.security.privateca.v1beta1 import resources_pb2 as google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2
from ......google.cloud.security.privateca.v1beta1 import service_pb2 as google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/security/privateca/v1beta1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class CertificateAuthorityServiceStub(object):
    """[Certificate Authority Service][google.cloud.security.privateca.v1beta1.CertificateAuthorityService] manages private
    certificate authorities and issued certificates.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateCertificate = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/CreateCertificate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.CreateCertificateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.FromString, _registered_method=True)
        self.GetCertificate = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetCertificateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.FromString, _registered_method=True)
        self.ListCertificates = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificates', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificatesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificatesResponse.FromString, _registered_method=True)
        self.RevokeCertificate = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/RevokeCertificate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.RevokeCertificateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.FromString, _registered_method=True)
        self.UpdateCertificate = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.UpdateCertificateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.FromString, _registered_method=True)
        self.ActivateCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ActivateCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ActivateCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/CreateCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.CreateCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DisableCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/DisableCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.DisableCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.EnableCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/EnableCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.EnableCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.FetchCertificateAuthorityCsr = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/FetchCertificateAuthorityCsr', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.FetchCertificateAuthorityCsrRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.FetchCertificateAuthorityCsrResponse.FromString, _registered_method=True)
        self.GetCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.CertificateAuthority.FromString, _registered_method=True)
        self.ListCertificateAuthorities = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificateAuthorities', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateAuthoritiesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateAuthoritiesResponse.FromString, _registered_method=True)
        self.RestoreCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/RestoreCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.RestoreCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ScheduleDeleteCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ScheduleDeleteCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ScheduleDeleteCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.UpdateCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.GetCertificateRevocationList = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificateRevocationList', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetCertificateRevocationListRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.CertificateRevocationList.FromString, _registered_method=True)
        self.ListCertificateRevocationLists = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificateRevocationLists', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateRevocationListsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateRevocationListsResponse.FromString, _registered_method=True)
        self.UpdateCertificateRevocationList = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificateRevocationList', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.UpdateCertificateRevocationListRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.GetReusableConfig = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetReusableConfig', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetReusableConfigRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.ReusableConfig.FromString, _registered_method=True)
        self.ListReusableConfigs = channel.unary_unary('/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListReusableConfigs', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListReusableConfigsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListReusableConfigsResponse.FromString, _registered_method=True)

class CertificateAuthorityServiceServicer(object):
    """[Certificate Authority Service][google.cloud.security.privateca.v1beta1.CertificateAuthorityService] manages private
    certificate authorities and issued certificates.
    """

    def CreateCertificate(self, request, context):
        """Create a new [Certificate][google.cloud.security.privateca.v1beta1.Certificate] in a given Project, Location from a particular
        [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCertificate(self, request, context):
        """Returns a [Certificate][google.cloud.security.privateca.v1beta1.Certificate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCertificates(self, request, context):
        """Lists [Certificates][google.cloud.security.privateca.v1beta1.Certificate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeCertificate(self, request, context):
        """Revoke a [Certificate][google.cloud.security.privateca.v1beta1.Certificate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCertificate(self, request, context):
        """Update a [Certificate][google.cloud.security.privateca.v1beta1.Certificate]. Currently, the only field you can update is the
        [labels][google.cloud.security.privateca.v1beta1.Certificate.labels] field.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActivateCertificateAuthority(self, request, context):
        """Activate a [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority] that is in state
        [PENDING_ACTIVATION][google.cloud.security.privateca.v1beta1.CertificateAuthority.State.PENDING_ACTIVATION] and is
        of type [SUBORDINATE][google.cloud.security.privateca.v1beta1.CertificateAuthority.Type.SUBORDINATE]. After the
        parent Certificate Authority signs a certificate signing request from
        [FetchCertificateAuthorityCsr][google.cloud.security.privateca.v1beta1.CertificateAuthorityService.FetchCertificateAuthorityCsr], this method can complete the activation
        process.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCertificateAuthority(self, request, context):
        """Create a new [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority] in a given Project and Location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableCertificateAuthority(self, request, context):
        """Disable a [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableCertificateAuthority(self, request, context):
        """Enable a [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchCertificateAuthorityCsr(self, request, context):
        """Fetch a certificate signing request (CSR) from a [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority]
        that is in state
        [PENDING_ACTIVATION][google.cloud.security.privateca.v1beta1.CertificateAuthority.State.PENDING_ACTIVATION] and is
        of type [SUBORDINATE][google.cloud.security.privateca.v1beta1.CertificateAuthority.Type.SUBORDINATE]. The CSR must
        then be signed by the desired parent Certificate Authority, which could be
        another [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority] resource, or could be an on-prem
        certificate authority. See also [ActivateCertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthorityService.ActivateCertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCertificateAuthority(self, request, context):
        """Returns a [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCertificateAuthorities(self, request, context):
        """Lists [CertificateAuthorities][google.cloud.security.privateca.v1beta1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestoreCertificateAuthority(self, request, context):
        """Restore a [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority] that is scheduled for deletion.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScheduleDeleteCertificateAuthority(self, request, context):
        """Schedule a [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority] for deletion.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCertificateAuthority(self, request, context):
        """Update a [CertificateAuthority][google.cloud.security.privateca.v1beta1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCertificateRevocationList(self, request, context):
        """Returns a [CertificateRevocationList][google.cloud.security.privateca.v1beta1.CertificateRevocationList].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCertificateRevocationLists(self, request, context):
        """Lists [CertificateRevocationLists][google.cloud.security.privateca.v1beta1.CertificateRevocationList].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCertificateRevocationList(self, request, context):
        """Update a [CertificateRevocationList][google.cloud.security.privateca.v1beta1.CertificateRevocationList].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReusableConfig(self, request, context):
        """Returns a [ReusableConfig][google.cloud.security.privateca.v1beta1.ReusableConfig].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListReusableConfigs(self, request, context):
        """Lists [ReusableConfigs][google.cloud.security.privateca.v1beta1.ReusableConfig].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_CertificateAuthorityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateCertificate': grpc.unary_unary_rpc_method_handler(servicer.CreateCertificate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.CreateCertificateRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.SerializeToString), 'GetCertificate': grpc.unary_unary_rpc_method_handler(servicer.GetCertificate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetCertificateRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.SerializeToString), 'ListCertificates': grpc.unary_unary_rpc_method_handler(servicer.ListCertificates, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificatesRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificatesResponse.SerializeToString), 'RevokeCertificate': grpc.unary_unary_rpc_method_handler(servicer.RevokeCertificate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.RevokeCertificateRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.SerializeToString), 'UpdateCertificate': grpc.unary_unary_rpc_method_handler(servicer.UpdateCertificate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.UpdateCertificateRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.SerializeToString), 'ActivateCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.ActivateCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ActivateCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.CreateCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.CreateCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DisableCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.DisableCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.DisableCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'EnableCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.EnableCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.EnableCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'FetchCertificateAuthorityCsr': grpc.unary_unary_rpc_method_handler(servicer.FetchCertificateAuthorityCsr, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.FetchCertificateAuthorityCsrRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.FetchCertificateAuthorityCsrResponse.SerializeToString), 'GetCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.GetCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetCertificateAuthorityRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.CertificateAuthority.SerializeToString), 'ListCertificateAuthorities': grpc.unary_unary_rpc_method_handler(servicer.ListCertificateAuthorities, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateAuthoritiesRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateAuthoritiesResponse.SerializeToString), 'RestoreCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.RestoreCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.RestoreCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ScheduleDeleteCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.ScheduleDeleteCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ScheduleDeleteCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.UpdateCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.UpdateCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'GetCertificateRevocationList': grpc.unary_unary_rpc_method_handler(servicer.GetCertificateRevocationList, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetCertificateRevocationListRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.CertificateRevocationList.SerializeToString), 'ListCertificateRevocationLists': grpc.unary_unary_rpc_method_handler(servicer.ListCertificateRevocationLists, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateRevocationListsRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateRevocationListsResponse.SerializeToString), 'UpdateCertificateRevocationList': grpc.unary_unary_rpc_method_handler(servicer.UpdateCertificateRevocationList, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.UpdateCertificateRevocationListRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'GetReusableConfig': grpc.unary_unary_rpc_method_handler(servicer.GetReusableConfig, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetReusableConfigRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.ReusableConfig.SerializeToString), 'ListReusableConfigs': grpc.unary_unary_rpc_method_handler(servicer.ListReusableConfigs, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListReusableConfigsRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListReusableConfigsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.security.privateca.v1beta1.CertificateAuthorityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.security.privateca.v1beta1.CertificateAuthorityService', rpc_method_handlers)

class CertificateAuthorityService(object):
    """[Certificate Authority Service][google.cloud.security.privateca.v1beta1.CertificateAuthorityService] manages private
    certificate authorities and issued certificates.
    """

    @staticmethod
    def CreateCertificate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/CreateCertificate', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.CreateCertificateRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCertificate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificate', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetCertificateRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCertificates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificates', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificatesRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificatesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RevokeCertificate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/RevokeCertificate', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.RevokeCertificateRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCertificate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificate', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.UpdateCertificateRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.Certificate.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ActivateCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ActivateCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ActivateCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/CreateCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.CreateCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DisableCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/DisableCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.DisableCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def EnableCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/EnableCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.EnableCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def FetchCertificateAuthorityCsr(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/FetchCertificateAuthorityCsr', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.FetchCertificateAuthorityCsrRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.FetchCertificateAuthorityCsrResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetCertificateAuthorityRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.CertificateAuthority.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCertificateAuthorities(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificateAuthorities', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateAuthoritiesRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateAuthoritiesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RestoreCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/RestoreCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.RestoreCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ScheduleDeleteCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ScheduleDeleteCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ScheduleDeleteCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.UpdateCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCertificateRevocationList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificateRevocationList', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetCertificateRevocationListRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.CertificateRevocationList.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCertificateRevocationLists(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificateRevocationLists', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateRevocationListsRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListCertificateRevocationListsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCertificateRevocationList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificateRevocationList', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.UpdateCertificateRevocationListRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetReusableConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetReusableConfig', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.GetReusableConfigRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_resources__pb2.ReusableConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListReusableConfigs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListReusableConfigs', google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListReusableConfigsRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1beta1_dot_service__pb2.ListReusableConfigsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)