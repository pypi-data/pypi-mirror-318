from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Service(_message.Message):
    __slots__ = ('hive_metastore_config', 'name', 'create_time', 'update_time', 'labels', 'network', 'endpoint_uri', 'port', 'state', 'state_message', 'artifact_gcs_uri', 'tier', 'maintenance_window', 'uid', 'metadata_management_activity', 'release_channel', 'encryption_config', 'network_config', 'database_type', 'telemetry_config', 'scaling_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Service.State]
        CREATING: _ClassVar[Service.State]
        ACTIVE: _ClassVar[Service.State]
        SUSPENDING: _ClassVar[Service.State]
        SUSPENDED: _ClassVar[Service.State]
        UPDATING: _ClassVar[Service.State]
        DELETING: _ClassVar[Service.State]
        ERROR: _ClassVar[Service.State]
    STATE_UNSPECIFIED: Service.State
    CREATING: Service.State
    ACTIVE: Service.State
    SUSPENDING: Service.State
    SUSPENDED: Service.State
    UPDATING: Service.State
    DELETING: Service.State
    ERROR: Service.State

    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_UNSPECIFIED: _ClassVar[Service.Tier]
        DEVELOPER: _ClassVar[Service.Tier]
        ENTERPRISE: _ClassVar[Service.Tier]
    TIER_UNSPECIFIED: Service.Tier
    DEVELOPER: Service.Tier
    ENTERPRISE: Service.Tier

    class ReleaseChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELEASE_CHANNEL_UNSPECIFIED: _ClassVar[Service.ReleaseChannel]
        CANARY: _ClassVar[Service.ReleaseChannel]
        STABLE: _ClassVar[Service.ReleaseChannel]
    RELEASE_CHANNEL_UNSPECIFIED: Service.ReleaseChannel
    CANARY: Service.ReleaseChannel
    STABLE: Service.ReleaseChannel

    class DatabaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATABASE_TYPE_UNSPECIFIED: _ClassVar[Service.DatabaseType]
        MYSQL: _ClassVar[Service.DatabaseType]
        SPANNER: _ClassVar[Service.DatabaseType]
    DATABASE_TYPE_UNSPECIFIED: Service.DatabaseType
    MYSQL: Service.DatabaseType
    SPANNER: Service.DatabaseType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    HIVE_METASTORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_URI_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_GCS_URI_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    METADATA_MANAGEMENT_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATABASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SCALING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    hive_metastore_config: HiveMetastoreConfig
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    network: str
    endpoint_uri: str
    port: int
    state: Service.State
    state_message: str
    artifact_gcs_uri: str
    tier: Service.Tier
    maintenance_window: MaintenanceWindow
    uid: str
    metadata_management_activity: MetadataManagementActivity
    release_channel: Service.ReleaseChannel
    encryption_config: EncryptionConfig
    network_config: NetworkConfig
    database_type: Service.DatabaseType
    telemetry_config: TelemetryConfig
    scaling_config: ScalingConfig

    def __init__(self, hive_metastore_config: _Optional[_Union[HiveMetastoreConfig, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., network: _Optional[str]=..., endpoint_uri: _Optional[str]=..., port: _Optional[int]=..., state: _Optional[_Union[Service.State, str]]=..., state_message: _Optional[str]=..., artifact_gcs_uri: _Optional[str]=..., tier: _Optional[_Union[Service.Tier, str]]=..., maintenance_window: _Optional[_Union[MaintenanceWindow, _Mapping]]=..., uid: _Optional[str]=..., metadata_management_activity: _Optional[_Union[MetadataManagementActivity, _Mapping]]=..., release_channel: _Optional[_Union[Service.ReleaseChannel, str]]=..., encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]]=..., network_config: _Optional[_Union[NetworkConfig, _Mapping]]=..., database_type: _Optional[_Union[Service.DatabaseType, str]]=..., telemetry_config: _Optional[_Union[TelemetryConfig, _Mapping]]=..., scaling_config: _Optional[_Union[ScalingConfig, _Mapping]]=...) -> None:
        ...

class MaintenanceWindow(_message.Message):
    __slots__ = ('hour_of_day', 'day_of_week')
    HOUR_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    hour_of_day: _wrappers_pb2.Int32Value
    day_of_week: _dayofweek_pb2.DayOfWeek

    def __init__(self, hour_of_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., day_of_week: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]]=...) -> None:
        ...

class HiveMetastoreConfig(_message.Message):
    __slots__ = ('version', 'config_overrides', 'kerberos_config', 'endpoint_protocol', 'auxiliary_versions')

    class EndpointProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENDPOINT_PROTOCOL_UNSPECIFIED: _ClassVar[HiveMetastoreConfig.EndpointProtocol]
        THRIFT: _ClassVar[HiveMetastoreConfig.EndpointProtocol]
        GRPC: _ClassVar[HiveMetastoreConfig.EndpointProtocol]
    ENDPOINT_PROTOCOL_UNSPECIFIED: HiveMetastoreConfig.EndpointProtocol
    THRIFT: HiveMetastoreConfig.EndpointProtocol
    GRPC: HiveMetastoreConfig.EndpointProtocol

    class ConfigOverridesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AuxiliaryVersionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AuxiliaryVersionConfig

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AuxiliaryVersionConfig, _Mapping]]=...) -> None:
            ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    version: str
    config_overrides: _containers.ScalarMap[str, str]
    kerberos_config: KerberosConfig
    endpoint_protocol: HiveMetastoreConfig.EndpointProtocol
    auxiliary_versions: _containers.MessageMap[str, AuxiliaryVersionConfig]

    def __init__(self, version: _Optional[str]=..., config_overrides: _Optional[_Mapping[str, str]]=..., kerberos_config: _Optional[_Union[KerberosConfig, _Mapping]]=..., endpoint_protocol: _Optional[_Union[HiveMetastoreConfig.EndpointProtocol, str]]=..., auxiliary_versions: _Optional[_Mapping[str, AuxiliaryVersionConfig]]=...) -> None:
        ...

class KerberosConfig(_message.Message):
    __slots__ = ('keytab', 'principal', 'krb5_config_gcs_uri')
    KEYTAB_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    KRB5_CONFIG_GCS_URI_FIELD_NUMBER: _ClassVar[int]
    keytab: Secret
    principal: str
    krb5_config_gcs_uri: str

    def __init__(self, keytab: _Optional[_Union[Secret, _Mapping]]=..., principal: _Optional[str]=..., krb5_config_gcs_uri: _Optional[str]=...) -> None:
        ...

class Secret(_message.Message):
    __slots__ = ('cloud_secret',)
    CLOUD_SECRET_FIELD_NUMBER: _ClassVar[int]
    cloud_secret: str

    def __init__(self, cloud_secret: _Optional[str]=...) -> None:
        ...

class EncryptionConfig(_message.Message):
    __slots__ = ('kms_key',)
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    kms_key: str

    def __init__(self, kms_key: _Optional[str]=...) -> None:
        ...

class AuxiliaryVersionConfig(_message.Message):
    __slots__ = ('version', 'config_overrides', 'network_config')

    class ConfigOverridesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    version: str
    config_overrides: _containers.ScalarMap[str, str]
    network_config: NetworkConfig

    def __init__(self, version: _Optional[str]=..., config_overrides: _Optional[_Mapping[str, str]]=..., network_config: _Optional[_Union[NetworkConfig, _Mapping]]=...) -> None:
        ...

class NetworkConfig(_message.Message):
    __slots__ = ('consumers',)

    class Consumer(_message.Message):
        __slots__ = ('subnetwork', 'endpoint_uri', 'endpoint_location')
        SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_URI_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_LOCATION_FIELD_NUMBER: _ClassVar[int]
        subnetwork: str
        endpoint_uri: str
        endpoint_location: str

        def __init__(self, subnetwork: _Optional[str]=..., endpoint_uri: _Optional[str]=..., endpoint_location: _Optional[str]=...) -> None:
            ...
    CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    consumers: _containers.RepeatedCompositeFieldContainer[NetworkConfig.Consumer]

    def __init__(self, consumers: _Optional[_Iterable[_Union[NetworkConfig.Consumer, _Mapping]]]=...) -> None:
        ...

class TelemetryConfig(_message.Message):
    __slots__ = ('log_format',)

    class LogFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOG_FORMAT_UNSPECIFIED: _ClassVar[TelemetryConfig.LogFormat]
        LEGACY: _ClassVar[TelemetryConfig.LogFormat]
        JSON: _ClassVar[TelemetryConfig.LogFormat]
    LOG_FORMAT_UNSPECIFIED: TelemetryConfig.LogFormat
    LEGACY: TelemetryConfig.LogFormat
    JSON: TelemetryConfig.LogFormat
    LOG_FORMAT_FIELD_NUMBER: _ClassVar[int]
    log_format: TelemetryConfig.LogFormat

    def __init__(self, log_format: _Optional[_Union[TelemetryConfig.LogFormat, str]]=...) -> None:
        ...

class MetadataManagementActivity(_message.Message):
    __slots__ = ('metadata_exports', 'restores')
    METADATA_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    RESTORES_FIELD_NUMBER: _ClassVar[int]
    metadata_exports: _containers.RepeatedCompositeFieldContainer[MetadataExport]
    restores: _containers.RepeatedCompositeFieldContainer[Restore]

    def __init__(self, metadata_exports: _Optional[_Iterable[_Union[MetadataExport, _Mapping]]]=..., restores: _Optional[_Iterable[_Union[Restore, _Mapping]]]=...) -> None:
        ...

class MetadataImport(_message.Message):
    __slots__ = ('database_dump', 'name', 'description', 'create_time', 'update_time', 'end_time', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MetadataImport.State]
        RUNNING: _ClassVar[MetadataImport.State]
        SUCCEEDED: _ClassVar[MetadataImport.State]
        UPDATING: _ClassVar[MetadataImport.State]
        FAILED: _ClassVar[MetadataImport.State]
    STATE_UNSPECIFIED: MetadataImport.State
    RUNNING: MetadataImport.State
    SUCCEEDED: MetadataImport.State
    UPDATING: MetadataImport.State
    FAILED: MetadataImport.State

    class DatabaseDump(_message.Message):
        __slots__ = ('database_type', 'gcs_uri', 'source_database', 'type')

        class DatabaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DATABASE_TYPE_UNSPECIFIED: _ClassVar[MetadataImport.DatabaseDump.DatabaseType]
            MYSQL: _ClassVar[MetadataImport.DatabaseDump.DatabaseType]
        DATABASE_TYPE_UNSPECIFIED: MetadataImport.DatabaseDump.DatabaseType
        MYSQL: MetadataImport.DatabaseDump.DatabaseType
        DATABASE_TYPE_FIELD_NUMBER: _ClassVar[int]
        GCS_URI_FIELD_NUMBER: _ClassVar[int]
        SOURCE_DATABASE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        database_type: MetadataImport.DatabaseDump.DatabaseType
        gcs_uri: str
        source_database: str
        type: DatabaseDumpSpec.Type

        def __init__(self, database_type: _Optional[_Union[MetadataImport.DatabaseDump.DatabaseType, str]]=..., gcs_uri: _Optional[str]=..., source_database: _Optional[str]=..., type: _Optional[_Union[DatabaseDumpSpec.Type, str]]=...) -> None:
            ...
    DATABASE_DUMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    database_dump: MetadataImport.DatabaseDump
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: MetadataImport.State

    def __init__(self, database_dump: _Optional[_Union[MetadataImport.DatabaseDump, _Mapping]]=..., name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[MetadataImport.State, str]]=...) -> None:
        ...

class MetadataExport(_message.Message):
    __slots__ = ('destination_gcs_uri', 'start_time', 'end_time', 'state', 'database_dump_type')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MetadataExport.State]
        RUNNING: _ClassVar[MetadataExport.State]
        SUCCEEDED: _ClassVar[MetadataExport.State]
        FAILED: _ClassVar[MetadataExport.State]
        CANCELLED: _ClassVar[MetadataExport.State]
    STATE_UNSPECIFIED: MetadataExport.State
    RUNNING: MetadataExport.State
    SUCCEEDED: MetadataExport.State
    FAILED: MetadataExport.State
    CANCELLED: MetadataExport.State
    DESTINATION_GCS_URI_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_DUMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    destination_gcs_uri: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: MetadataExport.State
    database_dump_type: DatabaseDumpSpec.Type

    def __init__(self, destination_gcs_uri: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[MetadataExport.State, str]]=..., database_dump_type: _Optional[_Union[DatabaseDumpSpec.Type, str]]=...) -> None:
        ...

class Backup(_message.Message):
    __slots__ = ('name', 'create_time', 'end_time', 'state', 'service_revision', 'description', 'restoring_services')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Backup.State]
        CREATING: _ClassVar[Backup.State]
        DELETING: _ClassVar[Backup.State]
        ACTIVE: _ClassVar[Backup.State]
        FAILED: _ClassVar[Backup.State]
        RESTORING: _ClassVar[Backup.State]
    STATE_UNSPECIFIED: Backup.State
    CREATING: Backup.State
    DELETING: Backup.State
    ACTIVE: Backup.State
    FAILED: Backup.State
    RESTORING: Backup.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_REVISION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESTORING_SERVICES_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: Backup.State
    service_revision: Service
    description: str
    restoring_services: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Backup.State, str]]=..., service_revision: _Optional[_Union[Service, _Mapping]]=..., description: _Optional[str]=..., restoring_services: _Optional[_Iterable[str]]=...) -> None:
        ...

class Restore(_message.Message):
    __slots__ = ('start_time', 'end_time', 'state', 'backup', 'type', 'details')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Restore.State]
        RUNNING: _ClassVar[Restore.State]
        SUCCEEDED: _ClassVar[Restore.State]
        FAILED: _ClassVar[Restore.State]
        CANCELLED: _ClassVar[Restore.State]
    STATE_UNSPECIFIED: Restore.State
    RUNNING: Restore.State
    SUCCEEDED: Restore.State
    FAILED: Restore.State
    CANCELLED: Restore.State

    class RestoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTORE_TYPE_UNSPECIFIED: _ClassVar[Restore.RestoreType]
        FULL: _ClassVar[Restore.RestoreType]
        METADATA_ONLY: _ClassVar[Restore.RestoreType]
    RESTORE_TYPE_UNSPECIFIED: Restore.RestoreType
    FULL: Restore.RestoreType
    METADATA_ONLY: Restore.RestoreType
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: Restore.State
    backup: str
    type: Restore.RestoreType
    details: str

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Restore.State, str]]=..., backup: _Optional[str]=..., type: _Optional[_Union[Restore.RestoreType, str]]=..., details: _Optional[str]=...) -> None:
        ...

class ScalingConfig(_message.Message):
    __slots__ = ('instance_size', 'scaling_factor')

    class InstanceSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTANCE_SIZE_UNSPECIFIED: _ClassVar[ScalingConfig.InstanceSize]
        EXTRA_SMALL: _ClassVar[ScalingConfig.InstanceSize]
        SMALL: _ClassVar[ScalingConfig.InstanceSize]
        MEDIUM: _ClassVar[ScalingConfig.InstanceSize]
        LARGE: _ClassVar[ScalingConfig.InstanceSize]
        EXTRA_LARGE: _ClassVar[ScalingConfig.InstanceSize]
    INSTANCE_SIZE_UNSPECIFIED: ScalingConfig.InstanceSize
    EXTRA_SMALL: ScalingConfig.InstanceSize
    SMALL: ScalingConfig.InstanceSize
    MEDIUM: ScalingConfig.InstanceSize
    LARGE: ScalingConfig.InstanceSize
    EXTRA_LARGE: ScalingConfig.InstanceSize
    INSTANCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SCALING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    instance_size: ScalingConfig.InstanceSize
    scaling_factor: float

    def __init__(self, instance_size: _Optional[_Union[ScalingConfig.InstanceSize, str]]=..., scaling_factor: _Optional[float]=...) -> None:
        ...

class ListServicesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListServicesResponse(_message.Message):
    __slots__ = ('services', 'next_page_token', 'unreachable')
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[Service]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, services: _Optional[_Iterable[_Union[Service, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateServiceRequest(_message.Message):
    __slots__ = ('parent', 'service_id', 'service', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_id: str
    service: Service
    request_id: str

    def __init__(self, parent: _Optional[str]=..., service_id: _Optional[str]=..., service: _Optional[_Union[Service, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateServiceRequest(_message.Message):
    __slots__ = ('update_mask', 'service', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    service: Service
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., service: _Optional[_Union[Service, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteServiceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListMetadataImportsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListMetadataImportsResponse(_message.Message):
    __slots__ = ('metadata_imports', 'next_page_token', 'unreachable')
    METADATA_IMPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    metadata_imports: _containers.RepeatedCompositeFieldContainer[MetadataImport]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, metadata_imports: _Optional[_Iterable[_Union[MetadataImport, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetMetadataImportRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateMetadataImportRequest(_message.Message):
    __slots__ = ('parent', 'metadata_import_id', 'metadata_import', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_IMPORT_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_IMPORT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    metadata_import_id: str
    metadata_import: MetadataImport
    request_id: str

    def __init__(self, parent: _Optional[str]=..., metadata_import_id: _Optional[str]=..., metadata_import: _Optional[_Union[MetadataImport, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateMetadataImportRequest(_message.Message):
    __slots__ = ('update_mask', 'metadata_import', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    METADATA_IMPORT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    metadata_import: MetadataImport
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., metadata_import: _Optional[_Union[MetadataImport, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListBackupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListBackupsResponse(_message.Message):
    __slots__ = ('backups', 'next_page_token', 'unreachable')
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[Backup]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, backups: _Optional[_Iterable[_Union[Backup, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateBackupRequest(_message.Message):
    __slots__ = ('parent', 'backup_id', 'backup', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_id: str
    backup: Backup
    request_id: str

    def __init__(self, parent: _Optional[str]=..., backup_id: _Optional[str]=..., backup: _Optional[_Union[Backup, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ExportMetadataRequest(_message.Message):
    __slots__ = ('destination_gcs_folder', 'service', 'request_id', 'database_dump_type')
    DESTINATION_GCS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_DUMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    destination_gcs_folder: str
    service: str
    request_id: str
    database_dump_type: DatabaseDumpSpec.Type

    def __init__(self, destination_gcs_folder: _Optional[str]=..., service: _Optional[str]=..., request_id: _Optional[str]=..., database_dump_type: _Optional[_Union[DatabaseDumpSpec.Type, str]]=...) -> None:
        ...

class RestoreServiceRequest(_message.Message):
    __slots__ = ('service', 'backup', 'restore_type', 'request_id')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    service: str
    backup: str
    restore_type: Restore.RestoreType
    request_id: str

    def __init__(self, service: _Optional[str]=..., backup: _Optional[str]=..., restore_type: _Optional[_Union[Restore.RestoreType, str]]=..., request_id: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class LocationMetadata(_message.Message):
    __slots__ = ('supported_hive_metastore_versions',)

    class HiveMetastoreVersion(_message.Message):
        __slots__ = ('version', 'is_default')
        VERSION_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        version: str
        is_default: bool

        def __init__(self, version: _Optional[str]=..., is_default: bool=...) -> None:
            ...
    SUPPORTED_HIVE_METASTORE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    supported_hive_metastore_versions: _containers.RepeatedCompositeFieldContainer[LocationMetadata.HiveMetastoreVersion]

    def __init__(self, supported_hive_metastore_versions: _Optional[_Iterable[_Union[LocationMetadata.HiveMetastoreVersion, _Mapping]]]=...) -> None:
        ...

class DatabaseDumpSpec(_message.Message):
    __slots__ = ()

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[DatabaseDumpSpec.Type]
        MYSQL: _ClassVar[DatabaseDumpSpec.Type]
        AVRO: _ClassVar[DatabaseDumpSpec.Type]
    TYPE_UNSPECIFIED: DatabaseDumpSpec.Type
    MYSQL: DatabaseDumpSpec.Type
    AVRO: DatabaseDumpSpec.Type

    def __init__(self) -> None:
        ...

class QueryMetadataRequest(_message.Message):
    __slots__ = ('service', 'query')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    service: str
    query: str

    def __init__(self, service: _Optional[str]=..., query: _Optional[str]=...) -> None:
        ...

class QueryMetadataResponse(_message.Message):
    __slots__ = ('result_manifest_uri',)
    RESULT_MANIFEST_URI_FIELD_NUMBER: _ClassVar[int]
    result_manifest_uri: str

    def __init__(self, result_manifest_uri: _Optional[str]=...) -> None:
        ...

class ErrorDetails(_message.Message):
    __slots__ = ('details',)

    class DetailsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.ScalarMap[str, str]

    def __init__(self, details: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class MoveTableToDatabaseRequest(_message.Message):
    __slots__ = ('service', 'table_name', 'db_name', 'destination_db_name')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DB_NAME_FIELD_NUMBER: _ClassVar[int]
    service: str
    table_name: str
    db_name: str
    destination_db_name: str

    def __init__(self, service: _Optional[str]=..., table_name: _Optional[str]=..., db_name: _Optional[str]=..., destination_db_name: _Optional[str]=...) -> None:
        ...

class MoveTableToDatabaseResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AlterMetadataResourceLocationRequest(_message.Message):
    __slots__ = ('service', 'resource_name', 'location_uri')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_URI_FIELD_NUMBER: _ClassVar[int]
    service: str
    resource_name: str
    location_uri: str

    def __init__(self, service: _Optional[str]=..., resource_name: _Optional[str]=..., location_uri: _Optional[str]=...) -> None:
        ...

class AlterMetadataResourceLocationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...