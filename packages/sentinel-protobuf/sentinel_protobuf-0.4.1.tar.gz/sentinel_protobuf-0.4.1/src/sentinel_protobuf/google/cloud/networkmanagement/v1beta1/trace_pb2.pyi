from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoadBalancerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOAD_BALANCER_TYPE_UNSPECIFIED: _ClassVar[LoadBalancerType]
    HTTPS_ADVANCED_LOAD_BALANCER: _ClassVar[LoadBalancerType]
    HTTPS_LOAD_BALANCER: _ClassVar[LoadBalancerType]
    REGIONAL_HTTPS_LOAD_BALANCER: _ClassVar[LoadBalancerType]
    INTERNAL_HTTPS_LOAD_BALANCER: _ClassVar[LoadBalancerType]
    SSL_PROXY_LOAD_BALANCER: _ClassVar[LoadBalancerType]
    TCP_PROXY_LOAD_BALANCER: _ClassVar[LoadBalancerType]
    INTERNAL_TCP_PROXY_LOAD_BALANCER: _ClassVar[LoadBalancerType]
    NETWORK_LOAD_BALANCER: _ClassVar[LoadBalancerType]
    LEGACY_NETWORK_LOAD_BALANCER: _ClassVar[LoadBalancerType]
    TCP_UDP_INTERNAL_LOAD_BALANCER: _ClassVar[LoadBalancerType]
LOAD_BALANCER_TYPE_UNSPECIFIED: LoadBalancerType
HTTPS_ADVANCED_LOAD_BALANCER: LoadBalancerType
HTTPS_LOAD_BALANCER: LoadBalancerType
REGIONAL_HTTPS_LOAD_BALANCER: LoadBalancerType
INTERNAL_HTTPS_LOAD_BALANCER: LoadBalancerType
SSL_PROXY_LOAD_BALANCER: LoadBalancerType
TCP_PROXY_LOAD_BALANCER: LoadBalancerType
INTERNAL_TCP_PROXY_LOAD_BALANCER: LoadBalancerType
NETWORK_LOAD_BALANCER: LoadBalancerType
LEGACY_NETWORK_LOAD_BALANCER: LoadBalancerType
TCP_UDP_INTERNAL_LOAD_BALANCER: LoadBalancerType

class Trace(_message.Message):
    __slots__ = ("endpoint_info", "steps", "forward_trace_id")
    ENDPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint_info: EndpointInfo
    steps: _containers.RepeatedCompositeFieldContainer[Step]
    forward_trace_id: int
    def __init__(self, endpoint_info: _Optional[_Union[EndpointInfo, _Mapping]] = ..., steps: _Optional[_Iterable[_Union[Step, _Mapping]]] = ..., forward_trace_id: _Optional[int] = ...) -> None: ...

class Step(_message.Message):
    __slots__ = ("description", "state", "causes_drop", "project_id", "instance", "firewall", "route", "endpoint", "google_service", "forwarding_rule", "vpn_gateway", "vpn_tunnel", "vpc_connector", "deliver", "forward", "abort", "drop", "load_balancer", "network", "gke_master", "cloud_sql_instance", "redis_instance", "redis_cluster", "cloud_function", "app_engine_version", "cloud_run_revision", "nat", "proxy_connection", "load_balancer_backend_info", "storage_bucket", "serverless_neg")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Step.State]
        START_FROM_INSTANCE: _ClassVar[Step.State]
        START_FROM_INTERNET: _ClassVar[Step.State]
        START_FROM_GOOGLE_SERVICE: _ClassVar[Step.State]
        START_FROM_PRIVATE_NETWORK: _ClassVar[Step.State]
        START_FROM_GKE_MASTER: _ClassVar[Step.State]
        START_FROM_CLOUD_SQL_INSTANCE: _ClassVar[Step.State]
        START_FROM_REDIS_INSTANCE: _ClassVar[Step.State]
        START_FROM_REDIS_CLUSTER: _ClassVar[Step.State]
        START_FROM_CLOUD_FUNCTION: _ClassVar[Step.State]
        START_FROM_APP_ENGINE_VERSION: _ClassVar[Step.State]
        START_FROM_CLOUD_RUN_REVISION: _ClassVar[Step.State]
        START_FROM_STORAGE_BUCKET: _ClassVar[Step.State]
        START_FROM_PSC_PUBLISHED_SERVICE: _ClassVar[Step.State]
        START_FROM_SERVERLESS_NEG: _ClassVar[Step.State]
        APPLY_INGRESS_FIREWALL_RULE: _ClassVar[Step.State]
        APPLY_EGRESS_FIREWALL_RULE: _ClassVar[Step.State]
        APPLY_ROUTE: _ClassVar[Step.State]
        APPLY_FORWARDING_RULE: _ClassVar[Step.State]
        ANALYZE_LOAD_BALANCER_BACKEND: _ClassVar[Step.State]
        SPOOFING_APPROVED: _ClassVar[Step.State]
        ARRIVE_AT_INSTANCE: _ClassVar[Step.State]
        ARRIVE_AT_INTERNAL_LOAD_BALANCER: _ClassVar[Step.State]
        ARRIVE_AT_EXTERNAL_LOAD_BALANCER: _ClassVar[Step.State]
        ARRIVE_AT_VPN_GATEWAY: _ClassVar[Step.State]
        ARRIVE_AT_VPN_TUNNEL: _ClassVar[Step.State]
        ARRIVE_AT_VPC_CONNECTOR: _ClassVar[Step.State]
        NAT: _ClassVar[Step.State]
        PROXY_CONNECTION: _ClassVar[Step.State]
        DELIVER: _ClassVar[Step.State]
        DROP: _ClassVar[Step.State]
        FORWARD: _ClassVar[Step.State]
        ABORT: _ClassVar[Step.State]
        VIEWER_PERMISSION_MISSING: _ClassVar[Step.State]
    STATE_UNSPECIFIED: Step.State
    START_FROM_INSTANCE: Step.State
    START_FROM_INTERNET: Step.State
    START_FROM_GOOGLE_SERVICE: Step.State
    START_FROM_PRIVATE_NETWORK: Step.State
    START_FROM_GKE_MASTER: Step.State
    START_FROM_CLOUD_SQL_INSTANCE: Step.State
    START_FROM_REDIS_INSTANCE: Step.State
    START_FROM_REDIS_CLUSTER: Step.State
    START_FROM_CLOUD_FUNCTION: Step.State
    START_FROM_APP_ENGINE_VERSION: Step.State
    START_FROM_CLOUD_RUN_REVISION: Step.State
    START_FROM_STORAGE_BUCKET: Step.State
    START_FROM_PSC_PUBLISHED_SERVICE: Step.State
    START_FROM_SERVERLESS_NEG: Step.State
    APPLY_INGRESS_FIREWALL_RULE: Step.State
    APPLY_EGRESS_FIREWALL_RULE: Step.State
    APPLY_ROUTE: Step.State
    APPLY_FORWARDING_RULE: Step.State
    ANALYZE_LOAD_BALANCER_BACKEND: Step.State
    SPOOFING_APPROVED: Step.State
    ARRIVE_AT_INSTANCE: Step.State
    ARRIVE_AT_INTERNAL_LOAD_BALANCER: Step.State
    ARRIVE_AT_EXTERNAL_LOAD_BALANCER: Step.State
    ARRIVE_AT_VPN_GATEWAY: Step.State
    ARRIVE_AT_VPN_TUNNEL: Step.State
    ARRIVE_AT_VPC_CONNECTOR: Step.State
    NAT: Step.State
    PROXY_CONNECTION: Step.State
    DELIVER: Step.State
    DROP: Step.State
    FORWARD: Step.State
    ABORT: Step.State
    VIEWER_PERMISSION_MISSING: Step.State
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CAUSES_DROP_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    FIREWALL_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    VPN_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    VPN_TUNNEL_FIELD_NUMBER: _ClassVar[int]
    VPC_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    DELIVER_FIELD_NUMBER: _ClassVar[int]
    FORWARD_FIELD_NUMBER: _ClassVar[int]
    ABORT_FIELD_NUMBER: _ClassVar[int]
    DROP_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    GKE_MASTER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REDIS_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REDIS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RUN_REVISION_FIELD_NUMBER: _ClassVar[int]
    NAT_FIELD_NUMBER: _ClassVar[int]
    PROXY_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_BACKEND_INFO_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SERVERLESS_NEG_FIELD_NUMBER: _ClassVar[int]
    description: str
    state: Step.State
    causes_drop: bool
    project_id: str
    instance: InstanceInfo
    firewall: FirewallInfo
    route: RouteInfo
    endpoint: EndpointInfo
    google_service: GoogleServiceInfo
    forwarding_rule: ForwardingRuleInfo
    vpn_gateway: VpnGatewayInfo
    vpn_tunnel: VpnTunnelInfo
    vpc_connector: VpcConnectorInfo
    deliver: DeliverInfo
    forward: ForwardInfo
    abort: AbortInfo
    drop: DropInfo
    load_balancer: LoadBalancerInfo
    network: NetworkInfo
    gke_master: GKEMasterInfo
    cloud_sql_instance: CloudSQLInstanceInfo
    redis_instance: RedisInstanceInfo
    redis_cluster: RedisClusterInfo
    cloud_function: CloudFunctionInfo
    app_engine_version: AppEngineVersionInfo
    cloud_run_revision: CloudRunRevisionInfo
    nat: NatInfo
    proxy_connection: ProxyConnectionInfo
    load_balancer_backend_info: LoadBalancerBackendInfo
    storage_bucket: StorageBucketInfo
    serverless_neg: ServerlessNegInfo
    def __init__(self, description: _Optional[str] = ..., state: _Optional[_Union[Step.State, str]] = ..., causes_drop: bool = ..., project_id: _Optional[str] = ..., instance: _Optional[_Union[InstanceInfo, _Mapping]] = ..., firewall: _Optional[_Union[FirewallInfo, _Mapping]] = ..., route: _Optional[_Union[RouteInfo, _Mapping]] = ..., endpoint: _Optional[_Union[EndpointInfo, _Mapping]] = ..., google_service: _Optional[_Union[GoogleServiceInfo, _Mapping]] = ..., forwarding_rule: _Optional[_Union[ForwardingRuleInfo, _Mapping]] = ..., vpn_gateway: _Optional[_Union[VpnGatewayInfo, _Mapping]] = ..., vpn_tunnel: _Optional[_Union[VpnTunnelInfo, _Mapping]] = ..., vpc_connector: _Optional[_Union[VpcConnectorInfo, _Mapping]] = ..., deliver: _Optional[_Union[DeliverInfo, _Mapping]] = ..., forward: _Optional[_Union[ForwardInfo, _Mapping]] = ..., abort: _Optional[_Union[AbortInfo, _Mapping]] = ..., drop: _Optional[_Union[DropInfo, _Mapping]] = ..., load_balancer: _Optional[_Union[LoadBalancerInfo, _Mapping]] = ..., network: _Optional[_Union[NetworkInfo, _Mapping]] = ..., gke_master: _Optional[_Union[GKEMasterInfo, _Mapping]] = ..., cloud_sql_instance: _Optional[_Union[CloudSQLInstanceInfo, _Mapping]] = ..., redis_instance: _Optional[_Union[RedisInstanceInfo, _Mapping]] = ..., redis_cluster: _Optional[_Union[RedisClusterInfo, _Mapping]] = ..., cloud_function: _Optional[_Union[CloudFunctionInfo, _Mapping]] = ..., app_engine_version: _Optional[_Union[AppEngineVersionInfo, _Mapping]] = ..., cloud_run_revision: _Optional[_Union[CloudRunRevisionInfo, _Mapping]] = ..., nat: _Optional[_Union[NatInfo, _Mapping]] = ..., proxy_connection: _Optional[_Union[ProxyConnectionInfo, _Mapping]] = ..., load_balancer_backend_info: _Optional[_Union[LoadBalancerBackendInfo, _Mapping]] = ..., storage_bucket: _Optional[_Union[StorageBucketInfo, _Mapping]] = ..., serverless_neg: _Optional[_Union[ServerlessNegInfo, _Mapping]] = ...) -> None: ...

class InstanceInfo(_message.Message):
    __slots__ = ("display_name", "uri", "interface", "network_uri", "internal_ip", "external_ip", "network_tags", "service_account", "psc_network_attachment_uri")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PSC_NETWORK_ATTACHMENT_URI_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    interface: str
    network_uri: str
    internal_ip: str
    external_ip: str
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    service_account: str
    psc_network_attachment_uri: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., interface: _Optional[str] = ..., network_uri: _Optional[str] = ..., internal_ip: _Optional[str] = ..., external_ip: _Optional[str] = ..., network_tags: _Optional[_Iterable[str]] = ..., service_account: _Optional[str] = ..., psc_network_attachment_uri: _Optional[str] = ...) -> None: ...

class NetworkInfo(_message.Message):
    __slots__ = ("display_name", "uri", "matched_subnet_uri", "matched_ip_range", "region")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    MATCHED_SUBNET_URI_FIELD_NUMBER: _ClassVar[int]
    MATCHED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    matched_subnet_uri: str
    matched_ip_range: str
    region: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., matched_subnet_uri: _Optional[str] = ..., matched_ip_range: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class FirewallInfo(_message.Message):
    __slots__ = ("display_name", "uri", "direction", "action", "priority", "network_uri", "target_tags", "target_service_accounts", "policy", "policy_uri", "firewall_rule_type")
    class FirewallRuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIREWALL_RULE_TYPE_UNSPECIFIED: _ClassVar[FirewallInfo.FirewallRuleType]
        HIERARCHICAL_FIREWALL_POLICY_RULE: _ClassVar[FirewallInfo.FirewallRuleType]
        VPC_FIREWALL_RULE: _ClassVar[FirewallInfo.FirewallRuleType]
        IMPLIED_VPC_FIREWALL_RULE: _ClassVar[FirewallInfo.FirewallRuleType]
        SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE: _ClassVar[FirewallInfo.FirewallRuleType]
        NETWORK_FIREWALL_POLICY_RULE: _ClassVar[FirewallInfo.FirewallRuleType]
        NETWORK_REGIONAL_FIREWALL_POLICY_RULE: _ClassVar[FirewallInfo.FirewallRuleType]
        UNSUPPORTED_FIREWALL_POLICY_RULE: _ClassVar[FirewallInfo.FirewallRuleType]
        TRACKING_STATE: _ClassVar[FirewallInfo.FirewallRuleType]
    FIREWALL_RULE_TYPE_UNSPECIFIED: FirewallInfo.FirewallRuleType
    HIERARCHICAL_FIREWALL_POLICY_RULE: FirewallInfo.FirewallRuleType
    VPC_FIREWALL_RULE: FirewallInfo.FirewallRuleType
    IMPLIED_VPC_FIREWALL_RULE: FirewallInfo.FirewallRuleType
    SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE: FirewallInfo.FirewallRuleType
    NETWORK_FIREWALL_POLICY_RULE: FirewallInfo.FirewallRuleType
    NETWORK_REGIONAL_FIREWALL_POLICY_RULE: FirewallInfo.FirewallRuleType
    UNSUPPORTED_FIREWALL_POLICY_RULE: FirewallInfo.FirewallRuleType
    TRACKING_STATE: FirewallInfo.FirewallRuleType
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    TARGET_TAGS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    POLICY_URI_FIELD_NUMBER: _ClassVar[int]
    FIREWALL_RULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    direction: str
    action: str
    priority: int
    network_uri: str
    target_tags: _containers.RepeatedScalarFieldContainer[str]
    target_service_accounts: _containers.RepeatedScalarFieldContainer[str]
    policy: str
    policy_uri: str
    firewall_rule_type: FirewallInfo.FirewallRuleType
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., direction: _Optional[str] = ..., action: _Optional[str] = ..., priority: _Optional[int] = ..., network_uri: _Optional[str] = ..., target_tags: _Optional[_Iterable[str]] = ..., target_service_accounts: _Optional[_Iterable[str]] = ..., policy: _Optional[str] = ..., policy_uri: _Optional[str] = ..., firewall_rule_type: _Optional[_Union[FirewallInfo.FirewallRuleType, str]] = ...) -> None: ...

class RouteInfo(_message.Message):
    __slots__ = ("route_type", "next_hop_type", "route_scope", "display_name", "uri", "region", "dest_ip_range", "next_hop", "network_uri", "priority", "instance_tags", "src_ip_range", "dest_port_ranges", "src_port_ranges", "protocols", "ncc_hub_uri", "ncc_spoke_uri", "advertised_route_source_router_uri", "advertised_route_next_hop_uri")
    class RouteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROUTE_TYPE_UNSPECIFIED: _ClassVar[RouteInfo.RouteType]
        SUBNET: _ClassVar[RouteInfo.RouteType]
        STATIC: _ClassVar[RouteInfo.RouteType]
        DYNAMIC: _ClassVar[RouteInfo.RouteType]
        PEERING_SUBNET: _ClassVar[RouteInfo.RouteType]
        PEERING_STATIC: _ClassVar[RouteInfo.RouteType]
        PEERING_DYNAMIC: _ClassVar[RouteInfo.RouteType]
        POLICY_BASED: _ClassVar[RouteInfo.RouteType]
        ADVERTISED: _ClassVar[RouteInfo.RouteType]
    ROUTE_TYPE_UNSPECIFIED: RouteInfo.RouteType
    SUBNET: RouteInfo.RouteType
    STATIC: RouteInfo.RouteType
    DYNAMIC: RouteInfo.RouteType
    PEERING_SUBNET: RouteInfo.RouteType
    PEERING_STATIC: RouteInfo.RouteType
    PEERING_DYNAMIC: RouteInfo.RouteType
    POLICY_BASED: RouteInfo.RouteType
    ADVERTISED: RouteInfo.RouteType
    class NextHopType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NEXT_HOP_TYPE_UNSPECIFIED: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_IP: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_INSTANCE: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_NETWORK: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_PEERING: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_INTERCONNECT: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_VPN_TUNNEL: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_VPN_GATEWAY: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_INTERNET_GATEWAY: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_BLACKHOLE: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_ILB: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_ROUTER_APPLIANCE: _ClassVar[RouteInfo.NextHopType]
        NEXT_HOP_NCC_HUB: _ClassVar[RouteInfo.NextHopType]
    NEXT_HOP_TYPE_UNSPECIFIED: RouteInfo.NextHopType
    NEXT_HOP_IP: RouteInfo.NextHopType
    NEXT_HOP_INSTANCE: RouteInfo.NextHopType
    NEXT_HOP_NETWORK: RouteInfo.NextHopType
    NEXT_HOP_PEERING: RouteInfo.NextHopType
    NEXT_HOP_INTERCONNECT: RouteInfo.NextHopType
    NEXT_HOP_VPN_TUNNEL: RouteInfo.NextHopType
    NEXT_HOP_VPN_GATEWAY: RouteInfo.NextHopType
    NEXT_HOP_INTERNET_GATEWAY: RouteInfo.NextHopType
    NEXT_HOP_BLACKHOLE: RouteInfo.NextHopType
    NEXT_HOP_ILB: RouteInfo.NextHopType
    NEXT_HOP_ROUTER_APPLIANCE: RouteInfo.NextHopType
    NEXT_HOP_NCC_HUB: RouteInfo.NextHopType
    class RouteScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROUTE_SCOPE_UNSPECIFIED: _ClassVar[RouteInfo.RouteScope]
        NETWORK: _ClassVar[RouteInfo.RouteScope]
        NCC_HUB: _ClassVar[RouteInfo.RouteScope]
    ROUTE_SCOPE_UNSPECIFIED: RouteInfo.RouteScope
    NETWORK: RouteInfo.RouteScope
    NCC_HUB: RouteInfo.RouteScope
    ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    DEST_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TAGS_FIELD_NUMBER: _ClassVar[int]
    SRC_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    DEST_PORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    SRC_PORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLS_FIELD_NUMBER: _ClassVar[int]
    NCC_HUB_URI_FIELD_NUMBER: _ClassVar[int]
    NCC_SPOKE_URI_FIELD_NUMBER: _ClassVar[int]
    ADVERTISED_ROUTE_SOURCE_ROUTER_URI_FIELD_NUMBER: _ClassVar[int]
    ADVERTISED_ROUTE_NEXT_HOP_URI_FIELD_NUMBER: _ClassVar[int]
    route_type: RouteInfo.RouteType
    next_hop_type: RouteInfo.NextHopType
    route_scope: RouteInfo.RouteScope
    display_name: str
    uri: str
    region: str
    dest_ip_range: str
    next_hop: str
    network_uri: str
    priority: int
    instance_tags: _containers.RepeatedScalarFieldContainer[str]
    src_ip_range: str
    dest_port_ranges: _containers.RepeatedScalarFieldContainer[str]
    src_port_ranges: _containers.RepeatedScalarFieldContainer[str]
    protocols: _containers.RepeatedScalarFieldContainer[str]
    ncc_hub_uri: str
    ncc_spoke_uri: str
    advertised_route_source_router_uri: str
    advertised_route_next_hop_uri: str
    def __init__(self, route_type: _Optional[_Union[RouteInfo.RouteType, str]] = ..., next_hop_type: _Optional[_Union[RouteInfo.NextHopType, str]] = ..., route_scope: _Optional[_Union[RouteInfo.RouteScope, str]] = ..., display_name: _Optional[str] = ..., uri: _Optional[str] = ..., region: _Optional[str] = ..., dest_ip_range: _Optional[str] = ..., next_hop: _Optional[str] = ..., network_uri: _Optional[str] = ..., priority: _Optional[int] = ..., instance_tags: _Optional[_Iterable[str]] = ..., src_ip_range: _Optional[str] = ..., dest_port_ranges: _Optional[_Iterable[str]] = ..., src_port_ranges: _Optional[_Iterable[str]] = ..., protocols: _Optional[_Iterable[str]] = ..., ncc_hub_uri: _Optional[str] = ..., ncc_spoke_uri: _Optional[str] = ..., advertised_route_source_router_uri: _Optional[str] = ..., advertised_route_next_hop_uri: _Optional[str] = ...) -> None: ...

class GoogleServiceInfo(_message.Message):
    __slots__ = ("source_ip", "google_service_type")
    class GoogleServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GOOGLE_SERVICE_TYPE_UNSPECIFIED: _ClassVar[GoogleServiceInfo.GoogleServiceType]
        IAP: _ClassVar[GoogleServiceInfo.GoogleServiceType]
        GFE_PROXY_OR_HEALTH_CHECK_PROBER: _ClassVar[GoogleServiceInfo.GoogleServiceType]
        CLOUD_DNS: _ClassVar[GoogleServiceInfo.GoogleServiceType]
        GOOGLE_API: _ClassVar[GoogleServiceInfo.GoogleServiceType]
        GOOGLE_API_PSC: _ClassVar[GoogleServiceInfo.GoogleServiceType]
        GOOGLE_API_VPC_SC: _ClassVar[GoogleServiceInfo.GoogleServiceType]
    GOOGLE_SERVICE_TYPE_UNSPECIFIED: GoogleServiceInfo.GoogleServiceType
    IAP: GoogleServiceInfo.GoogleServiceType
    GFE_PROXY_OR_HEALTH_CHECK_PROBER: GoogleServiceInfo.GoogleServiceType
    CLOUD_DNS: GoogleServiceInfo.GoogleServiceType
    GOOGLE_API: GoogleServiceInfo.GoogleServiceType
    GOOGLE_API_PSC: GoogleServiceInfo.GoogleServiceType
    GOOGLE_API_VPC_SC: GoogleServiceInfo.GoogleServiceType
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    source_ip: str
    google_service_type: GoogleServiceInfo.GoogleServiceType
    def __init__(self, source_ip: _Optional[str] = ..., google_service_type: _Optional[_Union[GoogleServiceInfo.GoogleServiceType, str]] = ...) -> None: ...

class ForwardingRuleInfo(_message.Message):
    __slots__ = ("display_name", "uri", "matched_protocol", "matched_port_range", "vip", "target", "network_uri", "region", "load_balancer_name", "psc_service_attachment_uri", "psc_google_api_target")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    MATCHED_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    MATCHED_PORT_RANGE_FIELD_NUMBER: _ClassVar[int]
    VIP_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_NAME_FIELD_NUMBER: _ClassVar[int]
    PSC_SERVICE_ATTACHMENT_URI_FIELD_NUMBER: _ClassVar[int]
    PSC_GOOGLE_API_TARGET_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    matched_protocol: str
    matched_port_range: str
    vip: str
    target: str
    network_uri: str
    region: str
    load_balancer_name: str
    psc_service_attachment_uri: str
    psc_google_api_target: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., matched_protocol: _Optional[str] = ..., matched_port_range: _Optional[str] = ..., vip: _Optional[str] = ..., target: _Optional[str] = ..., network_uri: _Optional[str] = ..., region: _Optional[str] = ..., load_balancer_name: _Optional[str] = ..., psc_service_attachment_uri: _Optional[str] = ..., psc_google_api_target: _Optional[str] = ...) -> None: ...

class LoadBalancerInfo(_message.Message):
    __slots__ = ("load_balancer_type", "health_check_uri", "backends", "backend_type", "backend_uri")
    class LoadBalancerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOAD_BALANCER_TYPE_UNSPECIFIED: _ClassVar[LoadBalancerInfo.LoadBalancerType]
        INTERNAL_TCP_UDP: _ClassVar[LoadBalancerInfo.LoadBalancerType]
        NETWORK_TCP_UDP: _ClassVar[LoadBalancerInfo.LoadBalancerType]
        HTTP_PROXY: _ClassVar[LoadBalancerInfo.LoadBalancerType]
        TCP_PROXY: _ClassVar[LoadBalancerInfo.LoadBalancerType]
        SSL_PROXY: _ClassVar[LoadBalancerInfo.LoadBalancerType]
    LOAD_BALANCER_TYPE_UNSPECIFIED: LoadBalancerInfo.LoadBalancerType
    INTERNAL_TCP_UDP: LoadBalancerInfo.LoadBalancerType
    NETWORK_TCP_UDP: LoadBalancerInfo.LoadBalancerType
    HTTP_PROXY: LoadBalancerInfo.LoadBalancerType
    TCP_PROXY: LoadBalancerInfo.LoadBalancerType
    SSL_PROXY: LoadBalancerInfo.LoadBalancerType
    class BackendType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BACKEND_TYPE_UNSPECIFIED: _ClassVar[LoadBalancerInfo.BackendType]
        BACKEND_SERVICE: _ClassVar[LoadBalancerInfo.BackendType]
        TARGET_POOL: _ClassVar[LoadBalancerInfo.BackendType]
        TARGET_INSTANCE: _ClassVar[LoadBalancerInfo.BackendType]
    BACKEND_TYPE_UNSPECIFIED: LoadBalancerInfo.BackendType
    BACKEND_SERVICE: LoadBalancerInfo.BackendType
    TARGET_POOL: LoadBalancerInfo.BackendType
    TARGET_INSTANCE: LoadBalancerInfo.BackendType
    LOAD_BALANCER_TYPE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_URI_FIELD_NUMBER: _ClassVar[int]
    BACKENDS_FIELD_NUMBER: _ClassVar[int]
    BACKEND_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKEND_URI_FIELD_NUMBER: _ClassVar[int]
    load_balancer_type: LoadBalancerInfo.LoadBalancerType
    health_check_uri: str
    backends: _containers.RepeatedCompositeFieldContainer[LoadBalancerBackend]
    backend_type: LoadBalancerInfo.BackendType
    backend_uri: str
    def __init__(self, load_balancer_type: _Optional[_Union[LoadBalancerInfo.LoadBalancerType, str]] = ..., health_check_uri: _Optional[str] = ..., backends: _Optional[_Iterable[_Union[LoadBalancerBackend, _Mapping]]] = ..., backend_type: _Optional[_Union[LoadBalancerInfo.BackendType, str]] = ..., backend_uri: _Optional[str] = ...) -> None: ...

class LoadBalancerBackend(_message.Message):
    __slots__ = ("display_name", "uri", "health_check_firewall_state", "health_check_allowing_firewall_rules", "health_check_blocking_firewall_rules")
    class HealthCheckFirewallState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED: _ClassVar[LoadBalancerBackend.HealthCheckFirewallState]
        CONFIGURED: _ClassVar[LoadBalancerBackend.HealthCheckFirewallState]
        MISCONFIGURED: _ClassVar[LoadBalancerBackend.HealthCheckFirewallState]
    HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED: LoadBalancerBackend.HealthCheckFirewallState
    CONFIGURED: LoadBalancerBackend.HealthCheckFirewallState
    MISCONFIGURED: LoadBalancerBackend.HealthCheckFirewallState
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_FIREWALL_STATE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_ALLOWING_FIREWALL_RULES_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_BLOCKING_FIREWALL_RULES_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    health_check_firewall_state: LoadBalancerBackend.HealthCheckFirewallState
    health_check_allowing_firewall_rules: _containers.RepeatedScalarFieldContainer[str]
    health_check_blocking_firewall_rules: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., health_check_firewall_state: _Optional[_Union[LoadBalancerBackend.HealthCheckFirewallState, str]] = ..., health_check_allowing_firewall_rules: _Optional[_Iterable[str]] = ..., health_check_blocking_firewall_rules: _Optional[_Iterable[str]] = ...) -> None: ...

class VpnGatewayInfo(_message.Message):
    __slots__ = ("display_name", "uri", "network_uri", "ip_address", "vpn_tunnel_uri", "region")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VPN_TUNNEL_URI_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    network_uri: str
    ip_address: str
    vpn_tunnel_uri: str
    region: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., network_uri: _Optional[str] = ..., ip_address: _Optional[str] = ..., vpn_tunnel_uri: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class VpnTunnelInfo(_message.Message):
    __slots__ = ("display_name", "uri", "source_gateway", "remote_gateway", "remote_gateway_ip", "source_gateway_ip", "network_uri", "region", "routing_type")
    class RoutingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROUTING_TYPE_UNSPECIFIED: _ClassVar[VpnTunnelInfo.RoutingType]
        ROUTE_BASED: _ClassVar[VpnTunnelInfo.RoutingType]
        POLICY_BASED: _ClassVar[VpnTunnelInfo.RoutingType]
        DYNAMIC: _ClassVar[VpnTunnelInfo.RoutingType]
    ROUTING_TYPE_UNSPECIFIED: VpnTunnelInfo.RoutingType
    ROUTE_BASED: VpnTunnelInfo.RoutingType
    POLICY_BASED: VpnTunnelInfo.RoutingType
    DYNAMIC: VpnTunnelInfo.RoutingType
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    REMOTE_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    REMOTE_GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ROUTING_TYPE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    source_gateway: str
    remote_gateway: str
    remote_gateway_ip: str
    source_gateway_ip: str
    network_uri: str
    region: str
    routing_type: VpnTunnelInfo.RoutingType
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., source_gateway: _Optional[str] = ..., remote_gateway: _Optional[str] = ..., remote_gateway_ip: _Optional[str] = ..., source_gateway_ip: _Optional[str] = ..., network_uri: _Optional[str] = ..., region: _Optional[str] = ..., routing_type: _Optional[_Union[VpnTunnelInfo.RoutingType, str]] = ...) -> None: ...

class EndpointInfo(_message.Message):
    __slots__ = ("source_ip", "destination_ip", "protocol", "source_port", "destination_port", "source_network_uri", "destination_network_uri", "source_agent_uri")
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IP_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_AGENT_URI_FIELD_NUMBER: _ClassVar[int]
    source_ip: str
    destination_ip: str
    protocol: str
    source_port: int
    destination_port: int
    source_network_uri: str
    destination_network_uri: str
    source_agent_uri: str
    def __init__(self, source_ip: _Optional[str] = ..., destination_ip: _Optional[str] = ..., protocol: _Optional[str] = ..., source_port: _Optional[int] = ..., destination_port: _Optional[int] = ..., source_network_uri: _Optional[str] = ..., destination_network_uri: _Optional[str] = ..., source_agent_uri: _Optional[str] = ...) -> None: ...

class DeliverInfo(_message.Message):
    __slots__ = ("target", "resource_uri", "ip_address", "storage_bucket", "psc_google_api_target")
    class Target(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARGET_UNSPECIFIED: _ClassVar[DeliverInfo.Target]
        INSTANCE: _ClassVar[DeliverInfo.Target]
        INTERNET: _ClassVar[DeliverInfo.Target]
        GOOGLE_API: _ClassVar[DeliverInfo.Target]
        GKE_MASTER: _ClassVar[DeliverInfo.Target]
        CLOUD_SQL_INSTANCE: _ClassVar[DeliverInfo.Target]
        PSC_PUBLISHED_SERVICE: _ClassVar[DeliverInfo.Target]
        PSC_GOOGLE_API: _ClassVar[DeliverInfo.Target]
        PSC_VPC_SC: _ClassVar[DeliverInfo.Target]
        SERVERLESS_NEG: _ClassVar[DeliverInfo.Target]
        STORAGE_BUCKET: _ClassVar[DeliverInfo.Target]
        PRIVATE_NETWORK: _ClassVar[DeliverInfo.Target]
        CLOUD_FUNCTION: _ClassVar[DeliverInfo.Target]
        APP_ENGINE_VERSION: _ClassVar[DeliverInfo.Target]
        CLOUD_RUN_REVISION: _ClassVar[DeliverInfo.Target]
        GOOGLE_MANAGED_SERVICE: _ClassVar[DeliverInfo.Target]
        REDIS_INSTANCE: _ClassVar[DeliverInfo.Target]
        REDIS_CLUSTER: _ClassVar[DeliverInfo.Target]
    TARGET_UNSPECIFIED: DeliverInfo.Target
    INSTANCE: DeliverInfo.Target
    INTERNET: DeliverInfo.Target
    GOOGLE_API: DeliverInfo.Target
    GKE_MASTER: DeliverInfo.Target
    CLOUD_SQL_INSTANCE: DeliverInfo.Target
    PSC_PUBLISHED_SERVICE: DeliverInfo.Target
    PSC_GOOGLE_API: DeliverInfo.Target
    PSC_VPC_SC: DeliverInfo.Target
    SERVERLESS_NEG: DeliverInfo.Target
    STORAGE_BUCKET: DeliverInfo.Target
    PRIVATE_NETWORK: DeliverInfo.Target
    CLOUD_FUNCTION: DeliverInfo.Target
    APP_ENGINE_VERSION: DeliverInfo.Target
    CLOUD_RUN_REVISION: DeliverInfo.Target
    GOOGLE_MANAGED_SERVICE: DeliverInfo.Target
    REDIS_INSTANCE: DeliverInfo.Target
    REDIS_CLUSTER: DeliverInfo.Target
    TARGET_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    PSC_GOOGLE_API_TARGET_FIELD_NUMBER: _ClassVar[int]
    target: DeliverInfo.Target
    resource_uri: str
    ip_address: str
    storage_bucket: str
    psc_google_api_target: str
    def __init__(self, target: _Optional[_Union[DeliverInfo.Target, str]] = ..., resource_uri: _Optional[str] = ..., ip_address: _Optional[str] = ..., storage_bucket: _Optional[str] = ..., psc_google_api_target: _Optional[str] = ...) -> None: ...

class ForwardInfo(_message.Message):
    __slots__ = ("target", "resource_uri", "ip_address")
    class Target(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARGET_UNSPECIFIED: _ClassVar[ForwardInfo.Target]
        PEERING_VPC: _ClassVar[ForwardInfo.Target]
        VPN_GATEWAY: _ClassVar[ForwardInfo.Target]
        INTERCONNECT: _ClassVar[ForwardInfo.Target]
        GKE_MASTER: _ClassVar[ForwardInfo.Target]
        IMPORTED_CUSTOM_ROUTE_NEXT_HOP: _ClassVar[ForwardInfo.Target]
        CLOUD_SQL_INSTANCE: _ClassVar[ForwardInfo.Target]
        ANOTHER_PROJECT: _ClassVar[ForwardInfo.Target]
        NCC_HUB: _ClassVar[ForwardInfo.Target]
        ROUTER_APPLIANCE: _ClassVar[ForwardInfo.Target]
    TARGET_UNSPECIFIED: ForwardInfo.Target
    PEERING_VPC: ForwardInfo.Target
    VPN_GATEWAY: ForwardInfo.Target
    INTERCONNECT: ForwardInfo.Target
    GKE_MASTER: ForwardInfo.Target
    IMPORTED_CUSTOM_ROUTE_NEXT_HOP: ForwardInfo.Target
    CLOUD_SQL_INSTANCE: ForwardInfo.Target
    ANOTHER_PROJECT: ForwardInfo.Target
    NCC_HUB: ForwardInfo.Target
    ROUTER_APPLIANCE: ForwardInfo.Target
    TARGET_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    target: ForwardInfo.Target
    resource_uri: str
    ip_address: str
    def __init__(self, target: _Optional[_Union[ForwardInfo.Target, str]] = ..., resource_uri: _Optional[str] = ..., ip_address: _Optional[str] = ...) -> None: ...

class AbortInfo(_message.Message):
    __slots__ = ("cause", "resource_uri", "ip_address", "projects_missing_permission")
    class Cause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAUSE_UNSPECIFIED: _ClassVar[AbortInfo.Cause]
        UNKNOWN_NETWORK: _ClassVar[AbortInfo.Cause]
        UNKNOWN_PROJECT: _ClassVar[AbortInfo.Cause]
        NO_EXTERNAL_IP: _ClassVar[AbortInfo.Cause]
        UNINTENDED_DESTINATION: _ClassVar[AbortInfo.Cause]
        SOURCE_ENDPOINT_NOT_FOUND: _ClassVar[AbortInfo.Cause]
        MISMATCHED_SOURCE_NETWORK: _ClassVar[AbortInfo.Cause]
        DESTINATION_ENDPOINT_NOT_FOUND: _ClassVar[AbortInfo.Cause]
        MISMATCHED_DESTINATION_NETWORK: _ClassVar[AbortInfo.Cause]
        UNKNOWN_IP: _ClassVar[AbortInfo.Cause]
        GOOGLE_MANAGED_SERVICE_UNKNOWN_IP: _ClassVar[AbortInfo.Cause]
        SOURCE_IP_ADDRESS_NOT_IN_SOURCE_NETWORK: _ClassVar[AbortInfo.Cause]
        PERMISSION_DENIED: _ClassVar[AbortInfo.Cause]
        PERMISSION_DENIED_NO_CLOUD_NAT_CONFIGS: _ClassVar[AbortInfo.Cause]
        PERMISSION_DENIED_NO_NEG_ENDPOINT_CONFIGS: _ClassVar[AbortInfo.Cause]
        PERMISSION_DENIED_NO_CLOUD_ROUTER_CONFIGS: _ClassVar[AbortInfo.Cause]
        NO_SOURCE_LOCATION: _ClassVar[AbortInfo.Cause]
        INVALID_ARGUMENT: _ClassVar[AbortInfo.Cause]
        TRACE_TOO_LONG: _ClassVar[AbortInfo.Cause]
        INTERNAL_ERROR: _ClassVar[AbortInfo.Cause]
        UNSUPPORTED: _ClassVar[AbortInfo.Cause]
        MISMATCHED_IP_VERSION: _ClassVar[AbortInfo.Cause]
        GKE_KONNECTIVITY_PROXY_UNSUPPORTED: _ClassVar[AbortInfo.Cause]
        RESOURCE_CONFIG_NOT_FOUND: _ClassVar[AbortInfo.Cause]
        VM_INSTANCE_CONFIG_NOT_FOUND: _ClassVar[AbortInfo.Cause]
        NETWORK_CONFIG_NOT_FOUND: _ClassVar[AbortInfo.Cause]
        FIREWALL_CONFIG_NOT_FOUND: _ClassVar[AbortInfo.Cause]
        ROUTE_CONFIG_NOT_FOUND: _ClassVar[AbortInfo.Cause]
        GOOGLE_MANAGED_SERVICE_AMBIGUOUS_PSC_ENDPOINT: _ClassVar[AbortInfo.Cause]
        SOURCE_PSC_CLOUD_SQL_UNSUPPORTED: _ClassVar[AbortInfo.Cause]
        SOURCE_REDIS_CLUSTER_UNSUPPORTED: _ClassVar[AbortInfo.Cause]
        SOURCE_REDIS_INSTANCE_UNSUPPORTED: _ClassVar[AbortInfo.Cause]
        SOURCE_FORWARDING_RULE_UNSUPPORTED: _ClassVar[AbortInfo.Cause]
        NON_ROUTABLE_IP_ADDRESS: _ClassVar[AbortInfo.Cause]
        UNKNOWN_ISSUE_IN_GOOGLE_MANAGED_PROJECT: _ClassVar[AbortInfo.Cause]
        UNSUPPORTED_GOOGLE_MANAGED_PROJECT_CONFIG: _ClassVar[AbortInfo.Cause]
    CAUSE_UNSPECIFIED: AbortInfo.Cause
    UNKNOWN_NETWORK: AbortInfo.Cause
    UNKNOWN_PROJECT: AbortInfo.Cause
    NO_EXTERNAL_IP: AbortInfo.Cause
    UNINTENDED_DESTINATION: AbortInfo.Cause
    SOURCE_ENDPOINT_NOT_FOUND: AbortInfo.Cause
    MISMATCHED_SOURCE_NETWORK: AbortInfo.Cause
    DESTINATION_ENDPOINT_NOT_FOUND: AbortInfo.Cause
    MISMATCHED_DESTINATION_NETWORK: AbortInfo.Cause
    UNKNOWN_IP: AbortInfo.Cause
    GOOGLE_MANAGED_SERVICE_UNKNOWN_IP: AbortInfo.Cause
    SOURCE_IP_ADDRESS_NOT_IN_SOURCE_NETWORK: AbortInfo.Cause
    PERMISSION_DENIED: AbortInfo.Cause
    PERMISSION_DENIED_NO_CLOUD_NAT_CONFIGS: AbortInfo.Cause
    PERMISSION_DENIED_NO_NEG_ENDPOINT_CONFIGS: AbortInfo.Cause
    PERMISSION_DENIED_NO_CLOUD_ROUTER_CONFIGS: AbortInfo.Cause
    NO_SOURCE_LOCATION: AbortInfo.Cause
    INVALID_ARGUMENT: AbortInfo.Cause
    TRACE_TOO_LONG: AbortInfo.Cause
    INTERNAL_ERROR: AbortInfo.Cause
    UNSUPPORTED: AbortInfo.Cause
    MISMATCHED_IP_VERSION: AbortInfo.Cause
    GKE_KONNECTIVITY_PROXY_UNSUPPORTED: AbortInfo.Cause
    RESOURCE_CONFIG_NOT_FOUND: AbortInfo.Cause
    VM_INSTANCE_CONFIG_NOT_FOUND: AbortInfo.Cause
    NETWORK_CONFIG_NOT_FOUND: AbortInfo.Cause
    FIREWALL_CONFIG_NOT_FOUND: AbortInfo.Cause
    ROUTE_CONFIG_NOT_FOUND: AbortInfo.Cause
    GOOGLE_MANAGED_SERVICE_AMBIGUOUS_PSC_ENDPOINT: AbortInfo.Cause
    SOURCE_PSC_CLOUD_SQL_UNSUPPORTED: AbortInfo.Cause
    SOURCE_REDIS_CLUSTER_UNSUPPORTED: AbortInfo.Cause
    SOURCE_REDIS_INSTANCE_UNSUPPORTED: AbortInfo.Cause
    SOURCE_FORWARDING_RULE_UNSUPPORTED: AbortInfo.Cause
    NON_ROUTABLE_IP_ADDRESS: AbortInfo.Cause
    UNKNOWN_ISSUE_IN_GOOGLE_MANAGED_PROJECT: AbortInfo.Cause
    UNSUPPORTED_GOOGLE_MANAGED_PROJECT_CONFIG: AbortInfo.Cause
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROJECTS_MISSING_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    cause: AbortInfo.Cause
    resource_uri: str
    ip_address: str
    projects_missing_permission: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cause: _Optional[_Union[AbortInfo.Cause, str]] = ..., resource_uri: _Optional[str] = ..., ip_address: _Optional[str] = ..., projects_missing_permission: _Optional[_Iterable[str]] = ...) -> None: ...

class DropInfo(_message.Message):
    __slots__ = ("cause", "resource_uri", "source_ip", "destination_ip", "region")
    class Cause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAUSE_UNSPECIFIED: _ClassVar[DropInfo.Cause]
        UNKNOWN_EXTERNAL_ADDRESS: _ClassVar[DropInfo.Cause]
        FOREIGN_IP_DISALLOWED: _ClassVar[DropInfo.Cause]
        FIREWALL_RULE: _ClassVar[DropInfo.Cause]
        NO_ROUTE: _ClassVar[DropInfo.Cause]
        ROUTE_BLACKHOLE: _ClassVar[DropInfo.Cause]
        ROUTE_WRONG_NETWORK: _ClassVar[DropInfo.Cause]
        ROUTE_NEXT_HOP_IP_ADDRESS_NOT_RESOLVED: _ClassVar[DropInfo.Cause]
        ROUTE_NEXT_HOP_RESOURCE_NOT_FOUND: _ClassVar[DropInfo.Cause]
        ROUTE_NEXT_HOP_INSTANCE_WRONG_NETWORK: _ClassVar[DropInfo.Cause]
        ROUTE_NEXT_HOP_INSTANCE_NON_PRIMARY_IP: _ClassVar[DropInfo.Cause]
        ROUTE_NEXT_HOP_FORWARDING_RULE_IP_MISMATCH: _ClassVar[DropInfo.Cause]
        ROUTE_NEXT_HOP_VPN_TUNNEL_NOT_ESTABLISHED: _ClassVar[DropInfo.Cause]
        ROUTE_NEXT_HOP_FORWARDING_RULE_TYPE_INVALID: _ClassVar[DropInfo.Cause]
        NO_ROUTE_FROM_INTERNET_TO_PRIVATE_IPV6_ADDRESS: _ClassVar[DropInfo.Cause]
        VPN_TUNNEL_LOCAL_SELECTOR_MISMATCH: _ClassVar[DropInfo.Cause]
        VPN_TUNNEL_REMOTE_SELECTOR_MISMATCH: _ClassVar[DropInfo.Cause]
        PRIVATE_TRAFFIC_TO_INTERNET: _ClassVar[DropInfo.Cause]
        PRIVATE_GOOGLE_ACCESS_DISALLOWED: _ClassVar[DropInfo.Cause]
        PRIVATE_GOOGLE_ACCESS_VIA_VPN_TUNNEL_UNSUPPORTED: _ClassVar[DropInfo.Cause]
        NO_EXTERNAL_ADDRESS: _ClassVar[DropInfo.Cause]
        UNKNOWN_INTERNAL_ADDRESS: _ClassVar[DropInfo.Cause]
        FORWARDING_RULE_MISMATCH: _ClassVar[DropInfo.Cause]
        FORWARDING_RULE_NO_INSTANCES: _ClassVar[DropInfo.Cause]
        FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK: _ClassVar[DropInfo.Cause]
        INSTANCE_NOT_RUNNING: _ClassVar[DropInfo.Cause]
        GKE_CLUSTER_NOT_RUNNING: _ClassVar[DropInfo.Cause]
        CLOUD_SQL_INSTANCE_NOT_RUNNING: _ClassVar[DropInfo.Cause]
        REDIS_INSTANCE_NOT_RUNNING: _ClassVar[DropInfo.Cause]
        REDIS_CLUSTER_NOT_RUNNING: _ClassVar[DropInfo.Cause]
        TRAFFIC_TYPE_BLOCKED: _ClassVar[DropInfo.Cause]
        GKE_MASTER_UNAUTHORIZED_ACCESS: _ClassVar[DropInfo.Cause]
        CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS: _ClassVar[DropInfo.Cause]
        DROPPED_INSIDE_GKE_SERVICE: _ClassVar[DropInfo.Cause]
        DROPPED_INSIDE_CLOUD_SQL_SERVICE: _ClassVar[DropInfo.Cause]
        GOOGLE_MANAGED_SERVICE_NO_PEERING: _ClassVar[DropInfo.Cause]
        GOOGLE_MANAGED_SERVICE_NO_PSC_ENDPOINT: _ClassVar[DropInfo.Cause]
        GKE_PSC_ENDPOINT_MISSING: _ClassVar[DropInfo.Cause]
        CLOUD_SQL_INSTANCE_NO_IP_ADDRESS: _ClassVar[DropInfo.Cause]
        GKE_CONTROL_PLANE_REGION_MISMATCH: _ClassVar[DropInfo.Cause]
        PUBLIC_GKE_CONTROL_PLANE_TO_PRIVATE_DESTINATION: _ClassVar[DropInfo.Cause]
        GKE_CONTROL_PLANE_NO_ROUTE: _ClassVar[DropInfo.Cause]
        CLOUD_SQL_INSTANCE_NOT_CONFIGURED_FOR_EXTERNAL_TRAFFIC: _ClassVar[DropInfo.Cause]
        PUBLIC_CLOUD_SQL_INSTANCE_TO_PRIVATE_DESTINATION: _ClassVar[DropInfo.Cause]
        CLOUD_SQL_INSTANCE_NO_ROUTE: _ClassVar[DropInfo.Cause]
        CLOUD_SQL_CONNECTOR_REQUIRED: _ClassVar[DropInfo.Cause]
        CLOUD_FUNCTION_NOT_ACTIVE: _ClassVar[DropInfo.Cause]
        VPC_CONNECTOR_NOT_SET: _ClassVar[DropInfo.Cause]
        VPC_CONNECTOR_NOT_RUNNING: _ClassVar[DropInfo.Cause]
        VPC_CONNECTOR_SERVERLESS_TRAFFIC_BLOCKED: _ClassVar[DropInfo.Cause]
        VPC_CONNECTOR_HEALTH_CHECK_TRAFFIC_BLOCKED: _ClassVar[DropInfo.Cause]
        FORWARDING_RULE_REGION_MISMATCH: _ClassVar[DropInfo.Cause]
        PSC_CONNECTION_NOT_ACCEPTED: _ClassVar[DropInfo.Cause]
        PSC_ENDPOINT_ACCESSED_FROM_PEERED_NETWORK: _ClassVar[DropInfo.Cause]
        PSC_NEG_PRODUCER_ENDPOINT_NO_GLOBAL_ACCESS: _ClassVar[DropInfo.Cause]
        PSC_NEG_PRODUCER_FORWARDING_RULE_MULTIPLE_PORTS: _ClassVar[DropInfo.Cause]
        CLOUD_SQL_PSC_NEG_UNSUPPORTED: _ClassVar[DropInfo.Cause]
        NO_NAT_SUBNETS_FOR_PSC_SERVICE_ATTACHMENT: _ClassVar[DropInfo.Cause]
        PSC_TRANSITIVITY_NOT_PROPAGATED: _ClassVar[DropInfo.Cause]
        HYBRID_NEG_NON_DYNAMIC_ROUTE_MATCHED: _ClassVar[DropInfo.Cause]
        HYBRID_NEG_NON_LOCAL_DYNAMIC_ROUTE_MATCHED: _ClassVar[DropInfo.Cause]
        CLOUD_RUN_REVISION_NOT_READY: _ClassVar[DropInfo.Cause]
        DROPPED_INSIDE_PSC_SERVICE_PRODUCER: _ClassVar[DropInfo.Cause]
        LOAD_BALANCER_HAS_NO_PROXY_SUBNET: _ClassVar[DropInfo.Cause]
        CLOUD_NAT_NO_ADDRESSES: _ClassVar[DropInfo.Cause]
        ROUTING_LOOP: _ClassVar[DropInfo.Cause]
        DROPPED_INSIDE_GOOGLE_MANAGED_SERVICE: _ClassVar[DropInfo.Cause]
        LOAD_BALANCER_BACKEND_INVALID_NETWORK: _ClassVar[DropInfo.Cause]
        BACKEND_SERVICE_NAMED_PORT_NOT_DEFINED: _ClassVar[DropInfo.Cause]
        DESTINATION_IS_PRIVATE_NAT_IP_RANGE: _ClassVar[DropInfo.Cause]
        DROPPED_INSIDE_REDIS_INSTANCE_SERVICE: _ClassVar[DropInfo.Cause]
        REDIS_INSTANCE_UNSUPPORTED_PORT: _ClassVar[DropInfo.Cause]
        REDIS_INSTANCE_CONNECTING_FROM_PUPI_ADDRESS: _ClassVar[DropInfo.Cause]
        REDIS_INSTANCE_NO_ROUTE_TO_DESTINATION_NETWORK: _ClassVar[DropInfo.Cause]
        REDIS_INSTANCE_NO_EXTERNAL_IP: _ClassVar[DropInfo.Cause]
        REDIS_INSTANCE_UNSUPPORTED_PROTOCOL: _ClassVar[DropInfo.Cause]
        DROPPED_INSIDE_REDIS_CLUSTER_SERVICE: _ClassVar[DropInfo.Cause]
        REDIS_CLUSTER_UNSUPPORTED_PORT: _ClassVar[DropInfo.Cause]
        REDIS_CLUSTER_NO_EXTERNAL_IP: _ClassVar[DropInfo.Cause]
        REDIS_CLUSTER_UNSUPPORTED_PROTOCOL: _ClassVar[DropInfo.Cause]
        NO_ADVERTISED_ROUTE_TO_GCP_DESTINATION: _ClassVar[DropInfo.Cause]
        NO_TRAFFIC_SELECTOR_TO_GCP_DESTINATION: _ClassVar[DropInfo.Cause]
        NO_KNOWN_ROUTE_FROM_PEERED_NETWORK_TO_DESTINATION: _ClassVar[DropInfo.Cause]
        PRIVATE_NAT_TO_PSC_ENDPOINT_UNSUPPORTED: _ClassVar[DropInfo.Cause]
    CAUSE_UNSPECIFIED: DropInfo.Cause
    UNKNOWN_EXTERNAL_ADDRESS: DropInfo.Cause
    FOREIGN_IP_DISALLOWED: DropInfo.Cause
    FIREWALL_RULE: DropInfo.Cause
    NO_ROUTE: DropInfo.Cause
    ROUTE_BLACKHOLE: DropInfo.Cause
    ROUTE_WRONG_NETWORK: DropInfo.Cause
    ROUTE_NEXT_HOP_IP_ADDRESS_NOT_RESOLVED: DropInfo.Cause
    ROUTE_NEXT_HOP_RESOURCE_NOT_FOUND: DropInfo.Cause
    ROUTE_NEXT_HOP_INSTANCE_WRONG_NETWORK: DropInfo.Cause
    ROUTE_NEXT_HOP_INSTANCE_NON_PRIMARY_IP: DropInfo.Cause
    ROUTE_NEXT_HOP_FORWARDING_RULE_IP_MISMATCH: DropInfo.Cause
    ROUTE_NEXT_HOP_VPN_TUNNEL_NOT_ESTABLISHED: DropInfo.Cause
    ROUTE_NEXT_HOP_FORWARDING_RULE_TYPE_INVALID: DropInfo.Cause
    NO_ROUTE_FROM_INTERNET_TO_PRIVATE_IPV6_ADDRESS: DropInfo.Cause
    VPN_TUNNEL_LOCAL_SELECTOR_MISMATCH: DropInfo.Cause
    VPN_TUNNEL_REMOTE_SELECTOR_MISMATCH: DropInfo.Cause
    PRIVATE_TRAFFIC_TO_INTERNET: DropInfo.Cause
    PRIVATE_GOOGLE_ACCESS_DISALLOWED: DropInfo.Cause
    PRIVATE_GOOGLE_ACCESS_VIA_VPN_TUNNEL_UNSUPPORTED: DropInfo.Cause
    NO_EXTERNAL_ADDRESS: DropInfo.Cause
    UNKNOWN_INTERNAL_ADDRESS: DropInfo.Cause
    FORWARDING_RULE_MISMATCH: DropInfo.Cause
    FORWARDING_RULE_NO_INSTANCES: DropInfo.Cause
    FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK: DropInfo.Cause
    INSTANCE_NOT_RUNNING: DropInfo.Cause
    GKE_CLUSTER_NOT_RUNNING: DropInfo.Cause
    CLOUD_SQL_INSTANCE_NOT_RUNNING: DropInfo.Cause
    REDIS_INSTANCE_NOT_RUNNING: DropInfo.Cause
    REDIS_CLUSTER_NOT_RUNNING: DropInfo.Cause
    TRAFFIC_TYPE_BLOCKED: DropInfo.Cause
    GKE_MASTER_UNAUTHORIZED_ACCESS: DropInfo.Cause
    CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS: DropInfo.Cause
    DROPPED_INSIDE_GKE_SERVICE: DropInfo.Cause
    DROPPED_INSIDE_CLOUD_SQL_SERVICE: DropInfo.Cause
    GOOGLE_MANAGED_SERVICE_NO_PEERING: DropInfo.Cause
    GOOGLE_MANAGED_SERVICE_NO_PSC_ENDPOINT: DropInfo.Cause
    GKE_PSC_ENDPOINT_MISSING: DropInfo.Cause
    CLOUD_SQL_INSTANCE_NO_IP_ADDRESS: DropInfo.Cause
    GKE_CONTROL_PLANE_REGION_MISMATCH: DropInfo.Cause
    PUBLIC_GKE_CONTROL_PLANE_TO_PRIVATE_DESTINATION: DropInfo.Cause
    GKE_CONTROL_PLANE_NO_ROUTE: DropInfo.Cause
    CLOUD_SQL_INSTANCE_NOT_CONFIGURED_FOR_EXTERNAL_TRAFFIC: DropInfo.Cause
    PUBLIC_CLOUD_SQL_INSTANCE_TO_PRIVATE_DESTINATION: DropInfo.Cause
    CLOUD_SQL_INSTANCE_NO_ROUTE: DropInfo.Cause
    CLOUD_SQL_CONNECTOR_REQUIRED: DropInfo.Cause
    CLOUD_FUNCTION_NOT_ACTIVE: DropInfo.Cause
    VPC_CONNECTOR_NOT_SET: DropInfo.Cause
    VPC_CONNECTOR_NOT_RUNNING: DropInfo.Cause
    VPC_CONNECTOR_SERVERLESS_TRAFFIC_BLOCKED: DropInfo.Cause
    VPC_CONNECTOR_HEALTH_CHECK_TRAFFIC_BLOCKED: DropInfo.Cause
    FORWARDING_RULE_REGION_MISMATCH: DropInfo.Cause
    PSC_CONNECTION_NOT_ACCEPTED: DropInfo.Cause
    PSC_ENDPOINT_ACCESSED_FROM_PEERED_NETWORK: DropInfo.Cause
    PSC_NEG_PRODUCER_ENDPOINT_NO_GLOBAL_ACCESS: DropInfo.Cause
    PSC_NEG_PRODUCER_FORWARDING_RULE_MULTIPLE_PORTS: DropInfo.Cause
    CLOUD_SQL_PSC_NEG_UNSUPPORTED: DropInfo.Cause
    NO_NAT_SUBNETS_FOR_PSC_SERVICE_ATTACHMENT: DropInfo.Cause
    PSC_TRANSITIVITY_NOT_PROPAGATED: DropInfo.Cause
    HYBRID_NEG_NON_DYNAMIC_ROUTE_MATCHED: DropInfo.Cause
    HYBRID_NEG_NON_LOCAL_DYNAMIC_ROUTE_MATCHED: DropInfo.Cause
    CLOUD_RUN_REVISION_NOT_READY: DropInfo.Cause
    DROPPED_INSIDE_PSC_SERVICE_PRODUCER: DropInfo.Cause
    LOAD_BALANCER_HAS_NO_PROXY_SUBNET: DropInfo.Cause
    CLOUD_NAT_NO_ADDRESSES: DropInfo.Cause
    ROUTING_LOOP: DropInfo.Cause
    DROPPED_INSIDE_GOOGLE_MANAGED_SERVICE: DropInfo.Cause
    LOAD_BALANCER_BACKEND_INVALID_NETWORK: DropInfo.Cause
    BACKEND_SERVICE_NAMED_PORT_NOT_DEFINED: DropInfo.Cause
    DESTINATION_IS_PRIVATE_NAT_IP_RANGE: DropInfo.Cause
    DROPPED_INSIDE_REDIS_INSTANCE_SERVICE: DropInfo.Cause
    REDIS_INSTANCE_UNSUPPORTED_PORT: DropInfo.Cause
    REDIS_INSTANCE_CONNECTING_FROM_PUPI_ADDRESS: DropInfo.Cause
    REDIS_INSTANCE_NO_ROUTE_TO_DESTINATION_NETWORK: DropInfo.Cause
    REDIS_INSTANCE_NO_EXTERNAL_IP: DropInfo.Cause
    REDIS_INSTANCE_UNSUPPORTED_PROTOCOL: DropInfo.Cause
    DROPPED_INSIDE_REDIS_CLUSTER_SERVICE: DropInfo.Cause
    REDIS_CLUSTER_UNSUPPORTED_PORT: DropInfo.Cause
    REDIS_CLUSTER_NO_EXTERNAL_IP: DropInfo.Cause
    REDIS_CLUSTER_UNSUPPORTED_PROTOCOL: DropInfo.Cause
    NO_ADVERTISED_ROUTE_TO_GCP_DESTINATION: DropInfo.Cause
    NO_TRAFFIC_SELECTOR_TO_GCP_DESTINATION: DropInfo.Cause
    NO_KNOWN_ROUTE_FROM_PEERED_NETWORK_TO_DESTINATION: DropInfo.Cause
    PRIVATE_NAT_TO_PSC_ENDPOINT_UNSUPPORTED: DropInfo.Cause
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IP_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    cause: DropInfo.Cause
    resource_uri: str
    source_ip: str
    destination_ip: str
    region: str
    def __init__(self, cause: _Optional[_Union[DropInfo.Cause, str]] = ..., resource_uri: _Optional[str] = ..., source_ip: _Optional[str] = ..., destination_ip: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class GKEMasterInfo(_message.Message):
    __slots__ = ("cluster_uri", "cluster_network_uri", "internal_ip", "external_ip", "dns_endpoint")
    CLUSTER_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    DNS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    cluster_uri: str
    cluster_network_uri: str
    internal_ip: str
    external_ip: str
    dns_endpoint: str
    def __init__(self, cluster_uri: _Optional[str] = ..., cluster_network_uri: _Optional[str] = ..., internal_ip: _Optional[str] = ..., external_ip: _Optional[str] = ..., dns_endpoint: _Optional[str] = ...) -> None: ...

class CloudSQLInstanceInfo(_message.Message):
    __slots__ = ("display_name", "uri", "network_uri", "internal_ip", "external_ip", "region")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    network_uri: str
    internal_ip: str
    external_ip: str
    region: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., network_uri: _Optional[str] = ..., internal_ip: _Optional[str] = ..., external_ip: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class RedisInstanceInfo(_message.Message):
    __slots__ = ("display_name", "uri", "network_uri", "primary_endpoint_ip", "read_endpoint_ip", "region")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_ENDPOINT_IP_FIELD_NUMBER: _ClassVar[int]
    READ_ENDPOINT_IP_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    network_uri: str
    primary_endpoint_ip: str
    read_endpoint_ip: str
    region: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., network_uri: _Optional[str] = ..., primary_endpoint_ip: _Optional[str] = ..., read_endpoint_ip: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class RedisClusterInfo(_message.Message):
    __slots__ = ("display_name", "uri", "network_uri", "discovery_endpoint_ip_address", "secondary_endpoint_ip_address", "location")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_ENDPOINT_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_ENDPOINT_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    network_uri: str
    discovery_endpoint_ip_address: str
    secondary_endpoint_ip_address: str
    location: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., network_uri: _Optional[str] = ..., discovery_endpoint_ip_address: _Optional[str] = ..., secondary_endpoint_ip_address: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class CloudFunctionInfo(_message.Message):
    __slots__ = ("display_name", "uri", "location", "version_id")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    location: str
    version_id: int
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., location: _Optional[str] = ..., version_id: _Optional[int] = ...) -> None: ...

class CloudRunRevisionInfo(_message.Message):
    __slots__ = ("display_name", "uri", "location", "service_uri")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_URI_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    location: str
    service_uri: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., location: _Optional[str] = ..., service_uri: _Optional[str] = ...) -> None: ...

class AppEngineVersionInfo(_message.Message):
    __slots__ = ("display_name", "uri", "runtime", "environment")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    runtime: str
    environment: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., runtime: _Optional[str] = ..., environment: _Optional[str] = ...) -> None: ...

class VpcConnectorInfo(_message.Message):
    __slots__ = ("display_name", "uri", "location")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    location: str
    def __init__(self, display_name: _Optional[str] = ..., uri: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class NatInfo(_message.Message):
    __slots__ = ("type", "protocol", "network_uri", "old_source_ip", "new_source_ip", "old_destination_ip", "new_destination_ip", "old_source_port", "new_source_port", "old_destination_port", "new_destination_port", "router_uri", "nat_gateway_name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[NatInfo.Type]
        INTERNAL_TO_EXTERNAL: _ClassVar[NatInfo.Type]
        EXTERNAL_TO_INTERNAL: _ClassVar[NatInfo.Type]
        CLOUD_NAT: _ClassVar[NatInfo.Type]
        PRIVATE_SERVICE_CONNECT: _ClassVar[NatInfo.Type]
    TYPE_UNSPECIFIED: NatInfo.Type
    INTERNAL_TO_EXTERNAL: NatInfo.Type
    EXTERNAL_TO_INTERNAL: NatInfo.Type
    CLOUD_NAT: NatInfo.Type
    PRIVATE_SERVICE_CONNECT: NatInfo.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    OLD_SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    NEW_SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    OLD_DESTINATION_IP_FIELD_NUMBER: _ClassVar[int]
    NEW_DESTINATION_IP_FIELD_NUMBER: _ClassVar[int]
    OLD_SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    NEW_SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    OLD_DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    NEW_DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    ROUTER_URI_FIELD_NUMBER: _ClassVar[int]
    NAT_GATEWAY_NAME_FIELD_NUMBER: _ClassVar[int]
    type: NatInfo.Type
    protocol: str
    network_uri: str
    old_source_ip: str
    new_source_ip: str
    old_destination_ip: str
    new_destination_ip: str
    old_source_port: int
    new_source_port: int
    old_destination_port: int
    new_destination_port: int
    router_uri: str
    nat_gateway_name: str
    def __init__(self, type: _Optional[_Union[NatInfo.Type, str]] = ..., protocol: _Optional[str] = ..., network_uri: _Optional[str] = ..., old_source_ip: _Optional[str] = ..., new_source_ip: _Optional[str] = ..., old_destination_ip: _Optional[str] = ..., new_destination_ip: _Optional[str] = ..., old_source_port: _Optional[int] = ..., new_source_port: _Optional[int] = ..., old_destination_port: _Optional[int] = ..., new_destination_port: _Optional[int] = ..., router_uri: _Optional[str] = ..., nat_gateway_name: _Optional[str] = ...) -> None: ...

class ProxyConnectionInfo(_message.Message):
    __slots__ = ("protocol", "old_source_ip", "new_source_ip", "old_destination_ip", "new_destination_ip", "old_source_port", "new_source_port", "old_destination_port", "new_destination_port", "subnet_uri", "network_uri")
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    OLD_SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    NEW_SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    OLD_DESTINATION_IP_FIELD_NUMBER: _ClassVar[int]
    NEW_DESTINATION_IP_FIELD_NUMBER: _ClassVar[int]
    OLD_SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    NEW_SOURCE_PORT_FIELD_NUMBER: _ClassVar[int]
    OLD_DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    NEW_DESTINATION_PORT_FIELD_NUMBER: _ClassVar[int]
    SUBNET_URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    protocol: str
    old_source_ip: str
    new_source_ip: str
    old_destination_ip: str
    new_destination_ip: str
    old_source_port: int
    new_source_port: int
    old_destination_port: int
    new_destination_port: int
    subnet_uri: str
    network_uri: str
    def __init__(self, protocol: _Optional[str] = ..., old_source_ip: _Optional[str] = ..., new_source_ip: _Optional[str] = ..., old_destination_ip: _Optional[str] = ..., new_destination_ip: _Optional[str] = ..., old_source_port: _Optional[int] = ..., new_source_port: _Optional[int] = ..., old_destination_port: _Optional[int] = ..., new_destination_port: _Optional[int] = ..., subnet_uri: _Optional[str] = ..., network_uri: _Optional[str] = ...) -> None: ...

class LoadBalancerBackendInfo(_message.Message):
    __slots__ = ("name", "instance_uri", "backend_service_uri", "instance_group_uri", "network_endpoint_group_uri", "backend_bucket_uri", "psc_service_attachment_uri", "psc_google_api_target", "health_check_uri", "health_check_firewalls_config_state")
    class HealthCheckFirewallsConfigState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED: _ClassVar[LoadBalancerBackendInfo.HealthCheckFirewallsConfigState]
        FIREWALLS_CONFIGURED: _ClassVar[LoadBalancerBackendInfo.HealthCheckFirewallsConfigState]
        FIREWALLS_PARTIALLY_CONFIGURED: _ClassVar[LoadBalancerBackendInfo.HealthCheckFirewallsConfigState]
        FIREWALLS_NOT_CONFIGURED: _ClassVar[LoadBalancerBackendInfo.HealthCheckFirewallsConfigState]
        FIREWALLS_UNSUPPORTED: _ClassVar[LoadBalancerBackendInfo.HealthCheckFirewallsConfigState]
    HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED: LoadBalancerBackendInfo.HealthCheckFirewallsConfigState
    FIREWALLS_CONFIGURED: LoadBalancerBackendInfo.HealthCheckFirewallsConfigState
    FIREWALLS_PARTIALLY_CONFIGURED: LoadBalancerBackendInfo.HealthCheckFirewallsConfigState
    FIREWALLS_NOT_CONFIGURED: LoadBalancerBackendInfo.HealthCheckFirewallsConfigState
    FIREWALLS_UNSUPPORTED: LoadBalancerBackendInfo.HealthCheckFirewallsConfigState
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_URI_FIELD_NUMBER: _ClassVar[int]
    BACKEND_SERVICE_URI_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_GROUP_URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ENDPOINT_GROUP_URI_FIELD_NUMBER: _ClassVar[int]
    BACKEND_BUCKET_URI_FIELD_NUMBER: _ClassVar[int]
    PSC_SERVICE_ATTACHMENT_URI_FIELD_NUMBER: _ClassVar[int]
    PSC_GOOGLE_API_TARGET_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_URI_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_FIREWALLS_CONFIG_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    instance_uri: str
    backend_service_uri: str
    instance_group_uri: str
    network_endpoint_group_uri: str
    backend_bucket_uri: str
    psc_service_attachment_uri: str
    psc_google_api_target: str
    health_check_uri: str
    health_check_firewalls_config_state: LoadBalancerBackendInfo.HealthCheckFirewallsConfigState
    def __init__(self, name: _Optional[str] = ..., instance_uri: _Optional[str] = ..., backend_service_uri: _Optional[str] = ..., instance_group_uri: _Optional[str] = ..., network_endpoint_group_uri: _Optional[str] = ..., backend_bucket_uri: _Optional[str] = ..., psc_service_attachment_uri: _Optional[str] = ..., psc_google_api_target: _Optional[str] = ..., health_check_uri: _Optional[str] = ..., health_check_firewalls_config_state: _Optional[_Union[LoadBalancerBackendInfo.HealthCheckFirewallsConfigState, str]] = ...) -> None: ...

class StorageBucketInfo(_message.Message):
    __slots__ = ("bucket",)
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    def __init__(self, bucket: _Optional[str] = ...) -> None: ...

class ServerlessNegInfo(_message.Message):
    __slots__ = ("neg_uri",)
    NEG_URI_FIELD_NUMBER: _ClassVar[int]
    neg_uri: str
    def __init__(self, neg_uri: _Optional[str] = ...) -> None: ...
