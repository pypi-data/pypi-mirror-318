from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.securityposture.v1 import sha_custom_config_pb2 as _sha_custom_config_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[EnablementState]
    ENABLED: _ClassVar[EnablementState]
    DISABLED: _ClassVar[EnablementState]
ENABLEMENT_STATE_UNSPECIFIED: EnablementState
ENABLED: EnablementState
DISABLED: EnablementState

class SecurityHealthAnalyticsModule(_message.Message):
    __slots__ = ('module_name', 'module_enablement_state')
    MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    MODULE_ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    module_name: str
    module_enablement_state: EnablementState

    def __init__(self, module_name: _Optional[str]=..., module_enablement_state: _Optional[_Union[EnablementState, str]]=...) -> None:
        ...

class SecurityHealthAnalyticsCustomModule(_message.Message):
    __slots__ = ('id', 'display_name', 'config', 'module_enablement_state')
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODULE_ENABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    config: _sha_custom_config_pb2.CustomConfig
    module_enablement_state: EnablementState

    def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=..., config: _Optional[_Union[_sha_custom_config_pb2.CustomConfig, _Mapping]]=..., module_enablement_state: _Optional[_Union[EnablementState, str]]=...) -> None:
        ...