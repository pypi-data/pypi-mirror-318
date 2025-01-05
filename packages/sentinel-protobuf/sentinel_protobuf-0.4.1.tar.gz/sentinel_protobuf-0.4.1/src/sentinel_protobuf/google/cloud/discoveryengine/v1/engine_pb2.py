"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1/engine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/discoveryengine/v1/engine.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/discoveryengine/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x83\x0b\n\x06Engine\x12V\n\x12chat_engine_config\x18\x0b \x01(\x0b28.google.cloud.discoveryengine.v1.Engine.ChatEngineConfigH\x00\x12Z\n\x14search_engine_config\x18\r \x01(\x0b2:.google.cloud.discoveryengine.v1.Engine.SearchEngineConfigH\x00\x12_\n\x14chat_engine_metadata\x18\x0c \x01(\x0b2:.google.cloud.discoveryengine.v1.Engine.ChatEngineMetadataB\x03\xe0A\x03H\x01\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x16\n\x0edata_store_ids\x18\x05 \x03(\t\x12I\n\rsolution_type\x18\x06 \x01(\x0e2-.google.cloud.discoveryengine.v1.SolutionTypeB\x03\xe0A\x02\x12L\n\x11industry_vertical\x18\x10 \x01(\x0e21.google.cloud.discoveryengine.v1.IndustryVertical\x12K\n\rcommon_config\x18\x0f \x01(\x0b24.google.cloud.discoveryengine.v1.Engine.CommonConfig\x12\x1e\n\x11disable_analytics\x18\x1a \x01(\x08B\x03\xe0A\x01\x1a\x9c\x01\n\x12SearchEngineConfig\x12@\n\x0bsearch_tier\x18\x01 \x01(\x0e2+.google.cloud.discoveryengine.v1.SearchTier\x12D\n\x0esearch_add_ons\x18\x02 \x03(\x0e2,.google.cloud.discoveryengine.v1.SearchAddOn\x1a\x93\x02\n\x10ChatEngineConfig\x12k\n\x15agent_creation_config\x18\x01 \x01(\x0b2L.google.cloud.discoveryengine.v1.Engine.ChatEngineConfig.AgentCreationConfig\x12 \n\x18dialogflow_agent_to_link\x18\x02 \x01(\t\x1ap\n\x13AgentCreationConfig\x12\x10\n\x08business\x18\x01 \x01(\t\x12\x1d\n\x15default_language_code\x18\x02 \x01(\t\x12\x16\n\ttime_zone\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08location\x18\x04 \x01(\t\x1a$\n\x0cCommonConfig\x12\x14\n\x0ccompany_name\x18\x01 \x01(\t\x1a.\n\x12ChatEngineMetadata\x12\x18\n\x10dialogflow_agent\x18\x01 \x01(\t:}\xeaAz\n%discoveryengine.googleapis.com/Engine\x12Qprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}B\x0f\n\rengine_configB\x11\n\x0fengine_metadataB\xfe\x01\n#com.google.cloud.discoveryengine.v1B\x0bEngineProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0bEngineProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG'].fields_by_name['time_zone']._loaded_options = None
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE'].fields_by_name['chat_engine_metadata']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['chat_engine_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE'].fields_by_name['name']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_ENGINE'].fields_by_name['display_name']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE'].fields_by_name['solution_type']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['solution_type']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE'].fields_by_name['disable_analytics']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['disable_analytics']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINE']._loaded_options = None
    _globals['_ENGINE']._serialized_options = b'\xeaAz\n%discoveryengine.googleapis.com/Engine\x12Qprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}'
    _globals['_ENGINE']._serialized_start = 221
    _globals['_ENGINE']._serialized_end = 1632
    _globals['_ENGINE_SEARCHENGINECONFIG']._serialized_start = 949
    _globals['_ENGINE_SEARCHENGINECONFIG']._serialized_end = 1105
    _globals['_ENGINE_CHATENGINECONFIG']._serialized_start = 1108
    _globals['_ENGINE_CHATENGINECONFIG']._serialized_end = 1383
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG']._serialized_start = 1271
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG']._serialized_end = 1383
    _globals['_ENGINE_COMMONCONFIG']._serialized_start = 1385
    _globals['_ENGINE_COMMONCONFIG']._serialized_end = 1421
    _globals['_ENGINE_CHATENGINEMETADATA']._serialized_start = 1423
    _globals['_ENGINE_CHATENGINEMETADATA']._serialized_end = 1469