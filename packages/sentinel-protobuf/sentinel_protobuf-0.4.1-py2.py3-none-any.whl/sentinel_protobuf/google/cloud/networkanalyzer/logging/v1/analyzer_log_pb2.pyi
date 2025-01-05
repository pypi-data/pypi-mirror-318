from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReportCauseCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_CAUSE_CODE_UNSPECIFIED: _ClassVar[ReportCauseCode]
    ROUTE_INVALID_NEXT_HOP_VM_IP_FORWARDING_DISABLED: _ClassVar[ReportCauseCode]
    ROUTE_INVALID_NEXT_HOP_VM_DELETED: _ClassVar[ReportCauseCode]
    ROUTE_INVALID_NEXT_HOP_VM_STOPPED: _ClassVar[ReportCauseCode]
    ROUTE_INVALID_NEXT_HOP_ILB_MISCONFIGURED: _ClassVar[ReportCauseCode]
    ROUTE_INVALID_NEXT_HOP_VPN_TUNNEL_DELETED: _ClassVar[ReportCauseCode]
    ROUTE_INVALID_NEXT_HOP_ILB_BACKEND_IP_FORWARDING_DISABLED: _ClassVar[ReportCauseCode]
    ROUTE_INVALID_NEXT_HOP_ILB_VIP_NOT_ASSIGNED: _ClassVar[ReportCauseCode]
    IP_UTILIZATION_IP_ALLOCATION_RATIO_HIGH: _ClassVar[ReportCauseCode]
    IP_UTILIZATION_IP_ALLOCATION_SUMMARY: _ClassVar[ReportCauseCode]
    GKE_NODE_TO_CONTROL_PLANE_BLOCKED_BY_ROUTING_ISSUE: _ClassVar[ReportCauseCode]
    GKE_NODE_TO_CONTROL_PLANE_PUBLIC_ENDPOINT_BLOCKED_BY_EGRESS_FIREWALL: _ClassVar[ReportCauseCode]
    GKE_NODE_TO_CONTROL_PLANE_PRIVATE_ENDPOINT_BLOCKED_BY_EGRESS_FIREWALL: _ClassVar[ReportCauseCode]
    GKE_CONTROL_PLANE_TO_NODE_BLOCKED_BY_ROUTING_ISSUE: _ClassVar[ReportCauseCode]
    GKE_CONTROL_PLANE_TO_NODE_BLOCKED_BY_INGRESS_FIREWALL_ON_NODE: _ClassVar[ReportCauseCode]
    GKE_IP_UTILIZATION_POD_RANGES_ALLOCATION_HIGH: _ClassVar[ReportCauseCode]
    GKE_IP_UTILIZATION_POD_RANGES_ALLOCATION_LIMITES_AUTOSCALING: _ClassVar[ReportCauseCode]
    GKE_NODE_SERVICE_ACCOUNT_SERVICE_ACCOUNT_DISABLED: _ClassVar[ReportCauseCode]
    GKE_NODE_SERVICE_ACCOUNT_DEFAULT_SERVICE_ACCOUNT_USED: _ClassVar[ReportCauseCode]
    GKE_NODE_SERVICE_ACCOUNT_BAD_OAUTH_SCOPES: _ClassVar[ReportCauseCode]
    CLOUD_SQL_PRIVATE_IP_BLOCKED_BY_EGRESS_FIREWALL: _ClassVar[ReportCauseCode]
    CLOUD_SQL_PRIVATE_IP_BLOCKED_BY_ROUTING_ISSUE: _ClassVar[ReportCauseCode]
    CLOUD_SQL_PRIVATE_IP_INSTANCE_NOT_RUNNING: _ClassVar[ReportCauseCode]
    DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_SUBNET_ROUTE: _ClassVar[ReportCauseCode]
    DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_PEERING_SUBNET_ROUTE: _ClassVar[ReportCauseCode]
    DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_STATIC_ROUTE: _ClassVar[ReportCauseCode]
    DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_PEERING_STATIC_ROUTE: _ClassVar[ReportCauseCode]
    DYNAMIC_ROUTE_SHADOWED_PARTIALLY_SHADOWED_BY_SUBNET_ROUTE: _ClassVar[ReportCauseCode]
    DYNAMIC_ROUTE_SHADOWED_PARTIALLY_SHADOWED_BY_PEERING_SUBNET_ROUTE: _ClassVar[ReportCauseCode]
    DYNAMIC_ROUTE_SHADOWED_PARTIALLY_SHADOWED_BY_STATIC_ROUTE: _ClassVar[ReportCauseCode]
    DYNAMIC_ROUTE_SHADOWED_PARTIALLY_SHADOWED_BY_PEERING_STATIC_ROUTE: _ClassVar[ReportCauseCode]
    LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_FIREWALL_NOT_CONFIGURED: _ClassVar[ReportCauseCode]
    LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_RANGE_BLOCKED: _ClassVar[ReportCauseCode]
    LOAD_BALANCER_HEALTH_CHECK_FIREWALL_FIREWALL_CONFIG_INCONSISTENT: _ClassVar[ReportCauseCode]
    LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_RANGE_PARTIALLY_BLOCKED: _ClassVar[ReportCauseCode]
    LOAD_BALANCER_BEST_PRACTICES_BACKEND_SERVICE_BALANCING_MODE_BREAKS_SESSION_AFFINITY: _ClassVar[ReportCauseCode]
    LOAD_BALANCER_BEST_PRACTICES_BACKEND_SERVICE_HEALTH_CHECK_PORT_MISMATCH: _ClassVar[ReportCauseCode]
REPORT_CAUSE_CODE_UNSPECIFIED: ReportCauseCode
ROUTE_INVALID_NEXT_HOP_VM_IP_FORWARDING_DISABLED: ReportCauseCode
ROUTE_INVALID_NEXT_HOP_VM_DELETED: ReportCauseCode
ROUTE_INVALID_NEXT_HOP_VM_STOPPED: ReportCauseCode
ROUTE_INVALID_NEXT_HOP_ILB_MISCONFIGURED: ReportCauseCode
ROUTE_INVALID_NEXT_HOP_VPN_TUNNEL_DELETED: ReportCauseCode
ROUTE_INVALID_NEXT_HOP_ILB_BACKEND_IP_FORWARDING_DISABLED: ReportCauseCode
ROUTE_INVALID_NEXT_HOP_ILB_VIP_NOT_ASSIGNED: ReportCauseCode
IP_UTILIZATION_IP_ALLOCATION_RATIO_HIGH: ReportCauseCode
IP_UTILIZATION_IP_ALLOCATION_SUMMARY: ReportCauseCode
GKE_NODE_TO_CONTROL_PLANE_BLOCKED_BY_ROUTING_ISSUE: ReportCauseCode
GKE_NODE_TO_CONTROL_PLANE_PUBLIC_ENDPOINT_BLOCKED_BY_EGRESS_FIREWALL: ReportCauseCode
GKE_NODE_TO_CONTROL_PLANE_PRIVATE_ENDPOINT_BLOCKED_BY_EGRESS_FIREWALL: ReportCauseCode
GKE_CONTROL_PLANE_TO_NODE_BLOCKED_BY_ROUTING_ISSUE: ReportCauseCode
GKE_CONTROL_PLANE_TO_NODE_BLOCKED_BY_INGRESS_FIREWALL_ON_NODE: ReportCauseCode
GKE_IP_UTILIZATION_POD_RANGES_ALLOCATION_HIGH: ReportCauseCode
GKE_IP_UTILIZATION_POD_RANGES_ALLOCATION_LIMITES_AUTOSCALING: ReportCauseCode
GKE_NODE_SERVICE_ACCOUNT_SERVICE_ACCOUNT_DISABLED: ReportCauseCode
GKE_NODE_SERVICE_ACCOUNT_DEFAULT_SERVICE_ACCOUNT_USED: ReportCauseCode
GKE_NODE_SERVICE_ACCOUNT_BAD_OAUTH_SCOPES: ReportCauseCode
CLOUD_SQL_PRIVATE_IP_BLOCKED_BY_EGRESS_FIREWALL: ReportCauseCode
CLOUD_SQL_PRIVATE_IP_BLOCKED_BY_ROUTING_ISSUE: ReportCauseCode
CLOUD_SQL_PRIVATE_IP_INSTANCE_NOT_RUNNING: ReportCauseCode
DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_SUBNET_ROUTE: ReportCauseCode
DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_PEERING_SUBNET_ROUTE: ReportCauseCode
DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_STATIC_ROUTE: ReportCauseCode
DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_PEERING_STATIC_ROUTE: ReportCauseCode
DYNAMIC_ROUTE_SHADOWED_PARTIALLY_SHADOWED_BY_SUBNET_ROUTE: ReportCauseCode
DYNAMIC_ROUTE_SHADOWED_PARTIALLY_SHADOWED_BY_PEERING_SUBNET_ROUTE: ReportCauseCode
DYNAMIC_ROUTE_SHADOWED_PARTIALLY_SHADOWED_BY_STATIC_ROUTE: ReportCauseCode
DYNAMIC_ROUTE_SHADOWED_PARTIALLY_SHADOWED_BY_PEERING_STATIC_ROUTE: ReportCauseCode
LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_FIREWALL_NOT_CONFIGURED: ReportCauseCode
LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_RANGE_BLOCKED: ReportCauseCode
LOAD_BALANCER_HEALTH_CHECK_FIREWALL_FIREWALL_CONFIG_INCONSISTENT: ReportCauseCode
LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_RANGE_PARTIALLY_BLOCKED: ReportCauseCode
LOAD_BALANCER_BEST_PRACTICES_BACKEND_SERVICE_BALANCING_MODE_BREAKS_SESSION_AFFINITY: ReportCauseCode
LOAD_BALANCER_BEST_PRACTICES_BACKEND_SERVICE_HEALTH_CHECK_PORT_MISMATCH: ReportCauseCode

class IpUtilizationInfo(_message.Message):
    __slots__ = ('subnet_ip_utilization',)

    class SubnetIpUtilization(_message.Message):
        __slots__ = ('subnet_uri', 'secondary_range_name', 'total_usable_addresses', 'allocation_ratio')
        SUBNET_URI_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_RANGE_NAME_FIELD_NUMBER: _ClassVar[int]
        TOTAL_USABLE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        ALLOCATION_RATIO_FIELD_NUMBER: _ClassVar[int]
        subnet_uri: str
        secondary_range_name: str
        total_usable_addresses: int
        allocation_ratio: float

        def __init__(self, subnet_uri: _Optional[str]=..., secondary_range_name: _Optional[str]=..., total_usable_addresses: _Optional[int]=..., allocation_ratio: _Optional[float]=...) -> None:
            ...
    SUBNET_IP_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    subnet_ip_utilization: _containers.RepeatedCompositeFieldContainer[IpUtilizationInfo.SubnetIpUtilization]

    def __init__(self, subnet_ip_utilization: _Optional[_Iterable[_Union[IpUtilizationInfo.SubnetIpUtilization, _Mapping]]]=...) -> None:
        ...

class Report(_message.Message):
    __slots__ = ('id', 'priority', 'type', 'status', 'first_report_time', 'cause_code', 'resource_name', 'location', 'report_documentation_uri', 'report_groups', 'ip_utilization_info')

    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[Report.Priority]
        CRITICAL: _ClassVar[Report.Priority]
        HIGH: _ClassVar[Report.Priority]
        MEDIUM: _ClassVar[Report.Priority]
        LOW: _ClassVar[Report.Priority]
    SEVERITY_UNSPECIFIED: Report.Priority
    CRITICAL: Report.Priority
    HIGH: Report.Priority
    MEDIUM: Report.Priority
    LOW: Report.Priority

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPORT_TYPE_UNSPECIFIED: _ClassVar[Report.Type]
        INFO: _ClassVar[Report.Type]
        WARNING: _ClassVar[Report.Type]
        ERROR: _ClassVar[Report.Type]
    REPORT_TYPE_UNSPECIFIED: Report.Type
    INFO: Report.Type
    WARNING: Report.Type
    ERROR: Report.Type

    class ReportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPORT_STATUS_UNSPECIFIED: _ClassVar[Report.ReportStatus]
        ACTIVE: _ClassVar[Report.ReportStatus]
        FIXED: _ClassVar[Report.ReportStatus]
        DISMISSED: _ClassVar[Report.ReportStatus]
    REPORT_STATUS_UNSPECIFIED: Report.ReportStatus
    ACTIVE: Report.ReportStatus
    FIXED: Report.ReportStatus
    DISMISSED: Report.ReportStatus

    class ReportGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATEGORY_UNSPECIFIED: _ClassVar[Report.ReportGroup]
        VPC_NETWORK: _ClassVar[Report.ReportGroup]
        NETWORK_SERVICES: _ClassVar[Report.ReportGroup]
        KUBERNETES_ENGINE: _ClassVar[Report.ReportGroup]
        HYBRID_CONNECTIVITY: _ClassVar[Report.ReportGroup]
        MANAGED_SERVICES: _ClassVar[Report.ReportGroup]
    CATEGORY_UNSPECIFIED: Report.ReportGroup
    VPC_NETWORK: Report.ReportGroup
    NETWORK_SERVICES: Report.ReportGroup
    KUBERNETES_ENGINE: Report.ReportGroup
    HYBRID_CONNECTIVITY: Report.ReportGroup
    MANAGED_SERVICES: Report.ReportGroup
    ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FIRST_REPORT_TIME_FIELD_NUMBER: _ClassVar[int]
    CAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    REPORT_DOCUMENTATION_URI_FIELD_NUMBER: _ClassVar[int]
    REPORT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    IP_UTILIZATION_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    priority: Report.Priority
    type: Report.Type
    status: Report.ReportStatus
    first_report_time: _timestamp_pb2.Timestamp
    cause_code: ReportCauseCode
    resource_name: str
    location: str
    report_documentation_uri: str
    report_groups: _containers.RepeatedScalarFieldContainer[Report.ReportGroup]
    ip_utilization_info: IpUtilizationInfo

    def __init__(self, id: _Optional[str]=..., priority: _Optional[_Union[Report.Priority, str]]=..., type: _Optional[_Union[Report.Type, str]]=..., status: _Optional[_Union[Report.ReportStatus, str]]=..., first_report_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cause_code: _Optional[_Union[ReportCauseCode, str]]=..., resource_name: _Optional[str]=..., location: _Optional[str]=..., report_documentation_uri: _Optional[str]=..., report_groups: _Optional[_Iterable[_Union[Report.ReportGroup, str]]]=..., ip_utilization_info: _Optional[_Union[IpUtilizationInfo, _Mapping]]=...) -> None:
        ...