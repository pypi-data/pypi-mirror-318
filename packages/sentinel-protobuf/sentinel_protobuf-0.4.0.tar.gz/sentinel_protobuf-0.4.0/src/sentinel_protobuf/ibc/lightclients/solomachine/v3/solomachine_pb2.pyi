
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ClientState(_message.Message):
    __slots__ = ['consensus_state', 'is_frozen', 'sequence']
    CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_FROZEN_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    consensus_state: ConsensusState
    is_frozen: bool
    sequence: int

    def __init__(self, sequence: _Optional[int]=..., is_frozen: bool=..., consensus_state: _Optional[_Union[(ConsensusState, _Mapping)]]=...) -> None:
        ...

class ConsensusState(_message.Message):
    __slots__ = ['diversifier', 'public_key', 'timestamp']
    DIVERSIFIER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    diversifier: str
    public_key: _any_pb2.Any
    timestamp: int

    def __init__(self, public_key: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=..., diversifier: _Optional[str]=..., timestamp: _Optional[int]=...) -> None:
        ...

class Header(_message.Message):
    __slots__ = ['new_diversifier', 'new_public_key', 'signature', 'timestamp']
    NEW_DIVERSIFIER_FIELD_NUMBER: _ClassVar[int]
    NEW_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    new_diversifier: str
    new_public_key: _any_pb2.Any
    signature: bytes
    timestamp: int

    def __init__(self, timestamp: _Optional[int]=..., signature: _Optional[bytes]=..., new_public_key: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=..., new_diversifier: _Optional[str]=...) -> None:
        ...

class HeaderData(_message.Message):
    __slots__ = ['new_diversifier', 'new_pub_key']
    NEW_DIVERSIFIER_FIELD_NUMBER: _ClassVar[int]
    NEW_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    new_diversifier: str
    new_pub_key: _any_pb2.Any

    def __init__(self, new_pub_key: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=..., new_diversifier: _Optional[str]=...) -> None:
        ...

class Misbehaviour(_message.Message):
    __slots__ = ['sequence', 'signature_one', 'signature_two']
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_ONE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_TWO_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    signature_one: SignatureAndData
    signature_two: SignatureAndData

    def __init__(self, sequence: _Optional[int]=..., signature_one: _Optional[_Union[(SignatureAndData, _Mapping)]]=..., signature_two: _Optional[_Union[(SignatureAndData, _Mapping)]]=...) -> None:
        ...

class SignBytes(_message.Message):
    __slots__ = ['data', 'diversifier', 'path', 'sequence', 'timestamp']
    DATA_FIELD_NUMBER: _ClassVar[int]
    DIVERSIFIER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    diversifier: str
    path: bytes
    sequence: int
    timestamp: int

    def __init__(self, sequence: _Optional[int]=..., timestamp: _Optional[int]=..., diversifier: _Optional[str]=..., path: _Optional[bytes]=..., data: _Optional[bytes]=...) -> None:
        ...

class SignatureAndData(_message.Message):
    __slots__ = ['data', 'path', 'signature', 'timestamp']
    DATA_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    path: bytes
    signature: bytes
    timestamp: int

    def __init__(self, signature: _Optional[bytes]=..., path: _Optional[bytes]=..., data: _Optional[bytes]=..., timestamp: _Optional[int]=...) -> None:
        ...

class TimestampedSignatureData(_message.Message):
    __slots__ = ['signature_data', 'timestamp']
    SIGNATURE_DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    signature_data: bytes
    timestamp: int

    def __init__(self, signature_data: _Optional[bytes]=..., timestamp: _Optional[int]=...) -> None:
        ...
