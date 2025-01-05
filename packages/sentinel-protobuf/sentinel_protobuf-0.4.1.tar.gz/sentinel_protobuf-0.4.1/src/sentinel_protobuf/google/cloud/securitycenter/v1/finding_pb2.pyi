from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.v1 import access_pb2 as _access_pb2
from google.cloud.securitycenter.v1 import application_pb2 as _application_pb2
from google.cloud.securitycenter.v1 import attack_exposure_pb2 as _attack_exposure_pb2
from google.cloud.securitycenter.v1 import backup_disaster_recovery_pb2 as _backup_disaster_recovery_pb2
from google.cloud.securitycenter.v1 import cloud_armor_pb2 as _cloud_armor_pb2
from google.cloud.securitycenter.v1 import cloud_dlp_data_profile_pb2 as _cloud_dlp_data_profile_pb2
from google.cloud.securitycenter.v1 import cloud_dlp_inspection_pb2 as _cloud_dlp_inspection_pb2
from google.cloud.securitycenter.v1 import compliance_pb2 as _compliance_pb2
from google.cloud.securitycenter.v1 import connection_pb2 as _connection_pb2
from google.cloud.securitycenter.v1 import contact_details_pb2 as _contact_details_pb2
from google.cloud.securitycenter.v1 import container_pb2 as _container_pb2
from google.cloud.securitycenter.v1 import database_pb2 as _database_pb2
from google.cloud.securitycenter.v1 import exfiltration_pb2 as _exfiltration_pb2
from google.cloud.securitycenter.v1 import external_system_pb2 as _external_system_pb2
from google.cloud.securitycenter.v1 import file_pb2 as _file_pb2
from google.cloud.securitycenter.v1 import group_membership_pb2 as _group_membership_pb2
from google.cloud.securitycenter.v1 import iam_binding_pb2 as _iam_binding_pb2
from google.cloud.securitycenter.v1 import indicator_pb2 as _indicator_pb2
from google.cloud.securitycenter.v1 import kernel_rootkit_pb2 as _kernel_rootkit_pb2
from google.cloud.securitycenter.v1 import kubernetes_pb2 as _kubernetes_pb2
from google.cloud.securitycenter.v1 import load_balancer_pb2 as _load_balancer_pb2
from google.cloud.securitycenter.v1 import log_entry_pb2 as _log_entry_pb2
from google.cloud.securitycenter.v1 import mitre_attack_pb2 as _mitre_attack_pb2
from google.cloud.securitycenter.v1 import notebook_pb2 as _notebook_pb2
from google.cloud.securitycenter.v1 import org_policy_pb2 as _org_policy_pb2
from google.cloud.securitycenter.v1 import process_pb2 as _process_pb2
from google.cloud.securitycenter.v1 import security_marks_pb2 as _security_marks_pb2
from google.cloud.securitycenter.v1 import security_posture_pb2 as _security_posture_pb2
from google.cloud.securitycenter.v1 import toxic_combination_pb2 as _toxic_combination_pb2
from google.cloud.securitycenter.v1 import vulnerability_pb2 as _vulnerability_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Finding(_message.Message):
    __slots__ = ('name', 'parent', 'resource_name', 'state', 'category', 'external_uri', 'source_properties', 'security_marks', 'event_time', 'create_time', 'severity', 'canonical_name', 'mute', 'finding_class', 'indicator', 'vulnerability', 'mute_update_time', 'external_systems', 'mitre_attack', 'access', 'connections', 'mute_initiator', 'mute_info', 'processes', 'contacts', 'compliances', 'parent_display_name', 'description', 'exfiltration', 'iam_bindings', 'next_steps', 'module_name', 'containers', 'kubernetes', 'database', 'attack_exposure', 'files', 'cloud_dlp_inspection', 'cloud_dlp_data_profile', 'kernel_rootkit', 'org_policies', 'application', 'backup_disaster_recovery', 'security_posture', 'log_entries', 'load_balancers', 'cloud_armor', 'notebook', 'toxic_combination', 'group_memberships')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Finding.State]
        ACTIVE: _ClassVar[Finding.State]
        INACTIVE: _ClassVar[Finding.State]
    STATE_UNSPECIFIED: Finding.State
    ACTIVE: Finding.State
    INACTIVE: Finding.State

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[Finding.Severity]
        CRITICAL: _ClassVar[Finding.Severity]
        HIGH: _ClassVar[Finding.Severity]
        MEDIUM: _ClassVar[Finding.Severity]
        LOW: _ClassVar[Finding.Severity]
    SEVERITY_UNSPECIFIED: Finding.Severity
    CRITICAL: Finding.Severity
    HIGH: Finding.Severity
    MEDIUM: Finding.Severity
    LOW: Finding.Severity

    class Mute(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUTE_UNSPECIFIED: _ClassVar[Finding.Mute]
        MUTED: _ClassVar[Finding.Mute]
        UNMUTED: _ClassVar[Finding.Mute]
        UNDEFINED: _ClassVar[Finding.Mute]
    MUTE_UNSPECIFIED: Finding.Mute
    MUTED: Finding.Mute
    UNMUTED: Finding.Mute
    UNDEFINED: Finding.Mute

    class FindingClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FINDING_CLASS_UNSPECIFIED: _ClassVar[Finding.FindingClass]
        THREAT: _ClassVar[Finding.FindingClass]
        VULNERABILITY: _ClassVar[Finding.FindingClass]
        MISCONFIGURATION: _ClassVar[Finding.FindingClass]
        OBSERVATION: _ClassVar[Finding.FindingClass]
        SCC_ERROR: _ClassVar[Finding.FindingClass]
        POSTURE_VIOLATION: _ClassVar[Finding.FindingClass]
        TOXIC_COMBINATION: _ClassVar[Finding.FindingClass]
    FINDING_CLASS_UNSPECIFIED: Finding.FindingClass
    THREAT: Finding.FindingClass
    VULNERABILITY: Finding.FindingClass
    MISCONFIGURATION: Finding.FindingClass
    OBSERVATION: Finding.FindingClass
    SCC_ERROR: Finding.FindingClass
    POSTURE_VIOLATION: Finding.FindingClass
    TOXIC_COMBINATION: Finding.FindingClass

    class MuteInfo(_message.Message):
        __slots__ = ('static_mute', 'dynamic_mute_records')

        class StaticMute(_message.Message):
            __slots__ = ('state', 'apply_time')
            STATE_FIELD_NUMBER: _ClassVar[int]
            APPLY_TIME_FIELD_NUMBER: _ClassVar[int]
            state: Finding.Mute
            apply_time: _timestamp_pb2.Timestamp

            def __init__(self, state: _Optional[_Union[Finding.Mute, str]]=..., apply_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
                ...

        class DynamicMuteRecord(_message.Message):
            __slots__ = ('mute_config', 'match_time')
            MUTE_CONFIG_FIELD_NUMBER: _ClassVar[int]
            MATCH_TIME_FIELD_NUMBER: _ClassVar[int]
            mute_config: str
            match_time: _timestamp_pb2.Timestamp

            def __init__(self, mute_config: _Optional[str]=..., match_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
                ...
        STATIC_MUTE_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_MUTE_RECORDS_FIELD_NUMBER: _ClassVar[int]
        static_mute: Finding.MuteInfo.StaticMute
        dynamic_mute_records: _containers.RepeatedCompositeFieldContainer[Finding.MuteInfo.DynamicMuteRecord]

        def __init__(self, static_mute: _Optional[_Union[Finding.MuteInfo.StaticMute, _Mapping]]=..., dynamic_mute_records: _Optional[_Iterable[_Union[Finding.MuteInfo.DynamicMuteRecord, _Mapping]]]=...) -> None:
            ...

    class SourcePropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...

    class ExternalSystemsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _external_system_pb2.ExternalSystem

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_external_system_pb2.ExternalSystem, _Mapping]]=...) -> None:
            ...

    class ContactsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _contact_details_pb2.ContactDetails

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_contact_details_pb2.ContactDetails, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MARKS_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_NAME_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIELD_NUMBER: _ClassVar[int]
    FINDING_CLASS_FIELD_NUMBER: _ClassVar[int]
    INDICATOR_FIELD_NUMBER: _ClassVar[int]
    VULNERABILITY_FIELD_NUMBER: _ClassVar[int]
    MUTE_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    MITRE_ATTACK_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    MUTE_INITIATOR_FIELD_NUMBER: _ClassVar[int]
    MUTE_INFO_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCES_FIELD_NUMBER: _ClassVar[int]
    PARENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXFILTRATION_FIELD_NUMBER: _ClassVar[int]
    IAM_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_STEPS_FIELD_NUMBER: _ClassVar[int]
    MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    ATTACK_EXPOSURE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DLP_INSPECTION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DLP_DATA_PROFILE_FIELD_NUMBER: _ClassVar[int]
    KERNEL_ROOTKIT_FIELD_NUMBER: _ClassVar[int]
    ORG_POLICIES_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISASTER_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_POSTURE_FIELD_NUMBER: _ClassVar[int]
    LOG_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCERS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARMOR_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_FIELD_NUMBER: _ClassVar[int]
    TOXIC_COMBINATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    resource_name: str
    state: Finding.State
    category: str
    external_uri: str
    source_properties: _containers.MessageMap[str, _struct_pb2.Value]
    security_marks: _security_marks_pb2.SecurityMarks
    event_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    severity: Finding.Severity
    canonical_name: str
    mute: Finding.Mute
    finding_class: Finding.FindingClass
    indicator: _indicator_pb2.Indicator
    vulnerability: _vulnerability_pb2.Vulnerability
    mute_update_time: _timestamp_pb2.Timestamp
    external_systems: _containers.MessageMap[str, _external_system_pb2.ExternalSystem]
    mitre_attack: _mitre_attack_pb2.MitreAttack
    access: _access_pb2.Access
    connections: _containers.RepeatedCompositeFieldContainer[_connection_pb2.Connection]
    mute_initiator: str
    mute_info: Finding.MuteInfo
    processes: _containers.RepeatedCompositeFieldContainer[_process_pb2.Process]
    contacts: _containers.MessageMap[str, _contact_details_pb2.ContactDetails]
    compliances: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.Compliance]
    parent_display_name: str
    description: str
    exfiltration: _exfiltration_pb2.Exfiltration
    iam_bindings: _containers.RepeatedCompositeFieldContainer[_iam_binding_pb2.IamBinding]
    next_steps: str
    module_name: str
    containers: _containers.RepeatedCompositeFieldContainer[_container_pb2.Container]
    kubernetes: _kubernetes_pb2.Kubernetes
    database: _database_pb2.Database
    attack_exposure: _attack_exposure_pb2.AttackExposure
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    cloud_dlp_inspection: _cloud_dlp_inspection_pb2.CloudDlpInspection
    cloud_dlp_data_profile: _cloud_dlp_data_profile_pb2.CloudDlpDataProfile
    kernel_rootkit: _kernel_rootkit_pb2.KernelRootkit
    org_policies: _containers.RepeatedCompositeFieldContainer[_org_policy_pb2.OrgPolicy]
    application: _application_pb2.Application
    backup_disaster_recovery: _backup_disaster_recovery_pb2.BackupDisasterRecovery
    security_posture: _security_posture_pb2.SecurityPosture
    log_entries: _containers.RepeatedCompositeFieldContainer[_log_entry_pb2.LogEntry]
    load_balancers: _containers.RepeatedCompositeFieldContainer[_load_balancer_pb2.LoadBalancer]
    cloud_armor: _cloud_armor_pb2.CloudArmor
    notebook: _notebook_pb2.Notebook
    toxic_combination: _toxic_combination_pb2.ToxicCombination
    group_memberships: _containers.RepeatedCompositeFieldContainer[_group_membership_pb2.GroupMembership]

    def __init__(self, name: _Optional[str]=..., parent: _Optional[str]=..., resource_name: _Optional[str]=..., state: _Optional[_Union[Finding.State, str]]=..., category: _Optional[str]=..., external_uri: _Optional[str]=..., source_properties: _Optional[_Mapping[str, _struct_pb2.Value]]=..., security_marks: _Optional[_Union[_security_marks_pb2.SecurityMarks, _Mapping]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., severity: _Optional[_Union[Finding.Severity, str]]=..., canonical_name: _Optional[str]=..., mute: _Optional[_Union[Finding.Mute, str]]=..., finding_class: _Optional[_Union[Finding.FindingClass, str]]=..., indicator: _Optional[_Union[_indicator_pb2.Indicator, _Mapping]]=..., vulnerability: _Optional[_Union[_vulnerability_pb2.Vulnerability, _Mapping]]=..., mute_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., external_systems: _Optional[_Mapping[str, _external_system_pb2.ExternalSystem]]=..., mitre_attack: _Optional[_Union[_mitre_attack_pb2.MitreAttack, _Mapping]]=..., access: _Optional[_Union[_access_pb2.Access, _Mapping]]=..., connections: _Optional[_Iterable[_Union[_connection_pb2.Connection, _Mapping]]]=..., mute_initiator: _Optional[str]=..., mute_info: _Optional[_Union[Finding.MuteInfo, _Mapping]]=..., processes: _Optional[_Iterable[_Union[_process_pb2.Process, _Mapping]]]=..., contacts: _Optional[_Mapping[str, _contact_details_pb2.ContactDetails]]=..., compliances: _Optional[_Iterable[_Union[_compliance_pb2.Compliance, _Mapping]]]=..., parent_display_name: _Optional[str]=..., description: _Optional[str]=..., exfiltration: _Optional[_Union[_exfiltration_pb2.Exfiltration, _Mapping]]=..., iam_bindings: _Optional[_Iterable[_Union[_iam_binding_pb2.IamBinding, _Mapping]]]=..., next_steps: _Optional[str]=..., module_name: _Optional[str]=..., containers: _Optional[_Iterable[_Union[_container_pb2.Container, _Mapping]]]=..., kubernetes: _Optional[_Union[_kubernetes_pb2.Kubernetes, _Mapping]]=..., database: _Optional[_Union[_database_pb2.Database, _Mapping]]=..., attack_exposure: _Optional[_Union[_attack_exposure_pb2.AttackExposure, _Mapping]]=..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=..., cloud_dlp_inspection: _Optional[_Union[_cloud_dlp_inspection_pb2.CloudDlpInspection, _Mapping]]=..., cloud_dlp_data_profile: _Optional[_Union[_cloud_dlp_data_profile_pb2.CloudDlpDataProfile, _Mapping]]=..., kernel_rootkit: _Optional[_Union[_kernel_rootkit_pb2.KernelRootkit, _Mapping]]=..., org_policies: _Optional[_Iterable[_Union[_org_policy_pb2.OrgPolicy, _Mapping]]]=..., application: _Optional[_Union[_application_pb2.Application, _Mapping]]=..., backup_disaster_recovery: _Optional[_Union[_backup_disaster_recovery_pb2.BackupDisasterRecovery, _Mapping]]=..., security_posture: _Optional[_Union[_security_posture_pb2.SecurityPosture, _Mapping]]=..., log_entries: _Optional[_Iterable[_Union[_log_entry_pb2.LogEntry, _Mapping]]]=..., load_balancers: _Optional[_Iterable[_Union[_load_balancer_pb2.LoadBalancer, _Mapping]]]=..., cloud_armor: _Optional[_Union[_cloud_armor_pb2.CloudArmor, _Mapping]]=..., notebook: _Optional[_Union[_notebook_pb2.Notebook, _Mapping]]=..., toxic_combination: _Optional[_Union[_toxic_combination_pb2.ToxicCombination, _Mapping]]=..., group_memberships: _Optional[_Iterable[_Union[_group_membership_pb2.GroupMembership, _Mapping]]]=...) -> None:
        ...