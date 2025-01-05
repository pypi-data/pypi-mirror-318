from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.node.v3 import params_pb2 as _params_pb2
from sentinel.types.v1 import price_pb2 as _price_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgRegisterNodeRequest(_message.Message):
    __slots__ = ('gigabyte_prices', 'hourly_prices', 'remote_url')
    FROM_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    gigabyte_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    hourly_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    remote_url: str

    def __init__(self, gigabyte_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., hourly_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., remote_url: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgUpdateNodeDetailsRequest(_message.Message):
    __slots__ = ('gigabyte_prices', 'hourly_prices', 'remote_url')
    FROM_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    gigabyte_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    hourly_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    remote_url: str

    def __init__(self, gigabyte_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., hourly_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., remote_url: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgUpdateNodeStatusRequest(_message.Message):
    __slots__ = ('status',)
    FROM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status

    def __init__(self, status: _Optional[_Union[_status_pb2.Status, str]]=..., **kwargs) -> None:
        ...

class MsgStartSessionRequest(_message.Message):
    __slots__ = ('node_address', 'gigabytes', 'hours', 'denom')
    FROM_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    node_address: str
    gigabytes: int
    hours: int
    denom: str

    def __init__(self, node_address: _Optional[str]=..., gigabytes: _Optional[int]=..., hours: _Optional[int]=..., denom: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgUpdateParamsRequest(_message.Message):
    __slots__ = ('params',)
    FROM_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.Params

    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]]=..., **kwargs) -> None:
        ...

class MsgRegisterNodeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateNodeDetailsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateNodeStatusResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgStartSessionResponse(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=...) -> None:
        ...

class MsgUpdateParamsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...