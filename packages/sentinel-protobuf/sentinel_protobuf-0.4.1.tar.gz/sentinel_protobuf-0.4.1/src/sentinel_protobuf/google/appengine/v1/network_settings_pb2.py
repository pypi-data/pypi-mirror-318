"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1/network_settings.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/appengine/v1/network_settings.proto\x12\x13google.appengine.v1"\xaa\x02\n\x0fNetworkSettings\x12[\n\x17ingress_traffic_allowed\x18\x01 \x01(\x0e2:.google.appengine.v1.NetworkSettings.IngressTrafficAllowed"\xb9\x01\n\x15IngressTrafficAllowed\x12\'\n#INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED\x10\x00\x12\x1f\n\x1bINGRESS_TRAFFIC_ALLOWED_ALL\x10\x01\x12)\n%INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY\x10\x02\x12+\n\'INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB\x10\x03B\xc5\x01\n\x17com.google.appengine.v1B\x14NetworkSettingsProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1.network_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.appengine.v1B\x14NetworkSettingsProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1'
    _globals['_NETWORKSETTINGS']._serialized_start = 68
    _globals['_NETWORKSETTINGS']._serialized_end = 366
    _globals['_NETWORKSETTINGS_INGRESSTRAFFICALLOWED']._serialized_start = 181
    _globals['_NETWORKSETTINGS_INGRESSTRAFFICALLOWED']._serialized_end = 366