"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1/lva.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/cloud/visionai/v1/lva.proto\x12\x18google.cloud.visionai.v1"\xca\x04\n\x12OperatorDefinition\x12\x10\n\x08operator\x18\x01 \x01(\t\x12S\n\ninput_args\x18\x02 \x03(\x0b2?.google.cloud.visionai.v1.OperatorDefinition.ArgumentDefinition\x12T\n\x0boutput_args\x18\x03 \x03(\x0b2?.google.cloud.visionai.v1.OperatorDefinition.ArgumentDefinition\x12T\n\nattributes\x18\x04 \x03(\x0b2@.google.cloud.visionai.v1.OperatorDefinition.AttributeDefinition\x12B\n\tresources\x18\x05 \x01(\x0b2/.google.cloud.visionai.v1.ResourceSpecification\x12\x19\n\x11short_description\x18\x06 \x01(\t\x12\x13\n\x0bdescription\x18\x07 \x01(\t\x1a4\n\x12ArgumentDefinition\x12\x10\n\x08argument\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x1aw\n\x13AttributeDefinition\x12\x11\n\tattribute\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12?\n\rdefault_value\x18\x03 \x01(\x0b2(.google.cloud.visionai.v1.AttributeValue"\x88\x01\n\x15ResourceSpecification\x12\x0b\n\x03cpu\x18\x01 \x01(\t\x12\x12\n\ncpu_limits\x18\x05 \x01(\t\x12\x0e\n\x06memory\x18\x02 \x01(\t\x12\x15\n\rmemory_limits\x18\x06 \x01(\t\x12\x0c\n\x04gpus\x18\x03 \x01(\x05\x12\x19\n\x11latency_budget_ms\x18\x04 \x01(\x05"M\n\x0eAttributeValue\x12\x0b\n\x01i\x18\x01 \x01(\x03H\x00\x12\x0b\n\x01f\x18\x02 \x01(\x02H\x00\x12\x0b\n\x01b\x18\x03 \x01(\x08H\x00\x12\x0b\n\x01s\x18\x04 \x01(\x0cH\x00B\x07\n\x05value"\xdb\x05\n\x12AnalyzerDefinition\x12\x10\n\x08analyzer\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12H\n\x06inputs\x18\x03 \x03(\x0b28.google.cloud.visionai.v1.AnalyzerDefinition.StreamInput\x12F\n\x05attrs\x18\x04 \x03(\x0b27.google.cloud.visionai.v1.AnalyzerDefinition.AttrsEntry\x12P\n\rdebug_options\x18\x05 \x01(\x0b29.google.cloud.visionai.v1.AnalyzerDefinition.DebugOptions\x12T\n\x0foperator_option\x18\x06 \x01(\x0b2;.google.cloud.visionai.v1.AnalyzerDefinition.OperatorOption\x1a\x1c\n\x0bStreamInput\x12\r\n\x05input\x18\x01 \x01(\t\x1a\xbf\x01\n\x0cDebugOptions\x12r\n\x15environment_variables\x18\x01 \x03(\x0b2S.google.cloud.visionai.v1.AnalyzerDefinition.DebugOptions.EnvironmentVariablesEntry\x1a;\n\x19EnvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a/\n\x0eOperatorOption\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x10\n\x08registry\x18\x02 \x01(\t\x1aV\n\nAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x127\n\x05value\x18\x02 \x01(\x0b2(.google.cloud.visionai.v1.AttributeValue:\x028\x01"U\n\x12AnalysisDefinition\x12?\n\tanalyzers\x18\x01 \x03(\x0b2,.google.cloud.visionai.v1.AnalyzerDefinition"\xbc\x01\n\tRunStatus\x128\n\x05state\x18\x01 \x01(\x0e2).google.cloud.visionai.v1.RunStatus.State\x12\x0e\n\x06reason\x18\x02 \x01(\t"e\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0b\n\x07PENDING\x10\x05*=\n\x07RunMode\x12\x18\n\x14RUN_MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04LIVE\x10\x01\x12\x0e\n\nSUBMISSION\x10\x02B\xb8\x01\n\x1ccom.google.cloud.visionai.v1B\x08LvaProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1.lva_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.visionai.v1B\x08LvaProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1'
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY']._loaded_options = None
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_ANALYZERDEFINITION_ATTRSENTRY']._loaded_options = None
    _globals['_ANALYZERDEFINITION_ATTRSENTRY']._serialized_options = b'8\x01'
    _globals['_RUNMODE']._serialized_start = 1883
    _globals['_RUNMODE']._serialized_end = 1944
    _globals['_OPERATORDEFINITION']._serialized_start = 65
    _globals['_OPERATORDEFINITION']._serialized_end = 651
    _globals['_OPERATORDEFINITION_ARGUMENTDEFINITION']._serialized_start = 478
    _globals['_OPERATORDEFINITION_ARGUMENTDEFINITION']._serialized_end = 530
    _globals['_OPERATORDEFINITION_ATTRIBUTEDEFINITION']._serialized_start = 532
    _globals['_OPERATORDEFINITION_ATTRIBUTEDEFINITION']._serialized_end = 651
    _globals['_RESOURCESPECIFICATION']._serialized_start = 654
    _globals['_RESOURCESPECIFICATION']._serialized_end = 790
    _globals['_ATTRIBUTEVALUE']._serialized_start = 792
    _globals['_ATTRIBUTEVALUE']._serialized_end = 869
    _globals['_ANALYZERDEFINITION']._serialized_start = 872
    _globals['_ANALYZERDEFINITION']._serialized_end = 1603
    _globals['_ANALYZERDEFINITION_STREAMINPUT']._serialized_start = 1244
    _globals['_ANALYZERDEFINITION_STREAMINPUT']._serialized_end = 1272
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS']._serialized_start = 1275
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS']._serialized_end = 1466
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY']._serialized_start = 1407
    _globals['_ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY']._serialized_end = 1466
    _globals['_ANALYZERDEFINITION_OPERATOROPTION']._serialized_start = 1468
    _globals['_ANALYZERDEFINITION_OPERATOROPTION']._serialized_end = 1515
    _globals['_ANALYZERDEFINITION_ATTRSENTRY']._serialized_start = 1517
    _globals['_ANALYZERDEFINITION_ATTRSENTRY']._serialized_end = 1603
    _globals['_ANALYSISDEFINITION']._serialized_start = 1605
    _globals['_ANALYSISDEFINITION']._serialized_end = 1690
    _globals['_RUNSTATUS']._serialized_start = 1693
    _globals['_RUNSTATUS']._serialized_end = 1881
    _globals['_RUNSTATUS_STATE']._serialized_start = 1780
    _globals['_RUNSTATUS_STATE']._serialized_end = 1881