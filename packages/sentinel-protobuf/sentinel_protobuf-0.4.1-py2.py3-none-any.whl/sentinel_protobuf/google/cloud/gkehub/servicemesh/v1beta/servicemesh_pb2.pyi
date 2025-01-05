from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MembershipSpec(_message.Message):
    __slots__ = ('control_plane', 'management')

    class ControlPlaneManagement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTROL_PLANE_MANAGEMENT_UNSPECIFIED: _ClassVar[MembershipSpec.ControlPlaneManagement]
        AUTOMATIC: _ClassVar[MembershipSpec.ControlPlaneManagement]
        MANUAL: _ClassVar[MembershipSpec.ControlPlaneManagement]
    CONTROL_PLANE_MANAGEMENT_UNSPECIFIED: MembershipSpec.ControlPlaneManagement
    AUTOMATIC: MembershipSpec.ControlPlaneManagement
    MANUAL: MembershipSpec.ControlPlaneManagement

    class Management(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANAGEMENT_UNSPECIFIED: _ClassVar[MembershipSpec.Management]
        MANAGEMENT_AUTOMATIC: _ClassVar[MembershipSpec.Management]
        MANAGEMENT_MANUAL: _ClassVar[MembershipSpec.Management]
    MANAGEMENT_UNSPECIFIED: MembershipSpec.Management
    MANAGEMENT_AUTOMATIC: MembershipSpec.Management
    MANAGEMENT_MANUAL: MembershipSpec.Management
    CONTROL_PLANE_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    control_plane: MembershipSpec.ControlPlaneManagement
    management: MembershipSpec.Management

    def __init__(self, control_plane: _Optional[_Union[MembershipSpec.ControlPlaneManagement, str]]=..., management: _Optional[_Union[MembershipSpec.Management, str]]=...) -> None:
        ...

class MembershipState(_message.Message):
    __slots__ = ('control_plane_management', 'data_plane_management', 'conditions')

    class LifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[MembershipState.LifecycleState]
        DISABLED: _ClassVar[MembershipState.LifecycleState]
        FAILED_PRECONDITION: _ClassVar[MembershipState.LifecycleState]
        PROVISIONING: _ClassVar[MembershipState.LifecycleState]
        ACTIVE: _ClassVar[MembershipState.LifecycleState]
        STALLED: _ClassVar[MembershipState.LifecycleState]
        NEEDS_ATTENTION: _ClassVar[MembershipState.LifecycleState]
        DEGRADED: _ClassVar[MembershipState.LifecycleState]
    LIFECYCLE_STATE_UNSPECIFIED: MembershipState.LifecycleState
    DISABLED: MembershipState.LifecycleState
    FAILED_PRECONDITION: MembershipState.LifecycleState
    PROVISIONING: MembershipState.LifecycleState
    ACTIVE: MembershipState.LifecycleState
    STALLED: MembershipState.LifecycleState
    NEEDS_ATTENTION: MembershipState.LifecycleState
    DEGRADED: MembershipState.LifecycleState

    class ControlPlaneManagement(_message.Message):
        __slots__ = ('details', 'state', 'implementation')

        class Implementation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            IMPLEMENTATION_UNSPECIFIED: _ClassVar[MembershipState.ControlPlaneManagement.Implementation]
            ISTIOD: _ClassVar[MembershipState.ControlPlaneManagement.Implementation]
            TRAFFIC_DIRECTOR: _ClassVar[MembershipState.ControlPlaneManagement.Implementation]
            UPDATING: _ClassVar[MembershipState.ControlPlaneManagement.Implementation]
        IMPLEMENTATION_UNSPECIFIED: MembershipState.ControlPlaneManagement.Implementation
        ISTIOD: MembershipState.ControlPlaneManagement.Implementation
        TRAFFIC_DIRECTOR: MembershipState.ControlPlaneManagement.Implementation
        UPDATING: MembershipState.ControlPlaneManagement.Implementation
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
        details: _containers.RepeatedCompositeFieldContainer[StatusDetails]
        state: MembershipState.LifecycleState
        implementation: MembershipState.ControlPlaneManagement.Implementation

        def __init__(self, details: _Optional[_Iterable[_Union[StatusDetails, _Mapping]]]=..., state: _Optional[_Union[MembershipState.LifecycleState, str]]=..., implementation: _Optional[_Union[MembershipState.ControlPlaneManagement.Implementation, str]]=...) -> None:
            ...

    class DataPlaneManagement(_message.Message):
        __slots__ = ('state', 'details')
        STATE_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        state: MembershipState.LifecycleState
        details: _containers.RepeatedCompositeFieldContainer[StatusDetails]

        def __init__(self, state: _Optional[_Union[MembershipState.LifecycleState, str]]=..., details: _Optional[_Iterable[_Union[StatusDetails, _Mapping]]]=...) -> None:
            ...

    class Condition(_message.Message):
        __slots__ = ('code', 'documentation_link', 'details', 'severity')

        class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CODE_UNSPECIFIED: _ClassVar[MembershipState.Condition.Code]
            MESH_IAM_PERMISSION_DENIED: _ClassVar[MembershipState.Condition.Code]
            CNI_CONFIG_UNSUPPORTED: _ClassVar[MembershipState.Condition.Code]
            GKE_SANDBOX_UNSUPPORTED: _ClassVar[MembershipState.Condition.Code]
            NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED: _ClassVar[MembershipState.Condition.Code]
            CNI_INSTALLATION_FAILED: _ClassVar[MembershipState.Condition.Code]
            CNI_POD_UNSCHEDULABLE: _ClassVar[MembershipState.Condition.Code]
            UNSUPPORTED_MULTIPLE_CONTROL_PLANES: _ClassVar[MembershipState.Condition.Code]
            VPCSC_GA_SUPPORTED: _ClassVar[MembershipState.Condition.Code]
            CONFIG_APPLY_INTERNAL_ERROR: _ClassVar[MembershipState.Condition.Code]
            CONFIG_VALIDATION_ERROR: _ClassVar[MembershipState.Condition.Code]
            CONFIG_VALIDATION_WARNING: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_BACKEND_SERVICES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_HEALTH_CHECKS: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_HTTP_ROUTES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_TCP_ROUTES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_TLS_ROUTES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_TRAFFIC_POLICIES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_ENDPOINT_POLICIES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_GATEWAYS: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_MESHES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_SERVER_TLS_POLICIES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_CLIENT_TLS_POLICIES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_SERVICE_LB_POLICIES: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_HTTP_FILTERS: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_TCP_FILTERS: _ClassVar[MembershipState.Condition.Code]
            QUOTA_EXCEEDED_NETWORK_ENDPOINT_GROUPS: _ClassVar[MembershipState.Condition.Code]
        CODE_UNSPECIFIED: MembershipState.Condition.Code
        MESH_IAM_PERMISSION_DENIED: MembershipState.Condition.Code
        CNI_CONFIG_UNSUPPORTED: MembershipState.Condition.Code
        GKE_SANDBOX_UNSUPPORTED: MembershipState.Condition.Code
        NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED: MembershipState.Condition.Code
        CNI_INSTALLATION_FAILED: MembershipState.Condition.Code
        CNI_POD_UNSCHEDULABLE: MembershipState.Condition.Code
        UNSUPPORTED_MULTIPLE_CONTROL_PLANES: MembershipState.Condition.Code
        VPCSC_GA_SUPPORTED: MembershipState.Condition.Code
        CONFIG_APPLY_INTERNAL_ERROR: MembershipState.Condition.Code
        CONFIG_VALIDATION_ERROR: MembershipState.Condition.Code
        CONFIG_VALIDATION_WARNING: MembershipState.Condition.Code
        QUOTA_EXCEEDED_BACKEND_SERVICES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_HEALTH_CHECKS: MembershipState.Condition.Code
        QUOTA_EXCEEDED_HTTP_ROUTES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_TCP_ROUTES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_TLS_ROUTES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_TRAFFIC_POLICIES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_ENDPOINT_POLICIES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_GATEWAYS: MembershipState.Condition.Code
        QUOTA_EXCEEDED_MESHES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_SERVER_TLS_POLICIES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_CLIENT_TLS_POLICIES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_SERVICE_LB_POLICIES: MembershipState.Condition.Code
        QUOTA_EXCEEDED_HTTP_FILTERS: MembershipState.Condition.Code
        QUOTA_EXCEEDED_TCP_FILTERS: MembershipState.Condition.Code
        QUOTA_EXCEEDED_NETWORK_ENDPOINT_GROUPS: MembershipState.Condition.Code

        class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEVERITY_UNSPECIFIED: _ClassVar[MembershipState.Condition.Severity]
            ERROR: _ClassVar[MembershipState.Condition.Severity]
            WARNING: _ClassVar[MembershipState.Condition.Severity]
            INFO: _ClassVar[MembershipState.Condition.Severity]
        SEVERITY_UNSPECIFIED: MembershipState.Condition.Severity
        ERROR: MembershipState.Condition.Severity
        WARNING: MembershipState.Condition.Severity
        INFO: MembershipState.Condition.Severity
        CODE_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_LINK_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        code: MembershipState.Condition.Code
        documentation_link: str
        details: str
        severity: MembershipState.Condition.Severity

        def __init__(self, code: _Optional[_Union[MembershipState.Condition.Code, str]]=..., documentation_link: _Optional[str]=..., details: _Optional[str]=..., severity: _Optional[_Union[MembershipState.Condition.Severity, str]]=...) -> None:
            ...
    CONTROL_PLANE_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    DATA_PLANE_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    control_plane_management: MembershipState.ControlPlaneManagement
    data_plane_management: MembershipState.DataPlaneManagement
    conditions: _containers.RepeatedCompositeFieldContainer[MembershipState.Condition]

    def __init__(self, control_plane_management: _Optional[_Union[MembershipState.ControlPlaneManagement, _Mapping]]=..., data_plane_management: _Optional[_Union[MembershipState.DataPlaneManagement, _Mapping]]=..., conditions: _Optional[_Iterable[_Union[MembershipState.Condition, _Mapping]]]=...) -> None:
        ...

class StatusDetails(_message.Message):
    __slots__ = ('code', 'details')
    CODE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    code: str
    details: str

    def __init__(self, code: _Optional[str]=..., details: _Optional[str]=...) -> None:
        ...