from google.ads.googleads.v16.enums import campaign_shared_set_status_pb2 as _campaign_shared_set_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignSharedSet(_message.Message):
    __slots__ = ("resource_name", "campaign", "shared_set", "status")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    SHARED_SET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign: str
    shared_set: str
    status: _campaign_shared_set_status_pb2.CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    def __init__(self, resource_name: _Optional[str] = ..., campaign: _Optional[str] = ..., shared_set: _Optional[str] = ..., status: _Optional[_Union[_campaign_shared_set_status_pb2.CampaignSharedSetStatusEnum.CampaignSharedSetStatus, str]] = ...) -> None: ...
