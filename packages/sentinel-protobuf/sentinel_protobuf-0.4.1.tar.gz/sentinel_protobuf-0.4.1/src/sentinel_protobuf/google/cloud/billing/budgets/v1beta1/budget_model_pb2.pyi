from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.type import date_pb2 as _date_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CalendarPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CALENDAR_PERIOD_UNSPECIFIED: _ClassVar[CalendarPeriod]
    MONTH: _ClassVar[CalendarPeriod]
    QUARTER: _ClassVar[CalendarPeriod]
    YEAR: _ClassVar[CalendarPeriod]
CALENDAR_PERIOD_UNSPECIFIED: CalendarPeriod
MONTH: CalendarPeriod
QUARTER: CalendarPeriod
YEAR: CalendarPeriod

class Budget(_message.Message):
    __slots__ = ('name', 'display_name', 'budget_filter', 'amount', 'threshold_rules', 'all_updates_rule', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FILTER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_RULES_FIELD_NUMBER: _ClassVar[int]
    ALL_UPDATES_RULE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    budget_filter: Filter
    amount: BudgetAmount
    threshold_rules: _containers.RepeatedCompositeFieldContainer[ThresholdRule]
    all_updates_rule: AllUpdatesRule
    etag: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., budget_filter: _Optional[_Union[Filter, _Mapping]]=..., amount: _Optional[_Union[BudgetAmount, _Mapping]]=..., threshold_rules: _Optional[_Iterable[_Union[ThresholdRule, _Mapping]]]=..., all_updates_rule: _Optional[_Union[AllUpdatesRule, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class BudgetAmount(_message.Message):
    __slots__ = ('specified_amount', 'last_period_amount')
    SPECIFIED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_PERIOD_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    specified_amount: _money_pb2.Money
    last_period_amount: LastPeriodAmount

    def __init__(self, specified_amount: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., last_period_amount: _Optional[_Union[LastPeriodAmount, _Mapping]]=...) -> None:
        ...

class LastPeriodAmount(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ThresholdRule(_message.Message):
    __slots__ = ('threshold_percent', 'spend_basis')

    class Basis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BASIS_UNSPECIFIED: _ClassVar[ThresholdRule.Basis]
        CURRENT_SPEND: _ClassVar[ThresholdRule.Basis]
        FORECASTED_SPEND: _ClassVar[ThresholdRule.Basis]
    BASIS_UNSPECIFIED: ThresholdRule.Basis
    CURRENT_SPEND: ThresholdRule.Basis
    FORECASTED_SPEND: ThresholdRule.Basis
    THRESHOLD_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SPEND_BASIS_FIELD_NUMBER: _ClassVar[int]
    threshold_percent: float
    spend_basis: ThresholdRule.Basis

    def __init__(self, threshold_percent: _Optional[float]=..., spend_basis: _Optional[_Union[ThresholdRule.Basis, str]]=...) -> None:
        ...

class AllUpdatesRule(_message.Message):
    __slots__ = ('pubsub_topic', 'schema_version', 'monitoring_notification_channels', 'disable_default_iam_recipients', 'enable_project_level_recipients')
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    MONITORING_NOTIFICATION_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DEFAULT_IAM_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PROJECT_LEVEL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    pubsub_topic: str
    schema_version: str
    monitoring_notification_channels: _containers.RepeatedScalarFieldContainer[str]
    disable_default_iam_recipients: bool
    enable_project_level_recipients: bool

    def __init__(self, pubsub_topic: _Optional[str]=..., schema_version: _Optional[str]=..., monitoring_notification_channels: _Optional[_Iterable[str]]=..., disable_default_iam_recipients: bool=..., enable_project_level_recipients: bool=...) -> None:
        ...

class Filter(_message.Message):
    __slots__ = ('projects', 'resource_ancestors', 'credit_types', 'credit_types_treatment', 'services', 'subaccounts', 'labels', 'calendar_period', 'custom_period')

    class CreditTypesTreatment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREDIT_TYPES_TREATMENT_UNSPECIFIED: _ClassVar[Filter.CreditTypesTreatment]
        INCLUDE_ALL_CREDITS: _ClassVar[Filter.CreditTypesTreatment]
        EXCLUDE_ALL_CREDITS: _ClassVar[Filter.CreditTypesTreatment]
        INCLUDE_SPECIFIED_CREDITS: _ClassVar[Filter.CreditTypesTreatment]
    CREDIT_TYPES_TREATMENT_UNSPECIFIED: Filter.CreditTypesTreatment
    INCLUDE_ALL_CREDITS: Filter.CreditTypesTreatment
    EXCLUDE_ALL_CREDITS: Filter.CreditTypesTreatment
    INCLUDE_SPECIFIED_CREDITS: Filter.CreditTypesTreatment

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ANCESTORS_FIELD_NUMBER: _ClassVar[int]
    CREDIT_TYPES_FIELD_NUMBER: _ClassVar[int]
    CREDIT_TYPES_TREATMENT_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PERIOD_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedScalarFieldContainer[str]
    resource_ancestors: _containers.RepeatedScalarFieldContainer[str]
    credit_types: _containers.RepeatedScalarFieldContainer[str]
    credit_types_treatment: Filter.CreditTypesTreatment
    services: _containers.RepeatedScalarFieldContainer[str]
    subaccounts: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.MessageMap[str, _struct_pb2.ListValue]
    calendar_period: CalendarPeriod
    custom_period: CustomPeriod

    def __init__(self, projects: _Optional[_Iterable[str]]=..., resource_ancestors: _Optional[_Iterable[str]]=..., credit_types: _Optional[_Iterable[str]]=..., credit_types_treatment: _Optional[_Union[Filter.CreditTypesTreatment, str]]=..., services: _Optional[_Iterable[str]]=..., subaccounts: _Optional[_Iterable[str]]=..., labels: _Optional[_Mapping[str, _struct_pb2.ListValue]]=..., calendar_period: _Optional[_Union[CalendarPeriod, str]]=..., custom_period: _Optional[_Union[CustomPeriod, _Mapping]]=...) -> None:
        ...

class CustomPeriod(_message.Message):
    __slots__ = ('start_date', 'end_date')
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date

    def __init__(self, start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...