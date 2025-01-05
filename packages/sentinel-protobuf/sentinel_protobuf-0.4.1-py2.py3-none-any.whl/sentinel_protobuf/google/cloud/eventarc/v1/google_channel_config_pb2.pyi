from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GoogleChannelConfig(_message.Message):
    __slots__ = ('name', 'update_time', 'crypto_key_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    update_time: _timestamp_pb2.Timestamp
    crypto_key_name: str

    def __init__(self, name: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., crypto_key_name: _Optional[str]=...) -> None:
        ...