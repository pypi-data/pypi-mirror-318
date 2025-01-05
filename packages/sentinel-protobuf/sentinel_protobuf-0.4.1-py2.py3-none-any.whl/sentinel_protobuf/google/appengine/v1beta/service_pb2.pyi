from google.appengine.v1beta import network_settings_pb2 as _network_settings_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Service(_message.Message):
    __slots__ = ('name', 'id', 'split', 'network_settings')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    split: TrafficSplit
    network_settings: _network_settings_pb2.NetworkSettings

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., split: _Optional[_Union[TrafficSplit, _Mapping]]=..., network_settings: _Optional[_Union[_network_settings_pb2.NetworkSettings, _Mapping]]=...) -> None:
        ...

class TrafficSplit(_message.Message):
    __slots__ = ('shard_by', 'allocations')

    class ShardBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TrafficSplit.ShardBy]
        COOKIE: _ClassVar[TrafficSplit.ShardBy]
        IP: _ClassVar[TrafficSplit.ShardBy]
        RANDOM: _ClassVar[TrafficSplit.ShardBy]
    UNSPECIFIED: TrafficSplit.ShardBy
    COOKIE: TrafficSplit.ShardBy
    IP: TrafficSplit.ShardBy
    RANDOM: TrafficSplit.ShardBy

    class AllocationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float

        def __init__(self, key: _Optional[str]=..., value: _Optional[float]=...) -> None:
            ...
    SHARD_BY_FIELD_NUMBER: _ClassVar[int]
    ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    shard_by: TrafficSplit.ShardBy
    allocations: _containers.ScalarMap[str, float]

    def __init__(self, shard_by: _Optional[_Union[TrafficSplit.ShardBy, str]]=..., allocations: _Optional[_Mapping[str, float]]=...) -> None:
        ...