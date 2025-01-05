"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/agentendpoint/v1/patch_jobs.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/osconfig/agentendpoint/v1/patch_jobs.proto\x12&google.cloud.osconfig.agentendpoint.v1"\x95\x06\n\x0bPatchConfig\x12W\n\rreboot_config\x18\x01 \x01(\x0e2@.google.cloud.osconfig.agentendpoint.v1.PatchConfig.RebootConfig\x12M\n\x0eretry_strategy\x18\x02 \x01(\x0b25.google.cloud.osconfig.agentendpoint.v1.RetryStrategy\x12@\n\x03apt\x18\x03 \x01(\x0b23.google.cloud.osconfig.agentendpoint.v1.AptSettings\x12@\n\x03yum\x18\x04 \x01(\x0b23.google.cloud.osconfig.agentendpoint.v1.YumSettings\x12@\n\x03goo\x18\x05 \x01(\x0b23.google.cloud.osconfig.agentendpoint.v1.GooSettings\x12F\n\x06zypper\x18\x06 \x01(\x0b26.google.cloud.osconfig.agentendpoint.v1.ZypperSettings\x12U\n\x0ewindows_update\x18\x07 \x01(\x0b2=.google.cloud.osconfig.agentendpoint.v1.WindowsUpdateSettings\x12B\n\x08pre_step\x18\x08 \x01(\x0b20.google.cloud.osconfig.agentendpoint.v1.ExecStep\x12C\n\tpost_step\x18\t \x01(\x0b20.google.cloud.osconfig.agentendpoint.v1.ExecStep\x12\x1d\n\x15mig_instances_allowed\x18\n \x01(\x08"Q\n\x0cRebootConfig\x12\x1d\n\x19REBOOT_CONFIG_UNSPECIFIED\x10\x00\x12\x0b\n\x07DEFAULT\x10\x01\x12\n\n\x06ALWAYS\x10\x02\x12\t\n\x05NEVER\x10\x03"\xb8\x01\n\x0bAptSettings\x12F\n\x04type\x18\x01 \x01(\x0e28.google.cloud.osconfig.agentendpoint.v1.AptSettings.Type\x12\x10\n\x08excludes\x18\x02 \x03(\t\x12\x1a\n\x12exclusive_packages\x18\x03 \x03(\t"3\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04DIST\x10\x01\x12\x0b\n\x07UPGRADE\x10\x02"^\n\x0bYumSettings\x12\x10\n\x08security\x18\x01 \x01(\x08\x12\x0f\n\x07minimal\x18\x02 \x01(\x08\x12\x10\n\x08excludes\x18\x03 \x03(\t\x12\x1a\n\x12exclusive_packages\x18\x04 \x03(\t"\r\n\x0bGooSettings"\x91\x01\n\x0eZypperSettings\x12\x15\n\rwith_optional\x18\x01 \x01(\x08\x12\x13\n\x0bwith_update\x18\x02 \x01(\x08\x12\x12\n\ncategories\x18\x03 \x03(\t\x12\x12\n\nseverities\x18\x04 \x03(\t\x12\x10\n\x08excludes\x18\x05 \x03(\t\x12\x19\n\x11exclusive_patches\x18\x06 \x03(\t"\xe3\x02\n\x15WindowsUpdateSettings\x12e\n\x0fclassifications\x18\x01 \x03(\x0e2L.google.cloud.osconfig.agentendpoint.v1.WindowsUpdateSettings.Classification\x12\x10\n\x08excludes\x18\x02 \x03(\t\x12\x19\n\x11exclusive_patches\x18\x03 \x03(\t"\xb5\x01\n\x0eClassification\x12\x1e\n\x1aCLASSIFICATION_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\x0c\n\x08SECURITY\x10\x02\x12\x0e\n\nDEFINITION\x10\x03\x12\n\n\x06DRIVER\x10\x04\x12\x10\n\x0cFEATURE_PACK\x10\x05\x12\x10\n\x0cSERVICE_PACK\x10\x06\x12\x08\n\x04TOOL\x10\x07\x12\x11\n\rUPDATE_ROLLUP\x10\x08\x12\n\n\x06UPDATE\x10\t" \n\rRetryStrategy\x12\x0f\n\x07enabled\x18\x01 \x01(\x08"\xbc\x01\n\x08ExecStep\x12V\n\x16linux_exec_step_config\x18\x01 \x01(\x0b26.google.cloud.osconfig.agentendpoint.v1.ExecStepConfig\x12X\n\x18windows_exec_step_config\x18\x02 \x01(\x0b26.google.cloud.osconfig.agentendpoint.v1.ExecStepConfig"\xc6\x02\n\x0eExecStepConfig\x12\x14\n\nlocal_path\x18\x01 \x01(\tH\x00\x12G\n\ngcs_object\x18\x02 \x01(\x0b21.google.cloud.osconfig.agentendpoint.v1.GcsObjectH\x00\x12\x1d\n\x15allowed_success_codes\x18\x03 \x03(\x05\x12W\n\x0binterpreter\x18\x04 \x01(\x0e2B.google.cloud.osconfig.agentendpoint.v1.ExecStepConfig.Interpreter"O\n\x0bInterpreter\x12\x1b\n\x17INTERPRETER_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x03\x12\t\n\x05SHELL\x10\x01\x12\x0e\n\nPOWERSHELL\x10\x02B\x0c\n\nexecutable"F\n\tGcsObject\x12\x0e\n\x06bucket\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12\x19\n\x11generation_number\x18\x03 \x01(\x03B\x89\x01\n*com.google.cloud.osconfig.agentendpoint.v1B\tPatchJobsZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.agentendpoint.v1.patch_jobs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.osconfig.agentendpoint.v1B\tPatchJobsZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpb'
    _globals['_PATCHCONFIG']._serialized_start = 100
    _globals['_PATCHCONFIG']._serialized_end = 889
    _globals['_PATCHCONFIG_REBOOTCONFIG']._serialized_start = 808
    _globals['_PATCHCONFIG_REBOOTCONFIG']._serialized_end = 889
    _globals['_APTSETTINGS']._serialized_start = 892
    _globals['_APTSETTINGS']._serialized_end = 1076
    _globals['_APTSETTINGS_TYPE']._serialized_start = 1025
    _globals['_APTSETTINGS_TYPE']._serialized_end = 1076
    _globals['_YUMSETTINGS']._serialized_start = 1078
    _globals['_YUMSETTINGS']._serialized_end = 1172
    _globals['_GOOSETTINGS']._serialized_start = 1174
    _globals['_GOOSETTINGS']._serialized_end = 1187
    _globals['_ZYPPERSETTINGS']._serialized_start = 1190
    _globals['_ZYPPERSETTINGS']._serialized_end = 1335
    _globals['_WINDOWSUPDATESETTINGS']._serialized_start = 1338
    _globals['_WINDOWSUPDATESETTINGS']._serialized_end = 1693
    _globals['_WINDOWSUPDATESETTINGS_CLASSIFICATION']._serialized_start = 1512
    _globals['_WINDOWSUPDATESETTINGS_CLASSIFICATION']._serialized_end = 1693
    _globals['_RETRYSTRATEGY']._serialized_start = 1695
    _globals['_RETRYSTRATEGY']._serialized_end = 1727
    _globals['_EXECSTEP']._serialized_start = 1730
    _globals['_EXECSTEP']._serialized_end = 1918
    _globals['_EXECSTEPCONFIG']._serialized_start = 1921
    _globals['_EXECSTEPCONFIG']._serialized_end = 2247
    _globals['_EXECSTEPCONFIG_INTERPRETER']._serialized_start = 2154
    _globals['_EXECSTEPCONFIG_INTERPRETER']._serialized_end = 2233
    _globals['_GCSOBJECT']._serialized_start = 2249
    _globals['_GCSOBJECT']._serialized_end = 2319