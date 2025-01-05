"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/batch/v1/job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.batch.v1 import task_pb2 as google_dot_cloud_dot_batch_dot_v1_dot_task__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/cloud/batch/v1/job.proto\x12\x15google.cloud.batch.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/cloud/batch/v1/task.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x90\x05\n\x03Job\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x10\n\x08priority\x18\x03 \x01(\x03\x12:\n\x0btask_groups\x18\x04 \x03(\x0b2 .google.cloud.batch.v1.TaskGroupB\x03\xe0A\x02\x12B\n\x11allocation_policy\x18\x07 \x01(\x0b2\'.google.cloud.batch.v1.AllocationPolicy\x126\n\x06labels\x18\x08 \x03(\x0b2&.google.cloud.batch.v1.Job.LabelsEntry\x125\n\x06status\x18\t \x01(\x0b2 .google.cloud.batch.v1.JobStatusB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\x0blogs_policy\x18\r \x01(\x0b2!.google.cloud.batch.v1.LogsPolicy\x12=\n\rnotifications\x18\x0e \x03(\x0b2&.google.cloud.batch.v1.JobNotification\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:Q\xeaAN\n\x18batch.googleapis.com/Job\x122projects/{project}/locations/{location}/jobs/{job}"\xcd\x02\n\nLogsPolicy\x12B\n\x0bdestination\x18\x01 \x01(\x0e2-.google.cloud.batch.v1.LogsPolicy.Destination\x12\x11\n\tlogs_path\x18\x02 \x01(\t\x12W\n\x14cloud_logging_option\x18\x03 \x01(\x0b24.google.cloud.batch.v1.LogsPolicy.CloudLoggingOptionB\x03\xe0A\x01\x1aF\n\x12CloudLoggingOption\x120\n#use_generic_task_monitored_resource\x18\x01 \x01(\x08B\x03\xe0A\x01"G\n\x0bDestination\x12\x1b\n\x17DESTINATION_UNSPECIFIED\x10\x00\x12\x11\n\rCLOUD_LOGGING\x10\x01\x12\x08\n\x04PATH\x10\x02"\x80\x07\n\tJobStatus\x125\n\x05state\x18\x01 \x01(\x0e2&.google.cloud.batch.v1.JobStatus.State\x129\n\rstatus_events\x18\x02 \x03(\x0b2".google.cloud.batch.v1.StatusEvent\x12E\n\x0btask_groups\x18\x04 \x03(\x0b20.google.cloud.batch.v1.JobStatus.TaskGroupsEntry\x12/\n\x0crun_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x1a\xd1\x01\n\x0eInstanceStatus\x12\x14\n\x0cmachine_type\x18\x01 \x01(\t\x12U\n\x12provisioning_model\x18\x02 \x01(\x0e29.google.cloud.batch.v1.AllocationPolicy.ProvisioningModel\x12\x11\n\ttask_pack\x18\x03 \x01(\x03\x12?\n\tboot_disk\x18\x04 \x01(\x0b2,.google.cloud.batch.v1.AllocationPolicy.Disk\x1a\xd2\x01\n\x0fTaskGroupStatus\x12L\n\x06counts\x18\x01 \x03(\x0b2<.google.cloud.batch.v1.JobStatus.TaskGroupStatus.CountsEntry\x12B\n\tinstances\x18\x02 \x03(\x0b2/.google.cloud.batch.v1.JobStatus.InstanceStatus\x1a-\n\x0bCountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01\x1ac\n\x0fTaskGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12?\n\x05value\x18\x02 \x01(\x0b20.google.cloud.batch.v1.JobStatus.TaskGroupStatus:\x028\x01"{\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\r\n\tSCHEDULED\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\n\n\x06FAILED\x10\x05\x12\x18\n\x14DELETION_IN_PROGRESS\x10\x06"\xfc\x02\n\x0fJobNotification\x12\x14\n\x0cpubsub_topic\x18\x01 \x01(\t\x12?\n\x07message\x18\x02 \x01(\x0b2..google.cloud.batch.v1.JobNotification.Message\x1a\xc4\x01\n\x07Message\x129\n\x04type\x18\x01 \x01(\x0e2+.google.cloud.batch.v1.JobNotification.Type\x12=\n\rnew_job_state\x18\x02 \x01(\x0e2&.google.cloud.batch.v1.JobStatus.State\x12?\n\x0enew_task_state\x18\x03 \x01(\x0e2\'.google.cloud.batch.v1.TaskStatus.State"K\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11JOB_STATE_CHANGED\x10\x01\x12\x16\n\x12TASK_STATE_CHANGED\x10\x02"\x81\x0f\n\x10AllocationPolicy\x12H\n\x08location\x18\x01 \x01(\x0b26.google.cloud.batch.v1.AllocationPolicy.LocationPolicy\x12S\n\tinstances\x18\x08 \x03(\x0b2@.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate\x12>\n\x0fservice_account\x18\t \x01(\x0b2%.google.cloud.batch.v1.ServiceAccount\x12C\n\x06labels\x18\x06 \x03(\x0b23.google.cloud.batch.v1.AllocationPolicy.LabelsEntry\x12F\n\x07network\x18\x07 \x01(\x0b25.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy\x12J\n\tplacement\x18\n \x01(\x0b27.google.cloud.batch.v1.AllocationPolicy.PlacementPolicy\x12\x11\n\x04tags\x18\x0b \x03(\tB\x03\xe0A\x01\x1a+\n\x0eLocationPolicy\x12\x19\n\x11allowed_locations\x18\x01 \x03(\t\x1aq\n\x04Disk\x12\x0f\n\x05image\x18\x04 \x01(\tH\x00\x12\x12\n\x08snapshot\x18\x05 \x01(\tH\x00\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07size_gb\x18\x02 \x01(\x03\x12\x16\n\x0edisk_interface\x18\x06 \x01(\tB\r\n\x0bdata_source\x1a\x8a\x01\n\x0cAttachedDisk\x12@\n\x08new_disk\x18\x01 \x01(\x0b2,.google.cloud.batch.v1.AllocationPolicy.DiskH\x00\x12\x17\n\rexisting_disk\x18\x02 \x01(\tH\x00\x12\x13\n\x0bdevice_name\x18\x03 \x01(\tB\n\n\x08attached\x1ah\n\x0bAccelerator\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05count\x18\x02 \x01(\x03\x12\x1f\n\x13install_gpu_drivers\x18\x03 \x01(\x08B\x02\x18\x01\x12\x1b\n\x0edriver_version\x18\x04 \x01(\tB\x03\xe0A\x01\x1a\x82\x03\n\x0eInstancePolicy\x12\x14\n\x0cmachine_type\x18\x02 \x01(\t\x12\x18\n\x10min_cpu_platform\x18\x03 \x01(\t\x12U\n\x12provisioning_model\x18\x04 \x01(\x0e29.google.cloud.batch.v1.AllocationPolicy.ProvisioningModel\x12I\n\x0caccelerators\x18\x05 \x03(\x0b23.google.cloud.batch.v1.AllocationPolicy.Accelerator\x12?\n\tboot_disk\x18\x08 \x01(\x0b2,.google.cloud.batch.v1.AllocationPolicy.Disk\x12C\n\x05disks\x18\x06 \x03(\x0b24.google.cloud.batch.v1.AllocationPolicy.AttachedDisk\x12\x18\n\x0breservation\x18\x07 \x01(\tB\x03\xe0A\x01\x1a\xf6\x01\n\x18InstancePolicyOrTemplate\x12H\n\x06policy\x18\x01 \x01(\x0b26.google.cloud.batch.v1.AllocationPolicy.InstancePolicyH\x00\x12\x1b\n\x11instance_template\x18\x02 \x01(\tH\x00\x12\x1b\n\x13install_gpu_drivers\x18\x03 \x01(\x08\x12\x1e\n\x11install_ops_agent\x18\x04 \x01(\x08B\x03\xe0A\x01\x12#\n\x16block_project_ssh_keys\x18\x05 \x01(\x08B\x03\xe0A\x01B\x11\n\x0fpolicy_template\x1aW\n\x10NetworkInterface\x12\x0f\n\x07network\x18\x01 \x01(\t\x12\x12\n\nsubnetwork\x18\x02 \x01(\t\x12\x1e\n\x16no_external_ip_address\x18\x03 \x01(\x08\x1ae\n\rNetworkPolicy\x12T\n\x12network_interfaces\x18\x01 \x03(\x0b28.google.cloud.batch.v1.AllocationPolicy.NetworkInterface\x1a<\n\x0fPlacementPolicy\x12\x13\n\x0bcollocation\x18\x01 \x01(\t\x12\x14\n\x0cmax_distance\x18\x02 \x01(\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"`\n\x11ProvisioningModel\x12"\n\x1ePROVISIONING_MODEL_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x08\n\x04SPOT\x10\x02\x12\x0f\n\x0bPREEMPTIBLE\x10\x03"\xcb\x04\n\tTaskGroup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x127\n\ttask_spec\x18\x03 \x01(\x0b2\x1f.google.cloud.batch.v1.TaskSpecB\x03\xe0A\x02\x12\x12\n\ntask_count\x18\x04 \x01(\x03\x12\x13\n\x0bparallelism\x18\x05 \x01(\x03\x12L\n\x11scheduling_policy\x18\x06 \x01(\x0e21.google.cloud.batch.v1.TaskGroup.SchedulingPolicy\x12=\n\x11task_environments\x18\t \x03(\x0b2".google.cloud.batch.v1.Environment\x12\x1b\n\x13task_count_per_node\x18\n \x01(\x03\x12\x1a\n\x12require_hosts_file\x18\x0b \x01(\x08\x12\x16\n\x0epermissive_ssh\x18\x0c \x01(\x08\x12\x1c\n\x0frun_as_non_root\x18\x0e \x01(\x08B\x03\xe0A\x01"\\\n\x10SchedulingPolicy\x12!\n\x1dSCHEDULING_POLICY_UNSPECIFIED\x10\x00\x12\x17\n\x13AS_SOON_AS_POSSIBLE\x10\x01\x12\x0c\n\x08IN_ORDER\x10\x02:o\xeaAl\n\x1ebatch.googleapis.com/TaskGroup\x12Jprojects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}"/\n\x0eServiceAccount\x12\r\n\x05email\x18\x01 \x01(\t\x12\x0e\n\x06scopes\x18\x02 \x03(\tB\xa9\x01\n\x19com.google.cloud.batch.v1B\x08JobProtoP\x01Z/cloud.google.com/go/batch/apiv1/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x15Google.Cloud.Batch.V1\xca\x02\x15Google\\Cloud\\Batch\\V1\xea\x02\x18Google::Cloud::Batch::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.batch.v1.job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.batch.v1B\x08JobProtoP\x01Z/cloud.google.com/go/batch/apiv1/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x15Google.Cloud.Batch.V1\xca\x02\x15Google\\Cloud\\Batch\\V1\xea\x02\x18Google::Cloud::Batch::V1'
    _globals['_JOB_LABELSENTRY']._loaded_options = None
    _globals['_JOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_JOB'].fields_by_name['name']._loaded_options = None
    _globals['_JOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['uid']._loaded_options = None
    _globals['_JOB'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['task_groups']._loaded_options = None
    _globals['_JOB'].fields_by_name['task_groups']._serialized_options = b'\xe0A\x02'
    _globals['_JOB'].fields_by_name['status']._loaded_options = None
    _globals['_JOB'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_JOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_JOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_JOB']._loaded_options = None
    _globals['_JOB']._serialized_options = b'\xeaAN\n\x18batch.googleapis.com/Job\x122projects/{project}/locations/{location}/jobs/{job}'
    _globals['_LOGSPOLICY_CLOUDLOGGINGOPTION'].fields_by_name['use_generic_task_monitored_resource']._loaded_options = None
    _globals['_LOGSPOLICY_CLOUDLOGGINGOPTION'].fields_by_name['use_generic_task_monitored_resource']._serialized_options = b'\xe0A\x01'
    _globals['_LOGSPOLICY'].fields_by_name['cloud_logging_option']._loaded_options = None
    _globals['_LOGSPOLICY'].fields_by_name['cloud_logging_option']._serialized_options = b'\xe0A\x01'
    _globals['_JOBSTATUS_TASKGROUPSTATUS_COUNTSENTRY']._loaded_options = None
    _globals['_JOBSTATUS_TASKGROUPSTATUS_COUNTSENTRY']._serialized_options = b'8\x01'
    _globals['_JOBSTATUS_TASKGROUPSENTRY']._loaded_options = None
    _globals['_JOBSTATUS_TASKGROUPSENTRY']._serialized_options = b'8\x01'
    _globals['_ALLOCATIONPOLICY_ACCELERATOR'].fields_by_name['install_gpu_drivers']._loaded_options = None
    _globals['_ALLOCATIONPOLICY_ACCELERATOR'].fields_by_name['install_gpu_drivers']._serialized_options = b'\x18\x01'
    _globals['_ALLOCATIONPOLICY_ACCELERATOR'].fields_by_name['driver_version']._loaded_options = None
    _globals['_ALLOCATIONPOLICY_ACCELERATOR'].fields_by_name['driver_version']._serialized_options = b'\xe0A\x01'
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICY'].fields_by_name['reservation']._loaded_options = None
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICY'].fields_by_name['reservation']._serialized_options = b'\xe0A\x01'
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICYORTEMPLATE'].fields_by_name['install_ops_agent']._loaded_options = None
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICYORTEMPLATE'].fields_by_name['install_ops_agent']._serialized_options = b'\xe0A\x01'
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICYORTEMPLATE'].fields_by_name['block_project_ssh_keys']._loaded_options = None
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICYORTEMPLATE'].fields_by_name['block_project_ssh_keys']._serialized_options = b'\xe0A\x01'
    _globals['_ALLOCATIONPOLICY_LABELSENTRY']._loaded_options = None
    _globals['_ALLOCATIONPOLICY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ALLOCATIONPOLICY'].fields_by_name['tags']._loaded_options = None
    _globals['_ALLOCATIONPOLICY'].fields_by_name['tags']._serialized_options = b'\xe0A\x01'
    _globals['_TASKGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_TASKGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TASKGROUP'].fields_by_name['task_spec']._loaded_options = None
    _globals['_TASKGROUP'].fields_by_name['task_spec']._serialized_options = b'\xe0A\x02'
    _globals['_TASKGROUP'].fields_by_name['run_as_non_root']._loaded_options = None
    _globals['_TASKGROUP'].fields_by_name['run_as_non_root']._serialized_options = b'\xe0A\x01'
    _globals['_TASKGROUP']._loaded_options = None
    _globals['_TASKGROUP']._serialized_options = b'\xeaAl\n\x1ebatch.googleapis.com/TaskGroup\x12Jprojects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}'
    _globals['_JOB']._serialized_start = 218
    _globals['_JOB']._serialized_end = 874
    _globals['_JOB_LABELSENTRY']._serialized_start = 746
    _globals['_JOB_LABELSENTRY']._serialized_end = 791
    _globals['_LOGSPOLICY']._serialized_start = 877
    _globals['_LOGSPOLICY']._serialized_end = 1210
    _globals['_LOGSPOLICY_CLOUDLOGGINGOPTION']._serialized_start = 1067
    _globals['_LOGSPOLICY_CLOUDLOGGINGOPTION']._serialized_end = 1137
    _globals['_LOGSPOLICY_DESTINATION']._serialized_start = 1139
    _globals['_LOGSPOLICY_DESTINATION']._serialized_end = 1210
    _globals['_JOBSTATUS']._serialized_start = 1213
    _globals['_JOBSTATUS']._serialized_end = 2109
    _globals['_JOBSTATUS_INSTANCESTATUS']._serialized_start = 1461
    _globals['_JOBSTATUS_INSTANCESTATUS']._serialized_end = 1670
    _globals['_JOBSTATUS_TASKGROUPSTATUS']._serialized_start = 1673
    _globals['_JOBSTATUS_TASKGROUPSTATUS']._serialized_end = 1883
    _globals['_JOBSTATUS_TASKGROUPSTATUS_COUNTSENTRY']._serialized_start = 1838
    _globals['_JOBSTATUS_TASKGROUPSTATUS_COUNTSENTRY']._serialized_end = 1883
    _globals['_JOBSTATUS_TASKGROUPSENTRY']._serialized_start = 1885
    _globals['_JOBSTATUS_TASKGROUPSENTRY']._serialized_end = 1984
    _globals['_JOBSTATUS_STATE']._serialized_start = 1986
    _globals['_JOBSTATUS_STATE']._serialized_end = 2109
    _globals['_JOBNOTIFICATION']._serialized_start = 2112
    _globals['_JOBNOTIFICATION']._serialized_end = 2492
    _globals['_JOBNOTIFICATION_MESSAGE']._serialized_start = 2219
    _globals['_JOBNOTIFICATION_MESSAGE']._serialized_end = 2415
    _globals['_JOBNOTIFICATION_TYPE']._serialized_start = 2417
    _globals['_JOBNOTIFICATION_TYPE']._serialized_end = 2492
    _globals['_ALLOCATIONPOLICY']._serialized_start = 2495
    _globals['_ALLOCATIONPOLICY']._serialized_end = 4416
    _globals['_ALLOCATIONPOLICY_LOCATIONPOLICY']._serialized_start = 2974
    _globals['_ALLOCATIONPOLICY_LOCATIONPOLICY']._serialized_end = 3017
    _globals['_ALLOCATIONPOLICY_DISK']._serialized_start = 3019
    _globals['_ALLOCATIONPOLICY_DISK']._serialized_end = 3132
    _globals['_ALLOCATIONPOLICY_ATTACHEDDISK']._serialized_start = 3135
    _globals['_ALLOCATIONPOLICY_ATTACHEDDISK']._serialized_end = 3273
    _globals['_ALLOCATIONPOLICY_ACCELERATOR']._serialized_start = 3275
    _globals['_ALLOCATIONPOLICY_ACCELERATOR']._serialized_end = 3379
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICY']._serialized_start = 3382
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICY']._serialized_end = 3768
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICYORTEMPLATE']._serialized_start = 3771
    _globals['_ALLOCATIONPOLICY_INSTANCEPOLICYORTEMPLATE']._serialized_end = 4017
    _globals['_ALLOCATIONPOLICY_NETWORKINTERFACE']._serialized_start = 4019
    _globals['_ALLOCATIONPOLICY_NETWORKINTERFACE']._serialized_end = 4106
    _globals['_ALLOCATIONPOLICY_NETWORKPOLICY']._serialized_start = 4108
    _globals['_ALLOCATIONPOLICY_NETWORKPOLICY']._serialized_end = 4209
    _globals['_ALLOCATIONPOLICY_PLACEMENTPOLICY']._serialized_start = 4211
    _globals['_ALLOCATIONPOLICY_PLACEMENTPOLICY']._serialized_end = 4271
    _globals['_ALLOCATIONPOLICY_LABELSENTRY']._serialized_start = 746
    _globals['_ALLOCATIONPOLICY_LABELSENTRY']._serialized_end = 791
    _globals['_ALLOCATIONPOLICY_PROVISIONINGMODEL']._serialized_start = 4320
    _globals['_ALLOCATIONPOLICY_PROVISIONINGMODEL']._serialized_end = 4416
    _globals['_TASKGROUP']._serialized_start = 4419
    _globals['_TASKGROUP']._serialized_end = 5006
    _globals['_TASKGROUP_SCHEDULINGPOLICY']._serialized_start = 4801
    _globals['_TASKGROUP_SCHEDULINGPOLICY']._serialized_end = 4893
    _globals['_SERVICEACCOUNT']._serialized_start = 5008
    _globals['_SERVICEACCOUNT']._serialized_end = 5055