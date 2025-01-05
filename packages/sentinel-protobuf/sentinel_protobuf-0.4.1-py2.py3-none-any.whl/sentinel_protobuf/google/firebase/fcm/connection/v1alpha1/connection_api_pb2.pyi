from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpstreamRequest(_message.Message):
    __slots__ = ('ack',)
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: Ack

    def __init__(self, ack: _Optional[_Union[Ack, _Mapping]]=...) -> None:
        ...

class DownstreamResponse(_message.Message):
    __slots__ = ('message',)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: Message

    def __init__(self, message: _Optional[_Union[Message, _Mapping]]=...) -> None:
        ...

class Ack(_message.Message):
    __slots__ = ('message_id',)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str

    def __init__(self, message_id: _Optional[str]=...) -> None:
        ...

class Message(_message.Message):
    __slots__ = ('message_id', 'create_time', 'expire_time', 'data')

    class DataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    create_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    data: _containers.ScalarMap[str, str]

    def __init__(self, message_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data: _Optional[_Mapping[str, str]]=...) -> None:
        ...