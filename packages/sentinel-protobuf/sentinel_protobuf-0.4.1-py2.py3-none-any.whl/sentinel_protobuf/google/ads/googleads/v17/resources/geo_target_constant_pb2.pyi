from google.ads.googleads.v17.enums import geo_target_constant_status_pb2 as _geo_target_constant_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeoTargetConstant(_message.Message):
    __slots__ = ("resource_name", "id", "name", "country_code", "target_type", "status", "canonical_name", "parent_geo_target")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_GEO_TARGET_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    country_code: str
    target_type: str
    status: _geo_target_constant_status_pb2.GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    canonical_name: str
    parent_geo_target: str
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., country_code: _Optional[str] = ..., target_type: _Optional[str] = ..., status: _Optional[_Union[_geo_target_constant_status_pb2.GeoTargetConstantStatusEnum.GeoTargetConstantStatus, str]] = ..., canonical_name: _Optional[str] = ..., parent_geo_target: _Optional[str] = ...) -> None: ...
