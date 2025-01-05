from google.ads.searchads360.v0.common import criteria_pb2 as _criteria_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupBidModifier(_message.Message):
    __slots__ = ("resource_name", "bid_modifier", "device")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    bid_modifier: float
    device: _criteria_pb2.DeviceInfo
    def __init__(self, resource_name: _Optional[str] = ..., bid_modifier: _Optional[float] = ..., device: _Optional[_Union[_criteria_pb2.DeviceInfo, _Mapping]] = ...) -> None: ...
