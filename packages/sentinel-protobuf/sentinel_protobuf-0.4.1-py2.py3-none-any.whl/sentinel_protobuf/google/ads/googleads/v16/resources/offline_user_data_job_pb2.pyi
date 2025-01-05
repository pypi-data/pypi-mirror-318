from google.ads.googleads.v16.common import offline_user_data_pb2 as _offline_user_data_pb2
from google.ads.googleads.v16.enums import offline_user_data_job_failure_reason_pb2 as _offline_user_data_job_failure_reason_pb2
from google.ads.googleads.v16.enums import offline_user_data_job_match_rate_range_pb2 as _offline_user_data_job_match_rate_range_pb2
from google.ads.googleads.v16.enums import offline_user_data_job_status_pb2 as _offline_user_data_job_status_pb2
from google.ads.googleads.v16.enums import offline_user_data_job_type_pb2 as _offline_user_data_job_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OfflineUserDataJob(_message.Message):
    __slots__ = ("resource_name", "id", "external_id", "type", "status", "failure_reason", "operation_metadata", "customer_match_user_list_metadata", "store_sales_metadata")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MATCH_USER_LIST_METADATA_FIELD_NUMBER: _ClassVar[int]
    STORE_SALES_METADATA_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    external_id: int
    type: _offline_user_data_job_type_pb2.OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    status: _offline_user_data_job_status_pb2.OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    failure_reason: _offline_user_data_job_failure_reason_pb2.OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    operation_metadata: OfflineUserDataJobMetadata
    customer_match_user_list_metadata: _offline_user_data_pb2.CustomerMatchUserListMetadata
    store_sales_metadata: _offline_user_data_pb2.StoreSalesMetadata
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., external_id: _Optional[int] = ..., type: _Optional[_Union[_offline_user_data_job_type_pb2.OfflineUserDataJobTypeEnum.OfflineUserDataJobType, str]] = ..., status: _Optional[_Union[_offline_user_data_job_status_pb2.OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus, str]] = ..., failure_reason: _Optional[_Union[_offline_user_data_job_failure_reason_pb2.OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason, str]] = ..., operation_metadata: _Optional[_Union[OfflineUserDataJobMetadata, _Mapping]] = ..., customer_match_user_list_metadata: _Optional[_Union[_offline_user_data_pb2.CustomerMatchUserListMetadata, _Mapping]] = ..., store_sales_metadata: _Optional[_Union[_offline_user_data_pb2.StoreSalesMetadata, _Mapping]] = ...) -> None: ...

class OfflineUserDataJobMetadata(_message.Message):
    __slots__ = ("match_rate_range",)
    MATCH_RATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    match_rate_range: _offline_user_data_job_match_rate_range_pb2.OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange
    def __init__(self, match_rate_range: _Optional[_Union[_offline_user_data_job_match_rate_range_pb2.OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange, str]] = ...) -> None: ...
