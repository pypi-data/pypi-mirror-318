from google.ads.googleads.v18.enums import offline_conversion_diagnostic_status_enum_pb2 as _offline_conversion_diagnostic_status_enum_pb2
from google.ads.googleads.v18.enums import offline_event_upload_client_enum_pb2 as _offline_event_upload_client_enum_pb2
from google.ads.googleads.v18.errors import collection_size_error_pb2 as _collection_size_error_pb2
from google.ads.googleads.v18.errors import conversion_adjustment_upload_error_pb2 as _conversion_adjustment_upload_error_pb2
from google.ads.googleads.v18.errors import conversion_upload_error_pb2 as _conversion_upload_error_pb2
from google.ads.googleads.v18.errors import date_error_pb2 as _date_error_pb2
from google.ads.googleads.v18.errors import distinct_error_pb2 as _distinct_error_pb2
from google.ads.googleads.v18.errors import field_error_pb2 as _field_error_pb2
from google.ads.googleads.v18.errors import mutate_error_pb2 as _mutate_error_pb2
from google.ads.googleads.v18.errors import not_allowlisted_error_pb2 as _not_allowlisted_error_pb2
from google.ads.googleads.v18.errors import string_format_error_pb2 as _string_format_error_pb2
from google.ads.googleads.v18.errors import string_length_error_pb2 as _string_length_error_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OfflineConversionUploadClientSummary(_message.Message):
    __slots__ = ('resource_name', 'client', 'status', 'total_event_count', 'successful_event_count', 'success_rate', 'pending_event_count', 'pending_rate', 'last_upload_date_time', 'daily_summaries', 'job_summaries', 'alerts')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    PENDING_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_RATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPLOAD_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DAILY_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    JOB_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    client: _offline_event_upload_client_enum_pb2.OfflineEventUploadClientEnum.OfflineEventUploadClient
    status: _offline_conversion_diagnostic_status_enum_pb2.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    total_event_count: int
    successful_event_count: int
    success_rate: float
    pending_event_count: int
    pending_rate: float
    last_upload_date_time: str
    daily_summaries: _containers.RepeatedCompositeFieldContainer[OfflineConversionSummary]
    job_summaries: _containers.RepeatedCompositeFieldContainer[OfflineConversionSummary]
    alerts: _containers.RepeatedCompositeFieldContainer[OfflineConversionAlert]

    def __init__(self, resource_name: _Optional[str]=..., client: _Optional[_Union[_offline_event_upload_client_enum_pb2.OfflineEventUploadClientEnum.OfflineEventUploadClient, str]]=..., status: _Optional[_Union[_offline_conversion_diagnostic_status_enum_pb2.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus, str]]=..., total_event_count: _Optional[int]=..., successful_event_count: _Optional[int]=..., success_rate: _Optional[float]=..., pending_event_count: _Optional[int]=..., pending_rate: _Optional[float]=..., last_upload_date_time: _Optional[str]=..., daily_summaries: _Optional[_Iterable[_Union[OfflineConversionSummary, _Mapping]]]=..., job_summaries: _Optional[_Iterable[_Union[OfflineConversionSummary, _Mapping]]]=..., alerts: _Optional[_Iterable[_Union[OfflineConversionAlert, _Mapping]]]=...) -> None:
        ...

class OfflineConversionSummary(_message.Message):
    __slots__ = ('successful_count', 'failed_count', 'pending_count', 'job_id', 'upload_date')
    SUCCESSFUL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_COUNT_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_DATE_FIELD_NUMBER: _ClassVar[int]
    successful_count: int
    failed_count: int
    pending_count: int
    job_id: int
    upload_date: str

    def __init__(self, successful_count: _Optional[int]=..., failed_count: _Optional[int]=..., pending_count: _Optional[int]=..., job_id: _Optional[int]=..., upload_date: _Optional[str]=...) -> None:
        ...

class OfflineConversionAlert(_message.Message):
    __slots__ = ('error', 'error_percentage')
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    error: OfflineConversionError
    error_percentage: float

    def __init__(self, error: _Optional[_Union[OfflineConversionError, _Mapping]]=..., error_percentage: _Optional[float]=...) -> None:
        ...

class OfflineConversionError(_message.Message):
    __slots__ = ('collection_size_error', 'conversion_adjustment_upload_error', 'conversion_upload_error', 'date_error', 'distinct_error', 'field_error', 'mutate_error', 'not_allowlisted_error', 'string_format_error', 'string_length_error')
    COLLECTION_SIZE_ERROR_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ADJUSTMENT_UPLOAD_ERROR_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_UPLOAD_ERROR_FIELD_NUMBER: _ClassVar[int]
    DATE_ERROR_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_ERROR_FIELD_NUMBER: _ClassVar[int]
    FIELD_ERROR_FIELD_NUMBER: _ClassVar[int]
    MUTATE_ERROR_FIELD_NUMBER: _ClassVar[int]
    NOT_ALLOWLISTED_ERROR_FIELD_NUMBER: _ClassVar[int]
    STRING_FORMAT_ERROR_FIELD_NUMBER: _ClassVar[int]
    STRING_LENGTH_ERROR_FIELD_NUMBER: _ClassVar[int]
    collection_size_error: _collection_size_error_pb2.CollectionSizeErrorEnum.CollectionSizeError
    conversion_adjustment_upload_error: _conversion_adjustment_upload_error_pb2.ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    conversion_upload_error: _conversion_upload_error_pb2.ConversionUploadErrorEnum.ConversionUploadError
    date_error: _date_error_pb2.DateErrorEnum.DateError
    distinct_error: _distinct_error_pb2.DistinctErrorEnum.DistinctError
    field_error: _field_error_pb2.FieldErrorEnum.FieldError
    mutate_error: _mutate_error_pb2.MutateErrorEnum.MutateError
    not_allowlisted_error: _not_allowlisted_error_pb2.NotAllowlistedErrorEnum.NotAllowlistedError
    string_format_error: _string_format_error_pb2.StringFormatErrorEnum.StringFormatError
    string_length_error: _string_length_error_pb2.StringLengthErrorEnum.StringLengthError

    def __init__(self, collection_size_error: _Optional[_Union[_collection_size_error_pb2.CollectionSizeErrorEnum.CollectionSizeError, str]]=..., conversion_adjustment_upload_error: _Optional[_Union[_conversion_adjustment_upload_error_pb2.ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError, str]]=..., conversion_upload_error: _Optional[_Union[_conversion_upload_error_pb2.ConversionUploadErrorEnum.ConversionUploadError, str]]=..., date_error: _Optional[_Union[_date_error_pb2.DateErrorEnum.DateError, str]]=..., distinct_error: _Optional[_Union[_distinct_error_pb2.DistinctErrorEnum.DistinctError, str]]=..., field_error: _Optional[_Union[_field_error_pb2.FieldErrorEnum.FieldError, str]]=..., mutate_error: _Optional[_Union[_mutate_error_pb2.MutateErrorEnum.MutateError, str]]=..., not_allowlisted_error: _Optional[_Union[_not_allowlisted_error_pb2.NotAllowlistedErrorEnum.NotAllowlistedError, str]]=..., string_format_error: _Optional[_Union[_string_format_error_pb2.StringFormatErrorEnum.StringFormatError, str]]=..., string_length_error: _Optional[_Union[_string_length_error_pb2.StringLengthErrorEnum.StringLengthError, str]]=...) -> None:
        ...