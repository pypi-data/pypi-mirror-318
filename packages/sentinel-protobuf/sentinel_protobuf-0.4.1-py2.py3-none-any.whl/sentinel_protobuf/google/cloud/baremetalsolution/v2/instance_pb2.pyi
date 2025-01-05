from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.baremetalsolution.v2 import common_pb2 as _common_pb2
from google.cloud.baremetalsolution.v2 import lun_pb2 as _lun_pb2
from google.cloud.baremetalsolution.v2 import network_pb2 as _network_pb2
from google.cloud.baremetalsolution.v2 import volume_pb2 as _volume_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Instance(_message.Message):
    __slots__ = ('name', 'id', 'create_time', 'update_time', 'machine_type', 'state', 'hyperthreading_enabled', 'labels', 'luns', 'volumes', 'networks', 'interactive_serial_console_enabled', 'os_image', 'pod', 'network_template', 'logical_interfaces', 'login_info', 'workload_profile', 'firmware_version')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        PROVISIONING: _ClassVar[Instance.State]
        RUNNING: _ClassVar[Instance.State]
        DELETED: _ClassVar[Instance.State]
        UPDATING: _ClassVar[Instance.State]
        STARTING: _ClassVar[Instance.State]
        STOPPING: _ClassVar[Instance.State]
        SHUTDOWN: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    PROVISIONING: Instance.State
    RUNNING: Instance.State
    DELETED: Instance.State
    UPDATING: Instance.State
    STARTING: Instance.State
    STOPPING: Instance.State
    SHUTDOWN: Instance.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    HYPERTHREADING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LUNS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVE_SERIAL_CONSOLE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OS_IMAGE_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_PROFILE_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    machine_type: str
    state: Instance.State
    hyperthreading_enabled: bool
    labels: _containers.ScalarMap[str, str]
    luns: _containers.RepeatedCompositeFieldContainer[_lun_pb2.Lun]
    volumes: _containers.RepeatedCompositeFieldContainer[_volume_pb2.Volume]
    networks: _containers.RepeatedCompositeFieldContainer[_network_pb2.Network]
    interactive_serial_console_enabled: bool
    os_image: str
    pod: str
    network_template: str
    logical_interfaces: _containers.RepeatedCompositeFieldContainer[_network_pb2.LogicalInterface]
    login_info: str
    workload_profile: _common_pb2.WorkloadProfile
    firmware_version: str

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., machine_type: _Optional[str]=..., state: _Optional[_Union[Instance.State, str]]=..., hyperthreading_enabled: bool=..., labels: _Optional[_Mapping[str, str]]=..., luns: _Optional[_Iterable[_Union[_lun_pb2.Lun, _Mapping]]]=..., volumes: _Optional[_Iterable[_Union[_volume_pb2.Volume, _Mapping]]]=..., networks: _Optional[_Iterable[_Union[_network_pb2.Network, _Mapping]]]=..., interactive_serial_console_enabled: bool=..., os_image: _Optional[str]=..., pod: _Optional[str]=..., network_template: _Optional[str]=..., logical_interfaces: _Optional[_Iterable[_Union[_network_pb2.LogicalInterface, _Mapping]]]=..., login_info: _Optional[str]=..., workload_profile: _Optional[_Union[_common_pb2.WorkloadProfile, str]]=..., firmware_version: _Optional[str]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
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

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ('instance', 'update_mask')
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    instance: Instance
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, instance: _Optional[_Union[Instance, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class RenameInstanceRequest(_message.Message):
    __slots__ = ('name', 'new_instance_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_instance_id: str

    def __init__(self, name: _Optional[str]=..., new_instance_id: _Optional[str]=...) -> None:
        ...

class ResetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StartInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StartInstanceResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class StopInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StopInstanceResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EnableInteractiveSerialConsoleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EnableInteractiveSerialConsoleResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DisableInteractiveSerialConsoleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DisableInteractiveSerialConsoleResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DetachLunRequest(_message.Message):
    __slots__ = ('instance', 'lun', 'skip_reboot')
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    SKIP_REBOOT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    lun: str
    skip_reboot: bool

    def __init__(self, instance: _Optional[str]=..., lun: _Optional[str]=..., skip_reboot: bool=...) -> None:
        ...

class ServerNetworkTemplate(_message.Message):
    __slots__ = ('name', 'applicable_instance_types', 'logical_interfaces')

    class LogicalInterface(_message.Message):
        __slots__ = ('name', 'type', 'required')

        class InterfaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            INTERFACE_TYPE_UNSPECIFIED: _ClassVar[ServerNetworkTemplate.LogicalInterface.InterfaceType]
            BOND: _ClassVar[ServerNetworkTemplate.LogicalInterface.InterfaceType]
            NIC: _ClassVar[ServerNetworkTemplate.LogicalInterface.InterfaceType]
        INTERFACE_TYPE_UNSPECIFIED: ServerNetworkTemplate.LogicalInterface.InterfaceType
        BOND: ServerNetworkTemplate.LogicalInterface.InterfaceType
        NIC: ServerNetworkTemplate.LogicalInterface.InterfaceType
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: ServerNetworkTemplate.LogicalInterface.InterfaceType
        required: bool

        def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[ServerNetworkTemplate.LogicalInterface.InterfaceType, str]]=..., required: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICABLE_INSTANCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    name: str
    applicable_instance_types: _containers.RepeatedScalarFieldContainer[str]
    logical_interfaces: _containers.RepeatedCompositeFieldContainer[ServerNetworkTemplate.LogicalInterface]

    def __init__(self, name: _Optional[str]=..., applicable_instance_types: _Optional[_Iterable[str]]=..., logical_interfaces: _Optional[_Iterable[_Union[ServerNetworkTemplate.LogicalInterface, _Mapping]]]=...) -> None:
        ...