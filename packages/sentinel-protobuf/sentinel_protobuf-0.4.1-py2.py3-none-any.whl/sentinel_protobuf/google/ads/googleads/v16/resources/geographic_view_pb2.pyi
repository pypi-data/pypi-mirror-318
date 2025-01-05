from google.ads.googleads.v16.enums import geo_targeting_type_pb2 as _geo_targeting_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeographicView(_message.Message):
    __slots__ = ("resource_name", "location_type", "country_criterion_id")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    location_type: _geo_targeting_type_pb2.GeoTargetingTypeEnum.GeoTargetingType
    country_criterion_id: int
    def __init__(self, resource_name: _Optional[str] = ..., location_type: _Optional[_Union[_geo_targeting_type_pb2.GeoTargetingTypeEnum.GeoTargetingType, str]] = ..., country_criterion_id: _Optional[int] = ...) -> None: ...
