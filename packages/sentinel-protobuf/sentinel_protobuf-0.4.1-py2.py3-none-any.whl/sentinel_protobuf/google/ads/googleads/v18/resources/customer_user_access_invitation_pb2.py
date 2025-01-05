"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/customer_user_access_invitation.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import access_invitation_status_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_access__invitation__status__pb2
from ......google.ads.googleads.v18.enums import access_role_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_access__role__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/ads/googleads/v18/resources/customer_user_access_invitation.proto\x12"google.ads.googleads.v18.resources\x1a=google/ads/googleads/v18/enums/access_invitation_status.proto\x1a0google/ads/googleads/v18/enums/access_role.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x99\x04\n\x1cCustomerUserAccessInvitation\x12T\n\rresource_name\x18\x01 \x01(\tB=\xe0A\x05\xfaA7\n5googleads.googleapis.com/CustomerUserAccessInvitation\x12\x1a\n\rinvitation_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12S\n\x0baccess_role\x18\x03 \x01(\x0e29.google.ads.googleads.v18.enums.AccessRoleEnum.AccessRoleB\x03\xe0A\x05\x12\x1a\n\remail_address\x18\x04 \x01(\tB\x03\xe0A\x05\x12\x1f\n\x12creation_date_time\x18\x05 \x01(\tB\x03\xe0A\x03\x12q\n\x11invitation_status\x18\x06 \x01(\x0e2Q.google.ads.googleads.v18.enums.AccessInvitationStatusEnum.AccessInvitationStatusB\x03\xe0A\x03:\x81\x01\xeaA~\n5googleads.googleapis.com/CustomerUserAccessInvitation\x12Ecustomers/{customer_id}/customerUserAccessInvitations/{invitation_id}B\x93\x02\n&com.google.ads.googleads.v18.resourcesB!CustomerUserAccessInvitationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.customer_user_access_invitation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB!CustomerUserAccessInvitationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA7\n5googleads.googleapis.com/CustomerUserAccessInvitation'
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['invitation_id']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['invitation_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['access_role']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['access_role']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['email_address']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['email_address']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['creation_date_time']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['creation_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['invitation_status']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATION'].fields_by_name['invitation_status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERUSERACCESSINVITATION']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSINVITATION']._serialized_options = b'\xeaA~\n5googleads.googleapis.com/CustomerUserAccessInvitation\x12Ecustomers/{customer_id}/customerUserAccessInvitations/{invitation_id}'
    _globals['_CUSTOMERUSERACCESSINVITATION']._serialized_start = 286
    _globals['_CUSTOMERUSERACCESSINVITATION']._serialized_end = 823