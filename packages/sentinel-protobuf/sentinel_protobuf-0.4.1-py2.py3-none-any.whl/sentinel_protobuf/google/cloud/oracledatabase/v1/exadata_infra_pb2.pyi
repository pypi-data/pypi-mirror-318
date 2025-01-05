from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.oracledatabase.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import month_pb2 as _month_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CloudExadataInfrastructure(_message.Message):
    __slots__ = ('name', 'display_name', 'gcp_oracle_zone', 'entitlement_id', 'properties', 'labels', 'create_time')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GCP_ORACLE_ZONE_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    gcp_oracle_zone: str
    entitlement_id: str
    properties: CloudExadataInfrastructureProperties
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., gcp_oracle_zone: _Optional[str]=..., entitlement_id: _Optional[str]=..., properties: _Optional[_Union[CloudExadataInfrastructureProperties, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CloudExadataInfrastructureProperties(_message.Message):
    __slots__ = ('ocid', 'compute_count', 'storage_count', 'total_storage_size_gb', 'available_storage_size_gb', 'maintenance_window', 'state', 'shape', 'oci_url', 'cpu_count', 'max_cpu_count', 'memory_size_gb', 'max_memory_gb', 'db_node_storage_size_gb', 'max_db_node_storage_size_gb', 'data_storage_size_tb', 'max_data_storage_tb', 'activated_storage_count', 'additional_storage_count', 'db_server_version', 'storage_server_version', 'next_maintenance_run_id', 'next_maintenance_run_time', 'next_security_maintenance_run_time', 'customer_contacts', 'monthly_storage_server_version', 'monthly_db_server_version')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CloudExadataInfrastructureProperties.State]
        PROVISIONING: _ClassVar[CloudExadataInfrastructureProperties.State]
        AVAILABLE: _ClassVar[CloudExadataInfrastructureProperties.State]
        UPDATING: _ClassVar[CloudExadataInfrastructureProperties.State]
        TERMINATING: _ClassVar[CloudExadataInfrastructureProperties.State]
        TERMINATED: _ClassVar[CloudExadataInfrastructureProperties.State]
        FAILED: _ClassVar[CloudExadataInfrastructureProperties.State]
        MAINTENANCE_IN_PROGRESS: _ClassVar[CloudExadataInfrastructureProperties.State]
    STATE_UNSPECIFIED: CloudExadataInfrastructureProperties.State
    PROVISIONING: CloudExadataInfrastructureProperties.State
    AVAILABLE: CloudExadataInfrastructureProperties.State
    UPDATING: CloudExadataInfrastructureProperties.State
    TERMINATING: CloudExadataInfrastructureProperties.State
    TERMINATED: CloudExadataInfrastructureProperties.State
    FAILED: CloudExadataInfrastructureProperties.State
    MAINTENANCE_IN_PROGRESS: CloudExadataInfrastructureProperties.State
    OCID_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    OCI_URL_FIELD_NUMBER: _ClassVar[int]
    CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
    DB_NODE_STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    MAX_DB_NODE_STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DATA_STORAGE_SIZE_TB_FIELD_NUMBER: _ClassVar[int]
    MAX_DATA_STORAGE_TB_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_STORAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_STORAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DB_SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    NEXT_MAINTENANCE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_MAINTENANCE_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_SECURITY_MAINTENANCE_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CONTACTS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_STORAGE_SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_DB_SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    ocid: str
    compute_count: int
    storage_count: int
    total_storage_size_gb: int
    available_storage_size_gb: int
    maintenance_window: MaintenanceWindow
    state: CloudExadataInfrastructureProperties.State
    shape: str
    oci_url: str
    cpu_count: int
    max_cpu_count: int
    memory_size_gb: int
    max_memory_gb: int
    db_node_storage_size_gb: int
    max_db_node_storage_size_gb: int
    data_storage_size_tb: float
    max_data_storage_tb: float
    activated_storage_count: int
    additional_storage_count: int
    db_server_version: str
    storage_server_version: str
    next_maintenance_run_id: str
    next_maintenance_run_time: _timestamp_pb2.Timestamp
    next_security_maintenance_run_time: _timestamp_pb2.Timestamp
    customer_contacts: _containers.RepeatedCompositeFieldContainer[_common_pb2.CustomerContact]
    monthly_storage_server_version: str
    monthly_db_server_version: str

    def __init__(self, ocid: _Optional[str]=..., compute_count: _Optional[int]=..., storage_count: _Optional[int]=..., total_storage_size_gb: _Optional[int]=..., available_storage_size_gb: _Optional[int]=..., maintenance_window: _Optional[_Union[MaintenanceWindow, _Mapping]]=..., state: _Optional[_Union[CloudExadataInfrastructureProperties.State, str]]=..., shape: _Optional[str]=..., oci_url: _Optional[str]=..., cpu_count: _Optional[int]=..., max_cpu_count: _Optional[int]=..., memory_size_gb: _Optional[int]=..., max_memory_gb: _Optional[int]=..., db_node_storage_size_gb: _Optional[int]=..., max_db_node_storage_size_gb: _Optional[int]=..., data_storage_size_tb: _Optional[float]=..., max_data_storage_tb: _Optional[float]=..., activated_storage_count: _Optional[int]=..., additional_storage_count: _Optional[int]=..., db_server_version: _Optional[str]=..., storage_server_version: _Optional[str]=..., next_maintenance_run_id: _Optional[str]=..., next_maintenance_run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_security_maintenance_run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., customer_contacts: _Optional[_Iterable[_Union[_common_pb2.CustomerContact, _Mapping]]]=..., monthly_storage_server_version: _Optional[str]=..., monthly_db_server_version: _Optional[str]=...) -> None:
        ...

class MaintenanceWindow(_message.Message):
    __slots__ = ('preference', 'months', 'weeks_of_month', 'days_of_week', 'hours_of_day', 'lead_time_week', 'patching_mode', 'custom_action_timeout_mins', 'is_custom_action_timeout_enabled')

    class MaintenanceWindowPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MAINTENANCE_WINDOW_PREFERENCE_UNSPECIFIED: _ClassVar[MaintenanceWindow.MaintenanceWindowPreference]
        CUSTOM_PREFERENCE: _ClassVar[MaintenanceWindow.MaintenanceWindowPreference]
        NO_PREFERENCE: _ClassVar[MaintenanceWindow.MaintenanceWindowPreference]
    MAINTENANCE_WINDOW_PREFERENCE_UNSPECIFIED: MaintenanceWindow.MaintenanceWindowPreference
    CUSTOM_PREFERENCE: MaintenanceWindow.MaintenanceWindowPreference
    NO_PREFERENCE: MaintenanceWindow.MaintenanceWindowPreference

    class PatchingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PATCHING_MODE_UNSPECIFIED: _ClassVar[MaintenanceWindow.PatchingMode]
        ROLLING: _ClassVar[MaintenanceWindow.PatchingMode]
        NON_ROLLING: _ClassVar[MaintenanceWindow.PatchingMode]
    PATCHING_MODE_UNSPECIFIED: MaintenanceWindow.PatchingMode
    ROLLING: MaintenanceWindow.PatchingMode
    NON_ROLLING: MaintenanceWindow.PatchingMode
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    MONTHS_FIELD_NUMBER: _ClassVar[int]
    WEEKS_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    DAYS_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    HOURS_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    LEAD_TIME_WEEK_FIELD_NUMBER: _ClassVar[int]
    PATCHING_MODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ACTION_TIMEOUT_MINS_FIELD_NUMBER: _ClassVar[int]
    IS_CUSTOM_ACTION_TIMEOUT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    preference: MaintenanceWindow.MaintenanceWindowPreference
    months: _containers.RepeatedScalarFieldContainer[_month_pb2.Month]
    weeks_of_month: _containers.RepeatedScalarFieldContainer[int]
    days_of_week: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]
    hours_of_day: _containers.RepeatedScalarFieldContainer[int]
    lead_time_week: int
    patching_mode: MaintenanceWindow.PatchingMode
    custom_action_timeout_mins: int
    is_custom_action_timeout_enabled: bool

    def __init__(self, preference: _Optional[_Union[MaintenanceWindow.MaintenanceWindowPreference, str]]=..., months: _Optional[_Iterable[_Union[_month_pb2.Month, str]]]=..., weeks_of_month: _Optional[_Iterable[int]]=..., days_of_week: _Optional[_Iterable[_Union[_dayofweek_pb2.DayOfWeek, str]]]=..., hours_of_day: _Optional[_Iterable[int]]=..., lead_time_week: _Optional[int]=..., patching_mode: _Optional[_Union[MaintenanceWindow.PatchingMode, str]]=..., custom_action_timeout_mins: _Optional[int]=..., is_custom_action_timeout_enabled: bool=...) -> None:
        ...