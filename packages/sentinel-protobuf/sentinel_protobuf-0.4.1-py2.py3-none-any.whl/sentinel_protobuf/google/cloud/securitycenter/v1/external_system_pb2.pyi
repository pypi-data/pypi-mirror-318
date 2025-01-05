from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExternalSystem(_message.Message):
    __slots__ = ('name', 'assignees', 'external_uid', 'status', 'external_system_update_time', 'case_uri', 'case_priority', 'case_sla', 'case_create_time', 'case_close_time', 'ticket_info')

    class TicketInfo(_message.Message):
        __slots__ = ('id', 'assignee', 'description', 'uri', 'status', 'update_time')
        ID_FIELD_NUMBER: _ClassVar[int]
        ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        URI_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        id: str
        assignee: str
        description: str
        uri: str
        status: str
        update_time: _timestamp_pb2.Timestamp

        def __init__(self, id: _Optional[str]=..., assignee: _Optional[str]=..., description: _Optional[str]=..., uri: _Optional[str]=..., status: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SYSTEM_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CASE_URI_FIELD_NUMBER: _ClassVar[int]
    CASE_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CASE_SLA_FIELD_NUMBER: _ClassVar[int]
    CASE_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CASE_CLOSE_TIME_FIELD_NUMBER: _ClassVar[int]
    TICKET_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    assignees: _containers.RepeatedScalarFieldContainer[str]
    external_uid: str
    status: str
    external_system_update_time: _timestamp_pb2.Timestamp
    case_uri: str
    case_priority: str
    case_sla: _timestamp_pb2.Timestamp
    case_create_time: _timestamp_pb2.Timestamp
    case_close_time: _timestamp_pb2.Timestamp
    ticket_info: ExternalSystem.TicketInfo

    def __init__(self, name: _Optional[str]=..., assignees: _Optional[_Iterable[str]]=..., external_uid: _Optional[str]=..., status: _Optional[str]=..., external_system_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., case_uri: _Optional[str]=..., case_priority: _Optional[str]=..., case_sla: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., case_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., case_close_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., ticket_info: _Optional[_Union[ExternalSystem.TicketInfo, _Mapping]]=...) -> None:
        ...