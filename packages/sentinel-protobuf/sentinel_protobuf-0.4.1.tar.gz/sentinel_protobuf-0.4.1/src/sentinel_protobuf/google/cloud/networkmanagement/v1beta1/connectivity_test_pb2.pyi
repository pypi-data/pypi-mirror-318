from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networkmanagement.v1beta1 import trace_pb2 as _trace_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectivityTest(_message.Message):
    __slots__ = ("name", "description", "source", "destination", "protocol", "related_projects", "display_name", "labels", "create_time", "update_time", "reachability_details", "probing_details", "round_trip", "return_reachability_details", "bypass_firewall_checks")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    RELATED_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REACHABILITY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PROBING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ROUND_TRIP_FIELD_NUMBER: _ClassVar[int]
    RETURN_REACHABILITY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BYPASS_FIREWALL_CHECKS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source: Endpoint
    destination: Endpoint
    protocol: str
    related_projects: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    reachability_details: ReachabilityDetails
    probing_details: ProbingDetails
    round_trip: bool
    return_reachability_details: ReachabilityDetails
    bypass_firewall_checks: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., source: _Optional[_Union[Endpoint, _Mapping]] = ..., destination: _Optional[_Union[Endpoint, _Mapping]] = ..., protocol: _Optional[str] = ..., related_projects: _Optional[_Iterable[str]] = ..., display_name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reachability_details: _Optional[_Union[ReachabilityDetails, _Mapping]] = ..., probing_details: _Optional[_Union[ProbingDetails, _Mapping]] = ..., round_trip: bool = ..., return_reachability_details: _Optional[_Union[ReachabilityDetails, _Mapping]] = ..., bypass_firewall_checks: bool = ...) -> None: ...

class Endpoint(_message.Message):
    __slots__ = ("ip_address", "port", "instance", "forwarding_rule", "forwarding_rule_target", "load_balancer_id", "load_balancer_type", "gke_master_cluster", "fqdn", "cloud_sql_instance", "redis_instance", "redis_cluster", "cloud_function", "app_engine_version", "cloud_run_revision", "network", "network_type", "project_id")
    class NetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NETWORK_TYPE_UNSPECIFIED: _ClassVar[Endpoint.NetworkType]
        GCP_NETWORK: _ClassVar[Endpoint.NetworkType]
        NON_GCP_NETWORK: _ClassVar[Endpoint.NetworkType]
    NETWORK_TYPE_UNSPECIFIED: Endpoint.NetworkType
    GCP_NETWORK: Endpoint.NetworkType
    NON_GCP_NETWORK: Endpoint.NetworkType
    class ForwardingRuleTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORWARDING_RULE_TARGET_UNSPECIFIED: _ClassVar[Endpoint.ForwardingRuleTarget]
        INSTANCE: _ClassVar[Endpoint.ForwardingRuleTarget]
        LOAD_BALANCER: _ClassVar[Endpoint.ForwardingRuleTarget]
        VPN_GATEWAY: _ClassVar[Endpoint.ForwardingRuleTarget]
        PSC: _ClassVar[Endpoint.ForwardingRuleTarget]
    FORWARDING_RULE_TARGET_UNSPECIFIED: Endpoint.ForwardingRuleTarget
    INSTANCE: Endpoint.ForwardingRuleTarget
    LOAD_BALANCER: Endpoint.ForwardingRuleTarget
    VPN_GATEWAY: Endpoint.ForwardingRuleTarget
    PSC: Endpoint.ForwardingRuleTarget
    class CloudFunctionEndpoint(_message.Message):
        __slots__ = ("uri",)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str
        def __init__(self, uri: _Optional[str] = ...) -> None: ...
    class AppEngineVersionEndpoint(_message.Message):
        __slots__ = ("uri",)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str
        def __init__(self, uri: _Optional[str] = ...) -> None: ...
    class CloudRunRevisionEndpoint(_message.Message):
        __slots__ = ("uri",)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str
        def __init__(self, uri: _Optional[str] = ...) -> None: ...
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULE_TARGET_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_ID_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_TYPE_FIELD_NUMBER: _ClassVar[int]
    GKE_MASTER_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REDIS_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REDIS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RUN_REVISION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    port: int
    instance: str
    forwarding_rule: str
    forwarding_rule_target: Endpoint.ForwardingRuleTarget
    load_balancer_id: str
    load_balancer_type: _trace_pb2.LoadBalancerType
    gke_master_cluster: str
    fqdn: str
    cloud_sql_instance: str
    redis_instance: str
    redis_cluster: str
    cloud_function: Endpoint.CloudFunctionEndpoint
    app_engine_version: Endpoint.AppEngineVersionEndpoint
    cloud_run_revision: Endpoint.CloudRunRevisionEndpoint
    network: str
    network_type: Endpoint.NetworkType
    project_id: str
    def __init__(self, ip_address: _Optional[str] = ..., port: _Optional[int] = ..., instance: _Optional[str] = ..., forwarding_rule: _Optional[str] = ..., forwarding_rule_target: _Optional[_Union[Endpoint.ForwardingRuleTarget, str]] = ..., load_balancer_id: _Optional[str] = ..., load_balancer_type: _Optional[_Union[_trace_pb2.LoadBalancerType, str]] = ..., gke_master_cluster: _Optional[str] = ..., fqdn: _Optional[str] = ..., cloud_sql_instance: _Optional[str] = ..., redis_instance: _Optional[str] = ..., redis_cluster: _Optional[str] = ..., cloud_function: _Optional[_Union[Endpoint.CloudFunctionEndpoint, _Mapping]] = ..., app_engine_version: _Optional[_Union[Endpoint.AppEngineVersionEndpoint, _Mapping]] = ..., cloud_run_revision: _Optional[_Union[Endpoint.CloudRunRevisionEndpoint, _Mapping]] = ..., network: _Optional[str] = ..., network_type: _Optional[_Union[Endpoint.NetworkType, str]] = ..., project_id: _Optional[str] = ...) -> None: ...

class ReachabilityDetails(_message.Message):
    __slots__ = ("result", "verify_time", "error", "traces")
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESULT_UNSPECIFIED: _ClassVar[ReachabilityDetails.Result]
        REACHABLE: _ClassVar[ReachabilityDetails.Result]
        UNREACHABLE: _ClassVar[ReachabilityDetails.Result]
        AMBIGUOUS: _ClassVar[ReachabilityDetails.Result]
        UNDETERMINED: _ClassVar[ReachabilityDetails.Result]
    RESULT_UNSPECIFIED: ReachabilityDetails.Result
    REACHABLE: ReachabilityDetails.Result
    UNREACHABLE: ReachabilityDetails.Result
    AMBIGUOUS: ReachabilityDetails.Result
    UNDETERMINED: ReachabilityDetails.Result
    RESULT_FIELD_NUMBER: _ClassVar[int]
    VERIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TRACES_FIELD_NUMBER: _ClassVar[int]
    result: ReachabilityDetails.Result
    verify_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    traces: _containers.RepeatedCompositeFieldContainer[_trace_pb2.Trace]
    def __init__(self, result: _Optional[_Union[ReachabilityDetails.Result, str]] = ..., verify_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., traces: _Optional[_Iterable[_Union[_trace_pb2.Trace, _Mapping]]] = ...) -> None: ...

class LatencyPercentile(_message.Message):
    __slots__ = ("percent", "latency_micros")
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MICROS_FIELD_NUMBER: _ClassVar[int]
    percent: int
    latency_micros: int
    def __init__(self, percent: _Optional[int] = ..., latency_micros: _Optional[int] = ...) -> None: ...

class LatencyDistribution(_message.Message):
    __slots__ = ("latency_percentiles",)
    LATENCY_PERCENTILES_FIELD_NUMBER: _ClassVar[int]
    latency_percentiles: _containers.RepeatedCompositeFieldContainer[LatencyPercentile]
    def __init__(self, latency_percentiles: _Optional[_Iterable[_Union[LatencyPercentile, _Mapping]]] = ...) -> None: ...

class ProbingDetails(_message.Message):
    __slots__ = ("result", "verify_time", "error", "abort_cause", "sent_probe_count", "successful_probe_count", "endpoint_info", "probing_latency", "destination_egress_location")
    class ProbingResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROBING_RESULT_UNSPECIFIED: _ClassVar[ProbingDetails.ProbingResult]
        REACHABLE: _ClassVar[ProbingDetails.ProbingResult]
        UNREACHABLE: _ClassVar[ProbingDetails.ProbingResult]
        REACHABILITY_INCONSISTENT: _ClassVar[ProbingDetails.ProbingResult]
        UNDETERMINED: _ClassVar[ProbingDetails.ProbingResult]
    PROBING_RESULT_UNSPECIFIED: ProbingDetails.ProbingResult
    REACHABLE: ProbingDetails.ProbingResult
    UNREACHABLE: ProbingDetails.ProbingResult
    REACHABILITY_INCONSISTENT: ProbingDetails.ProbingResult
    UNDETERMINED: ProbingDetails.ProbingResult
    class ProbingAbortCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROBING_ABORT_CAUSE_UNSPECIFIED: _ClassVar[ProbingDetails.ProbingAbortCause]
        PERMISSION_DENIED: _ClassVar[ProbingDetails.ProbingAbortCause]
        NO_SOURCE_LOCATION: _ClassVar[ProbingDetails.ProbingAbortCause]
    PROBING_ABORT_CAUSE_UNSPECIFIED: ProbingDetails.ProbingAbortCause
    PERMISSION_DENIED: ProbingDetails.ProbingAbortCause
    NO_SOURCE_LOCATION: ProbingDetails.ProbingAbortCause
    class EdgeLocation(_message.Message):
        __slots__ = ("metropolitan_area",)
        METROPOLITAN_AREA_FIELD_NUMBER: _ClassVar[int]
        metropolitan_area: str
        def __init__(self, metropolitan_area: _Optional[str] = ...) -> None: ...
    RESULT_FIELD_NUMBER: _ClassVar[int]
    VERIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ABORT_CAUSE_FIELD_NUMBER: _ClassVar[int]
    SENT_PROBE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_PROBE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    PROBING_LATENCY_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_EGRESS_LOCATION_FIELD_NUMBER: _ClassVar[int]
    result: ProbingDetails.ProbingResult
    verify_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    abort_cause: ProbingDetails.ProbingAbortCause
    sent_probe_count: int
    successful_probe_count: int
    endpoint_info: _trace_pb2.EndpointInfo
    probing_latency: LatencyDistribution
    destination_egress_location: ProbingDetails.EdgeLocation
    def __init__(self, result: _Optional[_Union[ProbingDetails.ProbingResult, str]] = ..., verify_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., abort_cause: _Optional[_Union[ProbingDetails.ProbingAbortCause, str]] = ..., sent_probe_count: _Optional[int] = ..., successful_probe_count: _Optional[int] = ..., endpoint_info: _Optional[_Union[_trace_pb2.EndpointInfo, _Mapping]] = ..., probing_latency: _Optional[_Union[LatencyDistribution, _Mapping]] = ..., destination_egress_location: _Optional[_Union[ProbingDetails.EdgeLocation, _Mapping]] = ...) -> None: ...
