from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.settings.v1beta1 import billing_settings_pb2 as _billing_settings_pb2
from google.cloud.securitycenter.settings.v1beta1 import component_settings_pb2 as _component_settings_pb2
from google.cloud.securitycenter.settings.v1beta1 import sink_settings_pb2 as _sink_settings_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Settings(_message.Message):
    __slots__ = ('name', 'billing_settings', 'state', 'org_service_account', 'sink_settings', 'component_settings', 'detector_group_settings', 'etag', 'update_time')

    class OnboardingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ONBOARDING_STATE_UNSPECIFIED: _ClassVar[Settings.OnboardingState]
        ENABLED: _ClassVar[Settings.OnboardingState]
        DISABLED: _ClassVar[Settings.OnboardingState]
        BILLING_SELECTED: _ClassVar[Settings.OnboardingState]
        PROVIDERS_SELECTED: _ClassVar[Settings.OnboardingState]
        RESOURCES_SELECTED: _ClassVar[Settings.OnboardingState]
        ORG_SERVICE_ACCOUNT_CREATED: _ClassVar[Settings.OnboardingState]
    ONBOARDING_STATE_UNSPECIFIED: Settings.OnboardingState
    ENABLED: Settings.OnboardingState
    DISABLED: Settings.OnboardingState
    BILLING_SELECTED: Settings.OnboardingState
    PROVIDERS_SELECTED: Settings.OnboardingState
    RESOURCES_SELECTED: Settings.OnboardingState
    ORG_SERVICE_ACCOUNT_CREATED: Settings.OnboardingState

    class DetectorGroupSettings(_message.Message):
        __slots__ = ('state',)
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: _component_settings_pb2.ComponentEnablementState

        def __init__(self, state: _Optional[_Union[_component_settings_pb2.ComponentEnablementState, str]]=...) -> None:
            ...

    class ComponentSettingsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _component_settings_pb2.ComponentSettings

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_component_settings_pb2.ComponentSettings, _Mapping]]=...) -> None:
            ...

    class DetectorGroupSettingsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Settings.DetectorGroupSettings

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Settings.DetectorGroupSettings, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    BILLING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ORG_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SINK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_GROUP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    billing_settings: _billing_settings_pb2.BillingSettings
    state: Settings.OnboardingState
    org_service_account: str
    sink_settings: _sink_settings_pb2.SinkSettings
    component_settings: _containers.MessageMap[str, _component_settings_pb2.ComponentSettings]
    detector_group_settings: _containers.MessageMap[str, Settings.DetectorGroupSettings]
    etag: str
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., billing_settings: _Optional[_Union[_billing_settings_pb2.BillingSettings, _Mapping]]=..., state: _Optional[_Union[Settings.OnboardingState, str]]=..., org_service_account: _Optional[str]=..., sink_settings: _Optional[_Union[_sink_settings_pb2.SinkSettings, _Mapping]]=..., component_settings: _Optional[_Mapping[str, _component_settings_pb2.ComponentSettings]]=..., detector_group_settings: _Optional[_Mapping[str, Settings.DetectorGroupSettings]]=..., etag: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...