from google.ads.admanager.v1 import custom_targeting_key_enums_pb2 as _custom_targeting_key_enums_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomTargetingKey(_message.Message):
    __slots__ = ('name', 'custom_targeting_key_id', 'ad_tag_name', 'display_name', 'type', 'status', 'reportable_type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGETING_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AD_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REPORTABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    custom_targeting_key_id: int
    ad_tag_name: str
    display_name: str
    type: _custom_targeting_key_enums_pb2.CustomTargetingKeyTypeEnum.CustomTargetingKeyType
    status: _custom_targeting_key_enums_pb2.CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus
    reportable_type: _custom_targeting_key_enums_pb2.CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType

    def __init__(self, name: _Optional[str]=..., custom_targeting_key_id: _Optional[int]=..., ad_tag_name: _Optional[str]=..., display_name: _Optional[str]=..., type: _Optional[_Union[_custom_targeting_key_enums_pb2.CustomTargetingKeyTypeEnum.CustomTargetingKeyType, str]]=..., status: _Optional[_Union[_custom_targeting_key_enums_pb2.CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus, str]]=..., reportable_type: _Optional[_Union[_custom_targeting_key_enums_pb2.CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType, str]]=...) -> None:
        ...