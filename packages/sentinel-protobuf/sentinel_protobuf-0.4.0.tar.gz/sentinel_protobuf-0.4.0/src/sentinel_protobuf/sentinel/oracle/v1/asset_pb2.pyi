
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Asset(_message.Message):
    __slots__ = ['base_asset_denom', 'decimals', 'denom', 'height', 'price', 'quote_asset_denom']
    BASE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUOTE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    base_asset_denom: str
    decimals: int
    denom: str
    height: int
    price: str
    quote_asset_denom: str

    def __init__(self, denom: _Optional[str]=..., decimals: _Optional[int]=..., base_asset_denom: _Optional[str]=..., quote_asset_denom: _Optional[str]=..., price: _Optional[str]=..., height: _Optional[int]=...) -> None:
        ...
