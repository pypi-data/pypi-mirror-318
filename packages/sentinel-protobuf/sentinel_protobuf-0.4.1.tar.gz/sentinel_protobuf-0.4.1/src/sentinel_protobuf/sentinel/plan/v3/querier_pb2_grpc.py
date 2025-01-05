"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ....sentinel.plan.v3 import querier_pb2 as sentinel_dot_plan_dot_v3_dot_querier__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in sentinel/plan/v3/querier_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class QueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryPlans = channel.unary_unary('/sentinel.plan.v3.QueryService/QueryPlans', request_serializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansRequest.SerializeToString, response_deserializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansResponse.FromString, _registered_method=True)
        self.QueryPlansForProvider = channel.unary_unary('/sentinel.plan.v3.QueryService/QueryPlansForProvider', request_serializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansForProviderRequest.SerializeToString, response_deserializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansForProviderResponse.FromString, _registered_method=True)
        self.QueryPlan = channel.unary_unary('/sentinel.plan.v3.QueryService/QueryPlan', request_serializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlanRequest.SerializeToString, response_deserializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlanResponse.FromString, _registered_method=True)

class QueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def QueryPlans(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPlansForProvider(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPlan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'QueryPlans': grpc.unary_unary_rpc_method_handler(servicer.QueryPlans, request_deserializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansRequest.FromString, response_serializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansResponse.SerializeToString), 'QueryPlansForProvider': grpc.unary_unary_rpc_method_handler(servicer.QueryPlansForProvider, request_deserializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansForProviderRequest.FromString, response_serializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansForProviderResponse.SerializeToString), 'QueryPlan': grpc.unary_unary_rpc_method_handler(servicer.QueryPlan, request_deserializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlanRequest.FromString, response_serializer=sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlanResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('sentinel.plan.v3.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentinel.plan.v3.QueryService', rpc_method_handlers)

class QueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def QueryPlans(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.plan.v3.QueryService/QueryPlans', sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansRequest.SerializeToString, sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryPlansForProvider(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.plan.v3.QueryService/QueryPlansForProvider', sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansForProviderRequest.SerializeToString, sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlansForProviderResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryPlan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.plan.v3.QueryService/QueryPlan', sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlanRequest.SerializeToString, sentinel_dot_plan_dot_v3_dot_querier__pb2.QueryPlanResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)