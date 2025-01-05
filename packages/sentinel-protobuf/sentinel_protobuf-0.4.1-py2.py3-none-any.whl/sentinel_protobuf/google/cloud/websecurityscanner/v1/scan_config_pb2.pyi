from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ScanConfig(_message.Message):
    __slots__ = ('name', 'display_name', 'max_qps', 'starting_urls', 'authentication', 'user_agent', 'blacklist_patterns', 'schedule', 'export_to_security_command_center', 'risk_level', 'managed_scan', 'static_ip_scan', 'ignore_http_status_errors')

    class UserAgent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER_AGENT_UNSPECIFIED: _ClassVar[ScanConfig.UserAgent]
        CHROME_LINUX: _ClassVar[ScanConfig.UserAgent]
        CHROME_ANDROID: _ClassVar[ScanConfig.UserAgent]
        SAFARI_IPHONE: _ClassVar[ScanConfig.UserAgent]
    USER_AGENT_UNSPECIFIED: ScanConfig.UserAgent
    CHROME_LINUX: ScanConfig.UserAgent
    CHROME_ANDROID: ScanConfig.UserAgent
    SAFARI_IPHONE: ScanConfig.UserAgent

    class RiskLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RISK_LEVEL_UNSPECIFIED: _ClassVar[ScanConfig.RiskLevel]
        NORMAL: _ClassVar[ScanConfig.RiskLevel]
        LOW: _ClassVar[ScanConfig.RiskLevel]
    RISK_LEVEL_UNSPECIFIED: ScanConfig.RiskLevel
    NORMAL: ScanConfig.RiskLevel
    LOW: ScanConfig.RiskLevel

    class ExportToSecurityCommandCenter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXPORT_TO_SECURITY_COMMAND_CENTER_UNSPECIFIED: _ClassVar[ScanConfig.ExportToSecurityCommandCenter]
        ENABLED: _ClassVar[ScanConfig.ExportToSecurityCommandCenter]
        DISABLED: _ClassVar[ScanConfig.ExportToSecurityCommandCenter]
    EXPORT_TO_SECURITY_COMMAND_CENTER_UNSPECIFIED: ScanConfig.ExportToSecurityCommandCenter
    ENABLED: ScanConfig.ExportToSecurityCommandCenter
    DISABLED: ScanConfig.ExportToSecurityCommandCenter

    class Authentication(_message.Message):
        __slots__ = ('google_account', 'custom_account', 'iap_credential')

        class GoogleAccount(_message.Message):
            __slots__ = ('username', 'password')
            USERNAME_FIELD_NUMBER: _ClassVar[int]
            PASSWORD_FIELD_NUMBER: _ClassVar[int]
            username: str
            password: str

            def __init__(self, username: _Optional[str]=..., password: _Optional[str]=...) -> None:
                ...

        class CustomAccount(_message.Message):
            __slots__ = ('username', 'password', 'login_url')
            USERNAME_FIELD_NUMBER: _ClassVar[int]
            PASSWORD_FIELD_NUMBER: _ClassVar[int]
            LOGIN_URL_FIELD_NUMBER: _ClassVar[int]
            username: str
            password: str
            login_url: str

            def __init__(self, username: _Optional[str]=..., password: _Optional[str]=..., login_url: _Optional[str]=...) -> None:
                ...

        class IapCredential(_message.Message):
            __slots__ = ('iap_test_service_account_info',)

            class IapTestServiceAccountInfo(_message.Message):
                __slots__ = ('target_audience_client_id',)
                TARGET_AUDIENCE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
                target_audience_client_id: str

                def __init__(self, target_audience_client_id: _Optional[str]=...) -> None:
                    ...
            IAP_TEST_SERVICE_ACCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
            iap_test_service_account_info: ScanConfig.Authentication.IapCredential.IapTestServiceAccountInfo

            def __init__(self, iap_test_service_account_info: _Optional[_Union[ScanConfig.Authentication.IapCredential.IapTestServiceAccountInfo, _Mapping]]=...) -> None:
                ...
        GOOGLE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        IAP_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
        google_account: ScanConfig.Authentication.GoogleAccount
        custom_account: ScanConfig.Authentication.CustomAccount
        iap_credential: ScanConfig.Authentication.IapCredential

        def __init__(self, google_account: _Optional[_Union[ScanConfig.Authentication.GoogleAccount, _Mapping]]=..., custom_account: _Optional[_Union[ScanConfig.Authentication.CustomAccount, _Mapping]]=..., iap_credential: _Optional[_Union[ScanConfig.Authentication.IapCredential, _Mapping]]=...) -> None:
            ...

    class Schedule(_message.Message):
        __slots__ = ('schedule_time', 'interval_duration_days')
        SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
        INTERVAL_DURATION_DAYS_FIELD_NUMBER: _ClassVar[int]
        schedule_time: _timestamp_pb2.Timestamp
        interval_duration_days: int

        def __init__(self, schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., interval_duration_days: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_QPS_FIELD_NUMBER: _ClassVar[int]
    STARTING_URLS_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    BLACKLIST_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_TO_SECURITY_COMMAND_CENTER_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MANAGED_SCAN_FIELD_NUMBER: _ClassVar[int]
    STATIC_IP_SCAN_FIELD_NUMBER: _ClassVar[int]
    IGNORE_HTTP_STATUS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    max_qps: int
    starting_urls: _containers.RepeatedScalarFieldContainer[str]
    authentication: ScanConfig.Authentication
    user_agent: ScanConfig.UserAgent
    blacklist_patterns: _containers.RepeatedScalarFieldContainer[str]
    schedule: ScanConfig.Schedule
    export_to_security_command_center: ScanConfig.ExportToSecurityCommandCenter
    risk_level: ScanConfig.RiskLevel
    managed_scan: bool
    static_ip_scan: bool
    ignore_http_status_errors: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., max_qps: _Optional[int]=..., starting_urls: _Optional[_Iterable[str]]=..., authentication: _Optional[_Union[ScanConfig.Authentication, _Mapping]]=..., user_agent: _Optional[_Union[ScanConfig.UserAgent, str]]=..., blacklist_patterns: _Optional[_Iterable[str]]=..., schedule: _Optional[_Union[ScanConfig.Schedule, _Mapping]]=..., export_to_security_command_center: _Optional[_Union[ScanConfig.ExportToSecurityCommandCenter, str]]=..., risk_level: _Optional[_Union[ScanConfig.RiskLevel, str]]=..., managed_scan: bool=..., static_ip_scan: bool=..., ignore_http_status_errors: bool=...) -> None:
        ...