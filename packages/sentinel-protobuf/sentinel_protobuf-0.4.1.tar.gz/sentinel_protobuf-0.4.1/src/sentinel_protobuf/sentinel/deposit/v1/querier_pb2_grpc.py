"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ....sentinel.deposit.v1 import querier_pb2 as sentinel_dot_deposit_dot_v1_dot_querier__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in sentinel/deposit/v1/querier_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class QueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryDeposits = channel.unary_unary('/sentinel.deposit.v1.QueryService/QueryDeposits', request_serializer=sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositsRequest.SerializeToString, response_deserializer=sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositsResponse.FromString, _registered_method=True)
        self.QueryDeposit = channel.unary_unary('/sentinel.deposit.v1.QueryService/QueryDeposit', request_serializer=sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositRequest.SerializeToString, response_deserializer=sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositResponse.FromString, _registered_method=True)

class QueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def QueryDeposits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryDeposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'QueryDeposits': grpc.unary_unary_rpc_method_handler(servicer.QueryDeposits, request_deserializer=sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositsRequest.FromString, response_serializer=sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositsResponse.SerializeToString), 'QueryDeposit': grpc.unary_unary_rpc_method_handler(servicer.QueryDeposit, request_deserializer=sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositRequest.FromString, response_serializer=sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('sentinel.deposit.v1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentinel.deposit.v1.QueryService', rpc_method_handlers)

class QueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def QueryDeposits(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.deposit.v1.QueryService/QueryDeposits', sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositsRequest.SerializeToString, sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryDeposit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.deposit.v1.QueryService/QueryDeposit', sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositRequest.SerializeToString, sentinel_dot_deposit_dot_v1_dot_querier__pb2.QueryDepositResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)