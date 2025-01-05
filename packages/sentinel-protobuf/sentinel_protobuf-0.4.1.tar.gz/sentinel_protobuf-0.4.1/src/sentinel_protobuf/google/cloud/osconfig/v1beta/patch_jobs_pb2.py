"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1beta/patch_jobs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.osconfig.v1beta import osconfig_common_pb2 as google_dot_cloud_dot_osconfig_dot_v1beta_dot_osconfig__common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/osconfig/v1beta/patch_jobs.proto\x12\x1cgoogle.cloud.osconfig.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/osconfig/v1beta/osconfig_common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe5\x02\n\x16ExecutePatchJobRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12O\n\x0finstance_filter\x18\x07 \x01(\x0b21.google.cloud.osconfig.v1beta.PatchInstanceFilterB\x03\xe0A\x02\x12?\n\x0cpatch_config\x18\x04 \x01(\x0b2).google.cloud.osconfig.v1beta.PatchConfig\x12+\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0f\n\x07dry_run\x18\x06 \x01(\x08\x12\x14\n\x0cdisplay_name\x18\x08 \x01(\t\x12;\n\x07rollout\x18\t \x01(\x0b2*.google.cloud.osconfig.v1beta.PatchRollout"\'\n\x12GetPatchJobRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"p\n"ListPatchJobInstanceDetailsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"\x99\x01\n#ListPatchJobInstanceDetailsResponse\x12Y\n\x1apatch_job_instance_details\x18\x01 \x03(\x0b25.google.cloud.osconfig.v1beta.PatchJobInstanceDetails\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb4\x01\n\x17PatchJobInstanceDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12instance_system_id\x18\x02 \x01(\t\x12@\n\x05state\x18\x03 \x01(\x0e21.google.cloud.osconfig.v1beta.Instance.PatchState\x12\x16\n\x0efailure_reason\x18\x04 \x01(\t\x12\x15\n\rattempt_count\x18\x05 \x01(\x03"b\n\x14ListPatchJobsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"l\n\x15ListPatchJobsResponse\x12:\n\npatch_jobs\x18\x01 \x03(\x0b2&.google.cloud.osconfig.v1beta.PatchJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc4\x0b\n\x08PatchJob\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x0e \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12;\n\x05state\x18\x05 \x01(\x0e2,.google.cloud.osconfig.v1beta.PatchJob.State\x12J\n\x0finstance_filter\x18\r \x01(\x0b21.google.cloud.osconfig.v1beta.PatchInstanceFilter\x12?\n\x0cpatch_config\x18\x07 \x01(\x0b2).google.cloud.osconfig.v1beta.PatchConfig\x12+\n\x08duration\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12_\n\x18instance_details_summary\x18\t \x01(\x0b2=.google.cloud.osconfig.v1beta.PatchJob.InstanceDetailsSummary\x12\x0f\n\x07dry_run\x18\n \x01(\x08\x12\x15\n\rerror_message\x18\x0b \x01(\t\x12\x18\n\x10percent_complete\x18\x0c \x01(\x01\x12\x1d\n\x10patch_deployment\x18\x0f \x01(\tB\x03\xe0A\x03\x12;\n\x07rollout\x18\x10 \x01(\x0b2*.google.cloud.osconfig.v1beta.PatchRollout\x1a\xbd\x04\n\x16InstanceDetailsSummary\x12\x1e\n\x16pending_instance_count\x18\x01 \x01(\x03\x12\x1f\n\x17inactive_instance_count\x18\x02 \x01(\x03\x12\x1f\n\x17notified_instance_count\x18\x03 \x01(\x03\x12\x1e\n\x16started_instance_count\x18\x04 \x01(\x03\x12*\n"downloading_patches_instance_count\x18\x05 \x01(\x03\x12\'\n\x1fapplying_patches_instance_count\x18\x06 \x01(\x03\x12 \n\x18rebooting_instance_count\x18\x07 \x01(\x03\x12 \n\x18succeeded_instance_count\x18\x08 \x01(\x03\x120\n(succeeded_reboot_required_instance_count\x18\t \x01(\x03\x12\x1d\n\x15failed_instance_count\x18\n \x01(\x03\x12\x1c\n\x14acked_instance_count\x18\x0b \x01(\x03\x12 \n\x18timed_out_instance_count\x18\x0c \x01(\x03\x12%\n\x1dpre_patch_step_instance_count\x18\r \x01(\x03\x12&\n\x1epost_patch_step_instance_count\x18\x0e \x01(\x03\x12(\n no_agent_detected_instance_count\x18\x0f \x01(\x03"\x95\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\x13\n\x0fINSTANCE_LOOKUP\x10\x02\x12\x0c\n\x08PATCHING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\x19\n\x15COMPLETED_WITH_ERRORS\x10\x05\x12\x0c\n\x08CANCELED\x10\x06\x12\r\n\tTIMED_OUT\x10\x07:O\xeaAL\n osconfig.googleapis.com/PatchJob\x12(projects/{project}/patchJobs/{patch_job}"\xf6\x04\n\x0bPatchConfig\x12M\n\rreboot_config\x18\x01 \x01(\x0e26.google.cloud.osconfig.v1beta.PatchConfig.RebootConfig\x126\n\x03apt\x18\x03 \x01(\x0b2).google.cloud.osconfig.v1beta.AptSettings\x126\n\x03yum\x18\x04 \x01(\x0b2).google.cloud.osconfig.v1beta.YumSettings\x126\n\x03goo\x18\x05 \x01(\x0b2).google.cloud.osconfig.v1beta.GooSettings\x12<\n\x06zypper\x18\x06 \x01(\x0b2,.google.cloud.osconfig.v1beta.ZypperSettings\x12K\n\x0ewindows_update\x18\x07 \x01(\x0b23.google.cloud.osconfig.v1beta.WindowsUpdateSettings\x128\n\x08pre_step\x18\x08 \x01(\x0b2&.google.cloud.osconfig.v1beta.ExecStep\x129\n\tpost_step\x18\t \x01(\x0b2&.google.cloud.osconfig.v1beta.ExecStep\x12\x1d\n\x15mig_instances_allowed\x18\n \x01(\x08"Q\n\x0cRebootConfig\x12\x1d\n\x19REBOOT_CONFIG_UNSPECIFIED\x10\x00\x12\x0b\n\x07DEFAULT\x10\x01\x12\n\n\x06ALWAYS\x10\x02\x12\t\n\x05NEVER\x10\x03"\xce\x02\n\x08Instance"\xc1\x02\n\nPatchState\x12\x1b\n\x17PATCH_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x12\x0c\n\x08NOTIFIED\x10\x03\x12\x0b\n\x07STARTED\x10\x04\x12\x17\n\x13DOWNLOADING_PATCHES\x10\x05\x12\x14\n\x10APPLYING_PATCHES\x10\x06\x12\r\n\tREBOOTING\x10\x07\x12\r\n\tSUCCEEDED\x10\x08\x12\x1d\n\x19SUCCEEDED_REBOOT_REQUIRED\x10\t\x12\n\n\x06FAILED\x10\n\x12\t\n\x05ACKED\x10\x0b\x12\r\n\tTIMED_OUT\x10\x0c\x12\x1a\n\x16RUNNING_PRE_PATCH_STEP\x10\r\x12\x1b\n\x17RUNNING_POST_PATCH_STEP\x10\x0e\x12\x15\n\x11NO_AGENT_DETECTED\x10\x0f"*\n\x15CancelPatchJobRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"\xae\x01\n\x0bAptSettings\x12<\n\x04type\x18\x01 \x01(\x0e2..google.cloud.osconfig.v1beta.AptSettings.Type\x12\x10\n\x08excludes\x18\x02 \x03(\t\x12\x1a\n\x12exclusive_packages\x18\x03 \x03(\t"3\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04DIST\x10\x01\x12\x0b\n\x07UPGRADE\x10\x02"^\n\x0bYumSettings\x12\x10\n\x08security\x18\x01 \x01(\x08\x12\x0f\n\x07minimal\x18\x02 \x01(\x08\x12\x10\n\x08excludes\x18\x03 \x03(\t\x12\x1a\n\x12exclusive_packages\x18\x04 \x03(\t"\r\n\x0bGooSettings"\x91\x01\n\x0eZypperSettings\x12\x15\n\rwith_optional\x18\x01 \x01(\x08\x12\x13\n\x0bwith_update\x18\x02 \x01(\x08\x12\x12\n\ncategories\x18\x03 \x03(\t\x12\x12\n\nseverities\x18\x04 \x03(\t\x12\x10\n\x08excludes\x18\x05 \x03(\t\x12\x19\n\x11exclusive_patches\x18\x06 \x03(\t"\xd9\x02\n\x15WindowsUpdateSettings\x12[\n\x0fclassifications\x18\x01 \x03(\x0e2B.google.cloud.osconfig.v1beta.WindowsUpdateSettings.Classification\x12\x10\n\x08excludes\x18\x02 \x03(\t\x12\x19\n\x11exclusive_patches\x18\x03 \x03(\t"\xb5\x01\n\x0eClassification\x12\x1e\n\x1aCLASSIFICATION_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\x0c\n\x08SECURITY\x10\x02\x12\x0e\n\nDEFINITION\x10\x03\x12\n\n\x06DRIVER\x10\x04\x12\x10\n\x0cFEATURE_PACK\x10\x05\x12\x10\n\x0cSERVICE_PACK\x10\x06\x12\x08\n\x04TOOL\x10\x07\x12\x11\n\rUPDATE_ROLLUP\x10\x08\x12\n\n\x06UPDATE\x10\t"\xa8\x01\n\x08ExecStep\x12L\n\x16linux_exec_step_config\x18\x01 \x01(\x0b2,.google.cloud.osconfig.v1beta.ExecStepConfig\x12N\n\x18windows_exec_step_config\x18\x02 \x01(\x0b2,.google.cloud.osconfig.v1beta.ExecStepConfig"\xa8\x02\n\x0eExecStepConfig\x12\x14\n\nlocal_path\x18\x01 \x01(\tH\x00\x12=\n\ngcs_object\x18\x02 \x01(\x0b2\'.google.cloud.osconfig.v1beta.GcsObjectH\x00\x12\x1d\n\x15allowed_success_codes\x18\x03 \x03(\x05\x12M\n\x0binterpreter\x18\x04 \x01(\x0e28.google.cloud.osconfig.v1beta.ExecStepConfig.Interpreter"E\n\x0bInterpreter\x12\x1b\n\x17INTERPRETER_UNSPECIFIED\x10\x00\x12\t\n\x05SHELL\x10\x01\x12\x0e\n\nPOWERSHELL\x10\x02B\x0c\n\nexecutable"U\n\tGcsObject\x12\x13\n\x06bucket\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06object\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11generation_number\x18\x03 \x01(\x03B\x03\xe0A\x02"\xd0\x02\n\x13PatchInstanceFilter\x12\x0b\n\x03all\x18\x01 \x01(\x08\x12R\n\x0cgroup_labels\x18\x02 \x03(\x0b2<.google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel\x12\r\n\x05zones\x18\x03 \x03(\t\x12\x11\n\tinstances\x18\x04 \x03(\t\x12\x1e\n\x16instance_name_prefixes\x18\x05 \x03(\t\x1a\x95\x01\n\nGroupLabel\x12X\n\x06labels\x18\x01 \x03(\x0b2H.google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xdc\x01\n\x0cPatchRollout\x12=\n\x04mode\x18\x01 \x01(\x0e2/.google.cloud.osconfig.v1beta.PatchRollout.Mode\x12G\n\x11disruption_budget\x18\x02 \x01(\x0b2,.google.cloud.osconfig.v1beta.FixedOrPercent"D\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x10\n\x0cZONE_BY_ZONE\x10\x01\x12\x14\n\x10CONCURRENT_ZONES\x10\x02Bk\n com.google.cloud.osconfig.v1betaB\tPatchJobsZ<cloud.google.com/go/osconfig/apiv1beta/osconfigpb;osconfigpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1beta.patch_jobs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.osconfig.v1betaB\tPatchJobsZ<cloud.google.com/go/osconfig/apiv1beta/osconfigpb;osconfigpb'
    _globals['_EXECUTEPATCHJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXECUTEPATCHJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_EXECUTEPATCHJOBREQUEST'].fields_by_name['instance_filter']._loaded_options = None
    _globals['_EXECUTEPATCHJOBREQUEST'].fields_by_name['instance_filter']._serialized_options = b'\xe0A\x02'
    _globals['_GETPATCHJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPATCHJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPATCHJOBINSTANCEDETAILSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPATCHJOBINSTANCEDETAILSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPATCHJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPATCHJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHJOB'].fields_by_name['patch_deployment']._loaded_options = None
    _globals['_PATCHJOB'].fields_by_name['patch_deployment']._serialized_options = b'\xe0A\x03'
    _globals['_PATCHJOB']._loaded_options = None
    _globals['_PATCHJOB']._serialized_options = b'\xeaAL\n osconfig.googleapis.com/PatchJob\x12(projects/{project}/patchJobs/{patch_job}'
    _globals['_CANCELPATCHJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELPATCHJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_GCSOBJECT'].fields_by_name['bucket']._loaded_options = None
    _globals['_GCSOBJECT'].fields_by_name['bucket']._serialized_options = b'\xe0A\x02'
    _globals['_GCSOBJECT'].fields_by_name['object']._loaded_options = None
    _globals['_GCSOBJECT'].fields_by_name['object']._serialized_options = b'\xe0A\x02'
    _globals['_GCSOBJECT'].fields_by_name['generation_number']._loaded_options = None
    _globals['_GCSOBJECT'].fields_by_name['generation_number']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL_LABELSENTRY']._loaded_options = None
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTEPATCHJOBREQUEST']._serialized_start = 257
    _globals['_EXECUTEPATCHJOBREQUEST']._serialized_end = 614
    _globals['_GETPATCHJOBREQUEST']._serialized_start = 616
    _globals['_GETPATCHJOBREQUEST']._serialized_end = 655
    _globals['_LISTPATCHJOBINSTANCEDETAILSREQUEST']._serialized_start = 657
    _globals['_LISTPATCHJOBINSTANCEDETAILSREQUEST']._serialized_end = 769
    _globals['_LISTPATCHJOBINSTANCEDETAILSRESPONSE']._serialized_start = 772
    _globals['_LISTPATCHJOBINSTANCEDETAILSRESPONSE']._serialized_end = 925
    _globals['_PATCHJOBINSTANCEDETAILS']._serialized_start = 928
    _globals['_PATCHJOBINSTANCEDETAILS']._serialized_end = 1108
    _globals['_LISTPATCHJOBSREQUEST']._serialized_start = 1110
    _globals['_LISTPATCHJOBSREQUEST']._serialized_end = 1208
    _globals['_LISTPATCHJOBSRESPONSE']._serialized_start = 1210
    _globals['_LISTPATCHJOBSRESPONSE']._serialized_end = 1318
    _globals['_PATCHJOB']._serialized_start = 1321
    _globals['_PATCHJOB']._serialized_end = 2797
    _globals['_PATCHJOB_INSTANCEDETAILSSUMMARY']._serialized_start = 1991
    _globals['_PATCHJOB_INSTANCEDETAILSSUMMARY']._serialized_end = 2564
    _globals['_PATCHJOB_STATE']._serialized_start = 2567
    _globals['_PATCHJOB_STATE']._serialized_end = 2716
    _globals['_PATCHCONFIG']._serialized_start = 2800
    _globals['_PATCHCONFIG']._serialized_end = 3430
    _globals['_PATCHCONFIG_REBOOTCONFIG']._serialized_start = 3349
    _globals['_PATCHCONFIG_REBOOTCONFIG']._serialized_end = 3430
    _globals['_INSTANCE']._serialized_start = 3433
    _globals['_INSTANCE']._serialized_end = 3767
    _globals['_INSTANCE_PATCHSTATE']._serialized_start = 3446
    _globals['_INSTANCE_PATCHSTATE']._serialized_end = 3767
    _globals['_CANCELPATCHJOBREQUEST']._serialized_start = 3769
    _globals['_CANCELPATCHJOBREQUEST']._serialized_end = 3811
    _globals['_APTSETTINGS']._serialized_start = 3814
    _globals['_APTSETTINGS']._serialized_end = 3988
    _globals['_APTSETTINGS_TYPE']._serialized_start = 3937
    _globals['_APTSETTINGS_TYPE']._serialized_end = 3988
    _globals['_YUMSETTINGS']._serialized_start = 3990
    _globals['_YUMSETTINGS']._serialized_end = 4084
    _globals['_GOOSETTINGS']._serialized_start = 4086
    _globals['_GOOSETTINGS']._serialized_end = 4099
    _globals['_ZYPPERSETTINGS']._serialized_start = 4102
    _globals['_ZYPPERSETTINGS']._serialized_end = 4247
    _globals['_WINDOWSUPDATESETTINGS']._serialized_start = 4250
    _globals['_WINDOWSUPDATESETTINGS']._serialized_end = 4595
    _globals['_WINDOWSUPDATESETTINGS_CLASSIFICATION']._serialized_start = 4414
    _globals['_WINDOWSUPDATESETTINGS_CLASSIFICATION']._serialized_end = 4595
    _globals['_EXECSTEP']._serialized_start = 4598
    _globals['_EXECSTEP']._serialized_end = 4766
    _globals['_EXECSTEPCONFIG']._serialized_start = 4769
    _globals['_EXECSTEPCONFIG']._serialized_end = 5065
    _globals['_EXECSTEPCONFIG_INTERPRETER']._serialized_start = 4982
    _globals['_EXECSTEPCONFIG_INTERPRETER']._serialized_end = 5051
    _globals['_GCSOBJECT']._serialized_start = 5067
    _globals['_GCSOBJECT']._serialized_end = 5152
    _globals['_PATCHINSTANCEFILTER']._serialized_start = 5155
    _globals['_PATCHINSTANCEFILTER']._serialized_end = 5491
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL']._serialized_start = 5342
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL']._serialized_end = 5491
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL_LABELSENTRY']._serialized_start = 5446
    _globals['_PATCHINSTANCEFILTER_GROUPLABEL_LABELSENTRY']._serialized_end = 5491
    _globals['_PATCHROLLOUT']._serialized_start = 5494
    _globals['_PATCHROLLOUT']._serialized_end = 5714
    _globals['_PATCHROLLOUT_MODE']._serialized_start = 5646
    _globals['_PATCHROLLOUT_MODE']._serialized_end = 5714