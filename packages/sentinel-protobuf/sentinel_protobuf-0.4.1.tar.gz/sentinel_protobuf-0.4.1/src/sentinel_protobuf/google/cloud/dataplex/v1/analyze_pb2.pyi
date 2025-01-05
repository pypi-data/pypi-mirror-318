from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataplex.v1 import resources_pb2 as _resources_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Environment(_message.Message):
    __slots__ = ('name', 'display_name', 'uid', 'create_time', 'update_time', 'labels', 'description', 'state', 'infrastructure_spec', 'session_spec', 'session_status', 'endpoints')

    class InfrastructureSpec(_message.Message):
        __slots__ = ('compute', 'os_image')

        class ComputeResources(_message.Message):
            __slots__ = ('disk_size_gb', 'node_count', 'max_node_count')
            DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
            NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
            MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
            disk_size_gb: int
            node_count: int
            max_node_count: int

            def __init__(self, disk_size_gb: _Optional[int]=..., node_count: _Optional[int]=..., max_node_count: _Optional[int]=...) -> None:
                ...

        class OsImageRuntime(_message.Message):
            __slots__ = ('image_version', 'java_libraries', 'python_packages', 'properties')

            class PropertiesEntry(_message.Message):
                __slots__ = ('key', 'value')
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str

                def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                    ...
            IMAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
            JAVA_LIBRARIES_FIELD_NUMBER: _ClassVar[int]
            PYTHON_PACKAGES_FIELD_NUMBER: _ClassVar[int]
            PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            image_version: str
            java_libraries: _containers.RepeatedScalarFieldContainer[str]
            python_packages: _containers.RepeatedScalarFieldContainer[str]
            properties: _containers.ScalarMap[str, str]

            def __init__(self, image_version: _Optional[str]=..., java_libraries: _Optional[_Iterable[str]]=..., python_packages: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, str]]=...) -> None:
                ...
        COMPUTE_FIELD_NUMBER: _ClassVar[int]
        OS_IMAGE_FIELD_NUMBER: _ClassVar[int]
        compute: Environment.InfrastructureSpec.ComputeResources
        os_image: Environment.InfrastructureSpec.OsImageRuntime

        def __init__(self, compute: _Optional[_Union[Environment.InfrastructureSpec.ComputeResources, _Mapping]]=..., os_image: _Optional[_Union[Environment.InfrastructureSpec.OsImageRuntime, _Mapping]]=...) -> None:
            ...

    class SessionSpec(_message.Message):
        __slots__ = ('max_idle_duration', 'enable_fast_startup')
        MAX_IDLE_DURATION_FIELD_NUMBER: _ClassVar[int]
        ENABLE_FAST_STARTUP_FIELD_NUMBER: _ClassVar[int]
        max_idle_duration: _duration_pb2.Duration
        enable_fast_startup: bool

        def __init__(self, max_idle_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., enable_fast_startup: bool=...) -> None:
            ...

    class SessionStatus(_message.Message):
        __slots__ = ('active',)
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        active: bool

        def __init__(self, active: bool=...) -> None:
            ...

    class Endpoints(_message.Message):
        __slots__ = ('notebooks', 'sql')
        NOTEBOOKS_FIELD_NUMBER: _ClassVar[int]
        SQL_FIELD_NUMBER: _ClassVar[int]
        notebooks: str
        sql: str

        def __init__(self, notebooks: _Optional[str]=..., sql: _Optional[str]=...) -> None:
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
    INFRASTRUCTURE_SPEC_FIELD_NUMBER: _ClassVar[int]
    SESSION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SESSION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    state: _resources_pb2.State
    infrastructure_spec: Environment.InfrastructureSpec
    session_spec: Environment.SessionSpec
    session_status: Environment.SessionStatus
    endpoints: Environment.Endpoints

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., state: _Optional[_Union[_resources_pb2.State, str]]=..., infrastructure_spec: _Optional[_Union[Environment.InfrastructureSpec, _Mapping]]=..., session_spec: _Optional[_Union[Environment.SessionSpec, _Mapping]]=..., session_status: _Optional[_Union[Environment.SessionStatus, _Mapping]]=..., endpoints: _Optional[_Union[Environment.Endpoints, _Mapping]]=...) -> None:
        ...

class Content(_message.Message):
    __slots__ = ('name', 'uid', 'path', 'create_time', 'update_time', 'labels', 'description', 'data_text', 'sql_script', 'notebook')

    class SqlScript(_message.Message):
        __slots__ = ('engine',)

        class QueryEngine(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            QUERY_ENGINE_UNSPECIFIED: _ClassVar[Content.SqlScript.QueryEngine]
            SPARK: _ClassVar[Content.SqlScript.QueryEngine]
        QUERY_ENGINE_UNSPECIFIED: Content.SqlScript.QueryEngine
        SPARK: Content.SqlScript.QueryEngine
        ENGINE_FIELD_NUMBER: _ClassVar[int]
        engine: Content.SqlScript.QueryEngine

        def __init__(self, engine: _Optional[_Union[Content.SqlScript.QueryEngine, str]]=...) -> None:
            ...

    class Notebook(_message.Message):
        __slots__ = ('kernel_type',)

        class KernelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            KERNEL_TYPE_UNSPECIFIED: _ClassVar[Content.Notebook.KernelType]
            PYTHON3: _ClassVar[Content.Notebook.KernelType]
        KERNEL_TYPE_UNSPECIFIED: Content.Notebook.KernelType
        PYTHON3: Content.Notebook.KernelType
        KERNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
        kernel_type: Content.Notebook.KernelType

        def __init__(self, kernel_type: _Optional[_Union[Content.Notebook.KernelType, str]]=...) -> None:
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
    UID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATA_TEXT_FIELD_NUMBER: _ClassVar[int]
    SQL_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    path: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    data_text: str
    sql_script: Content.SqlScript
    notebook: Content.Notebook

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., path: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., data_text: _Optional[str]=..., sql_script: _Optional[_Union[Content.SqlScript, _Mapping]]=..., notebook: _Optional[_Union[Content.Notebook, _Mapping]]=...) -> None:
        ...

class Session(_message.Message):
    __slots__ = ('name', 'user_id', 'create_time', 'state')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_id: str
    create_time: _timestamp_pb2.Timestamp
    state: _resources_pb2.State

    def __init__(self, name: _Optional[str]=..., user_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[_resources_pb2.State, str]]=...) -> None:
        ...