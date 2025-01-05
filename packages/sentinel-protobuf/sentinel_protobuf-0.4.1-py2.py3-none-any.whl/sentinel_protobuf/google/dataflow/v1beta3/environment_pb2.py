"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/dataflow/v1beta3/environment.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/dataflow/v1beta3/environment.proto\x12\x17google.dataflow.v1beta3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto"\xcf\x05\n\x0bEnvironment\x12\x1b\n\x13temp_storage_prefix\x18\x01 \x01(\t\x12#\n\x1bcluster_manager_api_service\x18\x02 \x01(\t\x12\x13\n\x0bexperiments\x18\x03 \x03(\t\x12\x17\n\x0fservice_options\x18\x10 \x03(\t\x12\x1c\n\x14service_kms_key_name\x18\x0c \x01(\t\x129\n\x0cworker_pools\x18\x04 \x03(\x0b2#.google.dataflow.v1beta3.WorkerPool\x12+\n\nuser_agent\x18\x05 \x01(\x0b2\x17.google.protobuf.Struct\x12(\n\x07version\x18\x06 \x01(\x0b2\x17.google.protobuf.Struct\x12\x0f\n\x07dataset\x18\x07 \x01(\t\x125\n\x14sdk_pipeline_options\x18\x08 \x01(\x0b2\x17.google.protobuf.Struct\x122\n\x14internal_experiments\x18\t \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x15service_account_email\x18\n \x01(\t\x12Z\n\x1dflex_resource_scheduling_goal\x18\x0b \x01(\x0e23.google.dataflow.v1beta3.FlexResourceSchedulingGoal\x12\x15\n\rworker_region\x18\r \x01(\t\x12\x13\n\x0bworker_zone\x18\x0e \x01(\t\x12?\n\x0cshuffle_mode\x18\x0f \x01(\x0e2$.google.dataflow.v1beta3.ShuffleModeB\x03\xe0A\x03\x12<\n\rdebug_options\x18\x11 \x01(\x0b2%.google.dataflow.v1beta3.DebugOptions")\n\x07Package\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t"?\n\x04Disk\x12\x0f\n\x07size_gb\x18\x01 \x01(\x05\x12\x11\n\tdisk_type\x18\x02 \x01(\t\x12\x13\n\x0bmount_point\x18\x03 \x01(\t"\xa1\x01\n\x0eWorkerSettings\x12\x10\n\x08base_url\x18\x01 \x01(\t\x12\x19\n\x11reporting_enabled\x18\x02 \x01(\x08\x12\x14\n\x0cservice_path\x18\x03 \x01(\t\x12\x1c\n\x14shuffle_service_path\x18\x04 \x01(\t\x12\x11\n\tworker_id\x18\x05 \x01(\t\x12\x1b\n\x13temp_storage_prefix\x18\x06 \x01(\t"\xa4\x04\n\x12TaskRunnerSettings\x12\x11\n\ttask_user\x18\x01 \x01(\t\x12\x12\n\ntask_group\x18\x02 \x01(\t\x12\x14\n\x0coauth_scopes\x18\x03 \x03(\t\x12\x10\n\x08base_url\x18\x04 \x01(\t\x12\x1c\n\x14dataflow_api_version\x18\x05 \x01(\t\x12I\n\x18parallel_worker_settings\x18\x06 \x01(\x0b2\'.google.dataflow.v1beta3.WorkerSettings\x12\x15\n\rbase_task_dir\x18\x07 \x01(\t\x12\x1d\n\x15continue_on_exception\x18\x08 \x01(\x08\x12\x1c\n\x14log_to_serialconsole\x18\t \x01(\x08\x12\x17\n\x0falsologtostderr\x18\n \x01(\x08\x12\x1b\n\x13log_upload_location\x18\x0b \x01(\t\x12\x0f\n\x07log_dir\x18\x0c \x01(\t\x12\x1b\n\x13temp_storage_prefix\x18\r \x01(\t\x12\x17\n\x0fharness_command\x18\x0e \x01(\t\x12\x1a\n\x12workflow_file_name\x18\x0f \x01(\t\x12\x1e\n\x16commandlines_file_name\x18\x10 \x01(\t\x12\r\n\x05vm_id\x18\x11 \x01(\t\x12\x15\n\rlanguage_hint\x18\x12 \x01(\t\x12#\n\x1bstreaming_worker_main_class\x18\x13 \x01(\t"p\n\x13AutoscalingSettings\x12@\n\talgorithm\x18\x01 \x01(\x0e2-.google.dataflow.v1beta3.AutoscalingAlgorithm\x12\x17\n\x0fmax_num_workers\x18\x02 \x01(\x05"\x88\x01\n\x18SdkHarnessContainerImage\x12\x17\n\x0fcontainer_image\x18\x01 \x01(\t\x12%\n\x1duse_single_core_per_container\x18\x02 \x01(\x08\x12\x16\n\x0eenvironment_id\x18\x03 \x01(\t\x12\x14\n\x0ccapabilities\x18\x04 \x03(\t"\xf2\x07\n\nWorkerPool\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x13\n\x0bnum_workers\x18\x02 \x01(\x05\x122\n\x08packages\x18\x03 \x03(\x0b2 .google.dataflow.v1beta3.Package\x12G\n\x13default_package_set\x18\x04 \x01(\x0e2*.google.dataflow.v1beta3.DefaultPackageSet\x12\x14\n\x0cmachine_type\x18\x05 \x01(\t\x12@\n\x0fteardown_policy\x18\x06 \x01(\x0e2\'.google.dataflow.v1beta3.TeardownPolicy\x12\x14\n\x0cdisk_size_gb\x18\x07 \x01(\x05\x12\x11\n\tdisk_type\x18\x10 \x01(\t\x12\x19\n\x11disk_source_image\x18\x08 \x01(\t\x12\x0c\n\x04zone\x18\t \x01(\t\x12H\n\x13taskrunner_settings\x18\n \x01(\x0b2+.google.dataflow.v1beta3.TaskRunnerSettings\x12\x1b\n\x13on_host_maintenance\x18\x0b \x01(\t\x121\n\ndata_disks\x18\x0c \x03(\x0b2\x1d.google.dataflow.v1beta3.Disk\x12C\n\x08metadata\x18\r \x03(\x0b21.google.dataflow.v1beta3.WorkerPool.MetadataEntry\x12J\n\x14autoscaling_settings\x18\x0e \x01(\x0b2,.google.dataflow.v1beta3.AutoscalingSettings\x12\'\n\tpool_args\x18\x0f \x01(\x0b2\x14.google.protobuf.Any\x12\x0f\n\x07network\x18\x11 \x01(\t\x12\x12\n\nsubnetwork\x18\x13 \x01(\t\x12&\n\x1eworker_harness_container_image\x18\x12 \x01(\t\x12\x1e\n\x16num_threads_per_worker\x18\x14 \x01(\x05\x12O\n\x10ip_configuration\x18\x15 \x01(\x0e25.google.dataflow.v1beta3.WorkerIPAddressConfiguration\x12W\n\x1csdk_harness_container_images\x18\x16 \x03(\x0b21.google.dataflow.v1beta3.SdkHarnessContainerImage\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01".\n\x0cDebugOptions\x12\x1e\n\x16enable_hot_key_logging\x18\x01 \x01(\x08*K\n\x07JobType\x12\x14\n\x10JOB_TYPE_UNKNOWN\x10\x00\x12\x12\n\x0eJOB_TYPE_BATCH\x10\x01\x12\x16\n\x12JOB_TYPE_STREAMING\x10\x02*k\n\x1aFlexResourceSchedulingGoal\x12\x16\n\x12FLEXRS_UNSPECIFIED\x10\x00\x12\x1a\n\x16FLEXRS_SPEED_OPTIMIZED\x10\x01\x12\x19\n\x15FLEXRS_COST_OPTIMIZED\x10\x02*o\n\x0eTeardownPolicy\x12\x1b\n\x17TEARDOWN_POLICY_UNKNOWN\x10\x00\x12\x13\n\x0fTEARDOWN_ALWAYS\x10\x01\x12\x17\n\x13TEARDOWN_ON_SUCCESS\x10\x02\x12\x12\n\x0eTEARDOWN_NEVER\x10\x03*\x90\x01\n\x11DefaultPackageSet\x12\x1f\n\x1bDEFAULT_PACKAGE_SET_UNKNOWN\x10\x00\x12\x1c\n\x18DEFAULT_PACKAGE_SET_NONE\x10\x01\x12\x1c\n\x18DEFAULT_PACKAGE_SET_JAVA\x10\x02\x12\x1e\n\x1aDEFAULT_PACKAGE_SET_PYTHON\x10\x03*z\n\x14AutoscalingAlgorithm\x12!\n\x1dAUTOSCALING_ALGORITHM_UNKNOWN\x10\x00\x12\x1e\n\x1aAUTOSCALING_ALGORITHM_NONE\x10\x01\x12\x1f\n\x1bAUTOSCALING_ALGORITHM_BASIC\x10\x02*f\n\x1cWorkerIPAddressConfiguration\x12\x19\n\x15WORKER_IP_UNSPECIFIED\x10\x00\x12\x14\n\x10WORKER_IP_PUBLIC\x10\x01\x12\x15\n\x11WORKER_IP_PRIVATE\x10\x02*L\n\x0bShuffleMode\x12\x1c\n\x18SHUFFLE_MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08VM_BASED\x10\x01\x12\x11\n\rSERVICE_BASED\x10\x02B\xd3\x01\n\x1bcom.google.dataflow.v1beta3B\x10EnvironmentProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.dataflow.v1beta3.environment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.dataflow.v1beta3B\x10EnvironmentProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3'
    _globals['_ENVIRONMENT'].fields_by_name['shuffle_mode']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['shuffle_mode']._serialized_options = b'\xe0A\x03'
    _globals['_WORKERPOOL_METADATAENTRY']._loaded_options = None
    _globals['_WORKERPOOL_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_JOBTYPE']._serialized_start = 3019
    _globals['_JOBTYPE']._serialized_end = 3094
    _globals['_FLEXRESOURCESCHEDULINGGOAL']._serialized_start = 3096
    _globals['_FLEXRESOURCESCHEDULINGGOAL']._serialized_end = 3203
    _globals['_TEARDOWNPOLICY']._serialized_start = 3205
    _globals['_TEARDOWNPOLICY']._serialized_end = 3316
    _globals['_DEFAULTPACKAGESET']._serialized_start = 3319
    _globals['_DEFAULTPACKAGESET']._serialized_end = 3463
    _globals['_AUTOSCALINGALGORITHM']._serialized_start = 3465
    _globals['_AUTOSCALINGALGORITHM']._serialized_end = 3587
    _globals['_WORKERIPADDRESSCONFIGURATION']._serialized_start = 3589
    _globals['_WORKERIPADDRESSCONFIGURATION']._serialized_end = 3691
    _globals['_SHUFFLEMODE']._serialized_start = 3693
    _globals['_SHUFFLEMODE']._serialized_end = 3769
    _globals['_ENVIRONMENT']._serialized_start = 161
    _globals['_ENVIRONMENT']._serialized_end = 880
    _globals['_PACKAGE']._serialized_start = 882
    _globals['_PACKAGE']._serialized_end = 923
    _globals['_DISK']._serialized_start = 925
    _globals['_DISK']._serialized_end = 988
    _globals['_WORKERSETTINGS']._serialized_start = 991
    _globals['_WORKERSETTINGS']._serialized_end = 1152
    _globals['_TASKRUNNERSETTINGS']._serialized_start = 1155
    _globals['_TASKRUNNERSETTINGS']._serialized_end = 1703
    _globals['_AUTOSCALINGSETTINGS']._serialized_start = 1705
    _globals['_AUTOSCALINGSETTINGS']._serialized_end = 1817
    _globals['_SDKHARNESSCONTAINERIMAGE']._serialized_start = 1820
    _globals['_SDKHARNESSCONTAINERIMAGE']._serialized_end = 1956
    _globals['_WORKERPOOL']._serialized_start = 1959
    _globals['_WORKERPOOL']._serialized_end = 2969
    _globals['_WORKERPOOL_METADATAENTRY']._serialized_start = 2922
    _globals['_WORKERPOOL_METADATAENTRY']._serialized_end = 2969
    _globals['_DEBUGOPTIONS']._serialized_start = 2971
    _globals['_DEBUGOPTIONS']._serialized_end = 3017