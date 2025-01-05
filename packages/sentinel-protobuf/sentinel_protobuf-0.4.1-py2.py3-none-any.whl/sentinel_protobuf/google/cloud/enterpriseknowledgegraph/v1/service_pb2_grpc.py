"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.enterpriseknowledgegraph.v1 import service_pb2 as google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/enterpriseknowledgegraph/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class EnterpriseKnowledgeGraphServiceStub(object):
    """APIs for enterprise knowledge graph product.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateEntityReconciliationJob = channel.unary_unary('/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/CreateEntityReconciliationJob', request_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.CreateEntityReconciliationJobRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.EntityReconciliationJob.FromString, _registered_method=True)
        self.GetEntityReconciliationJob = channel.unary_unary('/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/GetEntityReconciliationJob', request_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.GetEntityReconciliationJobRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.EntityReconciliationJob.FromString, _registered_method=True)
        self.ListEntityReconciliationJobs = channel.unary_unary('/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/ListEntityReconciliationJobs', request_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.ListEntityReconciliationJobsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.ListEntityReconciliationJobsResponse.FromString, _registered_method=True)
        self.CancelEntityReconciliationJob = channel.unary_unary('/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/CancelEntityReconciliationJob', request_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.CancelEntityReconciliationJobRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.DeleteEntityReconciliationJob = channel.unary_unary('/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/DeleteEntityReconciliationJob', request_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.DeleteEntityReconciliationJobRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.Lookup = channel.unary_unary('/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/Lookup', request_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupResponse.FromString, _registered_method=True)
        self.Search = channel.unary_unary('/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/Search', request_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchResponse.FromString, _registered_method=True)
        self.LookupPublicKg = channel.unary_unary('/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/LookupPublicKg', request_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupPublicKgRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupPublicKgResponse.FromString, _registered_method=True)
        self.SearchPublicKg = channel.unary_unary('/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/SearchPublicKg', request_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchPublicKgRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchPublicKgResponse.FromString, _registered_method=True)

class EnterpriseKnowledgeGraphServiceServicer(object):
    """APIs for enterprise knowledge graph product.
    """

    def CreateEntityReconciliationJob(self, request, context):
        """Creates a EntityReconciliationJob. A EntityReconciliationJob once created
        will right away be attempted to start.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEntityReconciliationJob(self, request, context):
        """Gets a EntityReconciliationJob.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEntityReconciliationJobs(self, request, context):
        """Lists Entity Reconciliation Jobs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelEntityReconciliationJob(self, request, context):
        """Cancels a EntityReconciliationJob. Success of cancellation is not
        guaranteed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEntityReconciliationJob(self, request, context):
        """Deletes a EntityReconciliationJob.
        It only deletes the job when the job state is in FAILED, SUCCEEDED, and
        CANCELLED.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Lookup(self, request, context):
        """Finds the Cloud KG entities with CKG ID(s).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Searches the Cloud KG entities with entity name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupPublicKg(self, request, context):
        """Finds the public KG entities with public KG ID(s).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchPublicKg(self, request, context):
        """Searches the public KG entities with entity name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_EnterpriseKnowledgeGraphServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateEntityReconciliationJob': grpc.unary_unary_rpc_method_handler(servicer.CreateEntityReconciliationJob, request_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.CreateEntityReconciliationJobRequest.FromString, response_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.EntityReconciliationJob.SerializeToString), 'GetEntityReconciliationJob': grpc.unary_unary_rpc_method_handler(servicer.GetEntityReconciliationJob, request_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.GetEntityReconciliationJobRequest.FromString, response_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.EntityReconciliationJob.SerializeToString), 'ListEntityReconciliationJobs': grpc.unary_unary_rpc_method_handler(servicer.ListEntityReconciliationJobs, request_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.ListEntityReconciliationJobsRequest.FromString, response_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.ListEntityReconciliationJobsResponse.SerializeToString), 'CancelEntityReconciliationJob': grpc.unary_unary_rpc_method_handler(servicer.CancelEntityReconciliationJob, request_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.CancelEntityReconciliationJobRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'DeleteEntityReconciliationJob': grpc.unary_unary_rpc_method_handler(servicer.DeleteEntityReconciliationJob, request_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.DeleteEntityReconciliationJobRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'Lookup': grpc.unary_unary_rpc_method_handler(servicer.Lookup, request_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupRequest.FromString, response_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupResponse.SerializeToString), 'Search': grpc.unary_unary_rpc_method_handler(servicer.Search, request_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchRequest.FromString, response_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchResponse.SerializeToString), 'LookupPublicKg': grpc.unary_unary_rpc_method_handler(servicer.LookupPublicKg, request_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupPublicKgRequest.FromString, response_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupPublicKgResponse.SerializeToString), 'SearchPublicKg': grpc.unary_unary_rpc_method_handler(servicer.SearchPublicKg, request_deserializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchPublicKgRequest.FromString, response_serializer=google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchPublicKgResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService', rpc_method_handlers)

class EnterpriseKnowledgeGraphService(object):
    """APIs for enterprise knowledge graph product.
    """

    @staticmethod
    def CreateEntityReconciliationJob(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/CreateEntityReconciliationJob', google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.CreateEntityReconciliationJobRequest.SerializeToString, google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.EntityReconciliationJob.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetEntityReconciliationJob(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/GetEntityReconciliationJob', google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.GetEntityReconciliationJobRequest.SerializeToString, google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.EntityReconciliationJob.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListEntityReconciliationJobs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/ListEntityReconciliationJobs', google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.ListEntityReconciliationJobsRequest.SerializeToString, google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.ListEntityReconciliationJobsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CancelEntityReconciliationJob(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/CancelEntityReconciliationJob', google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.CancelEntityReconciliationJobRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteEntityReconciliationJob(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/DeleteEntityReconciliationJob', google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.DeleteEntityReconciliationJobRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def Lookup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/Lookup', google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupRequest.SerializeToString, google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def Search(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/Search', google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchRequest.SerializeToString, google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def LookupPublicKg(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/LookupPublicKg', google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupPublicKgRequest.SerializeToString, google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.LookupPublicKgResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SearchPublicKg(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService/SearchPublicKg', google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchPublicKgRequest.SerializeToString, google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_service__pb2.SearchPublicKgResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)