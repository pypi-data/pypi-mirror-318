"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1beta/engine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/discoveryengine/v1beta/engine.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1beta/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa7\x0b\n\x06Engine\x12Z\n\x12chat_engine_config\x18\x0b \x01(\x0b2<.google.cloud.discoveryengine.v1beta.Engine.ChatEngineConfigH\x00\x12^\n\x14search_engine_config\x18\r \x01(\x0b2>.google.cloud.discoveryengine.v1beta.Engine.SearchEngineConfigH\x00\x12c\n\x14chat_engine_metadata\x18\x0c \x01(\x0b2>.google.cloud.discoveryengine.v1beta.Engine.ChatEngineMetadataB\x03\xe0A\x03H\x01\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x16\n\x0edata_store_ids\x18\x05 \x03(\t\x12M\n\rsolution_type\x18\x06 \x01(\x0e21.google.cloud.discoveryengine.v1beta.SolutionTypeB\x03\xe0A\x02\x12P\n\x11industry_vertical\x18\x10 \x01(\x0e25.google.cloud.discoveryengine.v1beta.IndustryVertical\x12O\n\rcommon_config\x18\x0f \x01(\x0b28.google.cloud.discoveryengine.v1beta.Engine.CommonConfig\x12\x1e\n\x11disable_analytics\x18\x1a \x01(\x08B\x03\xe0A\x01\x1a\xa4\x01\n\x12SearchEngineConfig\x12D\n\x0bsearch_tier\x18\x01 \x01(\x0e2/.google.cloud.discoveryengine.v1beta.SearchTier\x12H\n\x0esearch_add_ons\x18\x02 \x03(\x0e20.google.cloud.discoveryengine.v1beta.SearchAddOn\x1a\x97\x02\n\x10ChatEngineConfig\x12o\n\x15agent_creation_config\x18\x01 \x01(\x0b2P.google.cloud.discoveryengine.v1beta.Engine.ChatEngineConfig.AgentCreationConfig\x12 \n\x18dialogflow_agent_to_link\x18\x02 \x01(\t\x1ap\n\x13AgentCreationConfig\x12\x10\n\x08business\x18\x01 \x01(\t\x12\x1d\n\x15default_language_code\x18\x02 \x01(\t\x12\x16\n\ttime_zone\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08location\x18\x04 \x01(\t\x1a$\n\x0cCommonConfig\x12\x14\n\x0ccompany_name\x18\x01 \x01(\t\x1a.\n\x12ChatEngineMetadata\x12\x18\n\x10dialogflow_agent\x18\x01 \x01(\t:}\xeaAz\n%discoveryengine.googleapis.com/Engine\x12Qprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}B\x0f\n\rengine_configB\x11\n\x0fengine_metadataB\x92\x02\n\'com.google.cloud.discoveryengine.v1betaB\x0bEngineProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x0bEngineProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_ENGINE']._serialized_start = 233
    _globals['_ENGINE']._serialized_end = 1680
    _globals['_ENGINE_SEARCHENGINECONFIG']._serialized_start = 985
    _globals['_ENGINE_SEARCHENGINECONFIG']._serialized_end = 1149
    _globals['_ENGINE_CHATENGINECONFIG']._serialized_start = 1152
    _globals['_ENGINE_CHATENGINECONFIG']._serialized_end = 1431
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG']._serialized_start = 1319
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG']._serialized_end = 1431
    _globals['_ENGINE_COMMONCONFIG']._serialized_start = 1433
    _globals['_ENGINE_COMMONCONFIG']._serialized_end = 1469
    _globals['_ENGINE_CHATENGINEMETADATA']._serialized_start = 1471
    _globals['_ENGINE_CHATENGINEMETADATA']._serialized_end = 1517