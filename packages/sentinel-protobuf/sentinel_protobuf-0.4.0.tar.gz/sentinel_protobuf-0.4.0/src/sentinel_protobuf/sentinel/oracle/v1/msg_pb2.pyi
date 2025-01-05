
from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.oracle.v1 import params_pb2 as _params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateAssetRequest(_message.Message):
    __slots__ = ['base_asset_denom', 'decimals', 'denom', 'quote_asset_denom']
    BASE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    QUOTE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    base_asset_denom: str
    decimals: int
    denom: str
    quote_asset_denom: str

    def __init__(self, denom: _Optional[str]=..., decimals: _Optional[int]=..., base_asset_denom: _Optional[str]=..., quote_asset_denom: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgCreateAssetResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgDeleteAssetRequest(_message.Message):
    __slots__ = ['denom']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    denom: str

    def __init__(self, denom: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgDeleteAssetResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgUpdateAssetRequest(_message.Message):
    __slots__ = ['base_asset_denom', 'decimals', 'denom', 'quote_asset_denom']
    BASE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    QUOTE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    base_asset_denom: str
    decimals: int
    denom: str
    quote_asset_denom: str

    def __init__(self, denom: _Optional[str]=..., decimals: _Optional[int]=..., base_asset_denom: _Optional[str]=..., quote_asset_denom: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgUpdateAssetResponse(_message.Message):
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
