from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Network(_message.Message):
    __slots__ = ('name', 'id', 'type', 'ip_address', 'mac_address', 'state', 'vlan_id', 'cidr', 'vrf', 'labels', 'services_cidr', 'reservations', 'pod', 'mount_points', 'jumbo_frames_enabled', 'gateway_ip')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Network.Type]
        CLIENT: _ClassVar[Network.Type]
        PRIVATE: _ClassVar[Network.Type]
    TYPE_UNSPECIFIED: Network.Type
    CLIENT: Network.Type
    PRIVATE: Network.Type

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Network.State]
        PROVISIONING: _ClassVar[Network.State]
        PROVISIONED: _ClassVar[Network.State]
        DEPROVISIONING: _ClassVar[Network.State]
        UPDATING: _ClassVar[Network.State]
    STATE_UNSPECIFIED: Network.State
    PROVISIONING: Network.State
    PROVISIONED: Network.State
    DEPROVISIONING: Network.State
    UPDATING: Network.State

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
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    VRF_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SERVICES_CIDR_FIELD_NUMBER: _ClassVar[int]
    RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINTS_FIELD_NUMBER: _ClassVar[int]
    JUMBO_FRAMES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    type: Network.Type
    ip_address: str
    mac_address: _containers.RepeatedScalarFieldContainer[str]
    state: Network.State
    vlan_id: str
    cidr: str
    vrf: VRF
    labels: _containers.ScalarMap[str, str]
    services_cidr: str
    reservations: _containers.RepeatedCompositeFieldContainer[NetworkAddressReservation]
    pod: str
    mount_points: _containers.RepeatedCompositeFieldContainer[NetworkMountPoint]
    jumbo_frames_enabled: bool
    gateway_ip: str

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., type: _Optional[_Union[Network.Type, str]]=..., ip_address: _Optional[str]=..., mac_address: _Optional[_Iterable[str]]=..., state: _Optional[_Union[Network.State, str]]=..., vlan_id: _Optional[str]=..., cidr: _Optional[str]=..., vrf: _Optional[_Union[VRF, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., services_cidr: _Optional[str]=..., reservations: _Optional[_Iterable[_Union[NetworkAddressReservation, _Mapping]]]=..., pod: _Optional[str]=..., mount_points: _Optional[_Iterable[_Union[NetworkMountPoint, _Mapping]]]=..., jumbo_frames_enabled: bool=..., gateway_ip: _Optional[str]=...) -> None:
        ...

class NetworkAddressReservation(_message.Message):
    __slots__ = ('start_address', 'end_address', 'note')
    START_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    END_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    start_address: str
    end_address: str
    note: str

    def __init__(self, start_address: _Optional[str]=..., end_address: _Optional[str]=..., note: _Optional[str]=...) -> None:
        ...

class VRF(_message.Message):
    __slots__ = ('name', 'state', 'qos_policy', 'vlan_attachments')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[VRF.State]
        PROVISIONING: _ClassVar[VRF.State]
        PROVISIONED: _ClassVar[VRF.State]
    STATE_UNSPECIFIED: VRF.State
    PROVISIONING: VRF.State
    PROVISIONED: VRF.State

    class QosPolicy(_message.Message):
        __slots__ = ('bandwidth_gbps',)
        BANDWIDTH_GBPS_FIELD_NUMBER: _ClassVar[int]
        bandwidth_gbps: float

        def __init__(self, bandwidth_gbps: _Optional[float]=...) -> None:
            ...

    class VlanAttachment(_message.Message):
        __slots__ = ('peer_vlan_id', 'peer_ip', 'router_ip', 'pairing_key', 'qos_policy', 'id', 'interconnect_attachment')
        PEER_VLAN_ID_FIELD_NUMBER: _ClassVar[int]
        PEER_IP_FIELD_NUMBER: _ClassVar[int]
        ROUTER_IP_FIELD_NUMBER: _ClassVar[int]
        PAIRING_KEY_FIELD_NUMBER: _ClassVar[int]
        QOS_POLICY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        INTERCONNECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        peer_vlan_id: int
        peer_ip: str
        router_ip: str
        pairing_key: str
        qos_policy: VRF.QosPolicy
        id: str
        interconnect_attachment: str

        def __init__(self, peer_vlan_id: _Optional[int]=..., peer_ip: _Optional[str]=..., router_ip: _Optional[str]=..., pairing_key: _Optional[str]=..., qos_policy: _Optional[_Union[VRF.QosPolicy, _Mapping]]=..., id: _Optional[str]=..., interconnect_attachment: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    QOS_POLICY_FIELD_NUMBER: _ClassVar[int]
    VLAN_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: VRF.State
    qos_policy: VRF.QosPolicy
    vlan_attachments: _containers.RepeatedCompositeFieldContainer[VRF.VlanAttachment]

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[VRF.State, str]]=..., qos_policy: _Optional[_Union[VRF.QosPolicy, _Mapping]]=..., vlan_attachments: _Optional[_Iterable[_Union[VRF.VlanAttachment, _Mapping]]]=...) -> None:
        ...

class LogicalInterface(_message.Message):
    __slots__ = ('logical_network_interfaces', 'name', 'interface_index')

    class LogicalNetworkInterface(_message.Message):
        __slots__ = ('network', 'ip_address', 'default_gateway', 'network_type', 'id')
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_GATEWAY_FIELD_NUMBER: _ClassVar[int]
        NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        network: str
        ip_address: str
        default_gateway: bool
        network_type: Network.Type
        id: str

        def __init__(self, network: _Optional[str]=..., ip_address: _Optional[str]=..., default_gateway: bool=..., network_type: _Optional[_Union[Network.Type, str]]=..., id: _Optional[str]=...) -> None:
            ...
    LOGICAL_NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_INDEX_FIELD_NUMBER: _ClassVar[int]
    logical_network_interfaces: _containers.RepeatedCompositeFieldContainer[LogicalInterface.LogicalNetworkInterface]
    name: str
    interface_index: int

    def __init__(self, logical_network_interfaces: _Optional[_Iterable[_Union[LogicalInterface.LogicalNetworkInterface, _Mapping]]]=..., name: _Optional[str]=..., interface_index: _Optional[int]=...) -> None:
        ...

class GetNetworkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListNetworksRequest(_message.Message):
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

class ListNetworksResponse(_message.Message):
    __slots__ = ('networks', 'next_page_token', 'unreachable')
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    networks: _containers.RepeatedCompositeFieldContainer[Network]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, networks: _Optional[_Iterable[_Union[Network, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateNetworkRequest(_message.Message):
    __slots__ = ('network', 'update_mask')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    network: Network
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, network: _Optional[_Union[Network, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class NetworkUsage(_message.Message):
    __slots__ = ('network', 'used_ips')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    USED_IPS_FIELD_NUMBER: _ClassVar[int]
    network: Network
    used_ips: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, network: _Optional[_Union[Network, _Mapping]]=..., used_ips: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListNetworkUsageRequest(_message.Message):
    __slots__ = ('location',)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: str

    def __init__(self, location: _Optional[str]=...) -> None:
        ...

class ListNetworkUsageResponse(_message.Message):
    __slots__ = ('networks',)
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    networks: _containers.RepeatedCompositeFieldContainer[NetworkUsage]

    def __init__(self, networks: _Optional[_Iterable[_Union[NetworkUsage, _Mapping]]]=...) -> None:
        ...

class NetworkMountPoint(_message.Message):
    __slots__ = ('instance', 'logical_interface', 'default_gateway', 'ip_address')
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    instance: str
    logical_interface: str
    default_gateway: bool
    ip_address: str

    def __init__(self, instance: _Optional[str]=..., logical_interface: _Optional[str]=..., default_gateway: bool=..., ip_address: _Optional[str]=...) -> None:
        ...

class RenameNetworkRequest(_message.Message):
    __slots__ = ('name', 'new_network_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_network_id: str

    def __init__(self, name: _Optional[str]=..., new_network_id: _Optional[str]=...) -> None:
        ...