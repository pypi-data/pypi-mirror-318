"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/pipeline_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import artifact_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_artifact__pb2
from .....google.cloud.aiplatform.v1beta1 import context_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_context__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import execution_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_execution__pb2
from .....google.cloud.aiplatform.v1beta1 import pipeline_failure_policy_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_pipeline__failure__policy__pb2
from .....google.cloud.aiplatform.v1beta1 import pipeline_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_pipeline__state__pb2
from .....google.cloud.aiplatform.v1beta1 import service_networking_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_service__networking__pb2
from .....google.cloud.aiplatform.v1beta1 import ui_pipeline_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_ui__pipeline__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import value_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_value__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/aiplatform/v1beta1/pipeline_job.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/aiplatform/v1beta1/artifact.proto\x1a-google/cloud/aiplatform/v1beta1/context.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a/google/cloud/aiplatform/v1beta1/execution.proto\x1a=google/cloud/aiplatform/v1beta1/pipeline_failure_policy.proto\x1a4google/cloud/aiplatform/v1beta1/pipeline_state.proto\x1a8google/cloud/aiplatform/v1beta1/service_networking.proto\x1a6google/cloud/aiplatform/v1beta1/ui_pipeline_spec.proto\x1a+google/cloud/aiplatform/v1beta1/value.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xa0\x17\n\x0bPipelineJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12.\n\rpipeline_spec\x18\x07 \x01(\x0b2\x17.google.protobuf.Struct\x12B\n\x05state\x18\x08 \x01(\x0e2..google.cloud.aiplatform.v1beta1.PipelineStateB\x03\xe0A\x03\x12K\n\njob_detail\x18\t \x01(\x0b22.google.cloud.aiplatform.v1beta1.PipelineJobDetailB\x03\xe0A\x03\x12&\n\x05error\x18\n \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12H\n\x06labels\x18\x0b \x03(\x0b28.google.cloud.aiplatform.v1beta1.PipelineJob.LabelsEntry\x12R\n\x0eruntime_config\x18\x0c \x01(\x0b2:.google.cloud.aiplatform.v1beta1.PipelineJob.RuntimeConfig\x12H\n\x0fencryption_spec\x18\x10 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x12\x17\n\x0fservice_account\x18\x11 \x01(\t\x124\n\x07network\x18\x12 \x01(\tB#\xfaA \n\x1ecompute.googleapis.com/Network\x12\x1a\n\x12reserved_ip_ranges\x18\x19 \x03(\t\x12V\n\x14psc_interface_config\x18\x1f \x01(\x0b23.google.cloud.aiplatform.v1beta1.PscInterfaceConfigB\x03\xe0A\x01\x12\x14\n\x0ctemplate_uri\x18\x13 \x01(\t\x12Y\n\x11template_metadata\x18\x14 \x01(\x0b29.google.cloud.aiplatform.v1beta1.PipelineTemplateMetadataB\x03\xe0A\x03\x12\x1a\n\rschedule_name\x18\x16 \x01(\tB\x03\xe0A\x03\x12"\n\x15preflight_validations\x18\x1a \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\x1b \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x1c \x01(\x08B\x03\xe0A\x03\x12%\n\x18original_pipeline_job_id\x18\x1d \x01(\x03B\x03\xe0A\x01\x12b\n\x1bpipeline_task_rerun_configs\x18\x1e \x03(\x0b28.google.cloud.aiplatform.v1beta1.PipelineTaskRerunConfigB\x03\xe0A\x01\x1a\xeb\x0b\n\rRuntimeConfig\x12b\n\nparameters\x18\x01 \x03(\x0b2J.google.cloud.aiplatform.v1beta1.PipelineJob.RuntimeConfig.ParametersEntryB\x02\x18\x01\x12!\n\x14gcs_output_directory\x18\x02 \x01(\tB\x03\xe0A\x02\x12i\n\x10parameter_values\x18\x03 \x03(\x0b2O.google.cloud.aiplatform.v1beta1.PipelineJob.RuntimeConfig.ParameterValuesEntry\x12N\n\x0efailure_policy\x18\x04 \x01(\x0e26.google.cloud.aiplatform.v1beta1.PipelineFailurePolicy\x12g\n\x0finput_artifacts\x18\x05 \x03(\x0b2N.google.cloud.aiplatform.v1beta1.PipelineJob.RuntimeConfig.InputArtifactsEntry\x12g\n\x0fdefault_runtime\x18\x06 \x01(\x0b2I.google.cloud.aiplatform.v1beta1.PipelineJob.RuntimeConfig.DefaultRuntimeB\x03\xe0A\x01\x1a.\n\rInputArtifact\x12\x15\n\x0bartifact_id\x18\x01 \x01(\tH\x00B\x06\n\x04kind\x1a\xb9\x03\n\x1fPersistentResourceRuntimeDetail\x12 \n\x18persistent_resource_name\x18\x01 \x01(\t\x12.\n&task_resource_unavailable_wait_time_ms\x18\x02 \x01(\x03\x12\xb6\x01\n*task_resource_unavailable_timeout_behavior\x18\x03 \x01(\x0e2\x81\x01.google.cloud.aiplatform.v1beta1.PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail.TaskResourceUnavailableTimeoutBehavior"\x8a\x01\n&TaskResourceUnavailableTimeoutBehavior\x12:\n6TASK_RESOURCE_UNAVAILABLE_TIMEOUT_BEHAVIOR_UNSPECIFIED\x10\x00\x12\x08\n\x04FAIL\x10\x01\x12\x1a\n\x16FALL_BACK_TO_ON_DEMAND\x10\x02\x1a\xad\x01\n\x0eDefaultRuntime\x12\x88\x01\n"persistent_resource_runtime_detail\x18\x01 \x01(\x0b2Z.google.cloud.aiplatform.v1beta1.PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetailH\x00B\x10\n\x0eruntime_detail\x1aY\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.Value:\x028\x01\x1aN\n\x14ParameterValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01\x1a\x7f\n\x13InputArtifactsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12W\n\x05value\x18\x02 \x01(\x0b2H.google.cloud.aiplatform.v1beta1.PipelineJob.RuntimeConfig.InputArtifact:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:o\xeaAl\n%aiplatform.googleapis.com/PipelineJob\x12Cprojects/{project}/locations/{location}/pipelineJobs/{pipeline_job}"+\n\x18PipelineTemplateMetadata\x12\x0f\n\x07version\x18\x03 \x01(\t"\xf9\x01\n\x11PipelineJobDetail\x12G\n\x10pipeline_context\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.ContextB\x03\xe0A\x03\x12K\n\x14pipeline_run_context\x18\x02 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.ContextB\x03\xe0A\x03\x12N\n\x0ctask_details\x18\x03 \x03(\x0b23.google.cloud.aiplatform.v1beta1.PipelineTaskDetailB\x03\xe0A\x03"\xcf\x0b\n\x12PipelineTaskDetail\x12\x14\n\x07task_id\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x1b\n\x0eparent_task_id\x18\x0c \x01(\x03B\x03\xe0A\x03\x12\x16\n\ttask_name\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Y\n\x0fexecutor_detail\x18\x06 \x01(\x0b2;.google.cloud.aiplatform.v1beta1.PipelineTaskExecutorDetailB\x03\xe0A\x03\x12M\n\x05state\x18\x07 \x01(\x0e29.google.cloud.aiplatform.v1beta1.PipelineTaskDetail.StateB\x03\xe0A\x03\x12B\n\texecution\x18\x08 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.ExecutionB\x03\xe0A\x03\x12&\n\x05error\x18\t \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12i\n\x14pipeline_task_status\x18\r \x03(\x0b2F.google.cloud.aiplatform.v1beta1.PipelineTaskDetail.PipelineTaskStatusB\x03\xe0A\x03\x12T\n\x06inputs\x18\n \x03(\x0b2?.google.cloud.aiplatform.v1beta1.PipelineTaskDetail.InputsEntryB\x03\xe0A\x03\x12V\n\x07outputs\x18\x0b \x03(\x0b2@.google.cloud.aiplatform.v1beta1.PipelineTaskDetail.OutputsEntryB\x03\xe0A\x03\x1a\xc1\x01\n\x12PipelineTaskStatus\x124\n\x0bupdate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12M\n\x05state\x18\x02 \x01(\x0e29.google.cloud.aiplatform.v1beta1.PipelineTaskDetail.StateB\x03\xe0A\x03\x12&\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x1aQ\n\x0cArtifactList\x12A\n\tartifacts\x18\x01 \x03(\x0b2).google.cloud.aiplatform.v1beta1.ArtifactB\x03\xe0A\x03\x1ao\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12O\n\x05value\x18\x02 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.PipelineTaskDetail.ArtifactList:\x028\x01\x1ap\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12O\n\x05value\x18\x02 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.PipelineTaskDetail.ArtifactList:\x028\x01"\xa6\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\x12\n\x0eCANCEL_PENDING\x10\x04\x12\x0e\n\nCANCELLING\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\n\n\x06FAILED\x10\x07\x12\x0b\n\x07SKIPPED\x10\x08\x12\x11\n\rNOT_TRIGGERED\x10\t"\xd5\x04\n\x1aPipelineTaskExecutorDetail\x12l\n\x10container_detail\x18\x01 \x01(\x0b2K.google.cloud.aiplatform.v1beta1.PipelineTaskExecutorDetail.ContainerDetailB\x03\xe0A\x03H\x00\x12m\n\x11custom_job_detail\x18\x02 \x01(\x0b2K.google.cloud.aiplatform.v1beta1.PipelineTaskExecutorDetail.CustomJobDetailB\x03\xe0A\x03H\x00\x1a\xe7\x01\n\x0fContainerDetail\x12=\n\x08main_job\x18\x01 \x01(\tB+\xe0A\x03\xfaA%\n#aiplatform.googleapis.com/CustomJob\x12J\n\x15pre_caching_check_job\x18\x02 \x01(\tB+\xe0A\x03\xfaA%\n#aiplatform.googleapis.com/CustomJob\x12\x1d\n\x10failed_main_jobs\x18\x03 \x03(\tB\x03\xe0A\x03\x12*\n\x1dfailed_pre_caching_check_jobs\x18\x04 \x03(\tB\x03\xe0A\x03\x1ae\n\x0fCustomJobDetail\x128\n\x03job\x18\x01 \x01(\tB+\xe0A\x03\xfaA%\n#aiplatform.googleapis.com/CustomJob\x12\x18\n\x0bfailed_jobs\x18\x03 \x03(\tB\x03\xe0A\x03B\t\n\x07details"\xe4\x05\n\x17PipelineTaskRerunConfig\x12\x14\n\x07task_id\x18\x01 \x01(\x03B\x03\xe0A\x01\x12\x16\n\ttask_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12T\n\x06inputs\x18\x03 \x01(\x0b2?.google.cloud.aiplatform.v1beta1.PipelineTaskRerunConfig.InputsB\x03\xe0A\x01\x12\x16\n\tskip_task\x18\x04 \x01(\x08B\x03\xe0A\x01\x12"\n\x15skip_downstream_tasks\x18\x05 \x01(\x08B\x03\xe0A\x01\x1aX\n\x0cArtifactList\x12H\n\tartifacts\x18\x01 \x03(\x0b20.google.cloud.aiplatform.v1beta1.RuntimeArtifactB\x03\xe0A\x01\x1a\xae\x03\n\x06Inputs\x12f\n\tartifacts\x18\x01 \x03(\x0b2N.google.cloud.aiplatform.v1beta1.PipelineTaskRerunConfig.Inputs.ArtifactsEntryB\x03\xe0A\x01\x12s\n\x10parameter_values\x18\x02 \x03(\x0b2T.google.cloud.aiplatform.v1beta1.PipelineTaskRerunConfig.Inputs.ParameterValuesEntryB\x03\xe0A\x01\x1aw\n\x0eArtifactsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12T\n\x05value\x18\x02 \x01(\x0b2E.google.cloud.aiplatform.v1beta1.PipelineTaskRerunConfig.ArtifactList:\x028\x01\x1aN\n\x14ParameterValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01B\xb0\x02\n#com.google.cloud.aiplatform.v1beta1B\x08PipelineP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.pipeline_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x08PipelineP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}'
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY']._loaded_options = None
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY']._loaded_options = None
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINEJOB_RUNTIMECONFIG_INPUTARTIFACTSENTRY']._loaded_options = None
    _globals['_PIPELINEJOB_RUNTIMECONFIG_INPUTARTIFACTSENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINEJOB_RUNTIMECONFIG'].fields_by_name['parameters']._loaded_options = None
    _globals['_PIPELINEJOB_RUNTIMECONFIG'].fields_by_name['parameters']._serialized_options = b'\x18\x01'
    _globals['_PIPELINEJOB_RUNTIMECONFIG'].fields_by_name['gcs_output_directory']._loaded_options = None
    _globals['_PIPELINEJOB_RUNTIMECONFIG'].fields_by_name['gcs_output_directory']._serialized_options = b'\xe0A\x02'
    _globals['_PIPELINEJOB_RUNTIMECONFIG'].fields_by_name['default_runtime']._loaded_options = None
    _globals['_PIPELINEJOB_RUNTIMECONFIG'].fields_by_name['default_runtime']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINEJOB_LABELSENTRY']._loaded_options = None
    _globals['_PIPELINEJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINEJOB'].fields_by_name['name']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['start_time']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['end_time']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['state']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['job_detail']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['job_detail']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['error']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['network']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['network']._serialized_options = b'\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_PIPELINEJOB'].fields_by_name['psc_interface_config']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['psc_interface_config']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINEJOB'].fields_by_name['template_metadata']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['template_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['schedule_name']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['schedule_name']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['preflight_validations']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['preflight_validations']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINEJOB'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOB'].fields_by_name['original_pipeline_job_id']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['original_pipeline_job_id']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINEJOB'].fields_by_name['pipeline_task_rerun_configs']._loaded_options = None
    _globals['_PIPELINEJOB'].fields_by_name['pipeline_task_rerun_configs']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINEJOB']._loaded_options = None
    _globals['_PIPELINEJOB']._serialized_options = b'\xeaAl\n%aiplatform.googleapis.com/PipelineJob\x12Cprojects/{project}/locations/{location}/pipelineJobs/{pipeline_job}'
    _globals['_PIPELINEJOBDETAIL'].fields_by_name['pipeline_context']._loaded_options = None
    _globals['_PIPELINEJOBDETAIL'].fields_by_name['pipeline_context']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOBDETAIL'].fields_by_name['pipeline_run_context']._loaded_options = None
    _globals['_PIPELINEJOBDETAIL'].fields_by_name['pipeline_run_context']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINEJOBDETAIL'].fields_by_name['task_details']._loaded_options = None
    _globals['_PIPELINEJOBDETAIL'].fields_by_name['task_details']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL_PIPELINETASKSTATUS'].fields_by_name['update_time']._loaded_options = None
    _globals['_PIPELINETASKDETAIL_PIPELINETASKSTATUS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL_PIPELINETASKSTATUS'].fields_by_name['state']._loaded_options = None
    _globals['_PIPELINETASKDETAIL_PIPELINETASKSTATUS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL_PIPELINETASKSTATUS'].fields_by_name['error']._loaded_options = None
    _globals['_PIPELINETASKDETAIL_PIPELINETASKSTATUS'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL_ARTIFACTLIST'].fields_by_name['artifacts']._loaded_options = None
    _globals['_PIPELINETASKDETAIL_ARTIFACTLIST'].fields_by_name['artifacts']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL_INPUTSENTRY']._loaded_options = None
    _globals['_PIPELINETASKDETAIL_INPUTSENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINETASKDETAIL_OUTPUTSENTRY']._loaded_options = None
    _globals['_PIPELINETASKDETAIL_OUTPUTSENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['task_id']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['task_id']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['parent_task_id']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['parent_task_id']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['task_name']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['task_name']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['create_time']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['start_time']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['end_time']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['executor_detail']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['executor_detail']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['state']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['execution']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['execution']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['error']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['pipeline_task_status']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['pipeline_task_status']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['inputs']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['inputs']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKDETAIL'].fields_by_name['outputs']._loaded_options = None
    _globals['_PIPELINETASKDETAIL'].fields_by_name['outputs']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL'].fields_by_name['main_job']._loaded_options = None
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL'].fields_by_name['main_job']._serialized_options = b'\xe0A\x03\xfaA%\n#aiplatform.googleapis.com/CustomJob'
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL'].fields_by_name['pre_caching_check_job']._loaded_options = None
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL'].fields_by_name['pre_caching_check_job']._serialized_options = b'\xe0A\x03\xfaA%\n#aiplatform.googleapis.com/CustomJob'
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL'].fields_by_name['failed_main_jobs']._loaded_options = None
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL'].fields_by_name['failed_main_jobs']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL'].fields_by_name['failed_pre_caching_check_jobs']._loaded_options = None
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL'].fields_by_name['failed_pre_caching_check_jobs']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL'].fields_by_name['job']._loaded_options = None
    _globals['_PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL'].fields_by_name['job']._serialized_options = b'\xe0A\x03\xfaA%\n#aiplatform.googleapis.com/CustomJob'
    _globals['_PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL'].fields_by_name['failed_jobs']._loaded_options = None
    _globals['_PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL'].fields_by_name['failed_jobs']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKEXECUTORDETAIL'].fields_by_name['container_detail']._loaded_options = None
    _globals['_PIPELINETASKEXECUTORDETAIL'].fields_by_name['container_detail']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKEXECUTORDETAIL'].fields_by_name['custom_job_detail']._loaded_options = None
    _globals['_PIPELINETASKEXECUTORDETAIL'].fields_by_name['custom_job_detail']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINETASKRERUNCONFIG_ARTIFACTLIST'].fields_by_name['artifacts']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG_ARTIFACTLIST'].fields_by_name['artifacts']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS_ARTIFACTSENTRY']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS_ARTIFACTSENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS_PARAMETERVALUESENTRY']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS_PARAMETERVALUESENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS'].fields_by_name['artifacts']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS'].fields_by_name['artifacts']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS'].fields_by_name['parameter_values']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS'].fields_by_name['parameter_values']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['task_id']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['task_id']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['task_name']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['task_name']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['inputs']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['inputs']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['skip_task']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['skip_task']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['skip_downstream_tasks']._loaded_options = None
    _globals['_PIPELINETASKRERUNCONFIG'].fields_by_name['skip_downstream_tasks']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINEJOB']._serialized_start = 711
    _globals['_PIPELINEJOB']._serialized_end = 3687
    _globals['_PIPELINEJOB_RUNTIMECONFIG']._serialized_start = 2012
    _globals['_PIPELINEJOB_RUNTIMECONFIG']._serialized_end = 3527
    _globals['_PIPELINEJOB_RUNTIMECONFIG_INPUTARTIFACT']._serialized_start = 2561
    _globals['_PIPELINEJOB_RUNTIMECONFIG_INPUTARTIFACT']._serialized_end = 2607
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PERSISTENTRESOURCERUNTIMEDETAIL']._serialized_start = 2610
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PERSISTENTRESOURCERUNTIMEDETAIL']._serialized_end = 3051
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PERSISTENTRESOURCERUNTIMEDETAIL_TASKRESOURCEUNAVAILABLETIMEOUTBEHAVIOR']._serialized_start = 2913
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PERSISTENTRESOURCERUNTIMEDETAIL_TASKRESOURCEUNAVAILABLETIMEOUTBEHAVIOR']._serialized_end = 3051
    _globals['_PIPELINEJOB_RUNTIMECONFIG_DEFAULTRUNTIME']._serialized_start = 3054
    _globals['_PIPELINEJOB_RUNTIMECONFIG_DEFAULTRUNTIME']._serialized_end = 3227
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY']._serialized_start = 3229
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY']._serialized_end = 3318
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY']._serialized_start = 3320
    _globals['_PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY']._serialized_end = 3398
    _globals['_PIPELINEJOB_RUNTIMECONFIG_INPUTARTIFACTSENTRY']._serialized_start = 3400
    _globals['_PIPELINEJOB_RUNTIMECONFIG_INPUTARTIFACTSENTRY']._serialized_end = 3527
    _globals['_PIPELINEJOB_LABELSENTRY']._serialized_start = 3529
    _globals['_PIPELINEJOB_LABELSENTRY']._serialized_end = 3574
    _globals['_PIPELINETEMPLATEMETADATA']._serialized_start = 3689
    _globals['_PIPELINETEMPLATEMETADATA']._serialized_end = 3732
    _globals['_PIPELINEJOBDETAIL']._serialized_start = 3735
    _globals['_PIPELINEJOBDETAIL']._serialized_end = 3984
    _globals['_PIPELINETASKDETAIL']._serialized_start = 3987
    _globals['_PIPELINETASKDETAIL']._serialized_end = 5474
    _globals['_PIPELINETASKDETAIL_PIPELINETASKSTATUS']._serialized_start = 4802
    _globals['_PIPELINETASKDETAIL_PIPELINETASKSTATUS']._serialized_end = 4995
    _globals['_PIPELINETASKDETAIL_ARTIFACTLIST']._serialized_start = 4997
    _globals['_PIPELINETASKDETAIL_ARTIFACTLIST']._serialized_end = 5078
    _globals['_PIPELINETASKDETAIL_INPUTSENTRY']._serialized_start = 5080
    _globals['_PIPELINETASKDETAIL_INPUTSENTRY']._serialized_end = 5191
    _globals['_PIPELINETASKDETAIL_OUTPUTSENTRY']._serialized_start = 5193
    _globals['_PIPELINETASKDETAIL_OUTPUTSENTRY']._serialized_end = 5305
    _globals['_PIPELINETASKDETAIL_STATE']._serialized_start = 5308
    _globals['_PIPELINETASKDETAIL_STATE']._serialized_end = 5474
    _globals['_PIPELINETASKEXECUTORDETAIL']._serialized_start = 5477
    _globals['_PIPELINETASKEXECUTORDETAIL']._serialized_end = 6074
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL']._serialized_start = 5729
    _globals['_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL']._serialized_end = 5960
    _globals['_PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL']._serialized_start = 5962
    _globals['_PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL']._serialized_end = 6063
    _globals['_PIPELINETASKRERUNCONFIG']._serialized_start = 6077
    _globals['_PIPELINETASKRERUNCONFIG']._serialized_end = 6817
    _globals['_PIPELINETASKRERUNCONFIG_ARTIFACTLIST']._serialized_start = 6296
    _globals['_PIPELINETASKRERUNCONFIG_ARTIFACTLIST']._serialized_end = 6384
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS']._serialized_start = 6387
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS']._serialized_end = 6817
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS_ARTIFACTSENTRY']._serialized_start = 6618
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS_ARTIFACTSENTRY']._serialized_end = 6737
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS_PARAMETERVALUESENTRY']._serialized_start = 3320
    _globals['_PIPELINETASKRERUNCONFIG_INPUTS_PARAMETERVALUESENTRY']._serialized_end = 3398