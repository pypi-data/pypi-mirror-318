from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.chat.v1 import membership_pb2 as _membership_pb2
from google.chat.v1 import message_pb2 as _message_pb2
from google.chat.v1 import reaction_pb2 as _reaction_pb2
from google.chat.v1 import space_pb2 as _space_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MembershipCreatedEventData(_message.Message):
    __slots__ = ("membership",)
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    membership: _membership_pb2.Membership
    def __init__(self, membership: _Optional[_Union[_membership_pb2.Membership, _Mapping]] = ...) -> None: ...

class MembershipDeletedEventData(_message.Message):
    __slots__ = ("membership",)
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    membership: _membership_pb2.Membership
    def __init__(self, membership: _Optional[_Union[_membership_pb2.Membership, _Mapping]] = ...) -> None: ...

class MembershipUpdatedEventData(_message.Message):
    __slots__ = ("membership",)
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    membership: _membership_pb2.Membership
    def __init__(self, membership: _Optional[_Union[_membership_pb2.Membership, _Mapping]] = ...) -> None: ...

class MembershipBatchCreatedEventData(_message.Message):
    __slots__ = ("memberships",)
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    memberships: _containers.RepeatedCompositeFieldContainer[MembershipCreatedEventData]
    def __init__(self, memberships: _Optional[_Iterable[_Union[MembershipCreatedEventData, _Mapping]]] = ...) -> None: ...

class MembershipBatchUpdatedEventData(_message.Message):
    __slots__ = ("memberships",)
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    memberships: _containers.RepeatedCompositeFieldContainer[MembershipUpdatedEventData]
    def __init__(self, memberships: _Optional[_Iterable[_Union[MembershipUpdatedEventData, _Mapping]]] = ...) -> None: ...

class MembershipBatchDeletedEventData(_message.Message):
    __slots__ = ("memberships",)
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    memberships: _containers.RepeatedCompositeFieldContainer[MembershipDeletedEventData]
    def __init__(self, memberships: _Optional[_Iterable[_Union[MembershipDeletedEventData, _Mapping]]] = ...) -> None: ...

class MessageCreatedEventData(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class MessageUpdatedEventData(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class MessageDeletedEventData(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class MessageBatchCreatedEventData(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[MessageCreatedEventData]
    def __init__(self, messages: _Optional[_Iterable[_Union[MessageCreatedEventData, _Mapping]]] = ...) -> None: ...

class MessageBatchUpdatedEventData(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[MessageUpdatedEventData]
    def __init__(self, messages: _Optional[_Iterable[_Union[MessageUpdatedEventData, _Mapping]]] = ...) -> None: ...

class MessageBatchDeletedEventData(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[MessageDeletedEventData]
    def __init__(self, messages: _Optional[_Iterable[_Union[MessageDeletedEventData, _Mapping]]] = ...) -> None: ...

class SpaceUpdatedEventData(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...

class SpaceBatchUpdatedEventData(_message.Message):
    __slots__ = ("spaces",)
    SPACES_FIELD_NUMBER: _ClassVar[int]
    spaces: _containers.RepeatedCompositeFieldContainer[SpaceUpdatedEventData]
    def __init__(self, spaces: _Optional[_Iterable[_Union[SpaceUpdatedEventData, _Mapping]]] = ...) -> None: ...

class ReactionCreatedEventData(_message.Message):
    __slots__ = ("reaction",)
    REACTION_FIELD_NUMBER: _ClassVar[int]
    reaction: _reaction_pb2.Reaction
    def __init__(self, reaction: _Optional[_Union[_reaction_pb2.Reaction, _Mapping]] = ...) -> None: ...

class ReactionDeletedEventData(_message.Message):
    __slots__ = ("reaction",)
    REACTION_FIELD_NUMBER: _ClassVar[int]
    reaction: _reaction_pb2.Reaction
    def __init__(self, reaction: _Optional[_Union[_reaction_pb2.Reaction, _Mapping]] = ...) -> None: ...

class ReactionBatchCreatedEventData(_message.Message):
    __slots__ = ("reactions",)
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    reactions: _containers.RepeatedCompositeFieldContainer[ReactionCreatedEventData]
    def __init__(self, reactions: _Optional[_Iterable[_Union[ReactionCreatedEventData, _Mapping]]] = ...) -> None: ...

class ReactionBatchDeletedEventData(_message.Message):
    __slots__ = ("reactions",)
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    reactions: _containers.RepeatedCompositeFieldContainer[ReactionDeletedEventData]
    def __init__(self, reactions: _Optional[_Iterable[_Union[ReactionDeletedEventData, _Mapping]]] = ...) -> None: ...
