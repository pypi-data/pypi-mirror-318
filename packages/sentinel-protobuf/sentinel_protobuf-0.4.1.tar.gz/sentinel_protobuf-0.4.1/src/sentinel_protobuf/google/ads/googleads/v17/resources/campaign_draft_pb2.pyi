from google.ads.googleads.v17.enums import campaign_draft_status_pb2 as _campaign_draft_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignDraft(_message.Message):
    __slots__ = ("resource_name", "draft_id", "base_campaign", "name", "draft_campaign", "status", "has_experiment_running", "long_running_operation")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DRAFT_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HAS_EXPERIMENT_RUNNING_FIELD_NUMBER: _ClassVar[int]
    LONG_RUNNING_OPERATION_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    draft_id: int
    base_campaign: str
    name: str
    draft_campaign: str
    status: _campaign_draft_status_pb2.CampaignDraftStatusEnum.CampaignDraftStatus
    has_experiment_running: bool
    long_running_operation: str
    def __init__(self, resource_name: _Optional[str] = ..., draft_id: _Optional[int] = ..., base_campaign: _Optional[str] = ..., name: _Optional[str] = ..., draft_campaign: _Optional[str] = ..., status: _Optional[_Union[_campaign_draft_status_pb2.CampaignDraftStatusEnum.CampaignDraftStatus, str]] = ..., has_experiment_running: bool = ..., long_running_operation: _Optional[str] = ...) -> None: ...
