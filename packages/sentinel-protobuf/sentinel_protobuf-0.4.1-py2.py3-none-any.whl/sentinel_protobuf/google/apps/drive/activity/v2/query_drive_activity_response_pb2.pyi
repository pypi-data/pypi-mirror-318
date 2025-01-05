from google.apps.drive.activity.v2 import action_pb2 as _action_pb2
from google.apps.drive.activity.v2 import actor_pb2 as _actor_pb2
from google.apps.drive.activity.v2 import common_pb2 as _common_pb2
from google.apps.drive.activity.v2 import target_pb2 as _target_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryDriveActivityResponse(_message.Message):
    __slots__ = ("activities", "next_page_token")
    ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    activities: _containers.RepeatedCompositeFieldContainer[DriveActivity]
    next_page_token: str
    def __init__(self, activities: _Optional[_Iterable[_Union[DriveActivity, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DriveActivity(_message.Message):
    __slots__ = ("primary_action_detail", "actors", "actions", "targets", "timestamp", "time_range")
    PRIMARY_ACTION_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    primary_action_detail: _action_pb2.ActionDetail
    actors: _containers.RepeatedCompositeFieldContainer[_actor_pb2.Actor]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    targets: _containers.RepeatedCompositeFieldContainer[_target_pb2.Target]
    timestamp: _timestamp_pb2.Timestamp
    time_range: _common_pb2.TimeRange
    def __init__(self, primary_action_detail: _Optional[_Union[_action_pb2.ActionDetail, _Mapping]] = ..., actors: _Optional[_Iterable[_Union[_actor_pb2.Actor, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., targets: _Optional[_Iterable[_Union[_target_pb2.Target, _Mapping]]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ...) -> None: ...
