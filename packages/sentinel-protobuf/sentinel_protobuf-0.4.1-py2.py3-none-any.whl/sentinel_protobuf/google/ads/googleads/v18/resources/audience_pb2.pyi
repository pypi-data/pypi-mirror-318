from google.ads.googleads.v18.common import audiences_pb2 as _audiences_pb2
from google.ads.googleads.v18.enums import audience_scope_pb2 as _audience_scope_pb2
from google.ads.googleads.v18.enums import audience_status_pb2 as _audience_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Audience(_message.Message):
    __slots__ = ("resource_name", "id", "status", "name", "description", "dimensions", "exclusion_dimension", "scope", "asset_group")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    status: _audience_status_pb2.AudienceStatusEnum.AudienceStatus
    name: str
    description: str
    dimensions: _containers.RepeatedCompositeFieldContainer[_audiences_pb2.AudienceDimension]
    exclusion_dimension: _audiences_pb2.AudienceExclusionDimension
    scope: _audience_scope_pb2.AudienceScopeEnum.AudienceScope
    asset_group: str
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., status: _Optional[_Union[_audience_status_pb2.AudienceStatusEnum.AudienceStatus, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[_audiences_pb2.AudienceDimension, _Mapping]]] = ..., exclusion_dimension: _Optional[_Union[_audiences_pb2.AudienceExclusionDimension, _Mapping]] = ..., scope: _Optional[_Union[_audience_scope_pb2.AudienceScopeEnum.AudienceScope, str]] = ..., asset_group: _Optional[str] = ...) -> None: ...
