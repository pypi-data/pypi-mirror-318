from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TableView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TABLE_VIEW_UNSPECIFIED: _ClassVar[TableView]
    BASIC: _ClassVar[TableView]
    FULL: _ClassVar[TableView]
TABLE_VIEW_UNSPECIFIED: TableView
BASIC: TableView
FULL: TableView

class Catalog(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'delete_time', 'expire_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Database(_message.Message):
    __slots__ = ('hive_options', 'name', 'create_time', 'update_time', 'delete_time', 'expire_time', 'type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Database.Type]
        HIVE: _ClassVar[Database.Type]
    TYPE_UNSPECIFIED: Database.Type
    HIVE: Database.Type
    HIVE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    hive_options: HiveDatabaseOptions
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    type: Database.Type

    def __init__(self, hive_options: _Optional[_Union[HiveDatabaseOptions, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., type: _Optional[_Union[Database.Type, str]]=...) -> None:
        ...

class Table(_message.Message):
    __slots__ = ('hive_options', 'name', 'create_time', 'update_time', 'delete_time', 'expire_time', 'type', 'etag')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Table.Type]
        HIVE: _ClassVar[Table.Type]
    TYPE_UNSPECIFIED: Table.Type
    HIVE: Table.Type
    HIVE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    hive_options: HiveTableOptions
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    type: Table.Type
    etag: str

    def __init__(self, hive_options: _Optional[_Union[HiveTableOptions, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., type: _Optional[_Union[Table.Type, str]]=..., etag: _Optional[str]=...) -> None:
        ...

class CreateCatalogRequest(_message.Message):
    __slots__ = ('parent', 'catalog', 'catalog_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    catalog: Catalog
    catalog_id: str

    def __init__(self, parent: _Optional[str]=..., catalog: _Optional[_Union[Catalog, _Mapping]]=..., catalog_id: _Optional[str]=...) -> None:
        ...

class DeleteCatalogRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetCatalogRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCatalogsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListCatalogsResponse(_message.Message):
    __slots__ = ('catalogs', 'next_page_token')
    CATALOGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    catalogs: _containers.RepeatedCompositeFieldContainer[Catalog]
    next_page_token: str

    def __init__(self, catalogs: _Optional[_Iterable[_Union[Catalog, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateDatabaseRequest(_message.Message):
    __slots__ = ('parent', 'database', 'database_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    database: Database
    database_id: str

    def __init__(self, parent: _Optional[str]=..., database: _Optional[_Union[Database, _Mapping]]=..., database_id: _Optional[str]=...) -> None:
        ...

class DeleteDatabaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDatabaseRequest(_message.Message):
    __slots__ = ('database', 'update_mask')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    database: Database
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, database: _Optional[_Union[Database, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetDatabaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDatabasesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDatabasesResponse(_message.Message):
    __slots__ = ('databases', 'next_page_token')
    DATABASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    databases: _containers.RepeatedCompositeFieldContainer[Database]
    next_page_token: str

    def __init__(self, databases: _Optional[_Iterable[_Union[Database, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateTableRequest(_message.Message):
    __slots__ = ('parent', 'table', 'table_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    table: Table
    table_id: str

    def __init__(self, parent: _Optional[str]=..., table: _Optional[_Union[Table, _Mapping]]=..., table_id: _Optional[str]=...) -> None:
        ...

class DeleteTableRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateTableRequest(_message.Message):
    __slots__ = ('table', 'update_mask')
    TABLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    table: Table
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, table: _Optional[_Union[Table, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class RenameTableRequest(_message.Message):
    __slots__ = ('name', 'new_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_name: str

    def __init__(self, name: _Optional[str]=..., new_name: _Optional[str]=...) -> None:
        ...

class GetTableRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTablesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: TableView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[TableView, str]]=...) -> None:
        ...

class ListTablesResponse(_message.Message):
    __slots__ = ('tables', 'next_page_token')
    TABLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedCompositeFieldContainer[Table]
    next_page_token: str

    def __init__(self, tables: _Optional[_Iterable[_Union[Table, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class HiveDatabaseOptions(_message.Message):
    __slots__ = ('location_uri', 'parameters')

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    LOCATION_URI_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    location_uri: str
    parameters: _containers.ScalarMap[str, str]

    def __init__(self, location_uri: _Optional[str]=..., parameters: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class HiveTableOptions(_message.Message):
    __slots__ = ('parameters', 'table_type', 'storage_descriptor')

    class SerDeInfo(_message.Message):
        __slots__ = ('serialization_lib',)
        SERIALIZATION_LIB_FIELD_NUMBER: _ClassVar[int]
        serialization_lib: str

        def __init__(self, serialization_lib: _Optional[str]=...) -> None:
            ...

    class StorageDescriptor(_message.Message):
        __slots__ = ('location_uri', 'input_format', 'output_format', 'serde_info')
        LOCATION_URI_FIELD_NUMBER: _ClassVar[int]
        INPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
        SERDE_INFO_FIELD_NUMBER: _ClassVar[int]
        location_uri: str
        input_format: str
        output_format: str
        serde_info: HiveTableOptions.SerDeInfo

        def __init__(self, location_uri: _Optional[str]=..., input_format: _Optional[str]=..., output_format: _Optional[str]=..., serde_info: _Optional[_Union[HiveTableOptions.SerDeInfo, _Mapping]]=...) -> None:
            ...

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.ScalarMap[str, str]
    table_type: str
    storage_descriptor: HiveTableOptions.StorageDescriptor

    def __init__(self, parameters: _Optional[_Mapping[str, str]]=..., table_type: _Optional[str]=..., storage_descriptor: _Optional[_Union[HiveTableOptions.StorageDescriptor, _Mapping]]=...) -> None:
        ...