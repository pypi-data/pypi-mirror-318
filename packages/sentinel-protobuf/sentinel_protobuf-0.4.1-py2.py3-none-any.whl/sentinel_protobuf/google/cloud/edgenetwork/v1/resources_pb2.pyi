from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ResourceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNKNOWN: _ClassVar[ResourceState]
    STATE_PENDING: _ClassVar[ResourceState]
    STATE_PROVISIONING: _ClassVar[ResourceState]
    STATE_RUNNING: _ClassVar[ResourceState]
    STATE_SUSPENDED: _ClassVar[ResourceState]
    STATE_DELETING: _ClassVar[ResourceState]
STATE_UNKNOWN: ResourceState
STATE_PENDING: ResourceState
STATE_PROVISIONING: ResourceState
STATE_RUNNING: ResourceState
STATE_SUSPENDED: ResourceState
STATE_DELETING: ResourceState

class Zone(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'layout_name')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    layout_name: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., layout_name: _Optional[str]=...) -> None:
        ...

class Network(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'mtu')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    mtu: int

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., mtu: _Optional[int]=...) -> None:
        ...

class Subnet(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'network', 'ipv4_cidr', 'ipv6_cidr', 'vlan_id', 'bonding_type', 'state')

    class BondingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BONDING_TYPE_UNSPECIFIED: _ClassVar[Subnet.BondingType]
        BONDED: _ClassVar[Subnet.BondingType]
        NON_BONDED: _ClassVar[Subnet.BondingType]
    BONDING_TYPE_UNSPECIFIED: Subnet.BondingType
    BONDED: Subnet.BondingType
    NON_BONDED: Subnet.BondingType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    IPV4_CIDR_FIELD_NUMBER: _ClassVar[int]
    IPV6_CIDR_FIELD_NUMBER: _ClassVar[int]
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BONDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    network: str
    ipv4_cidr: _containers.RepeatedScalarFieldContainer[str]
    ipv6_cidr: _containers.RepeatedScalarFieldContainer[str]
    vlan_id: int
    bonding_type: Subnet.BondingType
    state: ResourceState

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., network: _Optional[str]=..., ipv4_cidr: _Optional[_Iterable[str]]=..., ipv6_cidr: _Optional[_Iterable[str]]=..., vlan_id: _Optional[int]=..., bonding_type: _Optional[_Union[Subnet.BondingType, str]]=..., state: _Optional[_Union[ResourceState, str]]=...) -> None:
        ...

class Interconnect(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'interconnect_type', 'uuid', 'device_cloud_resource_name', 'physical_ports')

    class InterconnectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERCONNECT_TYPE_UNSPECIFIED: _ClassVar[Interconnect.InterconnectType]
        DEDICATED: _ClassVar[Interconnect.InterconnectType]
    INTERCONNECT_TYPE_UNSPECIFIED: Interconnect.InterconnectType
    DEDICATED: Interconnect.InterconnectType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INTERCONNECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLOUD_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_PORTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    interconnect_type: Interconnect.InterconnectType
    uuid: str
    device_cloud_resource_name: str
    physical_ports: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., interconnect_type: _Optional[_Union[Interconnect.InterconnectType, str]]=..., uuid: _Optional[str]=..., device_cloud_resource_name: _Optional[str]=..., physical_ports: _Optional[_Iterable[str]]=...) -> None:
        ...

class InterconnectAttachment(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'interconnect', 'network', 'vlan_id', 'mtu', 'state')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INTERCONNECT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    interconnect: str
    network: str
    vlan_id: int
    mtu: int
    state: ResourceState

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., interconnect: _Optional[str]=..., network: _Optional[str]=..., vlan_id: _Optional[int]=..., mtu: _Optional[int]=..., state: _Optional[_Union[ResourceState, str]]=...) -> None:
        ...

class Router(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'network', 'interface', 'bgp_peer', 'bgp', 'state', 'route_advertisements')

    class Interface(_message.Message):
        __slots__ = ('name', 'ipv4_cidr', 'ipv6_cidr', 'linked_interconnect_attachment', 'subnetwork', 'loopback_ip_addresses')
        NAME_FIELD_NUMBER: _ClassVar[int]
        IPV4_CIDR_FIELD_NUMBER: _ClassVar[int]
        IPV6_CIDR_FIELD_NUMBER: _ClassVar[int]
        LINKED_INTERCONNECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
        LOOPBACK_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        name: str
        ipv4_cidr: str
        ipv6_cidr: str
        linked_interconnect_attachment: str
        subnetwork: str
        loopback_ip_addresses: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, name: _Optional[str]=..., ipv4_cidr: _Optional[str]=..., ipv6_cidr: _Optional[str]=..., linked_interconnect_attachment: _Optional[str]=..., subnetwork: _Optional[str]=..., loopback_ip_addresses: _Optional[_Iterable[str]]=...) -> None:
            ...

    class BgpPeer(_message.Message):
        __slots__ = ('name', 'interface', 'interface_ipv4_cidr', 'interface_ipv6_cidr', 'peer_ipv4_cidr', 'peer_ipv6_cidr', 'peer_asn', 'local_asn')
        NAME_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_IPV4_CIDR_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_IPV6_CIDR_FIELD_NUMBER: _ClassVar[int]
        PEER_IPV4_CIDR_FIELD_NUMBER: _ClassVar[int]
        PEER_IPV6_CIDR_FIELD_NUMBER: _ClassVar[int]
        PEER_ASN_FIELD_NUMBER: _ClassVar[int]
        LOCAL_ASN_FIELD_NUMBER: _ClassVar[int]
        name: str
        interface: str
        interface_ipv4_cidr: str
        interface_ipv6_cidr: str
        peer_ipv4_cidr: str
        peer_ipv6_cidr: str
        peer_asn: int
        local_asn: int

        def __init__(self, name: _Optional[str]=..., interface: _Optional[str]=..., interface_ipv4_cidr: _Optional[str]=..., interface_ipv6_cidr: _Optional[str]=..., peer_ipv4_cidr: _Optional[str]=..., peer_ipv6_cidr: _Optional[str]=..., peer_asn: _Optional[int]=..., local_asn: _Optional[int]=...) -> None:
            ...

    class Bgp(_message.Message):
        __slots__ = ('asn', 'keepalive_interval_in_seconds')
        ASN_FIELD_NUMBER: _ClassVar[int]
        KEEPALIVE_INTERVAL_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
        asn: int
        keepalive_interval_in_seconds: int

        def __init__(self, asn: _Optional[int]=..., keepalive_interval_in_seconds: _Optional[int]=...) -> None:
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
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    BGP_PEER_FIELD_NUMBER: _ClassVar[int]
    BGP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_ADVERTISEMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    network: str
    interface: _containers.RepeatedCompositeFieldContainer[Router.Interface]
    bgp_peer: _containers.RepeatedCompositeFieldContainer[Router.BgpPeer]
    bgp: Router.Bgp
    state: ResourceState
    route_advertisements: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., network: _Optional[str]=..., interface: _Optional[_Iterable[_Union[Router.Interface, _Mapping]]]=..., bgp_peer: _Optional[_Iterable[_Union[Router.BgpPeer, _Mapping]]]=..., bgp: _Optional[_Union[Router.Bgp, _Mapping]]=..., state: _Optional[_Union[ResourceState, str]]=..., route_advertisements: _Optional[_Iterable[str]]=...) -> None:
        ...

class LinkLayerAddress(_message.Message):
    __slots__ = ('mac_address', 'ip_address')
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    mac_address: str
    ip_address: str

    def __init__(self, mac_address: _Optional[str]=..., ip_address: _Optional[str]=...) -> None:
        ...

class SubnetStatus(_message.Message):
    __slots__ = ('name', 'mac_address', 'link_layer_addresses')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LINK_LAYER_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    name: str
    mac_address: str
    link_layer_addresses: _containers.RepeatedCompositeFieldContainer[LinkLayerAddress]

    def __init__(self, name: _Optional[str]=..., mac_address: _Optional[str]=..., link_layer_addresses: _Optional[_Iterable[_Union[LinkLayerAddress, _Mapping]]]=...) -> None:
        ...

class InterconnectDiagnostics(_message.Message):
    __slots__ = ('mac_address', 'link_layer_addresses', 'links')

    class LinkStatus(_message.Message):
        __slots__ = ('circuit_id', 'lacp_status', 'lldp_statuses', 'packet_counts')
        CIRCUIT_ID_FIELD_NUMBER: _ClassVar[int]
        LACP_STATUS_FIELD_NUMBER: _ClassVar[int]
        LLDP_STATUSES_FIELD_NUMBER: _ClassVar[int]
        PACKET_COUNTS_FIELD_NUMBER: _ClassVar[int]
        circuit_id: str
        lacp_status: InterconnectDiagnostics.LinkLACPStatus
        lldp_statuses: _containers.RepeatedCompositeFieldContainer[InterconnectDiagnostics.LinkLLDPStatus]
        packet_counts: InterconnectDiagnostics.PacketCounts

        def __init__(self, circuit_id: _Optional[str]=..., lacp_status: _Optional[_Union[InterconnectDiagnostics.LinkLACPStatus, _Mapping]]=..., lldp_statuses: _Optional[_Iterable[_Union[InterconnectDiagnostics.LinkLLDPStatus, _Mapping]]]=..., packet_counts: _Optional[_Union[InterconnectDiagnostics.PacketCounts, _Mapping]]=...) -> None:
            ...

    class PacketCounts(_message.Message):
        __slots__ = ('inbound_unicast', 'inbound_errors', 'inbound_discards', 'outbound_unicast', 'outbound_errors', 'outbound_discards')
        INBOUND_UNICAST_FIELD_NUMBER: _ClassVar[int]
        INBOUND_ERRORS_FIELD_NUMBER: _ClassVar[int]
        INBOUND_DISCARDS_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_UNICAST_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_ERRORS_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_DISCARDS_FIELD_NUMBER: _ClassVar[int]
        inbound_unicast: int
        inbound_errors: int
        inbound_discards: int
        outbound_unicast: int
        outbound_errors: int
        outbound_discards: int

        def __init__(self, inbound_unicast: _Optional[int]=..., inbound_errors: _Optional[int]=..., inbound_discards: _Optional[int]=..., outbound_unicast: _Optional[int]=..., outbound_errors: _Optional[int]=..., outbound_discards: _Optional[int]=...) -> None:
            ...

    class LinkLACPStatus(_message.Message):
        __slots__ = ('state', 'google_system_id', 'neighbor_system_id', 'aggregatable', 'collecting', 'distributing')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[InterconnectDiagnostics.LinkLACPStatus.State]
            ACTIVE: _ClassVar[InterconnectDiagnostics.LinkLACPStatus.State]
            DETACHED: _ClassVar[InterconnectDiagnostics.LinkLACPStatus.State]
        UNKNOWN: InterconnectDiagnostics.LinkLACPStatus.State
        ACTIVE: InterconnectDiagnostics.LinkLACPStatus.State
        DETACHED: InterconnectDiagnostics.LinkLACPStatus.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
        NEIGHBOR_SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
        AGGREGATABLE_FIELD_NUMBER: _ClassVar[int]
        COLLECTING_FIELD_NUMBER: _ClassVar[int]
        DISTRIBUTING_FIELD_NUMBER: _ClassVar[int]
        state: InterconnectDiagnostics.LinkLACPStatus.State
        google_system_id: str
        neighbor_system_id: str
        aggregatable: bool
        collecting: bool
        distributing: bool

        def __init__(self, state: _Optional[_Union[InterconnectDiagnostics.LinkLACPStatus.State, str]]=..., google_system_id: _Optional[str]=..., neighbor_system_id: _Optional[str]=..., aggregatable: bool=..., collecting: bool=..., distributing: bool=...) -> None:
            ...

    class LinkLLDPStatus(_message.Message):
        __slots__ = ('peer_system_name', 'peer_system_description', 'peer_chassis_id', 'peer_chassis_id_type', 'peer_port_id', 'peer_port_id_type')
        PEER_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
        PEER_SYSTEM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        PEER_CHASSIS_ID_FIELD_NUMBER: _ClassVar[int]
        PEER_CHASSIS_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
        PEER_PORT_ID_FIELD_NUMBER: _ClassVar[int]
        PEER_PORT_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
        peer_system_name: str
        peer_system_description: str
        peer_chassis_id: str
        peer_chassis_id_type: str
        peer_port_id: str
        peer_port_id_type: str

        def __init__(self, peer_system_name: _Optional[str]=..., peer_system_description: _Optional[str]=..., peer_chassis_id: _Optional[str]=..., peer_chassis_id_type: _Optional[str]=..., peer_port_id: _Optional[str]=..., peer_port_id_type: _Optional[str]=...) -> None:
            ...
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LINK_LAYER_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    mac_address: str
    link_layer_addresses: _containers.RepeatedCompositeFieldContainer[LinkLayerAddress]
    links: _containers.RepeatedCompositeFieldContainer[InterconnectDiagnostics.LinkStatus]

    def __init__(self, mac_address: _Optional[str]=..., link_layer_addresses: _Optional[_Iterable[_Union[LinkLayerAddress, _Mapping]]]=..., links: _Optional[_Iterable[_Union[InterconnectDiagnostics.LinkStatus, _Mapping]]]=...) -> None:
        ...

class RouterStatus(_message.Message):
    __slots__ = ('network', 'bgp_peer_status')

    class BgpPeerStatus(_message.Message):
        __slots__ = ('name', 'ip_address', 'peer_ip_address', 'status', 'state', 'uptime', 'uptime_seconds', 'prefix_counter')

        class BgpStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[RouterStatus.BgpPeerStatus.BgpStatus]
            UP: _ClassVar[RouterStatus.BgpPeerStatus.BgpStatus]
            DOWN: _ClassVar[RouterStatus.BgpPeerStatus.BgpStatus]
        UNKNOWN: RouterStatus.BgpPeerStatus.BgpStatus
        UP: RouterStatus.BgpPeerStatus.BgpStatus
        DOWN: RouterStatus.BgpPeerStatus.BgpStatus
        NAME_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PEER_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        UPTIME_FIELD_NUMBER: _ClassVar[int]
        UPTIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
        PREFIX_COUNTER_FIELD_NUMBER: _ClassVar[int]
        name: str
        ip_address: str
        peer_ip_address: str
        status: RouterStatus.BgpPeerStatus.BgpStatus
        state: str
        uptime: str
        uptime_seconds: int
        prefix_counter: RouterStatus.PrefixCounter

        def __init__(self, name: _Optional[str]=..., ip_address: _Optional[str]=..., peer_ip_address: _Optional[str]=..., status: _Optional[_Union[RouterStatus.BgpPeerStatus.BgpStatus, str]]=..., state: _Optional[str]=..., uptime: _Optional[str]=..., uptime_seconds: _Optional[int]=..., prefix_counter: _Optional[_Union[RouterStatus.PrefixCounter, _Mapping]]=...) -> None:
            ...

    class PrefixCounter(_message.Message):
        __slots__ = ('advertised', 'denied', 'received', 'sent', 'suppressed', 'withdrawn')
        ADVERTISED_FIELD_NUMBER: _ClassVar[int]
        DENIED_FIELD_NUMBER: _ClassVar[int]
        RECEIVED_FIELD_NUMBER: _ClassVar[int]
        SENT_FIELD_NUMBER: _ClassVar[int]
        SUPPRESSED_FIELD_NUMBER: _ClassVar[int]
        WITHDRAWN_FIELD_NUMBER: _ClassVar[int]
        advertised: int
        denied: int
        received: int
        sent: int
        suppressed: int
        withdrawn: int

        def __init__(self, advertised: _Optional[int]=..., denied: _Optional[int]=..., received: _Optional[int]=..., sent: _Optional[int]=..., suppressed: _Optional[int]=..., withdrawn: _Optional[int]=...) -> None:
            ...
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    BGP_PEER_STATUS_FIELD_NUMBER: _ClassVar[int]
    network: str
    bgp_peer_status: _containers.RepeatedCompositeFieldContainer[RouterStatus.BgpPeerStatus]

    def __init__(self, network: _Optional[str]=..., bgp_peer_status: _Optional[_Iterable[_Union[RouterStatus.BgpPeerStatus, _Mapping]]]=...) -> None:
        ...