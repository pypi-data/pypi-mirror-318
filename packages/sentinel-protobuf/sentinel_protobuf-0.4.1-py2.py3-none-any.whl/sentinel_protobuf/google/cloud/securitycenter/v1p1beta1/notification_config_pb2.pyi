from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NotificationConfig(_message.Message):
    __slots__ = ('name', 'description', 'event_type', 'pubsub_topic', 'service_account', 'streaming_config')

    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[NotificationConfig.EventType]
        FINDING: _ClassVar[NotificationConfig.EventType]
    EVENT_TYPE_UNSPECIFIED: NotificationConfig.EventType
    FINDING: NotificationConfig.EventType

    class StreamingConfig(_message.Message):
        __slots__ = ('filter',)
        FILTER_FIELD_NUMBER: _ClassVar[int]
        filter: str

        def __init__(self, filter: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STREAMING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    event_type: NotificationConfig.EventType
    pubsub_topic: str
    service_account: str
    streaming_config: NotificationConfig.StreamingConfig

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., event_type: _Optional[_Union[NotificationConfig.EventType, str]]=..., pubsub_topic: _Optional[str]=..., service_account: _Optional[str]=..., streaming_config: _Optional[_Union[NotificationConfig.StreamingConfig, _Mapping]]=...) -> None:
        ...