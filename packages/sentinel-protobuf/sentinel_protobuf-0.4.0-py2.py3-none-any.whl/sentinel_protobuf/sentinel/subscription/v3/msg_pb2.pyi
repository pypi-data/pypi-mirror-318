
from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.subscription.v2 import params_pb2 as _params_pb2
from sentinel.types.v1 import renewal_pb2 as _renewal_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgCancelSubscriptionRequest(_message.Message):
    __slots__ = ['id']
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=..., **kwargs) -> None:
        ...

class MsgCancelSubscriptionResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgRenewSubscriptionRequest(_message.Message):
    __slots__ = ['denom', 'id']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    denom: str
    id: int

    def __init__(self, id: _Optional[int]=..., denom: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgRenewSubscriptionResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgShareSubscriptionRequest(_message.Message):
    __slots__ = ['acc_address', 'bytes', 'id']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    bytes: str
    id: int

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., bytes: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgShareSubscriptionResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgStartSessionRequest(_message.Message):
    __slots__ = ['id', 'node_address']
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_address: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgStartSessionResponse(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=...) -> None:
        ...

class MsgStartSubscriptionRequest(_message.Message):
    __slots__ = ['denom', 'id', 'renewal_price_policy']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    denom: str
    id: int
    renewal_price_policy: _renewal_pb2.RenewalPricePolicy

    def __init__(self, id: _Optional[int]=..., denom: _Optional[str]=..., renewal_price_policy: _Optional[_Union[(_renewal_pb2.RenewalPricePolicy, str)]]=..., **kwargs) -> None:
        ...

class MsgStartSubscriptionResponse(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=...) -> None:
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

class MsgUpdateSubscriptionRequest(_message.Message):
    __slots__ = ['id', 'renewal_price_policy']
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    id: int
    renewal_price_policy: _renewal_pb2.RenewalPricePolicy

    def __init__(self, id: _Optional[int]=..., renewal_price_policy: _Optional[_Union[(_renewal_pb2.RenewalPricePolicy, str)]]=..., **kwargs) -> None:
        ...

class MsgUpdateSubscriptionResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...
