from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.pubsublite.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InitialSubscribeRequest(_message.Message):
    __slots__ = ('subscription', 'partition', 'initial_location')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    partition: int
    initial_location: SeekRequest

    def __init__(self, subscription: _Optional[str]=..., partition: _Optional[int]=..., initial_location: _Optional[_Union[SeekRequest, _Mapping]]=...) -> None:
        ...

class InitialSubscribeResponse(_message.Message):
    __slots__ = ('cursor',)
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    cursor: _common_pb2.Cursor

    def __init__(self, cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=...) -> None:
        ...

class SeekRequest(_message.Message):
    __slots__ = ('named_target', 'cursor')

    class NamedTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NAMED_TARGET_UNSPECIFIED: _ClassVar[SeekRequest.NamedTarget]
        HEAD: _ClassVar[SeekRequest.NamedTarget]
        COMMITTED_CURSOR: _ClassVar[SeekRequest.NamedTarget]
    NAMED_TARGET_UNSPECIFIED: SeekRequest.NamedTarget
    HEAD: SeekRequest.NamedTarget
    COMMITTED_CURSOR: SeekRequest.NamedTarget
    NAMED_TARGET_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    named_target: SeekRequest.NamedTarget
    cursor: _common_pb2.Cursor

    def __init__(self, named_target: _Optional[_Union[SeekRequest.NamedTarget, str]]=..., cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=...) -> None:
        ...

class SeekResponse(_message.Message):
    __slots__ = ('cursor',)
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    cursor: _common_pb2.Cursor

    def __init__(self, cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=...) -> None:
        ...

class FlowControlRequest(_message.Message):
    __slots__ = ('allowed_messages', 'allowed_bytes')
    ALLOWED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_BYTES_FIELD_NUMBER: _ClassVar[int]
    allowed_messages: int
    allowed_bytes: int

    def __init__(self, allowed_messages: _Optional[int]=..., allowed_bytes: _Optional[int]=...) -> None:
        ...

class SubscribeRequest(_message.Message):
    __slots__ = ('initial', 'seek', 'flow_control')
    INITIAL_FIELD_NUMBER: _ClassVar[int]
    SEEK_FIELD_NUMBER: _ClassVar[int]
    FLOW_CONTROL_FIELD_NUMBER: _ClassVar[int]
    initial: InitialSubscribeRequest
    seek: SeekRequest
    flow_control: FlowControlRequest

    def __init__(self, initial: _Optional[_Union[InitialSubscribeRequest, _Mapping]]=..., seek: _Optional[_Union[SeekRequest, _Mapping]]=..., flow_control: _Optional[_Union[FlowControlRequest, _Mapping]]=...) -> None:
        ...

class MessageResponse(_message.Message):
    __slots__ = ('messages',)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_common_pb2.SequencedMessage]

    def __init__(self, messages: _Optional[_Iterable[_Union[_common_pb2.SequencedMessage, _Mapping]]]=...) -> None:
        ...

class SubscribeResponse(_message.Message):
    __slots__ = ('initial', 'seek', 'messages')
    INITIAL_FIELD_NUMBER: _ClassVar[int]
    SEEK_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    initial: InitialSubscribeResponse
    seek: SeekResponse
    messages: MessageResponse

    def __init__(self, initial: _Optional[_Union[InitialSubscribeResponse, _Mapping]]=..., seek: _Optional[_Union[SeekResponse, _Mapping]]=..., messages: _Optional[_Union[MessageResponse, _Mapping]]=...) -> None:
        ...

class InitialPartitionAssignmentRequest(_message.Message):
    __slots__ = ('subscription', 'client_id')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    client_id: bytes

    def __init__(self, subscription: _Optional[str]=..., client_id: _Optional[bytes]=...) -> None:
        ...

class PartitionAssignment(_message.Message):
    __slots__ = ('partitions',)
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, partitions: _Optional[_Iterable[int]]=...) -> None:
        ...

class PartitionAssignmentAck(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PartitionAssignmentRequest(_message.Message):
    __slots__ = ('initial', 'ack')
    INITIAL_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    initial: InitialPartitionAssignmentRequest
    ack: PartitionAssignmentAck

    def __init__(self, initial: _Optional[_Union[InitialPartitionAssignmentRequest, _Mapping]]=..., ack: _Optional[_Union[PartitionAssignmentAck, _Mapping]]=...) -> None:
        ...