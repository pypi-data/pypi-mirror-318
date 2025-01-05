from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComponentEnablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPONENT_ENABLEMENT_STATE_UNSPECIFIED: _ClassVar[ComponentEnablementState]
    DISABLE: _ClassVar[ComponentEnablementState]
    ENABLE: _ClassVar[ComponentEnablementState]
    INHERIT: _ClassVar[ComponentEnablementState]
COMPONENT_ENABLEMENT_STATE_UNSPECIFIED: ComponentEnablementState
DISABLE: ComponentEnablementState
ENABLE: ComponentEnablementState
INHERIT: ComponentEnablementState

class ComponentSettings(_message.Message):
    __slots__ = ('name', 'state', 'project_service_account', 'detector_settings', 'etag', 'update_time', 'container_threat_detection_settings', 'event_threat_detection_settings', 'security_health_analytics_settings', 'web_security_scanner_settings')

    class DetectorSettings(_message.Message):
        __slots__ = ('state',)
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: ComponentEnablementState

        def __init__(self, state: _Optional[_Union[ComponentEnablementState, str]]=...) -> None:
            ...

    class DetectorSettingsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ComponentSettings.DetectorSettings

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ComponentSettings.DetectorSettings, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_THREAT_DETECTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    EVENT_THREAT_DETECTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_HEALTH_ANALYTICS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    WEB_SECURITY_SCANNER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: ComponentEnablementState
    project_service_account: str
    detector_settings: _containers.MessageMap[str, ComponentSettings.DetectorSettings]
    etag: str
    update_time: _timestamp_pb2.Timestamp
    container_threat_detection_settings: ContainerThreatDetectionSettings
    event_threat_detection_settings: EventThreatDetectionSettings
    security_health_analytics_settings: SecurityHealthAnalyticsSettings
    web_security_scanner_settings: WebSecurityScanner

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[ComponentEnablementState, str]]=..., project_service_account: _Optional[str]=..., detector_settings: _Optional[_Mapping[str, ComponentSettings.DetectorSettings]]=..., etag: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., container_threat_detection_settings: _Optional[_Union[ContainerThreatDetectionSettings, _Mapping]]=..., event_threat_detection_settings: _Optional[_Union[EventThreatDetectionSettings, _Mapping]]=..., security_health_analytics_settings: _Optional[_Union[SecurityHealthAnalyticsSettings, _Mapping]]=..., web_security_scanner_settings: _Optional[_Union[WebSecurityScanner, _Mapping]]=...) -> None:
        ...

class WebSecurityScanner(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ContainerThreatDetectionSettings(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EventThreatDetectionSettings(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SecurityHealthAnalyticsSettings(_message.Message):
    __slots__ = ('non_org_iam_member_settings', 'admin_service_account_settings')

    class NonOrgIamMemberSettings(_message.Message):
        __slots__ = ('approved_identities',)
        APPROVED_IDENTITIES_FIELD_NUMBER: _ClassVar[int]
        approved_identities: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, approved_identities: _Optional[_Iterable[str]]=...) -> None:
            ...

    class AdminServiceAccountSettings(_message.Message):
        __slots__ = ('approved_identities',)
        APPROVED_IDENTITIES_FIELD_NUMBER: _ClassVar[int]
        approved_identities: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, approved_identities: _Optional[_Iterable[str]]=...) -> None:
            ...
    NON_ORG_IAM_MEMBER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_SERVICE_ACCOUNT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    non_org_iam_member_settings: SecurityHealthAnalyticsSettings.NonOrgIamMemberSettings
    admin_service_account_settings: SecurityHealthAnalyticsSettings.AdminServiceAccountSettings

    def __init__(self, non_org_iam_member_settings: _Optional[_Union[SecurityHealthAnalyticsSettings.NonOrgIamMemberSettings, _Mapping]]=..., admin_service_account_settings: _Optional[_Union[SecurityHealthAnalyticsSettings.AdminServiceAccountSettings, _Mapping]]=...) -> None:
        ...