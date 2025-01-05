"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1/processor.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.documentai.v1 import document_schema_pb2 as google_dot_cloud_dot_documentai_dot_v1_dot_document__schema__pb2
from .....google.cloud.documentai.v1 import evaluation_pb2 as google_dot_cloud_dot_documentai_dot_v1_dot_evaluation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/documentai/v1/processor.proto\x12\x1agoogle.cloud.documentai.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/documentai/v1/document_schema.proto\x1a+google/cloud/documentai/v1/evaluation.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8b\x0f\n\x10ProcessorVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12C\n\x0fdocument_schema\x18\x0c \x01(\x0b2*.google.cloud.documentai.v1.DocumentSchema\x12F\n\x05state\x18\x06 \x01(\x0e22.google.cloud.documentai.v1.ProcessorVersion.StateB\x03\xe0A\x03\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12J\n\x11latest_evaluation\x18\x08 \x01(\x0b2/.google.cloud.documentai.v1.EvaluationReference\x12\x14\n\x0ckms_key_name\x18\t \x01(\t\x12\x1c\n\x14kms_key_version_name\x18\n \x01(\t\x12\x1b\n\x0egoogle_managed\x18\x0b \x01(\x08B\x03\xe0A\x03\x12V\n\x10deprecation_info\x18\r \x01(\x0b2<.google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo\x12O\n\nmodel_type\x18\x0f \x01(\x0e26.google.cloud.documentai.v1.ProcessorVersion.ModelTypeB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x10 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x11 \x01(\x08B\x03\xe0A\x03\x12[\n\x11gen_ai_model_info\x18\x12 \x01(\x0b2;.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfoB\x03\xe0A\x03\x1a\x9f\x01\n\x0fDeprecationInfo\x124\n\x10deprecation_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12V\n\x1dreplacement_processor_version\x18\x02 \x01(\tB/\xfaA,\n*documentai.googleapis.com/ProcessorVersion\x1a\x88\x05\n\x0eGenAiModelInfo\x12|\n\x1cfoundation_gen_ai_model_info\x18\x01 \x01(\x0b2T.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo.FoundationGenAiModelInfoH\x00\x12t\n\x18custom_gen_ai_model_info\x18\x02 \x01(\x0b2P.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfoH\x00\x1a[\n\x18FoundationGenAiModelInfo\x12\x1a\n\x12finetuning_allowed\x18\x01 \x01(\x08\x12#\n\x1bmin_train_labeled_documents\x18\x02 \x01(\x05\x1a\x96\x02\n\x14CustomGenAiModelInfo\x12{\n\x11custom_model_type\x18\x01 \x01(\x0e2`.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType\x12!\n\x19base_processor_version_id\x18\x02 \x01(\t"^\n\x0fCustomModelType\x12!\n\x1dCUSTOM_MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14VERSIONED_FOUNDATION\x10\x01\x12\x0e\n\nFINE_TUNED\x10\x02B\x0c\n\nmodel_info"\x93\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DEPLOYED\x10\x01\x12\r\n\tDEPLOYING\x10\x02\x12\x0e\n\nUNDEPLOYED\x10\x03\x12\x0f\n\x0bUNDEPLOYING\x10\x04\x12\x0c\n\x08CREATING\x10\x05\x12\x0c\n\x08DELETING\x10\x06\x12\n\n\x06FAILED\x10\x07\x12\r\n\tIMPORTING\x10\x08"Y\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15MODEL_TYPE_GENERATIVE\x10\x01\x12\x15\n\x11MODEL_TYPE_CUSTOM\x10\x02:\x96\x01\xeaA\x92\x01\n*documentai.googleapis.com/ProcessorVersion\x12dprojects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}"r\n\x15ProcessorVersionAlias\x12\r\n\x05alias\x18\x01 \x01(\t\x12J\n\x11processor_version\x18\x02 \x01(\tB/\xfaA,\n*documentai.googleapis.com/ProcessorVersion"\xc0\x05\n\tProcessor\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x05\xe0A\x03\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12?\n\x05state\x18\x04 \x01(\x0e2+.google.cloud.documentai.v1.Processor.StateB\x03\xe0A\x03\x12R\n\x19default_processor_version\x18\t \x01(\tB/\xfaA,\n*documentai.googleapis.com/ProcessorVersion\x12Y\n\x19processor_version_aliases\x18\n \x03(\x0b21.google.cloud.documentai.v1.ProcessorVersionAliasB\x03\xe0A\x03\x12 \n\x10process_endpoint\x18\x06 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0ckms_key_name\x18\x08 \x01(\t\x12\x1a\n\rsatisfies_pzs\x18\x0c \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\r \x01(\x08B\x03\xe0A\x03"~\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x12\x0c\n\x08ENABLING\x10\x03\x12\r\n\tDISABLING\x10\x04\x12\x0c\n\x08CREATING\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\x0c\n\x08DELETING\x10\x07:h\xeaAe\n#documentai.googleapis.com/Processor\x12>projects/{project}/locations/{location}/processors/{processor}B\xd1\x01\n\x1ecom.google.cloud.documentai.v1B\x13DocumentAiProcessorP\x01Z>cloud.google.com/go/documentai/apiv1/documentaipb;documentaipb\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1.processor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.documentai.v1B\x13DocumentAiProcessorP\x01Z>cloud.google.com/go/documentai/apiv1/documentaipb;documentaipb\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1'
    _globals['_PROCESSORVERSION_DEPRECATIONINFO'].fields_by_name['replacement_processor_version']._loaded_options = None
    _globals['_PROCESSORVERSION_DEPRECATIONINFO'].fields_by_name['replacement_processor_version']._serialized_options = b'\xfaA,\n*documentai.googleapis.com/ProcessorVersion'
    _globals['_PROCESSORVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_PROCESSORVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PROCESSORVERSION'].fields_by_name['state']._loaded_options = None
    _globals['_PROCESSORVERSION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSORVERSION'].fields_by_name['google_managed']._loaded_options = None
    _globals['_PROCESSORVERSION'].fields_by_name['google_managed']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSORVERSION'].fields_by_name['model_type']._loaded_options = None
    _globals['_PROCESSORVERSION'].fields_by_name['model_type']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSORVERSION'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_PROCESSORVERSION'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSORVERSION'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_PROCESSORVERSION'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSORVERSION'].fields_by_name['gen_ai_model_info']._loaded_options = None
    _globals['_PROCESSORVERSION'].fields_by_name['gen_ai_model_info']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSORVERSION']._loaded_options = None
    _globals['_PROCESSORVERSION']._serialized_options = b'\xeaA\x92\x01\n*documentai.googleapis.com/ProcessorVersion\x12dprojects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}'
    _globals['_PROCESSORVERSIONALIAS'].fields_by_name['processor_version']._loaded_options = None
    _globals['_PROCESSORVERSIONALIAS'].fields_by_name['processor_version']._serialized_options = b'\xfaA,\n*documentai.googleapis.com/ProcessorVersion'
    _globals['_PROCESSOR'].fields_by_name['name']._loaded_options = None
    _globals['_PROCESSOR'].fields_by_name['name']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_PROCESSOR'].fields_by_name['state']._loaded_options = None
    _globals['_PROCESSOR'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSOR'].fields_by_name['default_processor_version']._loaded_options = None
    _globals['_PROCESSOR'].fields_by_name['default_processor_version']._serialized_options = b'\xfaA,\n*documentai.googleapis.com/ProcessorVersion'
    _globals['_PROCESSOR'].fields_by_name['processor_version_aliases']._loaded_options = None
    _globals['_PROCESSOR'].fields_by_name['processor_version_aliases']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSOR'].fields_by_name['process_endpoint']._loaded_options = None
    _globals['_PROCESSOR'].fields_by_name['process_endpoint']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_PROCESSOR'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_PROCESSOR'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSOR'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_PROCESSOR'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSOR']._loaded_options = None
    _globals['_PROCESSOR']._serialized_options = b'\xeaAe\n#documentai.googleapis.com/Processor\x12>projects/{project}/locations/{location}/processors/{processor}'
    _globals['_PROCESSORVERSION']._serialized_start = 263
    _globals['_PROCESSORVERSION']._serialized_end = 2194
    _globals['_PROCESSORVERSION_DEPRECATIONINFO']._serialized_start = 990
    _globals['_PROCESSORVERSION_DEPRECATIONINFO']._serialized_end = 1149
    _globals['_PROCESSORVERSION_GENAIMODELINFO']._serialized_start = 1152
    _globals['_PROCESSORVERSION_GENAIMODELINFO']._serialized_end = 1800
    _globals['_PROCESSORVERSION_GENAIMODELINFO_FOUNDATIONGENAIMODELINFO']._serialized_start = 1414
    _globals['_PROCESSORVERSION_GENAIMODELINFO_FOUNDATIONGENAIMODELINFO']._serialized_end = 1505
    _globals['_PROCESSORVERSION_GENAIMODELINFO_CUSTOMGENAIMODELINFO']._serialized_start = 1508
    _globals['_PROCESSORVERSION_GENAIMODELINFO_CUSTOMGENAIMODELINFO']._serialized_end = 1786
    _globals['_PROCESSORVERSION_GENAIMODELINFO_CUSTOMGENAIMODELINFO_CUSTOMMODELTYPE']._serialized_start = 1692
    _globals['_PROCESSORVERSION_GENAIMODELINFO_CUSTOMGENAIMODELINFO_CUSTOMMODELTYPE']._serialized_end = 1786
    _globals['_PROCESSORVERSION_STATE']._serialized_start = 1803
    _globals['_PROCESSORVERSION_STATE']._serialized_end = 1950
    _globals['_PROCESSORVERSION_MODELTYPE']._serialized_start = 1952
    _globals['_PROCESSORVERSION_MODELTYPE']._serialized_end = 2041
    _globals['_PROCESSORVERSIONALIAS']._serialized_start = 2196
    _globals['_PROCESSORVERSIONALIAS']._serialized_end = 2310
    _globals['_PROCESSOR']._serialized_start = 2313
    _globals['_PROCESSOR']._serialized_end = 3017
    _globals['_PROCESSOR_STATE']._serialized_start = 2785
    _globals['_PROCESSOR_STATE']._serialized_end = 2911