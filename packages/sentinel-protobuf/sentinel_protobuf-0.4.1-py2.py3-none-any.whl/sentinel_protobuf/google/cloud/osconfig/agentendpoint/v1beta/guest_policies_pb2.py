"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/agentendpoint/v1beta/guest_policies.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/osconfig/agentendpoint/v1beta/guest_policies.proto\x12*google.cloud.osconfig.agentendpoint.v1beta\x1a\x1fgoogle/api/field_behavior.proto"\x8a\x02\n\x07Package\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\rdesired_state\x18\x02 \x01(\x0e28.google.cloud.osconfig.agentendpoint.v1beta.DesiredState\x12L\n\x07manager\x18\x03 \x01(\x0e2;.google.cloud.osconfig.agentendpoint.v1beta.Package.Manager"R\n\x07Manager\x12\x17\n\x13MANAGER_UNSPECIFIED\x10\x00\x12\x07\n\x03ANY\x10\x01\x12\x07\n\x03APT\x10\x02\x12\x07\n\x03YUM\x10\x03\x12\n\n\x06ZYPPER\x10\x04\x12\x07\n\x03GOO\x10\x05"\xf7\x01\n\rAptRepository\x12[\n\x0carchive_type\x18\x01 \x01(\x0e2E.google.cloud.osconfig.agentendpoint.v1beta.AptRepository.ArchiveType\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x14\n\x0cdistribution\x18\x03 \x01(\t\x12\x12\n\ncomponents\x18\x04 \x03(\t\x12\x0f\n\x07gpg_key\x18\x05 \x01(\t"A\n\x0bArchiveType\x12\x1c\n\x18ARCHIVE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03DEB\x10\x01\x12\x0b\n\x07DEB_SRC\x10\x02"U\n\rYumRepository\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x10\n\x08base_url\x18\x03 \x01(\t\x12\x10\n\x08gpg_keys\x18\x04 \x03(\t"X\n\x10ZypperRepository\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x10\n\x08base_url\x18\x03 \x01(\t\x12\x10\n\x08gpg_keys\x18\x04 \x03(\t"*\n\rGooRepository\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t"\xcf\x02\n\x11PackageRepository\x12H\n\x03apt\x18\x01 \x01(\x0b29.google.cloud.osconfig.agentendpoint.v1beta.AptRepositoryH\x00\x12H\n\x03yum\x18\x02 \x01(\x0b29.google.cloud.osconfig.agentendpoint.v1beta.YumRepositoryH\x00\x12N\n\x06zypper\x18\x03 \x01(\x0b2<.google.cloud.osconfig.agentendpoint.v1beta.ZypperRepositoryH\x00\x12H\n\x03goo\x18\x04 \x01(\x0b29.google.cloud.osconfig.agentendpoint.v1beta.GooRepositoryH\x00B\x0c\n\nrepository"\xa6\x12\n\x0eSoftwareRecipe\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12V\n\tartifacts\x18\x03 \x03(\x0b2C.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Artifact\x12V\n\rinstall_steps\x18\x04 \x03(\x0b2?.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step\x12U\n\x0cupdate_steps\x18\x05 \x03(\x0b2?.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step\x12O\n\rdesired_state\x18\x06 \x01(\x0e28.google.cloud.osconfig.agentendpoint.v1beta.DesiredState\x1a\xd4\x02\n\x08Artifact\x12\n\n\x02id\x18\x01 \x01(\t\x12\\\n\x06remote\x18\x02 \x01(\x0b2J.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Artifact.RemoteH\x00\x12V\n\x03gcs\x18\x03 \x01(\x0b2G.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Artifact.GcsH\x00\x12\x16\n\x0eallow_insecure\x18\x04 \x01(\x08\x1a\'\n\x06Remote\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x10\n\x08checksum\x18\x02 \x01(\t\x1a9\n\x03Gcs\x12\x0e\n\x06bucket\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12\x12\n\ngeneration\x18\x03 \x01(\x03B\n\n\x08artifact\x1a\xc5\x0c\n\x04Step\x12]\n\tfile_copy\x18\x01 \x01(\x0b2H.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step.CopyFileH\x00\x12l\n\x12archive_extraction\x18\x02 \x01(\x0b2N.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step.ExtractArchiveH\x00\x12f\n\x10msi_installation\x18\x03 \x01(\x0b2J.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step.InstallMsiH\x00\x12h\n\x11dpkg_installation\x18\x04 \x01(\x0b2K.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step.InstallDpkgH\x00\x12f\n\x10rpm_installation\x18\x05 \x01(\x0b2J.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step.InstallRpmH\x00\x12]\n\tfile_exec\x18\x06 \x01(\x0b2H.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step.ExecFileH\x00\x12_\n\nscript_run\x18\x07 \x01(\x0b2I.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step.RunScriptH\x00\x1a\\\n\x08CopyFile\x12\x13\n\x0bartifact_id\x18\x01 \x01(\t\x12\x13\n\x0bdestination\x18\x02 \x01(\t\x12\x11\n\toverwrite\x18\x03 \x01(\x08\x12\x13\n\x0bpermissions\x18\x04 \x01(\t\x1a\x99\x02\n\x0eExtractArchive\x12\x13\n\x0bartifact_id\x18\x01 \x01(\t\x12\x13\n\x0bdestination\x18\x02 \x01(\t\x12h\n\x04type\x18\x03 \x01(\x0e2Z.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step.ExtractArchive.ArchiveType"s\n\x0bArchiveType\x12\x1c\n\x18ARCHIVE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03TAR\x10\x01\x12\x0c\n\x08TAR_GZIP\x10\x02\x12\x0c\n\x08TAR_BZIP\x10\x03\x12\x0c\n\x08TAR_LZMA\x10\x04\x12\n\n\x06TAR_XZ\x10\x05\x12\x07\n\x03ZIP\x10\x0b\x1aL\n\nInstallMsi\x12\x13\n\x0bartifact_id\x18\x01 \x01(\t\x12\r\n\x05flags\x18\x02 \x03(\t\x12\x1a\n\x12allowed_exit_codes\x18\x03 \x03(\x05\x1a"\n\x0bInstallDpkg\x12\x13\n\x0bartifact_id\x18\x01 \x01(\t\x1a!\n\nInstallRpm\x12\x13\n\x0bartifact_id\x18\x01 \x01(\t\x1ar\n\x08ExecFile\x12\x15\n\x0bartifact_id\x18\x01 \x01(\tH\x00\x12\x14\n\nlocal_path\x18\x02 \x01(\tH\x00\x12\x0c\n\x04args\x18\x03 \x03(\t\x12\x1a\n\x12allowed_exit_codes\x18\x04 \x03(\x05B\x0f\n\rlocation_type\x1a\xea\x01\n\tRunScript\x12\x0e\n\x06script\x18\x01 \x01(\t\x12\x1a\n\x12allowed_exit_codes\x18\x02 \x03(\x05\x12j\n\x0binterpreter\x18\x03 \x01(\x0e2U.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe.Step.RunScript.Interpreter"E\n\x0bInterpreter\x12\x1b\n\x17INTERPRETER_UNSPECIFIED\x10\x00\x12\t\n\x05SHELL\x10\x01\x12\x0e\n\nPOWERSHELL\x10\x03B\x06\n\x04step"\x87\x01\n!LookupEffectiveGuestPolicyRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\ros_short_name\x18\x02 \x01(\t\x12\x12\n\nos_version\x18\x03 \x01(\t\x12\x17\n\x0fos_architecture\x18\x04 \x01(\t"\xd2\x05\n\x14EffectiveGuestPolicy\x12a\n\x08packages\x18\x01 \x03(\x0b2O.google.cloud.osconfig.agentendpoint.v1beta.EffectiveGuestPolicy.SourcedPackage\x12w\n\x14package_repositories\x18\x02 \x03(\x0b2Y.google.cloud.osconfig.agentendpoint.v1beta.EffectiveGuestPolicy.SourcedPackageRepository\x12p\n\x10software_recipes\x18\x03 \x03(\x0b2V.google.cloud.osconfig.agentendpoint.v1beta.EffectiveGuestPolicy.SourcedSoftwareRecipe\x1af\n\x0eSourcedPackage\x12\x0e\n\x06source\x18\x01 \x01(\t\x12D\n\x07package\x18\x02 \x01(\x0b23.google.cloud.osconfig.agentendpoint.v1beta.Package\x1a\x85\x01\n\x18SourcedPackageRepository\x12\x0e\n\x06source\x18\x01 \x01(\t\x12Y\n\x12package_repository\x18\x02 \x01(\x0b2=.google.cloud.osconfig.agentendpoint.v1beta.PackageRepository\x1a|\n\x15SourcedSoftwareRecipe\x12\x0e\n\x06source\x18\x01 \x01(\t\x12S\n\x0fsoftware_recipe\x18\x02 \x01(\x0b2:.google.cloud.osconfig.agentendpoint.v1beta.SoftwareRecipe*V\n\x0cDesiredState\x12\x1d\n\x19DESIRED_STATE_UNSPECIFIED\x10\x00\x12\r\n\tINSTALLED\x10\x01\x12\x0b\n\x07UPDATED\x10\x02\x12\x0b\n\x07REMOVED\x10\x03B\xb4\x01\n.com.google.cloud.osconfig.agentendpoint.v1betaB\rGuestPoliciesZTcloud.google.com/go/osconfig/agentendpoint/apiv1beta/agentendpointpb;agentendpointpb\xca\x02\x1cGoogle\\Cloud\\OsConfig\\V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.agentendpoint.v1beta.guest_policies_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.cloud.osconfig.agentendpoint.v1betaB\rGuestPoliciesZTcloud.google.com/go/osconfig/agentendpoint/apiv1beta/agentendpointpb;agentendpointpb\xca\x02\x1cGoogle\\Cloud\\OsConfig\\V1beta'
    _globals['_LOOKUPEFFECTIVEGUESTPOLICYREQUEST'].fields_by_name['instance_id_token']._loaded_options = None
    _globals['_LOOKUPEFFECTIVEGUESTPOLICYREQUEST'].fields_by_name['instance_id_token']._serialized_options = b'\xe0A\x02'
    _globals['_DESIREDSTATE']._serialized_start = 4430
    _globals['_DESIREDSTATE']._serialized_end = 4516
    _globals['_PACKAGE']._serialized_start = 145
    _globals['_PACKAGE']._serialized_end = 411
    _globals['_PACKAGE_MANAGER']._serialized_start = 329
    _globals['_PACKAGE_MANAGER']._serialized_end = 411
    _globals['_APTREPOSITORY']._serialized_start = 414
    _globals['_APTREPOSITORY']._serialized_end = 661
    _globals['_APTREPOSITORY_ARCHIVETYPE']._serialized_start = 596
    _globals['_APTREPOSITORY_ARCHIVETYPE']._serialized_end = 661
    _globals['_YUMREPOSITORY']._serialized_start = 663
    _globals['_YUMREPOSITORY']._serialized_end = 748
    _globals['_ZYPPERREPOSITORY']._serialized_start = 750
    _globals['_ZYPPERREPOSITORY']._serialized_end = 838
    _globals['_GOOREPOSITORY']._serialized_start = 840
    _globals['_GOOREPOSITORY']._serialized_end = 882
    _globals['_PACKAGEREPOSITORY']._serialized_start = 885
    _globals['_PACKAGEREPOSITORY']._serialized_end = 1220
    _globals['_SOFTWARERECIPE']._serialized_start = 1223
    _globals['_SOFTWARERECIPE']._serialized_end = 3565
    _globals['_SOFTWARERECIPE_ARTIFACT']._serialized_start = 1617
    _globals['_SOFTWARERECIPE_ARTIFACT']._serialized_end = 1957
    _globals['_SOFTWARERECIPE_ARTIFACT_REMOTE']._serialized_start = 1847
    _globals['_SOFTWARERECIPE_ARTIFACT_REMOTE']._serialized_end = 1886
    _globals['_SOFTWARERECIPE_ARTIFACT_GCS']._serialized_start = 1888
    _globals['_SOFTWARERECIPE_ARTIFACT_GCS']._serialized_end = 1945
    _globals['_SOFTWARERECIPE_STEP']._serialized_start = 1960
    _globals['_SOFTWARERECIPE_STEP']._serialized_end = 3565
    _globals['_SOFTWARERECIPE_STEP_COPYFILE']._serialized_start = 2679
    _globals['_SOFTWARERECIPE_STEP_COPYFILE']._serialized_end = 2771
    _globals['_SOFTWARERECIPE_STEP_EXTRACTARCHIVE']._serialized_start = 2774
    _globals['_SOFTWARERECIPE_STEP_EXTRACTARCHIVE']._serialized_end = 3055
    _globals['_SOFTWARERECIPE_STEP_EXTRACTARCHIVE_ARCHIVETYPE']._serialized_start = 2940
    _globals['_SOFTWARERECIPE_STEP_EXTRACTARCHIVE_ARCHIVETYPE']._serialized_end = 3055
    _globals['_SOFTWARERECIPE_STEP_INSTALLMSI']._serialized_start = 3057
    _globals['_SOFTWARERECIPE_STEP_INSTALLMSI']._serialized_end = 3133
    _globals['_SOFTWARERECIPE_STEP_INSTALLDPKG']._serialized_start = 3135
    _globals['_SOFTWARERECIPE_STEP_INSTALLDPKG']._serialized_end = 3169
    _globals['_SOFTWARERECIPE_STEP_INSTALLRPM']._serialized_start = 3171
    _globals['_SOFTWARERECIPE_STEP_INSTALLRPM']._serialized_end = 3204
    _globals['_SOFTWARERECIPE_STEP_EXECFILE']._serialized_start = 3206
    _globals['_SOFTWARERECIPE_STEP_EXECFILE']._serialized_end = 3320
    _globals['_SOFTWARERECIPE_STEP_RUNSCRIPT']._serialized_start = 3323
    _globals['_SOFTWARERECIPE_STEP_RUNSCRIPT']._serialized_end = 3557
    _globals['_SOFTWARERECIPE_STEP_RUNSCRIPT_INTERPRETER']._serialized_start = 3488
    _globals['_SOFTWARERECIPE_STEP_RUNSCRIPT_INTERPRETER']._serialized_end = 3557
    _globals['_LOOKUPEFFECTIVEGUESTPOLICYREQUEST']._serialized_start = 3568
    _globals['_LOOKUPEFFECTIVEGUESTPOLICYREQUEST']._serialized_end = 3703
    _globals['_EFFECTIVEGUESTPOLICY']._serialized_start = 3706
    _globals['_EFFECTIVEGUESTPOLICY']._serialized_end = 4428
    _globals['_EFFECTIVEGUESTPOLICY_SOURCEDPACKAGE']._serialized_start = 4064
    _globals['_EFFECTIVEGUESTPOLICY_SOURCEDPACKAGE']._serialized_end = 4166
    _globals['_EFFECTIVEGUESTPOLICY_SOURCEDPACKAGEREPOSITORY']._serialized_start = 4169
    _globals['_EFFECTIVEGUESTPOLICY_SOURCEDPACKAGEREPOSITORY']._serialized_end = 4302
    _globals['_EFFECTIVEGUESTPOLICY_SOURCEDSOFTWARERECIPE']._serialized_start = 4304
    _globals['_EFFECTIVEGUESTPOLICY_SOURCEDSOFTWARERECIPE']._serialized_end = 4428