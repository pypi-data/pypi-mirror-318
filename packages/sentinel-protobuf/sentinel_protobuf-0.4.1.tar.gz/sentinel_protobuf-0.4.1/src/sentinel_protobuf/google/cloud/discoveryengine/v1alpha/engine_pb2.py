"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/engine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/discoveryengine/v1alpha/engine.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/discoveryengine/v1alpha/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf4\x15\n\x06Engine\x12m\n\x18similar_documents_config\x18\t \x01(\x0b2I.google.cloud.discoveryengine.v1alpha.Engine.SimilarDocumentsEngineConfigH\x00\x12[\n\x12chat_engine_config\x18\x0b \x01(\x0b2=.google.cloud.discoveryengine.v1alpha.Engine.ChatEngineConfigH\x00\x12_\n\x14search_engine_config\x18\r \x01(\x0b2?.google.cloud.discoveryengine.v1alpha.Engine.SearchEngineConfigH\x00\x12z\n"media_recommendation_engine_config\x18\x0e \x01(\x0b2L.google.cloud.discoveryengine.v1alpha.Engine.MediaRecommendationEngineConfigH\x00\x12k\n\x17recommendation_metadata\x18\n \x01(\x0b2C.google.cloud.discoveryengine.v1alpha.Engine.RecommendationMetadataB\x03\xe0A\x03H\x01\x12d\n\x14chat_engine_metadata\x18\x0c \x01(\x0b2?.google.cloud.discoveryengine.v1alpha.Engine.ChatEngineMetadataB\x03\xe0A\x03H\x01\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x16\n\x0edata_store_ids\x18\x05 \x03(\t\x12N\n\rsolution_type\x18\x06 \x01(\x0e22.google.cloud.discoveryengine.v1alpha.SolutionTypeB\x03\xe0A\x02\x12Q\n\x11industry_vertical\x18\x10 \x01(\x0e26.google.cloud.discoveryengine.v1alpha.IndustryVertical\x12P\n\rcommon_config\x18\x0f \x01(\x0b29.google.cloud.discoveryengine.v1alpha.Engine.CommonConfig\x1a\xa6\x01\n\x12SearchEngineConfig\x12E\n\x0bsearch_tier\x18\x01 \x01(\x0e20.google.cloud.discoveryengine.v1alpha.SearchTier\x12I\n\x0esearch_add_ons\x18\x02 \x03(\x0e21.google.cloud.discoveryengine.v1alpha.SearchAddOn\x1a\x1e\n\x1cSimilarDocumentsEngineConfig\x1a\x86\x04\n\x1fMediaRecommendationEngineConfig\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x16optimization_objective\x18\x02 \x01(\t\x12\x8f\x01\n\x1doptimization_objective_config\x18\x03 \x01(\x0b2h.google.cloud.discoveryengine.v1alpha.Engine.MediaRecommendationEngineConfig.OptimizationObjectiveConfig\x12r\n\x0etraining_state\x18\x04 \x01(\x0e2Z.google.cloud.discoveryengine.v1alpha.Engine.MediaRecommendationEngineConfig.TrainingState\x1a_\n\x1bOptimizationObjectiveConfig\x12\x19\n\x0ctarget_field\x18\x01 \x01(\tB\x03\xe0A\x02\x12%\n\x18target_field_value_float\x18\x02 \x01(\x02B\x03\xe0A\x02"I\n\rTrainingState\x12\x1e\n\x1aTRAINING_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06PAUSED\x10\x01\x12\x0c\n\x08TRAINING\x10\x02\x1a\x98\x02\n\x10ChatEngineConfig\x12p\n\x15agent_creation_config\x18\x01 \x01(\x0b2Q.google.cloud.discoveryengine.v1alpha.Engine.ChatEngineConfig.AgentCreationConfig\x12 \n\x18dialogflow_agent_to_link\x18\x02 \x01(\t\x1ap\n\x13AgentCreationConfig\x12\x10\n\x08business\x18\x01 \x01(\t\x12\x1d\n\x15default_language_code\x18\x02 \x01(\t\x12\x16\n\ttime_zone\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08location\x18\x04 \x01(\t\x1a$\n\x0cCommonConfig\x12\x14\n\x0ccompany_name\x18\x01 \x01(\t\x1a\xe0\x03\n\x16RecommendationMetadata\x12l\n\rserving_state\x18\x01 \x01(\x0e2P.google.cloud.discoveryengine.v1alpha.Engine.RecommendationMetadata.ServingStateB\x03\xe0A\x03\x12f\n\ndata_state\x18\x02 \x01(\x0e2M.google.cloud.discoveryengine.v1alpha.Engine.RecommendationMetadata.DataStateB\x03\xe0A\x03\x127\n\x0elast_tune_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1d\n\x10tuning_operation\x18\x04 \x01(\tB\x03\xe0A\x03"R\n\x0cServingState\x12\x1d\n\x19SERVING_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\t\n\x05TUNED\x10\x03"D\n\tDataState\x12\x1a\n\x16DATA_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DATA_OK\x10\x01\x12\x0e\n\nDATA_ERROR\x10\x02\x1a.\n\x12ChatEngineMetadata\x12\x18\n\x10dialogflow_agent\x18\x01 \x01(\t:}\xeaAz\n%discoveryengine.googleapis.com/Engine\x12Qprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}B\x0f\n\rengine_configB\x11\n\x0fengine_metadataB\x97\x02\n(com.google.cloud.discoveryengine.v1alphaB\x0bEngineProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x0bEngineProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG'].fields_by_name['target_field']._loaded_options = None
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG'].fields_by_name['target_field']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG'].fields_by_name['target_field_value_float']._loaded_options = None
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG'].fields_by_name['target_field_value_float']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG'].fields_by_name['type']._loaded_options = None
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG'].fields_by_name['time_zone']._loaded_options = None
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE_RECOMMENDATIONMETADATA'].fields_by_name['serving_state']._loaded_options = None
    _globals['_ENGINE_RECOMMENDATIONMETADATA'].fields_by_name['serving_state']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE_RECOMMENDATIONMETADATA'].fields_by_name['data_state']._loaded_options = None
    _globals['_ENGINE_RECOMMENDATIONMETADATA'].fields_by_name['data_state']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE_RECOMMENDATIONMETADATA'].fields_by_name['last_tune_time']._loaded_options = None
    _globals['_ENGINE_RECOMMENDATIONMETADATA'].fields_by_name['last_tune_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE_RECOMMENDATIONMETADATA'].fields_by_name['tuning_operation']._loaded_options = None
    _globals['_ENGINE_RECOMMENDATIONMETADATA'].fields_by_name['tuning_operation']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE'].fields_by_name['recommendation_metadata']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['recommendation_metadata']._serialized_options = b'\xe0A\x03'
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
    _globals['_ENGINE']._loaded_options = None
    _globals['_ENGINE']._serialized_options = b'\xeaAz\n%discoveryengine.googleapis.com/Engine\x12Qprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}'
    _globals['_ENGINE']._serialized_start = 236
    _globals['_ENGINE']._serialized_end = 3040
    _globals['_ENGINE_SEARCHENGINECONFIG']._serialized_start = 1306
    _globals['_ENGINE_SEARCHENGINECONFIG']._serialized_end = 1472
    _globals['_ENGINE_SIMILARDOCUMENTSENGINECONFIG']._serialized_start = 1474
    _globals['_ENGINE_SIMILARDOCUMENTSENGINECONFIG']._serialized_end = 1504
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG']._serialized_start = 1507
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG']._serialized_end = 2025
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG']._serialized_start = 1855
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG']._serialized_end = 1950
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_TRAININGSTATE']._serialized_start = 1952
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_TRAININGSTATE']._serialized_end = 2025
    _globals['_ENGINE_CHATENGINECONFIG']._serialized_start = 2028
    _globals['_ENGINE_CHATENGINECONFIG']._serialized_end = 2308
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG']._serialized_start = 2196
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG']._serialized_end = 2308
    _globals['_ENGINE_COMMONCONFIG']._serialized_start = 2310
    _globals['_ENGINE_COMMONCONFIG']._serialized_end = 2346
    _globals['_ENGINE_RECOMMENDATIONMETADATA']._serialized_start = 2349
    _globals['_ENGINE_RECOMMENDATIONMETADATA']._serialized_end = 2829
    _globals['_ENGINE_RECOMMENDATIONMETADATA_SERVINGSTATE']._serialized_start = 2677
    _globals['_ENGINE_RECOMMENDATIONMETADATA_SERVINGSTATE']._serialized_end = 2759
    _globals['_ENGINE_RECOMMENDATIONMETADATA_DATASTATE']._serialized_start = 2761
    _globals['_ENGINE_RECOMMENDATIONMETADATA_DATASTATE']._serialized_end = 2829
    _globals['_ENGINE_CHATENGINEMETADATA']._serialized_start = 2831
    _globals['_ENGINE_CHATENGINEMETADATA']._serialized_end = 2877