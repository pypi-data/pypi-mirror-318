from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.connectors.v1 import authconfig_pb2 as _authconfig_pb2
from google.cloud.connectors.v1 import common_pb2 as _common_pb2
from google.cloud.connectors.v1 import destination_config_pb2 as _destination_config_pb2
from google.cloud.connectors.v1 import ssl_config_pb2 as _ssl_config_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_TYPE_UNSPECIFIED: _ClassVar[DataType]
    DATA_TYPE_INT: _ClassVar[DataType]
    DATA_TYPE_SMALLINT: _ClassVar[DataType]
    DATA_TYPE_DOUBLE: _ClassVar[DataType]
    DATA_TYPE_DATE: _ClassVar[DataType]
    DATA_TYPE_DATETIME: _ClassVar[DataType]
    DATA_TYPE_TIME: _ClassVar[DataType]
    DATA_TYPE_STRING: _ClassVar[DataType]
    DATA_TYPE_LONG: _ClassVar[DataType]
    DATA_TYPE_BOOLEAN: _ClassVar[DataType]
    DATA_TYPE_DECIMAL: _ClassVar[DataType]
    DATA_TYPE_UUID: _ClassVar[DataType]
    DATA_TYPE_BLOB: _ClassVar[DataType]
    DATA_TYPE_BIT: _ClassVar[DataType]
    DATA_TYPE_TINYINT: _ClassVar[DataType]
    DATA_TYPE_INTEGER: _ClassVar[DataType]
    DATA_TYPE_BIGINT: _ClassVar[DataType]
    DATA_TYPE_FLOAT: _ClassVar[DataType]
    DATA_TYPE_REAL: _ClassVar[DataType]
    DATA_TYPE_NUMERIC: _ClassVar[DataType]
    DATA_TYPE_CHAR: _ClassVar[DataType]
    DATA_TYPE_VARCHAR: _ClassVar[DataType]
    DATA_TYPE_LONGVARCHAR: _ClassVar[DataType]
    DATA_TYPE_TIMESTAMP: _ClassVar[DataType]
    DATA_TYPE_NCHAR: _ClassVar[DataType]
    DATA_TYPE_NVARCHAR: _ClassVar[DataType]
    DATA_TYPE_LONGNVARCHAR: _ClassVar[DataType]
    DATA_TYPE_NULL: _ClassVar[DataType]
    DATA_TYPE_OTHER: _ClassVar[DataType]
    DATA_TYPE_JAVA_OBJECT: _ClassVar[DataType]
    DATA_TYPE_DISTINCT: _ClassVar[DataType]
    DATA_TYPE_STRUCT: _ClassVar[DataType]
    DATA_TYPE_ARRAY: _ClassVar[DataType]
    DATA_TYPE_CLOB: _ClassVar[DataType]
    DATA_TYPE_REF: _ClassVar[DataType]
    DATA_TYPE_DATALINK: _ClassVar[DataType]
    DATA_TYPE_ROWID: _ClassVar[DataType]
    DATA_TYPE_BINARY: _ClassVar[DataType]
    DATA_TYPE_VARBINARY: _ClassVar[DataType]
    DATA_TYPE_LONGVARBINARY: _ClassVar[DataType]
    DATA_TYPE_NCLOB: _ClassVar[DataType]
    DATA_TYPE_SQLXML: _ClassVar[DataType]
    DATA_TYPE_REF_CURSOR: _ClassVar[DataType]
    DATA_TYPE_TIME_WITH_TIMEZONE: _ClassVar[DataType]
    DATA_TYPE_TIMESTAMP_WITH_TIMEZONE: _ClassVar[DataType]

class ConnectionView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTION_VIEW_UNSPECIFIED: _ClassVar[ConnectionView]
    BASIC: _ClassVar[ConnectionView]
    FULL: _ClassVar[ConnectionView]
DATA_TYPE_UNSPECIFIED: DataType
DATA_TYPE_INT: DataType
DATA_TYPE_SMALLINT: DataType
DATA_TYPE_DOUBLE: DataType
DATA_TYPE_DATE: DataType
DATA_TYPE_DATETIME: DataType
DATA_TYPE_TIME: DataType
DATA_TYPE_STRING: DataType
DATA_TYPE_LONG: DataType
DATA_TYPE_BOOLEAN: DataType
DATA_TYPE_DECIMAL: DataType
DATA_TYPE_UUID: DataType
DATA_TYPE_BLOB: DataType
DATA_TYPE_BIT: DataType
DATA_TYPE_TINYINT: DataType
DATA_TYPE_INTEGER: DataType
DATA_TYPE_BIGINT: DataType
DATA_TYPE_FLOAT: DataType
DATA_TYPE_REAL: DataType
DATA_TYPE_NUMERIC: DataType
DATA_TYPE_CHAR: DataType
DATA_TYPE_VARCHAR: DataType
DATA_TYPE_LONGVARCHAR: DataType
DATA_TYPE_TIMESTAMP: DataType
DATA_TYPE_NCHAR: DataType
DATA_TYPE_NVARCHAR: DataType
DATA_TYPE_LONGNVARCHAR: DataType
DATA_TYPE_NULL: DataType
DATA_TYPE_OTHER: DataType
DATA_TYPE_JAVA_OBJECT: DataType
DATA_TYPE_DISTINCT: DataType
DATA_TYPE_STRUCT: DataType
DATA_TYPE_ARRAY: DataType
DATA_TYPE_CLOB: DataType
DATA_TYPE_REF: DataType
DATA_TYPE_DATALINK: DataType
DATA_TYPE_ROWID: DataType
DATA_TYPE_BINARY: DataType
DATA_TYPE_VARBINARY: DataType
DATA_TYPE_LONGVARBINARY: DataType
DATA_TYPE_NCLOB: DataType
DATA_TYPE_SQLXML: DataType
DATA_TYPE_REF_CURSOR: DataType
DATA_TYPE_TIME_WITH_TIMEZONE: DataType
DATA_TYPE_TIMESTAMP_WITH_TIMEZONE: DataType
CONNECTION_VIEW_UNSPECIFIED: ConnectionView
BASIC: ConnectionView
FULL: ConnectionView

class Connection(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'connector_version', 'status', 'config_variables', 'auth_config', 'lock_config', 'destination_configs', 'image_location', 'service_account', 'service_directory', 'envoy_image_location', 'suspended', 'node_config', 'ssl_config')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOCK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ENVOY_IMAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SSL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    connector_version: str
    status: ConnectionStatus
    config_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.ConfigVariable]
    auth_config: _authconfig_pb2.AuthConfig
    lock_config: LockConfig
    destination_configs: _containers.RepeatedCompositeFieldContainer[_destination_config_pb2.DestinationConfig]
    image_location: str
    service_account: str
    service_directory: str
    envoy_image_location: str
    suspended: bool
    node_config: NodeConfig
    ssl_config: _ssl_config_pb2.SslConfig

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., connector_version: _Optional[str]=..., status: _Optional[_Union[ConnectionStatus, _Mapping]]=..., config_variables: _Optional[_Iterable[_Union[_common_pb2.ConfigVariable, _Mapping]]]=..., auth_config: _Optional[_Union[_authconfig_pb2.AuthConfig, _Mapping]]=..., lock_config: _Optional[_Union[LockConfig, _Mapping]]=..., destination_configs: _Optional[_Iterable[_Union[_destination_config_pb2.DestinationConfig, _Mapping]]]=..., image_location: _Optional[str]=..., service_account: _Optional[str]=..., service_directory: _Optional[str]=..., envoy_image_location: _Optional[str]=..., suspended: bool=..., node_config: _Optional[_Union[NodeConfig, _Mapping]]=..., ssl_config: _Optional[_Union[_ssl_config_pb2.SslConfig, _Mapping]]=...) -> None:
        ...

class NodeConfig(_message.Message):
    __slots__ = ('min_node_count', 'max_node_count')
    MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_node_count: int
    max_node_count: int

    def __init__(self, min_node_count: _Optional[int]=..., max_node_count: _Optional[int]=...) -> None:
        ...

class ConnectionSchemaMetadata(_message.Message):
    __slots__ = ('entities', 'actions', 'name', 'update_time', 'refresh_time', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ConnectionSchemaMetadata.State]
        REFRESHING: _ClassVar[ConnectionSchemaMetadata.State]
        UPDATED: _ClassVar[ConnectionSchemaMetadata.State]
    STATE_UNSPECIFIED: ConnectionSchemaMetadata.State
    REFRESHING: ConnectionSchemaMetadata.State
    UPDATED: ConnectionSchemaMetadata.State
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedScalarFieldContainer[str]
    actions: _containers.RepeatedScalarFieldContainer[str]
    name: str
    update_time: _timestamp_pb2.Timestamp
    refresh_time: _timestamp_pb2.Timestamp
    state: ConnectionSchemaMetadata.State

    def __init__(self, entities: _Optional[_Iterable[str]]=..., actions: _Optional[_Iterable[str]]=..., name: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., refresh_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ConnectionSchemaMetadata.State, str]]=...) -> None:
        ...

class RuntimeEntitySchema(_message.Message):
    __slots__ = ('entity', 'fields')

    class Field(_message.Message):
        __slots__ = ('field', 'description', 'data_type', 'key', 'readonly', 'nullable', 'default_value', 'additional_details')
        FIELD_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        READONLY_FIELD_NUMBER: _ClassVar[int]
        NULLABLE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
        field: str
        description: str
        data_type: DataType
        key: bool
        readonly: bool
        nullable: bool
        default_value: _struct_pb2.Value
        additional_details: _struct_pb2.Struct

        def __init__(self, field: _Optional[str]=..., description: _Optional[str]=..., data_type: _Optional[_Union[DataType, str]]=..., key: bool=..., readonly: bool=..., nullable: bool=..., default_value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., additional_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
            ...
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    entity: str
    fields: _containers.RepeatedCompositeFieldContainer[RuntimeEntitySchema.Field]

    def __init__(self, entity: _Optional[str]=..., fields: _Optional[_Iterable[_Union[RuntimeEntitySchema.Field, _Mapping]]]=...) -> None:
        ...

class RuntimeActionSchema(_message.Message):
    __slots__ = ('action', 'input_parameters', 'result_metadata')

    class InputParameter(_message.Message):
        __slots__ = ('parameter', 'description', 'data_type', 'nullable', 'default_value')
        PARAMETER_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        NULLABLE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        parameter: str
        description: str
        data_type: DataType
        nullable: bool
        default_value: _struct_pb2.Value

        def __init__(self, parameter: _Optional[str]=..., description: _Optional[str]=..., data_type: _Optional[_Union[DataType, str]]=..., nullable: bool=..., default_value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...

    class ResultMetadata(_message.Message):
        __slots__ = ('field', 'description', 'data_type')
        FIELD_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        field: str
        description: str
        data_type: DataType

        def __init__(self, field: _Optional[str]=..., description: _Optional[str]=..., data_type: _Optional[_Union[DataType, str]]=...) -> None:
            ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    RESULT_METADATA_FIELD_NUMBER: _ClassVar[int]
    action: str
    input_parameters: _containers.RepeatedCompositeFieldContainer[RuntimeActionSchema.InputParameter]
    result_metadata: _containers.RepeatedCompositeFieldContainer[RuntimeActionSchema.ResultMetadata]

    def __init__(self, action: _Optional[str]=..., input_parameters: _Optional[_Iterable[_Union[RuntimeActionSchema.InputParameter, _Mapping]]]=..., result_metadata: _Optional[_Iterable[_Union[RuntimeActionSchema.ResultMetadata, _Mapping]]]=...) -> None:
        ...

class LockConfig(_message.Message):
    __slots__ = ('locked', 'reason')
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    locked: bool
    reason: str

    def __init__(self, locked: bool=..., reason: _Optional[str]=...) -> None:
        ...

class ListConnectionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: ConnectionView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., view: _Optional[_Union[ConnectionView, str]]=...) -> None:
        ...

class ListConnectionsResponse(_message.Message):
    __slots__ = ('connections', 'next_page_token', 'unreachable')
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[Connection]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, connections: _Optional[_Iterable[_Union[Connection, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetConnectionRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: ConnectionView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[ConnectionView, str]]=...) -> None:
        ...

class CreateConnectionRequest(_message.Message):
    __slots__ = ('parent', 'connection_id', 'connection')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connection_id: str
    connection: Connection

    def __init__(self, parent: _Optional[str]=..., connection_id: _Optional[str]=..., connection: _Optional[_Union[Connection, _Mapping]]=...) -> None:
        ...

class UpdateConnectionRequest(_message.Message):
    __slots__ = ('connection', 'update_mask')
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    connection: Connection
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, connection: _Optional[_Union[Connection, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetConnectionSchemaMetadataRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RefreshConnectionSchemaMetadataRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRuntimeEntitySchemasRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRuntimeEntitySchemasResponse(_message.Message):
    __slots__ = ('runtime_entity_schemas', 'next_page_token')
    RUNTIME_ENTITY_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    runtime_entity_schemas: _containers.RepeatedCompositeFieldContainer[RuntimeEntitySchema]
    next_page_token: str

    def __init__(self, runtime_entity_schemas: _Optional[_Iterable[_Union[RuntimeEntitySchema, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListRuntimeActionSchemasRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRuntimeActionSchemasResponse(_message.Message):
    __slots__ = ('runtime_action_schemas', 'next_page_token')
    RUNTIME_ACTION_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    runtime_action_schemas: _containers.RepeatedCompositeFieldContainer[RuntimeActionSchema]
    next_page_token: str

    def __init__(self, runtime_action_schemas: _Optional[_Iterable[_Union[RuntimeActionSchema, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ConnectionStatus(_message.Message):
    __slots__ = ('state', 'description', 'status')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ConnectionStatus.State]
        CREATING: _ClassVar[ConnectionStatus.State]
        ACTIVE: _ClassVar[ConnectionStatus.State]
        INACTIVE: _ClassVar[ConnectionStatus.State]
        DELETING: _ClassVar[ConnectionStatus.State]
        UPDATING: _ClassVar[ConnectionStatus.State]
        ERROR: _ClassVar[ConnectionStatus.State]
        AUTHORIZATION_REQUIRED: _ClassVar[ConnectionStatus.State]
    STATE_UNSPECIFIED: ConnectionStatus.State
    CREATING: ConnectionStatus.State
    ACTIVE: ConnectionStatus.State
    INACTIVE: ConnectionStatus.State
    DELETING: ConnectionStatus.State
    UPDATING: ConnectionStatus.State
    ERROR: ConnectionStatus.State
    AUTHORIZATION_REQUIRED: ConnectionStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    state: ConnectionStatus.State
    description: str
    status: str

    def __init__(self, state: _Optional[_Union[ConnectionStatus.State, str]]=..., description: _Optional[str]=..., status: _Optional[str]=...) -> None:
        ...