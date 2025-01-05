"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/deployment/deployment.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/devtools/containeranalysis/v1beta1/deployment/deployment.proto\x12\x1agrafeas.v1beta1.deployment\x1a\x1fgoogle/protobuf/timestamp.proto""\n\nDeployable\x12\x14\n\x0cresource_uri\x18\x01 \x03(\t"E\n\x07Details\x12:\n\ndeployment\x18\x01 \x01(\x0b2&.grafeas.v1beta1.deployment.Deployment"\xc3\x02\n\nDeployment\x12\x12\n\nuser_email\x18\x01 \x01(\t\x12/\n\x0bdeploy_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x121\n\rundeploy_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06config\x18\x04 \x01(\t\x12\x0f\n\x07address\x18\x05 \x01(\t\x12\x14\n\x0cresource_uri\x18\x06 \x03(\t\x12A\n\x08platform\x18\x07 \x01(\x0e2/.grafeas.v1beta1.deployment.Deployment.Platform"C\n\x08Platform\x12\x18\n\x14PLATFORM_UNSPECIFIED\x10\x00\x12\x07\n\x03GKE\x10\x01\x12\x08\n\x04FLEX\x10\x02\x12\n\n\x06CUSTOM\x10\x03B\x81\x01\n\x1dio.grafeas.v1beta1.deploymentP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.deployment.deployment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dio.grafeas.v1beta1.deploymentP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_DEPLOYABLE']._serialized_start = 134
    _globals['_DEPLOYABLE']._serialized_end = 168
    _globals['_DETAILS']._serialized_start = 170
    _globals['_DETAILS']._serialized_end = 239
    _globals['_DEPLOYMENT']._serialized_start = 242
    _globals['_DEPLOYMENT']._serialized_end = 565
    _globals['_DEPLOYMENT_PLATFORM']._serialized_start = 498
    _globals['_DEPLOYMENT_PLATFORM']._serialized_end = 565