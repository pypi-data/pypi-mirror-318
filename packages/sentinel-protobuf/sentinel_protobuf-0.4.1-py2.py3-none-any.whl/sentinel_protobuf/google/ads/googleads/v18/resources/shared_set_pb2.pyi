from google.ads.googleads.v18.enums import shared_set_status_pb2 as _shared_set_status_pb2
from google.ads.googleads.v18.enums import shared_set_type_pb2 as _shared_set_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SharedSet(_message.Message):
    __slots__ = ("resource_name", "id", "type", "name", "status", "member_count", "reference_count")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    type: _shared_set_type_pb2.SharedSetTypeEnum.SharedSetType
    name: str
    status: _shared_set_status_pb2.SharedSetStatusEnum.SharedSetStatus
    member_count: int
    reference_count: int
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., type: _Optional[_Union[_shared_set_type_pb2.SharedSetTypeEnum.SharedSetType, str]] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_shared_set_status_pb2.SharedSetStatusEnum.SharedSetStatus, str]] = ..., member_count: _Optional[int] = ..., reference_count: _Optional[int] = ...) -> None: ...
