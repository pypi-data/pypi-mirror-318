"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1alpha1/lva.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/visionai/v1alpha1/lva.proto\x12\x1egoogle.cloud.visionai.v1alpha1"M\n\x0eAttributeValue\x12\x0b\n\x01i\x18\x01 \x01(\x03H\x00\x12\x0b\n\x01f\x18\x02 \x01(\x02H\x00\x12\x0b\n\x01b\x18\x03 \x01(\x08H\x00\x12\x0b\n\x01s\x18\x04 \x01(\x0cH\x00B\x07\n\x05value"\xf2\x04\n\x12AnalyzerDefinition\x12\x10\n\x08analyzer\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12N\n\x06inputs\x18\x03 \x03(\x0b2>.google.cloud.visionai.v1alpha1.AnalyzerDefinition.StreamInput\x12L\n\x05attrs\x18\x04 \x03(\x0b2=.google.cloud.visionai.v1alpha1.AnalyzerDefinition.AttrsEntry\x12V\n\rdebug_options\x18\x05 \x01(\x0b2?.google.cloud.visionai.v1alpha1.AnalyzerDefinition.DebugOptions\x1a\x1c\n\x0bStreamInput\x12\r\n\x05input\x18\x01 \x01(\t\x1a\xc5\x01\n\x0cDebugOptions\x12x\n\x15environment_variables\x18\x01 \x03(\x0b2Y.google.cloud.visionai.v1alpha1.AnalyzerDefinition.DebugOptions.EnvironmentVariablesEntry\x1a;\n\x19EnvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a\\\n\nAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b2..google.cloud.visionai.v1alpha1.AttributeValue:\x028\x01"[\n\x12AnalysisDefinition\x12E\n\tanalyzers\x18\x01 \x03(\x0b22.google.cloud.visionai.v1alpha1.AnalyzerDefinitionB\xd6\x01\n"com.google.cloud.visionai.v1alpha1B\x08LvaProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1alpha1.lva_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.visionai.v1alpha1B\x08LvaProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1'
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY']._loaded_options = None
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_ANALYZERDEFINITION_ATTRSENTRY']._loaded_options = None
    _globals['_ANALYZERDEFINITION_ATTRSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTRIBUTEVALUE']._serialized_start = 76
    _globals['_ATTRIBUTEVALUE']._serialized_end = 153
    _globals['_ANALYZERDEFINITION']._serialized_start = 156
    _globals['_ANALYZERDEFINITION']._serialized_end = 782
    _globals['_ANALYZERDEFINITION_STREAMINPUT']._serialized_start = 460
    _globals['_ANALYZERDEFINITION_STREAMINPUT']._serialized_end = 488
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS']._serialized_start = 491
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS']._serialized_end = 688
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY']._serialized_start = 629
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY']._serialized_end = 688
    _globals['_ANALYZERDEFINITION_ATTRSENTRY']._serialized_start = 690
    _globals['_ANALYZERDEFINITION_ATTRSENTRY']._serialized_end = 782
    _globals['_ANALYSISDEFINITION']._serialized_start = 784
    _globals['_ANALYSISDEFINITION']._serialized_end = 875