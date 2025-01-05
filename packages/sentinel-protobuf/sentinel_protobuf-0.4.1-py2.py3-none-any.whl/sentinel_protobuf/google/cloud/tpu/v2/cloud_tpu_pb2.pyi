from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GuestAttributes(_message.Message):
    __slots__ = ('query_path', 'query_value')
    QUERY_PATH_FIELD_NUMBER: _ClassVar[int]
    QUERY_VALUE_FIELD_NUMBER: _ClassVar[int]
    query_path: str
    query_value: GuestAttributesValue

    def __init__(self, query_path: _Optional[str]=..., query_value: _Optional[_Union[GuestAttributesValue, _Mapping]]=...) -> None:
        ...

class GuestAttributesValue(_message.Message):
    __slots__ = ('items',)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[GuestAttributesEntry]

    def __init__(self, items: _Optional[_Iterable[_Union[GuestAttributesEntry, _Mapping]]]=...) -> None:
        ...

class GuestAttributesEntry(_message.Message):
    __slots__ = ('namespace', 'key', 'value')
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    key: str
    value: str

    def __init__(self, namespace: _Optional[str]=..., key: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class AttachedDisk(_message.Message):
    __slots__ = ('source_disk', 'mode')

    class DiskMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISK_MODE_UNSPECIFIED: _ClassVar[AttachedDisk.DiskMode]
        READ_WRITE: _ClassVar[AttachedDisk.DiskMode]
        READ_ONLY: _ClassVar[AttachedDisk.DiskMode]
    DISK_MODE_UNSPECIFIED: AttachedDisk.DiskMode
    READ_WRITE: AttachedDisk.DiskMode
    READ_ONLY: AttachedDisk.DiskMode
    SOURCE_DISK_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    source_disk: str
    mode: AttachedDisk.DiskMode

    def __init__(self, source_disk: _Optional[str]=..., mode: _Optional[_Union[AttachedDisk.DiskMode, str]]=...) -> None:
        ...

class SchedulingConfig(_message.Message):
    __slots__ = ('preemptible', 'reserved')
    PREEMPTIBLE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    preemptible: bool
    reserved: bool

    def __init__(self, preemptible: bool=..., reserved: bool=...) -> None:
        ...

class NetworkEndpoint(_message.Message):
    __slots__ = ('ip_address', 'port', 'access_config')
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    port: int
    access_config: AccessConfig

    def __init__(self, ip_address: _Optional[str]=..., port: _Optional[int]=..., access_config: _Optional[_Union[AccessConfig, _Mapping]]=...) -> None:
        ...

class AccessConfig(_message.Message):
    __slots__ = ('external_ip',)
    EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    external_ip: str

    def __init__(self, external_ip: _Optional[str]=...) -> None:
        ...

class NetworkConfig(_message.Message):
    __slots__ = ('network', 'subnetwork', 'enable_external_ips', 'can_ip_forward')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_EXTERNAL_IPS_FIELD_NUMBER: _ClassVar[int]
    CAN_IP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str
    enable_external_ips: bool
    can_ip_forward: bool

    def __init__(self, network: _Optional[str]=..., subnetwork: _Optional[str]=..., enable_external_ips: bool=..., can_ip_forward: bool=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('email', 'scope')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    email: str
    scope: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, email: _Optional[str]=..., scope: _Optional[_Iterable[str]]=...) -> None:
        ...

class Node(_message.Message):
    __slots__ = ('name', 'description', 'accelerator_type', 'state', 'health_description', 'runtime_version', 'network_config', 'cidr_block', 'service_account', 'create_time', 'scheduling_config', 'network_endpoints', 'health', 'labels', 'metadata', 'tags', 'id', 'data_disks', 'api_version', 'symptoms', 'shielded_instance_config', 'accelerator_config', 'queued_resource', 'multislice_node')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Node.State]
        CREATING: _ClassVar[Node.State]
        READY: _ClassVar[Node.State]
        RESTARTING: _ClassVar[Node.State]
        REIMAGING: _ClassVar[Node.State]
        DELETING: _ClassVar[Node.State]
        REPAIRING: _ClassVar[Node.State]
        STOPPED: _ClassVar[Node.State]
        STOPPING: _ClassVar[Node.State]
        STARTING: _ClassVar[Node.State]
        PREEMPTED: _ClassVar[Node.State]
        TERMINATED: _ClassVar[Node.State]
        HIDING: _ClassVar[Node.State]
        HIDDEN: _ClassVar[Node.State]
        UNHIDING: _ClassVar[Node.State]
    STATE_UNSPECIFIED: Node.State
    CREATING: Node.State
    READY: Node.State
    RESTARTING: Node.State
    REIMAGING: Node.State
    DELETING: Node.State
    REPAIRING: Node.State
    STOPPED: Node.State
    STOPPING: Node.State
    STARTING: Node.State
    PREEMPTED: Node.State
    TERMINATED: Node.State
    HIDING: Node.State
    HIDDEN: Node.State
    UNHIDING: Node.State

    class Health(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEALTH_UNSPECIFIED: _ClassVar[Node.Health]
        HEALTHY: _ClassVar[Node.Health]
        TIMEOUT: _ClassVar[Node.Health]
        UNHEALTHY_TENSORFLOW: _ClassVar[Node.Health]
        UNHEALTHY_MAINTENANCE: _ClassVar[Node.Health]
    HEALTH_UNSPECIFIED: Node.Health
    HEALTHY: Node.Health
    TIMEOUT: Node.Health
    UNHEALTHY_TENSORFLOW: Node.Health
    UNHEALTHY_MAINTENANCE: Node.Health

    class ApiVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        API_VERSION_UNSPECIFIED: _ClassVar[Node.ApiVersion]
        V1_ALPHA1: _ClassVar[Node.ApiVersion]
        V1: _ClassVar[Node.ApiVersion]
        V2_ALPHA1: _ClassVar[Node.ApiVersion]
        V2: _ClassVar[Node.ApiVersion]
    API_VERSION_UNSPECIFIED: Node.ApiVersion
    V1_ALPHA1: Node.ApiVersion
    V1: Node.ApiVersion
    V2_ALPHA1: Node.ApiVersion
    V2: Node.ApiVersion

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_VERSION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_DISKS_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    SYMPTOMS_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUEUED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    MULTISLICE_NODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    accelerator_type: str
    state: Node.State
    health_description: str
    runtime_version: str
    network_config: NetworkConfig
    cidr_block: str
    service_account: ServiceAccount
    create_time: _timestamp_pb2.Timestamp
    scheduling_config: SchedulingConfig
    network_endpoints: _containers.RepeatedCompositeFieldContainer[NetworkEndpoint]
    health: Node.Health
    labels: _containers.ScalarMap[str, str]
    metadata: _containers.ScalarMap[str, str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    id: int
    data_disks: _containers.RepeatedCompositeFieldContainer[AttachedDisk]
    api_version: Node.ApiVersion
    symptoms: _containers.RepeatedCompositeFieldContainer[Symptom]
    shielded_instance_config: ShieldedInstanceConfig
    accelerator_config: AcceleratorConfig
    queued_resource: str
    multislice_node: bool

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., accelerator_type: _Optional[str]=..., state: _Optional[_Union[Node.State, str]]=..., health_description: _Optional[str]=..., runtime_version: _Optional[str]=..., network_config: _Optional[_Union[NetworkConfig, _Mapping]]=..., cidr_block: _Optional[str]=..., service_account: _Optional[_Union[ServiceAccount, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., scheduling_config: _Optional[_Union[SchedulingConfig, _Mapping]]=..., network_endpoints: _Optional[_Iterable[_Union[NetworkEndpoint, _Mapping]]]=..., health: _Optional[_Union[Node.Health, str]]=..., labels: _Optional[_Mapping[str, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., tags: _Optional[_Iterable[str]]=..., id: _Optional[int]=..., data_disks: _Optional[_Iterable[_Union[AttachedDisk, _Mapping]]]=..., api_version: _Optional[_Union[Node.ApiVersion, str]]=..., symptoms: _Optional[_Iterable[_Union[Symptom, _Mapping]]]=..., shielded_instance_config: _Optional[_Union[ShieldedInstanceConfig, _Mapping]]=..., accelerator_config: _Optional[_Union[AcceleratorConfig, _Mapping]]=..., queued_resource: _Optional[str]=..., multislice_node: bool=...) -> None:
        ...

class ListNodesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListNodesResponse(_message.Message):
    __slots__ = ('nodes', 'next_page_token', 'unreachable')
    NODES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetNodeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateNodeRequest(_message.Message):
    __slots__ = ('parent', 'node_id', 'node')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    node_id: str
    node: Node

    def __init__(self, parent: _Optional[str]=..., node_id: _Optional[str]=..., node: _Optional[_Union[Node, _Mapping]]=...) -> None:
        ...

class DeleteNodeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StopNodeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StartNodeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateNodeRequest(_message.Message):
    __slots__ = ('update_mask', 'node')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    node: Node

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., node: _Optional[_Union[Node, _Mapping]]=...) -> None:
        ...

class ServiceIdentity(_message.Message):
    __slots__ = ('email',)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str

    def __init__(self, email: _Optional[str]=...) -> None:
        ...

class GenerateServiceIdentityRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class GenerateServiceIdentityResponse(_message.Message):
    __slots__ = ('identity',)
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    identity: ServiceIdentity

    def __init__(self, identity: _Optional[_Union[ServiceIdentity, _Mapping]]=...) -> None:
        ...

class AcceleratorType(_message.Message):
    __slots__ = ('name', 'type', 'accelerator_configs')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    accelerator_configs: _containers.RepeatedCompositeFieldContainer[AcceleratorConfig]

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., accelerator_configs: _Optional[_Iterable[_Union[AcceleratorConfig, _Mapping]]]=...) -> None:
        ...

class GetAcceleratorTypeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAcceleratorTypesRequest(_message.Message):
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

class ListAcceleratorTypesResponse(_message.Message):
    __slots__ = ('accelerator_types', 'next_page_token', 'unreachable')
    ACCELERATOR_TYPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    accelerator_types: _containers.RepeatedCompositeFieldContainer[AcceleratorType]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, accelerator_types: _Optional[_Iterable[_Union[AcceleratorType, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class RuntimeVersion(_message.Message):
    __slots__ = ('name', 'version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str

    def __init__(self, name: _Optional[str]=..., version: _Optional[str]=...) -> None:
        ...

class GetRuntimeVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRuntimeVersionsRequest(_message.Message):
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

class ListRuntimeVersionsResponse(_message.Message):
    __slots__ = ('runtime_versions', 'next_page_token', 'unreachable')
    RUNTIME_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    runtime_versions: _containers.RepeatedCompositeFieldContainer[RuntimeVersion]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, runtime_versions: _Optional[_Iterable[_Union[RuntimeVersion, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_detail', 'cancel_requested', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_detail: str
    cancel_requested: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_detail: _Optional[str]=..., cancel_requested: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class Symptom(_message.Message):
    __slots__ = ('create_time', 'symptom_type', 'details', 'worker_id')

    class SymptomType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYMPTOM_TYPE_UNSPECIFIED: _ClassVar[Symptom.SymptomType]
        LOW_MEMORY: _ClassVar[Symptom.SymptomType]
        OUT_OF_MEMORY: _ClassVar[Symptom.SymptomType]
        EXECUTE_TIMED_OUT: _ClassVar[Symptom.SymptomType]
        MESH_BUILD_FAIL: _ClassVar[Symptom.SymptomType]
        HBM_OUT_OF_MEMORY: _ClassVar[Symptom.SymptomType]
        PROJECT_ABUSE: _ClassVar[Symptom.SymptomType]
    SYMPTOM_TYPE_UNSPECIFIED: Symptom.SymptomType
    LOW_MEMORY: Symptom.SymptomType
    OUT_OF_MEMORY: Symptom.SymptomType
    EXECUTE_TIMED_OUT: Symptom.SymptomType
    MESH_BUILD_FAIL: Symptom.SymptomType
    HBM_OUT_OF_MEMORY: Symptom.SymptomType
    PROJECT_ABUSE: Symptom.SymptomType
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SYMPTOM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    symptom_type: Symptom.SymptomType
    details: str
    worker_id: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., symptom_type: _Optional[_Union[Symptom.SymptomType, str]]=..., details: _Optional[str]=..., worker_id: _Optional[str]=...) -> None:
        ...

class GetGuestAttributesRequest(_message.Message):
    __slots__ = ('name', 'query_path', 'worker_ids')
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_PATH_FIELD_NUMBER: _ClassVar[int]
    WORKER_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    query_path: str
    worker_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., query_path: _Optional[str]=..., worker_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetGuestAttributesResponse(_message.Message):
    __slots__ = ('guest_attributes',)
    GUEST_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    guest_attributes: _containers.RepeatedCompositeFieldContainer[GuestAttributes]

    def __init__(self, guest_attributes: _Optional[_Iterable[_Union[GuestAttributes, _Mapping]]]=...) -> None:
        ...

class AcceleratorConfig(_message.Message):
    __slots__ = ('type', 'topology')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AcceleratorConfig.Type]
        V2: _ClassVar[AcceleratorConfig.Type]
        V3: _ClassVar[AcceleratorConfig.Type]
        V4: _ClassVar[AcceleratorConfig.Type]
    TYPE_UNSPECIFIED: AcceleratorConfig.Type
    V2: AcceleratorConfig.Type
    V3: AcceleratorConfig.Type
    V4: AcceleratorConfig.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    type: AcceleratorConfig.Type
    topology: str

    def __init__(self, type: _Optional[_Union[AcceleratorConfig.Type, str]]=..., topology: _Optional[str]=...) -> None:
        ...

class ShieldedInstanceConfig(_message.Message):
    __slots__ = ('enable_secure_boot',)
    ENABLE_SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    enable_secure_boot: bool

    def __init__(self, enable_secure_boot: bool=...) -> None:
        ...