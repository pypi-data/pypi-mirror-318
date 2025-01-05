"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/accounts/v1beta/businessidentity.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/shopping/merchant/accounts/v1beta/businessidentity.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xa5\t\n\x10BusinessIdentity\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12m\n\x12promotions_consent\x18\x02 \x01(\x0e2L.google.shopping.merchant.accounts.v1beta.BusinessIdentity.PromotionsConsentB\x03\xe0A\x01\x12f\n\x0bblack_owned\x18\x03 \x01(\x0b2L.google.shopping.merchant.accounts.v1beta.BusinessIdentity.IdentityAttributeB\x03\xe0A\x01\x12f\n\x0bwomen_owned\x18\x04 \x01(\x0b2L.google.shopping.merchant.accounts.v1beta.BusinessIdentity.IdentityAttributeB\x03\xe0A\x01\x12h\n\rveteran_owned\x18\x05 \x01(\x0b2L.google.shopping.merchant.accounts.v1beta.BusinessIdentity.IdentityAttributeB\x03\xe0A\x01\x12g\n\x0clatino_owned\x18\x06 \x01(\x0b2L.google.shopping.merchant.accounts.v1beta.BusinessIdentity.IdentityAttributeB\x03\xe0A\x01\x12i\n\x0esmall_business\x18\x07 \x01(\x0b2L.google.shopping.merchant.accounts.v1beta.BusinessIdentity.IdentityAttributeB\x03\xe0A\x01\x1a\x8d\x02\n\x11IdentityAttribute\x12\x83\x01\n\x14identity_declaration\x18\x01 \x01(\x0e2`.google.shopping.merchant.accounts.v1beta.BusinessIdentity.IdentityAttribute.IdentityDeclarationB\x03\xe0A\x02"r\n\x13IdentityDeclaration\x12$\n IDENTITY_DECLARATION_UNSPECIFIED\x10\x00\x12\x16\n\x12SELF_IDENTIFIES_AS\x10\x01\x12\x1d\n\x19DOES_NOT_SELF_IDENTIFY_AS\x10\x02"t\n\x11PromotionsConsent\x12"\n\x1ePROMOTIONS_CONSENT_UNSPECIFIED\x10\x00\x12\x1c\n\x18PROMOTIONS_CONSENT_GIVEN\x10\x01\x12\x1d\n\x19PROMOTIONS_CONSENT_DENIED\x10\x02:{\xeaAx\n+merchantapi.googleapis.com/BusinessIdentity\x12#accounts/{account}/businessIdentity*\x12businessIdentities2\x10businessIdentity"_\n\x1aGetBusinessIdentityRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/BusinessIdentity"\xb1\x01\n\x1dUpdateBusinessIdentityRequest\x12Z\n\x11business_identity\x18\x01 \x01(\x0b2:.google.shopping.merchant.accounts.v1beta.BusinessIdentityB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\xe3\x04\n\x17BusinessIdentityService\x12\xdb\x01\n\x13GetBusinessIdentity\x12D.google.shopping.merchant.accounts.v1beta.GetBusinessIdentityRequest\x1a:.google.shopping.merchant.accounts.v1beta.BusinessIdentity"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/accounts/v1beta/{name=accounts/*/businessIdentity}\x12\xa0\x02\n\x16UpdateBusinessIdentity\x12G.google.shopping.merchant.accounts.v1beta.UpdateBusinessIdentityRequest\x1a:.google.shopping.merchant.accounts.v1beta.BusinessIdentity"\x80\x01\xdaA\x1dbusiness_identity,update_mask\x82\xd3\xe4\x93\x02Z2E/accounts/v1beta/{business_identity.name=accounts/*/businessIdentity}:\x11business_identity\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x97\x01\n,com.google.shopping.merchant.accounts.v1betaB\x15BusinessIdentityProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.businessidentity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x15BusinessIdentityProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_BUSINESSIDENTITY_IDENTITYATTRIBUTE'].fields_by_name['identity_declaration']._loaded_options = None
    _globals['_BUSINESSIDENTITY_IDENTITYATTRIBUTE'].fields_by_name['identity_declaration']._serialized_options = b'\xe0A\x02'
    _globals['_BUSINESSIDENTITY'].fields_by_name['name']._loaded_options = None
    _globals['_BUSINESSIDENTITY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_BUSINESSIDENTITY'].fields_by_name['promotions_consent']._loaded_options = None
    _globals['_BUSINESSIDENTITY'].fields_by_name['promotions_consent']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSIDENTITY'].fields_by_name['black_owned']._loaded_options = None
    _globals['_BUSINESSIDENTITY'].fields_by_name['black_owned']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSIDENTITY'].fields_by_name['women_owned']._loaded_options = None
    _globals['_BUSINESSIDENTITY'].fields_by_name['women_owned']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSIDENTITY'].fields_by_name['veteran_owned']._loaded_options = None
    _globals['_BUSINESSIDENTITY'].fields_by_name['veteran_owned']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSIDENTITY'].fields_by_name['latino_owned']._loaded_options = None
    _globals['_BUSINESSIDENTITY'].fields_by_name['latino_owned']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSIDENTITY'].fields_by_name['small_business']._loaded_options = None
    _globals['_BUSINESSIDENTITY'].fields_by_name['small_business']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSIDENTITY']._loaded_options = None
    _globals['_BUSINESSIDENTITY']._serialized_options = b'\xeaAx\n+merchantapi.googleapis.com/BusinessIdentity\x12#accounts/{account}/businessIdentity*\x12businessIdentities2\x10businessIdentity'
    _globals['_GETBUSINESSIDENTITYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBUSINESSIDENTITYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/BusinessIdentity'
    _globals['_UPDATEBUSINESSIDENTITYREQUEST'].fields_by_name['business_identity']._loaded_options = None
    _globals['_UPDATEBUSINESSIDENTITYREQUEST'].fields_by_name['business_identity']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBUSINESSIDENTITYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBUSINESSIDENTITYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_BUSINESSIDENTITYSERVICE']._loaded_options = None
    _globals['_BUSINESSIDENTITYSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_BUSINESSIDENTITYSERVICE'].methods_by_name['GetBusinessIdentity']._loaded_options = None
    _globals['_BUSINESSIDENTITYSERVICE'].methods_by_name['GetBusinessIdentity']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/accounts/v1beta/{name=accounts/*/businessIdentity}'
    _globals['_BUSINESSIDENTITYSERVICE'].methods_by_name['UpdateBusinessIdentity']._loaded_options = None
    _globals['_BUSINESSIDENTITYSERVICE'].methods_by_name['UpdateBusinessIdentity']._serialized_options = b'\xdaA\x1dbusiness_identity,update_mask\x82\xd3\xe4\x93\x02Z2E/accounts/v1beta/{business_identity.name=accounts/*/businessIdentity}:\x11business_identity'
    _globals['_BUSINESSIDENTITY']._serialized_start = 259
    _globals['_BUSINESSIDENTITY']._serialized_end = 1448
    _globals['_BUSINESSIDENTITY_IDENTITYATTRIBUTE']._serialized_start = 936
    _globals['_BUSINESSIDENTITY_IDENTITYATTRIBUTE']._serialized_end = 1205
    _globals['_BUSINESSIDENTITY_IDENTITYATTRIBUTE_IDENTITYDECLARATION']._serialized_start = 1091
    _globals['_BUSINESSIDENTITY_IDENTITYATTRIBUTE_IDENTITYDECLARATION']._serialized_end = 1205
    _globals['_BUSINESSIDENTITY_PROMOTIONSCONSENT']._serialized_start = 1207
    _globals['_BUSINESSIDENTITY_PROMOTIONSCONSENT']._serialized_end = 1323
    _globals['_GETBUSINESSIDENTITYREQUEST']._serialized_start = 1450
    _globals['_GETBUSINESSIDENTITYREQUEST']._serialized_end = 1545
    _globals['_UPDATEBUSINESSIDENTITYREQUEST']._serialized_start = 1548
    _globals['_UPDATEBUSINESSIDENTITYREQUEST']._serialized_end = 1725
    _globals['_BUSINESSIDENTITYSERVICE']._serialized_start = 1728
    _globals['_BUSINESSIDENTITYSERVICE']._serialized_end = 2339