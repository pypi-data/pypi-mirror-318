
from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.lease.v1 import params_pb2 as _params_pb2
from sentinel.types.v1 import renewal_pb2 as _renewal_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgEndLeaseRequest(_message.Message):
    __slots__ = ['id']
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=..., **kwargs) -> None:
        ...

class MsgEndLeaseResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgRenewLeaseRequest(_message.Message):
    __slots__ = ['denom', 'hours', 'id']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    denom: str
    hours: int
    id: int

    def __init__(self, id: _Optional[int]=..., hours: _Optional[int]=..., denom: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgRenewLeaseResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgStartLeaseRequest(_message.Message):
    __slots__ = ['denom', 'hours', 'node_address', 'renewal_price_policy']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    denom: str
    hours: int
    node_address: str
    renewal_price_policy: _renewal_pb2.RenewalPricePolicy

    def __init__(self, node_address: _Optional[str]=..., hours: _Optional[int]=..., denom: _Optional[str]=..., renewal_price_policy: _Optional[_Union[(_renewal_pb2.RenewalPricePolicy, str)]]=..., **kwargs) -> None:
        ...

class MsgStartLeaseResponse(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=...) -> None:
        ...

class MsgUpdateLeaseRequest(_message.Message):
    __slots__ = ['id', 'renewal_price_policy']
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    id: int
    renewal_price_policy: _renewal_pb2.RenewalPricePolicy

    def __init__(self, id: _Optional[int]=..., renewal_price_policy: _Optional[_Union[(_renewal_pb2.RenewalPricePolicy, str)]]=..., **kwargs) -> None:
        ...

class MsgUpdateLeaseResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgUpdateParamsRequest(_message.Message):
    __slots__ = ['params']
    FROM_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.Params

    def __init__(self, params: _Optional[_Union[(_params_pb2.Params, _Mapping)]]=..., **kwargs) -> None:
        ...

class MsgUpdateParamsResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...
