from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.batch.v1alpha import task_pb2 as _task_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ('name', 'uid', 'priority', 'task_groups', 'scheduling_policy', 'dependencies', 'allocation_policy', 'labels', 'status', 'notification', 'create_time', 'update_time', 'logs_policy', 'notifications')

    class SchedulingPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCHEDULING_POLICY_UNSPECIFIED: _ClassVar[Job.SchedulingPolicy]
        AS_SOON_AS_POSSIBLE: _ClassVar[Job.SchedulingPolicy]
    SCHEDULING_POLICY_UNSPECIFIED: Job.SchedulingPolicy
    AS_SOON_AS_POSSIBLE: Job.SchedulingPolicy

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
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TASK_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    ALLOCATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LOGS_POLICY_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    priority: int
    task_groups: _containers.RepeatedCompositeFieldContainer[TaskGroup]
    scheduling_policy: Job.SchedulingPolicy
    dependencies: _containers.RepeatedCompositeFieldContainer[JobDependency]
    allocation_policy: AllocationPolicy
    labels: _containers.ScalarMap[str, str]
    status: JobStatus
    notification: JobNotification
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    logs_policy: LogsPolicy
    notifications: _containers.RepeatedCompositeFieldContainer[JobNotification]

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., priority: _Optional[int]=..., task_groups: _Optional[_Iterable[_Union[TaskGroup, _Mapping]]]=..., scheduling_policy: _Optional[_Union[Job.SchedulingPolicy, str]]=..., dependencies: _Optional[_Iterable[_Union[JobDependency, _Mapping]]]=..., allocation_policy: _Optional[_Union[AllocationPolicy, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., status: _Optional[_Union[JobStatus, _Mapping]]=..., notification: _Optional[_Union[JobNotification, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., logs_policy: _Optional[_Union[LogsPolicy, _Mapping]]=..., notifications: _Optional[_Iterable[_Union[JobNotification, _Mapping]]]=...) -> None:
        ...

class LogsPolicy(_message.Message):
    __slots__ = ('destination', 'logs_path', 'cloud_logging_option')

    class Destination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DESTINATION_UNSPECIFIED: _ClassVar[LogsPolicy.Destination]
        CLOUD_LOGGING: _ClassVar[LogsPolicy.Destination]
        PATH: _ClassVar[LogsPolicy.Destination]
    DESTINATION_UNSPECIFIED: LogsPolicy.Destination
    CLOUD_LOGGING: LogsPolicy.Destination
    PATH: LogsPolicy.Destination

    class CloudLoggingOption(_message.Message):
        __slots__ = ('use_generic_task_monitored_resource',)
        USE_GENERIC_TASK_MONITORED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        use_generic_task_monitored_resource: bool

        def __init__(self, use_generic_task_monitored_resource: bool=...) -> None:
            ...
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    LOGS_PATH_FIELD_NUMBER: _ClassVar[int]
    CLOUD_LOGGING_OPTION_FIELD_NUMBER: _ClassVar[int]
    destination: LogsPolicy.Destination
    logs_path: str
    cloud_logging_option: LogsPolicy.CloudLoggingOption

    def __init__(self, destination: _Optional[_Union[LogsPolicy.Destination, str]]=..., logs_path: _Optional[str]=..., cloud_logging_option: _Optional[_Union[LogsPolicy.CloudLoggingOption, _Mapping]]=...) -> None:
        ...

class JobDependency(_message.Message):
    __slots__ = ('items',)

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[JobDependency.Type]
        SUCCEEDED: _ClassVar[JobDependency.Type]
        FAILED: _ClassVar[JobDependency.Type]
        FINISHED: _ClassVar[JobDependency.Type]
    TYPE_UNSPECIFIED: JobDependency.Type
    SUCCEEDED: JobDependency.Type
    FAILED: JobDependency.Type
    FINISHED: JobDependency.Type

    class ItemsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: JobDependency.Type

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[JobDependency.Type, str]]=...) -> None:
            ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.ScalarMap[str, JobDependency.Type]

    def __init__(self, items: _Optional[_Mapping[str, JobDependency.Type]]=...) -> None:
        ...

class JobStatus(_message.Message):
    __slots__ = ('state', 'status_events', 'task_groups', 'run_duration', 'resource_usage')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[JobStatus.State]
        QUEUED: _ClassVar[JobStatus.State]
        SCHEDULED: _ClassVar[JobStatus.State]
        RUNNING: _ClassVar[JobStatus.State]
        SUCCEEDED: _ClassVar[JobStatus.State]
        FAILED: _ClassVar[JobStatus.State]
        DELETION_IN_PROGRESS: _ClassVar[JobStatus.State]
        CANCELLATION_IN_PROGRESS: _ClassVar[JobStatus.State]
        CANCELLED: _ClassVar[JobStatus.State]
    STATE_UNSPECIFIED: JobStatus.State
    QUEUED: JobStatus.State
    SCHEDULED: JobStatus.State
    RUNNING: JobStatus.State
    SUCCEEDED: JobStatus.State
    FAILED: JobStatus.State
    DELETION_IN_PROGRESS: JobStatus.State
    CANCELLATION_IN_PROGRESS: JobStatus.State
    CANCELLED: JobStatus.State

    class InstanceStatus(_message.Message):
        __slots__ = ('machine_type', 'provisioning_model', 'task_pack', 'boot_disk')
        MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_MODEL_FIELD_NUMBER: _ClassVar[int]
        TASK_PACK_FIELD_NUMBER: _ClassVar[int]
        BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
        machine_type: str
        provisioning_model: AllocationPolicy.ProvisioningModel
        task_pack: int
        boot_disk: AllocationPolicy.Disk

        def __init__(self, machine_type: _Optional[str]=..., provisioning_model: _Optional[_Union[AllocationPolicy.ProvisioningModel, str]]=..., task_pack: _Optional[int]=..., boot_disk: _Optional[_Union[AllocationPolicy.Disk, _Mapping]]=...) -> None:
            ...

    class TaskGroupStatus(_message.Message):
        __slots__ = ('counts', 'instances')

        class CountsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int

            def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
                ...
        COUNTS_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_FIELD_NUMBER: _ClassVar[int]
        counts: _containers.ScalarMap[str, int]
        instances: _containers.RepeatedCompositeFieldContainer[JobStatus.InstanceStatus]

        def __init__(self, counts: _Optional[_Mapping[str, int]]=..., instances: _Optional[_Iterable[_Union[JobStatus.InstanceStatus, _Mapping]]]=...) -> None:
            ...

    class TaskGroupsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: JobStatus.TaskGroupStatus

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[JobStatus.TaskGroupStatus, _Mapping]]=...) -> None:
            ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_EVENTS_FIELD_NUMBER: _ClassVar[int]
    TASK_GROUPS_FIELD_NUMBER: _ClassVar[int]
    RUN_DURATION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    state: JobStatus.State
    status_events: _containers.RepeatedCompositeFieldContainer[_task_pb2.StatusEvent]
    task_groups: _containers.MessageMap[str, JobStatus.TaskGroupStatus]
    run_duration: _duration_pb2.Duration
    resource_usage: ResourceUsage

    def __init__(self, state: _Optional[_Union[JobStatus.State, str]]=..., status_events: _Optional[_Iterable[_Union[_task_pb2.StatusEvent, _Mapping]]]=..., task_groups: _Optional[_Mapping[str, JobStatus.TaskGroupStatus]]=..., run_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., resource_usage: _Optional[_Union[ResourceUsage, _Mapping]]=...) -> None:
        ...

class ResourceUsage(_message.Message):
    __slots__ = ('core_hours',)
    CORE_HOURS_FIELD_NUMBER: _ClassVar[int]
    core_hours: float

    def __init__(self, core_hours: _Optional[float]=...) -> None:
        ...

class JobNotification(_message.Message):
    __slots__ = ('pubsub_topic', 'message')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[JobNotification.Type]
        JOB_STATE_CHANGED: _ClassVar[JobNotification.Type]
        TASK_STATE_CHANGED: _ClassVar[JobNotification.Type]
    TYPE_UNSPECIFIED: JobNotification.Type
    JOB_STATE_CHANGED: JobNotification.Type
    TASK_STATE_CHANGED: JobNotification.Type

    class Message(_message.Message):
        __slots__ = ('type', 'new_job_state', 'new_task_state')
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NEW_JOB_STATE_FIELD_NUMBER: _ClassVar[int]
        NEW_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
        type: JobNotification.Type
        new_job_state: JobStatus.State
        new_task_state: _task_pb2.TaskStatus.State

        def __init__(self, type: _Optional[_Union[JobNotification.Type, str]]=..., new_job_state: _Optional[_Union[JobStatus.State, str]]=..., new_task_state: _Optional[_Union[_task_pb2.TaskStatus.State, str]]=...) -> None:
            ...
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    pubsub_topic: str
    message: JobNotification.Message

    def __init__(self, pubsub_topic: _Optional[str]=..., message: _Optional[_Union[JobNotification.Message, _Mapping]]=...) -> None:
        ...

class AllocationPolicy(_message.Message):
    __slots__ = ('location', 'instance', 'instances', 'instance_templates', 'provisioning_models', 'service_account_email', 'service_account', 'labels', 'network', 'placement', 'tags')

    class ProvisioningModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROVISIONING_MODEL_UNSPECIFIED: _ClassVar[AllocationPolicy.ProvisioningModel]
        STANDARD: _ClassVar[AllocationPolicy.ProvisioningModel]
        SPOT: _ClassVar[AllocationPolicy.ProvisioningModel]
        PREEMPTIBLE: _ClassVar[AllocationPolicy.ProvisioningModel]
    PROVISIONING_MODEL_UNSPECIFIED: AllocationPolicy.ProvisioningModel
    STANDARD: AllocationPolicy.ProvisioningModel
    SPOT: AllocationPolicy.ProvisioningModel
    PREEMPTIBLE: AllocationPolicy.ProvisioningModel

    class LocationPolicy(_message.Message):
        __slots__ = ('allowed_locations', 'denied_locations')
        ALLOWED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        DENIED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        allowed_locations: _containers.RepeatedScalarFieldContainer[str]
        denied_locations: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, allowed_locations: _Optional[_Iterable[str]]=..., denied_locations: _Optional[_Iterable[str]]=...) -> None:
            ...

    class Disk(_message.Message):
        __slots__ = ('image', 'snapshot', 'type', 'size_gb', 'disk_interface')
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        DISK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        image: str
        snapshot: str
        type: str
        size_gb: int
        disk_interface: str

        def __init__(self, image: _Optional[str]=..., snapshot: _Optional[str]=..., type: _Optional[str]=..., size_gb: _Optional[int]=..., disk_interface: _Optional[str]=...) -> None:
            ...

    class AttachedDisk(_message.Message):
        __slots__ = ('new_disk', 'existing_disk', 'device_name')
        NEW_DISK_FIELD_NUMBER: _ClassVar[int]
        EXISTING_DISK_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        new_disk: AllocationPolicy.Disk
        existing_disk: str
        device_name: str

        def __init__(self, new_disk: _Optional[_Union[AllocationPolicy.Disk, _Mapping]]=..., existing_disk: _Optional[str]=..., device_name: _Optional[str]=...) -> None:
            ...

    class Accelerator(_message.Message):
        __slots__ = ('type', 'count', 'install_gpu_drivers', 'driver_version')
        TYPE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        INSTALL_GPU_DRIVERS_FIELD_NUMBER: _ClassVar[int]
        DRIVER_VERSION_FIELD_NUMBER: _ClassVar[int]
        type: str
        count: int
        install_gpu_drivers: bool
        driver_version: str

        def __init__(self, type: _Optional[str]=..., count: _Optional[int]=..., install_gpu_drivers: bool=..., driver_version: _Optional[str]=...) -> None:
            ...

    class InstancePolicy(_message.Message):
        __slots__ = ('allowed_machine_types', 'machine_type', 'min_cpu_platform', 'provisioning_model', 'accelerators', 'boot_disk', 'disks', 'reservation')
        ALLOWED_MACHINE_TYPES_FIELD_NUMBER: _ClassVar[int]
        MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
        MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_MODEL_FIELD_NUMBER: _ClassVar[int]
        ACCELERATORS_FIELD_NUMBER: _ClassVar[int]
        BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
        DISKS_FIELD_NUMBER: _ClassVar[int]
        RESERVATION_FIELD_NUMBER: _ClassVar[int]
        allowed_machine_types: _containers.RepeatedScalarFieldContainer[str]
        machine_type: str
        min_cpu_platform: str
        provisioning_model: AllocationPolicy.ProvisioningModel
        accelerators: _containers.RepeatedCompositeFieldContainer[AllocationPolicy.Accelerator]
        boot_disk: AllocationPolicy.Disk
        disks: _containers.RepeatedCompositeFieldContainer[AllocationPolicy.AttachedDisk]
        reservation: str

        def __init__(self, allowed_machine_types: _Optional[_Iterable[str]]=..., machine_type: _Optional[str]=..., min_cpu_platform: _Optional[str]=..., provisioning_model: _Optional[_Union[AllocationPolicy.ProvisioningModel, str]]=..., accelerators: _Optional[_Iterable[_Union[AllocationPolicy.Accelerator, _Mapping]]]=..., boot_disk: _Optional[_Union[AllocationPolicy.Disk, _Mapping]]=..., disks: _Optional[_Iterable[_Union[AllocationPolicy.AttachedDisk, _Mapping]]]=..., reservation: _Optional[str]=...) -> None:
            ...

    class InstancePolicyOrTemplate(_message.Message):
        __slots__ = ('policy', 'instance_template', 'install_gpu_drivers', 'install_ops_agent', 'block_project_ssh_keys')
        POLICY_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        INSTALL_GPU_DRIVERS_FIELD_NUMBER: _ClassVar[int]
        INSTALL_OPS_AGENT_FIELD_NUMBER: _ClassVar[int]
        BLOCK_PROJECT_SSH_KEYS_FIELD_NUMBER: _ClassVar[int]
        policy: AllocationPolicy.InstancePolicy
        instance_template: str
        install_gpu_drivers: bool
        install_ops_agent: bool
        block_project_ssh_keys: bool

        def __init__(self, policy: _Optional[_Union[AllocationPolicy.InstancePolicy, _Mapping]]=..., instance_template: _Optional[str]=..., install_gpu_drivers: bool=..., install_ops_agent: bool=..., block_project_ssh_keys: bool=...) -> None:
            ...

    class NetworkInterface(_message.Message):
        __slots__ = ('network', 'subnetwork', 'no_external_ip_address')
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
        NO_EXTERNAL_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        network: str
        subnetwork: str
        no_external_ip_address: bool

        def __init__(self, network: _Optional[str]=..., subnetwork: _Optional[str]=..., no_external_ip_address: bool=...) -> None:
            ...

    class NetworkPolicy(_message.Message):
        __slots__ = ('network_interfaces',)
        NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
        network_interfaces: _containers.RepeatedCompositeFieldContainer[AllocationPolicy.NetworkInterface]

        def __init__(self, network_interfaces: _Optional[_Iterable[_Union[AllocationPolicy.NetworkInterface, _Mapping]]]=...) -> None:
            ...

    class PlacementPolicy(_message.Message):
        __slots__ = ('collocation', 'max_distance')
        COLLOCATION_FIELD_NUMBER: _ClassVar[int]
        MAX_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        collocation: str
        max_distance: int

        def __init__(self, collocation: _Optional[str]=..., max_distance: _Optional[int]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_MODELS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    location: AllocationPolicy.LocationPolicy
    instance: AllocationPolicy.InstancePolicy
    instances: _containers.RepeatedCompositeFieldContainer[AllocationPolicy.InstancePolicyOrTemplate]
    instance_templates: _containers.RepeatedScalarFieldContainer[str]
    provisioning_models: _containers.RepeatedScalarFieldContainer[AllocationPolicy.ProvisioningModel]
    service_account_email: str
    service_account: ServiceAccount
    labels: _containers.ScalarMap[str, str]
    network: AllocationPolicy.NetworkPolicy
    placement: AllocationPolicy.PlacementPolicy
    tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, location: _Optional[_Union[AllocationPolicy.LocationPolicy, _Mapping]]=..., instance: _Optional[_Union[AllocationPolicy.InstancePolicy, _Mapping]]=..., instances: _Optional[_Iterable[_Union[AllocationPolicy.InstancePolicyOrTemplate, _Mapping]]]=..., instance_templates: _Optional[_Iterable[str]]=..., provisioning_models: _Optional[_Iterable[_Union[AllocationPolicy.ProvisioningModel, str]]]=..., service_account_email: _Optional[str]=..., service_account: _Optional[_Union[ServiceAccount, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., network: _Optional[_Union[AllocationPolicy.NetworkPolicy, _Mapping]]=..., placement: _Optional[_Union[AllocationPolicy.PlacementPolicy, _Mapping]]=..., tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class TaskGroup(_message.Message):
    __slots__ = ('name', 'task_spec', 'task_count', 'parallelism', 'scheduling_policy', 'allocation_policy', 'labels', 'task_environments', 'task_count_per_node', 'require_hosts_file', 'permissive_ssh', 'run_as_non_root', 'service_account')

    class SchedulingPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCHEDULING_POLICY_UNSPECIFIED: _ClassVar[TaskGroup.SchedulingPolicy]
        AS_SOON_AS_POSSIBLE: _ClassVar[TaskGroup.SchedulingPolicy]
        IN_ORDER: _ClassVar[TaskGroup.SchedulingPolicy]
    SCHEDULING_POLICY_UNSPECIFIED: TaskGroup.SchedulingPolicy
    AS_SOON_AS_POSSIBLE: TaskGroup.SchedulingPolicy
    IN_ORDER: TaskGroup.SchedulingPolicy

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_SPEC_FIELD_NUMBER: _ClassVar[int]
    TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARALLELISM_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    ALLOCATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TASK_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    TASK_COUNT_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_HOSTS_FILE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIVE_SSH_FIELD_NUMBER: _ClassVar[int]
    RUN_AS_NON_ROOT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    task_spec: _task_pb2.TaskSpec
    task_count: int
    parallelism: int
    scheduling_policy: TaskGroup.SchedulingPolicy
    allocation_policy: AllocationPolicy
    labels: _containers.ScalarMap[str, str]
    task_environments: _containers.RepeatedCompositeFieldContainer[_task_pb2.Environment]
    task_count_per_node: int
    require_hosts_file: bool
    permissive_ssh: bool
    run_as_non_root: bool
    service_account: ServiceAccount

    def __init__(self, name: _Optional[str]=..., task_spec: _Optional[_Union[_task_pb2.TaskSpec, _Mapping]]=..., task_count: _Optional[int]=..., parallelism: _Optional[int]=..., scheduling_policy: _Optional[_Union[TaskGroup.SchedulingPolicy, str]]=..., allocation_policy: _Optional[_Union[AllocationPolicy, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., task_environments: _Optional[_Iterable[_Union[_task_pb2.Environment, _Mapping]]]=..., task_count_per_node: _Optional[int]=..., require_hosts_file: bool=..., permissive_ssh: bool=..., run_as_non_root: bool=..., service_account: _Optional[_Union[ServiceAccount, _Mapping]]=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('email', 'scopes')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    email: str
    scopes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, email: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
        ...