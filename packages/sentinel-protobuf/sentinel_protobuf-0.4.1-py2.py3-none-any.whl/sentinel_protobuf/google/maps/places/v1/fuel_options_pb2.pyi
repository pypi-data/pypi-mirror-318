from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FuelOptions(_message.Message):
    __slots__ = ('fuel_prices',)

    class FuelPrice(_message.Message):
        __slots__ = ('type', 'price', 'update_time')

        class FuelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FUEL_TYPE_UNSPECIFIED: _ClassVar[FuelOptions.FuelPrice.FuelType]
            DIESEL: _ClassVar[FuelOptions.FuelPrice.FuelType]
            REGULAR_UNLEADED: _ClassVar[FuelOptions.FuelPrice.FuelType]
            MIDGRADE: _ClassVar[FuelOptions.FuelPrice.FuelType]
            PREMIUM: _ClassVar[FuelOptions.FuelPrice.FuelType]
            SP91: _ClassVar[FuelOptions.FuelPrice.FuelType]
            SP91_E10: _ClassVar[FuelOptions.FuelPrice.FuelType]
            SP92: _ClassVar[FuelOptions.FuelPrice.FuelType]
            SP95: _ClassVar[FuelOptions.FuelPrice.FuelType]
            SP95_E10: _ClassVar[FuelOptions.FuelPrice.FuelType]
            SP98: _ClassVar[FuelOptions.FuelPrice.FuelType]
            SP99: _ClassVar[FuelOptions.FuelPrice.FuelType]
            SP100: _ClassVar[FuelOptions.FuelPrice.FuelType]
            LPG: _ClassVar[FuelOptions.FuelPrice.FuelType]
            E80: _ClassVar[FuelOptions.FuelPrice.FuelType]
            E85: _ClassVar[FuelOptions.FuelPrice.FuelType]
            METHANE: _ClassVar[FuelOptions.FuelPrice.FuelType]
            BIO_DIESEL: _ClassVar[FuelOptions.FuelPrice.FuelType]
            TRUCK_DIESEL: _ClassVar[FuelOptions.FuelPrice.FuelType]
        FUEL_TYPE_UNSPECIFIED: FuelOptions.FuelPrice.FuelType
        DIESEL: FuelOptions.FuelPrice.FuelType
        REGULAR_UNLEADED: FuelOptions.FuelPrice.FuelType
        MIDGRADE: FuelOptions.FuelPrice.FuelType
        PREMIUM: FuelOptions.FuelPrice.FuelType
        SP91: FuelOptions.FuelPrice.FuelType
        SP91_E10: FuelOptions.FuelPrice.FuelType
        SP92: FuelOptions.FuelPrice.FuelType
        SP95: FuelOptions.FuelPrice.FuelType
        SP95_E10: FuelOptions.FuelPrice.FuelType
        SP98: FuelOptions.FuelPrice.FuelType
        SP99: FuelOptions.FuelPrice.FuelType
        SP100: FuelOptions.FuelPrice.FuelType
        LPG: FuelOptions.FuelPrice.FuelType
        E80: FuelOptions.FuelPrice.FuelType
        E85: FuelOptions.FuelPrice.FuelType
        METHANE: FuelOptions.FuelPrice.FuelType
        BIO_DIESEL: FuelOptions.FuelPrice.FuelType
        TRUCK_DIESEL: FuelOptions.FuelPrice.FuelType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        type: FuelOptions.FuelPrice.FuelType
        price: _money_pb2.Money
        update_time: _timestamp_pb2.Timestamp

        def __init__(self, type: _Optional[_Union[FuelOptions.FuelPrice.FuelType, str]]=..., price: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    FUEL_PRICES_FIELD_NUMBER: _ClassVar[int]
    fuel_prices: _containers.RepeatedCompositeFieldContainer[FuelOptions.FuelPrice]

    def __init__(self, fuel_prices: _Optional[_Iterable[_Union[FuelOptions.FuelPrice, _Mapping]]]=...) -> None:
        ...