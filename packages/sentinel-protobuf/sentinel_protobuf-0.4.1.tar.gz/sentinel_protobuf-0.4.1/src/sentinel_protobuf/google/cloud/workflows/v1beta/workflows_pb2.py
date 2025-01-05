"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/workflows/v1beta/workflows.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/workflows/v1beta/workflows.proto\x12\x1dgoogle.cloud.workflows.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfe\x04\n\x08Workflow\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12A\n\x05state\x18\x03 \x01(\x0e2-.google.cloud.workflows.v1beta.Workflow.StateB\x03\xe0A\x03\x12\x18\n\x0brevision_id\x18\x04 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x14revision_create_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x06labels\x18\x08 \x03(\x0b23.google.cloud.workflows.v1beta.Workflow.LabelsEntry\x12\x17\n\x0fservice_account\x18\t \x01(\t\x12\x19\n\x0fsource_contents\x18\n \x01(\tH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"*\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01:d\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}B\r\n\x0bsource_code"\x9a\x01\n\x14ListWorkflowsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x81\x01\n\x15ListWorkflowsResponse\x12:\n\tworkflows\x18\x01 \x03(\x0b2\'.google.cloud.workflows.v1beta.Workflow\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"M\n\x12GetWorkflowRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow"\xac\x01\n\x15CreateWorkflowRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12>\n\x08workflow\x18\x02 \x01(\x0b2\'.google.cloud.workflows.v1beta.WorkflowB\x03\xe0A\x02\x12\x18\n\x0bworkflow_id\x18\x03 \x01(\tB\x03\xe0A\x02"P\n\x15DeleteWorkflowRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow"\x88\x01\n\x15UpdateWorkflowRequest\x12>\n\x08workflow\x18\x01 \x01(\x0b2\'.google.cloud.workflows.v1beta.WorkflowB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xa5\x01\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t\x12\x13\n\x0bapi_version\x18\x05 \x01(\t2\xf9\x08\n\tWorkflows\x12\xbe\x01\n\rListWorkflows\x123.google.cloud.workflows.v1beta.ListWorkflowsRequest\x1a4.google.cloud.workflows.v1beta.ListWorkflowsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1beta/{parent=projects/*/locations/*}/workflows\x12\xab\x01\n\x0bGetWorkflow\x121.google.cloud.workflows.v1beta.GetWorkflowRequest\x1a\'.google.cloud.workflows.v1beta.Workflow"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1beta/{name=projects/*/locations/*/workflows/*}\x12\xe9\x01\n\x0eCreateWorkflow\x124.google.cloud.workflows.v1beta.CreateWorkflowRequest\x1a\x1d.google.longrunning.Operation"\x81\x01\xcaA\x1d\n\x08Workflow\x12\x11OperationMetadata\xdaA\x1bparent,workflow,workflow_id\x82\xd3\xe4\x93\x02="1/v1beta/{parent=projects/*/locations/*}/workflows:\x08workflow\x12\xd4\x01\n\x0eDeleteWorkflow\x124.google.cloud.workflows.v1beta.DeleteWorkflowRequest\x1a\x1d.google.longrunning.Operation"m\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1beta/{name=projects/*/locations/*/workflows/*}\x12\xeb\x01\n\x0eUpdateWorkflow\x124.google.cloud.workflows.v1beta.UpdateWorkflowRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA\x1d\n\x08Workflow\x12\x11OperationMetadata\xdaA\x14workflow,update_mask\x82\xd3\xe4\x93\x02F2:/v1beta/{workflow.name=projects/*/locations/*/workflows/*}:\x08workflow\x1aL\xcaA\x18workflows.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBv\n!com.google.cloud.workflows.v1betaB\x0eWorkflowsProtoP\x01Z?cloud.google.com/go/workflows/apiv1beta/workflowspb;workflowspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.workflows.v1beta.workflows_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.workflows.v1betaB\x0eWorkflowsProtoP\x01Z?cloud.google.com/go/workflows/apiv1beta/workflowspb;workflowspb'
    _globals['_WORKFLOW_LABELSENTRY']._loaded_options = None
    _globals['_WORKFLOW_LABELSENTRY']._serialized_options = b'8\x01'
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
    _globals['_WORKFLOW']._loaded_options = None
    _globals['_WORKFLOW']._serialized_options = b'\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}'
    _globals['_LISTWORKFLOWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTWORKFLOWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETWORKFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWORKFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!workflows.googleapis.com/Workflow'
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
    _globals['_WORKFLOWS'].methods_by_name['ListWorkflows']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1beta/{parent=projects/*/locations/*}/workflows'
    _globals['_WORKFLOWS'].methods_by_name['GetWorkflow']._loaded_options = None
    _globals['_WORKFLOWS'].methods_by_name['GetWorkflow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1beta/{name=projects/*/locations/*/workflows/*}'
    _globals['_WORKFLOWS'].methods_by_name['CreateWorkflow']._loaded_options = None
    _globals['_WORKFLOWS'].methods_by_name['CreateWorkflow']._serialized_options = b'\xcaA\x1d\n\x08Workflow\x12\x11OperationMetadata\xdaA\x1bparent,workflow,workflow_id\x82\xd3\xe4\x93\x02="1/v1beta/{parent=projects/*/locations/*}/workflows:\x08workflow'
    _globals['_WORKFLOWS'].methods_by_name['DeleteWorkflow']._loaded_options = None
    _globals['_WORKFLOWS'].methods_by_name['DeleteWorkflow']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1beta/{name=projects/*/locations/*/workflows/*}'
    _globals['_WORKFLOWS'].methods_by_name['UpdateWorkflow']._loaded_options = None
    _globals['_WORKFLOWS'].methods_by_name['UpdateWorkflow']._serialized_options = b'\xcaA\x1d\n\x08Workflow\x12\x11OperationMetadata\xdaA\x14workflow,update_mask\x82\xd3\xe4\x93\x02F2:/v1beta/{workflow.name=projects/*/locations/*/workflows/*}:\x08workflow'
    _globals['_WORKFLOW']._serialized_start = 300
    _globals['_WORKFLOW']._serialized_end = 938
    _globals['_WORKFLOW_LABELSENTRY']._serialized_start = 732
    _globals['_WORKFLOW_LABELSENTRY']._serialized_end = 777
    _globals['_WORKFLOW_STATE']._serialized_start = 779
    _globals['_WORKFLOW_STATE']._serialized_end = 821
    _globals['_LISTWORKFLOWSREQUEST']._serialized_start = 941
    _globals['_LISTWORKFLOWSREQUEST']._serialized_end = 1095
    _globals['_LISTWORKFLOWSRESPONSE']._serialized_start = 1098
    _globals['_LISTWORKFLOWSRESPONSE']._serialized_end = 1227
    _globals['_GETWORKFLOWREQUEST']._serialized_start = 1229
    _globals['_GETWORKFLOWREQUEST']._serialized_end = 1306
    _globals['_CREATEWORKFLOWREQUEST']._serialized_start = 1309
    _globals['_CREATEWORKFLOWREQUEST']._serialized_end = 1481
    _globals['_DELETEWORKFLOWREQUEST']._serialized_start = 1483
    _globals['_DELETEWORKFLOWREQUEST']._serialized_end = 1563
    _globals['_UPDATEWORKFLOWREQUEST']._serialized_start = 1566
    _globals['_UPDATEWORKFLOWREQUEST']._serialized_end = 1702
    _globals['_OPERATIONMETADATA']._serialized_start = 1705
    _globals['_OPERATIONMETADATA']._serialized_end = 1870
    _globals['_WORKFLOWS']._serialized_start = 1873
    _globals['_WORKFLOWS']._serialized_end = 3018