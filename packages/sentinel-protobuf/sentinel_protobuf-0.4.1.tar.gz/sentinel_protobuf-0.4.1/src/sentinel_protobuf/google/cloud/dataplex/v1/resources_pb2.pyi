from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[State]
    ACTIVE: _ClassVar[State]
    CREATING: _ClassVar[State]
    DELETING: _ClassVar[State]
    ACTION_REQUIRED: _ClassVar[State]
STATE_UNSPECIFIED: State
ACTIVE: State
CREATING: State
DELETING: State
ACTION_REQUIRED: State

class Lake(_message.Message):
    __slots__ = ('name', 'display_name', 'uid', 'create_time', 'update_time', 'labels', 'description', 'state', 'service_account', 'metastore', 'asset_status', 'metastore_status')

    class Metastore(_message.Message):
        __slots__ = ('service',)
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        service: str

        def __init__(self, service: _Optional[str]=...) -> None:
            ...

    class MetastoreStatus(_message.Message):
        __slots__ = ('state', 'message', 'update_time', 'endpoint')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Lake.MetastoreStatus.State]
            NONE: _ClassVar[Lake.MetastoreStatus.State]
            READY: _ClassVar[Lake.MetastoreStatus.State]
            UPDATING: _ClassVar[Lake.MetastoreStatus.State]
            ERROR: _ClassVar[Lake.MetastoreStatus.State]
        STATE_UNSPECIFIED: Lake.MetastoreStatus.State
        NONE: Lake.MetastoreStatus.State
        READY: Lake.MetastoreStatus.State
        UPDATING: Lake.MetastoreStatus.State
        ERROR: Lake.MetastoreStatus.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        state: Lake.MetastoreStatus.State
        message: str
        update_time: _timestamp_pb2.Timestamp
        endpoint: str

        def __init__(self, state: _Optional[_Union[Lake.MetastoreStatus.State, str]]=..., message: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., endpoint: _Optional[str]=...) -> None:
            ...

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
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    METASTORE_FIELD_NUMBER: _ClassVar[int]
    ASSET_STATUS_FIELD_NUMBER: _ClassVar[int]
    METASTORE_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    state: State
    service_account: str
    metastore: Lake.Metastore
    asset_status: AssetStatus
    metastore_status: Lake.MetastoreStatus

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., state: _Optional[_Union[State, str]]=..., service_account: _Optional[str]=..., metastore: _Optional[_Union[Lake.Metastore, _Mapping]]=..., asset_status: _Optional[_Union[AssetStatus, _Mapping]]=..., metastore_status: _Optional[_Union[Lake.MetastoreStatus, _Mapping]]=...) -> None:
        ...

class AssetStatus(_message.Message):
    __slots__ = ('update_time', 'active_assets', 'security_policy_applying_assets')
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ASSETS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_POLICY_APPLYING_ASSETS_FIELD_NUMBER: _ClassVar[int]
    update_time: _timestamp_pb2.Timestamp
    active_assets: int
    security_policy_applying_assets: int

    def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., active_assets: _Optional[int]=..., security_policy_applying_assets: _Optional[int]=...) -> None:
        ...

class Zone(_message.Message):
    __slots__ = ('name', 'display_name', 'uid', 'create_time', 'update_time', 'labels', 'description', 'state', 'type', 'discovery_spec', 'resource_spec', 'asset_status')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Zone.Type]
        RAW: _ClassVar[Zone.Type]
        CURATED: _ClassVar[Zone.Type]
    TYPE_UNSPECIFIED: Zone.Type
    RAW: Zone.Type
    CURATED: Zone.Type

    class ResourceSpec(_message.Message):
        __slots__ = ('location_type',)

        class LocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LOCATION_TYPE_UNSPECIFIED: _ClassVar[Zone.ResourceSpec.LocationType]
            SINGLE_REGION: _ClassVar[Zone.ResourceSpec.LocationType]
            MULTI_REGION: _ClassVar[Zone.ResourceSpec.LocationType]
        LOCATION_TYPE_UNSPECIFIED: Zone.ResourceSpec.LocationType
        SINGLE_REGION: Zone.ResourceSpec.LocationType
        MULTI_REGION: Zone.ResourceSpec.LocationType
        LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        location_type: Zone.ResourceSpec.LocationType

        def __init__(self, location_type: _Optional[_Union[Zone.ResourceSpec.LocationType, str]]=...) -> None:
            ...

    class DiscoverySpec(_message.Message):
        __slots__ = ('enabled', 'include_patterns', 'exclude_patterns', 'csv_options', 'json_options', 'schedule')

        class CsvOptions(_message.Message):
            __slots__ = ('header_rows', 'delimiter', 'encoding', 'disable_type_inference')
            HEADER_ROWS_FIELD_NUMBER: _ClassVar[int]
            DELIMITER_FIELD_NUMBER: _ClassVar[int]
            ENCODING_FIELD_NUMBER: _ClassVar[int]
            DISABLE_TYPE_INFERENCE_FIELD_NUMBER: _ClassVar[int]
            header_rows: int
            delimiter: str
            encoding: str
            disable_type_inference: bool

            def __init__(self, header_rows: _Optional[int]=..., delimiter: _Optional[str]=..., encoding: _Optional[str]=..., disable_type_inference: bool=...) -> None:
                ...

        class JsonOptions(_message.Message):
            __slots__ = ('encoding', 'disable_type_inference')
            ENCODING_FIELD_NUMBER: _ClassVar[int]
            DISABLE_TYPE_INFERENCE_FIELD_NUMBER: _ClassVar[int]
            encoding: str
            disable_type_inference: bool

            def __init__(self, encoding: _Optional[str]=..., disable_type_inference: bool=...) -> None:
                ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
        EXCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
        CSV_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        JSON_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        include_patterns: _containers.RepeatedScalarFieldContainer[str]
        exclude_patterns: _containers.RepeatedScalarFieldContainer[str]
        csv_options: Zone.DiscoverySpec.CsvOptions
        json_options: Zone.DiscoverySpec.JsonOptions
        schedule: str

        def __init__(self, enabled: bool=..., include_patterns: _Optional[_Iterable[str]]=..., exclude_patterns: _Optional[_Iterable[str]]=..., csv_options: _Optional[_Union[Zone.DiscoverySpec.CsvOptions, _Mapping]]=..., json_options: _Optional[_Union[Zone.DiscoverySpec.JsonOptions, _Mapping]]=..., schedule: _Optional[str]=...) -> None:
            ...

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
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_SPEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SPEC_FIELD_NUMBER: _ClassVar[int]
    ASSET_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    state: State
    type: Zone.Type
    discovery_spec: Zone.DiscoverySpec
    resource_spec: Zone.ResourceSpec
    asset_status: AssetStatus

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., state: _Optional[_Union[State, str]]=..., type: _Optional[_Union[Zone.Type, str]]=..., discovery_spec: _Optional[_Union[Zone.DiscoverySpec, _Mapping]]=..., resource_spec: _Optional[_Union[Zone.ResourceSpec, _Mapping]]=..., asset_status: _Optional[_Union[AssetStatus, _Mapping]]=...) -> None:
        ...

class Action(_message.Message):
    __slots__ = ('category', 'issue', 'detect_time', 'name', 'lake', 'zone', 'asset', 'data_locations', 'invalid_data_format', 'incompatible_data_schema', 'invalid_data_partition', 'missing_data', 'missing_resource', 'unauthorized_resource', 'failed_security_policy_apply', 'invalid_data_organization')

    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATEGORY_UNSPECIFIED: _ClassVar[Action.Category]
        RESOURCE_MANAGEMENT: _ClassVar[Action.Category]
        SECURITY_POLICY: _ClassVar[Action.Category]
        DATA_DISCOVERY: _ClassVar[Action.Category]
    CATEGORY_UNSPECIFIED: Action.Category
    RESOURCE_MANAGEMENT: Action.Category
    SECURITY_POLICY: Action.Category
    DATA_DISCOVERY: Action.Category

    class MissingResource(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class UnauthorizedResource(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class FailedSecurityPolicyApply(_message.Message):
        __slots__ = ('asset',)
        ASSET_FIELD_NUMBER: _ClassVar[int]
        asset: str

        def __init__(self, asset: _Optional[str]=...) -> None:
            ...

    class InvalidDataFormat(_message.Message):
        __slots__ = ('sampled_data_locations', 'expected_format', 'new_format')
        SAMPLED_DATA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_FORMAT_FIELD_NUMBER: _ClassVar[int]
        NEW_FORMAT_FIELD_NUMBER: _ClassVar[int]
        sampled_data_locations: _containers.RepeatedScalarFieldContainer[str]
        expected_format: str
        new_format: str

        def __init__(self, sampled_data_locations: _Optional[_Iterable[str]]=..., expected_format: _Optional[str]=..., new_format: _Optional[str]=...) -> None:
            ...

    class IncompatibleDataSchema(_message.Message):
        __slots__ = ('table', 'existing_schema', 'new_schema', 'sampled_data_locations', 'schema_change')

        class SchemaChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCHEMA_CHANGE_UNSPECIFIED: _ClassVar[Action.IncompatibleDataSchema.SchemaChange]
            INCOMPATIBLE: _ClassVar[Action.IncompatibleDataSchema.SchemaChange]
            MODIFIED: _ClassVar[Action.IncompatibleDataSchema.SchemaChange]
        SCHEMA_CHANGE_UNSPECIFIED: Action.IncompatibleDataSchema.SchemaChange
        INCOMPATIBLE: Action.IncompatibleDataSchema.SchemaChange
        MODIFIED: Action.IncompatibleDataSchema.SchemaChange
        TABLE_FIELD_NUMBER: _ClassVar[int]
        EXISTING_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        NEW_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        SAMPLED_DATA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_CHANGE_FIELD_NUMBER: _ClassVar[int]
        table: str
        existing_schema: str
        new_schema: str
        sampled_data_locations: _containers.RepeatedScalarFieldContainer[str]
        schema_change: Action.IncompatibleDataSchema.SchemaChange

        def __init__(self, table: _Optional[str]=..., existing_schema: _Optional[str]=..., new_schema: _Optional[str]=..., sampled_data_locations: _Optional[_Iterable[str]]=..., schema_change: _Optional[_Union[Action.IncompatibleDataSchema.SchemaChange, str]]=...) -> None:
            ...

    class InvalidDataPartition(_message.Message):
        __slots__ = ('expected_structure',)

        class PartitionStructure(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PARTITION_STRUCTURE_UNSPECIFIED: _ClassVar[Action.InvalidDataPartition.PartitionStructure]
            CONSISTENT_KEYS: _ClassVar[Action.InvalidDataPartition.PartitionStructure]
            HIVE_STYLE_KEYS: _ClassVar[Action.InvalidDataPartition.PartitionStructure]
        PARTITION_STRUCTURE_UNSPECIFIED: Action.InvalidDataPartition.PartitionStructure
        CONSISTENT_KEYS: Action.InvalidDataPartition.PartitionStructure
        HIVE_STYLE_KEYS: Action.InvalidDataPartition.PartitionStructure
        EXPECTED_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
        expected_structure: Action.InvalidDataPartition.PartitionStructure

        def __init__(self, expected_structure: _Optional[_Union[Action.InvalidDataPartition.PartitionStructure, str]]=...) -> None:
            ...

    class MissingData(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class InvalidDataOrganization(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    DETECT_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAKE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    INVALID_DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    INCOMPATIBLE_DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    INVALID_DATA_PARTITION_FIELD_NUMBER: _ClassVar[int]
    MISSING_DATA_FIELD_NUMBER: _ClassVar[int]
    MISSING_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    UNAUTHORIZED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    FAILED_SECURITY_POLICY_APPLY_FIELD_NUMBER: _ClassVar[int]
    INVALID_DATA_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    category: Action.Category
    issue: str
    detect_time: _timestamp_pb2.Timestamp
    name: str
    lake: str
    zone: str
    asset: str
    data_locations: _containers.RepeatedScalarFieldContainer[str]
    invalid_data_format: Action.InvalidDataFormat
    incompatible_data_schema: Action.IncompatibleDataSchema
    invalid_data_partition: Action.InvalidDataPartition
    missing_data: Action.MissingData
    missing_resource: Action.MissingResource
    unauthorized_resource: Action.UnauthorizedResource
    failed_security_policy_apply: Action.FailedSecurityPolicyApply
    invalid_data_organization: Action.InvalidDataOrganization

    def __init__(self, category: _Optional[_Union[Action.Category, str]]=..., issue: _Optional[str]=..., detect_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=..., lake: _Optional[str]=..., zone: _Optional[str]=..., asset: _Optional[str]=..., data_locations: _Optional[_Iterable[str]]=..., invalid_data_format: _Optional[_Union[Action.InvalidDataFormat, _Mapping]]=..., incompatible_data_schema: _Optional[_Union[Action.IncompatibleDataSchema, _Mapping]]=..., invalid_data_partition: _Optional[_Union[Action.InvalidDataPartition, _Mapping]]=..., missing_data: _Optional[_Union[Action.MissingData, _Mapping]]=..., missing_resource: _Optional[_Union[Action.MissingResource, _Mapping]]=..., unauthorized_resource: _Optional[_Union[Action.UnauthorizedResource, _Mapping]]=..., failed_security_policy_apply: _Optional[_Union[Action.FailedSecurityPolicyApply, _Mapping]]=..., invalid_data_organization: _Optional[_Union[Action.InvalidDataOrganization, _Mapping]]=...) -> None:
        ...

class Asset(_message.Message):
    __slots__ = ('name', 'display_name', 'uid', 'create_time', 'update_time', 'labels', 'description', 'state', 'resource_spec', 'resource_status', 'security_status', 'discovery_spec', 'discovery_status')

    class SecurityStatus(_message.Message):
        __slots__ = ('state', 'message', 'update_time')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Asset.SecurityStatus.State]
            READY: _ClassVar[Asset.SecurityStatus.State]
            APPLYING: _ClassVar[Asset.SecurityStatus.State]
            ERROR: _ClassVar[Asset.SecurityStatus.State]
        STATE_UNSPECIFIED: Asset.SecurityStatus.State
        READY: Asset.SecurityStatus.State
        APPLYING: Asset.SecurityStatus.State
        ERROR: Asset.SecurityStatus.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        state: Asset.SecurityStatus.State
        message: str
        update_time: _timestamp_pb2.Timestamp

        def __init__(self, state: _Optional[_Union[Asset.SecurityStatus.State, str]]=..., message: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class DiscoverySpec(_message.Message):
        __slots__ = ('enabled', 'include_patterns', 'exclude_patterns', 'csv_options', 'json_options', 'schedule')

        class CsvOptions(_message.Message):
            __slots__ = ('header_rows', 'delimiter', 'encoding', 'disable_type_inference')
            HEADER_ROWS_FIELD_NUMBER: _ClassVar[int]
            DELIMITER_FIELD_NUMBER: _ClassVar[int]
            ENCODING_FIELD_NUMBER: _ClassVar[int]
            DISABLE_TYPE_INFERENCE_FIELD_NUMBER: _ClassVar[int]
            header_rows: int
            delimiter: str
            encoding: str
            disable_type_inference: bool

            def __init__(self, header_rows: _Optional[int]=..., delimiter: _Optional[str]=..., encoding: _Optional[str]=..., disable_type_inference: bool=...) -> None:
                ...

        class JsonOptions(_message.Message):
            __slots__ = ('encoding', 'disable_type_inference')
            ENCODING_FIELD_NUMBER: _ClassVar[int]
            DISABLE_TYPE_INFERENCE_FIELD_NUMBER: _ClassVar[int]
            encoding: str
            disable_type_inference: bool

            def __init__(self, encoding: _Optional[str]=..., disable_type_inference: bool=...) -> None:
                ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
        EXCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
        CSV_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        JSON_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        include_patterns: _containers.RepeatedScalarFieldContainer[str]
        exclude_patterns: _containers.RepeatedScalarFieldContainer[str]
        csv_options: Asset.DiscoverySpec.CsvOptions
        json_options: Asset.DiscoverySpec.JsonOptions
        schedule: str

        def __init__(self, enabled: bool=..., include_patterns: _Optional[_Iterable[str]]=..., exclude_patterns: _Optional[_Iterable[str]]=..., csv_options: _Optional[_Union[Asset.DiscoverySpec.CsvOptions, _Mapping]]=..., json_options: _Optional[_Union[Asset.DiscoverySpec.JsonOptions, _Mapping]]=..., schedule: _Optional[str]=...) -> None:
            ...

    class ResourceSpec(_message.Message):
        __slots__ = ('name', 'type', 'read_access_mode')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[Asset.ResourceSpec.Type]
            STORAGE_BUCKET: _ClassVar[Asset.ResourceSpec.Type]
            BIGQUERY_DATASET: _ClassVar[Asset.ResourceSpec.Type]
        TYPE_UNSPECIFIED: Asset.ResourceSpec.Type
        STORAGE_BUCKET: Asset.ResourceSpec.Type
        BIGQUERY_DATASET: Asset.ResourceSpec.Type

        class AccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACCESS_MODE_UNSPECIFIED: _ClassVar[Asset.ResourceSpec.AccessMode]
            DIRECT: _ClassVar[Asset.ResourceSpec.AccessMode]
            MANAGED: _ClassVar[Asset.ResourceSpec.AccessMode]
        ACCESS_MODE_UNSPECIFIED: Asset.ResourceSpec.AccessMode
        DIRECT: Asset.ResourceSpec.AccessMode
        MANAGED: Asset.ResourceSpec.AccessMode
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        READ_ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: Asset.ResourceSpec.Type
        read_access_mode: Asset.ResourceSpec.AccessMode

        def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[Asset.ResourceSpec.Type, str]]=..., read_access_mode: _Optional[_Union[Asset.ResourceSpec.AccessMode, str]]=...) -> None:
            ...

    class ResourceStatus(_message.Message):
        __slots__ = ('state', 'message', 'update_time', 'managed_access_identity')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Asset.ResourceStatus.State]
            READY: _ClassVar[Asset.ResourceStatus.State]
            ERROR: _ClassVar[Asset.ResourceStatus.State]
        STATE_UNSPECIFIED: Asset.ResourceStatus.State
        READY: Asset.ResourceStatus.State
        ERROR: Asset.ResourceStatus.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        MANAGED_ACCESS_IDENTITY_FIELD_NUMBER: _ClassVar[int]
        state: Asset.ResourceStatus.State
        message: str
        update_time: _timestamp_pb2.Timestamp
        managed_access_identity: str

        def __init__(self, state: _Optional[_Union[Asset.ResourceStatus.State, str]]=..., message: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., managed_access_identity: _Optional[str]=...) -> None:
            ...

    class DiscoveryStatus(_message.Message):
        __slots__ = ('state', 'message', 'update_time', 'last_run_time', 'stats', 'last_run_duration')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Asset.DiscoveryStatus.State]
            SCHEDULED: _ClassVar[Asset.DiscoveryStatus.State]
            IN_PROGRESS: _ClassVar[Asset.DiscoveryStatus.State]
            PAUSED: _ClassVar[Asset.DiscoveryStatus.State]
            DISABLED: _ClassVar[Asset.DiscoveryStatus.State]
        STATE_UNSPECIFIED: Asset.DiscoveryStatus.State
        SCHEDULED: Asset.DiscoveryStatus.State
        IN_PROGRESS: Asset.DiscoveryStatus.State
        PAUSED: Asset.DiscoveryStatus.State
        DISABLED: Asset.DiscoveryStatus.State

        class Stats(_message.Message):
            __slots__ = ('data_items', 'data_size', 'tables', 'filesets')
            DATA_ITEMS_FIELD_NUMBER: _ClassVar[int]
            DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
            TABLES_FIELD_NUMBER: _ClassVar[int]
            FILESETS_FIELD_NUMBER: _ClassVar[int]
            data_items: int
            data_size: int
            tables: int
            filesets: int

            def __init__(self, data_items: _Optional[int]=..., data_size: _Optional[int]=..., tables: _Optional[int]=..., filesets: _Optional[int]=...) -> None:
                ...
        STATE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        LAST_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        LAST_RUN_DURATION_FIELD_NUMBER: _ClassVar[int]
        state: Asset.DiscoveryStatus.State
        message: str
        update_time: _timestamp_pb2.Timestamp
        last_run_time: _timestamp_pb2.Timestamp
        stats: Asset.DiscoveryStatus.Stats
        last_run_duration: _duration_pb2.Duration

        def __init__(self, state: _Optional[_Union[Asset.DiscoveryStatus.State, str]]=..., message: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., stats: _Optional[_Union[Asset.DiscoveryStatus.Stats, _Mapping]]=..., last_run_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

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
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SPEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_SPEC_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    state: State
    resource_spec: Asset.ResourceSpec
    resource_status: Asset.ResourceStatus
    security_status: Asset.SecurityStatus
    discovery_spec: Asset.DiscoverySpec
    discovery_status: Asset.DiscoveryStatus

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., state: _Optional[_Union[State, str]]=..., resource_spec: _Optional[_Union[Asset.ResourceSpec, _Mapping]]=..., resource_status: _Optional[_Union[Asset.ResourceStatus, _Mapping]]=..., security_status: _Optional[_Union[Asset.SecurityStatus, _Mapping]]=..., discovery_spec: _Optional[_Union[Asset.DiscoverySpec, _Mapping]]=..., discovery_status: _Optional[_Union[Asset.DiscoveryStatus, _Mapping]]=...) -> None:
        ...