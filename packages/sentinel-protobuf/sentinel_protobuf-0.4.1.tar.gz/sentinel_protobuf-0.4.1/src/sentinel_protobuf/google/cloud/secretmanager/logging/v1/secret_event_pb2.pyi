from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SecretEvent(_message.Message):
    __slots__ = ('name', 'type', 'log_message')

    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[SecretEvent.EventType]
        EXPIRES_IN_30_DAYS: _ClassVar[SecretEvent.EventType]
        EXPIRES_IN_7_DAYS: _ClassVar[SecretEvent.EventType]
        EXPIRES_IN_1_DAY: _ClassVar[SecretEvent.EventType]
        EXPIRES_IN_6_HOURS: _ClassVar[SecretEvent.EventType]
        EXPIRES_IN_1_HOUR: _ClassVar[SecretEvent.EventType]
        EXPIRED: _ClassVar[SecretEvent.EventType]
        TOPIC_NOT_FOUND: _ClassVar[SecretEvent.EventType]
        TOPIC_PERMISSION_DENIED: _ClassVar[SecretEvent.EventType]
    EVENT_TYPE_UNSPECIFIED: SecretEvent.EventType
    EXPIRES_IN_30_DAYS: SecretEvent.EventType
    EXPIRES_IN_7_DAYS: SecretEvent.EventType
    EXPIRES_IN_1_DAY: SecretEvent.EventType
    EXPIRES_IN_6_HOURS: SecretEvent.EventType
    EXPIRES_IN_1_HOUR: SecretEvent.EventType
    EXPIRED: SecretEvent.EventType
    TOPIC_NOT_FOUND: SecretEvent.EventType
    TOPIC_PERMISSION_DENIED: SecretEvent.EventType
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOG_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: SecretEvent.EventType
    log_message: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[SecretEvent.EventType, str]]=..., log_message: _Optional[str]=...) -> None:
        ...