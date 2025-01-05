from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TransactionOptions(_message.Message):
    __slots__ = ('read_write', 'partitioned_dml', 'read_only', 'exclude_txn_from_change_streams')

    class ReadWrite(_message.Message):
        __slots__ = ('read_lock_mode', 'multiplexed_session_previous_transaction_id')

        class ReadLockMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            READ_LOCK_MODE_UNSPECIFIED: _ClassVar[TransactionOptions.ReadWrite.ReadLockMode]
            PESSIMISTIC: _ClassVar[TransactionOptions.ReadWrite.ReadLockMode]
            OPTIMISTIC: _ClassVar[TransactionOptions.ReadWrite.ReadLockMode]
        READ_LOCK_MODE_UNSPECIFIED: TransactionOptions.ReadWrite.ReadLockMode
        PESSIMISTIC: TransactionOptions.ReadWrite.ReadLockMode
        OPTIMISTIC: TransactionOptions.ReadWrite.ReadLockMode
        READ_LOCK_MODE_FIELD_NUMBER: _ClassVar[int]
        MULTIPLEXED_SESSION_PREVIOUS_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        read_lock_mode: TransactionOptions.ReadWrite.ReadLockMode
        multiplexed_session_previous_transaction_id: bytes

        def __init__(self, read_lock_mode: _Optional[_Union[TransactionOptions.ReadWrite.ReadLockMode, str]]=..., multiplexed_session_previous_transaction_id: _Optional[bytes]=...) -> None:
            ...

    class PartitionedDml(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class ReadOnly(_message.Message):
        __slots__ = ('strong', 'min_read_timestamp', 'max_staleness', 'read_timestamp', 'exact_staleness', 'return_read_timestamp')
        STRONG_FIELD_NUMBER: _ClassVar[int]
        MIN_READ_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        MAX_STALENESS_FIELD_NUMBER: _ClassVar[int]
        READ_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        EXACT_STALENESS_FIELD_NUMBER: _ClassVar[int]
        RETURN_READ_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        strong: bool
        min_read_timestamp: _timestamp_pb2.Timestamp
        max_staleness: _duration_pb2.Duration
        read_timestamp: _timestamp_pb2.Timestamp
        exact_staleness: _duration_pb2.Duration
        return_read_timestamp: bool

        def __init__(self, strong: bool=..., min_read_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., max_staleness: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., read_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., exact_staleness: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., return_read_timestamp: bool=...) -> None:
            ...
    READ_WRITE_FIELD_NUMBER: _ClassVar[int]
    PARTITIONED_DML_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_TXN_FROM_CHANGE_STREAMS_FIELD_NUMBER: _ClassVar[int]
    read_write: TransactionOptions.ReadWrite
    partitioned_dml: TransactionOptions.PartitionedDml
    read_only: TransactionOptions.ReadOnly
    exclude_txn_from_change_streams: bool

    def __init__(self, read_write: _Optional[_Union[TransactionOptions.ReadWrite, _Mapping]]=..., partitioned_dml: _Optional[_Union[TransactionOptions.PartitionedDml, _Mapping]]=..., read_only: _Optional[_Union[TransactionOptions.ReadOnly, _Mapping]]=..., exclude_txn_from_change_streams: bool=...) -> None:
        ...

class Transaction(_message.Message):
    __slots__ = ('id', 'read_timestamp', 'precommit_token')
    ID_FIELD_NUMBER: _ClassVar[int]
    READ_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PRECOMMIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    read_timestamp: _timestamp_pb2.Timestamp
    precommit_token: MultiplexedSessionPrecommitToken

    def __init__(self, id: _Optional[bytes]=..., read_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., precommit_token: _Optional[_Union[MultiplexedSessionPrecommitToken, _Mapping]]=...) -> None:
        ...

class TransactionSelector(_message.Message):
    __slots__ = ('single_use', 'id', 'begin')
    SINGLE_USE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    single_use: TransactionOptions
    id: bytes
    begin: TransactionOptions

    def __init__(self, single_use: _Optional[_Union[TransactionOptions, _Mapping]]=..., id: _Optional[bytes]=..., begin: _Optional[_Union[TransactionOptions, _Mapping]]=...) -> None:
        ...

class MultiplexedSessionPrecommitToken(_message.Message):
    __slots__ = ('precommit_token', 'seq_num')
    PRECOMMIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    precommit_token: bytes
    seq_num: int

    def __init__(self, precommit_token: _Optional[bytes]=..., seq_num: _Optional[int]=...) -> None:
        ...