from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.deposit.v1 import genesis_pb2 as _genesis_pb2
from sentinel.lease.v1 import genesis_pb2 as _genesis_pb2_1
from sentinel.node.v3 import genesis_pb2 as _genesis_pb2_1_1
from sentinel.plan.v3 import genesis_pb2 as _genesis_pb2_1_1_1
from sentinel.provider.v2 import genesis_pb2 as _genesis_pb2_1_1_1_1
from sentinel.session.v3 import genesis_pb2 as _genesis_pb2_1_1_1_1_1
from sentinel.subscription.v3 import genesis_pb2 as _genesis_pb2_1_1_1_1_1_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ('deposit', 'lease', 'node', 'plan', 'provider', 'session', 'subscription')
    DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    LEASE_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    deposit: _genesis_pb2.GenesisState
    lease: _genesis_pb2_1.GenesisState
    node: _genesis_pb2_1_1.GenesisState
    plan: _genesis_pb2_1_1_1.GenesisState
    provider: _genesis_pb2_1_1_1_1.GenesisState
    session: _genesis_pb2_1_1_1_1_1.GenesisState
    subscription: _genesis_pb2_1_1_1_1_1_1.GenesisState

    def __init__(self, deposit: _Optional[_Union[_genesis_pb2.GenesisState, _Mapping]]=..., lease: _Optional[_Union[_genesis_pb2_1.GenesisState, _Mapping]]=..., node: _Optional[_Union[_genesis_pb2_1_1.GenesisState, _Mapping]]=..., plan: _Optional[_Union[_genesis_pb2_1_1_1.GenesisState, _Mapping]]=..., provider: _Optional[_Union[_genesis_pb2_1_1_1_1.GenesisState, _Mapping]]=..., session: _Optional[_Union[_genesis_pb2_1_1_1_1_1.GenesisState, _Mapping]]=..., subscription: _Optional[_Union[_genesis_pb2_1_1_1_1_1_1.GenesisState, _Mapping]]=...) -> None:
        ...