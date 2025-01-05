from google.ads.searchads360.v0.common import criteria_pb2 as _criteria_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupSignal(_message.Message):
    __slots__ = ("resource_name", "asset_group", "audience")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_group: str
    audience: _criteria_pb2.AudienceInfo
    def __init__(self, resource_name: _Optional[str] = ..., asset_group: _Optional[str] = ..., audience: _Optional[_Union[_criteria_pb2.AudienceInfo, _Mapping]] = ...) -> None: ...
