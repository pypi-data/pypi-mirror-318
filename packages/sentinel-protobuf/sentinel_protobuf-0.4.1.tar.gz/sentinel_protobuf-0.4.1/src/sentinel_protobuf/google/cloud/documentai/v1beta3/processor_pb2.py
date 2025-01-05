"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1beta3/processor.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.documentai.v1beta3 import document_schema_pb2 as google_dot_cloud_dot_documentai_dot_v1beta3_dot_document__schema__pb2
from .....google.cloud.documentai.v1beta3 import evaluation_pb2 as google_dot_cloud_dot_documentai_dot_v1beta3_dot_evaluation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/documentai/v1beta3/processor.proto\x12\x1fgoogle.cloud.documentai.v1beta3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/documentai/v1beta3/document_schema.proto\x1a0google/cloud/documentai/v1beta3/evaluation.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xba\x0f\n\x10ProcessorVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12H\n\x0fdocument_schema\x18\x0c \x01(\x0b2/.google.cloud.documentai.v1beta3.DocumentSchema\x12K\n\x05state\x18\x06 \x01(\x0e27.google.cloud.documentai.v1beta3.ProcessorVersion.StateB\x03\xe0A\x03\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12O\n\x11latest_evaluation\x18\x08 \x01(\x0b24.google.cloud.documentai.v1beta3.EvaluationReference\x12\x14\n\x0ckms_key_name\x18\t \x01(\t\x12\x1c\n\x14kms_key_version_name\x18\n \x01(\t\x12\x1b\n\x0egoogle_managed\x18\x0b \x01(\x08B\x03\xe0A\x03\x12[\n\x10deprecation_info\x18\r \x01(\x0b2A.google.cloud.documentai.v1beta3.ProcessorVersion.DeprecationInfo\x12T\n\nmodel_type\x18\x0f \x01(\x0e2;.google.cloud.documentai.v1beta3.ProcessorVersion.ModelTypeB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x10 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x11 \x01(\x08B\x03\xe0A\x03\x12`\n\x11gen_ai_model_info\x18\x12 \x01(\x0b2@.google.cloud.documentai.v1beta3.ProcessorVersion.GenAiModelInfoB\x03\xe0A\x03\x1a\x9f\x01\n\x0fDeprecationInfo\x124\n\x10deprecation_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12V\n\x1dreplacement_processor_version\x18\x02 \x01(\tB/\xfaA,\n*documentai.googleapis.com/ProcessorVersion\x1a\x99\x05\n\x0eGenAiModelInfo\x12\x81\x01\n\x1cfoundation_gen_ai_model_info\x18\x01 \x01(\x0b2Y.google.cloud.documentai.v1beta3.ProcessorVersion.GenAiModelInfo.FoundationGenAiModelInfoH\x00\x12y\n\x18custom_gen_ai_model_info\x18\x02 \x01(\x0b2U.google.cloud.documentai.v1beta3.ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfoH\x00\x1a[\n\x18FoundationGenAiModelInfo\x12\x1a\n\x12finetuning_allowed\x18\x01 \x01(\x08\x12#\n\x1bmin_train_labeled_documents\x18\x02 \x01(\x05\x1a\x9c\x02\n\x14CustomGenAiModelInfo\x12\x80\x01\n\x11custom_model_type\x18\x01 \x01(\x0e2e.google.cloud.documentai.v1beta3.ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType\x12!\n\x19base_processor_version_id\x18\x02 \x01(\t"^\n\x0fCustomModelType\x12!\n\x1dCUSTOM_MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14VERSIONED_FOUNDATION\x10\x01\x12\x0e\n\nFINE_TUNED\x10\x02B\x0c\n\nmodel_info"\x93\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DEPLOYED\x10\x01\x12\r\n\tDEPLOYING\x10\x02\x12\x0e\n\nUNDEPLOYED\x10\x03\x12\x0f\n\x0bUNDEPLOYING\x10\x04\x12\x0c\n\x08CREATING\x10\x05\x12\x0c\n\x08DELETING\x10\x06\x12\n\n\x06FAILED\x10\x07\x12\r\n\tIMPORTING\x10\x08"Y\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15MODEL_TYPE_GENERATIVE\x10\x01\x12\x15\n\x11MODEL_TYPE_CUSTOM\x10\x02:\x96\x01\xeaA\x92\x01\n*documentai.googleapis.com/ProcessorVersion\x12dprojects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}"r\n\x15ProcessorVersionAlias\x12\r\n\x05alias\x18\x01 \x01(\t\x12J\n\x11processor_version\x18\x02 \x01(\tB/\xfaA,\n*documentai.googleapis.com/ProcessorVersion"\xca\x05\n\tProcessor\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x05\xe0A\x03\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12D\n\x05state\x18\x04 \x01(\x0e20.google.cloud.documentai.v1beta3.Processor.StateB\x03\xe0A\x03\x12R\n\x19default_processor_version\x18\t \x01(\tB/\xfaA,\n*documentai.googleapis.com/ProcessorVersion\x12^\n\x19processor_version_aliases\x18\n \x03(\x0b26.google.cloud.documentai.v1beta3.ProcessorVersionAliasB\x03\xe0A\x03\x12 \n\x10process_endpoint\x18\x06 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0ckms_key_name\x18\x08 \x01(\t\x12\x1a\n\rsatisfies_pzs\x18\x0c \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\r \x01(\x08B\x03\xe0A\x03"~\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x12\x0c\n\x08ENABLING\x10\x03\x12\r\n\tDISABLING\x10\x04\x12\x0c\n\x08CREATING\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\x0c\n\x08DELETING\x10\x07:h\xeaAe\n#documentai.googleapis.com/Processor\x12>projects/{project}/locations/{location}/processors/{processor}B\xea\x01\n#com.google.cloud.documentai.v1beta3B\x13DocumentAiProcessorP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1beta3.processor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.documentai.v1beta3B\x13DocumentAiProcessorP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3'
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
    _globals['_PROCESSORVERSION']._serialized_start = 283
    _globals['_PROCESSORVERSION']._serialized_end = 2261
    _globals['_PROCESSORVERSION_DEPRECATIONINFO']._serialized_start = 1040
    _globals['_PROCESSORVERSION_DEPRECATIONINFO']._serialized_end = 1199
    _globals['_PROCESSORVERSION_GENAIMODELINFO']._serialized_start = 1202
    _globals['_PROCESSORVERSION_GENAIMODELINFO']._serialized_end = 1867
    _globals['_PROCESSORVERSION_GENAIMODELINFO_FOUNDATIONGENAIMODELINFO']._serialized_start = 1475
    _globals['_PROCESSORVERSION_GENAIMODELINFO_FOUNDATIONGENAIMODELINFO']._serialized_end = 1566
    _globals['_PROCESSORVERSION_GENAIMODELINFO_CUSTOMGENAIMODELINFO']._serialized_start = 1569
    _globals['_PROCESSORVERSION_GENAIMODELINFO_CUSTOMGENAIMODELINFO']._serialized_end = 1853
    _globals['_PROCESSORVERSION_GENAIMODELINFO_CUSTOMGENAIMODELINFO_CUSTOMMODELTYPE']._serialized_start = 1759
    _globals['_PROCESSORVERSION_GENAIMODELINFO_CUSTOMGENAIMODELINFO_CUSTOMMODELTYPE']._serialized_end = 1853
    _globals['_PROCESSORVERSION_STATE']._serialized_start = 1870
    _globals['_PROCESSORVERSION_STATE']._serialized_end = 2017
    _globals['_PROCESSORVERSION_MODELTYPE']._serialized_start = 2019
    _globals['_PROCESSORVERSION_MODELTYPE']._serialized_end = 2108
    _globals['_PROCESSORVERSIONALIAS']._serialized_start = 2263
    _globals['_PROCESSORVERSIONALIAS']._serialized_end = 2377
    _globals['_PROCESSOR']._serialized_start = 2380
    _globals['_PROCESSOR']._serialized_end = 3094
    _globals['_PROCESSOR_STATE']._serialized_start = 2862
    _globals['_PROCESSOR_STATE']._serialized_end = 2988