"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/document_processing_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/cloud/discoveryengine/v1alpha/document_processing_config.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd4\x0c\n\x18DocumentProcessingConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12f\n\x0fchunking_config\x18\x03 \x01(\x0b2M.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig.ChunkingConfig\x12l\n\x16default_parsing_config\x18\x04 \x01(\x0b2L.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig.ParsingConfig\x12|\n\x18parsing_config_overrides\x18\x05 \x03(\x0b2Z.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig.ParsingConfigOverridesEntry\x1a\x84\x02\n\x0eChunkingConfig\x12\x8f\x01\n\x1clayout_based_chunking_config\x18\x01 \x01(\x0b2g.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig.ChunkingConfig.LayoutBasedChunkingConfigH\x00\x1aR\n\x19LayoutBasedChunkingConfig\x12\x12\n\nchunk_size\x18\x01 \x01(\x05\x12!\n\x19include_ancestor_headings\x18\x02 \x01(\x08B\x0c\n\nchunk_mode\x1a\xb3\x04\n\rParsingConfig\x12\x83\x01\n\x16digital_parsing_config\x18\x01 \x01(\x0b2a.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig.ParsingConfig.DigitalParsingConfigH\x00\x12{\n\x12ocr_parsing_config\x18\x02 \x01(\x0b2].google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig.ParsingConfig.OcrParsingConfigH\x00\x12\x81\x01\n\x15layout_parsing_config\x18\x03 \x01(\x0b2`.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig.ParsingConfig.LayoutParsingConfigH\x00\x1a\x16\n\x14DigitalParsingConfig\x1aS\n\x10OcrParsingConfig\x12&\n\x1aenhanced_document_elements\x18\x01 \x03(\tB\x02\x18\x01\x12\x17\n\x0fuse_native_text\x18\x02 \x01(\x08\x1a\x15\n\x13LayoutParsingConfigB\x17\n\x15type_dedicated_config\x1a\x8b\x01\n\x1bParsingConfigOverridesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12[\n\x05value\x18\x02 \x01(\x0b2L.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig.ParsingConfig:\x028\x01:\x8a\x02\xeaA\x86\x02\n7discoveryengine.googleapis.com/DocumentProcessingConfig\x12Xprojects/{project}/locations/{location}/dataStores/{data_store}/documentProcessingConfig\x12qprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/documentProcessingConfigB\xa9\x02\n(com.google.cloud.discoveryengine.v1alphaB\x1dDocumentProcessingConfigProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.document_processing_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x1dDocumentProcessingConfigProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_OCRPARSINGCONFIG'].fields_by_name['enhanced_document_elements']._loaded_options = None
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_OCRPARSINGCONFIG'].fields_by_name['enhanced_document_elements']._serialized_options = b'\x18\x01'
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIGOVERRIDESENTRY']._loaded_options = None
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIGOVERRIDESENTRY']._serialized_options = b'8\x01'
    _globals['_DOCUMENTPROCESSINGCONFIG']._loaded_options = None
    _globals['_DOCUMENTPROCESSINGCONFIG']._serialized_options = b'\xeaA\x86\x02\n7discoveryengine.googleapis.com/DocumentProcessingConfig\x12Xprojects/{project}/locations/{location}/dataStores/{data_store}/documentProcessingConfig\x12qprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/documentProcessingConfig'
    _globals['_DOCUMENTPROCESSINGCONFIG']._serialized_start = 172
    _globals['_DOCUMENTPROCESSINGCONFIG']._serialized_end = 1792
    _globals['_DOCUMENTPROCESSINGCONFIG_CHUNKINGCONFIG']._serialized_start = 555
    _globals['_DOCUMENTPROCESSINGCONFIG_CHUNKINGCONFIG']._serialized_end = 815
    _globals['_DOCUMENTPROCESSINGCONFIG_CHUNKINGCONFIG_LAYOUTBASEDCHUNKINGCONFIG']._serialized_start = 719
    _globals['_DOCUMENTPROCESSINGCONFIG_CHUNKINGCONFIG_LAYOUTBASEDCHUNKINGCONFIG']._serialized_end = 801
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG']._serialized_start = 818
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG']._serialized_end = 1381
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_DIGITALPARSINGCONFIG']._serialized_start = 1226
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_DIGITALPARSINGCONFIG']._serialized_end = 1248
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_OCRPARSINGCONFIG']._serialized_start = 1250
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_OCRPARSINGCONFIG']._serialized_end = 1333
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_LAYOUTPARSINGCONFIG']._serialized_start = 1335
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIG_LAYOUTPARSINGCONFIG']._serialized_end = 1356
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIGOVERRIDESENTRY']._serialized_start = 1384
    _globals['_DOCUMENTPROCESSINGCONFIG_PARSINGCONFIGOVERRIDESENTRY']._serialized_end = 1523