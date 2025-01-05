from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import notification_pb2 as _notification_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListNotificationChannelDescriptorsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListNotificationChannelDescriptorsResponse(_message.Message):
    __slots__ = ('channel_descriptors', 'next_page_token')
    CHANNEL_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    channel_descriptors: _containers.RepeatedCompositeFieldContainer[_notification_pb2.NotificationChannelDescriptor]
    next_page_token: str

    def __init__(self, channel_descriptors: _Optional[_Iterable[_Union[_notification_pb2.NotificationChannelDescriptor, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetNotificationChannelDescriptorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateNotificationChannelRequest(_message.Message):
    __slots__ = ('name', 'notification_channel')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    notification_channel: _notification_pb2.NotificationChannel

    def __init__(self, name: _Optional[str]=..., notification_channel: _Optional[_Union[_notification_pb2.NotificationChannel, _Mapping]]=...) -> None:
        ...

class ListNotificationChannelsRequest(_message.Message):
    __slots__ = ('name', 'filter', 'order_by', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str
    order_by: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListNotificationChannelsResponse(_message.Message):
    __slots__ = ('notification_channels', 'next_page_token', 'total_size')
    NOTIFICATION_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    notification_channels: _containers.RepeatedCompositeFieldContainer[_notification_pb2.NotificationChannel]
    next_page_token: str
    total_size: int

    def __init__(self, notification_channels: _Optional[_Iterable[_Union[_notification_pb2.NotificationChannel, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class GetNotificationChannelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateNotificationChannelRequest(_message.Message):
    __slots__ = ('update_mask', 'notification_channel')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    notification_channel: _notification_pb2.NotificationChannel

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., notification_channel: _Optional[_Union[_notification_pb2.NotificationChannel, _Mapping]]=...) -> None:
        ...

class DeleteNotificationChannelRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class SendNotificationChannelVerificationCodeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetNotificationChannelVerificationCodeRequest(_message.Message):
    __slots__ = ('name', 'expire_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetNotificationChannelVerificationCodeResponse(_message.Message):
    __slots__ = ('code', 'expire_time')
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    code: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, code: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class VerifyNotificationChannelRequest(_message.Message):
    __slots__ = ('name', 'code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str

    def __init__(self, name: _Optional[str]=..., code: _Optional[str]=...) -> None:
        ...