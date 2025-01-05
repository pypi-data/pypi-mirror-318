from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.v1 import security_health_analytics_custom_config_pb2 as _security_health_analytics_custom_config_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SecurityHealthAnalyticsCustomModule(_message.Message):
    __slots__ = ('name', 'display_name', 'enablement_state', 'update_time', 'last_editor', 'ancestor_module', 'custom_config')

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
    custom_config: _security_health_analytics_custom_config_pb2.CustomConfig

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., enablement_state: _Optional[_Union[SecurityHealthAnalyticsCustomModule.EnablementState, str]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_editor: _Optional[str]=..., ancestor_module: _Optional[str]=..., custom_config: _Optional[_Union[_security_health_analytics_custom_config_pb2.CustomConfig, _Mapping]]=...) -> None:
        ...