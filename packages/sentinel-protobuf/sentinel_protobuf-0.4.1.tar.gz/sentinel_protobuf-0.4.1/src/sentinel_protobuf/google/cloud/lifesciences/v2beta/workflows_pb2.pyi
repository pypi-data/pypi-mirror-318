from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RunPipelineRequest(_message.Message):
    __slots__ = ('parent', 'pipeline', 'labels', 'pub_sub_topic')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PUB_SUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    pipeline: Pipeline
    labels: _containers.ScalarMap[str, str]
    pub_sub_topic: str

    def __init__(self, parent: _Optional[str]=..., pipeline: _Optional[_Union[Pipeline, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., pub_sub_topic: _Optional[str]=...) -> None:
        ...

class RunPipelineResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Pipeline(_message.Message):
    __slots__ = ('actions', 'resources', 'environment', 'encrypted_environment', 'timeout')

    class EnvironmentEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    resources: Resources
    environment: _containers.ScalarMap[str, str]
    encrypted_environment: Secret
    timeout: _duration_pb2.Duration

    def __init__(self, actions: _Optional[_Iterable[_Union[Action, _Mapping]]]=..., resources: _Optional[_Union[Resources, _Mapping]]=..., environment: _Optional[_Mapping[str, str]]=..., encrypted_environment: _Optional[_Union[Secret, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class Action(_message.Message):
    __slots__ = ('container_name', 'image_uri', 'commands', 'entrypoint', 'environment', 'encrypted_environment', 'pid_namespace', 'port_mappings', 'mounts', 'labels', 'credentials', 'timeout', 'ignore_exit_status', 'run_in_background', 'always_run', 'enable_fuse', 'publish_exposed_ports', 'disable_image_prefetch', 'disable_standard_error_capture', 'block_external_network')

    class EnvironmentEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class PortMappingsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int

        def __init__(self, key: _Optional[int]=..., value: _Optional[int]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    PID_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PORT_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    MOUNTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    IGNORE_EXIT_STATUS_FIELD_NUMBER: _ClassVar[int]
    RUN_IN_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_RUN_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FUSE_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_EXPOSED_PORTS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_IMAGE_PREFETCH_FIELD_NUMBER: _ClassVar[int]
    DISABLE_STANDARD_ERROR_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_EXTERNAL_NETWORK_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    image_uri: str
    commands: _containers.RepeatedScalarFieldContainer[str]
    entrypoint: str
    environment: _containers.ScalarMap[str, str]
    encrypted_environment: Secret
    pid_namespace: str
    port_mappings: _containers.ScalarMap[int, int]
    mounts: _containers.RepeatedCompositeFieldContainer[Mount]
    labels: _containers.ScalarMap[str, str]
    credentials: Secret
    timeout: _duration_pb2.Duration
    ignore_exit_status: bool
    run_in_background: bool
    always_run: bool
    enable_fuse: bool
    publish_exposed_ports: bool
    disable_image_prefetch: bool
    disable_standard_error_capture: bool
    block_external_network: bool

    def __init__(self, container_name: _Optional[str]=..., image_uri: _Optional[str]=..., commands: _Optional[_Iterable[str]]=..., entrypoint: _Optional[str]=..., environment: _Optional[_Mapping[str, str]]=..., encrypted_environment: _Optional[_Union[Secret, _Mapping]]=..., pid_namespace: _Optional[str]=..., port_mappings: _Optional[_Mapping[int, int]]=..., mounts: _Optional[_Iterable[_Union[Mount, _Mapping]]]=..., labels: _Optional[_Mapping[str, str]]=..., credentials: _Optional[_Union[Secret, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., ignore_exit_status: bool=..., run_in_background: bool=..., always_run: bool=..., enable_fuse: bool=..., publish_exposed_ports: bool=..., disable_image_prefetch: bool=..., disable_standard_error_capture: bool=..., block_external_network: bool=...) -> None:
        ...

class Secret(_message.Message):
    __slots__ = ('key_name', 'cipher_text')
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    CIPHER_TEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    cipher_text: str

    def __init__(self, key_name: _Optional[str]=..., cipher_text: _Optional[str]=...) -> None:
        ...

class Mount(_message.Message):
    __slots__ = ('disk', 'path', 'read_only')
    DISK_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    disk: str
    path: str
    read_only: bool

    def __init__(self, disk: _Optional[str]=..., path: _Optional[str]=..., read_only: bool=...) -> None:
        ...

class Resources(_message.Message):
    __slots__ = ('regions', 'zones', 'virtual_machine')
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    regions: _containers.RepeatedScalarFieldContainer[str]
    zones: _containers.RepeatedScalarFieldContainer[str]
    virtual_machine: VirtualMachine

    def __init__(self, regions: _Optional[_Iterable[str]]=..., zones: _Optional[_Iterable[str]]=..., virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]]=...) -> None:
        ...

class VirtualMachine(_message.Message):
    __slots__ = ('machine_type', 'preemptible', 'labels', 'disks', 'network', 'accelerators', 'service_account', 'boot_disk_size_gb', 'cpu_platform', 'boot_image', 'nvidia_driver_version', 'enable_stackdriver_monitoring', 'docker_cache_images', 'volumes', 'reservation')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREEMPTIBLE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ACCELERATORS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    BOOT_IMAGE_FIELD_NUMBER: _ClassVar[int]
    NVIDIA_DRIVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STACKDRIVER_MONITORING_FIELD_NUMBER: _ClassVar[int]
    DOCKER_CACHE_IMAGES_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    machine_type: str
    preemptible: bool
    labels: _containers.ScalarMap[str, str]
    disks: _containers.RepeatedCompositeFieldContainer[Disk]
    network: Network
    accelerators: _containers.RepeatedCompositeFieldContainer[Accelerator]
    service_account: ServiceAccount
    boot_disk_size_gb: int
    cpu_platform: str
    boot_image: str
    nvidia_driver_version: str
    enable_stackdriver_monitoring: bool
    docker_cache_images: _containers.RepeatedScalarFieldContainer[str]
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    reservation: str

    def __init__(self, machine_type: _Optional[str]=..., preemptible: bool=..., labels: _Optional[_Mapping[str, str]]=..., disks: _Optional[_Iterable[_Union[Disk, _Mapping]]]=..., network: _Optional[_Union[Network, _Mapping]]=..., accelerators: _Optional[_Iterable[_Union[Accelerator, _Mapping]]]=..., service_account: _Optional[_Union[ServiceAccount, _Mapping]]=..., boot_disk_size_gb: _Optional[int]=..., cpu_platform: _Optional[str]=..., boot_image: _Optional[str]=..., nvidia_driver_version: _Optional[str]=..., enable_stackdriver_monitoring: bool=..., docker_cache_images: _Optional[_Iterable[str]]=..., volumes: _Optional[_Iterable[_Union[Volume, _Mapping]]]=..., reservation: _Optional[str]=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('email', 'scopes')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    email: str
    scopes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, email: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
        ...

class Accelerator(_message.Message):
    __slots__ = ('type', 'count')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    type: str
    count: int

    def __init__(self, type: _Optional[str]=..., count: _Optional[int]=...) -> None:
        ...

class Network(_message.Message):
    __slots__ = ('network', 'use_private_address', 'subnetwork')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    USE_PRIVATE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str
    use_private_address: bool
    subnetwork: str

    def __init__(self, network: _Optional[str]=..., use_private_address: bool=..., subnetwork: _Optional[str]=...) -> None:
        ...

class Disk(_message.Message):
    __slots__ = ('name', 'size_gb', 'type', 'source_image')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    size_gb: int
    type: str
    source_image: str

    def __init__(self, name: _Optional[str]=..., size_gb: _Optional[int]=..., type: _Optional[str]=..., source_image: _Optional[str]=...) -> None:
        ...

class Volume(_message.Message):
    __slots__ = ('volume', 'persistent_disk', 'existing_disk', 'nfs_mount')
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_DISK_FIELD_NUMBER: _ClassVar[int]
    EXISTING_DISK_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_FIELD_NUMBER: _ClassVar[int]
    volume: str
    persistent_disk: PersistentDisk
    existing_disk: ExistingDisk
    nfs_mount: NFSMount

    def __init__(self, volume: _Optional[str]=..., persistent_disk: _Optional[_Union[PersistentDisk, _Mapping]]=..., existing_disk: _Optional[_Union[ExistingDisk, _Mapping]]=..., nfs_mount: _Optional[_Union[NFSMount, _Mapping]]=...) -> None:
        ...

class PersistentDisk(_message.Message):
    __slots__ = ('size_gb', 'type', 'source_image')
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    size_gb: int
    type: str
    source_image: str

    def __init__(self, size_gb: _Optional[int]=..., type: _Optional[str]=..., source_image: _Optional[str]=...) -> None:
        ...

class ExistingDisk(_message.Message):
    __slots__ = ('disk',)
    DISK_FIELD_NUMBER: _ClassVar[int]
    disk: str

    def __init__(self, disk: _Optional[str]=...) -> None:
        ...

class NFSMount(_message.Message):
    __slots__ = ('target',)
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: str

    def __init__(self, target: _Optional[str]=...) -> None:
        ...

class Metadata(_message.Message):
    __slots__ = ('pipeline', 'labels', 'events', 'create_time', 'start_time', 'end_time', 'pub_sub_topic')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PUB_SUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    pipeline: Pipeline
    labels: _containers.ScalarMap[str, str]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    pub_sub_topic: str

    def __init__(self, pipeline: _Optional[_Union[Pipeline, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., events: _Optional[_Iterable[_Union[Event, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., pub_sub_topic: _Optional[str]=...) -> None:
        ...

class Event(_message.Message):
    __slots__ = ('timestamp', 'description', 'delayed', 'worker_assigned', 'worker_released', 'pull_started', 'pull_stopped', 'container_started', 'container_stopped', 'container_killed', 'unexpected_exit_status', 'failed')
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DELAYED_FIELD_NUMBER: _ClassVar[int]
    WORKER_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    WORKER_RELEASED_FIELD_NUMBER: _ClassVar[int]
    PULL_STARTED_FIELD_NUMBER: _ClassVar[int]
    PULL_STOPPED_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_STARTED_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_STOPPED_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_KILLED_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_EXIT_STATUS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    description: str
    delayed: DelayedEvent
    worker_assigned: WorkerAssignedEvent
    worker_released: WorkerReleasedEvent
    pull_started: PullStartedEvent
    pull_stopped: PullStoppedEvent
    container_started: ContainerStartedEvent
    container_stopped: ContainerStoppedEvent
    container_killed: ContainerKilledEvent
    unexpected_exit_status: UnexpectedExitStatusEvent
    failed: FailedEvent

    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., delayed: _Optional[_Union[DelayedEvent, _Mapping]]=..., worker_assigned: _Optional[_Union[WorkerAssignedEvent, _Mapping]]=..., worker_released: _Optional[_Union[WorkerReleasedEvent, _Mapping]]=..., pull_started: _Optional[_Union[PullStartedEvent, _Mapping]]=..., pull_stopped: _Optional[_Union[PullStoppedEvent, _Mapping]]=..., container_started: _Optional[_Union[ContainerStartedEvent, _Mapping]]=..., container_stopped: _Optional[_Union[ContainerStoppedEvent, _Mapping]]=..., container_killed: _Optional[_Union[ContainerKilledEvent, _Mapping]]=..., unexpected_exit_status: _Optional[_Union[UnexpectedExitStatusEvent, _Mapping]]=..., failed: _Optional[_Union[FailedEvent, _Mapping]]=...) -> None:
        ...

class DelayedEvent(_message.Message):
    __slots__ = ('cause', 'metrics')
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    cause: str
    metrics: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, cause: _Optional[str]=..., metrics: _Optional[_Iterable[str]]=...) -> None:
        ...

class WorkerAssignedEvent(_message.Message):
    __slots__ = ('zone', 'instance', 'machine_type')
    ZONE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    zone: str
    instance: str
    machine_type: str

    def __init__(self, zone: _Optional[str]=..., instance: _Optional[str]=..., machine_type: _Optional[str]=...) -> None:
        ...

class WorkerReleasedEvent(_message.Message):
    __slots__ = ('zone', 'instance')
    ZONE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    zone: str
    instance: str

    def __init__(self, zone: _Optional[str]=..., instance: _Optional[str]=...) -> None:
        ...

class PullStartedEvent(_message.Message):
    __slots__ = ('image_uri',)
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    image_uri: str

    def __init__(self, image_uri: _Optional[str]=...) -> None:
        ...

class PullStoppedEvent(_message.Message):
    __slots__ = ('image_uri',)
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    image_uri: str

    def __init__(self, image_uri: _Optional[str]=...) -> None:
        ...

class ContainerStartedEvent(_message.Message):
    __slots__ = ('action_id', 'port_mappings', 'ip_address')

    class PortMappingsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int

        def __init__(self, key: _Optional[int]=..., value: _Optional[int]=...) -> None:
            ...
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PORT_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    action_id: int
    port_mappings: _containers.ScalarMap[int, int]
    ip_address: str

    def __init__(self, action_id: _Optional[int]=..., port_mappings: _Optional[_Mapping[int, int]]=..., ip_address: _Optional[str]=...) -> None:
        ...

class ContainerStoppedEvent(_message.Message):
    __slots__ = ('action_id', 'exit_status', 'stderr')
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXIT_STATUS_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    action_id: int
    exit_status: int
    stderr: str

    def __init__(self, action_id: _Optional[int]=..., exit_status: _Optional[int]=..., stderr: _Optional[str]=...) -> None:
        ...

class UnexpectedExitStatusEvent(_message.Message):
    __slots__ = ('action_id', 'exit_status')
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXIT_STATUS_FIELD_NUMBER: _ClassVar[int]
    action_id: int
    exit_status: int

    def __init__(self, action_id: _Optional[int]=..., exit_status: _Optional[int]=...) -> None:
        ...

class ContainerKilledEvent(_message.Message):
    __slots__ = ('action_id',)
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    action_id: int

    def __init__(self, action_id: _Optional[int]=...) -> None:
        ...

class FailedEvent(_message.Message):
    __slots__ = ('code', 'cause')
    CODE_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    code: _code_pb2.Code
    cause: str

    def __init__(self, code: _Optional[_Union[_code_pb2.Code, str]]=..., cause: _Optional[str]=...) -> None:
        ...