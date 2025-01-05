"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/service.proto')
_sym_db = _symbol_database.Default()
from ....google.appengine.v1beta import network_settings_pb2 as google_dot_appengine_dot_v1beta_dot_network__settings__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/appengine/v1beta/service.proto\x12\x17google.appengine.v1beta\x1a.google/appengine/v1beta/network_settings.proto"\x9d\x01\n\x07Service\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x124\n\x05split\x18\x03 \x01(\x0b2%.google.appengine.v1beta.TrafficSplit\x12B\n\x10network_settings\x18\x06 \x01(\x0b2(.google.appengine.v1beta.NetworkSettings"\x8c\x02\n\x0cTrafficSplit\x12?\n\x08shard_by\x18\x01 \x01(\x0e2-.google.appengine.v1beta.TrafficSplit.ShardBy\x12K\n\x0ballocations\x18\x02 \x03(\x0b26.google.appengine.v1beta.TrafficSplit.AllocationsEntry\x1a2\n\x10AllocationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x028\x01":\n\x07ShardBy\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\n\n\x06COOKIE\x10\x01\x12\x06\n\x02IP\x10\x02\x12\n\n\x06RANDOM\x10\x03B\xd2\x01\n\x1bcom.google.appengine.v1betaB\x0cServiceProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.v1betaB\x0cServiceProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_TRAFFICSPLIT_ALLOCATIONSENTRY']._loaded_options = None
    _globals['_TRAFFICSPLIT_ALLOCATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_SERVICE']._serialized_start = 115
    _globals['_SERVICE']._serialized_end = 272
    _globals['_TRAFFICSPLIT']._serialized_start = 275
    _globals['_TRAFFICSPLIT']._serialized_end = 543
    _globals['_TRAFFICSPLIT_ALLOCATIONSENTRY']._serialized_start = 433
    _globals['_TRAFFICSPLIT_ALLOCATIONSENTRY']._serialized_end = 483
    _globals['_TRAFFICSPLIT_SHARDBY']._serialized_start = 485
    _globals['_TRAFFICSPLIT_SHARDBY']._serialized_end = 543