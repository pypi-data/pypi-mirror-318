from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2alpha import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoggingConfig(_message.Message):
    __slots__ = ("name", "default_log_generation_rule", "service_log_generation_rules")
    class LoggingLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGGING_LEVEL_UNSPECIFIED: _ClassVar[LoggingConfig.LoggingLevel]
        LOGGING_DISABLED: _ClassVar[LoggingConfig.LoggingLevel]
        LOG_ERRORS_AND_ABOVE: _ClassVar[LoggingConfig.LoggingLevel]
        LOG_WARNINGS_AND_ABOVE: _ClassVar[LoggingConfig.LoggingLevel]
        LOG_ALL: _ClassVar[LoggingConfig.LoggingLevel]
    LOGGING_LEVEL_UNSPECIFIED: LoggingConfig.LoggingLevel
    LOGGING_DISABLED: LoggingConfig.LoggingLevel
    LOG_ERRORS_AND_ABOVE: LoggingConfig.LoggingLevel
    LOG_WARNINGS_AND_ABOVE: LoggingConfig.LoggingLevel
    LOG_ALL: LoggingConfig.LoggingLevel
    class LogGenerationRule(_message.Message):
        __slots__ = ("logging_level", "info_log_sample_rate")
        LOGGING_LEVEL_FIELD_NUMBER: _ClassVar[int]
        INFO_LOG_SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
        logging_level: LoggingConfig.LoggingLevel
        info_log_sample_rate: float
        def __init__(self, logging_level: _Optional[_Union[LoggingConfig.LoggingLevel, str]] = ..., info_log_sample_rate: _Optional[float] = ...) -> None: ...
    class ServiceLogGenerationRule(_message.Message):
        __slots__ = ("service_name", "log_generation_rule")
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        LOG_GENERATION_RULE_FIELD_NUMBER: _ClassVar[int]
        service_name: str
        log_generation_rule: LoggingConfig.LogGenerationRule
        def __init__(self, service_name: _Optional[str] = ..., log_generation_rule: _Optional[_Union[LoggingConfig.LogGenerationRule, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOG_GENERATION_RULE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LOG_GENERATION_RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    default_log_generation_rule: LoggingConfig.LogGenerationRule
    service_log_generation_rules: _containers.RepeatedCompositeFieldContainer[LoggingConfig.ServiceLogGenerationRule]
    def __init__(self, name: _Optional[str] = ..., default_log_generation_rule: _Optional[_Union[LoggingConfig.LogGenerationRule, _Mapping]] = ..., service_log_generation_rules: _Optional[_Iterable[_Union[LoggingConfig.ServiceLogGenerationRule, _Mapping]]] = ...) -> None: ...

class Project(_message.Message):
    __slots__ = ("name", "enrolled_solutions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENROLLED_SOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    enrolled_solutions: _containers.RepeatedScalarFieldContainer[_common_pb2.SolutionType]
    def __init__(self, name: _Optional[str] = ..., enrolled_solutions: _Optional[_Iterable[_Union[_common_pb2.SolutionType, str]]] = ...) -> None: ...

class AlertConfig(_message.Message):
    __slots__ = ("name", "alert_policies")
    class AlertPolicy(_message.Message):
        __slots__ = ("alert_group", "enroll_status", "recipients")
        class EnrollStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENROLL_STATUS_UNSPECIFIED: _ClassVar[AlertConfig.AlertPolicy.EnrollStatus]
            ENROLLED: _ClassVar[AlertConfig.AlertPolicy.EnrollStatus]
            DECLINED: _ClassVar[AlertConfig.AlertPolicy.EnrollStatus]
        ENROLL_STATUS_UNSPECIFIED: AlertConfig.AlertPolicy.EnrollStatus
        ENROLLED: AlertConfig.AlertPolicy.EnrollStatus
        DECLINED: AlertConfig.AlertPolicy.EnrollStatus
        class Recipient(_message.Message):
            __slots__ = ("email_address",)
            EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            email_address: str
            def __init__(self, email_address: _Optional[str] = ...) -> None: ...
        ALERT_GROUP_FIELD_NUMBER: _ClassVar[int]
        ENROLL_STATUS_FIELD_NUMBER: _ClassVar[int]
        RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
        alert_group: str
        enroll_status: AlertConfig.AlertPolicy.EnrollStatus
        recipients: _containers.RepeatedCompositeFieldContainer[AlertConfig.AlertPolicy.Recipient]
        def __init__(self, alert_group: _Optional[str] = ..., enroll_status: _Optional[_Union[AlertConfig.AlertPolicy.EnrollStatus, str]] = ..., recipients: _Optional[_Iterable[_Union[AlertConfig.AlertPolicy.Recipient, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALERT_POLICIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    alert_policies: _containers.RepeatedCompositeFieldContainer[AlertConfig.AlertPolicy]
    def __init__(self, name: _Optional[str] = ..., alert_policies: _Optional[_Iterable[_Union[AlertConfig.AlertPolicy, _Mapping]]] = ...) -> None: ...
