from google.ads.admanager.v1 import custom_targeting_value_enums_pb2 as _custom_targeting_value_enums_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomTargetingValue(_message.Message):
    __slots__ = ('name', 'ad_tag_name', 'display_name', 'match_type', 'status')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AD_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    ad_tag_name: str
    display_name: str
    match_type: _custom_targeting_value_enums_pb2.CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType
    status: _custom_targeting_value_enums_pb2.CustomTargetingValueStatusEnum.CustomTargetingValueStatus

    def __init__(self, name: _Optional[str]=..., ad_tag_name: _Optional[str]=..., display_name: _Optional[str]=..., match_type: _Optional[_Union[_custom_targeting_value_enums_pb2.CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchType, str]]=..., status: _Optional[_Union[_custom_targeting_value_enums_pb2.CustomTargetingValueStatusEnum.CustomTargetingValueStatus, str]]=...) -> None:
        ...