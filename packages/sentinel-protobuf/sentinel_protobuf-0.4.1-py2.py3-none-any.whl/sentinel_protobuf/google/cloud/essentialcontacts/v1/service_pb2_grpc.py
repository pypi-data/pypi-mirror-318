"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.essentialcontacts.v1 import service_pb2 as google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/essentialcontacts/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class EssentialContactsServiceStub(object):
    """Manages contacts for important Google Cloud notifications.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateContact = channel.unary_unary('/google.cloud.essentialcontacts.v1.EssentialContactsService/CreateContact', request_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.CreateContactRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.Contact.FromString, _registered_method=True)
        self.UpdateContact = channel.unary_unary('/google.cloud.essentialcontacts.v1.EssentialContactsService/UpdateContact', request_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.UpdateContactRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.Contact.FromString, _registered_method=True)
        self.ListContacts = channel.unary_unary('/google.cloud.essentialcontacts.v1.EssentialContactsService/ListContacts', request_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ListContactsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ListContactsResponse.FromString, _registered_method=True)
        self.GetContact = channel.unary_unary('/google.cloud.essentialcontacts.v1.EssentialContactsService/GetContact', request_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.GetContactRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.Contact.FromString, _registered_method=True)
        self.DeleteContact = channel.unary_unary('/google.cloud.essentialcontacts.v1.EssentialContactsService/DeleteContact', request_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.DeleteContactRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.ComputeContacts = channel.unary_unary('/google.cloud.essentialcontacts.v1.EssentialContactsService/ComputeContacts', request_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ComputeContactsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ComputeContactsResponse.FromString, _registered_method=True)
        self.SendTestMessage = channel.unary_unary('/google.cloud.essentialcontacts.v1.EssentialContactsService/SendTestMessage', request_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.SendTestMessageRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)

class EssentialContactsServiceServicer(object):
    """Manages contacts for important Google Cloud notifications.
    """

    def CreateContact(self, request, context):
        """Adds a new contact for a resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateContact(self, request, context):
        """Updates a contact.
        Note: A contact's email address cannot be changed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListContacts(self, request, context):
        """Lists the contacts that have been set on a resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetContact(self, request, context):
        """Gets a single contact.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteContact(self, request, context):
        """Deletes a contact.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ComputeContacts(self, request, context):
        """Lists all contacts for the resource that are subscribed to the
        specified notification categories, including contacts inherited from
        any parent resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTestMessage(self, request, context):
        """Allows a contact admin to send a test message to contact to verify that it
        has been configured correctly.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_EssentialContactsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateContact': grpc.unary_unary_rpc_method_handler(servicer.CreateContact, request_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.CreateContactRequest.FromString, response_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.Contact.SerializeToString), 'UpdateContact': grpc.unary_unary_rpc_method_handler(servicer.UpdateContact, request_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.UpdateContactRequest.FromString, response_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.Contact.SerializeToString), 'ListContacts': grpc.unary_unary_rpc_method_handler(servicer.ListContacts, request_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ListContactsRequest.FromString, response_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ListContactsResponse.SerializeToString), 'GetContact': grpc.unary_unary_rpc_method_handler(servicer.GetContact, request_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.GetContactRequest.FromString, response_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.Contact.SerializeToString), 'DeleteContact': grpc.unary_unary_rpc_method_handler(servicer.DeleteContact, request_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.DeleteContactRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ComputeContacts': grpc.unary_unary_rpc_method_handler(servicer.ComputeContacts, request_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ComputeContactsRequest.FromString, response_serializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ComputeContactsResponse.SerializeToString), 'SendTestMessage': grpc.unary_unary_rpc_method_handler(servicer.SendTestMessage, request_deserializer=google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.SendTestMessageRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.essentialcontacts.v1.EssentialContactsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.essentialcontacts.v1.EssentialContactsService', rpc_method_handlers)

class EssentialContactsService(object):
    """Manages contacts for important Google Cloud notifications.
    """

    @staticmethod
    def CreateContact(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.essentialcontacts.v1.EssentialContactsService/CreateContact', google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.CreateContactRequest.SerializeToString, google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.Contact.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateContact(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.essentialcontacts.v1.EssentialContactsService/UpdateContact', google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.UpdateContactRequest.SerializeToString, google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.Contact.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListContacts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.essentialcontacts.v1.EssentialContactsService/ListContacts', google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ListContactsRequest.SerializeToString, google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ListContactsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetContact(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.essentialcontacts.v1.EssentialContactsService/GetContact', google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.GetContactRequest.SerializeToString, google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.Contact.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteContact(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.essentialcontacts.v1.EssentialContactsService/DeleteContact', google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.DeleteContactRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ComputeContacts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.essentialcontacts.v1.EssentialContactsService/ComputeContacts', google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ComputeContactsRequest.SerializeToString, google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.ComputeContactsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SendTestMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.essentialcontacts.v1.EssentialContactsService/SendTestMessage', google_dot_cloud_dot_essentialcontacts_dot_v1_dot_service__pb2.SendTestMessageRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)