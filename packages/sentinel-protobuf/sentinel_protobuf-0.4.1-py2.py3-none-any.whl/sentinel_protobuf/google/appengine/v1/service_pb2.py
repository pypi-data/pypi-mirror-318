"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1/service.proto')
_sym_db = _symbol_database.Default()
from ....google.appengine.v1 import network_settings_pb2 as google_dot_appengine_dot_v1_dot_network__settings__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/appengine/v1/service.proto\x12\x13google.appengine.v1\x1a*google/appengine/v1/network_settings.proto"\xfe\x01\n\x07Service\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x120\n\x05split\x18\x03 \x01(\x0b2!.google.appengine.v1.TrafficSplit\x128\n\x06labels\x18\x04 \x03(\x0b2(.google.appengine.v1.Service.LabelsEntry\x12>\n\x10network_settings\x18\x06 \x01(\x0b2$.google.appengine.v1.NetworkSettings\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x84\x02\n\x0cTrafficSplit\x12;\n\x08shard_by\x18\x01 \x01(\x0e2).google.appengine.v1.TrafficSplit.ShardBy\x12G\n\x0ballocations\x18\x02 \x03(\x0b22.google.appengine.v1.TrafficSplit.AllocationsEntry\x1a2\n\x10AllocationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x028\x01":\n\x07ShardBy\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\n\n\x06COOKIE\x10\x01\x12\x06\n\x02IP\x10\x02\x12\n\n\x06RANDOM\x10\x03B\xbd\x01\n\x17com.google.appengine.v1B\x0cServiceProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.appengine.v1B\x0cServiceProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1'
    _globals['_SERVICE_LABELSENTRY']._loaded_options = None
    _globals['_SERVICE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TRAFFICSPLIT_ALLOCATIONSENTRY']._loaded_options = None
    _globals['_TRAFFICSPLIT_ALLOCATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_SERVICE']._serialized_start = 103
    _globals['_SERVICE']._serialized_end = 357
    _globals['_SERVICE_LABELSENTRY']._serialized_start = 312
    _globals['_SERVICE_LABELSENTRY']._serialized_end = 357
    _globals['_TRAFFICSPLIT']._serialized_start = 360
    _globals['_TRAFFICSPLIT']._serialized_end = 620
    _globals['_TRAFFICSPLIT_ALLOCATIONSENTRY']._serialized_start = 510
    _globals['_TRAFFICSPLIT_ALLOCATIONSENTRY']._serialized_end = 560
    _globals['_TRAFFICSPLIT_SHARDBY']._serialized_start = 562
    _globals['_TRAFFICSPLIT_SHARDBY']._serialized_end = 620