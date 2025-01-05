from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import job_state_pb2 as _job_state_pb2
from google.cloud.aiplatform.v1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1 import network_spec_pb2 as _network_spec_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NotebookExecutionJob(_message.Message):
    __slots__ = ('dataform_repository_source', 'gcs_notebook_source', 'direct_notebook_source', 'notebook_runtime_template_resource_name', 'custom_environment_spec', 'gcs_output_uri', 'execution_user', 'service_account', 'workbench_runtime', 'name', 'display_name', 'execution_timeout', 'schedule_resource_name', 'job_state', 'status', 'create_time', 'update_time', 'labels', 'kernel_name', 'encryption_spec')

    class DataformRepositorySource(_message.Message):
        __slots__ = ('dataform_repository_resource_name', 'commit_sha')
        DATAFORM_REPOSITORY_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
        dataform_repository_resource_name: str
        commit_sha: str

        def __init__(self, dataform_repository_resource_name: _Optional[str]=..., commit_sha: _Optional[str]=...) -> None:
            ...

    class GcsNotebookSource(_message.Message):
        __slots__ = ('uri', 'generation')
        URI_FIELD_NUMBER: _ClassVar[int]
        GENERATION_FIELD_NUMBER: _ClassVar[int]
        uri: str
        generation: str

        def __init__(self, uri: _Optional[str]=..., generation: _Optional[str]=...) -> None:
            ...

    class DirectNotebookSource(_message.Message):
        __slots__ = ('content',)
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        content: bytes

        def __init__(self, content: _Optional[bytes]=...) -> None:
            ...

    class CustomEnvironmentSpec(_message.Message):
        __slots__ = ('machine_spec', 'persistent_disk_spec', 'network_spec')
        MACHINE_SPEC_FIELD_NUMBER: _ClassVar[int]
        PERSISTENT_DISK_SPEC_FIELD_NUMBER: _ClassVar[int]
        NETWORK_SPEC_FIELD_NUMBER: _ClassVar[int]
        machine_spec: _machine_resources_pb2.MachineSpec
        persistent_disk_spec: _machine_resources_pb2.PersistentDiskSpec
        network_spec: _network_spec_pb2.NetworkSpec

        def __init__(self, machine_spec: _Optional[_Union[_machine_resources_pb2.MachineSpec, _Mapping]]=..., persistent_disk_spec: _Optional[_Union[_machine_resources_pb2.PersistentDiskSpec, _Mapping]]=..., network_spec: _Optional[_Union[_network_spec_pb2.NetworkSpec, _Mapping]]=...) -> None:
            ...

    class WorkbenchRuntime(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DATAFORM_REPOSITORY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_NOTEBOOK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIRECT_NOTEBOOK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_TEMPLATE_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ENVIRONMENT_SPEC_FIELD_NUMBER: _ClassVar[int]
    GCS_OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_USER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    WORKBENCH_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    KERNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    dataform_repository_source: NotebookExecutionJob.DataformRepositorySource
    gcs_notebook_source: NotebookExecutionJob.GcsNotebookSource
    direct_notebook_source: NotebookExecutionJob.DirectNotebookSource
    notebook_runtime_template_resource_name: str
    custom_environment_spec: NotebookExecutionJob.CustomEnvironmentSpec
    gcs_output_uri: str
    execution_user: str
    service_account: str
    workbench_runtime: NotebookExecutionJob.WorkbenchRuntime
    name: str
    display_name: str
    execution_timeout: _duration_pb2.Duration
    schedule_resource_name: str
    job_state: _job_state_pb2.JobState
    status: _status_pb2.Status
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    kernel_name: str
    encryption_spec: _encryption_spec_pb2.EncryptionSpec

    def __init__(self, dataform_repository_source: _Optional[_Union[NotebookExecutionJob.DataformRepositorySource, _Mapping]]=..., gcs_notebook_source: _Optional[_Union[NotebookExecutionJob.GcsNotebookSource, _Mapping]]=..., direct_notebook_source: _Optional[_Union[NotebookExecutionJob.DirectNotebookSource, _Mapping]]=..., notebook_runtime_template_resource_name: _Optional[str]=..., custom_environment_spec: _Optional[_Union[NotebookExecutionJob.CustomEnvironmentSpec, _Mapping]]=..., gcs_output_uri: _Optional[str]=..., execution_user: _Optional[str]=..., service_account: _Optional[str]=..., workbench_runtime: _Optional[_Union[NotebookExecutionJob.WorkbenchRuntime, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., execution_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., schedule_resource_name: _Optional[str]=..., job_state: _Optional[_Union[_job_state_pb2.JobState, str]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., kernel_name: _Optional[str]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=...) -> None:
        ...