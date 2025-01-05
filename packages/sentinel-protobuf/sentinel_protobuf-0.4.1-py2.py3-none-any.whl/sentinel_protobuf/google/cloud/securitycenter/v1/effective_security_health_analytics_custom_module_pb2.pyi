from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.v1 import security_health_analytics_custom_config_pb2 as _security_health_analytics_custom_config_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EffectiveSecurityHealthAnalyticsCustomModule(_message.Message):
    __slots__ = ('name', 'custom_config', 'enablement_state', 'display_name')

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
    custom_config: _security_health_analytics_custom_config_pb2.CustomConfig
    enablement_state: EffectiveSecurityHealthAnalyticsCustomModule.EnablementState
    display_name: str

    def __init__(self, name: _Optional[str]=..., custom_config: _Optional[_Union[_security_health_analytics_custom_config_pb2.CustomConfig, _Mapping]]=..., enablement_state: _Optional[_Union[EffectiveSecurityHealthAnalyticsCustomModule.EnablementState, str]]=..., display_name: _Optional[str]=...) -> None:
        ...