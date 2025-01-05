from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networkconnectivity.v1 import common_pb2 as _common_pb2
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

class LocationFeature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCATION_FEATURE_UNSPECIFIED: _ClassVar[LocationFeature]
    SITE_TO_CLOUD_SPOKES: _ClassVar[LocationFeature]
    SITE_TO_SITE_SPOKES: _ClassVar[LocationFeature]

class RouteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTE_TYPE_UNSPECIFIED: _ClassVar[RouteType]
    VPC_PRIMARY_SUBNET: _ClassVar[RouteType]
    VPC_SECONDARY_SUBNET: _ClassVar[RouteType]
    DYNAMIC_ROUTE: _ClassVar[RouteType]

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[State]
    CREATING: _ClassVar[State]
    ACTIVE: _ClassVar[State]
    DELETING: _ClassVar[State]
    ACCEPTING: _ClassVar[State]
    REJECTING: _ClassVar[State]
    UPDATING: _ClassVar[State]
    INACTIVE: _ClassVar[State]
    OBSOLETE: _ClassVar[State]

class SpokeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPOKE_TYPE_UNSPECIFIED: _ClassVar[SpokeType]
    VPN_TUNNEL: _ClassVar[SpokeType]
    INTERCONNECT_ATTACHMENT: _ClassVar[SpokeType]
    ROUTER_APPLIANCE: _ClassVar[SpokeType]
    VPC_NETWORK: _ClassVar[SpokeType]
    PRODUCER_VPC_NETWORK: _ClassVar[SpokeType]

class PolicyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POLICY_MODE_UNSPECIFIED: _ClassVar[PolicyMode]
    PRESET: _ClassVar[PolicyMode]

class PresetTopology(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRESET_TOPOLOGY_UNSPECIFIED: _ClassVar[PresetTopology]
    MESH: _ClassVar[PresetTopology]
    STAR: _ClassVar[PresetTopology]
LOCATION_FEATURE_UNSPECIFIED: LocationFeature
SITE_TO_CLOUD_SPOKES: LocationFeature
SITE_TO_SITE_SPOKES: LocationFeature
ROUTE_TYPE_UNSPECIFIED: RouteType
VPC_PRIMARY_SUBNET: RouteType
VPC_SECONDARY_SUBNET: RouteType
DYNAMIC_ROUTE: RouteType
STATE_UNSPECIFIED: State
CREATING: State
ACTIVE: State
DELETING: State
ACCEPTING: State
REJECTING: State
UPDATING: State
INACTIVE: State
OBSOLETE: State
SPOKE_TYPE_UNSPECIFIED: SpokeType
VPN_TUNNEL: SpokeType
INTERCONNECT_ATTACHMENT: SpokeType
ROUTER_APPLIANCE: SpokeType
VPC_NETWORK: SpokeType
PRODUCER_VPC_NETWORK: SpokeType
POLICY_MODE_UNSPECIFIED: PolicyMode
PRESET: PolicyMode
PRESET_TOPOLOGY_UNSPECIFIED: PresetTopology
MESH: PresetTopology
STAR: PresetTopology

class Hub(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "description", "unique_id", "state", "routing_vpcs", "route_tables", "spoke_summary", "policy_mode", "preset_topology", "export_psc")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_VPCS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TABLES_FIELD_NUMBER: _ClassVar[int]
    SPOKE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    POLICY_MODE_FIELD_NUMBER: _ClassVar[int]
    PRESET_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    EXPORT_PSC_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    unique_id: str
    state: State
    routing_vpcs: _containers.RepeatedCompositeFieldContainer[RoutingVPC]
    route_tables: _containers.RepeatedScalarFieldContainer[str]
    spoke_summary: SpokeSummary
    policy_mode: PolicyMode
    preset_topology: PresetTopology
    export_psc: bool
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., unique_id: _Optional[str] = ..., state: _Optional[_Union[State, str]] = ..., routing_vpcs: _Optional[_Iterable[_Union[RoutingVPC, _Mapping]]] = ..., route_tables: _Optional[_Iterable[str]] = ..., spoke_summary: _Optional[_Union[SpokeSummary, _Mapping]] = ..., policy_mode: _Optional[_Union[PolicyMode, str]] = ..., preset_topology: _Optional[_Union[PresetTopology, str]] = ..., export_psc: bool = ...) -> None: ...

class RoutingVPC(_message.Message):
    __slots__ = ("uri", "required_for_new_site_to_site_data_transfer_spokes")
    URI_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FOR_NEW_SITE_TO_SITE_DATA_TRANSFER_SPOKES_FIELD_NUMBER: _ClassVar[int]
    uri: str
    required_for_new_site_to_site_data_transfer_spokes: bool
    def __init__(self, uri: _Optional[str] = ..., required_for_new_site_to_site_data_transfer_spokes: bool = ...) -> None: ...

class Spoke(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "description", "hub", "group", "linked_vpn_tunnels", "linked_interconnect_attachments", "linked_router_appliance_instances", "linked_vpc_network", "linked_producer_vpc_network", "unique_id", "state", "reasons", "spoke_type")
    class StateReason(_message.Message):
        __slots__ = ("code", "message", "user_details")
        class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CODE_UNSPECIFIED: _ClassVar[Spoke.StateReason.Code]
            PENDING_REVIEW: _ClassVar[Spoke.StateReason.Code]
            REJECTED: _ClassVar[Spoke.StateReason.Code]
            PAUSED: _ClassVar[Spoke.StateReason.Code]
            FAILED: _ClassVar[Spoke.StateReason.Code]
        CODE_UNSPECIFIED: Spoke.StateReason.Code
        PENDING_REVIEW: Spoke.StateReason.Code
        REJECTED: Spoke.StateReason.Code
        PAUSED: Spoke.StateReason.Code
        FAILED: Spoke.StateReason.Code
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        USER_DETAILS_FIELD_NUMBER: _ClassVar[int]
        code: Spoke.StateReason.Code
        message: str
        user_details: str
        def __init__(self, code: _Optional[_Union[Spoke.StateReason.Code, str]] = ..., message: _Optional[str] = ..., user_details: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HUB_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    LINKED_VPN_TUNNELS_FIELD_NUMBER: _ClassVar[int]
    LINKED_INTERCONNECT_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    LINKED_ROUTER_APPLIANCE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    LINKED_VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    LINKED_PRODUCER_VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    SPOKE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    hub: str
    group: str
    linked_vpn_tunnels: LinkedVpnTunnels
    linked_interconnect_attachments: LinkedInterconnectAttachments
    linked_router_appliance_instances: LinkedRouterApplianceInstances
    linked_vpc_network: LinkedVpcNetwork
    linked_producer_vpc_network: LinkedProducerVpcNetwork
    unique_id: str
    state: State
    reasons: _containers.RepeatedCompositeFieldContainer[Spoke.StateReason]
    spoke_type: SpokeType
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., hub: _Optional[str] = ..., group: _Optional[str] = ..., linked_vpn_tunnels: _Optional[_Union[LinkedVpnTunnels, _Mapping]] = ..., linked_interconnect_attachments: _Optional[_Union[LinkedInterconnectAttachments, _Mapping]] = ..., linked_router_appliance_instances: _Optional[_Union[LinkedRouterApplianceInstances, _Mapping]] = ..., linked_vpc_network: _Optional[_Union[LinkedVpcNetwork, _Mapping]] = ..., linked_producer_vpc_network: _Optional[_Union[LinkedProducerVpcNetwork, _Mapping]] = ..., unique_id: _Optional[str] = ..., state: _Optional[_Union[State, str]] = ..., reasons: _Optional[_Iterable[_Union[Spoke.StateReason, _Mapping]]] = ..., spoke_type: _Optional[_Union[SpokeType, str]] = ...) -> None: ...

class RouteTable(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "description", "uid", "state")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    uid: str
    state: State
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., uid: _Optional[str] = ..., state: _Optional[_Union[State, str]] = ...) -> None: ...

class Route(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "ip_cidr_range", "type", "next_hop_vpc_network", "labels", "description", "uid", "state", "spoke", "location", "priority", "next_hop_vpn_tunnel", "next_hop_router_appliance_instance", "next_hop_interconnect_attachment")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    IP_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SPOKE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_VPN_TUNNEL_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_ROUTER_APPLIANCE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_INTERCONNECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    ip_cidr_range: str
    type: RouteType
    next_hop_vpc_network: NextHopVpcNetwork
    labels: _containers.ScalarMap[str, str]
    description: str
    uid: str
    state: State
    spoke: str
    location: str
    priority: int
    next_hop_vpn_tunnel: NextHopVPNTunnel
    next_hop_router_appliance_instance: NextHopRouterApplianceInstance
    next_hop_interconnect_attachment: NextHopInterconnectAttachment
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ip_cidr_range: _Optional[str] = ..., type: _Optional[_Union[RouteType, str]] = ..., next_hop_vpc_network: _Optional[_Union[NextHopVpcNetwork, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., uid: _Optional[str] = ..., state: _Optional[_Union[State, str]] = ..., spoke: _Optional[str] = ..., location: _Optional[str] = ..., priority: _Optional[int] = ..., next_hop_vpn_tunnel: _Optional[_Union[NextHopVPNTunnel, _Mapping]] = ..., next_hop_router_appliance_instance: _Optional[_Union[NextHopRouterApplianceInstance, _Mapping]] = ..., next_hop_interconnect_attachment: _Optional[_Union[NextHopInterconnectAttachment, _Mapping]] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "description", "uid", "state", "auto_accept", "route_table")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    AUTO_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    uid: str
    state: State
    auto_accept: AutoAccept
    route_table: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., uid: _Optional[str] = ..., state: _Optional[_Union[State, str]] = ..., auto_accept: _Optional[_Union[AutoAccept, _Mapping]] = ..., route_table: _Optional[str] = ...) -> None: ...

class AutoAccept(_message.Message):
    __slots__ = ("auto_accept_projects",)
    AUTO_ACCEPT_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    auto_accept_projects: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, auto_accept_projects: _Optional[_Iterable[str]] = ...) -> None: ...

class ListHubsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListHubsResponse(_message.Message):
    __slots__ = ("hubs", "next_page_token", "unreachable")
    HUBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    hubs: _containers.RepeatedCompositeFieldContainer[Hub]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hubs: _Optional[_Iterable[_Union[Hub, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetHubRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateHubRequest(_message.Message):
    __slots__ = ("parent", "hub_id", "hub", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    hub_id: str
    hub: Hub
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., hub_id: _Optional[str] = ..., hub: _Optional[_Union[Hub, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateHubRequest(_message.Message):
    __slots__ = ("update_mask", "hub", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    HUB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    hub: Hub
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., hub: _Optional[_Union[Hub, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteHubRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListHubSpokesRequest(_message.Message):
    __slots__ = ("name", "spoke_locations", "page_size", "page_token", "filter", "order_by", "view")
    class SpokeView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPOKE_VIEW_UNSPECIFIED: _ClassVar[ListHubSpokesRequest.SpokeView]
        BASIC: _ClassVar[ListHubSpokesRequest.SpokeView]
        DETAILED: _ClassVar[ListHubSpokesRequest.SpokeView]
    SPOKE_VIEW_UNSPECIFIED: ListHubSpokesRequest.SpokeView
    BASIC: ListHubSpokesRequest.SpokeView
    DETAILED: ListHubSpokesRequest.SpokeView
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPOKE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    spoke_locations: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: ListHubSpokesRequest.SpokeView
    def __init__(self, name: _Optional[str] = ..., spoke_locations: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., view: _Optional[_Union[ListHubSpokesRequest.SpokeView, str]] = ...) -> None: ...

class ListHubSpokesResponse(_message.Message):
    __slots__ = ("spokes", "next_page_token", "unreachable")
    SPOKES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    spokes: _containers.RepeatedCompositeFieldContainer[Spoke]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, spokes: _Optional[_Iterable[_Union[Spoke, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class QueryHubStatusRequest(_message.Message):
    __slots__ = ("name", "page_size", "page_token", "filter", "order_by", "group_by")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    group_by: str
    def __init__(self, name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., group_by: _Optional[str] = ...) -> None: ...

class QueryHubStatusResponse(_message.Message):
    __slots__ = ("hub_status_entries", "next_page_token")
    HUB_STATUS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    hub_status_entries: _containers.RepeatedCompositeFieldContainer[HubStatusEntry]
    next_page_token: str
    def __init__(self, hub_status_entries: _Optional[_Iterable[_Union[HubStatusEntry, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class HubStatusEntry(_message.Message):
    __slots__ = ("count", "group_by", "psc_propagation_status")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    PSC_PROPAGATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    count: int
    group_by: str
    psc_propagation_status: PscPropagationStatus
    def __init__(self, count: _Optional[int] = ..., group_by: _Optional[str] = ..., psc_propagation_status: _Optional[_Union[PscPropagationStatus, _Mapping]] = ...) -> None: ...

class PscPropagationStatus(_message.Message):
    __slots__ = ("source_spoke", "source_group", "source_forwarding_rule", "target_spoke", "target_group", "code", "message")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CODE_UNSPECIFIED: _ClassVar[PscPropagationStatus.Code]
        READY: _ClassVar[PscPropagationStatus.Code]
        PROPAGATING: _ClassVar[PscPropagationStatus.Code]
        ERROR_PRODUCER_PROPAGATED_CONNECTION_LIMIT_EXCEEDED: _ClassVar[PscPropagationStatus.Code]
        ERROR_PRODUCER_NAT_IP_SPACE_EXHAUSTED: _ClassVar[PscPropagationStatus.Code]
        ERROR_PRODUCER_QUOTA_EXCEEDED: _ClassVar[PscPropagationStatus.Code]
        ERROR_CONSUMER_QUOTA_EXCEEDED: _ClassVar[PscPropagationStatus.Code]
    CODE_UNSPECIFIED: PscPropagationStatus.Code
    READY: PscPropagationStatus.Code
    PROPAGATING: PscPropagationStatus.Code
    ERROR_PRODUCER_PROPAGATED_CONNECTION_LIMIT_EXCEEDED: PscPropagationStatus.Code
    ERROR_PRODUCER_NAT_IP_SPACE_EXHAUSTED: PscPropagationStatus.Code
    ERROR_PRODUCER_QUOTA_EXCEEDED: PscPropagationStatus.Code
    ERROR_CONSUMER_QUOTA_EXCEEDED: PscPropagationStatus.Code
    SOURCE_SPOKE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    TARGET_SPOKE_FIELD_NUMBER: _ClassVar[int]
    TARGET_GROUP_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    source_spoke: str
    source_group: str
    source_forwarding_rule: str
    target_spoke: str
    target_group: str
    code: PscPropagationStatus.Code
    message: str
    def __init__(self, source_spoke: _Optional[str] = ..., source_group: _Optional[str] = ..., source_forwarding_rule: _Optional[str] = ..., target_spoke: _Optional[str] = ..., target_group: _Optional[str] = ..., code: _Optional[_Union[PscPropagationStatus.Code, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ListSpokesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListSpokesResponse(_message.Message):
    __slots__ = ("spokes", "next_page_token", "unreachable")
    SPOKES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    spokes: _containers.RepeatedCompositeFieldContainer[Spoke]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, spokes: _Optional[_Iterable[_Union[Spoke, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSpokeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateSpokeRequest(_message.Message):
    __slots__ = ("parent", "spoke_id", "spoke", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SPOKE_ID_FIELD_NUMBER: _ClassVar[int]
    SPOKE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    spoke_id: str
    spoke: Spoke
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., spoke_id: _Optional[str] = ..., spoke: _Optional[_Union[Spoke, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateSpokeRequest(_message.Message):
    __slots__ = ("update_mask", "spoke", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SPOKE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    spoke: Spoke
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., spoke: _Optional[_Union[Spoke, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteSpokeRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class AcceptHubSpokeRequest(_message.Message):
    __slots__ = ("name", "spoke_uri", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPOKE_URI_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    spoke_uri: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., spoke_uri: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class AcceptHubSpokeResponse(_message.Message):
    __slots__ = ("spoke",)
    SPOKE_FIELD_NUMBER: _ClassVar[int]
    spoke: Spoke
    def __init__(self, spoke: _Optional[_Union[Spoke, _Mapping]] = ...) -> None: ...

class RejectHubSpokeRequest(_message.Message):
    __slots__ = ("name", "spoke_uri", "request_id", "details")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPOKE_URI_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    spoke_uri: str
    request_id: str
    details: str
    def __init__(self, name: _Optional[str] = ..., spoke_uri: _Optional[str] = ..., request_id: _Optional[str] = ..., details: _Optional[str] = ...) -> None: ...

class RejectHubSpokeResponse(_message.Message):
    __slots__ = ("spoke",)
    SPOKE_FIELD_NUMBER: _ClassVar[int]
    spoke: Spoke
    def __init__(self, spoke: _Optional[_Union[Spoke, _Mapping]] = ...) -> None: ...

class GetRouteTableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetRouteRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRoutesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListRoutesResponse(_message.Message):
    __slots__ = ("routes", "next_page_token", "unreachable")
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[Route]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, routes: _Optional[_Iterable[_Union[Route, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class ListRouteTablesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListRouteTablesResponse(_message.Message):
    __slots__ = ("route_tables", "next_page_token", "unreachable")
    ROUTE_TABLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    route_tables: _containers.RepeatedCompositeFieldContainer[RouteTable]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, route_tables: _Optional[_Iterable[_Union[RouteTable, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class ListGroupsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListGroupsResponse(_message.Message):
    __slots__ = ("groups", "next_page_token", "unreachable")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, groups: _Optional[_Iterable[_Union[Group, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class LinkedVpnTunnels(_message.Message):
    __slots__ = ("uris", "site_to_site_data_transfer", "vpc_network", "include_import_ranges")
    URIS_FIELD_NUMBER: _ClassVar[int]
    SITE_TO_SITE_DATA_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_IMPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    uris: _containers.RepeatedScalarFieldContainer[str]
    site_to_site_data_transfer: bool
    vpc_network: str
    include_import_ranges: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uris: _Optional[_Iterable[str]] = ..., site_to_site_data_transfer: bool = ..., vpc_network: _Optional[str] = ..., include_import_ranges: _Optional[_Iterable[str]] = ...) -> None: ...

class LinkedInterconnectAttachments(_message.Message):
    __slots__ = ("uris", "site_to_site_data_transfer", "vpc_network", "include_import_ranges")
    URIS_FIELD_NUMBER: _ClassVar[int]
    SITE_TO_SITE_DATA_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_IMPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    uris: _containers.RepeatedScalarFieldContainer[str]
    site_to_site_data_transfer: bool
    vpc_network: str
    include_import_ranges: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uris: _Optional[_Iterable[str]] = ..., site_to_site_data_transfer: bool = ..., vpc_network: _Optional[str] = ..., include_import_ranges: _Optional[_Iterable[str]] = ...) -> None: ...

class LinkedRouterApplianceInstances(_message.Message):
    __slots__ = ("instances", "site_to_site_data_transfer", "vpc_network", "include_import_ranges")
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    SITE_TO_SITE_DATA_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_IMPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[RouterApplianceInstance]
    site_to_site_data_transfer: bool
    vpc_network: str
    include_import_ranges: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instances: _Optional[_Iterable[_Union[RouterApplianceInstance, _Mapping]]] = ..., site_to_site_data_transfer: bool = ..., vpc_network: _Optional[str] = ..., include_import_ranges: _Optional[_Iterable[str]] = ...) -> None: ...

class LinkedVpcNetwork(_message.Message):
    __slots__ = ("uri", "exclude_export_ranges", "include_export_ranges", "producer_vpc_spokes")
    URI_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_EXPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_VPC_SPOKES_FIELD_NUMBER: _ClassVar[int]
    uri: str
    exclude_export_ranges: _containers.RepeatedScalarFieldContainer[str]
    include_export_ranges: _containers.RepeatedScalarFieldContainer[str]
    producer_vpc_spokes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uri: _Optional[str] = ..., exclude_export_ranges: _Optional[_Iterable[str]] = ..., include_export_ranges: _Optional[_Iterable[str]] = ..., producer_vpc_spokes: _Optional[_Iterable[str]] = ...) -> None: ...

class LinkedProducerVpcNetwork(_message.Message):
    __slots__ = ("network", "service_consumer_vpc_spoke", "peering", "producer_network", "exclude_export_ranges", "include_export_ranges")
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONSUMER_VPC_SPOKE_FIELD_NUMBER: _ClassVar[int]
    PEERING_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_EXPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    network: str
    service_consumer_vpc_spoke: str
    peering: str
    producer_network: str
    exclude_export_ranges: _containers.RepeatedScalarFieldContainer[str]
    include_export_ranges: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, network: _Optional[str] = ..., service_consumer_vpc_spoke: _Optional[str] = ..., peering: _Optional[str] = ..., producer_network: _Optional[str] = ..., exclude_export_ranges: _Optional[_Iterable[str]] = ..., include_export_ranges: _Optional[_Iterable[str]] = ...) -> None: ...

class RouterApplianceInstance(_message.Message):
    __slots__ = ("virtual_machine", "ip_address")
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    virtual_machine: str
    ip_address: str
    def __init__(self, virtual_machine: _Optional[str] = ..., ip_address: _Optional[str] = ...) -> None: ...

class LocationMetadata(_message.Message):
    __slots__ = ("location_features",)
    LOCATION_FEATURES_FIELD_NUMBER: _ClassVar[int]
    location_features: _containers.RepeatedScalarFieldContainer[LocationFeature]
    def __init__(self, location_features: _Optional[_Iterable[_Union[LocationFeature, str]]] = ...) -> None: ...

class NextHopVpcNetwork(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str
    def __init__(self, uri: _Optional[str] = ...) -> None: ...

class NextHopVPNTunnel(_message.Message):
    __slots__ = ("uri", "vpc_network", "site_to_site_data_transfer")
    URI_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    SITE_TO_SITE_DATA_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    uri: str
    vpc_network: str
    site_to_site_data_transfer: bool
    def __init__(self, uri: _Optional[str] = ..., vpc_network: _Optional[str] = ..., site_to_site_data_transfer: bool = ...) -> None: ...

class NextHopRouterApplianceInstance(_message.Message):
    __slots__ = ("uri", "vpc_network", "site_to_site_data_transfer")
    URI_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    SITE_TO_SITE_DATA_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    uri: str
    vpc_network: str
    site_to_site_data_transfer: bool
    def __init__(self, uri: _Optional[str] = ..., vpc_network: _Optional[str] = ..., site_to_site_data_transfer: bool = ...) -> None: ...

class NextHopInterconnectAttachment(_message.Message):
    __slots__ = ("uri", "vpc_network", "site_to_site_data_transfer")
    URI_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    SITE_TO_SITE_DATA_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    uri: str
    vpc_network: str
    site_to_site_data_transfer: bool
    def __init__(self, uri: _Optional[str] = ..., vpc_network: _Optional[str] = ..., site_to_site_data_transfer: bool = ...) -> None: ...

class SpokeSummary(_message.Message):
    __slots__ = ("spoke_type_counts", "spoke_state_counts", "spoke_state_reason_counts")
    class SpokeTypeCount(_message.Message):
        __slots__ = ("spoke_type", "count")
        SPOKE_TYPE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        spoke_type: SpokeType
        count: int
        def __init__(self, spoke_type: _Optional[_Union[SpokeType, str]] = ..., count: _Optional[int] = ...) -> None: ...
    class SpokeStateCount(_message.Message):
        __slots__ = ("state", "count")
        STATE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        state: State
        count: int
        def __init__(self, state: _Optional[_Union[State, str]] = ..., count: _Optional[int] = ...) -> None: ...
    class SpokeStateReasonCount(_message.Message):
        __slots__ = ("state_reason_code", "count")
        STATE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        state_reason_code: Spoke.StateReason.Code
        count: int
        def __init__(self, state_reason_code: _Optional[_Union[Spoke.StateReason.Code, str]] = ..., count: _Optional[int] = ...) -> None: ...
    SPOKE_TYPE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    SPOKE_STATE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    SPOKE_STATE_REASON_COUNTS_FIELD_NUMBER: _ClassVar[int]
    spoke_type_counts: _containers.RepeatedCompositeFieldContainer[SpokeSummary.SpokeTypeCount]
    spoke_state_counts: _containers.RepeatedCompositeFieldContainer[SpokeSummary.SpokeStateCount]
    spoke_state_reason_counts: _containers.RepeatedCompositeFieldContainer[SpokeSummary.SpokeStateReasonCount]
    def __init__(self, spoke_type_counts: _Optional[_Iterable[_Union[SpokeSummary.SpokeTypeCount, _Mapping]]] = ..., spoke_state_counts: _Optional[_Iterable[_Union[SpokeSummary.SpokeStateCount, _Mapping]]] = ..., spoke_state_reason_counts: _Optional[_Iterable[_Union[SpokeSummary.SpokeStateReasonCount, _Mapping]]] = ...) -> None: ...

class GetGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateGroupRequest(_message.Message):
    __slots__ = ("update_mask", "group", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    group: Group
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., group: _Optional[_Union[Group, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...
