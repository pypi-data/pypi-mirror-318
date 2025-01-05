from google.ads.googleads.v17.enums import placement_type_pb2 as _placement_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupPlacementView(_message.Message):
    __slots__ = ("resource_name", "placement", "display_name", "target_url", "placement_type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_URL_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    placement: str
    display_name: str
    target_url: str
    placement_type: _placement_type_pb2.PlacementTypeEnum.PlacementType
    def __init__(self, resource_name: _Optional[str] = ..., placement: _Optional[str] = ..., display_name: _Optional[str] = ..., target_url: _Optional[str] = ..., placement_type: _Optional[_Union[_placement_type_pb2.PlacementTypeEnum.PlacementType, str]] = ...) -> None: ...
