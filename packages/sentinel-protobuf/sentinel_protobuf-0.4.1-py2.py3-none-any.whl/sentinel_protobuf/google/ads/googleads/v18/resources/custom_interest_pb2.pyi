from google.ads.googleads.v18.enums import custom_interest_member_type_pb2 as _custom_interest_member_type_pb2
from google.ads.googleads.v18.enums import custom_interest_status_pb2 as _custom_interest_status_pb2
from google.ads.googleads.v18.enums import custom_interest_type_pb2 as _custom_interest_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomInterest(_message.Message):
    __slots__ = ("resource_name", "id", "status", "name", "type", "description", "members")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    status: _custom_interest_status_pb2.CustomInterestStatusEnum.CustomInterestStatus
    name: str
    type: _custom_interest_type_pb2.CustomInterestTypeEnum.CustomInterestType
    description: str
    members: _containers.RepeatedCompositeFieldContainer[CustomInterestMember]
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., status: _Optional[_Union[_custom_interest_status_pb2.CustomInterestStatusEnum.CustomInterestStatus, str]] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_custom_interest_type_pb2.CustomInterestTypeEnum.CustomInterestType, str]] = ..., description: _Optional[str] = ..., members: _Optional[_Iterable[_Union[CustomInterestMember, _Mapping]]] = ...) -> None: ...

class CustomInterestMember(_message.Message):
    __slots__ = ("member_type", "parameter")
    MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    member_type: _custom_interest_member_type_pb2.CustomInterestMemberTypeEnum.CustomInterestMemberType
    parameter: str
    def __init__(self, member_type: _Optional[_Union[_custom_interest_member_type_pb2.CustomInterestMemberTypeEnum.CustomInterestMemberType, str]] = ..., parameter: _Optional[str] = ...) -> None: ...
