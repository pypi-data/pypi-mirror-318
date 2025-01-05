from google.ads.googleads.v16.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v16.enums import smart_campaign_not_eligible_reason_pb2 as _smart_campaign_not_eligible_reason_pb2
from google.ads.googleads.v16.enums import smart_campaign_status_pb2 as _smart_campaign_status_pb2
from google.ads.googleads.v16.resources import smart_campaign_setting_pb2 as _smart_campaign_setting_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSmartCampaignStatusRequest(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class SmartCampaignNotEligibleDetails(_message.Message):
    __slots__ = ("not_eligible_reason",)
    NOT_ELIGIBLE_REASON_FIELD_NUMBER: _ClassVar[int]
    not_eligible_reason: _smart_campaign_not_eligible_reason_pb2.SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    def __init__(self, not_eligible_reason: _Optional[_Union[_smart_campaign_not_eligible_reason_pb2.SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason, str]] = ...) -> None: ...

class SmartCampaignEligibleDetails(_message.Message):
    __slots__ = ("last_impression_date_time", "end_date_time")
    LAST_IMPRESSION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    last_impression_date_time: str
    end_date_time: str
    def __init__(self, last_impression_date_time: _Optional[str] = ..., end_date_time: _Optional[str] = ...) -> None: ...

class SmartCampaignPausedDetails(_message.Message):
    __slots__ = ("paused_date_time",)
    PAUSED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    paused_date_time: str
    def __init__(self, paused_date_time: _Optional[str] = ...) -> None: ...

class SmartCampaignRemovedDetails(_message.Message):
    __slots__ = ("removed_date_time",)
    REMOVED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    removed_date_time: str
    def __init__(self, removed_date_time: _Optional[str] = ...) -> None: ...

class SmartCampaignEndedDetails(_message.Message):
    __slots__ = ("end_date_time",)
    END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    end_date_time: str
    def __init__(self, end_date_time: _Optional[str] = ...) -> None: ...

class GetSmartCampaignStatusResponse(_message.Message):
    __slots__ = ("smart_campaign_status", "not_eligible_details", "eligible_details", "paused_details", "removed_details", "ended_details")
    SMART_CAMPAIGN_STATUS_FIELD_NUMBER: _ClassVar[int]
    NOT_ELIGIBLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PAUSED_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ENDED_DETAILS_FIELD_NUMBER: _ClassVar[int]
    smart_campaign_status: _smart_campaign_status_pb2.SmartCampaignStatusEnum.SmartCampaignStatus
    not_eligible_details: SmartCampaignNotEligibleDetails
    eligible_details: SmartCampaignEligibleDetails
    paused_details: SmartCampaignPausedDetails
    removed_details: SmartCampaignRemovedDetails
    ended_details: SmartCampaignEndedDetails
    def __init__(self, smart_campaign_status: _Optional[_Union[_smart_campaign_status_pb2.SmartCampaignStatusEnum.SmartCampaignStatus, str]] = ..., not_eligible_details: _Optional[_Union[SmartCampaignNotEligibleDetails, _Mapping]] = ..., eligible_details: _Optional[_Union[SmartCampaignEligibleDetails, _Mapping]] = ..., paused_details: _Optional[_Union[SmartCampaignPausedDetails, _Mapping]] = ..., removed_details: _Optional[_Union[SmartCampaignRemovedDetails, _Mapping]] = ..., ended_details: _Optional[_Union[SmartCampaignEndedDetails, _Mapping]] = ...) -> None: ...

class MutateSmartCampaignSettingsRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure", "validate_only", "response_content_type")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[SmartCampaignSettingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[SmartCampaignSettingOperation, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class SmartCampaignSettingOperation(_message.Message):
    __slots__ = ("update", "update_mask")
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    update: _smart_campaign_setting_pb2.SmartCampaignSetting
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, update: _Optional[_Union[_smart_campaign_setting_pb2.SmartCampaignSetting, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class MutateSmartCampaignSettingsResponse(_message.Message):
    __slots__ = ("partial_failure_error", "results")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[MutateSmartCampaignSettingResult]
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[MutateSmartCampaignSettingResult, _Mapping]]] = ...) -> None: ...

class MutateSmartCampaignSettingResult(_message.Message):
    __slots__ = ("resource_name", "smart_campaign_setting")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SMART_CAMPAIGN_SETTING_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    smart_campaign_setting: _smart_campaign_setting_pb2.SmartCampaignSetting
    def __init__(self, resource_name: _Optional[str] = ..., smart_campaign_setting: _Optional[_Union[_smart_campaign_setting_pb2.SmartCampaignSetting, _Mapping]] = ...) -> None: ...
