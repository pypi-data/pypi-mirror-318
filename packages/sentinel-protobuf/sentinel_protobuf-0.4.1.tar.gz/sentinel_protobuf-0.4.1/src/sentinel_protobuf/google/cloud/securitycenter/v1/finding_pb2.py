"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/finding.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v1 import access_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_access__pb2
from .....google.cloud.securitycenter.v1 import application_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_application__pb2
from .....google.cloud.securitycenter.v1 import attack_exposure_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_attack__exposure__pb2
from .....google.cloud.securitycenter.v1 import backup_disaster_recovery_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_backup__disaster__recovery__pb2
from .....google.cloud.securitycenter.v1 import cloud_armor_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_cloud__armor__pb2
from .....google.cloud.securitycenter.v1 import cloud_dlp_data_profile_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_cloud__dlp__data__profile__pb2
from .....google.cloud.securitycenter.v1 import cloud_dlp_inspection_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_cloud__dlp__inspection__pb2
from .....google.cloud.securitycenter.v1 import compliance_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_compliance__pb2
from .....google.cloud.securitycenter.v1 import connection_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_connection__pb2
from .....google.cloud.securitycenter.v1 import contact_details_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_contact__details__pb2
from .....google.cloud.securitycenter.v1 import container_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_container__pb2
from .....google.cloud.securitycenter.v1 import database_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_database__pb2
from .....google.cloud.securitycenter.v1 import exfiltration_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_exfiltration__pb2
from .....google.cloud.securitycenter.v1 import external_system_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_external__system__pb2
from .....google.cloud.securitycenter.v1 import file_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_file__pb2
from .....google.cloud.securitycenter.v1 import group_membership_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_group__membership__pb2
from .....google.cloud.securitycenter.v1 import iam_binding_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_iam__binding__pb2
from .....google.cloud.securitycenter.v1 import indicator_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_indicator__pb2
from .....google.cloud.securitycenter.v1 import kernel_rootkit_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_kernel__rootkit__pb2
from .....google.cloud.securitycenter.v1 import kubernetes_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_kubernetes__pb2
from .....google.cloud.securitycenter.v1 import load_balancer_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_load__balancer__pb2
from .....google.cloud.securitycenter.v1 import log_entry_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_log__entry__pb2
from .....google.cloud.securitycenter.v1 import mitre_attack_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_mitre__attack__pb2
from .....google.cloud.securitycenter.v1 import notebook_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_notebook__pb2
from .....google.cloud.securitycenter.v1 import org_policy_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_org__policy__pb2
from .....google.cloud.securitycenter.v1 import process_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_process__pb2
from .....google.cloud.securitycenter.v1 import security_marks_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_security__marks__pb2
from .....google.cloud.securitycenter.v1 import security_posture_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_security__posture__pb2
from .....google.cloud.securitycenter.v1 import toxic_combination_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_toxic__combination__pb2
from .....google.cloud.securitycenter.v1 import vulnerability_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_vulnerability__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/securitycenter/v1/finding.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/securitycenter/v1/access.proto\x1a0google/cloud/securitycenter/v1/application.proto\x1a4google/cloud/securitycenter/v1/attack_exposure.proto\x1a=google/cloud/securitycenter/v1/backup_disaster_recovery.proto\x1a0google/cloud/securitycenter/v1/cloud_armor.proto\x1a;google/cloud/securitycenter/v1/cloud_dlp_data_profile.proto\x1a9google/cloud/securitycenter/v1/cloud_dlp_inspection.proto\x1a/google/cloud/securitycenter/v1/compliance.proto\x1a/google/cloud/securitycenter/v1/connection.proto\x1a4google/cloud/securitycenter/v1/contact_details.proto\x1a.google/cloud/securitycenter/v1/container.proto\x1a-google/cloud/securitycenter/v1/database.proto\x1a1google/cloud/securitycenter/v1/exfiltration.proto\x1a4google/cloud/securitycenter/v1/external_system.proto\x1a)google/cloud/securitycenter/v1/file.proto\x1a5google/cloud/securitycenter/v1/group_membership.proto\x1a0google/cloud/securitycenter/v1/iam_binding.proto\x1a.google/cloud/securitycenter/v1/indicator.proto\x1a3google/cloud/securitycenter/v1/kernel_rootkit.proto\x1a/google/cloud/securitycenter/v1/kubernetes.proto\x1a2google/cloud/securitycenter/v1/load_balancer.proto\x1a.google/cloud/securitycenter/v1/log_entry.proto\x1a1google/cloud/securitycenter/v1/mitre_attack.proto\x1a-google/cloud/securitycenter/v1/notebook.proto\x1a/google/cloud/securitycenter/v1/org_policy.proto\x1a,google/cloud/securitycenter/v1/process.proto\x1a3google/cloud/securitycenter/v1/security_marks.proto\x1a5google/cloud/securitycenter/v1/security_posture.proto\x1a6google/cloud/securitycenter/v1/toxic_combination.proto\x1a2google/cloud/securitycenter/v1/vulnerability.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8b!\n\x07Finding\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x15\n\rresource_name\x18\x03 \x01(\t\x12<\n\x05state\x18\x04 \x01(\x0e2-.google.cloud.securitycenter.v1.Finding.State\x12\x10\n\x08category\x18\x05 \x01(\t\x12\x14\n\x0cexternal_uri\x18\x06 \x01(\t\x12X\n\x11source_properties\x18\x07 \x03(\x0b2=.google.cloud.securitycenter.v1.Finding.SourcePropertiesEntry\x12J\n\x0esecurity_marks\x18\x08 \x01(\x0b2-.google.cloud.securitycenter.v1.SecurityMarksB\x03\xe0A\x03\x12.\n\nevent_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12B\n\x08severity\x18\x0c \x01(\x0e20.google.cloud.securitycenter.v1.Finding.Severity\x12\x16\n\x0ecanonical_name\x18\x0e \x01(\t\x12:\n\x04mute\x18\x0f \x01(\x0e2,.google.cloud.securitycenter.v1.Finding.Mute\x12K\n\rfinding_class\x18\x11 \x01(\x0e24.google.cloud.securitycenter.v1.Finding.FindingClass\x12<\n\tindicator\x18\x12 \x01(\x0b2).google.cloud.securitycenter.v1.Indicator\x12D\n\rvulnerability\x18\x14 \x01(\x0b2-.google.cloud.securitycenter.v1.Vulnerability\x129\n\x10mute_update_time\x18\x15 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12[\n\x10external_systems\x18\x16 \x03(\x0b2<.google.cloud.securitycenter.v1.Finding.ExternalSystemsEntryB\x03\xe0A\x03\x12A\n\x0cmitre_attack\x18\x19 \x01(\x0b2+.google.cloud.securitycenter.v1.MitreAttack\x126\n\x06access\x18\x1a \x01(\x0b2&.google.cloud.securitycenter.v1.Access\x12?\n\x0bconnections\x18\x1f \x03(\x0b2*.google.cloud.securitycenter.v1.Connection\x12\x16\n\x0emute_initiator\x18\x1c \x01(\t\x12H\n\tmute_info\x18= \x01(\x0b20.google.cloud.securitycenter.v1.Finding.MuteInfoB\x03\xe0A\x03\x12:\n\tprocesses\x18\x1e \x03(\x0b2\'.google.cloud.securitycenter.v1.Process\x12L\n\x08contacts\x18! \x03(\x0b25.google.cloud.securitycenter.v1.Finding.ContactsEntryB\x03\xe0A\x03\x12?\n\x0bcompliances\x18" \x03(\x0b2*.google.cloud.securitycenter.v1.Compliance\x12 \n\x13parent_display_name\x18$ \x01(\tB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18% \x01(\t\x12B\n\x0cexfiltration\x18& \x01(\x0b2,.google.cloud.securitycenter.v1.Exfiltration\x12@\n\x0ciam_bindings\x18\' \x03(\x0b2*.google.cloud.securitycenter.v1.IamBinding\x12\x12\n\nnext_steps\x18( \x01(\t\x12\x13\n\x0bmodule_name\x18) \x01(\t\x12=\n\ncontainers\x18* \x03(\x0b2).google.cloud.securitycenter.v1.Container\x12>\n\nkubernetes\x18+ \x01(\x0b2*.google.cloud.securitycenter.v1.Kubernetes\x12:\n\x08database\x18, \x01(\x0b2(.google.cloud.securitycenter.v1.Database\x12G\n\x0fattack_exposure\x18- \x01(\x0b2..google.cloud.securitycenter.v1.AttackExposure\x123\n\x05files\x18. \x03(\x0b2$.google.cloud.securitycenter.v1.File\x12P\n\x14cloud_dlp_inspection\x180 \x01(\x0b22.google.cloud.securitycenter.v1.CloudDlpInspection\x12S\n\x16cloud_dlp_data_profile\x181 \x01(\x0b23.google.cloud.securitycenter.v1.CloudDlpDataProfile\x12E\n\x0ekernel_rootkit\x182 \x01(\x0b2-.google.cloud.securitycenter.v1.KernelRootkit\x12?\n\x0corg_policies\x183 \x03(\x0b2).google.cloud.securitycenter.v1.OrgPolicy\x12@\n\x0bapplication\x185 \x01(\x0b2+.google.cloud.securitycenter.v1.Application\x12X\n\x18backup_disaster_recovery\x187 \x01(\x0b26.google.cloud.securitycenter.v1.BackupDisasterRecovery\x12I\n\x10security_posture\x188 \x01(\x0b2/.google.cloud.securitycenter.v1.SecurityPosture\x12=\n\x0blog_entries\x189 \x03(\x0b2(.google.cloud.securitycenter.v1.LogEntry\x12D\n\x0eload_balancers\x18: \x03(\x0b2,.google.cloud.securitycenter.v1.LoadBalancer\x12?\n\x0bcloud_armor\x18; \x01(\x0b2*.google.cloud.securitycenter.v1.CloudArmor\x12:\n\x08notebook\x18? \x01(\x0b2(.google.cloud.securitycenter.v1.Notebook\x12K\n\x11toxic_combination\x18@ \x01(\x0b20.google.cloud.securitycenter.v1.ToxicCombination\x12J\n\x11group_memberships\x18A \x03(\x0b2/.google.cloud.securitycenter.v1.GroupMembership\x1a\x93\x03\n\x08MuteInfo\x12P\n\x0bstatic_mute\x18\x01 \x01(\x0b2;.google.cloud.securitycenter.v1.Finding.MuteInfo.StaticMute\x12`\n\x14dynamic_mute_records\x18\x02 \x03(\x0b2B.google.cloud.securitycenter.v1.Finding.MuteInfo.DynamicMuteRecord\x1ay\n\nStaticMute\x12;\n\x05state\x18\x01 \x01(\x0e2,.google.cloud.securitycenter.v1.Finding.Mute\x12.\n\napply_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1aX\n\x11DynamicMuteRecord\x12\x13\n\x0bmute_config\x18\x01 \x01(\t\x12.\n\nmatch_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1aO\n\x15SourcePropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01\x1af\n\x14ExternalSystemsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b2..google.cloud.securitycenter.v1.ExternalSystem:\x028\x01\x1a_\n\rContactsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b2..google.cloud.securitycenter.v1.ContactDetails:\x028\x01"8\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02"Q\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x07\n\x03LOW\x10\x04"C\n\x04Mute\x12\x14\n\x10MUTE_UNSPECIFIED\x10\x00\x12\t\n\x05MUTED\x10\x01\x12\x0b\n\x07UNMUTED\x10\x02\x12\r\n\tUNDEFINED\x10\x04"\xb0\x01\n\x0cFindingClass\x12\x1d\n\x19FINDING_CLASS_UNSPECIFIED\x10\x00\x12\n\n\x06THREAT\x10\x01\x12\x11\n\rVULNERABILITY\x10\x02\x12\x14\n\x10MISCONFIGURATION\x10\x03\x12\x0f\n\x0bOBSERVATION\x10\x04\x12\r\n\tSCC_ERROR\x10\x05\x12\x15\n\x11POSTURE_VIOLATION\x10\x06\x12\x15\n\x11TOXIC_COMBINATION\x10\x07:\xee\x01\xeaA\xea\x01\n%securitycenter.googleapis.com/Finding\x12@organizations/{organization}/sources/{source}/findings/{finding}\x124folders/{folder}/sources/{source}/findings/{finding}\x126projects/{project}/sources/{source}/findings/{finding}*\x08findings2\x07findingB\xd8\x01\n"com.google.cloud.securitycenter.v1P\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.finding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1P\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_FINDING_SOURCEPROPERTIESENTRY']._loaded_options = None
    _globals['_FINDING_SOURCEPROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_FINDING_EXTERNALSYSTEMSENTRY']._loaded_options = None
    _globals['_FINDING_EXTERNALSYSTEMSENTRY']._serialized_options = b'8\x01'
    _globals['_FINDING_CONTACTSENTRY']._loaded_options = None
    _globals['_FINDING_CONTACTSENTRY']._serialized_options = b'8\x01'
    _globals['_FINDING'].fields_by_name['security_marks']._loaded_options = None
    _globals['_FINDING'].fields_by_name['security_marks']._serialized_options = b'\xe0A\x03'
    _globals['_FINDING'].fields_by_name['mute_update_time']._loaded_options = None
    _globals['_FINDING'].fields_by_name['mute_update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FINDING'].fields_by_name['external_systems']._loaded_options = None
    _globals['_FINDING'].fields_by_name['external_systems']._serialized_options = b'\xe0A\x03'
    _globals['_FINDING'].fields_by_name['mute_info']._loaded_options = None
    _globals['_FINDING'].fields_by_name['mute_info']._serialized_options = b'\xe0A\x03'
    _globals['_FINDING'].fields_by_name['contacts']._loaded_options = None
    _globals['_FINDING'].fields_by_name['contacts']._serialized_options = b'\xe0A\x03'
    _globals['_FINDING'].fields_by_name['parent_display_name']._loaded_options = None
    _globals['_FINDING'].fields_by_name['parent_display_name']._serialized_options = b'\xe0A\x03'
    _globals['_FINDING']._loaded_options = None
    _globals['_FINDING']._serialized_options = b'\xeaA\xea\x01\n%securitycenter.googleapis.com/Finding\x12@organizations/{organization}/sources/{source}/findings/{finding}\x124folders/{folder}/sources/{source}/findings/{finding}\x126projects/{project}/sources/{source}/findings/{finding}*\x08findings2\x07finding'
    _globals['_FINDING']._serialized_start = 1745
    _globals['_FINDING']._serialized_end = 5980
    _globals['_FINDING_MUTEINFO']._serialized_start = 4665
    _globals['_FINDING_MUTEINFO']._serialized_end = 5068
    _globals['_FINDING_MUTEINFO_STATICMUTE']._serialized_start = 4857
    _globals['_FINDING_MUTEINFO_STATICMUTE']._serialized_end = 4978
    _globals['_FINDING_MUTEINFO_DYNAMICMUTERECORD']._serialized_start = 4980
    _globals['_FINDING_MUTEINFO_DYNAMICMUTERECORD']._serialized_end = 5068
    _globals['_FINDING_SOURCEPROPERTIESENTRY']._serialized_start = 5070
    _globals['_FINDING_SOURCEPROPERTIESENTRY']._serialized_end = 5149
    _globals['_FINDING_EXTERNALSYSTEMSENTRY']._serialized_start = 5151
    _globals['_FINDING_EXTERNALSYSTEMSENTRY']._serialized_end = 5253
    _globals['_FINDING_CONTACTSENTRY']._serialized_start = 5255
    _globals['_FINDING_CONTACTSENTRY']._serialized_end = 5350
    _globals['_FINDING_STATE']._serialized_start = 5352
    _globals['_FINDING_STATE']._serialized_end = 5408
    _globals['_FINDING_SEVERITY']._serialized_start = 5410
    _globals['_FINDING_SEVERITY']._serialized_end = 5491
    _globals['_FINDING_MUTE']._serialized_start = 5493
    _globals['_FINDING_MUTE']._serialized_end = 5560
    _globals['_FINDING_FINDINGCLASS']._serialized_start = 5563
    _globals['_FINDING_FINDINGCLASS']._serialized_end = 5739