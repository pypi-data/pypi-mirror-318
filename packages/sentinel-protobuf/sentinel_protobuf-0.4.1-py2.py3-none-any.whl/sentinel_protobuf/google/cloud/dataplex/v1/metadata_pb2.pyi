from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StorageSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORAGE_SYSTEM_UNSPECIFIED: _ClassVar[StorageSystem]
    CLOUD_STORAGE: _ClassVar[StorageSystem]
    BIGQUERY: _ClassVar[StorageSystem]
STORAGE_SYSTEM_UNSPECIFIED: StorageSystem
CLOUD_STORAGE: StorageSystem
BIGQUERY: StorageSystem

class CreateEntityRequest(_message.Message):
    __slots__ = ('parent', 'entity', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity: Entity
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., entity: _Optional[_Union[Entity, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateEntityRequest(_message.Message):
    __slots__ = ('entity', 'validate_only')
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    entity: Entity
    validate_only: bool

    def __init__(self, entity: _Optional[_Union[Entity, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteEntityRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ListEntitiesRequest(_message.Message):
    __slots__ = ('parent', 'view', 'page_size', 'page_token', 'filter')

    class EntityView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENTITY_VIEW_UNSPECIFIED: _ClassVar[ListEntitiesRequest.EntityView]
        TABLES: _ClassVar[ListEntitiesRequest.EntityView]
        FILESETS: _ClassVar[ListEntitiesRequest.EntityView]
    ENTITY_VIEW_UNSPECIFIED: ListEntitiesRequest.EntityView
    TABLES: ListEntitiesRequest.EntityView
    FILESETS: ListEntitiesRequest.EntityView
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view: ListEntitiesRequest.EntityView
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., view: _Optional[_Union[ListEntitiesRequest.EntityView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListEntitiesResponse(_message.Message):
    __slots__ = ('entities', 'next_page_token')
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    next_page_token: str

    def __init__(self, entities: _Optional[_Iterable[_Union[Entity, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEntityRequest(_message.Message):
    __slots__ = ('name', 'view')

    class EntityView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENTITY_VIEW_UNSPECIFIED: _ClassVar[GetEntityRequest.EntityView]
        BASIC: _ClassVar[GetEntityRequest.EntityView]
        SCHEMA: _ClassVar[GetEntityRequest.EntityView]
        FULL: _ClassVar[GetEntityRequest.EntityView]
    ENTITY_VIEW_UNSPECIFIED: GetEntityRequest.EntityView
    BASIC: GetEntityRequest.EntityView
    SCHEMA: GetEntityRequest.EntityView
    FULL: GetEntityRequest.EntityView
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: GetEntityRequest.EntityView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[GetEntityRequest.EntityView, str]]=...) -> None:
        ...

class ListPartitionsRequest(_message.Message):
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

class CreatePartitionRequest(_message.Message):
    __slots__ = ('parent', 'partition', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    partition: Partition
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., partition: _Optional[_Union[Partition, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeletePartitionRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ListPartitionsResponse(_message.Message):
    __slots__ = ('partitions', 'next_page_token')
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedCompositeFieldContainer[Partition]
    next_page_token: str

    def __init__(self, partitions: _Optional[_Iterable[_Union[Partition, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPartitionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Entity(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'create_time', 'update_time', 'id', 'etag', 'type', 'asset', 'data_path', 'data_path_pattern', 'catalog_entry', 'system', 'format', 'compatibility', 'access', 'uid', 'schema')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Entity.Type]
        TABLE: _ClassVar[Entity.Type]
        FILESET: _ClassVar[Entity.Type]
    TYPE_UNSPECIFIED: Entity.Type
    TABLE: Entity.Type
    FILESET: Entity.Type

    class CompatibilityStatus(_message.Message):
        __slots__ = ('hive_metastore', 'bigquery')

        class Compatibility(_message.Message):
            __slots__ = ('compatible', 'reason')
            COMPATIBLE_FIELD_NUMBER: _ClassVar[int]
            REASON_FIELD_NUMBER: _ClassVar[int]
            compatible: bool
            reason: str

            def __init__(self, compatible: bool=..., reason: _Optional[str]=...) -> None:
                ...
        HIVE_METASTORE_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_FIELD_NUMBER: _ClassVar[int]
        hive_metastore: Entity.CompatibilityStatus.Compatibility
        bigquery: Entity.CompatibilityStatus.Compatibility

        def __init__(self, hive_metastore: _Optional[_Union[Entity.CompatibilityStatus.Compatibility, _Mapping]]=..., bigquery: _Optional[_Union[Entity.CompatibilityStatus.Compatibility, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    DATA_PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_PATH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ENTRY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    id: str
    etag: str
    type: Entity.Type
    asset: str
    data_path: str
    data_path_pattern: str
    catalog_entry: str
    system: StorageSystem
    format: StorageFormat
    compatibility: Entity.CompatibilityStatus
    access: StorageAccess
    uid: str
    schema: Schema

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., id: _Optional[str]=..., etag: _Optional[str]=..., type: _Optional[_Union[Entity.Type, str]]=..., asset: _Optional[str]=..., data_path: _Optional[str]=..., data_path_pattern: _Optional[str]=..., catalog_entry: _Optional[str]=..., system: _Optional[_Union[StorageSystem, str]]=..., format: _Optional[_Union[StorageFormat, _Mapping]]=..., compatibility: _Optional[_Union[Entity.CompatibilityStatus, _Mapping]]=..., access: _Optional[_Union[StorageAccess, _Mapping]]=..., uid: _Optional[str]=..., schema: _Optional[_Union[Schema, _Mapping]]=...) -> None:
        ...

class Partition(_message.Message):
    __slots__ = ('name', 'values', 'location', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedScalarFieldContainer[str]
    location: str
    etag: str

    def __init__(self, name: _Optional[str]=..., values: _Optional[_Iterable[str]]=..., location: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class Schema(_message.Message):
    __slots__ = ('user_managed', 'fields', 'partition_fields', 'partition_style')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Schema.Type]
        BOOLEAN: _ClassVar[Schema.Type]
        BYTE: _ClassVar[Schema.Type]
        INT16: _ClassVar[Schema.Type]
        INT32: _ClassVar[Schema.Type]
        INT64: _ClassVar[Schema.Type]
        FLOAT: _ClassVar[Schema.Type]
        DOUBLE: _ClassVar[Schema.Type]
        DECIMAL: _ClassVar[Schema.Type]
        STRING: _ClassVar[Schema.Type]
        BINARY: _ClassVar[Schema.Type]
        TIMESTAMP: _ClassVar[Schema.Type]
        DATE: _ClassVar[Schema.Type]
        TIME: _ClassVar[Schema.Type]
        RECORD: _ClassVar[Schema.Type]
        NULL: _ClassVar[Schema.Type]
    TYPE_UNSPECIFIED: Schema.Type
    BOOLEAN: Schema.Type
    BYTE: Schema.Type
    INT16: Schema.Type
    INT32: Schema.Type
    INT64: Schema.Type
    FLOAT: Schema.Type
    DOUBLE: Schema.Type
    DECIMAL: Schema.Type
    STRING: Schema.Type
    BINARY: Schema.Type
    TIMESTAMP: Schema.Type
    DATE: Schema.Type
    TIME: Schema.Type
    RECORD: Schema.Type
    NULL: Schema.Type

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[Schema.Mode]
        REQUIRED: _ClassVar[Schema.Mode]
        NULLABLE: _ClassVar[Schema.Mode]
        REPEATED: _ClassVar[Schema.Mode]
    MODE_UNSPECIFIED: Schema.Mode
    REQUIRED: Schema.Mode
    NULLABLE: Schema.Mode
    REPEATED: Schema.Mode

    class PartitionStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTITION_STYLE_UNSPECIFIED: _ClassVar[Schema.PartitionStyle]
        HIVE_COMPATIBLE: _ClassVar[Schema.PartitionStyle]
    PARTITION_STYLE_UNSPECIFIED: Schema.PartitionStyle
    HIVE_COMPATIBLE: Schema.PartitionStyle

    class SchemaField(_message.Message):
        __slots__ = ('name', 'description', 'type', 'mode', 'fields')
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        type: Schema.Type
        mode: Schema.Mode
        fields: _containers.RepeatedCompositeFieldContainer[Schema.SchemaField]

        def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., type: _Optional[_Union[Schema.Type, str]]=..., mode: _Optional[_Union[Schema.Mode, str]]=..., fields: _Optional[_Iterable[_Union[Schema.SchemaField, _Mapping]]]=...) -> None:
            ...

    class PartitionField(_message.Message):
        __slots__ = ('name', 'type')
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: Schema.Type

        def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[Schema.Type, str]]=...) -> None:
            ...
    USER_MANAGED_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_STYLE_FIELD_NUMBER: _ClassVar[int]
    user_managed: bool
    fields: _containers.RepeatedCompositeFieldContainer[Schema.SchemaField]
    partition_fields: _containers.RepeatedCompositeFieldContainer[Schema.PartitionField]
    partition_style: Schema.PartitionStyle

    def __init__(self, user_managed: bool=..., fields: _Optional[_Iterable[_Union[Schema.SchemaField, _Mapping]]]=..., partition_fields: _Optional[_Iterable[_Union[Schema.PartitionField, _Mapping]]]=..., partition_style: _Optional[_Union[Schema.PartitionStyle, str]]=...) -> None:
        ...

class StorageFormat(_message.Message):
    __slots__ = ('format', 'compression_format', 'mime_type', 'csv', 'json', 'iceberg')

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[StorageFormat.Format]
        PARQUET: _ClassVar[StorageFormat.Format]
        AVRO: _ClassVar[StorageFormat.Format]
        ORC: _ClassVar[StorageFormat.Format]
        CSV: _ClassVar[StorageFormat.Format]
        JSON: _ClassVar[StorageFormat.Format]
        IMAGE: _ClassVar[StorageFormat.Format]
        AUDIO: _ClassVar[StorageFormat.Format]
        VIDEO: _ClassVar[StorageFormat.Format]
        TEXT: _ClassVar[StorageFormat.Format]
        TFRECORD: _ClassVar[StorageFormat.Format]
        OTHER: _ClassVar[StorageFormat.Format]
        UNKNOWN: _ClassVar[StorageFormat.Format]
    FORMAT_UNSPECIFIED: StorageFormat.Format
    PARQUET: StorageFormat.Format
    AVRO: StorageFormat.Format
    ORC: StorageFormat.Format
    CSV: StorageFormat.Format
    JSON: StorageFormat.Format
    IMAGE: StorageFormat.Format
    AUDIO: StorageFormat.Format
    VIDEO: StorageFormat.Format
    TEXT: StorageFormat.Format
    TFRECORD: StorageFormat.Format
    OTHER: StorageFormat.Format
    UNKNOWN: StorageFormat.Format

    class CompressionFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPRESSION_FORMAT_UNSPECIFIED: _ClassVar[StorageFormat.CompressionFormat]
        GZIP: _ClassVar[StorageFormat.CompressionFormat]
        BZIP2: _ClassVar[StorageFormat.CompressionFormat]
    COMPRESSION_FORMAT_UNSPECIFIED: StorageFormat.CompressionFormat
    GZIP: StorageFormat.CompressionFormat
    BZIP2: StorageFormat.CompressionFormat

    class CsvOptions(_message.Message):
        __slots__ = ('encoding', 'header_rows', 'delimiter', 'quote')
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        HEADER_ROWS_FIELD_NUMBER: _ClassVar[int]
        DELIMITER_FIELD_NUMBER: _ClassVar[int]
        QUOTE_FIELD_NUMBER: _ClassVar[int]
        encoding: str
        header_rows: int
        delimiter: str
        quote: str

        def __init__(self, encoding: _Optional[str]=..., header_rows: _Optional[int]=..., delimiter: _Optional[str]=..., quote: _Optional[str]=...) -> None:
            ...

    class JsonOptions(_message.Message):
        __slots__ = ('encoding',)
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        encoding: str

        def __init__(self, encoding: _Optional[str]=...) -> None:
            ...

    class IcebergOptions(_message.Message):
        __slots__ = ('metadata_location',)
        METADATA_LOCATION_FIELD_NUMBER: _ClassVar[int]
        metadata_location: str

        def __init__(self, metadata_location: _Optional[str]=...) -> None:
            ...
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FORMAT_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    CSV_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    ICEBERG_FIELD_NUMBER: _ClassVar[int]
    format: StorageFormat.Format
    compression_format: StorageFormat.CompressionFormat
    mime_type: str
    csv: StorageFormat.CsvOptions
    json: StorageFormat.JsonOptions
    iceberg: StorageFormat.IcebergOptions

    def __init__(self, format: _Optional[_Union[StorageFormat.Format, str]]=..., compression_format: _Optional[_Union[StorageFormat.CompressionFormat, str]]=..., mime_type: _Optional[str]=..., csv: _Optional[_Union[StorageFormat.CsvOptions, _Mapping]]=..., json: _Optional[_Union[StorageFormat.JsonOptions, _Mapping]]=..., iceberg: _Optional[_Union[StorageFormat.IcebergOptions, _Mapping]]=...) -> None:
        ...

class StorageAccess(_message.Message):
    __slots__ = ('read',)

    class AccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCESS_MODE_UNSPECIFIED: _ClassVar[StorageAccess.AccessMode]
        DIRECT: _ClassVar[StorageAccess.AccessMode]
        MANAGED: _ClassVar[StorageAccess.AccessMode]
    ACCESS_MODE_UNSPECIFIED: StorageAccess.AccessMode
    DIRECT: StorageAccess.AccessMode
    MANAGED: StorageAccess.AccessMode
    READ_FIELD_NUMBER: _ClassVar[int]
    read: StorageAccess.AccessMode

    def __init__(self, read: _Optional[_Union[StorageAccess.AccessMode, str]]=...) -> None:
        ...