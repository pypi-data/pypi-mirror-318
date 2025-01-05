from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NotificationStage(_message.Message):
    __slots__ = ('stage', 'event_time', 'notification_id', 'event', 'message')

    class Stage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STAGE_UNSPECIFIED: _ClassVar[NotificationStage.Stage]
        SENT: _ClassVar[NotificationStage.Stage]
        SEND_FAILURE: _ClassVar[NotificationStage.Stage]
        DROPPED: _ClassVar[NotificationStage.Stage]
    STAGE_UNSPECIFIED: NotificationStage.Stage
    SENT: NotificationStage.Stage
    SEND_FAILURE: NotificationStage.Stage
    DROPPED: NotificationStage.Stage

    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_UNSPECIFIED: _ClassVar[NotificationStage.Event]
        HEALTH_STATUS_CHANGE: _ClassVar[NotificationStage.Event]
    EVENT_UNSPECIFIED: NotificationStage.Event
    HEALTH_STATUS_CHANGE: NotificationStage.Event
    STAGE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    stage: NotificationStage.Stage
    event_time: _timestamp_pb2.Timestamp
    notification_id: str
    event: NotificationStage.Event
    message: str

    def __init__(self, stage: _Optional[_Union[NotificationStage.Stage, str]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., notification_id: _Optional[str]=..., event: _Optional[_Union[NotificationStage.Event, str]]=..., message: _Optional[str]=...) -> None:
        ...