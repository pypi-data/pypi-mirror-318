from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Subscription(_message.Message):
    __slots__ = ('expire_time', 'ttl', 'name', 'uid', 'target_resource', 'event_types', 'payload_options', 'notification_endpoint', 'state', 'suspension_reason', 'authority', 'create_time', 'update_time', 'reconciling', 'etag')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Subscription.State]
        ACTIVE: _ClassVar[Subscription.State]
        SUSPENDED: _ClassVar[Subscription.State]
        DELETED: _ClassVar[Subscription.State]
    STATE_UNSPECIFIED: Subscription.State
    ACTIVE: Subscription.State
    SUSPENDED: Subscription.State
    DELETED: Subscription.State

    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_TYPE_UNSPECIFIED: _ClassVar[Subscription.ErrorType]
        USER_SCOPE_REVOKED: _ClassVar[Subscription.ErrorType]
        RESOURCE_DELETED: _ClassVar[Subscription.ErrorType]
        USER_AUTHORIZATION_FAILURE: _ClassVar[Subscription.ErrorType]
        ENDPOINT_PERMISSION_DENIED: _ClassVar[Subscription.ErrorType]
        ENDPOINT_NOT_FOUND: _ClassVar[Subscription.ErrorType]
        ENDPOINT_RESOURCE_EXHAUSTED: _ClassVar[Subscription.ErrorType]
        OTHER: _ClassVar[Subscription.ErrorType]
    ERROR_TYPE_UNSPECIFIED: Subscription.ErrorType
    USER_SCOPE_REVOKED: Subscription.ErrorType
    RESOURCE_DELETED: Subscription.ErrorType
    USER_AUTHORIZATION_FAILURE: Subscription.ErrorType
    ENDPOINT_PERMISSION_DENIED: Subscription.ErrorType
    ENDPOINT_NOT_FOUND: Subscription.ErrorType
    ENDPOINT_RESOURCE_EXHAUSTED: Subscription.ErrorType
    OTHER: Subscription.ErrorType
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_REASON_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    expire_time: _timestamp_pb2.Timestamp
    ttl: _duration_pb2.Duration
    name: str
    uid: str
    target_resource: str
    event_types: _containers.RepeatedScalarFieldContainer[str]
    payload_options: PayloadOptions
    notification_endpoint: NotificationEndpoint
    state: Subscription.State
    suspension_reason: Subscription.ErrorType
    authority: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    reconciling: bool
    etag: str

    def __init__(self, expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., name: _Optional[str]=..., uid: _Optional[str]=..., target_resource: _Optional[str]=..., event_types: _Optional[_Iterable[str]]=..., payload_options: _Optional[_Union[PayloadOptions, _Mapping]]=..., notification_endpoint: _Optional[_Union[NotificationEndpoint, _Mapping]]=..., state: _Optional[_Union[Subscription.State, str]]=..., suspension_reason: _Optional[_Union[Subscription.ErrorType, str]]=..., authority: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., reconciling: bool=..., etag: _Optional[str]=...) -> None:
        ...

class PayloadOptions(_message.Message):
    __slots__ = ('include_resource', 'field_mask')
    INCLUDE_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    include_resource: bool
    field_mask: _field_mask_pb2.FieldMask

    def __init__(self, include_resource: bool=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class NotificationEndpoint(_message.Message):
    __slots__ = ('pubsub_topic',)
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    pubsub_topic: str

    def __init__(self, pubsub_topic: _Optional[str]=...) -> None:
        ...