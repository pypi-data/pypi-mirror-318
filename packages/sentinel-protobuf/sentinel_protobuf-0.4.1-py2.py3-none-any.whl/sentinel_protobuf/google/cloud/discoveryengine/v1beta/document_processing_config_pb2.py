"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1beta/document_processing_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/cloud/discoveryengine/v1beta/document_processing_config.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xcc\x0c\n\x18DocumentProcessingConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12e\n\x0fchunking_config\x18\x03 \x01(\x0b2L.google.cloud.discoveryengine.v1beta.DocumentProcessingConfig.ChunkingConfig\x12k\n\x16default_parsing_config\x18\x04 \x01(\x0b2K.google.cloud.discoveryengine.v1beta.DocumentProcessingConfig.ParsingConfig\x12{\n\x18parsing_config_overrides\x18\x05 \x03(\x0b2Y.google.cloud.discoveryengine.v1beta.DocumentProcessingConfig.ParsingConfigOverridesEntry\x1a\x83\x02\n\x0eChunkingConfig\x12\x8e\x01\n\x1clayout_based_chunking_config\x18\x01 \x01(\x0b2f.google.cloud.discoveryengine.v1beta.DocumentProcessingConfig.ChunkingConfig.LayoutBasedChunkingConfigH\x00\x1aR\n\x19LayoutBasedChunkingConfig\x12\x12\n\nchunk_size\x18\x01 \x01(\x05\x12!\n\x19include_ancestor_headings\x18\x02 \x01(\x08B\x0c\n\nchunk_mode\x1a\xb0\x04\n\rParsingConfig\x12\x82\x01\n\x16digital_parsing_config\x18\x01 \x01(\x0b2`.google.cloud.discoveryengine.v1beta.DocumentProcessingConfig.ParsingConfig.DigitalParsingConfigH\x00\x12z\n\x12ocr_parsing_config\x18\x02 \x01(\x0b2\\.google.cloud.discoveryengine.v1beta.DocumentProcessingConfig.ParsingConfig.OcrParsingConfigH\x00\x12\x80\x01\n\x15layout_parsing_config\x18\x03 \x01(\x0b2_.google.cloud.discoveryengine.v1beta.DocumentProcessingConfig.ParsingConfig.LayoutParsingConfigH\x00\x1a\x16\n\x14DigitalParsingConfig\x1aS\n\x10OcrParsingConfig\x12&\n\x1aenhanced_document_elements\x18\x01 \x03(\tB\x02\x18\x01\x12\x17\n\x0fuse_native_text\x18\x02 \x01(\x08\x1a\x15\n\x13LayoutParsingConfigB\x17\n\x15type_dedicated_config\x1a\x8a\x01\n\x1bParsingConfigOverridesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Z\n\x05value\x18\x02 \x01(\x0b2K.google.cloud.discoveryengine.v1beta.DocumentProcessingConfig.ParsingConfig:\x028\x01:\x8a\x02\xeaA\x86\x02\n7discoveryengine.googleapis.com/DocumentProcessingConfig\x12Xprojects/{project}/locations/{location}/dataStores/{data_store}/documentProcessingConfig\x12qprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/documentProcessingConfigB\xa4\x02\n\'com.google.cloud.discoveryengine.v1betaB\x1dDocumentProcessingConfigProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.document_processing_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x1dDocumentProcessingConfigProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_OCRPARSINGCONFIG'].fields_by_name['enhanced_document_elements']._loaded_options = None
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_OCRPARSINGCONFIG'].fields_by_name['enhanced_document_elements']._serialized_options = b'\x18\x01'
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIGOVERRIDESENTRY']._loaded_options = None
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIGOVERRIDESENTRY']._serialized_options = b'8\x01'
    _globals['_DOCUMENTPROCESSINGCONFIG']._loaded_options = None
    _globals['_DOCUMENTPROCESSINGCONFIG']._serialized_options = b'\xeaA\x86\x02\n7discoveryengine.googleapis.com/DocumentProcessingConfig\x12Xprojects/{project}/locations/{location}/dataStores/{data_store}/documentProcessingConfig\x12qprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/documentProcessingConfig'
    _globals['_DOCUMENTPROCESSINGCONFIG']._serialized_start = 170
    _globals['_DOCUMENTPROCESSINGCONFIG']._serialized_end = 1782
    _globals['_DOCUMENTPROCESSINGCONFIG_CHUNKINGCONFIG']._serialized_start = 550
    _globals['_DOCUMENTPROCESSINGCONFIG_CHUNKINGCONFIG']._serialized_end = 809
    _globals['_DOCUMENTPROCESSINGCONFIG_CHUNKINGCONFIG_LAYOUTBASEDCHUNKINGCONFIG']._serialized_start = 713
    _globals['_DOCUMENTPROCESSINGCONFIG_CHUNKINGCONFIG_LAYOUTBASEDCHUNKINGCONFIG']._serialized_end = 795
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG']._serialized_start = 812
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG']._serialized_end = 1372
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_DIGITALPARSINGCONFIG']._serialized_start = 1217
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_DIGITALPARSINGCONFIG']._serialized_end = 1239
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_OCRPARSINGCONFIG']._serialized_start = 1241
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_OCRPARSINGCONFIG']._serialized_end = 1324
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_LAYOUTPARSINGCONFIG']._serialized_start = 1326
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_LAYOUTPARSINGCONFIG']._serialized_end = 1347
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIGOVERRIDESENTRY']._serialized_start = 1375
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIGOVERRIDESENTRY']._serialized_end = 1513