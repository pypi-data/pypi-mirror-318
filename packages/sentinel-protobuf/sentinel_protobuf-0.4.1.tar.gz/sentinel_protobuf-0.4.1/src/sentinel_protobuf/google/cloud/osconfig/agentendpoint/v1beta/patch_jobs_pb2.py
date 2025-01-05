"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/agentendpoint/v1beta/patch_jobs.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/osconfig/agentendpoint/v1beta/patch_jobs.proto\x12*google.cloud.osconfig.agentendpoint.v1beta"\xb9\x06\n\x0bPatchConfig\x12[\n\rreboot_config\x18\x01 \x01(\x0e2D.google.cloud.osconfig.agentendpoint.v1beta.PatchConfig.RebootConfig\x12Q\n\x0eretry_strategy\x18\x02 \x01(\x0b29.google.cloud.osconfig.agentendpoint.v1beta.RetryStrategy\x12D\n\x03apt\x18\x03 \x01(\x0b27.google.cloud.osconfig.agentendpoint.v1beta.AptSettings\x12D\n\x03yum\x18\x04 \x01(\x0b27.google.cloud.osconfig.agentendpoint.v1beta.YumSettings\x12D\n\x03goo\x18\x05 \x01(\x0b27.google.cloud.osconfig.agentendpoint.v1beta.GooSettings\x12J\n\x06zypper\x18\x06 \x01(\x0b2:.google.cloud.osconfig.agentendpoint.v1beta.ZypperSettings\x12Y\n\x0ewindows_update\x18\x07 \x01(\x0b2A.google.cloud.osconfig.agentendpoint.v1beta.WindowsUpdateSettings\x12F\n\x08pre_step\x18\x08 \x01(\x0b24.google.cloud.osconfig.agentendpoint.v1beta.ExecStep\x12G\n\tpost_step\x18\t \x01(\x0b24.google.cloud.osconfig.agentendpoint.v1beta.ExecStep\x12\x1d\n\x15mig_instances_allowed\x18\n \x01(\x08"Q\n\x0cRebootConfig\x12\x1d\n\x19REBOOT_CONFIG_UNSPECIFIED\x10\x00\x12\x0b\n\x07DEFAULT\x10\x01\x12\n\n\x06ALWAYS\x10\x02\x12\t\n\x05NEVER\x10\x03"\xbc\x01\n\x0bAptSettings\x12J\n\x04type\x18\x01 \x01(\x0e2<.google.cloud.osconfig.agentendpoint.v1beta.AptSettings.Type\x12\x10\n\x08excludes\x18\x02 \x03(\t\x12\x1a\n\x12exclusive_packages\x18\x03 \x03(\t"3\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04DIST\x10\x01\x12\x0b\n\x07UPGRADE\x10\x02"^\n\x0bYumSettings\x12\x10\n\x08security\x18\x01 \x01(\x08\x12\x0f\n\x07minimal\x18\x02 \x01(\x08\x12\x10\n\x08excludes\x18\x03 \x03(\t\x12\x1a\n\x12exclusive_packages\x18\x04 \x03(\t"\r\n\x0bGooSettings"\x91\x01\n\x0eZypperSettings\x12\x15\n\rwith_optional\x18\x01 \x01(\x08\x12\x13\n\x0bwith_update\x18\x02 \x01(\x08\x12\x12\n\ncategories\x18\x03 \x03(\t\x12\x12\n\nseverities\x18\x04 \x03(\t\x12\x10\n\x08excludes\x18\x05 \x03(\t\x12\x19\n\x11exclusive_patches\x18\x06 \x03(\t"\xe7\x02\n\x15WindowsUpdateSettings\x12i\n\x0fclassifications\x18\x01 \x03(\x0e2P.google.cloud.osconfig.agentendpoint.v1beta.WindowsUpdateSettings.Classification\x12\x10\n\x08excludes\x18\x02 \x03(\t\x12\x19\n\x11exclusive_patches\x18\x03 \x03(\t"\xb5\x01\n\x0eClassification\x12\x1e\n\x1aCLASSIFICATION_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\x0c\n\x08SECURITY\x10\x02\x12\x0e\n\nDEFINITION\x10\x03\x12\n\n\x06DRIVER\x10\x04\x12\x10\n\x0cFEATURE_PACK\x10\x05\x12\x10\n\x0cSERVICE_PACK\x10\x06\x12\x08\n\x04TOOL\x10\x07\x12\x11\n\rUPDATE_ROLLUP\x10\x08\x12\n\n\x06UPDATE\x10\t" \n\rRetryStrategy\x12\x0f\n\x07enabled\x18\x01 \x01(\x08"\xc4\x01\n\x08ExecStep\x12Z\n\x16linux_exec_step_config\x18\x01 \x01(\x0b2:.google.cloud.osconfig.agentendpoint.v1beta.ExecStepConfig\x12\\\n\x18windows_exec_step_config\x18\x02 \x01(\x0b2:.google.cloud.osconfig.agentendpoint.v1beta.ExecStepConfig"\xce\x02\n\x0eExecStepConfig\x12\x14\n\nlocal_path\x18\x01 \x01(\tH\x00\x12K\n\ngcs_object\x18\x02 \x01(\x0b25.google.cloud.osconfig.agentendpoint.v1beta.GcsObjectH\x00\x12\x1d\n\x15allowed_success_codes\x18\x03 \x03(\x05\x12[\n\x0binterpreter\x18\x04 \x01(\x0e2F.google.cloud.osconfig.agentendpoint.v1beta.ExecStepConfig.Interpreter"O\n\x0bInterpreter\x12\x1b\n\x17INTERPRETER_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x03\x12\t\n\x05SHELL\x10\x01\x12\x0e\n\nPOWERSHELL\x10\x02B\x0c\n\nexecutable"F\n\tGcsObject\x12\x0e\n\x06bucket\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12\x19\n\x11generation_number\x18\x03 \x01(\x03B\xb0\x01\n.com.google.cloud.osconfig.agentendpoint.v1betaB\tPatchJobsZTcloud.google.com/go/osconfig/agentendpoint/apiv1beta/agentendpointpb;agentendpointpb\xca\x02\x1cGoogle\\Cloud\\OsConfig\\V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.agentendpoint.v1beta.patch_jobs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.cloud.osconfig.agentendpoint.v1betaB\tPatchJobsZTcloud.google.com/go/osconfig/agentendpoint/apiv1beta/agentendpointpb;agentendpointpb\xca\x02\x1cGoogle\\Cloud\\OsConfig\\V1beta'
    _globals['_PATCHCONFIG']._serialized_start = 108
    _globals['_PATCHCONFIG']._serialized_end = 933
    _globals['_PATCHCONFIG_REBOOTCONFIG']._serialized_start = 852
    _globals['_PATCHCONFIG_REBOOTCONFIG']._serialized_end = 933
    _globals['_APTSETTINGS']._serialized_start = 936
    _globals['_APTSETTINGS']._serialized_end = 1124
    _globals['_APTSETTINGS_TYPE']._serialized_start = 1073
    _globals['_APTSETTINGS_TYPE']._serialized_end = 1124
    _globals['_YUMSETTINGS']._serialized_start = 1126
    _globals['_YUMSETTINGS']._serialized_end = 1220
    _globals['_GOOSETTINGS']._serialized_start = 1222
    _globals['_GOOSETTINGS']._serialized_end = 1235
    _globals['_ZYPPERSETTINGS']._serialized_start = 1238
    _globals['_ZYPPERSETTINGS']._serialized_end = 1383
    _globals['_WINDOWSUPDATESETTINGS']._serialized_start = 1386
    _globals['_WINDOWSUPDATESETTINGS']._serialized_end = 1745
    _globals['_WINDOWSUPDATESETTINGS_CLASSIFICATION']._serialized_start = 1564
    _globals['_WINDOWSUPDATESETTINGS_CLASSIFICATION']._serialized_end = 1745
    _globals['_RETRYSTRATEGY']._serialized_start = 1747
    _globals['_RETRYSTRATEGY']._serialized_end = 1779
    _globals['_EXECSTEP']._serialized_start = 1782
    _globals['_EXECSTEP']._serialized_end = 1978
    _globals['_EXECSTEPCONFIG']._serialized_start = 1981
    _globals['_EXECSTEPCONFIG']._serialized_end = 2315
    _globals['_EXECSTEPCONFIG_INTERPRETER']._serialized_start = 2222
    _globals['_EXECSTEPCONFIG_INTERPRETER']._serialized_end = 2301
    _globals['_GCSOBJECT']._serialized_start = 2317
    _globals['_GCSOBJECT']._serialized_end = 2387