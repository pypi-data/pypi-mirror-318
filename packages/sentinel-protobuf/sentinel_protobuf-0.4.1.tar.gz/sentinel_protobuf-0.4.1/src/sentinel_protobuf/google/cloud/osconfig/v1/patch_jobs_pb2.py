"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1/patch_jobs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.osconfig.v1 import osconfig_common_pb2 as google_dot_cloud_dot_osconfig_dot_v1_dot_osconfig__common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/osconfig/v1/patch_jobs.proto\x12\x18google.cloud.osconfig.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/osconfig/v1/osconfig_common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x89\x03\n\x16ExecutePatchJobRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12K\n\x0finstance_filter\x18\x07 \x01(\x0b2-.google.cloud.osconfig.v1.PatchInstanceFilterB\x03\xe0A\x02\x12;\n\x0cpatch_config\x18\x04 \x01(\x0b2%.google.cloud.osconfig.v1.PatchConfig\x12+\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0f\n\x07dry_run\x18\x06 \x01(\x08\x12\x14\n\x0cdisplay_name\x18\x08 \x01(\t\x127\n\x07rollout\x18\t \x01(\x0b2&.google.cloud.osconfig.v1.PatchRollout"L\n\x12GetPatchJobRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n osconfig.googleapis.com/PatchJob"\x95\x01\n"ListPatchJobInstanceDetailsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n osconfig.googleapis.com/PatchJob\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"\x95\x01\n#ListPatchJobInstanceDetailsResponse\x12U\n\x1apatch_job_instance_details\x18\x01 \x03(\x0b21.google.cloud.osconfig.v1.PatchJobInstanceDetails\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xd6\x01\n\x17PatchJobInstanceDetails\x122\n\x04name\x18\x01 \x01(\tB$\xfaA!\n\x1fcompute.googleapis.com/Instance\x12\x1a\n\x12instance_system_id\x18\x02 \x01(\t\x12<\n\x05state\x18\x03 \x01(\x0e2-.google.cloud.osconfig.v1.Instance.PatchState\x12\x16\n\x0efailure_reason\x18\x04 \x01(\t\x12\x15\n\rattempt_count\x18\x05 \x01(\x03"\x92\x01\n\x14ListPatchJobsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"h\n\x15ListPatchJobsResponse\x126\n\npatch_jobs\x18\x01 \x03(\x0b2".google.cloud.osconfig.v1.PatchJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xdc\x0b\n\x08PatchJob\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x0e \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x127\n\x05state\x18\x05 \x01(\x0e2(.google.cloud.osconfig.v1.PatchJob.State\x12F\n\x0finstance_filter\x18\r \x01(\x0b2-.google.cloud.osconfig.v1.PatchInstanceFilter\x12;\n\x0cpatch_config\x18\x07 \x01(\x0b2%.google.cloud.osconfig.v1.PatchConfig\x12+\n\x08duration\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12[\n\x18instance_details_summary\x18\t \x01(\x0b29.google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary\x12\x0f\n\x07dry_run\x18\n \x01(\x08\x12\x15\n\rerror_message\x18\x0b \x01(\t\x12\x18\n\x10percent_complete\x18\x0c \x01(\x01\x12I\n\x10patch_deployment\x18\x0f \x01(\tB/\xe0A\x03\xfaA)\n\'osconfig.googleapis.com/PatchDeployment\x127\n\x07rollout\x18\x10 \x01(\x0b2&.google.cloud.osconfig.v1.PatchRollout\x1a\xbd\x04\n\x16InstanceDetailsSummary\x12\x1e\n\x16pending_instance_count\x18\x01 \x01(\x03\x12\x1f\n\x17inactive_instance_count\x18\x02 \x01(\x03\x12\x1f\n\x17notified_instance_count\x18\x03 \x01(\x03\x12\x1e\n\x16started_instance_count\x18\x04 \x01(\x03\x12*\n"downloading_patches_instance_count\x18\x05 \x01(\x03\x12\'\n\x1fapplying_patches_instance_count\x18\x06 \x01(\x03\x12 \n\x18rebooting_instance_count\x18\x07 \x01(\x03\x12 \n\x18succeeded_instance_count\x18\x08 \x01(\x03\x120\n(succeeded_reboot_required_instance_count\x18\t \x01(\x03\x12\x1d\n\x15failed_instance_count\x18\n \x01(\x03\x12\x1c\n\x14acked_instance_count\x18\x0b \x01(\x03\x12 \n\x18timed_out_instance_count\x18\x0c \x01(\x03\x12%\n\x1dpre_patch_step_instance_count\x18\r \x01(\x03\x12&\n\x1epost_patch_step_instance_count\x18\x0e \x01(\x03\x12(\n no_agent_detected_instance_count\x18\x0f \x01(\x03"\x95\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\x13\n\x0fINSTANCE_LOOKUP\x10\x02\x12\x0c\n\x08PATCHING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\x19\n\x15COMPLETED_WITH_ERRORS\x10\x05\x12\x0c\n\x08CANCELED\x10\x06\x12\r\n\tTIMED_OUT\x10\x07:O\xeaAL\n osconfig.googleapis.com/PatchJob\x12(projects/{project}/patchJobs/{patch_job}"\xd6\x04\n\x0bPatchConfig\x12I\n\rreboot_config\x18\x01 \x01(\x0e22.google.cloud.osconfig.v1.PatchConfig.RebootConfig\x122\n\x03apt\x18\x03 \x01(\x0b2%.google.cloud.osconfig.v1.AptSettings\x122\n\x03yum\x18\x04 \x01(\x0b2%.google.cloud.osconfig.v1.YumSettings\x122\n\x03goo\x18\x05 \x01(\x0b2%.google.cloud.osconfig.v1.GooSettings\x128\n\x06zypper\x18\x06 \x01(\x0b2(.google.cloud.osconfig.v1.ZypperSettings\x12G\n\x0ewindows_update\x18\x07 \x01(\x0b2/.google.cloud.osconfig.v1.WindowsUpdateSettings\x124\n\x08pre_step\x18\x08 \x01(\x0b2".google.cloud.osconfig.v1.ExecStep\x125\n\tpost_step\x18\t \x01(\x0b2".google.cloud.osconfig.v1.ExecStep\x12\x1d\n\x15mig_instances_allowed\x18\n \x01(\x08"Q\n\x0cRebootConfig\x12\x1d\n\x19REBOOT_CONFIG_UNSPECIFIED\x10\x00\x12\x0b\n\x07DEFAULT\x10\x01\x12\n\n\x06ALWAYS\x10\x02\x12\t\n\x05NEVER\x10\x03"\xce\x02\n\x08Instance"\xc1\x02\n\nPatchState\x12\x1b\n\x17PATCH_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x12\x0c\n\x08NOTIFIED\x10\x03\x12\x0b\n\x07STARTED\x10\x04\x12\x17\n\x13DOWNLOADING_PATCHES\x10\x05\x12\x14\n\x10APPLYING_PATCHES\x10\x06\x12\r\n\tREBOOTING\x10\x07\x12\r\n\tSUCCEEDED\x10\x08\x12\x1d\n\x19SUCCEEDED_REBOOT_REQUIRED\x10\t\x12\n\n\x06FAILED\x10\n\x12\t\n\x05ACKED\x10\x0b\x12\r\n\tTIMED_OUT\x10\x0c\x12\x1a\n\x16RUNNING_PRE_PATCH_STEP\x10\r\x12\x1b\n\x17RUNNING_POST_PATCH_STEP\x10\x0e\x12\x15\n\x11NO_AGENT_DETECTED\x10\x0f"O\n\x15CancelPatchJobRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n osconfig.googleapis.com/PatchJob"\xaa\x01\n\x0bAptSettings\x128\n\x04type\x18\x01 \x01(\x0e2*.google.cloud.osconfig.v1.AptSettings.Type\x12\x10\n\x08excludes\x18\x02 \x03(\t\x12\x1a\n\x12exclusive_packages\x18\x03 \x03(\t"3\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04DIST\x10\x01\x12\x0b\n\x07UPGRADE\x10\x02"^\n\x0bYumSettings\x12\x10\n\x08security\x18\x01 \x01(\x08\x12\x0f\n\x07minimal\x18\x02 \x01(\x08\x12\x10\n\x08excludes\x18\x03 \x03(\t\x12\x1a\n\x12exclusive_packages\x18\x04 \x03(\t"\r\n\x0bGooSettings"\x91\x01\n\x0eZypperSettings\x12\x15\n\rwith_optional\x18\x01 \x01(\x08\x12\x13\n\x0bwith_update\x18\x02 \x01(\x08\x12\x12\n\ncategories\x18\x03 \x03(\t\x12\x12\n\nseverities\x18\x04 \x03(\t\x12\x10\n\x08excludes\x18\x05 \x03(\t\x12\x19\n\x11exclusive_patches\x18\x06 \x03(\t"\xd5\x02\n\x15WindowsUpdateSettings\x12W\n\x0fclassifications\x18\x01 \x03(\x0e2>.google.cloud.osconfig.v1.WindowsUpdateSettings.Classification\x12\x10\n\x08excludes\x18\x02 \x03(\t\x12\x19\n\x11exclusive_patches\x18\x03 \x03(\t"\xb5\x01\n\x0eClassification\x12\x1e\n\x1aCLASSIFICATION_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\x0c\n\x08SECURITY\x10\x02\x12\x0e\n\nDEFINITION\x10\x03\x12\n\n\x06DRIVER\x10\x04\x12\x10\n\x0cFEATURE_PACK\x10\x05\x12\x10\n\x0cSERVICE_PACK\x10\x06\x12\x08\n\x04TOOL\x10\x07\x12\x11\n\rUPDATE_ROLLUP\x10\x08\x12\n\n\x06UPDATE\x10\t"\xa0\x01\n\x08ExecStep\x12H\n\x16linux_exec_step_config\x18\x01 \x01(\x0b2(.google.cloud.osconfig.v1.ExecStepConfig\x12J\n\x18windows_exec_step_config\x18\x02 \x01(\x0b2(.google.cloud.osconfig.v1.ExecStepConfig"\xa0\x02\n\x0eExecStepConfig\x12\x14\n\nlocal_path\x18\x01 \x01(\tH\x00\x129\n\ngcs_object\x18\x02 \x01(\x0b2#.google.cloud.osconfig.v1.GcsObjectH\x00\x12\x1d\n\x15allowed_success_codes\x18\x03 \x03(\x05\x12I\n\x0binterpreter\x18\x04 \x01(\x0e24.google.cloud.osconfig.v1.ExecStepConfig.Interpreter"E\n\x0bInterpreter\x12\x1b\n\x17INTERPRETER_UNSPECIFIED\x10\x00\x12\t\n\x05SHELL\x10\x01\x12\x0e\n\nPOWERSHELL\x10\x02B\x0c\n\nexecutable"U\n\tGcsObject\x12\x13\n\x06bucket\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06object\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11generation_number\x18\x03 \x01(\x03B\x03\xe0A\x02"\xc8\x02\n\x13PatchInstanceFilter\x12\x0b\n\x03all\x18\x01 \x01(\x08\x12N\n\x0cgroup_labels\x18\x02 \x03(\x0b28.google.cloud.osconfig.v1.PatchInstanceFilter.GroupLabel\x12\r\n\x05zones\x18\x03 \x03(\t\x12\x11\n\tinstances\x18\x04 \x03(\t\x12\x1e\n\x16instance_name_prefixes\x18\x05 \x03(\t\x1a\x91\x01\n\nGroupLabel\x12T\n\x06labels\x18\x01 \x03(\x0b2D.google.cloud.osconfig.v1.PatchInstanceFilter.GroupLabel.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xd4\x01\n\x0cPatchRollout\x129\n\x04mode\x18\x01 \x01(\x0e2+.google.cloud.osconfig.v1.PatchRollout.Mode\x12C\n\x11disruption_budget\x18\x02 \x01(\x0b2(.google.cloud.osconfig.v1.FixedOrPercent"D\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x10\n\x0cZONE_BY_ZONE\x10\x01\x12\x14\n\x10CONCURRENT_ZONES\x10\x02B\xb7\x01\n\x1ccom.google.cloud.osconfig.v1B\tPatchJobsZ8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1.patch_jobs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.osconfig.v1B\tPatchJobsZ8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1'
    _globals['_EXECUTEPATCHJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXECUTEPATCHJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_EXECUTEPATCHJOBREQUEST'].fields_by_name['instance_filter']._loaded_options = None
    _globals['_EXECUTEPATCHJOBREQUEST'].fields_by_name['instance_filter']._serialized_options = b'\xe0A\x02'
    _globals['_GETPATCHJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPATCHJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n osconfig.googleapis.com/PatchJob'
    _globals['_LISTPATCHJOBINSTANCEDETAILSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPATCHJOBINSTANCEDETAILSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n osconfig.googleapis.com/PatchJob'
    _globals['_PATCHJOBINSTANCEDETAILS'].fields_by_name['name']._loaded_options = None
    _globals['_PATCHJOBINSTANCEDETAILS'].fields_by_name['name']._serialized_options = b'\xfaA!\n\x1fcompute.googleapis.com/Instance'
    _globals['_LISTPATCHJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPATCHJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_PATCHJOB'].fields_by_name['patch_deployment']._loaded_options = None
    _globals['_PATCHJOB'].fields_by_name['patch_deployment']._serialized_options = b"\xe0A\x03\xfaA)\n'osconfig.googleapis.com/PatchDeployment"
    _globals['_PATCHJOB']._loaded_options = None
    _globals['_PATCHJOB']._serialized_options = b'\xeaAL\n osconfig.googleapis.com/PatchJob\x12(projects/{project}/patchJobs/{patch_job}'
    _globals['_CANCELPATCHJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELPATCHJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n osconfig.googleapis.com/PatchJob'
    _globals['_GCSOBJECT'].fields_by_name['bucket']._loaded_options = None
    _globals['_GCSOBJECT'].fields_by_name['bucket']._serialized_options = b'\xe0A\x02'
    _globals['_GCSOBJECT'].fields_by_name['object']._loaded_options = None
    _globals['_GCSOBJECT'].fields_by_name['object']._serialized_options = b'\xe0A\x02'
    _globals['_GCSOBJECT'].fields_by_name['generation_number']._loaded_options = None
    _globals['_GCSOBJECT'].fields_by_name['generation_number']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL_LABELSENTRY']._loaded_options = None
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTEPATCHJOBREQUEST']._serialized_start = 245
    _globals['_EXECUTEPATCHJOBREQUEST']._serialized_end = 638
    _globals['_GETPATCHJOBREQUEST']._serialized_start = 640
    _globals['_GETPATCHJOBREQUEST']._serialized_end = 716
    _globals['_LISTPATCHJOBINSTANCEDETAILSREQUEST']._serialized_start = 719
    _globals['_LISTPATCHJOBINSTANCEDETAILSREQUEST']._serialized_end = 868
    _globals['_LISTPATCHJOBINSTANCEDETAILSRESPONSE']._serialized_start = 871
    _globals['_LISTPATCHJOBINSTANCEDETAILSRESPONSE']._serialized_end = 1020
    _globals['_PATCHJOBINSTANCEDETAILS']._serialized_start = 1023
    _globals['_PATCHJOBINSTANCEDETAILS']._serialized_end = 1237
    _globals['_LISTPATCHJOBSREQUEST']._serialized_start = 1240
    _globals['_LISTPATCHJOBSREQUEST']._serialized_end = 1386
    _globals['_LISTPATCHJOBSRESPONSE']._serialized_start = 1388
    _globals['_LISTPATCHJOBSRESPONSE']._serialized_end = 1492
    _globals['_PATCHJOB']._serialized_start = 1495
    _globals['_PATCHJOB']._serialized_end = 2995
    _globals['_PATCHJOB_INSTANCEDETAILSSUMMARY']._serialized_start = 2189
    _globals['_PATCHJOB_INSTANCEDETAILSSUMMARY']._serialized_end = 2762
    _globals['_PATCHJOB_STATE']._serialized_start = 2765
    _globals['_PATCHJOB_STATE']._serialized_end = 2914
    _globals['_PATCHCONFIG']._serialized_start = 2998
    _globals['_PATCHCONFIG']._serialized_end = 3596
    _globals['_PATCHCONFIG_REBOOTCONFIG']._serialized_start = 3515
    _globals['_PATCHCONFIG_REBOOTCONFIG']._serialized_end = 3596
    _globals['_INSTANCE']._serialized_start = 3599
    _globals['_INSTANCE']._serialized_end = 3933
    _globals['_INSTANCE_PATCHSTATE']._serialized_start = 3612
    _globals['_INSTANCE_PATCHSTATE']._serialized_end = 3933
    _globals['_CANCELPATCHJOBREQUEST']._serialized_start = 3935
    _globals['_CANCELPATCHJOBREQUEST']._serialized_end = 4014
    _globals['_APTSETTINGS']._serialized_start = 4017
    _globals['_APTSETTINGS']._serialized_end = 4187
    _globals['_APTSETTINGS_TYPE']._serialized_start = 4136
    _globals['_APTSETTINGS_TYPE']._serialized_end = 4187
    _globals['_YUMSETTINGS']._serialized_start = 4189
    _globals['_YUMSETTINGS']._serialized_end = 4283
    _globals['_GOOSETTINGS']._serialized_start = 4285
    _globals['_GOOSETTINGS']._serialized_end = 4298
    _globals['_ZYPPERSETTINGS']._serialized_start = 4301
    _globals['_ZYPPERSETTINGS']._serialized_end = 4446
    _globals['_WINDOWSUPDATESETTINGS']._serialized_start = 4449
    _globals['_WINDOWSUPDATESETTINGS']._serialized_end = 4790
    _globals['_WINDOWSUPDATESETTINGS_CLASSIFICATION']._serialized_start = 4609
    _globals['_WINDOWSUPDATESETTINGS_CLASSIFICATION']._serialized_end = 4790
    _globals['_EXECSTEP']._serialized_start = 4793
    _globals['_EXECSTEP']._serialized_end = 4953
    _globals['_EXECSTEPCONFIG']._serialized_start = 4956
    _globals['_EXECSTEPCONFIG']._serialized_end = 5244
    _globals['_EXECSTEPCONFIG_INTERPRETER']._serialized_start = 5161
    _globals['_EXECSTEPCONFIG_INTERPRETER']._serialized_end = 5230
    _globals['_GCSOBJECT']._serialized_start = 5246
    _globals['_GCSOBJECT']._serialized_end = 5331
    _globals['_PATCHINSTANCEFILTER']._serialized_start = 5334
    _globals['_PATCHINSTANCEFILTER']._serialized_end = 5662
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL']._serialized_start = 5517
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL']._serialized_end = 5662
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL_LABELSENTRY']._serialized_start = 5617
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL_LABELSENTRY']._serialized_end = 5662
    _globals['_PATCHROLLOUT']._serialized_start = 5665
    _globals['_PATCHROLLOUT']._serialized_end = 5877
    _globals['_PATCHROLLOUT_MODE']._serialized_start = 5809
    _globals['_PATCHROLLOUT_MODE']._serialized_end = 5877