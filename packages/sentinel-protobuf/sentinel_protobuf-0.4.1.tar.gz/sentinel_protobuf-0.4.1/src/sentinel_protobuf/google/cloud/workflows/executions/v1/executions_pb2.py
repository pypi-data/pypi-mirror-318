"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/workflows/executions/v1/executions.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/workflows/executions/v1/executions.proto\x12$google.cloud.workflows.executions.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbd\x0e\n\tExecution\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x120\n\x08duration\x18\x0c \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03\x12I\n\x05state\x18\x04 \x01(\x0e25.google.cloud.workflows.executions.v1.Execution.StateB\x03\xe0A\x03\x12\x10\n\x08argument\x18\x05 \x01(\t\x12\x13\n\x06result\x18\x06 \x01(\tB\x03\xe0A\x03\x12I\n\x05error\x18\x07 \x01(\x0b25.google.cloud.workflows.executions.v1.Execution.ErrorB\x03\xe0A\x03\x12!\n\x14workflow_revision_id\x18\x08 \x01(\tB\x03\xe0A\x03\x12T\n\x0ecall_log_level\x18\t \x01(\x0e2<.google.cloud.workflows.executions.v1.Execution.CallLogLevel\x12K\n\x06status\x18\n \x01(\x0b26.google.cloud.workflows.executions.v1.Execution.StatusB\x03\xe0A\x03\x12K\n\x06labels\x18\x0b \x03(\x0b2;.google.cloud.workflows.executions.v1.Execution.LabelsEntry\x12T\n\x0bstate_error\x18\r \x01(\x0b2:.google.cloud.workflows.executions.v1.Execution.StateErrorB\x03\xe0A\x03\x1a\xca\x01\n\x11StackTraceElement\x12\x0c\n\x04step\x18\x01 \x01(\t\x12\x0f\n\x07routine\x18\x02 \x01(\t\x12\\\n\x08position\x18\x03 \x01(\x0b2J.google.cloud.workflows.executions.v1.Execution.StackTraceElement.Position\x1a8\n\x08Position\x12\x0c\n\x04line\x18\x01 \x01(\x03\x12\x0e\n\x06column\x18\x02 \x01(\x03\x12\x0e\n\x06length\x18\x03 \x01(\x03\x1aa\n\nStackTrace\x12S\n\x08elements\x18\x01 \x03(\x0b2A.google.cloud.workflows.executions.v1.Execution.StackTraceElement\x1az\n\x05Error\x12\x0f\n\x07payload\x18\x01 \x01(\t\x12\x0f\n\x07context\x18\x02 \x01(\t\x12O\n\x0bstack_trace\x18\x03 \x01(\x0b2:.google.cloud.workflows.executions.v1.Execution.StackTrace\x1a\x83\x01\n\x06Status\x12R\n\rcurrent_steps\x18\x01 \x03(\x0b2;.google.cloud.workflows.executions.v1.Execution.Status.Step\x1a%\n\x04Step\x12\x0f\n\x07routine\x18\x01 \x01(\t\x12\x0c\n\x04step\x18\x02 \x01(\t\x1a\x99\x01\n\nStateError\x12\x0f\n\x07details\x18\x01 \x01(\t\x12M\n\x04type\x18\x02 \x01(\x0e2?.google.cloud.workflows.executions.v1.Execution.StateError.Type"+\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\r\n\tKMS_ERROR\x10\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"q\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06FAILED\x10\x03\x12\r\n\tCANCELLED\x10\x04\x12\x0f\n\x0bUNAVAILABLE\x10\x05\x12\n\n\x06QUEUED\x10\x06"d\n\x0cCallLogLevel\x12\x1e\n\x1aCALL_LOG_LEVEL_UNSPECIFIED\x10\x00\x12\x11\n\rLOG_ALL_CALLS\x10\x01\x12\x13\n\x0fLOG_ERRORS_ONLY\x10\x02\x12\x0c\n\x08LOG_NONE\x10\x03:\x86\x01\xeaA\x82\x01\n+workflowexecutions.googleapis.com/Execution\x12Sprojects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}"\xed\x01\n\x15ListExecutionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12F\n\x04view\x18\x04 \x01(\x0e23.google.cloud.workflows.executions.v1.ExecutionViewB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x06 \x01(\tB\x03\xe0A\x01"v\n\x16ListExecutionsResponse\x12C\n\nexecutions\x18\x01 \x03(\x0b2/.google.cloud.workflows.executions.v1.Execution\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9c\x01\n\x16CreateExecutionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow\x12G\n\texecution\x18\x02 \x01(\x0b2/.google.cloud.workflows.executions.v1.ExecutionB\x03\xe0A\x02"\xa0\x01\n\x13GetExecutionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+workflowexecutions.googleapis.com/Execution\x12F\n\x04view\x18\x02 \x01(\x0e23.google.cloud.workflows.executions.v1.ExecutionViewB\x03\xe0A\x01"[\n\x16CancelExecutionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+workflowexecutions.googleapis.com/Execution*D\n\rExecutionView\x12\x1e\n\x1aEXECUTION_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x022\xc3\x07\n\nExecutions\x12\xd8\x01\n\x0eListExecutions\x12;.google.cloud.workflows.executions.v1.ListExecutionsRequest\x1a<.google.cloud.workflows.executions.v1.ListExecutionsResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*/workflows/*}/executions\x12\xe2\x01\n\x0fCreateExecution\x12<.google.cloud.workflows.executions.v1.CreateExecutionRequest\x1a/.google.cloud.workflows.executions.v1.Execution"`\xdaA\x10parent,execution\x82\xd3\xe4\x93\x02G":/v1/{parent=projects/*/locations/*/workflows/*}/executions:\texecution\x12\xc5\x01\n\x0cGetExecution\x129.google.cloud.workflows.executions.v1.GetExecutionRequest\x1a/.google.cloud.workflows.executions.v1.Execution"I\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/*/workflows/*/executions/*}\x12\xd5\x01\n\x0fCancelExecution\x12<.google.cloud.workflows.executions.v1.CancelExecutionRequest\x1a/.google.cloud.workflows.executions.v1.Execution"S\xdaA\x04name\x82\xd3\xe4\x93\x02F"A/v1/{name=projects/*/locations/*/workflows/*/executions/*}:cancel:\x01*\x1aU\xcaA!workflowexecutions.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xeb\x01\n(com.google.cloud.workflows.executions.v1B\x0fExecutionsProtoP\x01ZHcloud.google.com/go/workflows/executions/apiv1/executionspb;executionspb\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.workflows.executions.v1.executions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.cloud.workflows.executions.v1B\x0fExecutionsProtoP\x01ZHcloud.google.com/go/workflows/executions/apiv1/executionspb;executionspb\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}'
    _globals['_EXECUTION_LABELSENTRY']._loaded_options = None
    _globals['_EXECUTION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTION'].fields_by_name['name']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['start_time']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['end_time']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['duration']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['duration']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['state']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['result']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['result']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['error']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['workflow_revision_id']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['workflow_revision_id']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['status']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['state_error']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['state_error']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION']._loaded_options = None
    _globals['_EXECUTION']._serialized_options = b'\xeaA\x82\x01\n+workflowexecutions.googleapis.com/Execution\x12Sprojects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}'
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow'
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEEXECUTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEEXECUTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow'
    _globals['_CREATEEXECUTIONREQUEST'].fields_by_name['execution']._loaded_options = None
    _globals['_CREATEEXECUTIONREQUEST'].fields_by_name['execution']._serialized_options = b'\xe0A\x02'
    _globals['_GETEXECUTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEXECUTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+workflowexecutions.googleapis.com/Execution'
    _globals['_GETEXECUTIONREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETEXECUTIONREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_CANCELEXECUTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELEXECUTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+workflowexecutions.googleapis.com/Execution'
    _globals['_EXECUTIONS']._loaded_options = None
    _globals['_EXECUTIONS']._serialized_options = b'\xcaA!workflowexecutions.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_EXECUTIONS'].methods_by_name['ListExecutions']._loaded_options = None
    _globals['_EXECUTIONS'].methods_by_name['ListExecutions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*/workflows/*}/executions'
    _globals['_EXECUTIONS'].methods_by_name['CreateExecution']._loaded_options = None
    _globals['_EXECUTIONS'].methods_by_name['CreateExecution']._serialized_options = b'\xdaA\x10parent,execution\x82\xd3\xe4\x93\x02G":/v1/{parent=projects/*/locations/*/workflows/*}/executions:\texecution'
    _globals['_EXECUTIONS'].methods_by_name['GetExecution']._loaded_options = None
    _globals['_EXECUTIONS'].methods_by_name['GetExecution']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/*/workflows/*/executions/*}'
    _globals['_EXECUTIONS'].methods_by_name['CancelExecution']._loaded_options = None
    _globals['_EXECUTIONS'].methods_by_name['CancelExecution']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02F"A/v1/{name=projects/*/locations/*/workflows/*/executions/*}:cancel:\x01*'
    _globals['_EXECUTIONVIEW']._serialized_start = 2906
    _globals['_EXECUTIONVIEW']._serialized_end = 2974
    _globals['_EXECUTION']._serialized_start = 276
    _globals['_EXECUTION']._serialized_end = 2129
    _globals['_EXECUTION_STACKTRACEELEMENT']._serialized_start = 1013
    _globals['_EXECUTION_STACKTRACEELEMENT']._serialized_end = 1215
    _globals['_EXECUTION_STACKTRACEELEMENT_POSITION']._serialized_start = 1159
    _globals['_EXECUTION_STACKTRACEELEMENT_POSITION']._serialized_end = 1215
    _globals['_EXECUTION_STACKTRACE']._serialized_start = 1217
    _globals['_EXECUTION_STACKTRACE']._serialized_end = 1314
    _globals['_EXECUTION_ERROR']._serialized_start = 1316
    _globals['_EXECUTION_ERROR']._serialized_end = 1438
    _globals['_EXECUTION_STATUS']._serialized_start = 1441
    _globals['_EXECUTION_STATUS']._serialized_end = 1572
    _globals['_EXECUTION_STATUS_STEP']._serialized_start = 1535
    _globals['_EXECUTION_STATUS_STEP']._serialized_end = 1572
    _globals['_EXECUTION_STATEERROR']._serialized_start = 1575
    _globals['_EXECUTION_STATEERROR']._serialized_end = 1728
    _globals['_EXECUTION_STATEERROR_TYPE']._serialized_start = 1685
    _globals['_EXECUTION_STATEERROR_TYPE']._serialized_end = 1728
    _globals['_EXECUTION_LABELSENTRY']._serialized_start = 1730
    _globals['_EXECUTION_LABELSENTRY']._serialized_end = 1775
    _globals['_EXECUTION_STATE']._serialized_start = 1777
    _globals['_EXECUTION_STATE']._serialized_end = 1890
    _globals['_EXECUTION_CALLLOGLEVEL']._serialized_start = 1892
    _globals['_EXECUTION_CALLLOGLEVEL']._serialized_end = 1992
    _globals['_LISTEXECUTIONSREQUEST']._serialized_start = 2132
    _globals['_LISTEXECUTIONSREQUEST']._serialized_end = 2369
    _globals['_LISTEXECUTIONSRESPONSE']._serialized_start = 2371
    _globals['_LISTEXECUTIONSRESPONSE']._serialized_end = 2489
    _globals['_CREATEEXECUTIONREQUEST']._serialized_start = 2492
    _globals['_CREATEEXECUTIONREQUEST']._serialized_end = 2648
    _globals['_GETEXECUTIONREQUEST']._serialized_start = 2651
    _globals['_GETEXECUTIONREQUEST']._serialized_end = 2811
    _globals['_CANCELEXECUTIONREQUEST']._serialized_start = 2813
    _globals['_CANCELEXECUTIONREQUEST']._serialized_end = 2904
    _globals['_EXECUTIONS']._serialized_start = 2977
    _globals['_EXECUTIONS']._serialized_end = 3940