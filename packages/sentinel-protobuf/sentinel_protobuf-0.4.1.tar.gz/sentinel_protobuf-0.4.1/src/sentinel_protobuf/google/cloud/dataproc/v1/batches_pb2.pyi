from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataproc.v1 import shared_pb2 as _shared_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateBatchRequest(_message.Message):
    __slots__ = ('parent', 'batch', 'batch_id', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    batch: Batch
    batch_id: str
    request_id: str

    def __init__(self, parent: _Optional[str]=..., batch: _Optional[_Union[Batch, _Mapping]]=..., batch_id: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetBatchRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBatchesRequest(_message.Message):
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

class ListBatchesResponse(_message.Message):
    __slots__ = ('batches', 'next_page_token', 'unreachable')
    BATCHES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    batches: _containers.RepeatedCompositeFieldContainer[Batch]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, batches: _Optional[_Iterable[_Union[Batch, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteBatchRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Batch(_message.Message):
    __slots__ = ('name', 'uuid', 'create_time', 'pyspark_batch', 'spark_batch', 'spark_r_batch', 'spark_sql_batch', 'runtime_info', 'state', 'state_message', 'state_time', 'creator', 'labels', 'runtime_config', 'environment_config', 'operation', 'state_history')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Batch.State]
        PENDING: _ClassVar[Batch.State]
        RUNNING: _ClassVar[Batch.State]
        CANCELLING: _ClassVar[Batch.State]
        CANCELLED: _ClassVar[Batch.State]
        SUCCEEDED: _ClassVar[Batch.State]
        FAILED: _ClassVar[Batch.State]
    STATE_UNSPECIFIED: Batch.State
    PENDING: Batch.State
    RUNNING: Batch.State
    CANCELLING: Batch.State
    CANCELLED: Batch.State
    SUCCEEDED: Batch.State
    FAILED: Batch.State

    class StateHistory(_message.Message):
        __slots__ = ('state', 'state_message', 'state_start_time')
        STATE_FIELD_NUMBER: _ClassVar[int]
        STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
        state: Batch.State
        state_message: str
        state_start_time: _timestamp_pb2.Timestamp

        def __init__(self, state: _Optional[_Union[Batch.State, str]]=..., state_message: _Optional[str]=..., state_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
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
    UUID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PYSPARK_BATCH_FIELD_NUMBER: _ClassVar[int]
    SPARK_BATCH_FIELD_NUMBER: _ClassVar[int]
    SPARK_R_BATCH_FIELD_NUMBER: _ClassVar[int]
    SPARK_SQL_BATCH_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    STATE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    name: str
    uuid: str
    create_time: _timestamp_pb2.Timestamp
    pyspark_batch: PySparkBatch
    spark_batch: SparkBatch
    spark_r_batch: SparkRBatch
    spark_sql_batch: SparkSqlBatch
    runtime_info: _shared_pb2.RuntimeInfo
    state: Batch.State
    state_message: str
    state_time: _timestamp_pb2.Timestamp
    creator: str
    labels: _containers.ScalarMap[str, str]
    runtime_config: _shared_pb2.RuntimeConfig
    environment_config: _shared_pb2.EnvironmentConfig
    operation: str
    state_history: _containers.RepeatedCompositeFieldContainer[Batch.StateHistory]

    def __init__(self, name: _Optional[str]=..., uuid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., pyspark_batch: _Optional[_Union[PySparkBatch, _Mapping]]=..., spark_batch: _Optional[_Union[SparkBatch, _Mapping]]=..., spark_r_batch: _Optional[_Union[SparkRBatch, _Mapping]]=..., spark_sql_batch: _Optional[_Union[SparkSqlBatch, _Mapping]]=..., runtime_info: _Optional[_Union[_shared_pb2.RuntimeInfo, _Mapping]]=..., state: _Optional[_Union[Batch.State, str]]=..., state_message: _Optional[str]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., creator: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., runtime_config: _Optional[_Union[_shared_pb2.RuntimeConfig, _Mapping]]=..., environment_config: _Optional[_Union[_shared_pb2.EnvironmentConfig, _Mapping]]=..., operation: _Optional[str]=..., state_history: _Optional[_Iterable[_Union[Batch.StateHistory, _Mapping]]]=...) -> None:
        ...

class PySparkBatch(_message.Message):
    __slots__ = ('main_python_file_uri', 'args', 'python_file_uris', 'jar_file_uris', 'file_uris', 'archive_uris')
    MAIN_PYTHON_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    PYTHON_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
    main_python_file_uri: str
    args: _containers.RepeatedScalarFieldContainer[str]
    python_file_uris: _containers.RepeatedScalarFieldContainer[str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]
    file_uris: _containers.RepeatedScalarFieldContainer[str]
    archive_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, main_python_file_uri: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., python_file_uris: _Optional[_Iterable[str]]=..., jar_file_uris: _Optional[_Iterable[str]]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class SparkBatch(_message.Message):
    __slots__ = ('main_jar_file_uri', 'main_class', 'args', 'jar_file_uris', 'file_uris', 'archive_uris')
    MAIN_JAR_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
    main_jar_file_uri: str
    main_class: str
    args: _containers.RepeatedScalarFieldContainer[str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]
    file_uris: _containers.RepeatedScalarFieldContainer[str]
    archive_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, main_jar_file_uri: _Optional[str]=..., main_class: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., jar_file_uris: _Optional[_Iterable[str]]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class SparkRBatch(_message.Message):
    __slots__ = ('main_r_file_uri', 'args', 'file_uris', 'archive_uris')
    MAIN_R_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
    main_r_file_uri: str
    args: _containers.RepeatedScalarFieldContainer[str]
    file_uris: _containers.RepeatedScalarFieldContainer[str]
    archive_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, main_r_file_uri: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class SparkSqlBatch(_message.Message):
    __slots__ = ('query_file_uri', 'query_variables', 'jar_file_uris')

    class QueryVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    QUERY_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    query_file_uri: str
    query_variables: _containers.ScalarMap[str, str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, query_file_uri: _Optional[str]=..., query_variables: _Optional[_Mapping[str, str]]=..., jar_file_uris: _Optional[_Iterable[str]]=...) -> None:
        ...