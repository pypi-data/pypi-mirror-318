from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Channel(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'provider', 'pubsub_topic', 'state', 'activation_token', 'crypto_key_name', 'satisfies_pzs')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Channel.State]
        PENDING: _ClassVar[Channel.State]
        ACTIVE: _ClassVar[Channel.State]
        INACTIVE: _ClassVar[Channel.State]
    STATE_UNSPECIFIED: Channel.State
    PENDING: Channel.State
    ACTIVE: Channel.State
    INACTIVE: Channel.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    provider: str
    pubsub_topic: str
    state: Channel.State
    activation_token: str
    crypto_key_name: str
    satisfies_pzs: bool

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., provider: _Optional[str]=..., pubsub_topic: _Optional[str]=..., state: _Optional[_Union[Channel.State, str]]=..., activation_token: _Optional[str]=..., crypto_key_name: _Optional[str]=..., satisfies_pzs: bool=...) -> None:
        ...