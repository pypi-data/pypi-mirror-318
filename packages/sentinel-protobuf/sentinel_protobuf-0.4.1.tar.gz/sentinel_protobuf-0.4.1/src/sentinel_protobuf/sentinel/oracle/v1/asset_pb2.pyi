from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Asset(_message.Message):
    __slots__ = ('denom', 'decimals', 'base_asset_denom', 'quote_asset_denom', 'price', 'height')
    DENOM_FIELD_NUMBER: _ClassVar[int]
    DECIMALS_FIELD_NUMBER: _ClassVar[int]
    BASE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    QUOTE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    denom: str
    decimals: int
    base_asset_denom: str
    quote_asset_denom: str
    price: str
    height: int

    def __init__(self, denom: _Optional[str]=..., decimals: _Optional[int]=..., base_asset_denom: _Optional[str]=..., quote_asset_denom: _Optional[str]=..., price: _Optional[str]=..., height: _Optional[int]=...) -> None:
        ...