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

class Task(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'display_name', 'state', 'labels', 'trigger_spec', 'execution_spec', 'execution_status', 'spark', 'notebook')

    class InfrastructureSpec(_message.Message):
        __slots__ = ('batch', 'container_image', 'vpc_network')

        class BatchComputeResources(_message.Message):
            __slots__ = ('executors_count', 'max_executors_count')
            EXECUTORS_COUNT_FIELD_NUMBER: _ClassVar[int]
            MAX_EXECUTORS_COUNT_FIELD_NUMBER: _ClassVar[int]
            executors_count: int
            max_executors_count: int

            def __init__(self, executors_count: _Optional[int]=..., max_executors_count: _Optional[int]=...) -> None:
                ...

        class ContainerImageRuntime(_message.Message):
            __slots__ = ('image', 'java_jars', 'python_packages', 'properties')

            class PropertiesEntry(_message.Message):
                __slots__ = ('key', 'value')
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str

                def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                    ...
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            JAVA_JARS_FIELD_NUMBER: _ClassVar[int]
            PYTHON_PACKAGES_FIELD_NUMBER: _ClassVar[int]
            PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            image: str
            java_jars: _containers.RepeatedScalarFieldContainer[str]
            python_packages: _containers.RepeatedScalarFieldContainer[str]
            properties: _containers.ScalarMap[str, str]

            def __init__(self, image: _Optional[str]=..., java_jars: _Optional[_Iterable[str]]=..., python_packages: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, str]]=...) -> None:
                ...

        class VpcNetwork(_message.Message):
            __slots__ = ('network', 'sub_network', 'network_tags')
            NETWORK_FIELD_NUMBER: _ClassVar[int]
            SUB_NETWORK_FIELD_NUMBER: _ClassVar[int]
            NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
            network: str
            sub_network: str
            network_tags: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, network: _Optional[str]=..., sub_network: _Optional[str]=..., network_tags: _Optional[_Iterable[str]]=...) -> None:
                ...
        BATCH_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
        VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
        batch: Task.InfrastructureSpec.BatchComputeResources
        container_image: Task.InfrastructureSpec.ContainerImageRuntime
        vpc_network: Task.InfrastructureSpec.VpcNetwork

        def __init__(self, batch: _Optional[_Union[Task.InfrastructureSpec.BatchComputeResources, _Mapping]]=..., container_image: _Optional[_Union[Task.InfrastructureSpec.ContainerImageRuntime, _Mapping]]=..., vpc_network: _Optional[_Union[Task.InfrastructureSpec.VpcNetwork, _Mapping]]=...) -> None:
            ...

    class TriggerSpec(_message.Message):
        __slots__ = ('type', 'start_time', 'disabled', 'max_retries', 'schedule')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[Task.TriggerSpec.Type]
            ON_DEMAND: _ClassVar[Task.TriggerSpec.Type]
            RECURRING: _ClassVar[Task.TriggerSpec.Type]
        TYPE_UNSPECIFIED: Task.TriggerSpec.Type
        ON_DEMAND: Task.TriggerSpec.Type
        RECURRING: Task.TriggerSpec.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        type: Task.TriggerSpec.Type
        start_time: _timestamp_pb2.Timestamp
        disabled: bool
        max_retries: int
        schedule: str

        def __init__(self, type: _Optional[_Union[Task.TriggerSpec.Type, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., disabled: bool=..., max_retries: _Optional[int]=..., schedule: _Optional[str]=...) -> None:
            ...

    class ExecutionSpec(_message.Message):
        __slots__ = ('args', 'service_account', 'project', 'max_job_execution_lifetime', 'kms_key')

        class ArgsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        ARGS_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        MAX_JOB_EXECUTION_LIFETIME_FIELD_NUMBER: _ClassVar[int]
        KMS_KEY_FIELD_NUMBER: _ClassVar[int]
        args: _containers.ScalarMap[str, str]
        service_account: str
        project: str
        max_job_execution_lifetime: _duration_pb2.Duration
        kms_key: str

        def __init__(self, args: _Optional[_Mapping[str, str]]=..., service_account: _Optional[str]=..., project: _Optional[str]=..., max_job_execution_lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., kms_key: _Optional[str]=...) -> None:
            ...

    class SparkTaskConfig(_message.Message):
        __slots__ = ('main_jar_file_uri', 'main_class', 'python_script_file', 'sql_script_file', 'sql_script', 'file_uris', 'archive_uris', 'infrastructure_spec')
        MAIN_JAR_FILE_URI_FIELD_NUMBER: _ClassVar[int]
        MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
        PYTHON_SCRIPT_FILE_FIELD_NUMBER: _ClassVar[int]
        SQL_SCRIPT_FILE_FIELD_NUMBER: _ClassVar[int]
        SQL_SCRIPT_FIELD_NUMBER: _ClassVar[int]
        FILE_URIS_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
        INFRASTRUCTURE_SPEC_FIELD_NUMBER: _ClassVar[int]
        main_jar_file_uri: str
        main_class: str
        python_script_file: str
        sql_script_file: str
        sql_script: str
        file_uris: _containers.RepeatedScalarFieldContainer[str]
        archive_uris: _containers.RepeatedScalarFieldContainer[str]
        infrastructure_spec: Task.InfrastructureSpec

        def __init__(self, main_jar_file_uri: _Optional[str]=..., main_class: _Optional[str]=..., python_script_file: _Optional[str]=..., sql_script_file: _Optional[str]=..., sql_script: _Optional[str]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=..., infrastructure_spec: _Optional[_Union[Task.InfrastructureSpec, _Mapping]]=...) -> None:
            ...

    class NotebookTaskConfig(_message.Message):
        __slots__ = ('notebook', 'infrastructure_spec', 'file_uris', 'archive_uris')
        NOTEBOOK_FIELD_NUMBER: _ClassVar[int]
        INFRASTRUCTURE_SPEC_FIELD_NUMBER: _ClassVar[int]
        FILE_URIS_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
        notebook: str
        infrastructure_spec: Task.InfrastructureSpec
        file_uris: _containers.RepeatedScalarFieldContainer[str]
        archive_uris: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, notebook: _Optional[str]=..., infrastructure_spec: _Optional[_Union[Task.InfrastructureSpec, _Mapping]]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=...) -> None:
            ...

    class ExecutionStatus(_message.Message):
        __slots__ = ('update_time', 'latest_job')
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        LATEST_JOB_FIELD_NUMBER: _ClassVar[int]
        update_time: _timestamp_pb2.Timestamp
        latest_job: Job

        def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., latest_job: _Optional[_Union[Job, _Mapping]]=...) -> None:
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
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_SPEC_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    SPARK_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    display_name: str
    state: _resources_pb2.State
    labels: _containers.ScalarMap[str, str]
    trigger_spec: Task.TriggerSpec
    execution_spec: Task.ExecutionSpec
    execution_status: Task.ExecutionStatus
    spark: Task.SparkTaskConfig
    notebook: Task.NotebookTaskConfig

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[_resources_pb2.State, str]]=..., labels: _Optional[_Mapping[str, str]]=..., trigger_spec: _Optional[_Union[Task.TriggerSpec, _Mapping]]=..., execution_spec: _Optional[_Union[Task.ExecutionSpec, _Mapping]]=..., execution_status: _Optional[_Union[Task.ExecutionStatus, _Mapping]]=..., spark: _Optional[_Union[Task.SparkTaskConfig, _Mapping]]=..., notebook: _Optional[_Union[Task.NotebookTaskConfig, _Mapping]]=...) -> None:
        ...

class Job(_message.Message):
    __slots__ = ('name', 'uid', 'start_time', 'end_time', 'state', 'retry_count', 'service', 'service_job', 'message', 'labels', 'trigger', 'execution_spec')

    class Service(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVICE_UNSPECIFIED: _ClassVar[Job.Service]
        DATAPROC: _ClassVar[Job.Service]
    SERVICE_UNSPECIFIED: Job.Service
    DATAPROC: Job.Service

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Job.State]
        RUNNING: _ClassVar[Job.State]
        CANCELLING: _ClassVar[Job.State]
        CANCELLED: _ClassVar[Job.State]
        SUCCEEDED: _ClassVar[Job.State]
        FAILED: _ClassVar[Job.State]
        ABORTED: _ClassVar[Job.State]
    STATE_UNSPECIFIED: Job.State
    RUNNING: Job.State
    CANCELLING: Job.State
    CANCELLED: Job.State
    SUCCEEDED: Job.State
    FAILED: Job.State
    ABORTED: Job.State

    class Trigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRIGGER_UNSPECIFIED: _ClassVar[Job.Trigger]
        TASK_CONFIG: _ClassVar[Job.Trigger]
        RUN_REQUEST: _ClassVar[Job.Trigger]
    TRIGGER_UNSPECIFIED: Job.Trigger
    TASK_CONFIG: Job.Trigger
    RUN_REQUEST: Job.Trigger

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
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_JOB_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: Job.State
    retry_count: int
    service: Job.Service
    service_job: str
    message: str
    labels: _containers.ScalarMap[str, str]
    trigger: Job.Trigger
    execution_spec: Task.ExecutionSpec

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Job.State, str]]=..., retry_count: _Optional[int]=..., service: _Optional[_Union[Job.Service, str]]=..., service_job: _Optional[str]=..., message: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., trigger: _Optional[_Union[Job.Trigger, str]]=..., execution_spec: _Optional[_Union[Task.ExecutionSpec, _Mapping]]=...) -> None:
        ...