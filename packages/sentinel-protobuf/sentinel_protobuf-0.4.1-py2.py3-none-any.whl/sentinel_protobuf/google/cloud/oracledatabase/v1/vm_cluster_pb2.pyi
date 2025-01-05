from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CloudVmCluster(_message.Message):
    __slots__ = ('name', 'exadata_infrastructure', 'display_name', 'gcp_oracle_zone', 'properties', 'labels', 'create_time', 'cidr', 'backup_subnet_cidr', 'network')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXADATA_INFRASTRUCTURE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GCP_ORACLE_ZONE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SUBNET_CIDR_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    name: str
    exadata_infrastructure: str
    display_name: str
    gcp_oracle_zone: str
    properties: CloudVmClusterProperties
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    cidr: str
    backup_subnet_cidr: str
    network: str

    def __init__(self, name: _Optional[str]=..., exadata_infrastructure: _Optional[str]=..., display_name: _Optional[str]=..., gcp_oracle_zone: _Optional[str]=..., properties: _Optional[_Union[CloudVmClusterProperties, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cidr: _Optional[str]=..., backup_subnet_cidr: _Optional[str]=..., network: _Optional[str]=...) -> None:
        ...

class CloudVmClusterProperties(_message.Message):
    __slots__ = ('ocid', 'license_type', 'gi_version', 'time_zone', 'ssh_public_keys', 'node_count', 'shape', 'ocpu_count', 'memory_size_gb', 'db_node_storage_size_gb', 'storage_size_gb', 'data_storage_size_tb', 'disk_redundancy', 'sparse_diskgroup_enabled', 'local_backup_enabled', 'hostname_prefix', 'diagnostics_data_collection_options', 'state', 'scan_listener_port_tcp', 'scan_listener_port_tcp_ssl', 'domain', 'scan_dns', 'hostname', 'cpu_core_count', 'system_version', 'scan_ip_ids', 'scan_dns_record_id', 'oci_url', 'db_server_ocids', 'compartment_id', 'dns_listener_ip', 'cluster_name')

    class LicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LICENSE_TYPE_UNSPECIFIED: _ClassVar[CloudVmClusterProperties.LicenseType]
        LICENSE_INCLUDED: _ClassVar[CloudVmClusterProperties.LicenseType]
        BRING_YOUR_OWN_LICENSE: _ClassVar[CloudVmClusterProperties.LicenseType]
    LICENSE_TYPE_UNSPECIFIED: CloudVmClusterProperties.LicenseType
    LICENSE_INCLUDED: CloudVmClusterProperties.LicenseType
    BRING_YOUR_OWN_LICENSE: CloudVmClusterProperties.LicenseType

    class DiskRedundancy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISK_REDUNDANCY_UNSPECIFIED: _ClassVar[CloudVmClusterProperties.DiskRedundancy]
        HIGH: _ClassVar[CloudVmClusterProperties.DiskRedundancy]
        NORMAL: _ClassVar[CloudVmClusterProperties.DiskRedundancy]
    DISK_REDUNDANCY_UNSPECIFIED: CloudVmClusterProperties.DiskRedundancy
    HIGH: CloudVmClusterProperties.DiskRedundancy
    NORMAL: CloudVmClusterProperties.DiskRedundancy

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CloudVmClusterProperties.State]
        PROVISIONING: _ClassVar[CloudVmClusterProperties.State]
        AVAILABLE: _ClassVar[CloudVmClusterProperties.State]
        UPDATING: _ClassVar[CloudVmClusterProperties.State]
        TERMINATING: _ClassVar[CloudVmClusterProperties.State]
        TERMINATED: _ClassVar[CloudVmClusterProperties.State]
        FAILED: _ClassVar[CloudVmClusterProperties.State]
        MAINTENANCE_IN_PROGRESS: _ClassVar[CloudVmClusterProperties.State]
    STATE_UNSPECIFIED: CloudVmClusterProperties.State
    PROVISIONING: CloudVmClusterProperties.State
    AVAILABLE: CloudVmClusterProperties.State
    UPDATING: CloudVmClusterProperties.State
    TERMINATING: CloudVmClusterProperties.State
    TERMINATED: CloudVmClusterProperties.State
    FAILED: CloudVmClusterProperties.State
    MAINTENANCE_IN_PROGRESS: CloudVmClusterProperties.State
    OCID_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GI_VERSION_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    SSH_PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    OCPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DB_NODE_STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DATA_STORAGE_SIZE_TB_FIELD_NUMBER: _ClassVar[int]
    DISK_REDUNDANCY_FIELD_NUMBER: _ClassVar[int]
    SPARSE_DISKGROUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCAL_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_DATA_COLLECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCAN_LISTENER_PORT_TCP_FIELD_NUMBER: _ClassVar[int]
    SCAN_LISTENER_PORT_TCP_SSL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SCAN_DNS_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    CPU_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCAN_IP_IDS_FIELD_NUMBER: _ClassVar[int]
    SCAN_DNS_RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    OCI_URL_FIELD_NUMBER: _ClassVar[int]
    DB_SERVER_OCIDS_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DNS_LISTENER_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    ocid: str
    license_type: CloudVmClusterProperties.LicenseType
    gi_version: str
    time_zone: _datetime_pb2.TimeZone
    ssh_public_keys: _containers.RepeatedScalarFieldContainer[str]
    node_count: int
    shape: str
    ocpu_count: float
    memory_size_gb: int
    db_node_storage_size_gb: int
    storage_size_gb: int
    data_storage_size_tb: float
    disk_redundancy: CloudVmClusterProperties.DiskRedundancy
    sparse_diskgroup_enabled: bool
    local_backup_enabled: bool
    hostname_prefix: str
    diagnostics_data_collection_options: DataCollectionOptions
    state: CloudVmClusterProperties.State
    scan_listener_port_tcp: int
    scan_listener_port_tcp_ssl: int
    domain: str
    scan_dns: str
    hostname: str
    cpu_core_count: int
    system_version: str
    scan_ip_ids: _containers.RepeatedScalarFieldContainer[str]
    scan_dns_record_id: str
    oci_url: str
    db_server_ocids: _containers.RepeatedScalarFieldContainer[str]
    compartment_id: str
    dns_listener_ip: str
    cluster_name: str

    def __init__(self, ocid: _Optional[str]=..., license_type: _Optional[_Union[CloudVmClusterProperties.LicenseType, str]]=..., gi_version: _Optional[str]=..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]]=..., ssh_public_keys: _Optional[_Iterable[str]]=..., node_count: _Optional[int]=..., shape: _Optional[str]=..., ocpu_count: _Optional[float]=..., memory_size_gb: _Optional[int]=..., db_node_storage_size_gb: _Optional[int]=..., storage_size_gb: _Optional[int]=..., data_storage_size_tb: _Optional[float]=..., disk_redundancy: _Optional[_Union[CloudVmClusterProperties.DiskRedundancy, str]]=..., sparse_diskgroup_enabled: bool=..., local_backup_enabled: bool=..., hostname_prefix: _Optional[str]=..., diagnostics_data_collection_options: _Optional[_Union[DataCollectionOptions, _Mapping]]=..., state: _Optional[_Union[CloudVmClusterProperties.State, str]]=..., scan_listener_port_tcp: _Optional[int]=..., scan_listener_port_tcp_ssl: _Optional[int]=..., domain: _Optional[str]=..., scan_dns: _Optional[str]=..., hostname: _Optional[str]=..., cpu_core_count: _Optional[int]=..., system_version: _Optional[str]=..., scan_ip_ids: _Optional[_Iterable[str]]=..., scan_dns_record_id: _Optional[str]=..., oci_url: _Optional[str]=..., db_server_ocids: _Optional[_Iterable[str]]=..., compartment_id: _Optional[str]=..., dns_listener_ip: _Optional[str]=..., cluster_name: _Optional[str]=...) -> None:
        ...

class DataCollectionOptions(_message.Message):
    __slots__ = ('diagnostics_events_enabled', 'health_monitoring_enabled', 'incident_logs_enabled')
    DIAGNOSTICS_EVENTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HEALTH_MONITORING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INCIDENT_LOGS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    diagnostics_events_enabled: bool
    health_monitoring_enabled: bool
    incident_logs_enabled: bool

    def __init__(self, diagnostics_events_enabled: bool=..., health_monitoring_enabled: bool=..., incident_logs_enabled: bool=...) -> None:
        ...