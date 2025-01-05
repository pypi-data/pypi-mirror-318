"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ....sentinel.subscription.v3 import querier_pb2 as sentinel_dot_subscription_dot_v3_dot_querier__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in sentinel/subscription/v3/querier_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class QueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QuerySubscriptions = channel.unary_unary('/sentinel.subscription.v3.QueryService/QuerySubscriptions', request_serializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsResponse.FromString, _registered_method=True)
        self.QuerySubscriptionsForAccount = channel.unary_unary('/sentinel.subscription.v3.QueryService/QuerySubscriptionsForAccount', request_serializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForAccountRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForAccountResponse.FromString, _registered_method=True)
        self.QuerySubscriptionsForPlan = channel.unary_unary('/sentinel.subscription.v3.QueryService/QuerySubscriptionsForPlan', request_serializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForPlanRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForPlanResponse.FromString, _registered_method=True)
        self.QuerySubscription = channel.unary_unary('/sentinel.subscription.v3.QueryService/QuerySubscription', request_serializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionResponse.FromString, _registered_method=True)

class QueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def QuerySubscriptions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySubscriptionsForAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySubscriptionsForPlan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySubscription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'QuerySubscriptions': grpc.unary_unary_rpc_method_handler(servicer.QuerySubscriptions, request_deserializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsResponse.SerializeToString), 'QuerySubscriptionsForAccount': grpc.unary_unary_rpc_method_handler(servicer.QuerySubscriptionsForAccount, request_deserializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForAccountRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForAccountResponse.SerializeToString), 'QuerySubscriptionsForPlan': grpc.unary_unary_rpc_method_handler(servicer.QuerySubscriptionsForPlan, request_deserializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForPlanRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForPlanResponse.SerializeToString), 'QuerySubscription': grpc.unary_unary_rpc_method_handler(servicer.QuerySubscription, request_deserializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('sentinel.subscription.v3.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentinel.subscription.v3.QueryService', rpc_method_handlers)

class QueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def QuerySubscriptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v3.QueryService/QuerySubscriptions', sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsRequest.SerializeToString, sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySubscriptionsForAccount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v3.QueryService/QuerySubscriptionsForAccount', sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForAccountRequest.SerializeToString, sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySubscriptionsForPlan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v3.QueryService/QuerySubscriptionsForPlan', sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForPlanRequest.SerializeToString, sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionsForPlanResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySubscription(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v3.QueryService/QuerySubscription', sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionRequest.SerializeToString, sentinel_dot_subscription_dot_v3_dot_querier__pb2.QuerySubscriptionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)