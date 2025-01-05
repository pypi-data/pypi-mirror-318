from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RunAssetDiscoveryResponse(_message.Message):
    __slots__ = ('state', 'duration')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[RunAssetDiscoveryResponse.State]
        COMPLETED: _ClassVar[RunAssetDiscoveryResponse.State]
        SUPERSEDED: _ClassVar[RunAssetDiscoveryResponse.State]
        TERMINATED: _ClassVar[RunAssetDiscoveryResponse.State]
    STATE_UNSPECIFIED: RunAssetDiscoveryResponse.State
    COMPLETED: RunAssetDiscoveryResponse.State
    SUPERSEDED: RunAssetDiscoveryResponse.State
    TERMINATED: RunAssetDiscoveryResponse.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    state: RunAssetDiscoveryResponse.State
    duration: _duration_pb2.Duration

    def __init__(self, state: _Optional[_Union[RunAssetDiscoveryResponse.State, str]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...