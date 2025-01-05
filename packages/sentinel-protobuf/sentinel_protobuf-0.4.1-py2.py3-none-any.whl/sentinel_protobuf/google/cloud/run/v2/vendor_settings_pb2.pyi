from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IngressTraffic(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INGRESS_TRAFFIC_UNSPECIFIED: _ClassVar[IngressTraffic]
    INGRESS_TRAFFIC_ALL: _ClassVar[IngressTraffic]
    INGRESS_TRAFFIC_INTERNAL_ONLY: _ClassVar[IngressTraffic]
    INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER: _ClassVar[IngressTraffic]
    INGRESS_TRAFFIC_NONE: _ClassVar[IngressTraffic]

class ExecutionEnvironment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_ENVIRONMENT_UNSPECIFIED: _ClassVar[ExecutionEnvironment]
    EXECUTION_ENVIRONMENT_GEN1: _ClassVar[ExecutionEnvironment]
    EXECUTION_ENVIRONMENT_GEN2: _ClassVar[ExecutionEnvironment]

class EncryptionKeyRevocationAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED: _ClassVar[EncryptionKeyRevocationAction]
    PREVENT_NEW: _ClassVar[EncryptionKeyRevocationAction]
    SHUTDOWN: _ClassVar[EncryptionKeyRevocationAction]
INGRESS_TRAFFIC_UNSPECIFIED: IngressTraffic
INGRESS_TRAFFIC_ALL: IngressTraffic
INGRESS_TRAFFIC_INTERNAL_ONLY: IngressTraffic
INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER: IngressTraffic
INGRESS_TRAFFIC_NONE: IngressTraffic
EXECUTION_ENVIRONMENT_UNSPECIFIED: ExecutionEnvironment
EXECUTION_ENVIRONMENT_GEN1: ExecutionEnvironment
EXECUTION_ENVIRONMENT_GEN2: ExecutionEnvironment
ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED: EncryptionKeyRevocationAction
PREVENT_NEW: EncryptionKeyRevocationAction
SHUTDOWN: EncryptionKeyRevocationAction

class VpcAccess(_message.Message):
    __slots__ = ("connector", "egress", "network_interfaces")
    class VpcEgress(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VPC_EGRESS_UNSPECIFIED: _ClassVar[VpcAccess.VpcEgress]
        ALL_TRAFFIC: _ClassVar[VpcAccess.VpcEgress]
        PRIVATE_RANGES_ONLY: _ClassVar[VpcAccess.VpcEgress]
    VPC_EGRESS_UNSPECIFIED: VpcAccess.VpcEgress
    ALL_TRAFFIC: VpcAccess.VpcEgress
    PRIVATE_RANGES_ONLY: VpcAccess.VpcEgress
    class NetworkInterface(_message.Message):
        __slots__ = ("network", "subnetwork", "tags")
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        network: str
        subnetwork: str
        tags: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, network: _Optional[str] = ..., subnetwork: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    EGRESS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    connector: str
    egress: VpcAccess.VpcEgress
    network_interfaces: _containers.RepeatedCompositeFieldContainer[VpcAccess.NetworkInterface]
    def __init__(self, connector: _Optional[str] = ..., egress: _Optional[_Union[VpcAccess.VpcEgress, str]] = ..., network_interfaces: _Optional[_Iterable[_Union[VpcAccess.NetworkInterface, _Mapping]]] = ...) -> None: ...

class BinaryAuthorization(_message.Message):
    __slots__ = ("use_default", "policy", "breakglass_justification")
    USE_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    BREAKGLASS_JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
    use_default: bool
    policy: str
    breakglass_justification: str
    def __init__(self, use_default: bool = ..., policy: _Optional[str] = ..., breakglass_justification: _Optional[str] = ...) -> None: ...

class RevisionScaling(_message.Message):
    __slots__ = ("min_instance_count", "max_instance_count")
    MIN_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_instance_count: int
    max_instance_count: int
    def __init__(self, min_instance_count: _Optional[int] = ..., max_instance_count: _Optional[int] = ...) -> None: ...

class ServiceMesh(_message.Message):
    __slots__ = ("mesh",)
    MESH_FIELD_NUMBER: _ClassVar[int]
    mesh: str
    def __init__(self, mesh: _Optional[str] = ...) -> None: ...

class ServiceScaling(_message.Message):
    __slots__ = ("min_instance_count", "scaling_mode", "manual_instance_count")
    class ScalingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCALING_MODE_UNSPECIFIED: _ClassVar[ServiceScaling.ScalingMode]
        AUTOMATIC: _ClassVar[ServiceScaling.ScalingMode]
        MANUAL: _ClassVar[ServiceScaling.ScalingMode]
    SCALING_MODE_UNSPECIFIED: ServiceScaling.ScalingMode
    AUTOMATIC: ServiceScaling.ScalingMode
    MANUAL: ServiceScaling.ScalingMode
    MIN_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCALING_MODE_FIELD_NUMBER: _ClassVar[int]
    MANUAL_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_instance_count: int
    scaling_mode: ServiceScaling.ScalingMode
    manual_instance_count: int
    def __init__(self, min_instance_count: _Optional[int] = ..., scaling_mode: _Optional[_Union[ServiceScaling.ScalingMode, str]] = ..., manual_instance_count: _Optional[int] = ...) -> None: ...

class NodeSelector(_message.Message):
    __slots__ = ("accelerator",)
    ACCELERATOR_FIELD_NUMBER: _ClassVar[int]
    accelerator: str
    def __init__(self, accelerator: _Optional[str] = ...) -> None: ...
