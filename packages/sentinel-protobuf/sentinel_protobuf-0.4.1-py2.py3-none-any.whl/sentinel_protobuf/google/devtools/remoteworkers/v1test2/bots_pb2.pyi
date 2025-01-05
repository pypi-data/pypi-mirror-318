from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.remoteworkers.v1test2 import worker_pb2 as _worker_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BotStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BOT_STATUS_UNSPECIFIED: _ClassVar[BotStatus]
    OK: _ClassVar[BotStatus]
    UNHEALTHY: _ClassVar[BotStatus]
    HOST_REBOOTING: _ClassVar[BotStatus]
    BOT_TERMINATING: _ClassVar[BotStatus]
    INITIALIZING: _ClassVar[BotStatus]

class LeaseState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LEASE_STATE_UNSPECIFIED: _ClassVar[LeaseState]
    PENDING: _ClassVar[LeaseState]
    ACTIVE: _ClassVar[LeaseState]
    COMPLETED: _ClassVar[LeaseState]
    CANCELLED: _ClassVar[LeaseState]
BOT_STATUS_UNSPECIFIED: BotStatus
OK: BotStatus
UNHEALTHY: BotStatus
HOST_REBOOTING: BotStatus
BOT_TERMINATING: BotStatus
INITIALIZING: BotStatus
LEASE_STATE_UNSPECIFIED: LeaseState
PENDING: LeaseState
ACTIVE: LeaseState
COMPLETED: LeaseState
CANCELLED: LeaseState

class BotSession(_message.Message):
    __slots__ = ('name', 'bot_id', 'status', 'worker', 'leases', 'expire_time', 'version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BOT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WORKER_FIELD_NUMBER: _ClassVar[int]
    LEASES_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    bot_id: str
    status: BotStatus
    worker: _worker_pb2.Worker
    leases: _containers.RepeatedCompositeFieldContainer[Lease]
    expire_time: _timestamp_pb2.Timestamp
    version: str

    def __init__(self, name: _Optional[str]=..., bot_id: _Optional[str]=..., status: _Optional[_Union[BotStatus, str]]=..., worker: _Optional[_Union[_worker_pb2.Worker, _Mapping]]=..., leases: _Optional[_Iterable[_Union[Lease, _Mapping]]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., version: _Optional[str]=...) -> None:
        ...

class Lease(_message.Message):
    __slots__ = ('id', 'payload', 'result', 'state', 'status', 'requirements', 'expire_time', 'assignment', 'inline_assignment')
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    INLINE_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: _any_pb2.Any
    result: _any_pb2.Any
    state: LeaseState
    status: _status_pb2.Status
    requirements: _worker_pb2.Worker
    expire_time: _timestamp_pb2.Timestamp
    assignment: str
    inline_assignment: _any_pb2.Any

    def __init__(self, id: _Optional[str]=..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., result: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., state: _Optional[_Union[LeaseState, str]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., requirements: _Optional[_Union[_worker_pb2.Worker, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., assignment: _Optional[str]=..., inline_assignment: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
        ...

class AdminTemp(_message.Message):
    __slots__ = ('command', 'arg')

    class Command(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdminTemp.Command]
        BOT_UPDATE: _ClassVar[AdminTemp.Command]
        BOT_RESTART: _ClassVar[AdminTemp.Command]
        BOT_TERMINATE: _ClassVar[AdminTemp.Command]
        HOST_RESTART: _ClassVar[AdminTemp.Command]
    UNSPECIFIED: AdminTemp.Command
    BOT_UPDATE: AdminTemp.Command
    BOT_RESTART: AdminTemp.Command
    BOT_TERMINATE: AdminTemp.Command
    HOST_RESTART: AdminTemp.Command
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ARG_FIELD_NUMBER: _ClassVar[int]
    command: AdminTemp.Command
    arg: str

    def __init__(self, command: _Optional[_Union[AdminTemp.Command, str]]=..., arg: _Optional[str]=...) -> None:
        ...

class CreateBotSessionRequest(_message.Message):
    __slots__ = ('parent', 'bot_session')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BOT_SESSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    bot_session: BotSession

    def __init__(self, parent: _Optional[str]=..., bot_session: _Optional[_Union[BotSession, _Mapping]]=...) -> None:
        ...

class UpdateBotSessionRequest(_message.Message):
    __slots__ = ('name', 'bot_session', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BOT_SESSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    bot_session: BotSession
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., bot_session: _Optional[_Union[BotSession, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...