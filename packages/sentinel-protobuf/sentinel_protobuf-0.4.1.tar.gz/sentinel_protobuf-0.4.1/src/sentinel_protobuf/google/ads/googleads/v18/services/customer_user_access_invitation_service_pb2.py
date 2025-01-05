"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/customer_user_access_invitation_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.resources import customer_user_access_invitation_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_resources_dot_customer__user__access__invitation__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOgoogle/ads/googleads/v18/services/customer_user_access_invitation_service.proto\x12!google.ads.googleads.v18.services\x1aHgoogle/ads/googleads/v18/resources/customer_user_access_invitation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa7\x01\n)MutateCustomerUserAccessInvitationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12`\n\toperation\x18\x02 \x01(\x0b2H.google.ads.googleads.v18.services.CustomerUserAccessInvitationOperationB\x03\xe0A\x02"\xd6\x01\n%CustomerUserAccessInvitationOperation\x12R\n\x06create\x18\x01 \x01(\x0b2@.google.ads.googleads.v18.resources.CustomerUserAccessInvitationH\x00\x12L\n\x06remove\x18\x02 \x01(\tB:\xfaA7\n5googleads.googleapis.com/CustomerUserAccessInvitationH\x00B\x0b\n\toperation"\x89\x01\n*MutateCustomerUserAccessInvitationResponse\x12[\n\x06result\x18\x01 \x01(\x0b2K.google.ads.googleads.v18.services.MutateCustomerUserAccessInvitationResult"}\n(MutateCustomerUserAccessInvitationResult\x12Q\n\rresource_name\x18\x01 \x01(\tB:\xfaA7\n5googleads.googleapis.com/CustomerUserAccessInvitation2\x98\x03\n#CustomerUserAccessInvitationService\x12\xa9\x02\n"MutateCustomerUserAccessInvitation\x12L.google.ads.googleads.v18.services.MutateCustomerUserAccessInvitationRequest\x1aM.google.ads.googleads.v18.services.MutateCustomerUserAccessInvitationResponse"f\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02H"C/v18/customers/{customer_id=*}/customerUserAccessInvitations:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x94\x02\n%com.google.ads.googleads.v18.servicesB(CustomerUserAccessInvitationServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.customer_user_access_invitation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB(CustomerUserAccessInvitationServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMERUSERACCESSINVITATIONOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATIONOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA7\n5googleads.googleapis.com/CustomerUserAccessInvitation'
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA7\n5googleads.googleapis.com/CustomerUserAccessInvitation'
    _globals['_CUSTOMERUSERACCESSINVITATIONSERVICE']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMERUSERACCESSINVITATIONSERVICE'].methods_by_name['MutateCustomerUserAccessInvitation']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATIONSERVICE'].methods_by_name['MutateCustomerUserAccessInvitation']._serialized_options = b'\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02H"C/v18/customers/{customer_id=*}/customerUserAccessInvitations:mutate:\x01*'
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONREQUEST']._serialized_start = 308
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONREQUEST']._serialized_end = 475
    _globals['_CUSTOMERUSERACCESSINVITATIONOPERATION']._serialized_start = 478
    _globals['_CUSTOMERUSERACCESSINVITATIONOPERATION']._serialized_end = 692
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONRESPONSE']._serialized_start = 695
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONRESPONSE']._serialized_end = 832
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONRESULT']._serialized_start = 834
    _globals['_MUTATECUSTOMERUSERACCESSINVITATIONRESULT']._serialized_end = 959
    _globals['_CUSTOMERUSERACCESSINVITATIONSERVICE']._serialized_start = 962
    _globals['_CUSTOMERUSERACCESSINVITATIONSERVICE']._serialized_end = 1370