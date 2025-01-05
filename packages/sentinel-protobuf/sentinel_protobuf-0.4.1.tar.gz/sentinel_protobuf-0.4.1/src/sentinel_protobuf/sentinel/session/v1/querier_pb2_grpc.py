"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ....sentinel.session.v1 import querier_pb2 as sentinel_dot_session_dot_v1_dot_querier__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in sentinel/session/v1/querier_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class QueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QuerySessions = channel.unary_unary('/sentinel.session.v1.QueryService/QuerySessions', request_serializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsResponse.FromString, _registered_method=True)
        self.QuerySessionsForAddress = channel.unary_unary('/sentinel.session.v1.QueryService/QuerySessionsForAddress', request_serializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsForAddressRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsForAddressResponse.FromString, _registered_method=True)
        self.QuerySession = channel.unary_unary('/sentinel.session.v1.QueryService/QuerySession', request_serializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionResponse.FromString, _registered_method=True)
        self.QueryParams = channel.unary_unary('/sentinel.session.v1.QueryService/QueryParams', request_serializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QueryParamsRequest.SerializeToString, response_deserializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QueryParamsResponse.FromString, _registered_method=True)

class QueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def QuerySessions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySessionsForAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'QuerySessions': grpc.unary_unary_rpc_method_handler(servicer.QuerySessions, request_deserializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsRequest.FromString, response_serializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsResponse.SerializeToString), 'QuerySessionsForAddress': grpc.unary_unary_rpc_method_handler(servicer.QuerySessionsForAddress, request_deserializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsForAddressRequest.FromString, response_serializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsForAddressResponse.SerializeToString), 'QuerySession': grpc.unary_unary_rpc_method_handler(servicer.QuerySession, request_deserializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionRequest.FromString, response_serializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionResponse.SerializeToString), 'QueryParams': grpc.unary_unary_rpc_method_handler(servicer.QueryParams, request_deserializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QueryParamsRequest.FromString, response_serializer=sentinel_dot_session_dot_v1_dot_querier__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('sentinel.session.v1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentinel.session.v1.QueryService', rpc_method_handlers)

class QueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def QuerySessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v1.QueryService/QuerySessions', sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsRequest.SerializeToString, sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySessionsForAddress(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v1.QueryService/QuerySessionsForAddress', sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsForAddressRequest.SerializeToString, sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionsForAddressResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v1.QueryService/QuerySession', sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionRequest.SerializeToString, sentinel_dot_session_dot_v1_dot_querier__pb2.QuerySessionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryParams(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.session.v1.QueryService/QueryParams', sentinel_dot_session_dot_v1_dot_querier__pb2.QueryParamsRequest.SerializeToString, sentinel_dot_session_dot_v1_dot_querier__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)