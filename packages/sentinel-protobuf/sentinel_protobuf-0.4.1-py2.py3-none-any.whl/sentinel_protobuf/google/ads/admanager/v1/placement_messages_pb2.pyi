from google.ads.admanager.v1 import placement_enums_pb2 as _placement_enums_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Placement(_message.Message):
    __slots__ = ('name', 'placement_id', 'display_name', 'description', 'placement_code', 'status', 'targeted_ad_units', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TARGETED_AD_UNITS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    placement_id: int
    display_name: str
    description: str
    placement_code: str
    status: _placement_enums_pb2.PlacementStatusEnum.PlacementStatus
    targeted_ad_units: _containers.RepeatedScalarFieldContainer[str]
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., placement_id: _Optional[int]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., placement_code: _Optional[str]=..., status: _Optional[_Union[_placement_enums_pb2.PlacementStatusEnum.PlacementStatus, str]]=..., targeted_ad_units: _Optional[_Iterable[str]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...