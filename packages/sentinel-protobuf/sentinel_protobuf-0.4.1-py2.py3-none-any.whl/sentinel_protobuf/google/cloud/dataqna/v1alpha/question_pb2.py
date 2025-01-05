"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataqna/v1alpha/question.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataqna.v1alpha import annotated_string_pb2 as google_dot_cloud_dot_dataqna_dot_v1alpha_dot_annotated__string__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/dataqna/v1alpha/question.proto\x12\x1cgoogle.cloud.dataqna.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/dataqna/v1alpha/annotated_string.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x9d\x04\n\x08Question\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x16\n\x06scopes\x18\x02 \x03(\tB\x06\xe0A\x02\xe0A\x05\x12\x15\n\x05query\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x1f\n\x17data_source_annotations\x18\x04 \x03(\t\x12E\n\x0finterpret_error\x18\x05 \x01(\x0b2,.google.cloud.dataqna.v1alpha.InterpretError\x12E\n\x0finterpretations\x18\x06 \x03(\x0b2,.google.cloud.dataqna.v1alpha.Interpretation\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\nuser_email\x18\x08 \x01(\tB\x03\xe0A\x03\x12E\n\x0bdebug_flags\x18\t \x01(\x0b2(.google.cloud.dataqna.v1alpha.DebugFlagsB\x06\xe0A\x05\xe0A\x04\x12(\n\ndebug_info\x18\n \x01(\x0b2\x14.google.protobuf.Any:b\xeaA_\n\x1fdataqna.googleapis.com/Question\x12<projects/{project}/locations/{location}/questions/{question}"\xdb\x06\n\x0eInterpretError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12M\n\x04code\x18\x02 \x01(\x0e2?.google.cloud.dataqna.v1alpha.InterpretError.InterpretErrorCode\x12S\n\x07details\x18\x03 \x01(\x0b2B.google.cloud.dataqna.v1alpha.InterpretError.InterpretErrorDetails\x1a\xd1\x02\n\x15InterpretErrorDetails\x12e\n\x13unsupported_details\x18\x01 \x01(\x0b2H.google.cloud.dataqna.v1alpha.InterpretError.InterpretUnsupportedDetails\x12n\n\x18incomplete_query_details\x18\x02 \x01(\x0b2L.google.cloud.dataqna.v1alpha.InterpretError.InterpretIncompleteQueryDetails\x12a\n\x11ambiguity_details\x18\x03 \x01(\x0b2F.google.cloud.dataqna.v1alpha.InterpretError.InterpretAmbiguityDetails\x1a@\n\x1bInterpretUnsupportedDetails\x12\x11\n\toperators\x18\x01 \x03(\t\x12\x0e\n\x06intent\x18\x02 \x03(\t\x1ab\n\x1fInterpretIncompleteQueryDetails\x12?\n\x08entities\x18\x01 \x03(\x0e2-.google.cloud.dataqna.v1alpha.InterpretEntity\x1a\x1b\n\x19InterpretAmbiguityDetails"}\n\x12InterpretErrorCode\x12$\n INTERPRET_ERROR_CODE_UNSPECIFIED\x10\x00\x12\x11\n\rINVALID_QUERY\x10\x01\x12\x18\n\x14FAILED_TO_UNDERSTAND\x10\x02\x12\x14\n\x10FAILED_TO_ANSWER\x10\x03"\x82\x03\n\rExecutionInfo\x12/\n\x13job_creation_status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12Z\n\x13job_execution_state\x18\x02 \x01(\x0e2=.google.cloud.dataqna.v1alpha.ExecutionInfo.JobExecutionState\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12?\n\x0cbigquery_job\x18\x04 \x01(\x0b2).google.cloud.dataqna.v1alpha.BigQueryJob"r\n\x11JobExecutionState\x12#\n\x1fJOB_EXECUTION_STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_EXECUTED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04"C\n\x0bBigQueryJob\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t"\xf2\x02\n\x0eInterpretation\x12\x14\n\x0cdata_sources\x18\x01 \x03(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x01\x12\x16\n\x0eunused_phrases\x18\x03 \x03(\t\x12C\n\x0ehuman_readable\x18\x04 \x01(\x0b2+.google.cloud.dataqna.v1alpha.HumanReadable\x12W\n\x18interpretation_structure\x18\x05 \x01(\x0b25.google.cloud.dataqna.v1alpha.InterpretationStructure\x12;\n\ndata_query\x18\x06 \x01(\x0b2\'.google.cloud.dataqna.v1alpha.DataQuery\x12C\n\x0eexecution_info\x18\x07 \x01(\x0b2+.google.cloud.dataqna.v1alpha.ExecutionInfo"\x18\n\tDataQuery\x12\x0b\n\x03sql\x18\x01 \x01(\t"\xaa\x01\n\rHumanReadable\x12O\n\x18generated_interpretation\x18\x01 \x01(\x0b2-.google.cloud.dataqna.v1alpha.AnnotatedString\x12H\n\x11original_question\x18\x02 \x01(\x0b2-.google.cloud.dataqna.v1alpha.AnnotatedString"\x92\x04\n\x17InterpretationStructure\x12d\n\x13visualization_types\x18\x01 \x03(\x0e2G.google.cloud.dataqna.v1alpha.InterpretationStructure.VisualizationType\x12U\n\x0bcolumn_info\x18\x02 \x03(\x0b2@.google.cloud.dataqna.v1alpha.InterpretationStructure.ColumnInfo\x1a8\n\nColumnInfo\x12\x14\n\x0coutput_alias\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t"\xff\x01\n\x11VisualizationType\x12"\n\x1eVISUALIZATION_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TABLE\x10\x01\x12\r\n\tBAR_CHART\x10\x02\x12\x10\n\x0cCOLUMN_CHART\x10\x03\x12\x0c\n\x08TIMELINE\x10\x04\x12\x10\n\x0cSCATTER_PLOT\x10\x05\x12\r\n\tPIE_CHART\x10\x06\x12\x0e\n\nLINE_CHART\x10\x07\x12\x0e\n\nAREA_CHART\x10\x08\x12\x0f\n\x0bCOMBO_CHART\x10\t\x12\r\n\tHISTOGRAM\x10\n\x12\x11\n\rGENERIC_CHART\x10\x0b\x12\x18\n\x14CHART_NOT_UNDERSTOOD\x10\x0c"\x95\x03\n\nDebugFlags\x12\x18\n\x10include_va_query\x18\x01 \x01(\x08\x12\x1f\n\x17include_nested_va_query\x18\x02 \x01(\x08\x12$\n\x1cinclude_human_interpretation\x18\x03 \x01(\x08\x12#\n\x1binclude_aqua_debug_response\x18\x04 \x01(\x08\x12\x15\n\rtime_override\x18\x05 \x01(\x03\x12\x1f\n\x17is_internal_google_user\x18\x06 \x01(\x08\x12\x14\n\x0cignore_cache\x18\x07 \x01(\x08\x12#\n\x1binclude_search_entities_rpc\x18\x08 \x01(\x08\x12+\n#include_list_column_annotations_rpc\x18\t \x01(\x08\x12(\n include_virtual_analyst_entities\x18\n \x01(\x08\x12\x1a\n\x12include_table_list\x18\x0b \x01(\x08\x12\x1b\n\x13include_domain_list\x18\x0c \x01(\x08*N\n\x0fInterpretEntity\x12 \n\x1cINTERPRET_ENTITY_UNSPECIFIED\x10\x00\x12\r\n\tDIMENSION\x10\x01\x12\n\n\x06METRIC\x10\x02B\xcf\x01\n com.google.cloud.dataqna.v1alphaB\rQuestionProtoP\x01Z:cloud.google.com/go/dataqna/apiv1alpha/dataqnapb;dataqnapb\xaa\x02\x1cGoogle.Cloud.DataQnA.V1Alpha\xca\x02\x1cGoogle\\Cloud\\DataQnA\\V1alpha\xea\x02\x1fGoogle::Cloud::DataQnA::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataqna.v1alpha.question_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.dataqna.v1alphaB\rQuestionProtoP\x01Z:cloud.google.com/go/dataqna/apiv1alpha/dataqnapb;dataqnapb\xaa\x02\x1cGoogle.Cloud.DataQnA.V1Alpha\xca\x02\x1cGoogle\\Cloud\\DataQnA\\V1alpha\xea\x02\x1fGoogle::Cloud::DataQnA::V1alpha'
    _globals['_QUESTION'].fields_by_name['name']._loaded_options = None
    _globals['_QUESTION'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_QUESTION'].fields_by_name['scopes']._loaded_options = None
    _globals['_QUESTION'].fields_by_name['scopes']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_QUESTION'].fields_by_name['query']._loaded_options = None
    _globals['_QUESTION'].fields_by_name['query']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_QUESTION'].fields_by_name['user_email']._loaded_options = None
    _globals['_QUESTION'].fields_by_name['user_email']._serialized_options = b'\xe0A\x03'
    _globals['_QUESTION'].fields_by_name['debug_flags']._loaded_options = None
    _globals['_QUESTION'].fields_by_name['debug_flags']._serialized_options = b'\xe0A\x05\xe0A\x04'
    _globals['_QUESTION']._loaded_options = None
    _globals['_QUESTION']._serialized_options = b'\xeaA_\n\x1fdataqna.googleapis.com/Question\x12<projects/{project}/locations/{location}/questions/{question}'
    _globals['_INTERPRETENTITY']._serialized_start = 3652
    _globals['_INTERPRETENTITY']._serialized_end = 3730
    _globals['_QUESTION']._serialized_start = 276
    _globals['_QUESTION']._serialized_end = 817
    _globals['_INTERPRETERROR']._serialized_start = 820
    _globals['_INTERPRETERROR']._serialized_end = 1679
    _globals['_INTERPRETERROR_INTERPRETERRORDETAILS']._serialized_start = 1020
    _globals['_INTERPRETERROR_INTERPRETERRORDETAILS']._serialized_end = 1357
    _globals['_INTERPRETERROR_INTERPRETUNSUPPORTEDDETAILS']._serialized_start = 1359
    _globals['_INTERPRETERROR_INTERPRETUNSUPPORTEDDETAILS']._serialized_end = 1423
    _globals['_INTERPRETERROR_INTERPRETINCOMPLETEQUERYDETAILS']._serialized_start = 1425
    _globals['_INTERPRETERROR_INTERPRETINCOMPLETEQUERYDETAILS']._serialized_end = 1523
    _globals['_INTERPRETERROR_INTERPRETAMBIGUITYDETAILS']._serialized_start = 1525
    _globals['_INTERPRETERROR_INTERPRETAMBIGUITYDETAILS']._serialized_end = 1552
    _globals['_INTERPRETERROR_INTERPRETERRORCODE']._serialized_start = 1554
    _globals['_INTERPRETERROR_INTERPRETERRORCODE']._serialized_end = 1679
    _globals['_EXECUTIONINFO']._serialized_start = 1682
    _globals['_EXECUTIONINFO']._serialized_end = 2068
    _globals['_EXECUTIONINFO_JOBEXECUTIONSTATE']._serialized_start = 1954
    _globals['_EXECUTIONINFO_JOBEXECUTIONSTATE']._serialized_end = 2068
    _globals['_BIGQUERYJOB']._serialized_start = 2070
    _globals['_BIGQUERYJOB']._serialized_end = 2137
    _globals['_INTERPRETATION']._serialized_start = 2140
    _globals['_INTERPRETATION']._serialized_end = 2510
    _globals['_DATAQUERY']._serialized_start = 2512
    _globals['_DATAQUERY']._serialized_end = 2536
    _globals['_HUMANREADABLE']._serialized_start = 2539
    _globals['_HUMANREADABLE']._serialized_end = 2709
    _globals['_INTERPRETATIONSTRUCTURE']._serialized_start = 2712
    _globals['_INTERPRETATIONSTRUCTURE']._serialized_end = 3242
    _globals['_INTERPRETATIONSTRUCTURE_COLUMNINFO']._serialized_start = 2928
    _globals['_INTERPRETATIONSTRUCTURE_COLUMNINFO']._serialized_end = 2984
    _globals['_INTERPRETATIONSTRUCTURE_VISUALIZATIONTYPE']._serialized_start = 2987
    _globals['_INTERPRETATIONSTRUCTURE_VISUALIZATIONTYPE']._serialized_end = 3242
    _globals['_DEBUGFLAGS']._serialized_start = 3245
    _globals['_DEBUGFLAGS']._serialized_end = 3650