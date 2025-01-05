"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1beta/grounding.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/discoveryengine/v1beta/grounding.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa7\x01\n\x0fGroundingConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02:\x80\x01\xeaA}\n.discoveryengine.googleapis.com/GroundingConfig\x12Kprojects/{project}/locations/{location}/groundingConfigs/{grounding_config}"\xad\x01\n\rGroundingFact\x12\x11\n\tfact_text\x18\x01 \x01(\t\x12V\n\nattributes\x18\x02 \x03(\x0b2B.google.cloud.discoveryengine.v1beta.GroundingFact.AttributesEntry\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xd2\x01\n\tFactChunk\x12\x12\n\nchunk_text\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\r\n\x05index\x18\x04 \x01(\x05\x12[\n\x0fsource_metadata\x18\x03 \x03(\x0b2B.google.cloud.discoveryengine.v1beta.FactChunk.SourceMetadataEntry\x1a5\n\x13SourceMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x95\x02\n\'com.google.cloud.discoveryengine.v1betaB\x0eGroundingProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.grounding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x0eGroundingProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_GROUNDINGCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_GROUNDINGCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_GROUNDINGCONFIG']._loaded_options = None
    _globals['_GROUNDINGCONFIG']._serialized_options = b'\xeaA}\n.discoveryengine.googleapis.com/GroundingConfig\x12Kprojects/{project}/locations/{location}/groundingConfigs/{grounding_config}'
    _globals['_GROUNDINGFACT_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_GROUNDINGFACT_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_FACTCHUNK_SOURCEMETADATAENTRY']._loaded_options = None
    _globals['_FACTCHUNK_SOURCEMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_GROUNDINGCONFIG']._serialized_start = 153
    _globals['_GROUNDINGCONFIG']._serialized_end = 320
    _globals['_GROUNDINGFACT']._serialized_start = 323
    _globals['_GROUNDINGFACT']._serialized_end = 496
    _globals['_GROUNDINGFACT_ATTRIBUTESENTRY']._serialized_start = 447
    _globals['_GROUNDINGFACT_ATTRIBUTESENTRY']._serialized_end = 496
    _globals['_FACTCHUNK']._serialized_start = 499
    _globals['_FACTCHUNK']._serialized_end = 709
    _globals['_FACTCHUNK_SOURCEMETADATAENTRY']._serialized_start = 656
    _globals['_FACTCHUNK_SOURCEMETADATAENTRY']._serialized_end = 709