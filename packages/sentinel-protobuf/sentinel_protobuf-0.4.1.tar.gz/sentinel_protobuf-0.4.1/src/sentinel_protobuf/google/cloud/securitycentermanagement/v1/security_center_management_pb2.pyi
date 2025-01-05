from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecurityCenterService(_message.Message):
    __slots__ = ("name", "intended_enablement_state", "effective_enablement_state", "modules", "update_time", "service_config")
    class EnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[SecurityCenterService.EnablementState]
        INHERITED: _ClassVar[SecurityCenterService.EnablementState]
        ENABLED: _ClassVar[SecurityCenterService.EnablementState]
        DISABLED: _ClassVar[SecurityCenterService.EnablementState]
        INGEST_ONLY: _ClassVar[SecurityCenterService.EnablementState]
    ENABLEMENT_STATE_UNSPECIFIED: SecurityCenterService.EnablementState
    INHERITED: SecurityCenterService.EnablementState
    ENABLED: SecurityCenterService.EnablementState
    DISABLED: SecurityCenterService.EnablementState
    INGEST_ONLY: SecurityCenterService.EnablementState
    class ModuleSettings(_message.Message):
        __slots__ = ("intended_enablement_state", "effective_enablement_state")
        INTENDED_ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
        intended_enablement_state: SecurityCenterService.EnablementState
        effective_enablement_state: SecurityCenterService.EnablementState
        def __init__(self, intended_enablement_state: _Optional[_Union[SecurityCenterService.EnablementState, str]] = ..., effective_enablement_state: _Optional[_Union[SecurityCenterService.EnablementState, str]] = ...) -> None: ...
    class ModulesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SecurityCenterService.ModuleSettings
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SecurityCenterService.ModuleSettings, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTENDED_ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    intended_enablement_state: SecurityCenterService.EnablementState
    effective_enablement_state: SecurityCenterService.EnablementState
    modules: _containers.MessageMap[str, SecurityCenterService.ModuleSettings]
    update_time: _timestamp_pb2.Timestamp
    service_config: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., intended_enablement_state: _Optional[_Union[SecurityCenterService.EnablementState, str]] = ..., effective_enablement_state: _Optional[_Union[SecurityCenterService.EnablementState, str]] = ..., modules: _Optional[_Mapping[str, SecurityCenterService.ModuleSettings]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., service_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class EffectiveSecurityHealthAnalyticsCustomModule(_message.Message):
    __slots__ = ("name", "custom_config", "enablement_state", "display_name")
    class EnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[EffectiveSecurityHealthAnalyticsCustomModule.EnablementState]
        ENABLED: _ClassVar[EffectiveSecurityHealthAnalyticsCustomModule.EnablementState]
        DISABLED: _ClassVar[EffectiveSecurityHealthAnalyticsCustomModule.EnablementState]
    ENABLEMENT_STATE_UNSPECIFIED: EffectiveSecurityHealthAnalyticsCustomModule.EnablementState
    ENABLED: EffectiveSecurityHealthAnalyticsCustomModule.EnablementState
    DISABLED: EffectiveSecurityHealthAnalyticsCustomModule.EnablementState
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    custom_config: CustomConfig
    enablement_state: EffectiveSecurityHealthAnalyticsCustomModule.EnablementState
    display_name: str
    def __init__(self, name: _Optional[str] = ..., custom_config: _Optional[_Union[CustomConfig, _Mapping]] = ..., enablement_state: _Optional[_Union[EffectiveSecurityHealthAnalyticsCustomModule.EnablementState, str]] = ..., display_name: _Optional[str] = ...) -> None: ...

class ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEffectiveSecurityHealthAnalyticsCustomModulesResponse(_message.Message):
    __slots__ = ("effective_security_health_analytics_custom_modules", "next_page_token")
    EFFECTIVE_SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    effective_security_health_analytics_custom_modules: _containers.RepeatedCompositeFieldContainer[EffectiveSecurityHealthAnalyticsCustomModule]
    next_page_token: str
    def __init__(self, effective_security_health_analytics_custom_modules: _Optional[_Iterable[_Union[EffectiveSecurityHealthAnalyticsCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SecurityHealthAnalyticsCustomModule(_message.Message):
    __slots__ = ("name", "display_name", "enablement_state", "update_time", "last_editor", "ancestor_module", "custom_config")
    class EnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[SecurityHealthAnalyticsCustomModule.EnablementState]
        ENABLED: _ClassVar[SecurityHealthAnalyticsCustomModule.EnablementState]
        DISABLED: _ClassVar[SecurityHealthAnalyticsCustomModule.EnablementState]
        INHERITED: _ClassVar[SecurityHealthAnalyticsCustomModule.EnablementState]
    ENABLEMENT_STATE_UNSPECIFIED: SecurityHealthAnalyticsCustomModule.EnablementState
    ENABLED: SecurityHealthAnalyticsCustomModule.EnablementState
    DISABLED: SecurityHealthAnalyticsCustomModule.EnablementState
    INHERITED: SecurityHealthAnalyticsCustomModule.EnablementState
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITOR_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_MODULE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    enablement_state: SecurityHealthAnalyticsCustomModule.EnablementState
    update_time: _timestamp_pb2.Timestamp
    last_editor: str
    ancestor_module: str
    custom_config: CustomConfig
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., enablement_state: _Optional[_Union[SecurityHealthAnalyticsCustomModule.EnablementState, str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_editor: _Optional[str] = ..., ancestor_module: _Optional[str] = ..., custom_config: _Optional[_Union[CustomConfig, _Mapping]] = ...) -> None: ...

class CustomConfig(_message.Message):
    __slots__ = ("predicate", "custom_output", "resource_selector", "severity", "description", "recommendation")
    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[CustomConfig.Severity]
        CRITICAL: _ClassVar[CustomConfig.Severity]
        HIGH: _ClassVar[CustomConfig.Severity]
        MEDIUM: _ClassVar[CustomConfig.Severity]
        LOW: _ClassVar[CustomConfig.Severity]
    SEVERITY_UNSPECIFIED: CustomConfig.Severity
    CRITICAL: CustomConfig.Severity
    HIGH: CustomConfig.Severity
    MEDIUM: CustomConfig.Severity
    LOW: CustomConfig.Severity
    class CustomOutputSpec(_message.Message):
        __slots__ = ("properties",)
        class Property(_message.Message):
            __slots__ = ("name", "value_expression")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
            name: str
            value_expression: _expr_pb2.Expr
            def __init__(self, name: _Optional[str] = ..., value_expression: _Optional[_Union[_expr_pb2.Expr, _Mapping]] = ...) -> None: ...
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        properties: _containers.RepeatedCompositeFieldContainer[CustomConfig.CustomOutputSpec.Property]
        def __init__(self, properties: _Optional[_Iterable[_Union[CustomConfig.CustomOutputSpec.Property, _Mapping]]] = ...) -> None: ...
    class ResourceSelector(_message.Message):
        __slots__ = ("resource_types",)
        RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
        resource_types: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, resource_types: _Optional[_Iterable[str]] = ...) -> None: ...
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    predicate: _expr_pb2.Expr
    custom_output: CustomConfig.CustomOutputSpec
    resource_selector: CustomConfig.ResourceSelector
    severity: CustomConfig.Severity
    description: str
    recommendation: str
    def __init__(self, predicate: _Optional[_Union[_expr_pb2.Expr, _Mapping]] = ..., custom_output: _Optional[_Union[CustomConfig.CustomOutputSpec, _Mapping]] = ..., resource_selector: _Optional[_Union[CustomConfig.ResourceSelector, _Mapping]] = ..., severity: _Optional[_Union[CustomConfig.Severity, str]] = ..., description: _Optional[str] = ..., recommendation: _Optional[str] = ...) -> None: ...

class ListSecurityHealthAnalyticsCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSecurityHealthAnalyticsCustomModulesResponse(_message.Message):
    __slots__ = ("security_health_analytics_custom_modules", "next_page_token")
    SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    security_health_analytics_custom_modules: _containers.RepeatedCompositeFieldContainer[SecurityHealthAnalyticsCustomModule]
    next_page_token: str
    def __init__(self, security_health_analytics_custom_modules: _Optional[_Iterable[_Union[SecurityHealthAnalyticsCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListDescendantSecurityHealthAnalyticsCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDescendantSecurityHealthAnalyticsCustomModulesResponse(_message.Message):
    __slots__ = ("security_health_analytics_custom_modules", "next_page_token")
    SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    security_health_analytics_custom_modules: _containers.RepeatedCompositeFieldContainer[SecurityHealthAnalyticsCustomModule]
    next_page_token: str
    def __init__(self, security_health_analytics_custom_modules: _Optional[_Iterable[_Union[SecurityHealthAnalyticsCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("parent", "security_health_analytics_custom_module", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    security_health_analytics_custom_module: SecurityHealthAnalyticsCustomModule
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., security_health_analytics_custom_module: _Optional[_Union[SecurityHealthAnalyticsCustomModule, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class UpdateSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("update_mask", "security_health_analytics_custom_module", "validate_only")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    security_health_analytics_custom_module: SecurityHealthAnalyticsCustomModule
    validate_only: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., security_health_analytics_custom_module: _Optional[_Union[SecurityHealthAnalyticsCustomModule, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class DeleteSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("name", "validate_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class SimulateSecurityHealthAnalyticsCustomModuleRequest(_message.Message):
    __slots__ = ("parent", "custom_config", "resource")
    class SimulatedResource(_message.Message):
        __slots__ = ("resource_type", "resource_data", "iam_policy_data")
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_DATA_FIELD_NUMBER: _ClassVar[int]
        IAM_POLICY_DATA_FIELD_NUMBER: _ClassVar[int]
        resource_type: str
        resource_data: _struct_pb2.Struct
        iam_policy_data: _policy_pb2.Policy
        def __init__(self, resource_type: _Optional[str] = ..., resource_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., iam_policy_data: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    custom_config: CustomConfig
    resource: SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource
    def __init__(self, parent: _Optional[str] = ..., custom_config: _Optional[_Union[CustomConfig, _Mapping]] = ..., resource: _Optional[_Union[SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource, _Mapping]] = ...) -> None: ...

class SimulatedFinding(_message.Message):
    __slots__ = ("name", "parent", "resource_name", "category", "state", "source_properties", "event_time", "severity", "finding_class")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[SimulatedFinding.State]
        ACTIVE: _ClassVar[SimulatedFinding.State]
        INACTIVE: _ClassVar[SimulatedFinding.State]
    STATE_UNSPECIFIED: SimulatedFinding.State
    ACTIVE: SimulatedFinding.State
    INACTIVE: SimulatedFinding.State
    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[SimulatedFinding.Severity]
        CRITICAL: _ClassVar[SimulatedFinding.Severity]
        HIGH: _ClassVar[SimulatedFinding.Severity]
        MEDIUM: _ClassVar[SimulatedFinding.Severity]
        LOW: _ClassVar[SimulatedFinding.Severity]
    SEVERITY_UNSPECIFIED: SimulatedFinding.Severity
    CRITICAL: SimulatedFinding.Severity
    HIGH: SimulatedFinding.Severity
    MEDIUM: SimulatedFinding.Severity
    LOW: SimulatedFinding.Severity
    class FindingClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FINDING_CLASS_UNSPECIFIED: _ClassVar[SimulatedFinding.FindingClass]
        THREAT: _ClassVar[SimulatedFinding.FindingClass]
        VULNERABILITY: _ClassVar[SimulatedFinding.FindingClass]
        MISCONFIGURATION: _ClassVar[SimulatedFinding.FindingClass]
        OBSERVATION: _ClassVar[SimulatedFinding.FindingClass]
        SCC_ERROR: _ClassVar[SimulatedFinding.FindingClass]
        POSTURE_VIOLATION: _ClassVar[SimulatedFinding.FindingClass]
        TOXIC_COMBINATION: _ClassVar[SimulatedFinding.FindingClass]
    FINDING_CLASS_UNSPECIFIED: SimulatedFinding.FindingClass
    THREAT: SimulatedFinding.FindingClass
    VULNERABILITY: SimulatedFinding.FindingClass
    MISCONFIGURATION: SimulatedFinding.FindingClass
    OBSERVATION: SimulatedFinding.FindingClass
    SCC_ERROR: SimulatedFinding.FindingClass
    POSTURE_VIOLATION: SimulatedFinding.FindingClass
    TOXIC_COMBINATION: SimulatedFinding.FindingClass
    class SourcePropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    FINDING_CLASS_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    resource_name: str
    category: str
    state: SimulatedFinding.State
    source_properties: _containers.MessageMap[str, _struct_pb2.Value]
    event_time: _timestamp_pb2.Timestamp
    severity: SimulatedFinding.Severity
    finding_class: SimulatedFinding.FindingClass
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ..., resource_name: _Optional[str] = ..., category: _Optional[str] = ..., state: _Optional[_Union[SimulatedFinding.State, str]] = ..., source_properties: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., severity: _Optional[_Union[SimulatedFinding.Severity, str]] = ..., finding_class: _Optional[_Union[SimulatedFinding.FindingClass, str]] = ...) -> None: ...

class SimulateSecurityHealthAnalyticsCustomModuleResponse(_message.Message):
    __slots__ = ("result",)
    class SimulatedResult(_message.Message):
        __slots__ = ("finding", "no_violation", "error")
        FINDING_FIELD_NUMBER: _ClassVar[int]
        NO_VIOLATION_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        finding: SimulatedFinding
        no_violation: _empty_pb2.Empty
        error: _status_pb2.Status
        def __init__(self, finding: _Optional[_Union[SimulatedFinding, _Mapping]] = ..., no_violation: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: SimulateSecurityHealthAnalyticsCustomModuleResponse.SimulatedResult
    def __init__(self, result: _Optional[_Union[SimulateSecurityHealthAnalyticsCustomModuleResponse.SimulatedResult, _Mapping]] = ...) -> None: ...

class EffectiveEventThreatDetectionCustomModule(_message.Message):
    __slots__ = ("name", "config", "enablement_state", "type", "display_name", "description")
    class EnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[EffectiveEventThreatDetectionCustomModule.EnablementState]
        ENABLED: _ClassVar[EffectiveEventThreatDetectionCustomModule.EnablementState]
        DISABLED: _ClassVar[EffectiveEventThreatDetectionCustomModule.EnablementState]
    ENABLEMENT_STATE_UNSPECIFIED: EffectiveEventThreatDetectionCustomModule.EnablementState
    ENABLED: EffectiveEventThreatDetectionCustomModule.EnablementState
    DISABLED: EffectiveEventThreatDetectionCustomModule.EnablementState
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: _struct_pb2.Struct
    enablement_state: EffectiveEventThreatDetectionCustomModule.EnablementState
    type: str
    display_name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., enablement_state: _Optional[_Union[EffectiveEventThreatDetectionCustomModule.EnablementState, str]] = ..., type: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ListEffectiveEventThreatDetectionCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEffectiveEventThreatDetectionCustomModulesResponse(_message.Message):
    __slots__ = ("effective_event_threat_detection_custom_modules", "next_page_token")
    EFFECTIVE_EVENT_THREAT_DETECTION_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    effective_event_threat_detection_custom_modules: _containers.RepeatedCompositeFieldContainer[EffectiveEventThreatDetectionCustomModule]
    next_page_token: str
    def __init__(self, effective_event_threat_detection_custom_modules: _Optional[_Iterable[_Union[EffectiveEventThreatDetectionCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetEffectiveEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class EventThreatDetectionCustomModule(_message.Message):
    __slots__ = ("name", "config", "ancestor_module", "enablement_state", "type", "display_name", "description", "update_time", "last_editor")
    class EnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[EventThreatDetectionCustomModule.EnablementState]
        ENABLED: _ClassVar[EventThreatDetectionCustomModule.EnablementState]
        DISABLED: _ClassVar[EventThreatDetectionCustomModule.EnablementState]
        INHERITED: _ClassVar[EventThreatDetectionCustomModule.EnablementState]
    ENABLEMENT_STATE_UNSPECIFIED: EventThreatDetectionCustomModule.EnablementState
    ENABLED: EventThreatDetectionCustomModule.EnablementState
    DISABLED: EventThreatDetectionCustomModule.EnablementState
    INHERITED: EventThreatDetectionCustomModule.EnablementState
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_MODULE_FIELD_NUMBER: _ClassVar[int]
    ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: _struct_pb2.Struct
    ancestor_module: str
    enablement_state: EventThreatDetectionCustomModule.EnablementState
    type: str
    display_name: str
    description: str
    update_time: _timestamp_pb2.Timestamp
    last_editor: str
    def __init__(self, name: _Optional[str] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., ancestor_module: _Optional[str] = ..., enablement_state: _Optional[_Union[EventThreatDetectionCustomModule.EnablementState, str]] = ..., type: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_editor: _Optional[str] = ...) -> None: ...

class ListEventThreatDetectionCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEventThreatDetectionCustomModulesResponse(_message.Message):
    __slots__ = ("event_threat_detection_custom_modules", "next_page_token")
    EVENT_THREAT_DETECTION_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    event_threat_detection_custom_modules: _containers.RepeatedCompositeFieldContainer[EventThreatDetectionCustomModule]
    next_page_token: str
    def __init__(self, event_threat_detection_custom_modules: _Optional[_Iterable[_Union[EventThreatDetectionCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListDescendantEventThreatDetectionCustomModulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDescendantEventThreatDetectionCustomModulesResponse(_message.Message):
    __slots__ = ("event_threat_detection_custom_modules", "next_page_token")
    EVENT_THREAT_DETECTION_CUSTOM_MODULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    event_threat_detection_custom_modules: _containers.RepeatedCompositeFieldContainer[EventThreatDetectionCustomModule]
    next_page_token: str
    def __init__(self, event_threat_detection_custom_modules: _Optional[_Iterable[_Union[EventThreatDetectionCustomModule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("parent", "event_threat_detection_custom_module", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_THREAT_DETECTION_CUSTOM_MODULE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    event_threat_detection_custom_module: EventThreatDetectionCustomModule
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., event_threat_detection_custom_module: _Optional[_Union[EventThreatDetectionCustomModule, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class UpdateEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("update_mask", "event_threat_detection_custom_module", "validate_only")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    EVENT_THREAT_DETECTION_CUSTOM_MODULE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    event_threat_detection_custom_module: EventThreatDetectionCustomModule
    validate_only: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., event_threat_detection_custom_module: _Optional[_Union[EventThreatDetectionCustomModule, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class DeleteEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("name", "validate_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class ValidateEventThreatDetectionCustomModuleRequest(_message.Message):
    __slots__ = ("parent", "raw_text", "type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RAW_TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    raw_text: str
    type: str
    def __init__(self, parent: _Optional[str] = ..., raw_text: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class ValidateEventThreatDetectionCustomModuleResponse(_message.Message):
    __slots__ = ("errors",)
    class CustomModuleValidationError(_message.Message):
        __slots__ = ("description", "field_path", "start", "end")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        description: str
        field_path: str
        start: ValidateEventThreatDetectionCustomModuleResponse.Position
        end: ValidateEventThreatDetectionCustomModuleResponse.Position
        def __init__(self, description: _Optional[str] = ..., field_path: _Optional[str] = ..., start: _Optional[_Union[ValidateEventThreatDetectionCustomModuleResponse.Position, _Mapping]] = ..., end: _Optional[_Union[ValidateEventThreatDetectionCustomModuleResponse.Position, _Mapping]] = ...) -> None: ...
    class Position(_message.Message):
        __slots__ = ("line_number", "column_number")
        LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        COLUMN_NUMBER_FIELD_NUMBER: _ClassVar[int]
        line_number: int
        column_number: int
        def __init__(self, line_number: _Optional[int] = ..., column_number: _Optional[int] = ...) -> None: ...
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[ValidateEventThreatDetectionCustomModuleResponse.CustomModuleValidationError]
    def __init__(self, errors: _Optional[_Iterable[_Union[ValidateEventThreatDetectionCustomModuleResponse.CustomModuleValidationError, _Mapping]]] = ...) -> None: ...

class GetSecurityCenterServiceRequest(_message.Message):
    __slots__ = ("name", "show_eligible_modules_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_ELIGIBLE_MODULES_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    show_eligible_modules_only: bool
    def __init__(self, name: _Optional[str] = ..., show_eligible_modules_only: bool = ...) -> None: ...

class ListSecurityCenterServicesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "show_eligible_modules_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_ELIGIBLE_MODULES_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_eligible_modules_only: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., show_eligible_modules_only: bool = ...) -> None: ...

class ListSecurityCenterServicesResponse(_message.Message):
    __slots__ = ("security_center_services", "next_page_token")
    SECURITY_CENTER_SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    security_center_services: _containers.RepeatedCompositeFieldContainer[SecurityCenterService]
    next_page_token: str
    def __init__(self, security_center_services: _Optional[_Iterable[_Union[SecurityCenterService, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateSecurityCenterServiceRequest(_message.Message):
    __slots__ = ("security_center_service", "update_mask", "validate_only")
    SECURITY_CENTER_SERVICE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    security_center_service: SecurityCenterService
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool
    def __init__(self, security_center_service: _Optional[_Union[SecurityCenterService, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., validate_only: bool = ...) -> None: ...
