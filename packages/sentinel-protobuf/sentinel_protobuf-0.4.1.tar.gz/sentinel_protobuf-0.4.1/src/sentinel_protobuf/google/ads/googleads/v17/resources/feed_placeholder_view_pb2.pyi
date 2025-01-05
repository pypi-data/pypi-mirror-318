from google.ads.googleads.v17.enums import placeholder_type_pb2 as _placeholder_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeedPlaceholderView(_message.Message):
    __slots__ = ('resource_name', 'placeholder_type')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    placeholder_type: _placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType

    def __init__(self, resource_name: _Optional[str]=..., placeholder_type: _Optional[_Union[_placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType, str]]=...) -> None:
        ...