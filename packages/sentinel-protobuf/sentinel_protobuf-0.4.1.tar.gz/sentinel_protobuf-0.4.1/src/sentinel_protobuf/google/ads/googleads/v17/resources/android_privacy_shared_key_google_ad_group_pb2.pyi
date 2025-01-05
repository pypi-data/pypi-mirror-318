from google.ads.googleads.v17.enums import android_privacy_interaction_type_pb2 as _android_privacy_interaction_type_pb2
from google.ads.googleads.v17.enums import android_privacy_network_type_pb2 as _android_privacy_network_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AndroidPrivacySharedKeyGoogleAdGroup(_message.Message):
    __slots__ = ('resource_name', 'campaign_id', 'android_privacy_interaction_type', 'android_privacy_interaction_date', 'android_privacy_network_type', 'ad_group_id', 'shared_ad_group_key')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    ANDROID_PRIVACY_INTERACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANDROID_PRIVACY_INTERACTION_DATE_FIELD_NUMBER: _ClassVar[int]
    ANDROID_PRIVACY_NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SHARED_AD_GROUP_KEY_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign_id: int
    android_privacy_interaction_type: _android_privacy_interaction_type_pb2.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    android_privacy_interaction_date: str
    android_privacy_network_type: _android_privacy_network_type_pb2.AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    ad_group_id: int
    shared_ad_group_key: str

    def __init__(self, resource_name: _Optional[str]=..., campaign_id: _Optional[int]=..., android_privacy_interaction_type: _Optional[_Union[_android_privacy_interaction_type_pb2.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType, str]]=..., android_privacy_interaction_date: _Optional[str]=..., android_privacy_network_type: _Optional[_Union[_android_privacy_network_type_pb2.AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType, str]]=..., ad_group_id: _Optional[int]=..., shared_ad_group_key: _Optional[str]=...) -> None:
        ...