"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networksecurity/v1beta1/tls.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/networksecurity/v1beta1/tls.proto\x12$google.cloud.networksecurity.v1beta1\x1a\x1fgoogle/api/field_behavior.proto"\'\n\x0cGrpcEndpoint\x12\x17\n\ntarget_uri\x18\x01 \x01(\tB\x03\xe0A\x02"\xcf\x01\n\x0cValidationCA\x12K\n\rgrpc_endpoint\x18\x02 \x01(\x0b22.google.cloud.networksecurity.v1beta1.GrpcEndpointH\x00\x12j\n\x1dcertificate_provider_instance\x18\x03 \x01(\x0b2A.google.cloud.networksecurity.v1beta1.CertificateProviderInstanceH\x00B\x06\n\x04type";\n\x1bCertificateProviderInstance\x12\x1c\n\x0fplugin_instance\x18\x01 \x01(\tB\x03\xe0A\x02"\xd6\x01\n\x13CertificateProvider\x12K\n\rgrpc_endpoint\x18\x02 \x01(\x0b22.google.cloud.networksecurity.v1beta1.GrpcEndpointH\x00\x12j\n\x1dcertificate_provider_instance\x18\x03 \x01(\x0b2A.google.cloud.networksecurity.v1beta1.CertificateProviderInstanceH\x00B\x06\n\x04typeB\x82\x02\n(com.google.cloud.networksecurity.v1beta1B\x08TlsProtoP\x01ZRcloud.google.com/go/networksecurity/apiv1beta1/networksecuritypb;networksecuritypb\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02\'Google::Cloud::NetworkSecurity::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networksecurity.v1beta1.tls_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.networksecurity.v1beta1B\x08TlsProtoP\x01ZRcloud.google.com/go/networksecurity/apiv1beta1/networksecuritypb;networksecuritypb\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02'Google::Cloud::NetworkSecurity::V1beta1"
    _globals['_GRPCENDPOINT'].fields_by_name['target_uri']._loaded_options = None
    _globals['_GRPCENDPOINT'].fields_by_name['target_uri']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATEPROVIDERINSTANCE'].fields_by_name['plugin_instance']._loaded_options = None
    _globals['_CERTIFICATEPROVIDERINSTANCE'].fields_by_name['plugin_instance']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCENDPOINT']._serialized_start = 121
    _globals['_GRPCENDPOINT']._serialized_end = 160
    _globals['_VALIDATIONCA']._serialized_start = 163
    _globals['_VALIDATIONCA']._serialized_end = 370
    _globals['_CERTIFICATEPROVIDERINSTANCE']._serialized_start = 372
    _globals['_CERTIFICATEPROVIDERINSTANCE']._serialized_end = 431
    _globals['_CERTIFICATEPROVIDER']._serialized_start = 434
    _globals['_CERTIFICATEPROVIDER']._serialized_end = 648