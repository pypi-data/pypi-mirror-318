"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/team_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/ads/admanager/v1/team_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x86\x01\n\x04Team\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x07team_id\x18\x02 \x01(\x03B\x03\xe0A\x03:U\xeaAR\n\x1dadmanager.googleapis.com/Team\x12$networks/{network_code}/teams/{team}*\x05teams2\x04teamB\xc5\x01\n\x1bcom.google.ads.admanager.v1B\x11TeamMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.team_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x11TeamMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_TEAM'].fields_by_name['name']._loaded_options = None
    _globals['_TEAM'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TEAM'].fields_by_name['team_id']._loaded_options = None
    _globals['_TEAM'].fields_by_name['team_id']._serialized_options = b'\xe0A\x03'
    _globals['_TEAM']._loaded_options = None
    _globals['_TEAM']._serialized_options = b'\xeaAR\n\x1dadmanager.googleapis.com/Team\x12$networks/{network_code}/teams/{team}*\x05teams2\x04team'
    _globals['_TEAM']._serialized_start = 133
    _globals['_TEAM']._serialized_end = 267