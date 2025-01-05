"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/workflows/v1/workflows.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/workflows/v1/workflows.proto\x12\x19google.cloud.workflows.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe0\t\n\x08Workflow\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12=\n\x05state\x18\x03 \x01(\x0e2).google.cloud.workflows.v1.Workflow.StateB\x03\xe0A\x03\x12\x18\n\x0brevision_id\x18\x04 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x14revision_create_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x06labels\x18\x08 \x03(\x0b2/.google.cloud.workflows.v1.Workflow.LabelsEntry\x12\x17\n\x0fservice_account\x18\t \x01(\t\x12\x19\n\x0fsource_contents\x18\n \x01(\tH\x00\x12B\n\x0fcrypto_key_name\x18\x0b \x01(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12H\n\x0bstate_error\x18\x0c \x01(\x0b2..google.cloud.workflows.v1.Workflow.StateErrorB\x03\xe0A\x03\x12M\n\x0ecall_log_level\x18\r \x01(\x0e20.google.cloud.workflows.v1.Workflow.CallLogLevelB\x03\xe0A\x01\x12P\n\ruser_env_vars\x18\x0e \x03(\x0b24.google.cloud.workflows.v1.Workflow.UserEnvVarsEntryB\x03\xe0A\x01\x1a\x8d\x01\n\nStateError\x12\x0f\n\x07details\x18\x01 \x01(\t\x12A\n\x04type\x18\x02 \x01(\x0e23.google.cloud.workflows.v1.Workflow.StateError.Type"+\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\r\n\tKMS_ERROR\x10\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10UserEnvVarsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01";\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0f\n\x0bUNAVAILABLE\x10\x02"d\n\x0cCallLogLevel\x12\x1e\n\x1aCALL_LOG_LEVEL_UNSPECIFIED\x10\x00\x12\x11\n\rLOG_ALL_CALLS\x10\x01\x12\x13\n\x0fLOG_ERRORS_ONLY\x10\x02\x12\x0c\n\x08LOG_NONE\x10\x03:d\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}B\r\n\x0bsource_code"\x9a\x01\n\x14ListWorkflowsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"}\n\x15ListWorkflowsResponse\x126\n\tworkflows\x18\x01 \x03(\x0b2#.google.cloud.workflows.v1.Workflow\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"g\n\x12GetWorkflowRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow\x12\x18\n\x0brevision_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xa8\x01\n\x15CreateWorkflowRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12:\n\x08workflow\x18\x02 \x01(\x0b2#.google.cloud.workflows.v1.WorkflowB\x03\xe0A\x02\x12\x18\n\x0bworkflow_id\x18\x03 \x01(\tB\x03\xe0A\x02"P\n\x15DeleteWorkflowRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow"\x84\x01\n\x15UpdateWorkflowRequest\x12:\n\x08workflow\x18\x01 \x01(\x0b2#.google.cloud.workflows.v1.WorkflowB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xa5\x01\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t\x12\x13\n\x0bapi_version\x18\x05 \x01(\t2\xc7\x08\n\tWorkflows\x12\xb2\x01\n\rListWorkflows\x12/.google.cloud.workflows.v1.ListWorkflowsRequest\x1a0.google.cloud.workflows.v1.ListWorkflowsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/workflows\x12\x9f\x01\n\x0bGetWorkflow\x12-.google.cloud.workflows.v1.GetWorkflowRequest\x1a#.google.cloud.workflows.v1.Workflow"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/workflows/*}\x12\xe0\x01\n\x0eCreateWorkflow\x120.google.cloud.workflows.v1.CreateWorkflowRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1d\n\x08Workflow\x12\x11OperationMetadata\xdaA\x1bparent,workflow,workflow_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/workflows:\x08workflow\x12\xcc\x01\n\x0eDeleteWorkflow\x120.google.cloud.workflows.v1.DeleteWorkflowRequest\x1a\x1d.google.longrunning.Operation"i\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/workflows/*}\x12\xe2\x01\n\x0eUpdateWorkflow\x120.google.cloud.workflows.v1.UpdateWorkflowRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA\x1d\n\x08Workflow\x12\x11OperationMetadata\xdaA\x14workflow,update_mask\x82\xd3\xe4\x93\x02B26/v1/{workflow.name=projects/*/locations/*/workflows/*}:\x08workflow\x1aL\xcaA\x18workflows.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe7\x01\n\x1dcom.google.cloud.workflows.v1B\x0eWorkflowsProtoP\x01Z;cloud.google.com/go/workflows/apiv1/workflowspb;workflowspb\xeaAv\n!cloudkms.googleapis.com/CryptoKey\x12Qprojects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.workflows.v1.workflows_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.workflows.v1B\x0eWorkflowsProtoP\x01Z;cloud.google.com/go/workflows/apiv1/workflowspb;workflowspb\xeaAv\n!cloudkms.googleapis.com/CryptoKey\x12Qprojects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}'
    _globals['_WORKFLOW_LABELSENTRY']._loaded_options = None
    _globals['_WORKFLOW_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_WORKFLOW_USERENVVARSENTRY']._loaded_options = None
    _globals['_WORKFLOW_USERENVVARSENTRY']._serialized_options = b'8\x01'
    _globals['_WORKFLOW'].fields_by_name['state']._loaded_options = None
    _globals['_WORKFLOW'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFLOW'].fields_by_name['revision_id']._loaded_options = None
    _globals['_WORKFLOW'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFLOW'].fields_by_name['create_time']._loaded_options = None
    _globals['_WORKFLOW'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFLOW'].fields_by_name['update_time']._loaded_options = None
    _globals['_WORKFLOW'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFLOW'].fields_by_name['revision_create_time']._loaded_options = None
    _globals['_WORKFLOW'].fields_by_name['revision_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFLOW'].fields_by_name['crypto_key_name']._loaded_options = None
    _globals['_WORKFLOW'].fields_by_name['crypto_key_name']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_WORKFLOW'].fields_by_name['state_error']._loaded_options = None
    _globals['_WORKFLOW'].fields_by_name['state_error']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFLOW'].fields_by_name['call_log_level']._loaded_options = None
    _globals['_WORKFLOW'].fields_by_name['call_log_level']._serialized_options = b'\xe0A\x01'
    _globals['_WORKFLOW'].fields_by_name['user_env_vars']._loaded_options = None
    _globals['_WORKFLOW'].fields_by_name['user_env_vars']._serialized_options = b'\xe0A\x01'
    _globals['_WORKFLOW']._loaded_options = None
    _globals['_WORKFLOW']._serialized_options = b'\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}'
    _globals['_LISTWORKFLOWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTWORKFLOWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETWORKFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWORKFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow'
    _globals['_GETWORKFLOWREQUEST'].fields_by_name['revision_id']._loaded_options = None
    _globals['_GETWORKFLOWREQUEST'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEWORKFLOWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEWORKFLOWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEWORKFLOWREQUEST'].fields_by_name['workflow']._loaded_options = None
    _globals['_CREATEWORKFLOWREQUEST'].fields_by_name['workflow']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEWORKFLOWREQUEST'].fields_by_name['workflow_id']._loaded_options = None
    _globals['_CREATEWORKFLOWREQUEST'].fields_by_name['workflow_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEWORKFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEWORKFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow'
    _globals['_UPDATEWORKFLOWREQUEST'].fields_by_name['workflow']._loaded_options = None
    _globals['_UPDATEWORKFLOWREQUEST'].fields_by_name['workflow']._serialized_options = b'\xe0A\x02'
    _globals['_WORKFLOWS']._loaded_options = None
    _globals['_WORKFLOWS']._serialized_options = b'\xcaA\x18workflows.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_WORKFLOWS'].methods_by_name['ListWorkflows']._loaded_options = None
    _globals['_WORKFLOWS'].methods_by_name['ListWorkflows']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/workflows'
    _globals['_WORKFLOWS'].methods_by_name['GetWorkflow']._loaded_options = None
    _globals['_WORKFLOWS'].methods_by_name['GetWorkflow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/workflows/*}'
    _globals['_WORKFLOWS'].methods_by_name['CreateWorkflow']._loaded_options = None
    _globals['_WORKFLOWS'].methods_by_name['CreateWorkflow']._serialized_options = b'\xcaA\x1d\n\x08Workflow\x12\x11OperationMetadata\xdaA\x1bparent,workflow,workflow_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/workflows:\x08workflow'
    _globals['_WORKFLOWS'].methods_by_name['DeleteWorkflow']._loaded_options = None
    _globals['_WORKFLOWS'].methods_by_name['DeleteWorkflow']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/workflows/*}'
    _globals['_WORKFLOWS'].methods_by_name['UpdateWorkflow']._loaded_options = None
    _globals['_WORKFLOWS'].methods_by_name['UpdateWorkflow']._serialized_options = b'\xcaA\x1d\n\x08Workflow\x12\x11OperationMetadata\xdaA\x14workflow,update_mask\x82\xd3\xe4\x93\x02B26/v1/{workflow.name=projects/*/locations/*/workflows/*}:\x08workflow'
    _globals['_WORKFLOW']._serialized_start = 321
    _globals['_WORKFLOW']._serialized_end = 1569
    _globals['_WORKFLOW_STATEERROR']._serialized_start = 1049
    _globals['_WORKFLOW_STATEERROR']._serialized_end = 1190
    _globals['_WORKFLOW_STATEERROR_TYPE']._serialized_start = 1147
    _globals['_WORKFLOW_STATEERROR_TYPE']._serialized_end = 1190
    _globals['_WORKFLOW_LABELSENTRY']._serialized_start = 1192
    _globals['_WORKFLOW_LABELSENTRY']._serialized_end = 1237
    _globals['_WORKFLOW_USERENVVARSENTRY']._serialized_start = 1239
    _globals['_WORKFLOW_USERENVVARSENTRY']._serialized_end = 1289
    _globals['_WORKFLOW_STATE']._serialized_start = 1291
    _globals['_WORKFLOW_STATE']._serialized_end = 1350
    _globals['_WORKFLOW_CALLLOGLEVEL']._serialized_start = 1352
    _globals['_WORKFLOW_CALLLOGLEVEL']._serialized_end = 1452
    _globals['_LISTWORKFLOWSREQUEST']._serialized_start = 1572
    _globals['_LISTWORKFLOWSREQUEST']._serialized_end = 1726
    _globals['_LISTWORKFLOWSRESPONSE']._serialized_start = 1728
    _globals['_LISTWORKFLOWSRESPONSE']._serialized_end = 1853
    _globals['_GETWORKFLOWREQUEST']._serialized_start = 1855
    _globals['_GETWORKFLOWREQUEST']._serialized_end = 1958
    _globals['_CREATEWORKFLOWREQUEST']._serialized_start = 1961
    _globals['_CREATEWORKFLOWREQUEST']._serialized_end = 2129
    _globals['_DELETEWORKFLOWREQUEST']._serialized_start = 2131
    _globals['_DELETEWORKFLOWREQUEST']._serialized_end = 2211
    _globals['_UPDATEWORKFLOWREQUEST']._serialized_start = 2214
    _globals['_UPDATEWORKFLOWREQUEST']._serialized_end = 2346
    _globals['_OPERATIONMETADATA']._serialized_start = 2349
    _globals['_OPERATIONMETADATA']._serialized_end = 2514
    _globals['_WORKFLOWS']._serialized_start = 2517
    _globals['_WORKFLOWS']._serialized_end = 3612