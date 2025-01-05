"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.channel.v1 import channel_partner_links_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2
from .....google.cloud.channel.v1 import customers_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2
from .....google.cloud.channel.v1 import entitlements_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_entitlements__pb2
from .....google.cloud.channel.v1 import offers_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_offers__pb2
from .....google.cloud.channel.v1 import repricing_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2
from .....google.cloud.channel.v1 import service_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_service__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/channel/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class CloudChannelServiceStub(object):
    """CloudChannelService lets Google cloud resellers and distributors manage
    their customers, channel partners, entitlements, and reports.

    Using this service:
    1. Resellers and distributors can manage a customer entity.
    2. Distributors can register an authorized reseller in their channel and
    provide them with delegated admin access.
    3. Resellers and distributors can manage customer entitlements.

    CloudChannelService exposes the following resources:
    - [Customer][google.cloud.channel.v1.Customer]s: An entity-usually an
    enterprise-managed by a reseller or distributor.

    - [Entitlement][google.cloud.channel.v1.Entitlement]s: An entity that
    provides a customer with the means to use a service. Entitlements are created
    or updated as a result of a successful fulfillment.

    - [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]s: An
    entity that identifies links between distributors and their indirect
    resellers in a channel.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListCustomers = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListCustomers', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomersResponse.FromString, _registered_method=True)
        self.GetCustomer = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/GetCustomer', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetCustomerRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.FromString, _registered_method=True)
        self.CheckCloudIdentityAccountsExist = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/CheckCloudIdentityAccountsExist', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CheckCloudIdentityAccountsExistRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CheckCloudIdentityAccountsExistResponse.FromString, _registered_method=True)
        self.CreateCustomer = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/CreateCustomer', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateCustomerRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.FromString, _registered_method=True)
        self.UpdateCustomer = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/UpdateCustomer', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateCustomerRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.FromString, _registered_method=True)
        self.DeleteCustomer = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/DeleteCustomer', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.DeleteCustomerRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.ImportCustomer = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ImportCustomer', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ImportCustomerRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.FromString, _registered_method=True)
        self.ProvisionCloudIdentity = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ProvisionCloudIdentity', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ProvisionCloudIdentityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListEntitlements = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListEntitlements', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementsResponse.FromString, _registered_method=True)
        self.ListTransferableSkus = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListTransferableSkus', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableSkusRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableSkusResponse.FromString, _registered_method=True)
        self.ListTransferableOffers = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListTransferableOffers', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableOffersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableOffersResponse.FromString, _registered_method=True)
        self.GetEntitlement = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/GetEntitlement', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetEntitlementRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_entitlements__pb2.Entitlement.FromString, _registered_method=True)
        self.CreateEntitlement = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/CreateEntitlement', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateEntitlementRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ChangeParameters = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ChangeParameters', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ChangeParametersRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ChangeRenewalSettings = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ChangeRenewalSettings', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ChangeRenewalSettingsRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ChangeOffer = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ChangeOffer', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ChangeOfferRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.StartPaidService = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/StartPaidService', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.StartPaidServiceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.SuspendEntitlement = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/SuspendEntitlement', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.SuspendEntitlementRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CancelEntitlement = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/CancelEntitlement', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CancelEntitlementRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ActivateEntitlement = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ActivateEntitlement', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ActivateEntitlementRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.TransferEntitlements = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/TransferEntitlements', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.TransferEntitlementsRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.TransferEntitlementsToGoogle = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/TransferEntitlementsToGoogle', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.TransferEntitlementsToGoogleRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListChannelPartnerLinks = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListChannelPartnerLinks', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerLinksRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerLinksResponse.FromString, _registered_method=True)
        self.GetChannelPartnerLink = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/GetChannelPartnerLink', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetChannelPartnerLinkRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2.ChannelPartnerLink.FromString, _registered_method=True)
        self.CreateChannelPartnerLink = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/CreateChannelPartnerLink', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateChannelPartnerLinkRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2.ChannelPartnerLink.FromString, _registered_method=True)
        self.UpdateChannelPartnerLink = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/UpdateChannelPartnerLink', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateChannelPartnerLinkRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2.ChannelPartnerLink.FromString, _registered_method=True)
        self.GetCustomerRepricingConfig = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/GetCustomerRepricingConfig', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetCustomerRepricingConfigRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.CustomerRepricingConfig.FromString, _registered_method=True)
        self.ListCustomerRepricingConfigs = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListCustomerRepricingConfigs', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomerRepricingConfigsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomerRepricingConfigsResponse.FromString, _registered_method=True)
        self.CreateCustomerRepricingConfig = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/CreateCustomerRepricingConfig', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateCustomerRepricingConfigRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.CustomerRepricingConfig.FromString, _registered_method=True)
        self.UpdateCustomerRepricingConfig = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/UpdateCustomerRepricingConfig', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateCustomerRepricingConfigRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.CustomerRepricingConfig.FromString, _registered_method=True)
        self.DeleteCustomerRepricingConfig = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/DeleteCustomerRepricingConfig', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.DeleteCustomerRepricingConfigRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.GetChannelPartnerRepricingConfig = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/GetChannelPartnerRepricingConfig', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetChannelPartnerRepricingConfigRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.ChannelPartnerRepricingConfig.FromString, _registered_method=True)
        self.ListChannelPartnerRepricingConfigs = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListChannelPartnerRepricingConfigs', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerRepricingConfigsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerRepricingConfigsResponse.FromString, _registered_method=True)
        self.CreateChannelPartnerRepricingConfig = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/CreateChannelPartnerRepricingConfig', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateChannelPartnerRepricingConfigRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.ChannelPartnerRepricingConfig.FromString, _registered_method=True)
        self.UpdateChannelPartnerRepricingConfig = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/UpdateChannelPartnerRepricingConfig', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateChannelPartnerRepricingConfigRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.ChannelPartnerRepricingConfig.FromString, _registered_method=True)
        self.DeleteChannelPartnerRepricingConfig = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/DeleteChannelPartnerRepricingConfig', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.DeleteChannelPartnerRepricingConfigRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.ListSkuGroups = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListSkuGroups', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupsResponse.FromString, _registered_method=True)
        self.ListSkuGroupBillableSkus = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListSkuGroupBillableSkus', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupBillableSkusRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupBillableSkusResponse.FromString, _registered_method=True)
        self.LookupOffer = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/LookupOffer', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.LookupOfferRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_offers__pb2.Offer.FromString, _registered_method=True)
        self.ListProducts = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListProducts', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListProductsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListProductsResponse.FromString, _registered_method=True)
        self.ListSkus = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListSkus', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkusRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkusResponse.FromString, _registered_method=True)
        self.ListOffers = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListOffers', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListOffersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListOffersResponse.FromString, _registered_method=True)
        self.ListPurchasableSkus = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListPurchasableSkus', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableSkusRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableSkusResponse.FromString, _registered_method=True)
        self.ListPurchasableOffers = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListPurchasableOffers', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableOffersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableOffersResponse.FromString, _registered_method=True)
        self.QueryEligibleBillingAccounts = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/QueryEligibleBillingAccounts', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.QueryEligibleBillingAccountsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.QueryEligibleBillingAccountsResponse.FromString, _registered_method=True)
        self.RegisterSubscriber = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/RegisterSubscriber', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.RegisterSubscriberRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.RegisterSubscriberResponse.FromString, _registered_method=True)
        self.UnregisterSubscriber = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/UnregisterSubscriber', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UnregisterSubscriberRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UnregisterSubscriberResponse.FromString, _registered_method=True)
        self.ListSubscribers = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListSubscribers', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSubscribersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSubscribersResponse.FromString, _registered_method=True)
        self.ListEntitlementChanges = channel.unary_unary('/google.cloud.channel.v1.CloudChannelService/ListEntitlementChanges', request_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementChangesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementChangesResponse.FromString, _registered_method=True)

class CloudChannelServiceServicer(object):
    """CloudChannelService lets Google cloud resellers and distributors manage
    their customers, channel partners, entitlements, and reports.

    Using this service:
    1. Resellers and distributors can manage a customer entity.
    2. Distributors can register an authorized reseller in their channel and
    provide them with delegated admin access.
    3. Resellers and distributors can manage customer entitlements.

    CloudChannelService exposes the following resources:
    - [Customer][google.cloud.channel.v1.Customer]s: An entity-usually an
    enterprise-managed by a reseller or distributor.

    - [Entitlement][google.cloud.channel.v1.Entitlement]s: An entity that
    provides a customer with the means to use a service. Entitlements are created
    or updated as a result of a successful fulfillment.

    - [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]s: An
    entity that identifies links between distributors and their indirect
    resellers in a channel.
    """

    def ListCustomers(self, request, context):
        """List [Customer][google.cloud.channel.v1.Customer]s.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.

        Return value:
        List of [Customer][google.cloud.channel.v1.Customer]s, or an empty list if
        there are no customers.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomer(self, request, context):
        """Returns the requested [Customer][google.cloud.channel.v1.Customer]
        resource.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: The customer resource doesn't exist. Usually the result of an
        invalid name parameter.

        Return value:
        The [Customer][google.cloud.channel.v1.Customer] resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckCloudIdentityAccountsExist(self, request, context):
        """Confirms the existence of Cloud Identity accounts based on the domain and
        if the Cloud Identity accounts are owned by the reseller.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * INVALID_VALUE: Invalid domain value in the request.

        Return value:
        A list of
        [CloudIdentityCustomerAccount][google.cloud.channel.v1.CloudIdentityCustomerAccount]
        resources for the domain (may be empty)

        Note: in the v1alpha1 version of the API, a NOT_FOUND error returns if
        no
        [CloudIdentityCustomerAccount][google.cloud.channel.v1.CloudIdentityCustomerAccount]
        resources match the domain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCustomer(self, request, context):
        """Creates a new [Customer][google.cloud.channel.v1.Customer] resource under
        the reseller or distributor account.

        Possible error codes:

        * PERMISSION_DENIED:
        * The reseller account making the request is different from the
        reseller account in the API request.
        * You are not authorized to create a customer. See
        https://support.google.com/channelservices/answer/9759265
        * INVALID_ARGUMENT:
        * Required request parameters are missing or invalid.
        * Domain field value doesn't match the primary email domain.

        Return value:
        The newly created [Customer][google.cloud.channel.v1.Customer] resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCustomer(self, request, context):
        """Updates an existing [Customer][google.cloud.channel.v1.Customer] resource
        for the reseller or distributor.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: No [Customer][google.cloud.channel.v1.Customer] resource found
        for the name in the request.

        Return value:
        The updated [Customer][google.cloud.channel.v1.Customer] resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCustomer(self, request, context):
        """Deletes the given [Customer][google.cloud.channel.v1.Customer] permanently.

        Possible error codes:

        * PERMISSION_DENIED: The account making the request does not own
        this customer.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * FAILED_PRECONDITION: The customer has existing entitlements.
        * NOT_FOUND: No [Customer][google.cloud.channel.v1.Customer] resource found
        for the name in the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportCustomer(self, request, context):
        """Imports a [Customer][google.cloud.channel.v1.Customer] from the Cloud
        Identity associated with the provided Cloud Identity ID or domain before a
        TransferEntitlements call. If a linked Customer already exists and
        overwrite_if_exists is true, it will update that Customer's data.

        Possible error codes:

        * PERMISSION_DENIED:
        * The reseller account making the request is different from the
        reseller account in the API request.
        * You are not authorized to import the customer. See
        https://support.google.com/channelservices/answer/9759265
        * NOT_FOUND: Cloud Identity doesn't exist or was deleted.
        * INVALID_ARGUMENT: Required parameters are missing, or the auth_token is
        expired or invalid.
        * ALREADY_EXISTS: A customer already exists and has conflicting critical
        fields. Requires an overwrite.

        Return value:
        The [Customer][google.cloud.channel.v1.Customer].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProvisionCloudIdentity(self, request, context):
        """Creates a Cloud Identity for the given customer using the customer's
        information, or the information provided here.

        Possible error codes:

        *  PERMISSION_DENIED:
        * The customer doesn't belong to the reseller.
        * You are not authorized to provision cloud identity id. See
        https://support.google.com/channelservices/answer/9759265
        *  INVALID_ARGUMENT: Required request parameters are missing or invalid.
        *  NOT_FOUND: The customer was not found.
        *  ALREADY_EXISTS: The customer's primary email already exists. Retry
        after changing the customer's primary contact email.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The Operation metadata contains an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEntitlements(self, request, context):
        """Lists [Entitlement][google.cloud.channel.v1.Entitlement]s belonging to a
        customer.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.

        Return value:
        A list of the customer's
        [Entitlement][google.cloud.channel.v1.Entitlement]s.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTransferableSkus(self, request, context):
        """List [TransferableSku][google.cloud.channel.v1.TransferableSku]s of a
        customer based on the Cloud Identity ID or Customer Name in the request.

        Use this method to list the entitlements information of an
        unowned customer. You should provide the customer's
        Cloud Identity ID or Customer Name.

        Possible error codes:

        * PERMISSION_DENIED:
        * The customer doesn't belong to the reseller and has no auth token.
        * The supplied auth token is invalid.
        * The reseller account making the request is different
        from the reseller account in the query.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.

        Return value:
        A list of the customer's
        [TransferableSku][google.cloud.channel.v1.TransferableSku].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTransferableOffers(self, request, context):
        """List [TransferableOffer][google.cloud.channel.v1.TransferableOffer]s of a
        customer based on Cloud Identity ID or Customer Name in the request.

        Use this method when a reseller gets the entitlement information of an
        unowned customer. The reseller should provide the customer's
        Cloud Identity ID or Customer Name.

        Possible error codes:

        * PERMISSION_DENIED:
        * The customer doesn't belong to the reseller and has no auth token.
        * The customer provided incorrect reseller information when generating
        auth token.
        * The reseller account making the request is different
        from the reseller account in the query.
        * The reseller is not authorized to transact on this Product. See
        https://support.google.com/channelservices/answer/9759265
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.

        Return value:
        List of [TransferableOffer][google.cloud.channel.v1.TransferableOffer] for
        the given customer and SKU.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEntitlement(self, request, context):
        """Returns the requested [Entitlement][google.cloud.channel.v1.Entitlement]
        resource.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: The customer entitlement was not found.

        Return value:
        The requested [Entitlement][google.cloud.channel.v1.Entitlement] resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEntitlement(self, request, context):
        """Creates an entitlement for a customer.

        Possible error codes:

        * PERMISSION_DENIED:
        * The customer doesn't belong to the reseller.
        * The reseller is not authorized to transact on this Product. See
        https://support.google.com/channelservices/answer/9759265
        * INVALID_ARGUMENT:
        * Required request parameters are missing or invalid.
        * There is already a customer entitlement for a SKU from the same
        product family.
        * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact
        Google Channel support for further troubleshooting.
        * NOT_FOUND: The customer or offer resource was not found.
        * ALREADY_EXISTS:
        * The SKU was already purchased for the customer.
        * The customer's primary email already exists. Retry
        after changing the customer's primary contact email.
        * CONDITION_NOT_MET or FAILED_PRECONDITION:
        * The domain required for purchasing a SKU has not been verified.
        * A pre-requisite SKU required to purchase an Add-On SKU is missing.
        For example, Google Workspace Business Starter is required to purchase
        Vault or Drive.
        * (Developer accounts only) Reseller and resold domain must meet the
        following naming requirements:
        * Domain names must start with goog-test.
        * Domain names must include the reseller domain.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeParameters(self, request, context):
        """Change parameters of the entitlement.

        An entitlement update is a long-running operation and it updates the
        entitlement as a result of fulfillment.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        For example, the number of seats being changed is greater than the allowed
        number of max seats, or decreasing seats for a commitment based plan.
        * NOT_FOUND: Entitlement resource not found.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeRenewalSettings(self, request, context):
        """Updates the renewal settings for an existing customer entitlement.

        An entitlement update is a long-running operation and it updates the
        entitlement as a result of fulfillment.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: Entitlement resource not found.
        * NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for a
        commitment plan. Can't enable or disable renewals for non-commitment plans.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeOffer(self, request, context):
        """Updates the Offer for an existing customer entitlement.

        An entitlement update is a long-running operation and it updates the
        entitlement as a result of fulfillment.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: Offer or Entitlement resource not found.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartPaidService(self, request, context):
        """Starts paid service for a trial entitlement.

        Starts paid service for a trial entitlement immediately. This method is
        only applicable if a plan is set up for a trial entitlement but has some
        trial days remaining.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: Entitlement resource not found.
        * FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for
        entitlement on trial plans.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SuspendEntitlement(self, request, context):
        """Suspends a previously fulfilled entitlement.

        An entitlement suspension is a long-running operation.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: Entitlement resource not found.
        * NOT_ACTIVE: Entitlement is not active.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelEntitlement(self, request, context):
        """Cancels a previously fulfilled entitlement.

        An entitlement cancellation is a long-running operation.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * FAILED_PRECONDITION: There are Google Cloud projects linked to the
        Google Cloud entitlement's Cloud Billing subaccount.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: Entitlement resource not found.
        * DELETION_TYPE_NOT_ALLOWED: Cancel is only allowed for Google Workspace
        add-ons, or entitlements for Google Cloud's development platform.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The response will contain
        google.protobuf.Empty on success. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActivateEntitlement(self, request, context):
        """Activates a previously suspended entitlement. Entitlements suspended for
        pending ToS acceptance can't be activated using this method.

        An entitlement activation is a long-running operation and it updates
        the state of the customer entitlement.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: Entitlement resource not found.
        * SUSPENSION_NOT_RESELLER_INITIATED: Can only activate reseller-initiated
        suspensions and entitlements that have accepted the TOS.
        * NOT_SUSPENDED: Can only activate suspended entitlements not in an ACTIVE
        state.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferEntitlements(self, request, context):
        """Transfers customer entitlements to new reseller.

        Possible error codes:

        * PERMISSION_DENIED:
        * The customer doesn't belong to the reseller.
        * The reseller is not authorized to transact on this Product. See
        https://support.google.com/channelservices/answer/9759265
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: The customer or offer resource was not found.
        * ALREADY_EXISTS: The SKU was already transferred for the customer.
        * CONDITION_NOT_MET or FAILED_PRECONDITION:
        * The SKU requires domain verification to transfer, but the domain is
        not verified.
        * An Add-On SKU (example, Vault or Drive) is missing the
        pre-requisite SKU (example, G Suite Basic).
        * (Developer accounts only) Reseller and resold domain must meet the
        following naming requirements:
        * Domain names must start with goog-test.
        * Domain names must include the reseller domain.
        * Specify all transferring entitlements.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferEntitlementsToGoogle(self, request, context):
        """Transfers customer entitlements from their current reseller to Google.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: The customer or offer resource was not found.
        * ALREADY_EXISTS: The SKU was already transferred for the customer.
        * CONDITION_NOT_MET or FAILED_PRECONDITION:
        * The SKU requires domain verification to transfer, but the domain is
        not verified.
        * An Add-On SKU (example, Vault or Drive) is missing the
        pre-requisite SKU (example, G Suite Basic).
        * (Developer accounts only) Reseller and resold domain must meet the
        following naming requirements:
        * Domain names must start with goog-test.
        * Domain names must include the reseller domain.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The ID of a long-running operation.

        To get the results of the operation, call the GetOperation method of
        CloudChannelOperationsService. The response will contain
        google.protobuf.Empty on success. The Operation metadata will contain an
        instance of [OperationMetadata][google.cloud.channel.v1.OperationMetadata].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListChannelPartnerLinks(self, request, context):
        """List [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]s
        belonging to a distributor. You must be a distributor to call this method.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.

        Return value:
        The list of the distributor account's
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink] resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannelPartnerLink(self, request, context):
        """Returns the requested
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink] resource.
        You must be a distributor to call this method.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: ChannelPartnerLink resource not found because of an
        invalid channel partner link name.

        Return value:
        The [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateChannelPartnerLink(self, request, context):
        """Initiates a channel partner link between a distributor and a reseller, or
        between resellers in an n-tier reseller channel.
        Invited partners need to follow the invite_link_uri provided in the
        response to accept. After accepting the invitation, a link is set up
        between the two parties.
        You must be a distributor to call this method.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * ALREADY_EXISTS: The ChannelPartnerLink sent in the request already
        exists.
        * NOT_FOUND: No Cloud Identity customer exists for provided domain.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The new [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateChannelPartnerLink(self, request, context):
        """Updates a channel partner link. Distributors call this method to change a
        link's status. For example, to suspend a partner link.
        You must be a distributor to call this method.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request is different
        from the reseller account in the API request.
        * INVALID_ARGUMENT:
        * Required request parameters are missing or invalid.
        * Link state cannot change from invited to active or suspended.
        * Cannot send reseller_cloud_identity_id, invite_url, or name in update
        mask.
        * NOT_FOUND: ChannelPartnerLink resource not found.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The updated
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink] resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomerRepricingConfig(self, request, context):
        """Gets information about how a Reseller modifies their bill before sending
        it to a Customer.

        Possible Error Codes:

        * PERMISSION_DENIED: If the account making the request and the account
        being queried are different.
        * NOT_FOUND: The
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        was not found.
        * INTERNAL: Any non-user error related to technical issues in the
        backend. In this case, contact Cloud Channel support.

        Return Value:
        If successful, the
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resource, otherwise returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCustomerRepricingConfigs(self, request, context):
        """Lists information about how a Reseller modifies their bill before sending
        it to a Customer.

        Possible Error Codes:

        * PERMISSION_DENIED: If the account making the request and the account
        being queried are different.
        * NOT_FOUND: The
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        specified does not exist or is not associated with the given account.
        * INTERNAL: Any non-user error related to technical issues in the
        backend. In this case, contact Cloud Channel support.

        Return Value:
        If successful, the
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resources. The data for each resource is displayed in the ascending order
        of:

        * Customer ID
        * [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement]
        * [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        * [CustomerRepricingConfig.update_time][google.cloud.channel.v1.CustomerRepricingConfig.update_time]

        If unsuccessful, returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCustomerRepricingConfig(self, request, context):
        """Creates a CustomerRepricingConfig. Call this method to set modifications
        for a specific customer's bill. You can only create configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. If needed, you can create a config for the current
        month, with some restrictions.

        When creating a config for a future month, make sure there are no existing
        configs for that
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        The following restrictions are for creating configs in the current month.

        * This functionality is reserved for recovering from an erroneous config,
        and should not be used for regular business cases.
        * The new config will not modify exports used with other configs.
        Changes to the config may be immediate, but may take up to 24 hours.
        * There is a limit of ten configs for any
        [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement],
        for any
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].
        * The contained
        [CustomerRepricingConfig.repricing_config][google.cloud.channel.v1.CustomerRepricingConfig.repricing_config]
        value must be different from the value used in the current config for a
        [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement].

        Possible Error Codes:

        * PERMISSION_DENIED: If the account making the request and the account
        being queried are different.
        * INVALID_ARGUMENT: Missing or invalid required parameters in the
        request. Also displays if the updated config is for the current month or
        past months.
        * NOT_FOUND: The
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        specified does not exist or is not associated with the given account.
        * INTERNAL: Any non-user error related to technical issues in the
        backend. In this case, contact Cloud Channel support.

        Return Value:
        If successful, the updated
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resource, otherwise returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCustomerRepricingConfig(self, request, context):
        """Updates a CustomerRepricingConfig. Call this method to set modifications
        for a specific customer's bill. This method overwrites the existing
        CustomerRepricingConfig.

        You can only update configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. To make changes to configs for the current month, use
        [CreateCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateCustomerRepricingConfig],
        taking note of its restrictions. You cannot update the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        When updating a config in the future:

        * This config must already exist.

        Possible Error Codes:

        * PERMISSION_DENIED: If the account making the request and the account
        being queried are different.
        * INVALID_ARGUMENT: Missing or invalid required parameters in the
        request. Also displays if the updated config is for the current month or
        past months.
        * NOT_FOUND: The
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        specified does not exist or is not associated with the given account.
        * INTERNAL: Any non-user error related to technical issues in the
        backend. In this case, contact Cloud Channel support.

        Return Value:
        If successful, the updated
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resource, otherwise returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCustomerRepricingConfig(self, request, context):
        """Deletes the given
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        permanently. You can only delete configs if their
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is set to a date after the current month.

        Possible error codes:

        * PERMISSION_DENIED: The account making the request does not own
        this customer.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * FAILED_PRECONDITION: The
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        is active or in the past.
        * NOT_FOUND: No
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        found for the name in the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannelPartnerRepricingConfig(self, request, context):
        """Gets information about how a Distributor modifies their bill before sending
        it to a ChannelPartner.

        Possible Error Codes:

        * PERMISSION_DENIED: If the account making the request and the account
        being queried are different.
        * NOT_FOUND: The
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        was not found.
        * INTERNAL: Any non-user error related to technical issues in the
        backend. In this case, contact Cloud Channel support.

        Return Value:
        If successful, the
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resource, otherwise returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListChannelPartnerRepricingConfigs(self, request, context):
        """Lists information about how a Reseller modifies their bill before sending
        it to a ChannelPartner.

        Possible Error Codes:

        * PERMISSION_DENIED: If the account making the request and the account
        being queried are different.
        * NOT_FOUND: The
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        specified does not exist or is not associated with the given account.
        * INTERNAL: Any non-user error related to technical issues in the
        backend. In this case, contact Cloud Channel support.

        Return Value:
        If successful, the
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resources. The data for each resource is displayed in the ascending order
        of:

        * Channel Partner ID
        * [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        * [ChannelPartnerRepricingConfig.update_time][google.cloud.channel.v1.ChannelPartnerRepricingConfig.update_time]

        If unsuccessful, returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateChannelPartnerRepricingConfig(self, request, context):
        """Creates a ChannelPartnerRepricingConfig. Call this method to set
        modifications for a specific ChannelPartner's bill. You can only create
        configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. If needed, you can create a config for the current
        month, with some restrictions.

        When creating a config for a future month, make sure there are no existing
        configs for that
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        The following restrictions are for creating configs in the current month.

        * This functionality is reserved for recovering from an erroneous config,
        and should not be used for regular business cases.
        * The new config will not modify exports used with other configs.
        Changes to the config may be immediate, but may take up to 24 hours.
        * There is a limit of ten configs for any ChannelPartner or
        [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement],
        for any
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].
        * The contained
        [ChannelPartnerRepricingConfig.repricing_config][google.cloud.channel.v1.ChannelPartnerRepricingConfig.repricing_config]
        value must be different from the value used in the current config for a
        ChannelPartner.

        Possible Error Codes:

        * PERMISSION_DENIED: If the account making the request and the account
        being queried are different.
        * INVALID_ARGUMENT: Missing or invalid required parameters in the
        request. Also displays if the updated config is for the current month or
        past months.
        * NOT_FOUND: The
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        specified does not exist or is not associated with the given account.
        * INTERNAL: Any non-user error related to technical issues in the
        backend. In this case, contact Cloud Channel support.

        Return Value:
        If successful, the updated
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resource, otherwise returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateChannelPartnerRepricingConfig(self, request, context):
        """Updates a ChannelPartnerRepricingConfig. Call this method to set
        modifications for a specific ChannelPartner's bill. This method overwrites
        the existing CustomerRepricingConfig.

        You can only update configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. To make changes to configs for the current month, use
        [CreateChannelPartnerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerRepricingConfig],
        taking note of its restrictions. You cannot update the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        When updating a config in the future:

        * This config must already exist.

        Possible Error Codes:

        * PERMISSION_DENIED: If the account making the request and the account
        being queried are different.
        * INVALID_ARGUMENT: Missing or invalid required parameters in the
        request. Also displays if the updated config is for the current month or
        past months.
        * NOT_FOUND: The
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        specified does not exist or is not associated with the given account.
        * INTERNAL: Any non-user error related to technical issues in the
        backend. In this case, contact Cloud Channel support.

        Return Value:
        If successful, the updated
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resource, otherwise returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteChannelPartnerRepricingConfig(self, request, context):
        """Deletes the given
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        permanently. You can only delete configs if their
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is set to a date after the current month.

        Possible error codes:

        * PERMISSION_DENIED: The account making the request does not own
        this customer.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * FAILED_PRECONDITION: The
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        is active or in the past.
        * NOT_FOUND: No
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        found for the name in the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSkuGroups(self, request, context):
        """Lists the Rebilling supported SKU groups the account is authorized to
        sell.
        Reference: https://cloud.google.com/skus/sku-groups

        Possible Error Codes:

        * PERMISSION_DENIED: If the account making the request and the account
        being queried are different, or the account doesn't exist.
        * INTERNAL: Any non-user error related to technical issues in the
        backend. In this case, contact Cloud Channel support.

        Return Value:
        If successful, the [SkuGroup][google.cloud.channel.v1.SkuGroup] resources.
        The data for each resource is displayed in the alphabetical order of SKU
        group display name.
        The data for each resource is displayed in the ascending order of
        [SkuGroup.display_name][google.cloud.channel.v1.SkuGroup.display_name]

        If unsuccessful, returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSkuGroupBillableSkus(self, request, context):
        """Lists the Billable SKUs in a given SKU group.

        Possible error codes:
        PERMISSION_DENIED: If the account making the request and the account
        being queried for are different, or the account doesn't exist.
        INVALID_ARGUMENT: Missing or invalid required parameters in the
        request.
        INTERNAL: Any non-user error related to technical issue in the
        backend. In this case, contact cloud channel support.

        Return Value:
        If successful, the [BillableSku][google.cloud.channel.v1.BillableSku]
        resources. The data for each resource is displayed in the ascending order
        of:

        * [BillableSku.service_display_name][google.cloud.channel.v1.BillableSku.service_display_name]
        * [BillableSku.sku_display_name][google.cloud.channel.v1.BillableSku.sku_display_name]

        If unsuccessful, returns an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupOffer(self, request, context):
        """Returns the requested [Offer][google.cloud.channel.v1.Offer] resource.

        Possible error codes:

        * PERMISSION_DENIED: The entitlement doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: Entitlement or offer was not found.

        Return value:
        The [Offer][google.cloud.channel.v1.Offer] resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProducts(self, request, context):
        """Lists the Products the reseller is authorized to sell.

        Possible error codes:

        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSkus(self, request, context):
        """Lists the SKUs for a product the reseller is authorized to sell.

        Possible error codes:

        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOffers(self, request, context):
        """Lists the Offers the reseller can sell.

        Possible error codes:

        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPurchasableSkus(self, request, context):
        """Lists the following:

        * SKUs that you can purchase for a customer
        * SKUs that you can upgrade or downgrade for an entitlement.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPurchasableOffers(self, request, context):
        """Lists the following:

        * Offers that you can purchase for a customer.
        * Offers that you can change for an entitlement.

        Possible error codes:

        * PERMISSION_DENIED:
        * The customer doesn't belong to the reseller
        * The reseller is not authorized to transact on this Product. See
        https://support.google.com/channelservices/answer/9759265
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryEligibleBillingAccounts(self, request, context):
        """Lists the billing accounts that are eligible to purchase particular SKUs
        for a given customer.

        Possible error codes:

        * PERMISSION_DENIED: The customer doesn't belong to the reseller.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.

        Return value:
        Based on the provided list of SKUs, returns a list of SKU groups that must
        be purchased using the same billing account and the billing accounts
        eligible to purchase each SKU group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterSubscriber(self, request, context):
        """Registers a service account with subscriber privileges on the Cloud Pub/Sub
        topic for this Channel Services account. After you create a
        subscriber, you get the events through
        [SubscriberEvent][google.cloud.channel.v1.SubscriberEvent]

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request and the
        provided reseller account are different, or the impersonated user
        is not a super admin.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The topic name with the registered service email address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnregisterSubscriber(self, request, context):
        """Unregisters a service account with subscriber privileges on the Cloud
        Pub/Sub topic created for this Channel Services account. If there are no
        service accounts left with subscriber privileges, this deletes the topic.
        You can call ListSubscribers to check for these accounts.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request and the
        provided reseller account are different, or the impersonated user
        is not a super admin.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: The topic resource doesn't exist.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        The topic name that unregistered the service email address.
        Returns a success response if the service email address wasn't registered
        with the topic.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSubscribers(self, request, context):
        """Lists service accounts with subscriber privileges on the Cloud Pub/Sub
        topic created for this Channel Services account.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request and the
        provided reseller account are different, or the impersonated user
        is not a super admin.
        * INVALID_ARGUMENT: Required request parameters are missing or invalid.
        * NOT_FOUND: The topic resource doesn't exist.
        * INTERNAL: Any non-user error related to a technical issue in the
        backend. Contact Cloud Channel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        Contact Cloud Channel support.

        Return value:
        A list of service email addresses.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEntitlementChanges(self, request, context):
        """List entitlement history.

        Possible error codes:

        * PERMISSION_DENIED: The reseller account making the request and the
        provided reseller account are different.
        * INVALID_ARGUMENT: Missing or invalid required fields in the request.
        * NOT_FOUND: The parent resource doesn't exist. Usually the result of an
        invalid name parameter.
        * INTERNAL: Any non-user error related to a technical issue in the backend.
        In this case, contact CloudChannel support.
        * UNKNOWN: Any non-user error related to a technical issue in the backend.
        In this case, contact Cloud Channel support.

        Return value:
        List of [EntitlementChange][google.cloud.channel.v1.EntitlementChange]s.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_CloudChannelServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListCustomers': grpc.unary_unary_rpc_method_handler(servicer.ListCustomers, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomersRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomersResponse.SerializeToString), 'GetCustomer': grpc.unary_unary_rpc_method_handler(servicer.GetCustomer, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetCustomerRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.SerializeToString), 'CheckCloudIdentityAccountsExist': grpc.unary_unary_rpc_method_handler(servicer.CheckCloudIdentityAccountsExist, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CheckCloudIdentityAccountsExistRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CheckCloudIdentityAccountsExistResponse.SerializeToString), 'CreateCustomer': grpc.unary_unary_rpc_method_handler(servicer.CreateCustomer, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateCustomerRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.SerializeToString), 'UpdateCustomer': grpc.unary_unary_rpc_method_handler(servicer.UpdateCustomer, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateCustomerRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.SerializeToString), 'DeleteCustomer': grpc.unary_unary_rpc_method_handler(servicer.DeleteCustomer, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.DeleteCustomerRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ImportCustomer': grpc.unary_unary_rpc_method_handler(servicer.ImportCustomer, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ImportCustomerRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.SerializeToString), 'ProvisionCloudIdentity': grpc.unary_unary_rpc_method_handler(servicer.ProvisionCloudIdentity, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ProvisionCloudIdentityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListEntitlements': grpc.unary_unary_rpc_method_handler(servicer.ListEntitlements, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementsRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementsResponse.SerializeToString), 'ListTransferableSkus': grpc.unary_unary_rpc_method_handler(servicer.ListTransferableSkus, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableSkusRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableSkusResponse.SerializeToString), 'ListTransferableOffers': grpc.unary_unary_rpc_method_handler(servicer.ListTransferableOffers, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableOffersRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableOffersResponse.SerializeToString), 'GetEntitlement': grpc.unary_unary_rpc_method_handler(servicer.GetEntitlement, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetEntitlementRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_entitlements__pb2.Entitlement.SerializeToString), 'CreateEntitlement': grpc.unary_unary_rpc_method_handler(servicer.CreateEntitlement, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateEntitlementRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ChangeParameters': grpc.unary_unary_rpc_method_handler(servicer.ChangeParameters, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ChangeParametersRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ChangeRenewalSettings': grpc.unary_unary_rpc_method_handler(servicer.ChangeRenewalSettings, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ChangeRenewalSettingsRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ChangeOffer': grpc.unary_unary_rpc_method_handler(servicer.ChangeOffer, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ChangeOfferRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'StartPaidService': grpc.unary_unary_rpc_method_handler(servicer.StartPaidService, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.StartPaidServiceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'SuspendEntitlement': grpc.unary_unary_rpc_method_handler(servicer.SuspendEntitlement, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.SuspendEntitlementRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CancelEntitlement': grpc.unary_unary_rpc_method_handler(servicer.CancelEntitlement, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CancelEntitlementRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ActivateEntitlement': grpc.unary_unary_rpc_method_handler(servicer.ActivateEntitlement, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ActivateEntitlementRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'TransferEntitlements': grpc.unary_unary_rpc_method_handler(servicer.TransferEntitlements, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.TransferEntitlementsRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'TransferEntitlementsToGoogle': grpc.unary_unary_rpc_method_handler(servicer.TransferEntitlementsToGoogle, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.TransferEntitlementsToGoogleRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListChannelPartnerLinks': grpc.unary_unary_rpc_method_handler(servicer.ListChannelPartnerLinks, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerLinksRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerLinksResponse.SerializeToString), 'GetChannelPartnerLink': grpc.unary_unary_rpc_method_handler(servicer.GetChannelPartnerLink, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetChannelPartnerLinkRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2.ChannelPartnerLink.SerializeToString), 'CreateChannelPartnerLink': grpc.unary_unary_rpc_method_handler(servicer.CreateChannelPartnerLink, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateChannelPartnerLinkRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2.ChannelPartnerLink.SerializeToString), 'UpdateChannelPartnerLink': grpc.unary_unary_rpc_method_handler(servicer.UpdateChannelPartnerLink, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateChannelPartnerLinkRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2.ChannelPartnerLink.SerializeToString), 'GetCustomerRepricingConfig': grpc.unary_unary_rpc_method_handler(servicer.GetCustomerRepricingConfig, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetCustomerRepricingConfigRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.CustomerRepricingConfig.SerializeToString), 'ListCustomerRepricingConfigs': grpc.unary_unary_rpc_method_handler(servicer.ListCustomerRepricingConfigs, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomerRepricingConfigsRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomerRepricingConfigsResponse.SerializeToString), 'CreateCustomerRepricingConfig': grpc.unary_unary_rpc_method_handler(servicer.CreateCustomerRepricingConfig, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateCustomerRepricingConfigRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.CustomerRepricingConfig.SerializeToString), 'UpdateCustomerRepricingConfig': grpc.unary_unary_rpc_method_handler(servicer.UpdateCustomerRepricingConfig, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateCustomerRepricingConfigRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.CustomerRepricingConfig.SerializeToString), 'DeleteCustomerRepricingConfig': grpc.unary_unary_rpc_method_handler(servicer.DeleteCustomerRepricingConfig, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.DeleteCustomerRepricingConfigRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'GetChannelPartnerRepricingConfig': grpc.unary_unary_rpc_method_handler(servicer.GetChannelPartnerRepricingConfig, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetChannelPartnerRepricingConfigRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.ChannelPartnerRepricingConfig.SerializeToString), 'ListChannelPartnerRepricingConfigs': grpc.unary_unary_rpc_method_handler(servicer.ListChannelPartnerRepricingConfigs, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerRepricingConfigsRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerRepricingConfigsResponse.SerializeToString), 'CreateChannelPartnerRepricingConfig': grpc.unary_unary_rpc_method_handler(servicer.CreateChannelPartnerRepricingConfig, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateChannelPartnerRepricingConfigRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.ChannelPartnerRepricingConfig.SerializeToString), 'UpdateChannelPartnerRepricingConfig': grpc.unary_unary_rpc_method_handler(servicer.UpdateChannelPartnerRepricingConfig, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateChannelPartnerRepricingConfigRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.ChannelPartnerRepricingConfig.SerializeToString), 'DeleteChannelPartnerRepricingConfig': grpc.unary_unary_rpc_method_handler(servicer.DeleteChannelPartnerRepricingConfig, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.DeleteChannelPartnerRepricingConfigRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ListSkuGroups': grpc.unary_unary_rpc_method_handler(servicer.ListSkuGroups, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupsRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupsResponse.SerializeToString), 'ListSkuGroupBillableSkus': grpc.unary_unary_rpc_method_handler(servicer.ListSkuGroupBillableSkus, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupBillableSkusRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupBillableSkusResponse.SerializeToString), 'LookupOffer': grpc.unary_unary_rpc_method_handler(servicer.LookupOffer, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.LookupOfferRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_offers__pb2.Offer.SerializeToString), 'ListProducts': grpc.unary_unary_rpc_method_handler(servicer.ListProducts, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListProductsRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListProductsResponse.SerializeToString), 'ListSkus': grpc.unary_unary_rpc_method_handler(servicer.ListSkus, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkusRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkusResponse.SerializeToString), 'ListOffers': grpc.unary_unary_rpc_method_handler(servicer.ListOffers, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListOffersRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListOffersResponse.SerializeToString), 'ListPurchasableSkus': grpc.unary_unary_rpc_method_handler(servicer.ListPurchasableSkus, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableSkusRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableSkusResponse.SerializeToString), 'ListPurchasableOffers': grpc.unary_unary_rpc_method_handler(servicer.ListPurchasableOffers, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableOffersRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableOffersResponse.SerializeToString), 'QueryEligibleBillingAccounts': grpc.unary_unary_rpc_method_handler(servicer.QueryEligibleBillingAccounts, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.QueryEligibleBillingAccountsRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.QueryEligibleBillingAccountsResponse.SerializeToString), 'RegisterSubscriber': grpc.unary_unary_rpc_method_handler(servicer.RegisterSubscriber, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.RegisterSubscriberRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.RegisterSubscriberResponse.SerializeToString), 'UnregisterSubscriber': grpc.unary_unary_rpc_method_handler(servicer.UnregisterSubscriber, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UnregisterSubscriberRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UnregisterSubscriberResponse.SerializeToString), 'ListSubscribers': grpc.unary_unary_rpc_method_handler(servicer.ListSubscribers, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSubscribersRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSubscribersResponse.SerializeToString), 'ListEntitlementChanges': grpc.unary_unary_rpc_method_handler(servicer.ListEntitlementChanges, request_deserializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementChangesRequest.FromString, response_serializer=google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementChangesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.channel.v1.CloudChannelService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.channel.v1.CloudChannelService', rpc_method_handlers)

class CloudChannelService(object):
    """CloudChannelService lets Google cloud resellers and distributors manage
    their customers, channel partners, entitlements, and reports.

    Using this service:
    1. Resellers and distributors can manage a customer entity.
    2. Distributors can register an authorized reseller in their channel and
    provide them with delegated admin access.
    3. Resellers and distributors can manage customer entitlements.

    CloudChannelService exposes the following resources:
    - [Customer][google.cloud.channel.v1.Customer]s: An entity-usually an
    enterprise-managed by a reseller or distributor.

    - [Entitlement][google.cloud.channel.v1.Entitlement]s: An entity that
    provides a customer with the means to use a service. Entitlements are created
    or updated as a result of a successful fulfillment.

    - [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]s: An
    entity that identifies links between distributors and their indirect
    resellers in a channel.
    """

    @staticmethod
    def ListCustomers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListCustomers', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomersRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCustomer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/GetCustomer', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetCustomerRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CheckCloudIdentityAccountsExist(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/CheckCloudIdentityAccountsExist', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CheckCloudIdentityAccountsExistRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CheckCloudIdentityAccountsExistResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCustomer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/CreateCustomer', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateCustomerRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCustomer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/UpdateCustomer', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateCustomerRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteCustomer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/DeleteCustomer', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.DeleteCustomerRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ImportCustomer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ImportCustomer', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ImportCustomerRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_customers__pb2.Customer.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ProvisionCloudIdentity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ProvisionCloudIdentity', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ProvisionCloudIdentityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListEntitlements(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListEntitlements', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementsRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListTransferableSkus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListTransferableSkus', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableSkusRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableSkusResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListTransferableOffers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListTransferableOffers', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableOffersRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListTransferableOffersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetEntitlement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/GetEntitlement', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetEntitlementRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_entitlements__pb2.Entitlement.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateEntitlement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/CreateEntitlement', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateEntitlementRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ChangeParameters(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ChangeParameters', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ChangeParametersRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ChangeRenewalSettings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ChangeRenewalSettings', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ChangeRenewalSettingsRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ChangeOffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ChangeOffer', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ChangeOfferRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def StartPaidService(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/StartPaidService', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.StartPaidServiceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SuspendEntitlement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/SuspendEntitlement', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.SuspendEntitlementRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CancelEntitlement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/CancelEntitlement', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CancelEntitlementRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ActivateEntitlement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ActivateEntitlement', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ActivateEntitlementRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def TransferEntitlements(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/TransferEntitlements', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.TransferEntitlementsRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def TransferEntitlementsToGoogle(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/TransferEntitlementsToGoogle', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.TransferEntitlementsToGoogleRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListChannelPartnerLinks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListChannelPartnerLinks', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerLinksRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerLinksResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetChannelPartnerLink(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/GetChannelPartnerLink', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetChannelPartnerLinkRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2.ChannelPartnerLink.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateChannelPartnerLink(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/CreateChannelPartnerLink', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateChannelPartnerLinkRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2.ChannelPartnerLink.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateChannelPartnerLink(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/UpdateChannelPartnerLink', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateChannelPartnerLinkRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_channel__partner__links__pb2.ChannelPartnerLink.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCustomerRepricingConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/GetCustomerRepricingConfig', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetCustomerRepricingConfigRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.CustomerRepricingConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCustomerRepricingConfigs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListCustomerRepricingConfigs', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomerRepricingConfigsRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListCustomerRepricingConfigsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCustomerRepricingConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/CreateCustomerRepricingConfig', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateCustomerRepricingConfigRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.CustomerRepricingConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCustomerRepricingConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/UpdateCustomerRepricingConfig', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateCustomerRepricingConfigRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.CustomerRepricingConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteCustomerRepricingConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/DeleteCustomerRepricingConfig', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.DeleteCustomerRepricingConfigRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetChannelPartnerRepricingConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/GetChannelPartnerRepricingConfig', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.GetChannelPartnerRepricingConfigRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.ChannelPartnerRepricingConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListChannelPartnerRepricingConfigs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListChannelPartnerRepricingConfigs', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerRepricingConfigsRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListChannelPartnerRepricingConfigsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateChannelPartnerRepricingConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/CreateChannelPartnerRepricingConfig', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.CreateChannelPartnerRepricingConfigRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.ChannelPartnerRepricingConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateChannelPartnerRepricingConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/UpdateChannelPartnerRepricingConfig', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UpdateChannelPartnerRepricingConfigRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_repricing__pb2.ChannelPartnerRepricingConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteChannelPartnerRepricingConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/DeleteChannelPartnerRepricingConfig', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.DeleteChannelPartnerRepricingConfigRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSkuGroups(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListSkuGroups', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupsRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSkuGroupBillableSkus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListSkuGroupBillableSkus', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupBillableSkusRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkuGroupBillableSkusResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def LookupOffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/LookupOffer', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.LookupOfferRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_offers__pb2.Offer.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListProducts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListProducts', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListProductsRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListProductsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSkus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListSkus', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkusRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSkusResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListOffers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListOffers', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListOffersRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListOffersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListPurchasableSkus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListPurchasableSkus', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableSkusRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableSkusResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListPurchasableOffers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListPurchasableOffers', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableOffersRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListPurchasableOffersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryEligibleBillingAccounts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/QueryEligibleBillingAccounts', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.QueryEligibleBillingAccountsRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.QueryEligibleBillingAccountsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RegisterSubscriber(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/RegisterSubscriber', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.RegisterSubscriberRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.RegisterSubscriberResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UnregisterSubscriber(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/UnregisterSubscriber', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UnregisterSubscriberRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.UnregisterSubscriberResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSubscribers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListSubscribers', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSubscribersRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListSubscribersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListEntitlementChanges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.channel.v1.CloudChannelService/ListEntitlementChanges', google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementChangesRequest.SerializeToString, google_dot_cloud_dot_channel_dot_v1_dot_service__pb2.ListEntitlementChangesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)