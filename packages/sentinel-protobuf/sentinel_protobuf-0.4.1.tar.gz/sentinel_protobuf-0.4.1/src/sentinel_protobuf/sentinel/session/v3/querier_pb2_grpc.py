"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ....sentinel.session.v3 import querier_pb2 as sentinel_dot_session_dot_v3_dot_querier__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in sentinel/session/v3/querier_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class QueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QuerySessions = channel.unary_unary('/sentinel.session.v3.QueryService/QuerySessions', request_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsResponse.FromString, _registered_method=True)
        self.QuerySessionsForAccount = channel.unary_unary('/sentinel.session.v3.QueryService/QuerySessionsForAccount', request_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAccountRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAccountResponse.FromString, _registered_method=True)
        self.QuerySessionsForNode = channel.unary_unary('/sentinel.session.v3.QueryService/QuerySessionsForNode', request_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForNodeRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForNodeResponse.FromString, _registered_method=True)
        self.QuerySessionsForSubscription = channel.unary_unary('/sentinel.session.v3.QueryService/QuerySessionsForSubscription', request_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForSubscriptionRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForSubscriptionResponse.FromString, _registered_method=True)
        self.QuerySessionsForAllocation = channel.unary_unary('/sentinel.session.v3.QueryService/QuerySessionsForAllocation', request_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAllocationRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAllocationResponse.FromString, _registered_method=True)
        self.QuerySession = channel.unary_unary('/sentinel.session.v3.QueryService/QuerySession', request_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionResponse.FromString, _registered_method=True)

class QueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def QuerySessions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySessionsForAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySessionsForNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySessionsForSubscription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySessionsForAllocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'QuerySessions': grpc.unary_unary_rpc_method_handler(servicer.QuerySessions, request_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsRequest.FromString, response_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsResponse.SerializeToString), 'QuerySessionsForAccount': grpc.unary_unary_rpc_method_handler(servicer.QuerySessionsForAccount, request_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAccountRequest.FromString, response_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAccountResponse.SerializeToString), 'QuerySessionsForNode': grpc.unary_unary_rpc_method_handler(servicer.QuerySessionsForNode, request_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForNodeRequest.FromString, response_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForNodeResponse.SerializeToString), 'QuerySessionsForSubscription': grpc.unary_unary_rpc_method_handler(servicer.QuerySessionsForSubscription, request_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForSubscriptionRequest.FromString, response_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForSubscriptionResponse.SerializeToString), 'QuerySessionsForAllocation': grpc.unary_unary_rpc_method_handler(servicer.QuerySessionsForAllocation, request_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAllocationRequest.FromString, response_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAllocationResponse.SerializeToString), 'QuerySession': grpc.unary_unary_rpc_method_handler(servicer.QuerySession, request_deserializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionRequest.FromString, response_serializer=sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('sentinel.session.v3.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentinel.session.v3.QueryService', rpc_method_handlers)

class QueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def QuerySessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v3.QueryService/QuerySessions', sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsRequest.SerializeToString, sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySessionsForAccount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v3.QueryService/QuerySessionsForAccount', sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAccountRequest.SerializeToString, sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySessionsForNode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v3.QueryService/QuerySessionsForNode', sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForNodeRequest.SerializeToString, sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForNodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySessionsForSubscription(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v3.QueryService/QuerySessionsForSubscription', sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForSubscriptionRequest.SerializeToString, sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForSubscriptionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySessionsForAllocation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v3.QueryService/QuerySessionsForAllocation', sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAllocationRequest.SerializeToString, sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionsForAllocationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v3.QueryService/QuerySession', sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionRequest.SerializeToString, sentinel_dot_session_dot_v3_dot_querier__pb2.QuerySessionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)