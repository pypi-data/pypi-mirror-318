from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.channel.v1 import operations_pb2 as _operations_pb2
from google.longrunning import operations_pb2 as _operations_pb2_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.type import decimal_pb2 as _decimal_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RunReportJobRequest(_message.Message):
    __slots__ = ('name', 'date_range', 'filter', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    date_range: DateRange
    filter: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., date_range: _Optional[_Union[DateRange, _Mapping]]=..., filter: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class RunReportJobResponse(_message.Message):
    __slots__ = ('report_job', 'report_metadata')
    REPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    REPORT_METADATA_FIELD_NUMBER: _ClassVar[int]
    report_job: ReportJob
    report_metadata: ReportResultsMetadata

    def __init__(self, report_job: _Optional[_Union[ReportJob, _Mapping]]=..., report_metadata: _Optional[_Union[ReportResultsMetadata, _Mapping]]=...) -> None:
        ...

class FetchReportResultsRequest(_message.Message):
    __slots__ = ('report_job', 'page_size', 'page_token', 'partition_keys')
    REPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEYS_FIELD_NUMBER: _ClassVar[int]
    report_job: str
    page_size: int
    page_token: str
    partition_keys: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, report_job: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., partition_keys: _Optional[_Iterable[str]]=...) -> None:
        ...

class FetchReportResultsResponse(_message.Message):
    __slots__ = ('report_metadata', 'rows', 'next_page_token')
    REPORT_METADATA_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    report_metadata: ReportResultsMetadata
    rows: _containers.RepeatedCompositeFieldContainer[Row]
    next_page_token: str

    def __init__(self, report_metadata: _Optional[_Union[ReportResultsMetadata, _Mapping]]=..., rows: _Optional[_Iterable[_Union[Row, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListReportsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    language_code: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListReportsResponse(_message.Message):
    __slots__ = ('reports', 'next_page_token')
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[Report]
    next_page_token: str

    def __init__(self, reports: _Optional[_Iterable[_Union[Report, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ReportJob(_message.Message):
    __slots__ = ('name', 'report_status')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    report_status: ReportStatus

    def __init__(self, name: _Optional[str]=..., report_status: _Optional[_Union[ReportStatus, _Mapping]]=...) -> None:
        ...

class ReportResultsMetadata(_message.Message):
    __slots__ = ('report', 'row_count', 'date_range', 'preceding_date_range')
    REPORT_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    PRECEDING_DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    report: Report
    row_count: int
    date_range: DateRange
    preceding_date_range: DateRange

    def __init__(self, report: _Optional[_Union[Report, _Mapping]]=..., row_count: _Optional[int]=..., date_range: _Optional[_Union[DateRange, _Mapping]]=..., preceding_date_range: _Optional[_Union[DateRange, _Mapping]]=...) -> None:
        ...

class Column(_message.Message):
    __slots__ = ('column_id', 'display_name', 'data_type')

    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[Column.DataType]
        STRING: _ClassVar[Column.DataType]
        INT: _ClassVar[Column.DataType]
        DECIMAL: _ClassVar[Column.DataType]
        MONEY: _ClassVar[Column.DataType]
        DATE: _ClassVar[Column.DataType]
        DATE_TIME: _ClassVar[Column.DataType]
    DATA_TYPE_UNSPECIFIED: Column.DataType
    STRING: Column.DataType
    INT: Column.DataType
    DECIMAL: Column.DataType
    MONEY: Column.DataType
    DATE: Column.DataType
    DATE_TIME: Column.DataType
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    column_id: str
    display_name: str
    data_type: Column.DataType

    def __init__(self, column_id: _Optional[str]=..., display_name: _Optional[str]=..., data_type: _Optional[_Union[Column.DataType, str]]=...) -> None:
        ...

class DateRange(_message.Message):
    __slots__ = ('usage_start_date_time', 'usage_end_date_time', 'invoice_start_date', 'invoice_end_date')
    USAGE_START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    USAGE_END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INVOICE_START_DATE_FIELD_NUMBER: _ClassVar[int]
    INVOICE_END_DATE_FIELD_NUMBER: _ClassVar[int]
    usage_start_date_time: _datetime_pb2.DateTime
    usage_end_date_time: _datetime_pb2.DateTime
    invoice_start_date: _date_pb2.Date
    invoice_end_date: _date_pb2.Date

    def __init__(self, usage_start_date_time: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., usage_end_date_time: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., invoice_start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., invoice_end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class Row(_message.Message):
    __slots__ = ('values', 'partition_key')
    VALUES_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[ReportValue]
    partition_key: str

    def __init__(self, values: _Optional[_Iterable[_Union[ReportValue, _Mapping]]]=..., partition_key: _Optional[str]=...) -> None:
        ...

class ReportValue(_message.Message):
    __slots__ = ('string_value', 'int_value', 'decimal_value', 'money_value', 'date_value', 'date_time_value')
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    MONEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    int_value: int
    decimal_value: _decimal_pb2.Decimal
    money_value: _money_pb2.Money
    date_value: _date_pb2.Date
    date_time_value: _datetime_pb2.DateTime

    def __init__(self, string_value: _Optional[str]=..., int_value: _Optional[int]=..., decimal_value: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]]=..., money_value: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., date_value: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., date_time_value: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=...) -> None:
        ...

class ReportStatus(_message.Message):
    __slots__ = ('state', 'start_time', 'end_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ReportStatus.State]
        STARTED: _ClassVar[ReportStatus.State]
        WRITING: _ClassVar[ReportStatus.State]
        AVAILABLE: _ClassVar[ReportStatus.State]
        FAILED: _ClassVar[ReportStatus.State]
    STATE_UNSPECIFIED: ReportStatus.State
    STARTED: ReportStatus.State
    WRITING: ReportStatus.State
    AVAILABLE: ReportStatus.State
    FAILED: ReportStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    state: ReportStatus.State
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[ReportStatus.State, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Report(_message.Message):
    __slots__ = ('name', 'display_name', 'columns', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    description: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., columns: _Optional[_Iterable[_Union[Column, _Mapping]]]=..., description: _Optional[str]=...) -> None:
        ...