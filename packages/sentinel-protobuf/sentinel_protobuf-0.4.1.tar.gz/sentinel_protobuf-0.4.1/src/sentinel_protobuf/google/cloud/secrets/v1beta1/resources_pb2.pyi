from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Secret(_message.Message):
    __slots__ = ('name', 'replication', 'create_time', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    replication: Replication
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., replication: _Optional[_Union[Replication, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class SecretVersion(_message.Message):
    __slots__ = ('name', 'create_time', 'destroy_time', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[SecretVersion.State]
        ENABLED: _ClassVar[SecretVersion.State]
        DISABLED: _ClassVar[SecretVersion.State]
        DESTROYED: _ClassVar[SecretVersion.State]
    STATE_UNSPECIFIED: SecretVersion.State
    ENABLED: SecretVersion.State
    DISABLED: SecretVersion.State
    DESTROYED: SecretVersion.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESTROY_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    destroy_time: _timestamp_pb2.Timestamp
    state: SecretVersion.State

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., destroy_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[SecretVersion.State, str]]=...) -> None:
        ...

class Replication(_message.Message):
    __slots__ = ('automatic', 'user_managed')

    class Automatic(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class UserManaged(_message.Message):
        __slots__ = ('replicas',)

        class Replica(_message.Message):
            __slots__ = ('location',)
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            location: str

            def __init__(self, location: _Optional[str]=...) -> None:
                ...
        REPLICAS_FIELD_NUMBER: _ClassVar[int]
        replicas: _containers.RepeatedCompositeFieldContainer[Replication.UserManaged.Replica]

        def __init__(self, replicas: _Optional[_Iterable[_Union[Replication.UserManaged.Replica, _Mapping]]]=...) -> None:
            ...
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    USER_MANAGED_FIELD_NUMBER: _ClassVar[int]
    automatic: Replication.Automatic
    user_managed: Replication.UserManaged

    def __init__(self, automatic: _Optional[_Union[Replication.Automatic, _Mapping]]=..., user_managed: _Optional[_Union[Replication.UserManaged, _Mapping]]=...) -> None:
        ...

class SecretPayload(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes

    def __init__(self, data: _Optional[bytes]=...) -> None:
        ...