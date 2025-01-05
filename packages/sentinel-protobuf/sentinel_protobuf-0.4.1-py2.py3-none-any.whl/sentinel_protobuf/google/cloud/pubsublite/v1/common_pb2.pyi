from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AttributeValues(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, values: _Optional[_Iterable[bytes]]=...) -> None:
        ...

class PubSubMessage(_message.Message):
    __slots__ = ('key', 'data', 'attributes', 'event_time')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValues

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValues, _Mapping]]=...) -> None:
            ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    data: bytes
    attributes: _containers.MessageMap[str, AttributeValues]
    event_time: _timestamp_pb2.Timestamp

    def __init__(self, key: _Optional[bytes]=..., data: _Optional[bytes]=..., attributes: _Optional[_Mapping[str, AttributeValues]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Cursor(_message.Message):
    __slots__ = ('offset',)
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: int

    def __init__(self, offset: _Optional[int]=...) -> None:
        ...

class SequencedMessage(_message.Message):
    __slots__ = ('cursor', 'publish_time', 'message', 'size_bytes')
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    cursor: Cursor
    publish_time: _timestamp_pb2.Timestamp
    message: PubSubMessage
    size_bytes: int

    def __init__(self, cursor: _Optional[_Union[Cursor, _Mapping]]=..., publish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., message: _Optional[_Union[PubSubMessage, _Mapping]]=..., size_bytes: _Optional[int]=...) -> None:
        ...

class Reservation(_message.Message):
    __slots__ = ('name', 'throughput_capacity')
    NAME_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    throughput_capacity: int

    def __init__(self, name: _Optional[str]=..., throughput_capacity: _Optional[int]=...) -> None:
        ...

class Topic(_message.Message):
    __slots__ = ('name', 'partition_config', 'retention_config', 'reservation_config')

    class PartitionConfig(_message.Message):
        __slots__ = ('count', 'scale', 'capacity')

        class Capacity(_message.Message):
            __slots__ = ('publish_mib_per_sec', 'subscribe_mib_per_sec')
            PUBLISH_MIB_PER_SEC_FIELD_NUMBER: _ClassVar[int]
            SUBSCRIBE_MIB_PER_SEC_FIELD_NUMBER: _ClassVar[int]
            publish_mib_per_sec: int
            subscribe_mib_per_sec: int

            def __init__(self, publish_mib_per_sec: _Optional[int]=..., subscribe_mib_per_sec: _Optional[int]=...) -> None:
                ...
        COUNT_FIELD_NUMBER: _ClassVar[int]
        SCALE_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_FIELD_NUMBER: _ClassVar[int]
        count: int
        scale: int
        capacity: Topic.PartitionConfig.Capacity

        def __init__(self, count: _Optional[int]=..., scale: _Optional[int]=..., capacity: _Optional[_Union[Topic.PartitionConfig.Capacity, _Mapping]]=...) -> None:
            ...

    class RetentionConfig(_message.Message):
        __slots__ = ('per_partition_bytes', 'period')
        PER_PARTITION_BYTES_FIELD_NUMBER: _ClassVar[int]
        PERIOD_FIELD_NUMBER: _ClassVar[int]
        per_partition_bytes: int
        period: _duration_pb2.Duration

        def __init__(self, per_partition_bytes: _Optional[int]=..., period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class ReservationConfig(_message.Message):
        __slots__ = ('throughput_reservation',)
        THROUGHPUT_RESERVATION_FIELD_NUMBER: _ClassVar[int]
        throughput_reservation: str

        def __init__(self, throughput_reservation: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RETENTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    partition_config: Topic.PartitionConfig
    retention_config: Topic.RetentionConfig
    reservation_config: Topic.ReservationConfig

    def __init__(self, name: _Optional[str]=..., partition_config: _Optional[_Union[Topic.PartitionConfig, _Mapping]]=..., retention_config: _Optional[_Union[Topic.RetentionConfig, _Mapping]]=..., reservation_config: _Optional[_Union[Topic.ReservationConfig, _Mapping]]=...) -> None:
        ...

class Subscription(_message.Message):
    __slots__ = ('name', 'topic', 'delivery_config', 'export_config')

    class DeliveryConfig(_message.Message):
        __slots__ = ('delivery_requirement',)

        class DeliveryRequirement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DELIVERY_REQUIREMENT_UNSPECIFIED: _ClassVar[Subscription.DeliveryConfig.DeliveryRequirement]
            DELIVER_IMMEDIATELY: _ClassVar[Subscription.DeliveryConfig.DeliveryRequirement]
            DELIVER_AFTER_STORED: _ClassVar[Subscription.DeliveryConfig.DeliveryRequirement]
        DELIVERY_REQUIREMENT_UNSPECIFIED: Subscription.DeliveryConfig.DeliveryRequirement
        DELIVER_IMMEDIATELY: Subscription.DeliveryConfig.DeliveryRequirement
        DELIVER_AFTER_STORED: Subscription.DeliveryConfig.DeliveryRequirement
        DELIVERY_REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
        delivery_requirement: Subscription.DeliveryConfig.DeliveryRequirement

        def __init__(self, delivery_requirement: _Optional[_Union[Subscription.DeliveryConfig.DeliveryRequirement, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    topic: str
    delivery_config: Subscription.DeliveryConfig
    export_config: ExportConfig

    def __init__(self, name: _Optional[str]=..., topic: _Optional[str]=..., delivery_config: _Optional[_Union[Subscription.DeliveryConfig, _Mapping]]=..., export_config: _Optional[_Union[ExportConfig, _Mapping]]=...) -> None:
        ...

class ExportConfig(_message.Message):
    __slots__ = ('desired_state', 'current_state', 'dead_letter_topic', 'pubsub_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ExportConfig.State]
        ACTIVE: _ClassVar[ExportConfig.State]
        PAUSED: _ClassVar[ExportConfig.State]
        PERMISSION_DENIED: _ClassVar[ExportConfig.State]
        NOT_FOUND: _ClassVar[ExportConfig.State]
    STATE_UNSPECIFIED: ExportConfig.State
    ACTIVE: ExportConfig.State
    PAUSED: ExportConfig.State
    PERMISSION_DENIED: ExportConfig.State
    NOT_FOUND: ExportConfig.State

    class PubSubConfig(_message.Message):
        __slots__ = ('topic',)
        TOPIC_FIELD_NUMBER: _ClassVar[int]
        topic: str

        def __init__(self, topic: _Optional[str]=...) -> None:
            ...
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_TOPIC_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    desired_state: ExportConfig.State
    current_state: ExportConfig.State
    dead_letter_topic: str
    pubsub_config: ExportConfig.PubSubConfig

    def __init__(self, desired_state: _Optional[_Union[ExportConfig.State, str]]=..., current_state: _Optional[_Union[ExportConfig.State, str]]=..., dead_letter_topic: _Optional[str]=..., pubsub_config: _Optional[_Union[ExportConfig.PubSubConfig, _Mapping]]=...) -> None:
        ...

class TimeTarget(_message.Message):
    __slots__ = ('publish_time', 'event_time')
    PUBLISH_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    publish_time: _timestamp_pb2.Timestamp
    event_time: _timestamp_pb2.Timestamp

    def __init__(self, publish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...