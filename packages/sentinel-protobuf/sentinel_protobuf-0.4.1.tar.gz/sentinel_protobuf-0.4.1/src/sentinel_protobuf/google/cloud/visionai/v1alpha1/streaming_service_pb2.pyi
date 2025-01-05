from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.cloud.visionai.v1alpha1 import streaming_resources_pb2 as _streaming_resources_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LeaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LEASE_TYPE_UNSPECIFIED: _ClassVar[LeaseType]
    LEASE_TYPE_READER: _ClassVar[LeaseType]
    LEASE_TYPE_WRITER: _ClassVar[LeaseType]
LEASE_TYPE_UNSPECIFIED: LeaseType
LEASE_TYPE_READER: LeaseType
LEASE_TYPE_WRITER: LeaseType

class ReceiveEventsRequest(_message.Message):
    __slots__ = ('setup_request', 'commit_request')

    class SetupRequest(_message.Message):
        __slots__ = ('cluster', 'stream', 'receiver', 'controlled_mode', 'heartbeat_interval', 'writes_done_grace_period')
        CLUSTER_FIELD_NUMBER: _ClassVar[int]
        STREAM_FIELD_NUMBER: _ClassVar[int]
        RECEIVER_FIELD_NUMBER: _ClassVar[int]
        CONTROLLED_MODE_FIELD_NUMBER: _ClassVar[int]
        HEARTBEAT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        WRITES_DONE_GRACE_PERIOD_FIELD_NUMBER: _ClassVar[int]
        cluster: str
        stream: str
        receiver: str
        controlled_mode: ControlledMode
        heartbeat_interval: _duration_pb2.Duration
        writes_done_grace_period: _duration_pb2.Duration

        def __init__(self, cluster: _Optional[str]=..., stream: _Optional[str]=..., receiver: _Optional[str]=..., controlled_mode: _Optional[_Union[ControlledMode, _Mapping]]=..., heartbeat_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., writes_done_grace_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    SETUP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    COMMIT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    setup_request: ReceiveEventsRequest.SetupRequest
    commit_request: CommitRequest

    def __init__(self, setup_request: _Optional[_Union[ReceiveEventsRequest.SetupRequest, _Mapping]]=..., commit_request: _Optional[_Union[CommitRequest, _Mapping]]=...) -> None:
        ...

class EventUpdate(_message.Message):
    __slots__ = ('stream', 'event', 'series', 'update_time', 'offset')
    STREAM_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    stream: str
    event: str
    series: str
    update_time: _timestamp_pb2.Timestamp
    offset: int

    def __init__(self, stream: _Optional[str]=..., event: _Optional[str]=..., series: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., offset: _Optional[int]=...) -> None:
        ...

class ReceiveEventsControlResponse(_message.Message):
    __slots__ = ('heartbeat', 'writes_done_request')
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    WRITES_DONE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    heartbeat: bool
    writes_done_request: bool

    def __init__(self, heartbeat: bool=..., writes_done_request: bool=...) -> None:
        ...

class ReceiveEventsResponse(_message.Message):
    __slots__ = ('event_update', 'control')
    EVENT_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    event_update: EventUpdate
    control: ReceiveEventsControlResponse

    def __init__(self, event_update: _Optional[_Union[EventUpdate, _Mapping]]=..., control: _Optional[_Union[ReceiveEventsControlResponse, _Mapping]]=...) -> None:
        ...

class Lease(_message.Message):
    __slots__ = ('id', 'series', 'owner', 'expire_time', 'lease_type')
    ID_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    LEASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    series: str
    owner: str
    expire_time: _timestamp_pb2.Timestamp
    lease_type: LeaseType

    def __init__(self, id: _Optional[str]=..., series: _Optional[str]=..., owner: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., lease_type: _Optional[_Union[LeaseType, str]]=...) -> None:
        ...

class AcquireLeaseRequest(_message.Message):
    __slots__ = ('series', 'owner', 'term', 'lease_type')
    SERIES_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    LEASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    series: str
    owner: str
    term: _duration_pb2.Duration
    lease_type: LeaseType

    def __init__(self, series: _Optional[str]=..., owner: _Optional[str]=..., term: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., lease_type: _Optional[_Union[LeaseType, str]]=...) -> None:
        ...

class RenewLeaseRequest(_message.Message):
    __slots__ = ('id', 'series', 'owner', 'term')
    ID_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    id: str
    series: str
    owner: str
    term: _duration_pb2.Duration

    def __init__(self, id: _Optional[str]=..., series: _Optional[str]=..., owner: _Optional[str]=..., term: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class ReleaseLeaseRequest(_message.Message):
    __slots__ = ('id', 'series', 'owner')
    ID_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    id: str
    series: str
    owner: str

    def __init__(self, id: _Optional[str]=..., series: _Optional[str]=..., owner: _Optional[str]=...) -> None:
        ...

class ReleaseLeaseResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RequestMetadata(_message.Message):
    __slots__ = ('stream', 'event', 'series', 'lease_id', 'owner', 'lease_term')
    STREAM_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    LEASE_TERM_FIELD_NUMBER: _ClassVar[int]
    stream: str
    event: str
    series: str
    lease_id: str
    owner: str
    lease_term: _duration_pb2.Duration

    def __init__(self, stream: _Optional[str]=..., event: _Optional[str]=..., series: _Optional[str]=..., lease_id: _Optional[str]=..., owner: _Optional[str]=..., lease_term: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class SendPacketsRequest(_message.Message):
    __slots__ = ('packet', 'metadata')
    PACKET_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    packet: _streaming_resources_pb2.Packet
    metadata: RequestMetadata

    def __init__(self, packet: _Optional[_Union[_streaming_resources_pb2.Packet, _Mapping]]=..., metadata: _Optional[_Union[RequestMetadata, _Mapping]]=...) -> None:
        ...

class SendPacketsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReceivePacketsRequest(_message.Message):
    __slots__ = ('setup_request', 'commit_request')

    class SetupRequest(_message.Message):
        __slots__ = ('eager_receive_mode', 'controlled_receive_mode', 'metadata', 'receiver', 'heartbeat_interval', 'writes_done_grace_period')
        EAGER_RECEIVE_MODE_FIELD_NUMBER: _ClassVar[int]
        CONTROLLED_RECEIVE_MODE_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        RECEIVER_FIELD_NUMBER: _ClassVar[int]
        HEARTBEAT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        WRITES_DONE_GRACE_PERIOD_FIELD_NUMBER: _ClassVar[int]
        eager_receive_mode: EagerMode
        controlled_receive_mode: ControlledMode
        metadata: RequestMetadata
        receiver: str
        heartbeat_interval: _duration_pb2.Duration
        writes_done_grace_period: _duration_pb2.Duration

        def __init__(self, eager_receive_mode: _Optional[_Union[EagerMode, _Mapping]]=..., controlled_receive_mode: _Optional[_Union[ControlledMode, _Mapping]]=..., metadata: _Optional[_Union[RequestMetadata, _Mapping]]=..., receiver: _Optional[str]=..., heartbeat_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., writes_done_grace_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    SETUP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    COMMIT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    setup_request: ReceivePacketsRequest.SetupRequest
    commit_request: CommitRequest

    def __init__(self, setup_request: _Optional[_Union[ReceivePacketsRequest.SetupRequest, _Mapping]]=..., commit_request: _Optional[_Union[CommitRequest, _Mapping]]=...) -> None:
        ...

class ReceivePacketsControlResponse(_message.Message):
    __slots__ = ('heartbeat', 'writes_done_request')
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    WRITES_DONE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    heartbeat: bool
    writes_done_request: bool

    def __init__(self, heartbeat: bool=..., writes_done_request: bool=...) -> None:
        ...

class ReceivePacketsResponse(_message.Message):
    __slots__ = ('packet', 'control')
    PACKET_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    packet: _streaming_resources_pb2.Packet
    control: ReceivePacketsControlResponse

    def __init__(self, packet: _Optional[_Union[_streaming_resources_pb2.Packet, _Mapping]]=..., control: _Optional[_Union[ReceivePacketsControlResponse, _Mapping]]=...) -> None:
        ...

class EagerMode(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ControlledMode(_message.Message):
    __slots__ = ('starting_logical_offset', 'fallback_starting_offset')
    STARTING_LOGICAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_STARTING_OFFSET_FIELD_NUMBER: _ClassVar[int]
    starting_logical_offset: str
    fallback_starting_offset: str

    def __init__(self, starting_logical_offset: _Optional[str]=..., fallback_starting_offset: _Optional[str]=...) -> None:
        ...

class CommitRequest(_message.Message):
    __slots__ = ('offset',)
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: int

    def __init__(self, offset: _Optional[int]=...) -> None:
        ...