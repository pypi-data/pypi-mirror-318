"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/entity_signals_mapping_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/admanager/v1/entity_signals_mapping_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8b\x03\n\x14EntitySignalsMapping\x12\x1d\n\x13audience_segment_id\x18\x03 \x01(\x03H\x00\x12\x1b\n\x11content_bundle_id\x18\x04 \x01(\x03H\x00\x12#\n\x19custom_targeting_value_id\x18\x05 \x01(\x03H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12&\n\x19entity_signals_mapping_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12"\n\x15taxonomy_category_ids\x18\x06 \x03(\x03B\x03\xe0A\x02:\xa8\x01\xeaA\xa4\x01\n-admanager.googleapis.com/EntitySignalsMapping\x12Fnetworks/{network_code}/entitySignalsMappings/{entity_signals_mapping}*\x15entitySignalsMappings2\x14entitySignalsMappingB\x08\n\x06entityB\xd5\x01\n\x1bcom.google.ads.admanager.v1B!EntitySignalsMappingMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.entity_signals_mapping_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B!EntitySignalsMappingMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_ENTITYSIGNALSMAPPING'].fields_by_name['name']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPING'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ENTITYSIGNALSMAPPING'].fields_by_name['entity_signals_mapping_id']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPING'].fields_by_name['entity_signals_mapping_id']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITYSIGNALSMAPPING'].fields_by_name['taxonomy_category_ids']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPING'].fields_by_name['taxonomy_category_ids']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYSIGNALSMAPPING']._loaded_options = None
    _globals['_ENTITYSIGNALSMAPPING']._serialized_options = b'\xeaA\xa4\x01\n-admanager.googleapis.com/EntitySignalsMapping\x12Fnetworks/{network_code}/entitySignalsMappings/{entity_signals_mapping}*\x15entitySignalsMappings2\x14entitySignalsMapping'
    _globals['_ENTITYSIGNALSMAPPING']._serialized_start = 151
    _globals['_ENTITYSIGNALSMAPPING']._serialized_end = 546