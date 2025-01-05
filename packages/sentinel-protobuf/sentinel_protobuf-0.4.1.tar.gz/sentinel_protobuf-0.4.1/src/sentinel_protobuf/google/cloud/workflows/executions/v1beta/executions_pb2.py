"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/workflows/executions/v1beta/executions.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/workflows/executions/v1beta/executions.proto\x12(google.cloud.workflows.executions.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf8\x04\n\tExecution\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12M\n\x05state\x18\x04 \x01(\x0e29.google.cloud.workflows.executions.v1beta.Execution.StateB\x03\xe0A\x03\x12\x10\n\x08argument\x18\x05 \x01(\t\x12\x13\n\x06result\x18\x06 \x01(\tB\x03\xe0A\x03\x12M\n\x05error\x18\x07 \x01(\x0b29.google.cloud.workflows.executions.v1beta.Execution.ErrorB\x03\xe0A\x03\x12!\n\x14workflow_revision_id\x18\x08 \x01(\tB\x03\xe0A\x03\x1a)\n\x05Error\x12\x0f\n\x07payload\x18\x01 \x01(\t\x12\x0f\n\x07context\x18\x02 \x01(\t"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06FAILED\x10\x03\x12\r\n\tCANCELLED\x10\x04:\x86\x01\xeaA\x82\x01\n+workflowexecutions.googleapis.com/Execution\x12Sprojects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}"\xc5\x01\n\x15ListExecutionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12J\n\x04view\x18\x04 \x01(\x0e27.google.cloud.workflows.executions.v1beta.ExecutionViewB\x03\xe0A\x01"z\n\x16ListExecutionsResponse\x12G\n\nexecutions\x18\x01 \x03(\x0b23.google.cloud.workflows.executions.v1beta.Execution\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa0\x01\n\x16CreateExecutionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow\x12K\n\texecution\x18\x02 \x01(\x0b23.google.cloud.workflows.executions.v1beta.ExecutionB\x03\xe0A\x02"\xa4\x01\n\x13GetExecutionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+workflowexecutions.googleapis.com/Execution\x12J\n\x04view\x18\x02 \x01(\x0e27.google.cloud.workflows.executions.v1beta.ExecutionViewB\x03\xe0A\x01"[\n\x16CancelExecutionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+workflowexecutions.googleapis.com/Execution*D\n\rExecutionView\x12\x1e\n\x1aEXECUTION_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x022\xf3\x07\n\nExecutions\x12\xe4\x01\n\x0eListExecutions\x12?.google.cloud.workflows.executions.v1beta.ListExecutionsRequest\x1a@.google.cloud.workflows.executions.v1beta.ListExecutionsResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta/{parent=projects/*/locations/*/workflows/*}/executions\x12\xee\x01\n\x0fCreateExecution\x12@.google.cloud.workflows.executions.v1beta.CreateExecutionRequest\x1a3.google.cloud.workflows.executions.v1beta.Execution"d\xdaA\x10parent,execution\x82\xd3\xe4\x93\x02K">/v1beta/{parent=projects/*/locations/*/workflows/*}/executions:\texecution\x12\xd1\x01\n\x0cGetExecution\x12=.google.cloud.workflows.executions.v1beta.GetExecutionRequest\x1a3.google.cloud.workflows.executions.v1beta.Execution"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta/{name=projects/*/locations/*/workflows/*/executions/*}\x12\xe1\x01\n\x0fCancelExecution\x12@.google.cloud.workflows.executions.v1beta.CancelExecutionRequest\x1a3.google.cloud.workflows.executions.v1beta.Execution"W\xdaA\x04name\x82\xd3\xe4\x93\x02J"E/v1beta/{name=projects/*/locations/*/workflows/*/executions/*}:cancel:\x01*\x1aU\xcaA!workflowexecutions.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf3\x01\n,com.google.cloud.workflows.executions.v1betaB\x0fExecutionsProtoP\x01ZLcloud.google.com/go/workflows/executions/apiv1beta/executionspb;executionspb\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.workflows.executions.v1beta.executions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.workflows.executions.v1betaB\x0fExecutionsProtoP\x01ZLcloud.google.com/go/workflows/executions/apiv1beta/executionspb;executionspb\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}'
    _globals['_EXECUTION'].fields_by_name['name']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['start_time']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['end_time']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['state']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['result']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['result']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['error']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['workflow_revision_id']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['workflow_revision_id']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION']._loaded_options = None
    _globals['_EXECUTION']._serialized_options = b'\xeaA\x82\x01\n+workflowexecutions.googleapis.com/Execution\x12Sprojects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}'
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow'
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
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
    _globals['_EXECUTIONS'].methods_by_name['ListExecutions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta/{parent=projects/*/locations/*/workflows/*}/executions'
    _globals['_EXECUTIONS'].methods_by_name['CreateExecution']._loaded_options = None
    _globals['_EXECUTIONS'].methods_by_name['CreateExecution']._serialized_options = b'\xdaA\x10parent,execution\x82\xd3\xe4\x93\x02K">/v1beta/{parent=projects/*/locations/*/workflows/*}/executions:\texecution'
    _globals['_EXECUTIONS'].methods_by_name['GetExecution']._loaded_options = None
    _globals['_EXECUTIONS'].methods_by_name['GetExecution']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta/{name=projects/*/locations/*/workflows/*/executions/*}'
    _globals['_EXECUTIONS'].methods_by_name['CancelExecution']._loaded_options = None
    _globals['_EXECUTIONS'].methods_by_name['CancelExecution']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02J"E/v1beta/{name=projects/*/locations/*/workflows/*/executions/*}:cancel:\x01*'
    _globals['_EXECUTIONVIEW']._serialized_start = 1633
    _globals['_EXECUTIONVIEW']._serialized_end = 1701
    _globals['_EXECUTION']._serialized_start = 252
    _globals['_EXECUTION']._serialized_end = 884
    _globals['_EXECUTION_ERROR']._serialized_start = 620
    _globals['_EXECUTION_ERROR']._serialized_end = 661
    _globals['_EXECUTION_STATE']._serialized_start = 663
    _globals['_EXECUTION_STATE']._serialized_end = 747
    _globals['_LISTEXECUTIONSREQUEST']._serialized_start = 887
    _globals['_LISTEXECUTIONSREQUEST']._serialized_end = 1084
    _globals['_LISTEXECUTIONSRESPONSE']._serialized_start = 1086
    _globals['_LISTEXECUTIONSRESPONSE']._serialized_end = 1208
    _globals['_CREATEEXECUTIONREQUEST']._serialized_start = 1211
    _globals['_CREATEEXECUTIONREQUEST']._serialized_end = 1371
    _globals['_GETEXECUTIONREQUEST']._serialized_start = 1374
    _globals['_GETEXECUTIONREQUEST']._serialized_end = 1538
    _globals['_CANCELEXECUTIONREQUEST']._serialized_start = 1540
    _globals['_CANCELEXECUTIONREQUEST']._serialized_end = 1631
    _globals['_EXECUTIONS']._serialized_start = 1704
    _globals['_EXECUTIONS']._serialized_end = 2715