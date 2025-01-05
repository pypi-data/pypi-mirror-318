"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/connectors/v1/authconfig.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.connectors.v1 import common_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/connectors/v1/authconfig.proto\x12\x1agoogle.cloud.connectors.v1\x1a\'google/cloud/connectors/v1/common.proto"\xc6\x08\n\nAuthConfig\x127\n\tauth_type\x18\x01 \x01(\x0e2$.google.cloud.connectors.v1.AuthType\x12L\n\ruser_password\x18\x02 \x01(\x0b23.google.cloud.connectors.v1.AuthConfig.UserPasswordH\x00\x12S\n\x11oauth2_jwt_bearer\x18\x03 \x01(\x0b26.google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearerH\x00\x12c\n\x19oauth2_client_credentials\x18\x04 \x01(\x0b2>.google.cloud.connectors.v1.AuthConfig.Oauth2ClientCredentialsH\x00\x12M\n\x0essh_public_key\x18\x06 \x01(\x0b23.google.cloud.connectors.v1.AuthConfig.SshPublicKeyH\x00\x12H\n\x14additional_variables\x18\x05 \x03(\x0b2*.google.cloud.connectors.v1.ConfigVariable\x1aV\n\x0cUserPassword\x12\x10\n\x08username\x18\x01 \x01(\t\x124\n\x08password\x18\x02 \x01(\x0b2".google.cloud.connectors.v1.Secret\x1a\xdf\x01\n\x0fOauth2JwtBearer\x126\n\nclient_key\x18\x01 \x01(\x0b2".google.cloud.connectors.v1.Secret\x12T\n\njwt_claims\x18\x02 \x01(\x0b2@.google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.JwtClaims\x1a>\n\tJwtClaims\x12\x0e\n\x06issuer\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x10\n\x08audience\x18\x03 \x01(\t\x1ag\n\x17Oauth2ClientCredentials\x12\x11\n\tclient_id\x18\x01 \x01(\t\x129\n\rclient_secret\x18\x02 \x01(\x0b2".google.cloud.connectors.v1.Secret\x1a\xb2\x01\n\x0cSshPublicKey\x12\x10\n\x08username\x18\x01 \x01(\t\x12;\n\x0fssh_client_cert\x18\x03 \x01(\x0b2".google.cloud.connectors.v1.Secret\x12\x11\n\tcert_type\x18\x04 \x01(\t\x12@\n\x14ssh_client_cert_pass\x18\x05 \x01(\x0b2".google.cloud.connectors.v1.SecretB\x06\n\x04type"\xcf\x01\n\x12AuthConfigTemplate\x127\n\tauth_type\x18\x01 \x01(\x0e2$.google.cloud.connectors.v1.AuthType\x12U\n\x19config_variable_templates\x18\x02 \x03(\x0b22.google.cloud.connectors.v1.ConfigVariableTemplate\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t*\x9d\x01\n\x08AuthType\x12\x19\n\x15AUTH_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rUSER_PASSWORD\x10\x01\x12\x15\n\x11OAUTH2_JWT_BEARER\x10\x02\x12\x1d\n\x19OAUTH2_CLIENT_CREDENTIALS\x10\x03\x12\x12\n\x0eSSH_PUBLIC_KEY\x10\x04\x12\x19\n\x15OAUTH2_AUTH_CODE_FLOW\x10\x05Bs\n\x1ecom.google.cloud.connectors.v1B\x0fAuthConfigProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.connectors.v1.authconfig_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.connectors.v1B\x0fAuthConfigProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspb'
    _globals['_AUTHTYPE']._serialized_start = 1424
    _globals['_AUTHTYPE']._serialized_end = 1581
    _globals['_AUTHCONFIG']._serialized_start = 117
    _globals['_AUTHCONFIG']._serialized_end = 1211
    _globals['_AUTHCONFIG_USERPASSWORD']._serialized_start = 605
    _globals['_AUTHCONFIG_USERPASSWORD']._serialized_end = 691
    _globals['_AUTHCONFIG_OAUTH2JWTBEARER']._serialized_start = 694
    _globals['_AUTHCONFIG_OAUTH2JWTBEARER']._serialized_end = 917
    _globals['_AUTHCONFIG_OAUTH2JWTBEARER_JWTCLAIMS']._serialized_start = 855
    _globals['_AUTHCONFIG_OAUTH2JWTBEARER_JWTCLAIMS']._serialized_end = 917
    _globals['_AUTHCONFIG_OAUTH2CLIENTCREDENTIALS']._serialized_start = 919
    _globals['_AUTHCONFIG_OAUTH2CLIENTCREDENTIALS']._serialized_end = 1022
    _globals['_AUTHCONFIG_SSHPUBLICKEY']._serialized_start = 1025
    _globals['_AUTHCONFIG_SSHPUBLICKEY']._serialized_end = 1203
    _globals['_AUTHCONFIGTEMPLATE']._serialized_start = 1214
    _globals['_AUTHCONFIGTEMPLATE']._serialized_end = 1421