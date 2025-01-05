"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.advisorynotifications.v1 import service_pb2 as google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/advisorynotifications/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class AdvisoryNotificationsServiceStub(object):
    """Service to manage Security and Privacy Notifications.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListNotifications = channel.unary_unary('/google.cloud.advisorynotifications.v1.AdvisoryNotificationsService/ListNotifications', request_serializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.ListNotificationsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.ListNotificationsResponse.FromString, _registered_method=True)
        self.GetNotification = channel.unary_unary('/google.cloud.advisorynotifications.v1.AdvisoryNotificationsService/GetNotification', request_serializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.GetNotificationRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.Notification.FromString, _registered_method=True)
        self.GetSettings = channel.unary_unary('/google.cloud.advisorynotifications.v1.AdvisoryNotificationsService/GetSettings', request_serializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.GetSettingsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.Settings.FromString, _registered_method=True)
        self.UpdateSettings = channel.unary_unary('/google.cloud.advisorynotifications.v1.AdvisoryNotificationsService/UpdateSettings', request_serializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.UpdateSettingsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.Settings.FromString, _registered_method=True)

class AdvisoryNotificationsServiceServicer(object):
    """Service to manage Security and Privacy Notifications.
    """

    def ListNotifications(self, request, context):
        """Lists notifications under a given parent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNotification(self, request, context):
        """Gets a notification.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSettings(self, request, context):
        """Get notification settings.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSettings(self, request, context):
        """Update notification settings.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AdvisoryNotificationsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListNotifications': grpc.unary_unary_rpc_method_handler(servicer.ListNotifications, request_deserializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.ListNotificationsRequest.FromString, response_serializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.ListNotificationsResponse.SerializeToString), 'GetNotification': grpc.unary_unary_rpc_method_handler(servicer.GetNotification, request_deserializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.GetNotificationRequest.FromString, response_serializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.Notification.SerializeToString), 'GetSettings': grpc.unary_unary_rpc_method_handler(servicer.GetSettings, request_deserializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.GetSettingsRequest.FromString, response_serializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.Settings.SerializeToString), 'UpdateSettings': grpc.unary_unary_rpc_method_handler(servicer.UpdateSettings, request_deserializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.UpdateSettingsRequest.FromString, response_serializer=google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.Settings.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.advisorynotifications.v1.AdvisoryNotificationsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.advisorynotifications.v1.AdvisoryNotificationsService', rpc_method_handlers)

class AdvisoryNotificationsService(object):
    """Service to manage Security and Privacy Notifications.
    """

    @staticmethod
    def ListNotifications(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.advisorynotifications.v1.AdvisoryNotificationsService/ListNotifications', google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.ListNotificationsRequest.SerializeToString, google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.ListNotificationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetNotification(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.advisorynotifications.v1.AdvisoryNotificationsService/GetNotification', google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.GetNotificationRequest.SerializeToString, google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.Notification.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetSettings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.advisorynotifications.v1.AdvisoryNotificationsService/GetSettings', google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.GetSettingsRequest.SerializeToString, google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.Settings.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateSettings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.advisorynotifications.v1.AdvisoryNotificationsService/UpdateSettings', google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.UpdateSettingsRequest.SerializeToString, google_dot_cloud_dot_advisorynotifications_dot_v1_dot_service__pb2.Settings.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)