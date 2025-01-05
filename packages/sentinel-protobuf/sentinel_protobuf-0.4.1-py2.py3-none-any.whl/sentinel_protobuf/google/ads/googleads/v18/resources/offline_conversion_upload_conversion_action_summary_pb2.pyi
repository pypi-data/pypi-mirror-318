from google.ads.googleads.v18.enums import offline_conversion_diagnostic_status_enum_pb2 as _offline_conversion_diagnostic_status_enum_pb2
from google.ads.googleads.v18.enums import offline_event_upload_client_enum_pb2 as _offline_event_upload_client_enum_pb2
from google.ads.googleads.v18.resources import offline_conversion_upload_client_summary_pb2 as _offline_conversion_upload_client_summary_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OfflineConversionUploadConversionActionSummary(_message.Message):
    __slots__ = ('resource_name', 'client', 'conversion_action_id', 'conversion_action_name', 'status', 'total_event_count', 'successful_event_count', 'pending_event_count', 'last_upload_date_time', 'daily_summaries', 'job_summaries', 'alerts')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPLOAD_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DAILY_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    JOB_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    client: _offline_event_upload_client_enum_pb2.OfflineEventUploadClientEnum.OfflineEventUploadClient
    conversion_action_id: int
    conversion_action_name: str
    status: _offline_conversion_diagnostic_status_enum_pb2.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    total_event_count: int
    successful_event_count: int
    pending_event_count: int
    last_upload_date_time: str
    daily_summaries: _containers.RepeatedCompositeFieldContainer[_offline_conversion_upload_client_summary_pb2.OfflineConversionSummary]
    job_summaries: _containers.RepeatedCompositeFieldContainer[_offline_conversion_upload_client_summary_pb2.OfflineConversionSummary]
    alerts: _containers.RepeatedCompositeFieldContainer[_offline_conversion_upload_client_summary_pb2.OfflineConversionAlert]

    def __init__(self, resource_name: _Optional[str]=..., client: _Optional[_Union[_offline_event_upload_client_enum_pb2.OfflineEventUploadClientEnum.OfflineEventUploadClient, str]]=..., conversion_action_id: _Optional[int]=..., conversion_action_name: _Optional[str]=..., status: _Optional[_Union[_offline_conversion_diagnostic_status_enum_pb2.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus, str]]=..., total_event_count: _Optional[int]=..., successful_event_count: _Optional[int]=..., pending_event_count: _Optional[int]=..., last_upload_date_time: _Optional[str]=..., daily_summaries: _Optional[_Iterable[_Union[_offline_conversion_upload_client_summary_pb2.OfflineConversionSummary, _Mapping]]]=..., job_summaries: _Optional[_Iterable[_Union[_offline_conversion_upload_client_summary_pb2.OfflineConversionSummary, _Mapping]]]=..., alerts: _Optional[_Iterable[_Union[_offline_conversion_upload_client_summary_pb2.OfflineConversionAlert, _Mapping]]]=...) -> None:
        ...