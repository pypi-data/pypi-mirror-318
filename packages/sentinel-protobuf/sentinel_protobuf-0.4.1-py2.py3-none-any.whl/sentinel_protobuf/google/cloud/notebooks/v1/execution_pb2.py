"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/v1/execution.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/notebooks/v1/execution.proto\x12\x19google.cloud.notebooks.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xea\x0c\n\x11ExecutionTemplate\x12Q\n\nscale_tier\x18\x01 \x01(\x0e26.google.cloud.notebooks.v1.ExecutionTemplate.ScaleTierB\x05\x18\x01\xe0A\x02\x12\x13\n\x0bmaster_type\x18\x02 \x01(\t\x12c\n\x12accelerator_config\x18\x03 \x01(\x0b2G.google.cloud.notebooks.v1.ExecutionTemplate.SchedulerAcceleratorConfig\x12H\n\x06labels\x18\x04 \x03(\x0b28.google.cloud.notebooks.v1.ExecutionTemplate.LabelsEntry\x12\x1b\n\x13input_notebook_file\x18\x05 \x01(\t\x12\x1b\n\x13container_image_uri\x18\x06 \x01(\t\x12\x1e\n\x16output_notebook_folder\x18\x07 \x01(\t\x12\x18\n\x10params_yaml_file\x18\x08 \x01(\t\x12\x12\n\nparameters\x18\t \x01(\t\x12\x17\n\x0fservice_account\x18\n \x01(\t\x12F\n\x08job_type\x18\x0b \x01(\x0e24.google.cloud.notebooks.v1.ExecutionTemplate.JobType\x12^\n\x13dataproc_parameters\x18\x0c \x01(\x0b2?.google.cloud.notebooks.v1.ExecutionTemplate.DataprocParametersH\x00\x12_\n\x14vertex_ai_parameters\x18\r \x01(\x0b2?.google.cloud.notebooks.v1.ExecutionTemplate.VertexAIParametersH\x00\x12\x13\n\x0bkernel_spec\x18\x0e \x01(\t\x12?\n\x0btensorboard\x18\x0f \x01(\tB*\xfaA\'\n%aiplatform.googleapis.com/Tensorboard\x1a\x85\x01\n\x1aSchedulerAcceleratorConfig\x12S\n\x04type\x18\x01 \x01(\x0e2E.google.cloud.notebooks.v1.ExecutionTemplate.SchedulerAcceleratorType\x12\x12\n\ncore_count\x18\x02 \x01(\x03\x1a%\n\x12DataprocParameters\x12\x0f\n\x07cluster\x18\x01 \x01(\t\x1a\xa8\x01\n\x12VertexAIParameters\x12\x0f\n\x07network\x18\x01 \x01(\t\x12U\n\x03env\x18\x02 \x03(\x0b2H.google.cloud.notebooks.v1.ExecutionTemplate.VertexAIParameters.EnvEntry\x1a*\n\x08EnvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"{\n\tScaleTier\x12\x1a\n\x16SCALE_TIER_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x0e\n\nSTANDARD_1\x10\x02\x12\r\n\tPREMIUM_1\x10\x03\x12\r\n\tBASIC_GPU\x10\x04\x12\r\n\tBASIC_TPU\x10\x05\x12\n\n\x06CUSTOM\x10\x06"\xe3\x01\n\x18SchedulerAcceleratorType\x12*\n&SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10NVIDIA_TESLA_K80\x10\x01\x12\x15\n\x11NVIDIA_TESLA_P100\x10\x02\x12\x15\n\x11NVIDIA_TESLA_V100\x10\x03\x12\x13\n\x0fNVIDIA_TESLA_P4\x10\x04\x12\x13\n\x0fNVIDIA_TESLA_T4\x10\x05\x12\x15\n\x11NVIDIA_TESLA_A100\x10\n\x12\n\n\x06TPU_V2\x10\x06\x12\n\n\x06TPU_V3\x10\x07"@\n\x07JobType\x12\x18\n\x14JOB_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tVERTEX_AI\x10\x01\x12\x0c\n\x08DATAPROC\x10\x02B\x10\n\x0ejob_parameters"\x82\x05\n\tExecution\x12H\n\x12execution_template\x18\x01 \x01(\x0b2,.google.cloud.notebooks.v1.ExecutionTemplate\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12>\n\x05state\x18\x07 \x01(\x0e2*.google.cloud.notebooks.v1.Execution.StateB\x03\xe0A\x03\x12\x1c\n\x14output_notebook_file\x18\x08 \x01(\t\x12\x14\n\x07job_uri\x18\t \x01(\tB\x03\xe0A\x03"\x9f\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\r\n\tPREPARING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\n\n\x06FAILED\x10\x05\x12\x0e\n\nCANCELLING\x10\x06\x12\r\n\tCANCELLED\x10\x07\x12\x0b\n\x07EXPIRED\x10\t\x12\x10\n\x0cINITIALIZING\x10\n:f\xeaAc\n"notebooks.googleapis.com/Execution\x12=projects/{project}/location/{location}/executions/{execution}B\xdc\x01\n\x1dcom.google.cloud.notebooks.v1B\x0eExecutionProtoP\x01Z;cloud.google.com/go/notebooks/apiv1/notebookspb;notebookspb\xeaAk\n%aiplatform.googleapis.com/Tensorboard\x12Bprojects/{project}/locations/{location}/tensorboards/{tensorboard}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v1.execution_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.notebooks.v1B\x0eExecutionProtoP\x01Z;cloud.google.com/go/notebooks/apiv1/notebookspb;notebookspb\xeaAk\n%aiplatform.googleapis.com/Tensorboard\x12Bprojects/{project}/locations/{location}/tensorboards/{tensorboard}'
    _globals['_EXECUTIONTEMPLATE_VERTEXAIPARAMETERS_ENVENTRY']._loaded_options = None
    _globals['_EXECUTIONTEMPLATE_VERTEXAIPARAMETERS_ENVENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTIONTEMPLATE_LABELSENTRY']._loaded_options = None
    _globals['_EXECUTIONTEMPLATE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTIONTEMPLATE'].fields_by_name['scale_tier']._loaded_options = None
    _globals['_EXECUTIONTEMPLATE'].fields_by_name['scale_tier']._serialized_options = b'\x18\x01\xe0A\x02'
    _globals['_EXECUTIONTEMPLATE'].fields_by_name['tensorboard']._loaded_options = None
    _globals['_EXECUTIONTEMPLATE'].fields_by_name['tensorboard']._serialized_options = b"\xfaA'\n%aiplatform.googleapis.com/Tensorboard"
    _globals['_EXECUTION'].fields_by_name['name']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['display_name']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['create_time']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['update_time']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['state']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION'].fields_by_name['job_uri']._loaded_options = None
    _globals['_EXECUTION'].fields_by_name['job_uri']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTION']._loaded_options = None
    _globals['_EXECUTION']._serialized_options = b'\xeaAc\n"notebooks.googleapis.com/Execution\x12=projects/{project}/location/{location}/executions/{execution}'
    _globals['_EXECUTIONTEMPLATE']._serialized_start = 166
    _globals['_EXECUTIONTEMPLATE']._serialized_end = 1808
    _globals['_EXECUTIONTEMPLATE_SCHEDULERACCELERATORCONFIG']._serialized_start = 979
    _globals['_EXECUTIONTEMPLATE_SCHEDULERACCELERATORCONFIG']._serialized_end = 1112
    _globals['_EXECUTIONTEMPLATE_DATAPROCPARAMETERS']._serialized_start = 1114
    _globals['_EXECUTIONTEMPLATE_DATAPROCPARAMETERS']._serialized_end = 1151
    _globals['_EXECUTIONTEMPLATE_VERTEXAIPARAMETERS']._serialized_start = 1154
    _globals['_EXECUTIONTEMPLATE_VERTEXAIPARAMETERS']._serialized_end = 1322
    _globals['_EXECUTIONTEMPLATE_VERTEXAIPARAMETERS_ENVENTRY']._serialized_start = 1280
    _globals['_EXECUTIONTEMPLATE_VERTEXAIPARAMETERS_ENVENTRY']._serialized_end = 1322
    _globals['_EXECUTIONTEMPLATE_LABELSENTRY']._serialized_start = 1324
    _globals['_EXECUTIONTEMPLATE_LABELSENTRY']._serialized_end = 1369
    _globals['_EXECUTIONTEMPLATE_SCALETIER']._serialized_start = 1371
    _globals['_EXECUTIONTEMPLATE_SCALETIER']._serialized_end = 1494
    _globals['_EXECUTIONTEMPLATE_SCHEDULERACCELERATORTYPE']._serialized_start = 1497
    _globals['_EXECUTIONTEMPLATE_SCHEDULERACCELERATORTYPE']._serialized_end = 1724
    _globals['_EXECUTIONTEMPLATE_JOBTYPE']._serialized_start = 1726
    _globals['_EXECUTIONTEMPLATE_JOBTYPE']._serialized_end = 1790
    _globals['_EXECUTION']._serialized_start = 1811
    _globals['_EXECUTION']._serialized_end = 2453
    _globals['_EXECUTION_STATE']._serialized_start = 2190
    _globals['_EXECUTION_STATE']._serialized_end = 2349