"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/marketingplatform/admin/v1alpha/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/marketingplatform/admin/v1alpha/resources.proto\x12&google.marketingplatform.admin.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xab\x01\n\x0cOrganization\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t:r\xeaAo\n2marketingplatformadmin.googleapis.com/Organization\x12\x1corganizations/{organization}*\rorganizations2\x0corganization"\xb3\x03\n\x14AnalyticsAccountLink\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12K\n\x11analytics_account\x18\x02 \x01(\tB0\xe0A\x02\xe0A\x05\xfaA\'\n%analyticsadmin.googleapis.com/Account\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x03\x12c\n\x17link_verification_state\x18\x04 \x01(\x0e2=.google.marketingplatform.admin.v1alpha.LinkVerificationStateB\x03\xe0A\x03:\xba\x01\xeaA\xb6\x01\n:marketingplatformadmin.googleapis.com/AnalyticsAccountLink\x12Korganizations/{organization}/analyticsAccountLinks/{analytics_account_link}*\x15analyticsAccountLinks2\x14analyticsAccountLink*\x90\x01\n\x15LinkVerificationState\x12\'\n#LINK_VERIFICATION_STATE_UNSPECIFIED\x10\x00\x12$\n LINK_VERIFICATION_STATE_VERIFIED\x10\x01\x12(\n$LINK_VERIFICATION_STATE_NOT_VERIFIED\x10\x02B\xd8\x02\n.com.google.ads.marketingplatform.admin.v1alphaB\x0eResourcesProtoP\x01ZKgoogle.golang.org/genproto/googleapis/marketingplatform/admin/v1alpha;admin\xaa\x02*Google.Ads.MarketingPlatform.Admin.V1Alpha\xca\x02*Google\\Ads\\MarketingPlatform\\Admin\\V1alpha\xea\x02.Google::Ads::MarketingPlatform::Admin::V1alpha\xeaA;\n%analyticsadmin.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.marketingplatform.admin.v1alpha.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.ads.marketingplatform.admin.v1alphaB\x0eResourcesProtoP\x01ZKgoogle.golang.org/genproto/googleapis/marketingplatform/admin/v1alpha;admin\xaa\x02*Google.Ads.MarketingPlatform.Admin.V1Alpha\xca\x02*Google\\Ads\\MarketingPlatform\\Admin\\V1alpha\xea\x02.Google::Ads::MarketingPlatform::Admin::V1alpha\xeaA;\n%analyticsadmin.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_ORGANIZATION'].fields_by_name['name']._loaded_options = None
    _globals['_ORGANIZATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ORGANIZATION']._loaded_options = None
    _globals['_ORGANIZATION']._serialized_options = b'\xeaAo\n2marketingplatformadmin.googleapis.com/Organization\x12\x1corganizations/{organization}*\rorganizations2\x0corganization'
    _globals['_ANALYTICSACCOUNTLINK'].fields_by_name['name']._loaded_options = None
    _globals['_ANALYTICSACCOUNTLINK'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ANALYTICSACCOUNTLINK'].fields_by_name['analytics_account']._loaded_options = None
    _globals['_ANALYTICSACCOUNTLINK'].fields_by_name['analytics_account']._serialized_options = b"\xe0A\x02\xe0A\x05\xfaA'\n%analyticsadmin.googleapis.com/Account"
    _globals['_ANALYTICSACCOUNTLINK'].fields_by_name['display_name']._loaded_options = None
    _globals['_ANALYTICSACCOUNTLINK'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_ANALYTICSACCOUNTLINK'].fields_by_name['link_verification_state']._loaded_options = None
    _globals['_ANALYTICSACCOUNTLINK'].fields_by_name['link_verification_state']._serialized_options = b'\xe0A\x03'
    _globals['_ANALYTICSACCOUNTLINK']._loaded_options = None
    _globals['_ANALYTICSACCOUNTLINK']._serialized_options = b'\xeaA\xb6\x01\n:marketingplatformadmin.googleapis.com/AnalyticsAccountLink\x12Korganizations/{organization}/analyticsAccountLinks/{analytics_account_link}*\x15analyticsAccountLinks2\x14analyticsAccountLink'
    _globals['_LINKVERIFICATIONSTATE']._serialized_start = 771
    _globals['_LINKVERIFICATIONSTATE']._serialized_end = 915
    _globals['_ORGANIZATION']._serialized_start = 159
    _globals['_ORGANIZATION']._serialized_end = 330
    _globals['_ANALYTICSACCOUNTLINK']._serialized_start = 333
    _globals['_ANALYTICSACCOUNTLINK']._serialized_end = 768