"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/notebook_execution_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_job__state__pb2
from .....google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1beta1 import network_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_network__spec__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/aiplatform/v1beta1/notebook_execution_job.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a/google/cloud/aiplatform/v1beta1/job_state.proto\x1a7google/cloud/aiplatform/v1beta1/machine_resources.proto\x1a2google/cloud/aiplatform/v1beta1/network_spec.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xba\x10\n\x14NotebookExecutionJob\x12t\n\x1adataform_repository_source\x18\x03 \x01(\x0b2N.google.cloud.aiplatform.v1beta1.NotebookExecutionJob.DataformRepositorySourceH\x00\x12f\n\x13gcs_notebook_source\x18\x04 \x01(\x0b2G.google.cloud.aiplatform.v1beta1.NotebookExecutionJob.GcsNotebookSourceH\x00\x12l\n\x16direct_notebook_source\x18\x11 \x01(\x0b2J.google.cloud.aiplatform.v1beta1.NotebookExecutionJob.DirectNotebookSourceH\x00\x12i\n\'notebook_runtime_template_resource_name\x18\x0e \x01(\tB6\xfaA3\n1aiplatform.googleapis.com/NotebookRuntimeTemplateH\x01\x12n\n\x17custom_environment_spec\x18\x10 \x01(\x0b2K.google.cloud.aiplatform.v1beta1.NotebookExecutionJob.CustomEnvironmentSpecH\x01\x12\x18\n\x0egcs_output_uri\x18\x08 \x01(\tH\x02\x12\x18\n\x0eexecution_user\x18\t \x01(\tH\x03\x12\x19\n\x0fservice_account\x18\x12 \x01(\tH\x03\x12c\n\x11workbench_runtime\x18\x17 \x01(\x0b2F.google.cloud.aiplatform.v1beta1.NotebookExecutionJob.WorkbenchRuntimeH\x04\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x124\n\x11execution_timeout\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12J\n\x16schedule_resource_name\x18\x06 \x01(\tB*\xe0A\x03\xfaA$\n"aiplatform.googleapis.com/Schedule\x12A\n\tjob_state\x18\n \x01(\x0e2).google.cloud.aiplatform.v1beta1.JobStateB\x03\xe0A\x03\x12\'\n\x06status\x18\x0b \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Q\n\x06labels\x18\x13 \x03(\x0b2A.google.cloud.aiplatform.v1beta1.NotebookExecutionJob.LabelsEntry\x12\x13\n\x0bkernel_name\x18\x14 \x01(\t\x12H\n\x0fencryption_spec\x18\x16 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x1aY\n\x18DataformRepositorySource\x12)\n!dataform_repository_resource_name\x18\x01 \x01(\t\x12\x12\n\ncommit_sha\x18\x02 \x01(\t\x1a4\n\x11GcsNotebookSource\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x12\n\ngeneration\x18\x02 \x01(\t\x1a\'\n\x14DirectNotebookSource\x12\x0f\n\x07content\x18\x01 \x01(\x0c\x1a\xf2\x01\n\x15CustomEnvironmentSpec\x12B\n\x0cmachine_spec\x18\x01 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.MachineSpec\x12Q\n\x14persistent_disk_spec\x18\x02 \x01(\x0b23.google.cloud.aiplatform.v1beta1.PersistentDiskSpec\x12B\n\x0cnetwork_spec\x18\x03 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.NetworkSpec\x1a\x12\n\x10WorkbenchRuntime\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xb9\x01\xeaA\xb5\x01\n.aiplatform.googleapis.com/NotebookExecutionJob\x12Vprojects/{project}/locations/{location}/notebookExecutionJobs/{notebook_execution_job}*\x15notebookExecutionJobs2\x14notebookExecutionJobB\x11\n\x0fnotebook_sourceB\x12\n\x10environment_specB\x10\n\x0eexecution_sinkB\x14\n\x12execution_identityB\x15\n\x13runtime_environmentB\xf0\x01\n#com.google.cloud.aiplatform.v1beta1B\x19NotebookExecutionJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.notebook_execution_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x19NotebookExecutionJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_NOTEBOOKEXECUTIONJOB_LABELSENTRY']._loaded_options = None
    _globals['_NOTEBOOKEXECUTIONJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['notebook_runtime_template_resource_name']._loaded_options = None
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['notebook_runtime_template_resource_name']._serialized_options = b'\xfaA3\n1aiplatform.googleapis.com/NotebookRuntimeTemplate'
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['name']._loaded_options = None
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['schedule_resource_name']._loaded_options = None
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['schedule_resource_name']._serialized_options = b'\xe0A\x03\xfaA$\n"aiplatform.googleapis.com/Schedule'
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['job_state']._loaded_options = None
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['job_state']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['status']._loaded_options = None
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_NOTEBOOKEXECUTIONJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKEXECUTIONJOB']._loaded_options = None
    _globals['_NOTEBOOKEXECUTIONJOB']._serialized_options = b'\xeaA\xb5\x01\n.aiplatform.googleapis.com/NotebookExecutionJob\x12Vprojects/{project}/locations/{location}/notebookExecutionJobs/{notebook_execution_job}*\x15notebookExecutionJobs2\x14notebookExecutionJob'
    _globals['_NOTEBOOKEXECUTIONJOB']._serialized_start = 461
    _globals['_NOTEBOOKEXECUTIONJOB']._serialized_end = 2567
    _globals['_NOTEBOOKEXECUTIONJOB_DATAFORMREPOSITORYSOURCE']._serialized_start = 1781
    _globals['_NOTEBOOKEXECUTIONJOB_DATAFORMREPOSITORYSOURCE']._serialized_end = 1870
    _globals['_NOTEBOOKEXECUTIONJOB_GCSNOTEBOOKSOURCE']._serialized_start = 1872
    _globals['_NOTEBOOKEXECUTIONJOB_GCSNOTEBOOKSOURCE']._serialized_end = 1924
    _globals['_NOTEBOOKEXECUTIONJOB_DIRECTNOTEBOOKSOURCE']._serialized_start = 1926
    _globals['_NOTEBOOKEXECUTIONJOB_DIRECTNOTEBOOKSOURCE']._serialized_end = 1965
    _globals['_NOTEBOOKEXECUTIONJOB_CUSTOMENVIRONMENTSPEC']._serialized_start = 1968
    _globals['_NOTEBOOKEXECUTIONJOB_CUSTOMENVIRONMENTSPEC']._serialized_end = 2210
    _globals['_NOTEBOOKEXECUTIONJOB_WORKBENCHRUNTIME']._serialized_start = 2212
    _globals['_NOTEBOOKEXECUTIONJOB_WORKBENCHRUNTIME']._serialized_end = 2230
    _globals['_NOTEBOOKEXECUTIONJOB_LABELSENTRY']._serialized_start = 2232
    _globals['_NOTEBOOKEXECUTIONJOB_LABELSENTRY']._serialized_end = 2277