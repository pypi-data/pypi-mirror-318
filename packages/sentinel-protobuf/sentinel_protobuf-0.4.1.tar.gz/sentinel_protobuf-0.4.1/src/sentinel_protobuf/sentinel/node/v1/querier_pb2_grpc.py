"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ....sentinel.node.v1 import querier_pb2 as sentinel_dot_node_dot_v1_dot_querier__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in sentinel/node/v1/querier_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class QueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryNodes = channel.unary_unary('/sentinel.node.v1.QueryService/QueryNodes', request_serializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesRequest.SerializeToString, response_deserializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesResponse.FromString, _registered_method=True)
        self.QueryNodesForProvider = channel.unary_unary('/sentinel.node.v1.QueryService/QueryNodesForProvider', request_serializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesForProviderRequest.SerializeToString, response_deserializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesForProviderResponse.FromString, _registered_method=True)
        self.QueryNode = channel.unary_unary('/sentinel.node.v1.QueryService/QueryNode', request_serializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodeRequest.SerializeToString, response_deserializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodeResponse.FromString, _registered_method=True)
        self.QueryParams = channel.unary_unary('/sentinel.node.v1.QueryService/QueryParams', request_serializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryParamsRequest.SerializeToString, response_deserializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryParamsResponse.FromString, _registered_method=True)

class QueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def QueryNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryNodesForProvider(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryNode(self, request, context):
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
    rpc_method_handlers = {'QueryNodes': grpc.unary_unary_rpc_method_handler(servicer.QueryNodes, request_deserializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesRequest.FromString, response_serializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesResponse.SerializeToString), 'QueryNodesForProvider': grpc.unary_unary_rpc_method_handler(servicer.QueryNodesForProvider, request_deserializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesForProviderRequest.FromString, response_serializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesForProviderResponse.SerializeToString), 'QueryNode': grpc.unary_unary_rpc_method_handler(servicer.QueryNode, request_deserializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodeRequest.FromString, response_serializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodeResponse.SerializeToString), 'QueryParams': grpc.unary_unary_rpc_method_handler(servicer.QueryParams, request_deserializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryParamsRequest.FromString, response_serializer=sentinel_dot_node_dot_v1_dot_querier__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('sentinel.node.v1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentinel.node.v1.QueryService', rpc_method_handlers)

class QueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def QueryNodes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.node.v1.QueryService/QueryNodes', sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesRequest.SerializeToString, sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryNodesForProvider(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.node.v1.QueryService/QueryNodesForProvider', sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesForProviderRequest.SerializeToString, sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodesForProviderResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryNode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.node.v1.QueryService/QueryNode', sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodeRequest.SerializeToString, sentinel_dot_node_dot_v1_dot_querier__pb2.QueryNodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryParams(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.node.v1.QueryService/QueryParams', sentinel_dot_node_dot_v1_dot_querier__pb2.QueryParamsRequest.SerializeToString, sentinel_dot_node_dot_v1_dot_querier__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)