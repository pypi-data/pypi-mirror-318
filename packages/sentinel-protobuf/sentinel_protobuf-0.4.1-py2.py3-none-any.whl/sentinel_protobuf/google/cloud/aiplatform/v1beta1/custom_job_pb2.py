"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/custom_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import env_var_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_env__var__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from .....google.cloud.aiplatform.v1beta1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_job__state__pb2
from .....google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1beta1 import service_networking_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_service__networking__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/aiplatform/v1beta1/custom_job.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a-google/cloud/aiplatform/v1beta1/env_var.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a/google/cloud/aiplatform/v1beta1/job_state.proto\x1a7google/cloud/aiplatform/v1beta1/machine_resources.proto\x1a8google/cloud/aiplatform/v1beta1/service_networking.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xb2\x07\n\tCustomJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12E\n\x08job_spec\x18\x04 \x01(\x0b2..google.cloud.aiplatform.v1beta1.CustomJobSpecB\x03\xe0A\x02\x12=\n\x05state\x18\x05 \x01(\x0e2).google.cloud.aiplatform.v1beta1.JobStateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12&\n\x05error\x18\n \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12F\n\x06labels\x18\x0b \x03(\x0b26.google.cloud.aiplatform.v1beta1.CustomJob.LabelsEntry\x12H\n\x0fencryption_spec\x18\x0c \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x12[\n\x0fweb_access_uris\x18\x10 \x03(\x0b2=.google.cloud.aiplatform.v1beta1.CustomJob.WebAccessUrisEntryB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x12 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x13 \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a4\n\x12WebAccessUrisEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:i\xeaAf\n#aiplatform.googleapis.com/CustomJob\x12?projects/{project}/locations/{location}/customJobs/{custom_job}"\xff\x06\n\rCustomJobSpec\x12T\n\x16persistent_resource_id\x18\x0e \x01(\tB4\xe0A\x01\xfaA.\n,aiplatform.googleapis.com/PersistentResource\x12O\n\x11worker_pool_specs\x18\x01 \x03(\x0b2/.google.cloud.aiplatform.v1beta1.WorkerPoolSpecB\x03\xe0A\x02\x12?\n\nscheduling\x18\x03 \x01(\x0b2+.google.cloud.aiplatform.v1beta1.Scheduling\x12\x17\n\x0fservice_account\x18\x04 \x01(\t\x127\n\x07network\x18\x05 \x01(\tB&\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network\x12\x1f\n\x12reserved_ip_ranges\x18\r \x03(\tB\x03\xe0A\x01\x12V\n\x14psc_interface_config\x18\x15 \x01(\x0b23.google.cloud.aiplatform.v1beta1.PscInterfaceConfigB\x03\xe0A\x01\x12N\n\x15base_output_directory\x18\x06 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.GcsDestination\x12&\n\x1eprotected_artifact_location_id\x18\x13 \x01(\t\x12B\n\x0btensorboard\x18\x07 \x01(\tB-\xe0A\x01\xfaA\'\n%aiplatform.googleapis.com/Tensorboard\x12\x1e\n\x11enable_web_access\x18\n \x01(\x08B\x03\xe0A\x01\x12$\n\x17enable_dashboard_access\x18\x10 \x01(\x08B\x03\xe0A\x01\x12=\n\nexperiment\x18\x11 \x01(\tB)\xe0A\x01\xfaA#\n!aiplatform.googleapis.com/Context\x12A\n\x0eexperiment_run\x18\x12 \x01(\tB)\xe0A\x01\xfaA#\n!aiplatform.googleapis.com/Context\x127\n\x06models\x18\x14 \x03(\tB\'\xe0A\x01\xfaA!\n\x1faiplatform.googleapis.com/Model"\x9f\x03\n\x0eWorkerPoolSpec\x12H\n\x0econtainer_spec\x18\x06 \x01(\x0b2..google.cloud.aiplatform.v1beta1.ContainerSpecH\x00\x12Q\n\x13python_package_spec\x18\x07 \x01(\x0b22.google.cloud.aiplatform.v1beta1.PythonPackageSpecH\x00\x12J\n\x0cmachine_spec\x18\x01 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.MachineSpecB\x06\xe0A\x01\xe0A\x05\x12\x1a\n\rreplica_count\x18\x02 \x01(\x03B\x03\xe0A\x01\x12B\n\nnfs_mounts\x18\x04 \x03(\x0b2).google.cloud.aiplatform.v1beta1.NfsMountB\x03\xe0A\x01\x12<\n\tdisk_spec\x18\x05 \x01(\x0b2).google.cloud.aiplatform.v1beta1.DiskSpecB\x06\n\x04task"|\n\rContainerSpec\x12\x16\n\timage_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0f\n\x07command\x18\x02 \x03(\t\x12\x0c\n\x04args\x18\x03 \x03(\t\x124\n\x03env\x18\x04 \x03(\x0b2\'.google.cloud.aiplatform.v1beta1.EnvVar"\xaf\x01\n\x11PythonPackageSpec\x12\x1f\n\x12executor_image_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cpackage_uris\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x1a\n\rpython_module\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04args\x18\x04 \x03(\t\x124\n\x03env\x18\x05 \x03(\x0b2\'.google.cloud.aiplatform.v1beta1.EnvVar"\xf8\x02\n\nScheduling\x12*\n\x07timeout\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12%\n\x1drestart_job_on_worker_restart\x18\x03 \x01(\x08\x12K\n\x08strategy\x18\x04 \x01(\x0e24.google.cloud.aiplatform.v1beta1.Scheduling.StrategyB\x03\xe0A\x01\x12\x1c\n\x0fdisable_retries\x18\x05 \x01(\x08B\x03\xe0A\x01\x129\n\x11max_wait_duration\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01"q\n\x08Strategy\x12\x18\n\x14STRATEGY_UNSPECIFIED\x10\x00\x12\x11\n\tON_DEMAND\x10\x01\x1a\x02\x08\x01\x12\x10\n\x08LOW_COST\x10\x02\x1a\x02\x08\x01\x12\x0c\n\x08STANDARD\x10\x03\x12\x08\n\x04SPOT\x10\x04\x12\x0e\n\nFLEX_START\x10\x06B\xe5\x01\n#com.google.cloud.aiplatform.v1beta1B\x0eCustomJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.custom_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0eCustomJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CUSTOMJOB_LABELSENTRY']._loaded_options = None
    _globals['_CUSTOMJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CUSTOMJOB_WEBACCESSURISENTRY']._loaded_options = None
    _globals['_CUSTOMJOB_WEBACCESSURISENTRY']._serialized_options = b'8\x01'
    _globals['_CUSTOMJOB'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB'].fields_by_name['display_name']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMJOB'].fields_by_name['job_spec']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['job_spec']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMJOB'].fields_by_name['state']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB'].fields_by_name['start_time']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB'].fields_by_name['end_time']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB'].fields_by_name['error']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB'].fields_by_name['web_access_uris']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['web_access_uris']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_CUSTOMJOB'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMJOB']._loaded_options = None
    _globals['_CUSTOMJOB']._serialized_options = b'\xeaAf\n#aiplatform.googleapis.com/CustomJob\x12?projects/{project}/locations/{location}/customJobs/{custom_job}'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['persistent_resource_id']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['persistent_resource_id']._serialized_options = b'\xe0A\x01\xfaA.\n,aiplatform.googleapis.com/PersistentResource'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['worker_pool_specs']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['worker_pool_specs']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['network']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['network']._serialized_options = b'\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['reserved_ip_ranges']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['reserved_ip_ranges']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['psc_interface_config']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['psc_interface_config']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['tensorboard']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['tensorboard']._serialized_options = b"\xe0A\x01\xfaA'\n%aiplatform.googleapis.com/Tensorboard"
    _globals['_CUSTOMJOBSPEC'].fields_by_name['enable_web_access']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['enable_web_access']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['enable_dashboard_access']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['enable_dashboard_access']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['experiment']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['experiment']._serialized_options = b'\xe0A\x01\xfaA#\n!aiplatform.googleapis.com/Context'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['experiment_run']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['experiment_run']._serialized_options = b'\xe0A\x01\xfaA#\n!aiplatform.googleapis.com/Context'
    _globals['_CUSTOMJOBSPEC'].fields_by_name['models']._loaded_options = None
    _globals['_CUSTOMJOBSPEC'].fields_by_name['models']._serialized_options = b'\xe0A\x01\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_WORKERPOOLSPEC'].fields_by_name['machine_spec']._loaded_options = None
    _globals['_WORKERPOOLSPEC'].fields_by_name['machine_spec']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_WORKERPOOLSPEC'].fields_by_name['replica_count']._loaded_options = None
    _globals['_WORKERPOOLSPEC'].fields_by_name['replica_count']._serialized_options = b'\xe0A\x01'
    _globals['_WORKERPOOLSPEC'].fields_by_name['nfs_mounts']._loaded_options = None
    _globals['_WORKERPOOLSPEC'].fields_by_name['nfs_mounts']._serialized_options = b'\xe0A\x01'
    _globals['_CONTAINERSPEC'].fields_by_name['image_uri']._loaded_options = None
    _globals['_CONTAINERSPEC'].fields_by_name['image_uri']._serialized_options = b'\xe0A\x02'
    _globals['_PYTHONPACKAGESPEC'].fields_by_name['executor_image_uri']._loaded_options = None
    _globals['_PYTHONPACKAGESPEC'].fields_by_name['executor_image_uri']._serialized_options = b'\xe0A\x02'
    _globals['_PYTHONPACKAGESPEC'].fields_by_name['package_uris']._loaded_options = None
    _globals['_PYTHONPACKAGESPEC'].fields_by_name['package_uris']._serialized_options = b'\xe0A\x02'
    _globals['_PYTHONPACKAGESPEC'].fields_by_name['python_module']._loaded_options = None
    _globals['_PYTHONPACKAGESPEC'].fields_by_name['python_module']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEDULING_STRATEGY'].values_by_name['ON_DEMAND']._loaded_options = None
    _globals['_SCHEDULING_STRATEGY'].values_by_name['ON_DEMAND']._serialized_options = b'\x08\x01'
    _globals['_SCHEDULING_STRATEGY'].values_by_name['LOW_COST']._loaded_options = None
    _globals['_SCHEDULING_STRATEGY'].values_by_name['LOW_COST']._serialized_options = b'\x08\x01'
    _globals['_SCHEDULING'].fields_by_name['strategy']._loaded_options = None
    _globals['_SCHEDULING'].fields_by_name['strategy']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEDULING'].fields_by_name['disable_retries']._loaded_options = None
    _globals['_SCHEDULING'].fields_by_name['disable_retries']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEDULING'].fields_by_name['max_wait_duration']._loaded_options = None
    _globals['_SCHEDULING'].fields_by_name['max_wait_duration']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMJOB']._serialized_start = 544
    _globals['_CUSTOMJOB']._serialized_end = 1490
    _globals['_CUSTOMJOB_LABELSENTRY']._serialized_start = 1284
    _globals['_CUSTOMJOB_LABELSENTRY']._serialized_end = 1329
    _globals['_CUSTOMJOB_WEBACCESSURISENTRY']._serialized_start = 1331
    _globals['_CUSTOMJOB_WEBACCESSURISENTRY']._serialized_end = 1383
    _globals['_CUSTOMJOBSPEC']._serialized_start = 1493
    _globals['_CUSTOMJOBSPEC']._serialized_end = 2388
    _globals['_WORKERPOOLSPEC']._serialized_start = 2391
    _globals['_WORKERPOOLSPEC']._serialized_end = 2806
    _globals['_CONTAINERSPEC']._serialized_start = 2808
    _globals['_CONTAINERSPEC']._serialized_end = 2932
    _globals['_PYTHONPACKAGESPEC']._serialized_start = 2935
    _globals['_PYTHONPACKAGESPEC']._serialized_end = 3110
    _globals['_SCHEDULING']._serialized_start = 3113
    _globals['_SCHEDULING']._serialized_end = 3489
    _globals['_SCHEDULING_STRATEGY']._serialized_start = 3376
    _globals['_SCHEDULING_STRATEGY']._serialized_end = 3489