"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/connectors/v1/ssl_config.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.connectors.v1 import common_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/connectors/v1/ssl_config.proto\x12\x1agoogle.cloud.connectors.v1\x1a\'google/cloud/connectors/v1/common.proto"\xb6\x02\n\x11SslConfigTemplate\x125\n\x08ssl_type\x18\x01 \x01(\x0e2#.google.cloud.connectors.v1.SslType\x12\x18\n\x10is_tls_mandatory\x18\x02 \x01(\x08\x12>\n\x10server_cert_type\x18\x03 \x03(\x0e2$.google.cloud.connectors.v1.CertType\x12>\n\x10client_cert_type\x18\x04 \x03(\x0e2$.google.cloud.connectors.v1.CertType\x12P\n\x14additional_variables\x18\x05 \x03(\x0b22.google.cloud.connectors.v1.ConfigVariableTemplate"\xa2\x05\n\tSslConfig\x121\n\x04type\x18\x01 \x01(\x0e2#.google.cloud.connectors.v1.SslType\x12E\n\x0btrust_model\x18\x02 \x01(\x0e20.google.cloud.connectors.v1.SslConfig.TrustModel\x12F\n\x1aprivate_server_certificate\x18\x03 \x01(\x0b2".google.cloud.connectors.v1.Secret\x12>\n\x12client_certificate\x18\x04 \x01(\x0b2".google.cloud.connectors.v1.Secret\x12>\n\x12client_private_key\x18\x05 \x01(\x0b2".google.cloud.connectors.v1.Secret\x12C\n\x17client_private_key_pass\x18\x06 \x01(\x0b2".google.cloud.connectors.v1.Secret\x12>\n\x10server_cert_type\x18\x07 \x01(\x0e2$.google.cloud.connectors.v1.CertType\x12>\n\x10client_cert_type\x18\x08 \x01(\x0e2$.google.cloud.connectors.v1.CertType\x12\x0f\n\x07use_ssl\x18\t \x01(\x08\x12H\n\x14additional_variables\x18\n \x03(\x0b2*.google.cloud.connectors.v1.ConfigVariable"3\n\nTrustModel\x12\n\n\x06PUBLIC\x10\x00\x12\x0b\n\x07PRIVATE\x10\x01\x12\x0c\n\x08INSECURE\x10\x02*6\n\x07SslType\x12\x18\n\x14SSL_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03TLS\x10\x01\x12\x08\n\x04MTLS\x10\x02*.\n\x08CertType\x12\x19\n\x15CERT_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03PEM\x10\x01Br\n\x1ecom.google.cloud.connectors.v1B\x0eSslConfigProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.connectors.v1.ssl_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.connectors.v1B\x0eSslConfigProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspb'
    _globals['_SSLTYPE']._serialized_start = 1106
    _globals['_SSLTYPE']._serialized_end = 1160
    _globals['_CERTTYPE']._serialized_start = 1162
    _globals['_CERTTYPE']._serialized_end = 1208
    _globals['_SSLCONFIGTEMPLATE']._serialized_start = 117
    _globals['_SSLCONFIGTEMPLATE']._serialized_end = 427
    _globals['_SSLCONFIG']._serialized_start = 430
    _globals['_SSLCONFIG']._serialized_end = 1104
    _globals['_SSLCONFIG_TRUSTMODEL']._serialized_start = 1053
    _globals['_SSLCONFIG_TRUSTMODEL']._serialized_end = 1104