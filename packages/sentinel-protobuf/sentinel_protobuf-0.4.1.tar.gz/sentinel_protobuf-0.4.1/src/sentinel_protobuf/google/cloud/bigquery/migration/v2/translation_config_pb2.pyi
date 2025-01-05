from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TranslationConfigDetails(_message.Message):
    __slots__ = ('gcs_source_path', 'gcs_target_path', 'name_mapping_list', 'source_dialect', 'target_dialect', 'source_env', 'request_source', 'target_types')
    GCS_SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    GCS_TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_MAPPING_LIST_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DIALECT_FIELD_NUMBER: _ClassVar[int]
    TARGET_DIALECT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENV_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    gcs_source_path: str
    gcs_target_path: str
    name_mapping_list: ObjectNameMappingList
    source_dialect: Dialect
    target_dialect: Dialect
    source_env: SourceEnv
    request_source: str
    target_types: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, gcs_source_path: _Optional[str]=..., gcs_target_path: _Optional[str]=..., name_mapping_list: _Optional[_Union[ObjectNameMappingList, _Mapping]]=..., source_dialect: _Optional[_Union[Dialect, _Mapping]]=..., target_dialect: _Optional[_Union[Dialect, _Mapping]]=..., source_env: _Optional[_Union[SourceEnv, _Mapping]]=..., request_source: _Optional[str]=..., target_types: _Optional[_Iterable[str]]=...) -> None:
        ...

class Dialect(_message.Message):
    __slots__ = ('bigquery_dialect', 'hiveql_dialect', 'redshift_dialect', 'teradata_dialect', 'oracle_dialect', 'sparksql_dialect', 'snowflake_dialect', 'netezza_dialect', 'azure_synapse_dialect', 'vertica_dialect', 'sql_server_dialect', 'postgresql_dialect', 'presto_dialect', 'mysql_dialect', 'db2_dialect', 'sqlite_dialect', 'greenplum_dialect')
    BIGQUERY_DIALECT_FIELD_NUMBER: _ClassVar[int]
    HIVEQL_DIALECT_FIELD_NUMBER: _ClassVar[int]
    REDSHIFT_DIALECT_FIELD_NUMBER: _ClassVar[int]
    TERADATA_DIALECT_FIELD_NUMBER: _ClassVar[int]
    ORACLE_DIALECT_FIELD_NUMBER: _ClassVar[int]
    SPARKSQL_DIALECT_FIELD_NUMBER: _ClassVar[int]
    SNOWFLAKE_DIALECT_FIELD_NUMBER: _ClassVar[int]
    NETEZZA_DIALECT_FIELD_NUMBER: _ClassVar[int]
    AZURE_SYNAPSE_DIALECT_FIELD_NUMBER: _ClassVar[int]
    VERTICA_DIALECT_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_DIALECT_FIELD_NUMBER: _ClassVar[int]
    POSTGRESQL_DIALECT_FIELD_NUMBER: _ClassVar[int]
    PRESTO_DIALECT_FIELD_NUMBER: _ClassVar[int]
    MYSQL_DIALECT_FIELD_NUMBER: _ClassVar[int]
    DB2_DIALECT_FIELD_NUMBER: _ClassVar[int]
    SQLITE_DIALECT_FIELD_NUMBER: _ClassVar[int]
    GREENPLUM_DIALECT_FIELD_NUMBER: _ClassVar[int]
    bigquery_dialect: BigQueryDialect
    hiveql_dialect: HiveQLDialect
    redshift_dialect: RedshiftDialect
    teradata_dialect: TeradataDialect
    oracle_dialect: OracleDialect
    sparksql_dialect: SparkSQLDialect
    snowflake_dialect: SnowflakeDialect
    netezza_dialect: NetezzaDialect
    azure_synapse_dialect: AzureSynapseDialect
    vertica_dialect: VerticaDialect
    sql_server_dialect: SQLServerDialect
    postgresql_dialect: PostgresqlDialect
    presto_dialect: PrestoDialect
    mysql_dialect: MySQLDialect
    db2_dialect: DB2Dialect
    sqlite_dialect: SQLiteDialect
    greenplum_dialect: GreenplumDialect

    def __init__(self, bigquery_dialect: _Optional[_Union[BigQueryDialect, _Mapping]]=..., hiveql_dialect: _Optional[_Union[HiveQLDialect, _Mapping]]=..., redshift_dialect: _Optional[_Union[RedshiftDialect, _Mapping]]=..., teradata_dialect: _Optional[_Union[TeradataDialect, _Mapping]]=..., oracle_dialect: _Optional[_Union[OracleDialect, _Mapping]]=..., sparksql_dialect: _Optional[_Union[SparkSQLDialect, _Mapping]]=..., snowflake_dialect: _Optional[_Union[SnowflakeDialect, _Mapping]]=..., netezza_dialect: _Optional[_Union[NetezzaDialect, _Mapping]]=..., azure_synapse_dialect: _Optional[_Union[AzureSynapseDialect, _Mapping]]=..., vertica_dialect: _Optional[_Union[VerticaDialect, _Mapping]]=..., sql_server_dialect: _Optional[_Union[SQLServerDialect, _Mapping]]=..., postgresql_dialect: _Optional[_Union[PostgresqlDialect, _Mapping]]=..., presto_dialect: _Optional[_Union[PrestoDialect, _Mapping]]=..., mysql_dialect: _Optional[_Union[MySQLDialect, _Mapping]]=..., db2_dialect: _Optional[_Union[DB2Dialect, _Mapping]]=..., sqlite_dialect: _Optional[_Union[SQLiteDialect, _Mapping]]=..., greenplum_dialect: _Optional[_Union[GreenplumDialect, _Mapping]]=...) -> None:
        ...

class BigQueryDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class HiveQLDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RedshiftDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TeradataDialect(_message.Message):
    __slots__ = ('mode',)

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[TeradataDialect.Mode]
        SQL: _ClassVar[TeradataDialect.Mode]
        BTEQ: _ClassVar[TeradataDialect.Mode]
    MODE_UNSPECIFIED: TeradataDialect.Mode
    SQL: TeradataDialect.Mode
    BTEQ: TeradataDialect.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: TeradataDialect.Mode

    def __init__(self, mode: _Optional[_Union[TeradataDialect.Mode, str]]=...) -> None:
        ...

class OracleDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SparkSQLDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SnowflakeDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class NetezzaDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AzureSynapseDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class VerticaDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SQLServerDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PostgresqlDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PrestoDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MySQLDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DB2Dialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SQLiteDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GreenplumDialect(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ObjectNameMappingList(_message.Message):
    __slots__ = ('name_map',)
    NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    name_map: _containers.RepeatedCompositeFieldContainer[ObjectNameMapping]

    def __init__(self, name_map: _Optional[_Iterable[_Union[ObjectNameMapping, _Mapping]]]=...) -> None:
        ...

class ObjectNameMapping(_message.Message):
    __slots__ = ('source', 'target')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    source: NameMappingKey
    target: NameMappingValue

    def __init__(self, source: _Optional[_Union[NameMappingKey, _Mapping]]=..., target: _Optional[_Union[NameMappingValue, _Mapping]]=...) -> None:
        ...

class NameMappingKey(_message.Message):
    __slots__ = ('type', 'database', 'schema', 'relation', 'attribute')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[NameMappingKey.Type]
        DATABASE: _ClassVar[NameMappingKey.Type]
        SCHEMA: _ClassVar[NameMappingKey.Type]
        RELATION: _ClassVar[NameMappingKey.Type]
        ATTRIBUTE: _ClassVar[NameMappingKey.Type]
        RELATION_ALIAS: _ClassVar[NameMappingKey.Type]
        ATTRIBUTE_ALIAS: _ClassVar[NameMappingKey.Type]
        FUNCTION: _ClassVar[NameMappingKey.Type]
    TYPE_UNSPECIFIED: NameMappingKey.Type
    DATABASE: NameMappingKey.Type
    SCHEMA: NameMappingKey.Type
    RELATION: NameMappingKey.Type
    ATTRIBUTE: NameMappingKey.Type
    RELATION_ALIAS: NameMappingKey.Type
    ATTRIBUTE_ALIAS: NameMappingKey.Type
    FUNCTION: NameMappingKey.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    type: NameMappingKey.Type
    database: str
    schema: str
    relation: str
    attribute: str

    def __init__(self, type: _Optional[_Union[NameMappingKey.Type, str]]=..., database: _Optional[str]=..., schema: _Optional[str]=..., relation: _Optional[str]=..., attribute: _Optional[str]=...) -> None:
        ...

class NameMappingValue(_message.Message):
    __slots__ = ('database', 'schema', 'relation', 'attribute')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    database: str
    schema: str
    relation: str
    attribute: str

    def __init__(self, database: _Optional[str]=..., schema: _Optional[str]=..., relation: _Optional[str]=..., attribute: _Optional[str]=...) -> None:
        ...

class SourceEnv(_message.Message):
    __slots__ = ('default_database', 'schema_search_path', 'metadata_store_dataset')
    DEFAULT_DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_SEARCH_PATH_FIELD_NUMBER: _ClassVar[int]
    METADATA_STORE_DATASET_FIELD_NUMBER: _ClassVar[int]
    default_database: str
    schema_search_path: _containers.RepeatedScalarFieldContainer[str]
    metadata_store_dataset: str

    def __init__(self, default_database: _Optional[str]=..., schema_search_path: _Optional[_Iterable[str]]=..., metadata_store_dataset: _Optional[str]=...) -> None:
        ...