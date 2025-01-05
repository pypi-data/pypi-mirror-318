from google.ads.googleads.v18.enums import custom_audience_member_type_pb2 as _custom_audience_member_type_pb2
from google.ads.googleads.v18.enums import custom_audience_status_pb2 as _custom_audience_status_pb2
from google.ads.googleads.v18.enums import custom_audience_type_pb2 as _custom_audience_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomAudience(_message.Message):
    __slots__ = ('resource_name', 'id', 'status', 'name', 'type', 'description', 'members')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    status: _custom_audience_status_pb2.CustomAudienceStatusEnum.CustomAudienceStatus
    name: str
    type: _custom_audience_type_pb2.CustomAudienceTypeEnum.CustomAudienceType
    description: str
    members: _containers.RepeatedCompositeFieldContainer[CustomAudienceMember]

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., status: _Optional[_Union[_custom_audience_status_pb2.CustomAudienceStatusEnum.CustomAudienceStatus, str]]=..., name: _Optional[str]=..., type: _Optional[_Union[_custom_audience_type_pb2.CustomAudienceTypeEnum.CustomAudienceType, str]]=..., description: _Optional[str]=..., members: _Optional[_Iterable[_Union[CustomAudienceMember, _Mapping]]]=...) -> None:
        ...

class CustomAudienceMember(_message.Message):
    __slots__ = ('member_type', 'keyword', 'url', 'place_category', 'app')
    MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PLACE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    member_type: _custom_audience_member_type_pb2.CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    keyword: str
    url: str
    place_category: int
    app: str

    def __init__(self, member_type: _Optional[_Union[_custom_audience_member_type_pb2.CustomAudienceMemberTypeEnum.CustomAudienceMemberType, str]]=..., keyword: _Optional[str]=..., url: _Optional[str]=..., place_category: _Optional[int]=..., app: _Optional[str]=...) -> None:
        ...