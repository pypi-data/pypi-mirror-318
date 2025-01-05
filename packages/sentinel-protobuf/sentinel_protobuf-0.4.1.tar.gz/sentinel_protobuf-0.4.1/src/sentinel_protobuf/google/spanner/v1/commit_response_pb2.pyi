from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.spanner.v1 import transaction_pb2 as _transaction_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CommitResponse(_message.Message):
    __slots__ = ('commit_timestamp', 'commit_stats', 'precommit_token')

    class CommitStats(_message.Message):
        __slots__ = ('mutation_count',)
        MUTATION_COUNT_FIELD_NUMBER: _ClassVar[int]
        mutation_count: int

        def __init__(self, mutation_count: _Optional[int]=...) -> None:
            ...
    COMMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COMMIT_STATS_FIELD_NUMBER: _ClassVar[int]
    PRECOMMIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    commit_timestamp: _timestamp_pb2.Timestamp
    commit_stats: CommitResponse.CommitStats
    precommit_token: _transaction_pb2.MultiplexedSessionPrecommitToken

    def __init__(self, commit_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., commit_stats: _Optional[_Union[CommitResponse.CommitStats, _Mapping]]=..., precommit_token: _Optional[_Union[_transaction_pb2.MultiplexedSessionPrecommitToken, _Mapping]]=...) -> None:
        ...