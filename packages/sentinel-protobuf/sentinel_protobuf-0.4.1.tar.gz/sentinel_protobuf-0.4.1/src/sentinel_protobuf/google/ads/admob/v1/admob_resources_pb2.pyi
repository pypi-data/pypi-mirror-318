from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_ORDER_UNSPECIFIED: _ClassVar[SortOrder]
    ASCENDING: _ClassVar[SortOrder]
    DESCENDING: _ClassVar[SortOrder]
SORT_ORDER_UNSPECIFIED: SortOrder
ASCENDING: SortOrder
DESCENDING: SortOrder

class PublisherAccount(_message.Message):
    __slots__ = ('name', 'publisher_id', 'reporting_time_zone', 'currency_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_ID_FIELD_NUMBER: _ClassVar[int]
    REPORTING_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    publisher_id: str
    reporting_time_zone: str
    currency_code: str

    def __init__(self, name: _Optional[str]=..., publisher_id: _Optional[str]=..., reporting_time_zone: _Optional[str]=..., currency_code: _Optional[str]=...) -> None:
        ...

class NetworkReportSpec(_message.Message):
    __slots__ = ('date_range', 'dimensions', 'metrics', 'dimension_filters', 'sort_conditions', 'localization_settings', 'max_report_rows', 'time_zone')

    class Dimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIMENSION_UNSPECIFIED: _ClassVar[NetworkReportSpec.Dimension]
        DATE: _ClassVar[NetworkReportSpec.Dimension]
        MONTH: _ClassVar[NetworkReportSpec.Dimension]
        WEEK: _ClassVar[NetworkReportSpec.Dimension]
        AD_UNIT: _ClassVar[NetworkReportSpec.Dimension]
        APP: _ClassVar[NetworkReportSpec.Dimension]
        AD_TYPE: _ClassVar[NetworkReportSpec.Dimension]
        COUNTRY: _ClassVar[NetworkReportSpec.Dimension]
        FORMAT: _ClassVar[NetworkReportSpec.Dimension]
        PLATFORM: _ClassVar[NetworkReportSpec.Dimension]
    DIMENSION_UNSPECIFIED: NetworkReportSpec.Dimension
    DATE: NetworkReportSpec.Dimension
    MONTH: NetworkReportSpec.Dimension
    WEEK: NetworkReportSpec.Dimension
    AD_UNIT: NetworkReportSpec.Dimension
    APP: NetworkReportSpec.Dimension
    AD_TYPE: NetworkReportSpec.Dimension
    COUNTRY: NetworkReportSpec.Dimension
    FORMAT: NetworkReportSpec.Dimension
    PLATFORM: NetworkReportSpec.Dimension

    class Metric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METRIC_UNSPECIFIED: _ClassVar[NetworkReportSpec.Metric]
        AD_REQUESTS: _ClassVar[NetworkReportSpec.Metric]
        CLICKS: _ClassVar[NetworkReportSpec.Metric]
        ESTIMATED_EARNINGS: _ClassVar[NetworkReportSpec.Metric]
        IMPRESSIONS: _ClassVar[NetworkReportSpec.Metric]
        IMPRESSION_CTR: _ClassVar[NetworkReportSpec.Metric]
        IMPRESSION_RPM: _ClassVar[NetworkReportSpec.Metric]
        MATCHED_REQUESTS: _ClassVar[NetworkReportSpec.Metric]
        MATCH_RATE: _ClassVar[NetworkReportSpec.Metric]
        SHOW_RATE: _ClassVar[NetworkReportSpec.Metric]
    METRIC_UNSPECIFIED: NetworkReportSpec.Metric
    AD_REQUESTS: NetworkReportSpec.Metric
    CLICKS: NetworkReportSpec.Metric
    ESTIMATED_EARNINGS: NetworkReportSpec.Metric
    IMPRESSIONS: NetworkReportSpec.Metric
    IMPRESSION_CTR: NetworkReportSpec.Metric
    IMPRESSION_RPM: NetworkReportSpec.Metric
    MATCHED_REQUESTS: NetworkReportSpec.Metric
    MATCH_RATE: NetworkReportSpec.Metric
    SHOW_RATE: NetworkReportSpec.Metric

    class DimensionFilter(_message.Message):
        __slots__ = ('matches_any', 'dimension')
        MATCHES_ANY_FIELD_NUMBER: _ClassVar[int]
        DIMENSION_FIELD_NUMBER: _ClassVar[int]
        matches_any: StringList
        dimension: NetworkReportSpec.Dimension

        def __init__(self, matches_any: _Optional[_Union[StringList, _Mapping]]=..., dimension: _Optional[_Union[NetworkReportSpec.Dimension, str]]=...) -> None:
            ...

    class SortCondition(_message.Message):
        __slots__ = ('dimension', 'metric', 'order')
        DIMENSION_FIELD_NUMBER: _ClassVar[int]
        METRIC_FIELD_NUMBER: _ClassVar[int]
        ORDER_FIELD_NUMBER: _ClassVar[int]
        dimension: NetworkReportSpec.Dimension
        metric: NetworkReportSpec.Metric
        order: SortOrder

        def __init__(self, dimension: _Optional[_Union[NetworkReportSpec.Dimension, str]]=..., metric: _Optional[_Union[NetworkReportSpec.Metric, str]]=..., order: _Optional[_Union[SortOrder, str]]=...) -> None:
            ...
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MAX_REPORT_ROWS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    date_range: DateRange
    dimensions: _containers.RepeatedScalarFieldContainer[NetworkReportSpec.Dimension]
    metrics: _containers.RepeatedScalarFieldContainer[NetworkReportSpec.Metric]
    dimension_filters: _containers.RepeatedCompositeFieldContainer[NetworkReportSpec.DimensionFilter]
    sort_conditions: _containers.RepeatedCompositeFieldContainer[NetworkReportSpec.SortCondition]
    localization_settings: LocalizationSettings
    max_report_rows: int
    time_zone: str

    def __init__(self, date_range: _Optional[_Union[DateRange, _Mapping]]=..., dimensions: _Optional[_Iterable[_Union[NetworkReportSpec.Dimension, str]]]=..., metrics: _Optional[_Iterable[_Union[NetworkReportSpec.Metric, str]]]=..., dimension_filters: _Optional[_Iterable[_Union[NetworkReportSpec.DimensionFilter, _Mapping]]]=..., sort_conditions: _Optional[_Iterable[_Union[NetworkReportSpec.SortCondition, _Mapping]]]=..., localization_settings: _Optional[_Union[LocalizationSettings, _Mapping]]=..., max_report_rows: _Optional[int]=..., time_zone: _Optional[str]=...) -> None:
        ...

class MediationReportSpec(_message.Message):
    __slots__ = ('date_range', 'dimensions', 'metrics', 'dimension_filters', 'sort_conditions', 'localization_settings', 'max_report_rows', 'time_zone')

    class Dimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIMENSION_UNSPECIFIED: _ClassVar[MediationReportSpec.Dimension]
        DATE: _ClassVar[MediationReportSpec.Dimension]
        MONTH: _ClassVar[MediationReportSpec.Dimension]
        WEEK: _ClassVar[MediationReportSpec.Dimension]
        AD_SOURCE: _ClassVar[MediationReportSpec.Dimension]
        AD_SOURCE_INSTANCE: _ClassVar[MediationReportSpec.Dimension]
        AD_UNIT: _ClassVar[MediationReportSpec.Dimension]
        APP: _ClassVar[MediationReportSpec.Dimension]
        MEDIATION_GROUP: _ClassVar[MediationReportSpec.Dimension]
        COUNTRY: _ClassVar[MediationReportSpec.Dimension]
        FORMAT: _ClassVar[MediationReportSpec.Dimension]
        PLATFORM: _ClassVar[MediationReportSpec.Dimension]
    DIMENSION_UNSPECIFIED: MediationReportSpec.Dimension
    DATE: MediationReportSpec.Dimension
    MONTH: MediationReportSpec.Dimension
    WEEK: MediationReportSpec.Dimension
    AD_SOURCE: MediationReportSpec.Dimension
    AD_SOURCE_INSTANCE: MediationReportSpec.Dimension
    AD_UNIT: MediationReportSpec.Dimension
    APP: MediationReportSpec.Dimension
    MEDIATION_GROUP: MediationReportSpec.Dimension
    COUNTRY: MediationReportSpec.Dimension
    FORMAT: MediationReportSpec.Dimension
    PLATFORM: MediationReportSpec.Dimension

    class Metric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METRIC_UNSPECIFIED: _ClassVar[MediationReportSpec.Metric]
        AD_REQUESTS: _ClassVar[MediationReportSpec.Metric]
        CLICKS: _ClassVar[MediationReportSpec.Metric]
        ESTIMATED_EARNINGS: _ClassVar[MediationReportSpec.Metric]
        IMPRESSIONS: _ClassVar[MediationReportSpec.Metric]
        IMPRESSION_CTR: _ClassVar[MediationReportSpec.Metric]
        MATCHED_REQUESTS: _ClassVar[MediationReportSpec.Metric]
        MATCH_RATE: _ClassVar[MediationReportSpec.Metric]
        OBSERVED_ECPM: _ClassVar[MediationReportSpec.Metric]
    METRIC_UNSPECIFIED: MediationReportSpec.Metric
    AD_REQUESTS: MediationReportSpec.Metric
    CLICKS: MediationReportSpec.Metric
    ESTIMATED_EARNINGS: MediationReportSpec.Metric
    IMPRESSIONS: MediationReportSpec.Metric
    IMPRESSION_CTR: MediationReportSpec.Metric
    MATCHED_REQUESTS: MediationReportSpec.Metric
    MATCH_RATE: MediationReportSpec.Metric
    OBSERVED_ECPM: MediationReportSpec.Metric

    class DimensionFilter(_message.Message):
        __slots__ = ('matches_any', 'dimension')
        MATCHES_ANY_FIELD_NUMBER: _ClassVar[int]
        DIMENSION_FIELD_NUMBER: _ClassVar[int]
        matches_any: StringList
        dimension: MediationReportSpec.Dimension

        def __init__(self, matches_any: _Optional[_Union[StringList, _Mapping]]=..., dimension: _Optional[_Union[MediationReportSpec.Dimension, str]]=...) -> None:
            ...

    class SortCondition(_message.Message):
        __slots__ = ('dimension', 'metric', 'order')
        DIMENSION_FIELD_NUMBER: _ClassVar[int]
        METRIC_FIELD_NUMBER: _ClassVar[int]
        ORDER_FIELD_NUMBER: _ClassVar[int]
        dimension: MediationReportSpec.Dimension
        metric: MediationReportSpec.Metric
        order: SortOrder

        def __init__(self, dimension: _Optional[_Union[MediationReportSpec.Dimension, str]]=..., metric: _Optional[_Union[MediationReportSpec.Metric, str]]=..., order: _Optional[_Union[SortOrder, str]]=...) -> None:
            ...
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MAX_REPORT_ROWS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    date_range: DateRange
    dimensions: _containers.RepeatedScalarFieldContainer[MediationReportSpec.Dimension]
    metrics: _containers.RepeatedScalarFieldContainer[MediationReportSpec.Metric]
    dimension_filters: _containers.RepeatedCompositeFieldContainer[MediationReportSpec.DimensionFilter]
    sort_conditions: _containers.RepeatedCompositeFieldContainer[MediationReportSpec.SortCondition]
    localization_settings: LocalizationSettings
    max_report_rows: int
    time_zone: str

    def __init__(self, date_range: _Optional[_Union[DateRange, _Mapping]]=..., dimensions: _Optional[_Iterable[_Union[MediationReportSpec.Dimension, str]]]=..., metrics: _Optional[_Iterable[_Union[MediationReportSpec.Metric, str]]]=..., dimension_filters: _Optional[_Iterable[_Union[MediationReportSpec.DimensionFilter, _Mapping]]]=..., sort_conditions: _Optional[_Iterable[_Union[MediationReportSpec.SortCondition, _Mapping]]]=..., localization_settings: _Optional[_Union[LocalizationSettings, _Mapping]]=..., max_report_rows: _Optional[int]=..., time_zone: _Optional[str]=...) -> None:
        ...

class ReportRow(_message.Message):
    __slots__ = ('dimension_values', 'metric_values')

    class DimensionValue(_message.Message):
        __slots__ = ('value', 'display_label')
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_LABEL_FIELD_NUMBER: _ClassVar[int]
        value: str
        display_label: str

        def __init__(self, value: _Optional[str]=..., display_label: _Optional[str]=...) -> None:
            ...

    class MetricValue(_message.Message):
        __slots__ = ('integer_value', 'double_value', 'micros_value')
        INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        MICROS_VALUE_FIELD_NUMBER: _ClassVar[int]
        integer_value: int
        double_value: float
        micros_value: int

        def __init__(self, integer_value: _Optional[int]=..., double_value: _Optional[float]=..., micros_value: _Optional[int]=...) -> None:
            ...

    class DimensionValuesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReportRow.DimensionValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ReportRow.DimensionValue, _Mapping]]=...) -> None:
            ...

    class MetricValuesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReportRow.MetricValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ReportRow.MetricValue, _Mapping]]=...) -> None:
            ...
    DIMENSION_VALUES_FIELD_NUMBER: _ClassVar[int]
    METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    dimension_values: _containers.MessageMap[str, ReportRow.DimensionValue]
    metric_values: _containers.MessageMap[str, ReportRow.MetricValue]

    def __init__(self, dimension_values: _Optional[_Mapping[str, ReportRow.DimensionValue]]=..., metric_values: _Optional[_Mapping[str, ReportRow.MetricValue]]=...) -> None:
        ...

class ReportWarning(_message.Message):
    __slots__ = ('type', 'description')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[ReportWarning.Type]
        DATA_BEFORE_ACCOUNT_TIMEZONE_CHANGE: _ClassVar[ReportWarning.Type]
        DATA_DELAYED: _ClassVar[ReportWarning.Type]
        OTHER: _ClassVar[ReportWarning.Type]
        REPORT_CURRENCY_NOT_ACCOUNT_CURRENCY: _ClassVar[ReportWarning.Type]
    TYPE_UNSPECIFIED: ReportWarning.Type
    DATA_BEFORE_ACCOUNT_TIMEZONE_CHANGE: ReportWarning.Type
    DATA_DELAYED: ReportWarning.Type
    OTHER: ReportWarning.Type
    REPORT_CURRENCY_NOT_ACCOUNT_CURRENCY: ReportWarning.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    type: ReportWarning.Type
    description: str

    def __init__(self, type: _Optional[_Union[ReportWarning.Type, str]]=..., description: _Optional[str]=...) -> None:
        ...

class ReportHeader(_message.Message):
    __slots__ = ('date_range', 'localization_settings', 'reporting_time_zone')
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REPORTING_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    date_range: DateRange
    localization_settings: LocalizationSettings
    reporting_time_zone: str

    def __init__(self, date_range: _Optional[_Union[DateRange, _Mapping]]=..., localization_settings: _Optional[_Union[LocalizationSettings, _Mapping]]=..., reporting_time_zone: _Optional[str]=...) -> None:
        ...

class ReportFooter(_message.Message):
    __slots__ = ('warnings', 'matching_row_count')
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    MATCHING_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    warnings: _containers.RepeatedCompositeFieldContainer[ReportWarning]
    matching_row_count: int

    def __init__(self, warnings: _Optional[_Iterable[_Union[ReportWarning, _Mapping]]]=..., matching_row_count: _Optional[int]=...) -> None:
        ...

class DateRange(_message.Message):
    __slots__ = ('start_date', 'end_date')
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date

    def __init__(self, start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class LocalizationSettings(_message.Message):
    __slots__ = ('currency_code', 'language_code')
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    currency_code: str
    language_code: str

    def __init__(self, currency_code: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class StringList(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
        ...