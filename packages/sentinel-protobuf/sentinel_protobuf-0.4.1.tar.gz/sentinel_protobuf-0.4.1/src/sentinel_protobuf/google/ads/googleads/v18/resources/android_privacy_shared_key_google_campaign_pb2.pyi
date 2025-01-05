from google.ads.googleads.v18.enums import android_privacy_interaction_type_pb2 as _android_privacy_interaction_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AndroidPrivacySharedKeyGoogleCampaign(_message.Message):
    __slots__ = ('resource_name', 'campaign_id', 'android_privacy_interaction_type', 'android_privacy_interaction_date', 'shared_campaign_key')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    ANDROID_PRIVACY_INTERACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANDROID_PRIVACY_INTERACTION_DATE_FIELD_NUMBER: _ClassVar[int]
    SHARED_CAMPAIGN_KEY_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign_id: int
    android_privacy_interaction_type: _android_privacy_interaction_type_pb2.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    android_privacy_interaction_date: str
    shared_campaign_key: str

    def __init__(self, resource_name: _Optional[str]=..., campaign_id: _Optional[int]=..., android_privacy_interaction_type: _Optional[_Union[_android_privacy_interaction_type_pb2.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType, str]]=..., android_privacy_interaction_date: _Optional[str]=..., shared_campaign_key: _Optional[str]=...) -> None:
        ...