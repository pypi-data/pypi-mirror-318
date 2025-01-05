"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/discoveryengine/v1alpha/common.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x19google/api/resource.proto"x\n\x08Interval\x12\x11\n\x07minimum\x18\x01 \x01(\x01H\x00\x12\x1b\n\x11exclusive_minimum\x18\x02 \x01(\x01H\x00\x12\x11\n\x07maximum\x18\x03 \x01(\x01H\x01\x12\x1b\n\x11exclusive_maximum\x18\x04 \x01(\x01H\x01B\x05\n\x03minB\x05\n\x03max"0\n\x0fCustomAttribute\x12\x0c\n\x04text\x18\x01 \x03(\t\x12\x0f\n\x07numbers\x18\x02 \x03(\x01"/\n\x08UserInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nuser_agent\x18\x02 \x01(\t"%\n\x0fEmbeddingConfig\x12\x12\n\nfield_path\x18\x01 \x01(\t"\x1c\n\nDoubleList\x12\x0e\n\x06values\x18\x01 \x03(\x01"y\n\x10GuidedSearchSpec\x12$\n\x1cenable_refinement_attributes\x18\x01 \x01(\x08\x12 \n\x18enable_related_questions\x18\x02 \x01(\x08\x12\x1d\n\x15max_related_questions\x18\x03 \x01(\x05"5\n\x14CustomFineTuningSpec\x12\x1d\n\x15enable_search_adaptor\x18\x01 \x01(\x08"\xaa\x02\n\tIdpConfig\x12I\n\x08idp_type\x18\x01 \x01(\x0e27.google.cloud.discoveryengine.v1alpha.IdpConfig.IdpType\x12^\n\x13external_idp_config\x18\x02 \x01(\x0b2A.google.cloud.discoveryengine.v1alpha.IdpConfig.ExternalIdpConfig\x1a0\n\x11ExternalIdpConfig\x12\x1b\n\x13workforce_pool_name\x18\x01 \x01(\t"@\n\x07IdpType\x12\x18\n\x14IDP_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06GSUITE\x10\x01\x12\x0f\n\x0bTHIRD_PARTY\x10\x02"?\n\tPrincipal\x12\x11\n\x07user_id\x18\x01 \x01(\tH\x00\x12\x12\n\x08group_id\x18\x02 \x01(\tH\x00B\x0b\n\tprincipal*b\n\x10IndustryVertical\x12!\n\x1dINDUSTRY_VERTICAL_UNSPECIFIED\x10\x00\x12\x0b\n\x07GENERIC\x10\x01\x12\t\n\x05MEDIA\x10\x02\x12\x13\n\x0fHEALTHCARE_FHIR\x10\x07*\xa4\x01\n\x0cSolutionType\x12\x1d\n\x19SOLUTION_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1cSOLUTION_TYPE_RECOMMENDATION\x10\x01\x12\x18\n\x14SOLUTION_TYPE_SEARCH\x10\x02\x12\x16\n\x12SOLUTION_TYPE_CHAT\x10\x03\x12!\n\x1dSOLUTION_TYPE_GENERATIVE_CHAT\x10\x04*h\n\rSearchUseCase\x12\x1f\n\x1bSEARCH_USE_CASE_UNSPECIFIED\x10\x00\x12\x1a\n\x16SEARCH_USE_CASE_SEARCH\x10\x01\x12\x1a\n\x16SEARCH_USE_CASE_BROWSE\x10\x02*_\n\nSearchTier\x12\x1b\n\x17SEARCH_TIER_UNSPECIFIED\x10\x00\x12\x18\n\x14SEARCH_TIER_STANDARD\x10\x01\x12\x1a\n\x16SEARCH_TIER_ENTERPRISE\x10\x02*C\n\x0bSearchAddOn\x12\x1d\n\x19SEARCH_ADD_ON_UNSPECIFIED\x10\x00\x12\x15\n\x11SEARCH_ADD_ON_LLM\x10\x01B\xbc\x08\n(com.google.cloud.discoveryengine.v1alphaB\x0bCommonProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alpha\xeaA\xe6\x01\n%discoveryengine.googleapis.com/Branch\x12Qprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}\x12jprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}\xeaAm\n)discoveryengine.googleapis.com/Collection\x12@projects/{project}/locations/{location}/collections/{collection}\xeaAR\n\'discoveryengine.googleapis.com/Location\x12\'projects/{project}/locations/{location}\xeaA}\n.discoveryengine.googleapis.com/GroundingConfig\x12Kprojects/{project}/locations/{location}/groundingConfigs/{grounding_config}\xeaAw\n,discoveryengine.googleapis.com/RankingConfig\x12Gprojects/{project}/locations/{location}/rankingConfigs/{ranking_config}\xeaAy\n#healthcare.googleapis.com/FhirStore\x12Rprojects/{project}/locations/{location}/datasets/{dataset}/fhirStores/{fhir_store}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x0bCommonProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha\xeaA\xe6\x01\n%discoveryengine.googleapis.com/Branch\x12Qprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}\x12jprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}\xeaAm\n)discoveryengine.googleapis.com/Collection\x12@projects/{project}/locations/{location}/collections/{collection}\xeaAR\n'discoveryengine.googleapis.com/Location\x12'projects/{project}/locations/{location}\xeaA}\n.discoveryengine.googleapis.com/GroundingConfig\x12Kprojects/{project}/locations/{location}/groundingConfigs/{grounding_config}\xeaAw\n,discoveryengine.googleapis.com/RankingConfig\x12Gprojects/{project}/locations/{location}/rankingConfigs/{ranking_config}\xeaAy\n#healthcare.googleapis.com/FhirStore\x12Rprojects/{project}/locations/{location}/datasets/{dataset}/fhirStores/{fhir_store}"
    _globals['_INDUSTRYVERTICAL']._serialized_start = 952
    _globals['_INDUSTRYVERTICAL']._serialized_end = 1050
    _globals['_SOLUTIONTYPE']._serialized_start = 1053
    _globals['_SOLUTIONTYPE']._serialized_end = 1217
    _globals['_SEARCHUSECASE']._serialized_start = 1219
    _globals['_SEARCHUSECASE']._serialized_end = 1323
    _globals['_SEARCHTIER']._serialized_start = 1325
    _globals['_SEARCHTIER']._serialized_end = 1420
    _globals['_SEARCHADDON']._serialized_start = 1422
    _globals['_SEARCHADDON']._serialized_end = 1489
    _globals['_INTERVAL']._serialized_start = 118
    _globals['_INTERVAL']._serialized_end = 238
    _globals['_CUSTOMATTRIBUTE']._serialized_start = 240
    _globals['_CUSTOMATTRIBUTE']._serialized_end = 288
    _globals['_USERINFO']._serialized_start = 290
    _globals['_USERINFO']._serialized_end = 337
    _globals['_EMBEDDINGCONFIG']._serialized_start = 339
    _globals['_EMBEDDINGCONFIG']._serialized_end = 376
    _globals['_DOUBLELIST']._serialized_start = 378
    _globals['_DOUBLELIST']._serialized_end = 406
    _globals['_GUIDEDSEARCHSPEC']._serialized_start = 408
    _globals['_GUIDEDSEARCHSPEC']._serialized_end = 529
    _globals['_CUSTOMFINETUNINGSPEC']._serialized_start = 531
    _globals['_CUSTOMFINETUNINGSPEC']._serialized_end = 584
    _globals['_IDPCONFIG']._serialized_start = 587
    _globals['_IDPCONFIG']._serialized_end = 885
    _globals['_IDPCONFIG_EXTERNALIDPCONFIG']._serialized_start = 771
    _globals['_IDPCONFIG_EXTERNALIDPCONFIG']._serialized_end = 819
    _globals['_IDPCONFIG_IDPTYPE']._serialized_start = 821
    _globals['_IDPCONFIG_IDPTYPE']._serialized_end = 885
    _globals['_PRINCIPAL']._serialized_start = 887
    _globals['_PRINCIPAL']._serialized_end = 950