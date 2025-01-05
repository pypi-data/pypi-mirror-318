from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Weight(_message.Message):
    __slots__ = ("amount_micros", "unit")
    class WeightUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WEIGHT_UNIT_UNSPECIFIED: _ClassVar[Weight.WeightUnit]
        POUND: _ClassVar[Weight.WeightUnit]
        KILOGRAM: _ClassVar[Weight.WeightUnit]
    WEIGHT_UNIT_UNSPECIFIED: Weight.WeightUnit
    POUND: Weight.WeightUnit
    KILOGRAM: Weight.WeightUnit
    AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    amount_micros: int
    unit: Weight.WeightUnit
    def __init__(self, amount_micros: _Optional[int] = ..., unit: _Optional[_Union[Weight.WeightUnit, str]] = ...) -> None: ...

class Price(_message.Message):
    __slots__ = ("amount_micros", "currency_code")
    AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    amount_micros: int
    currency_code: str
    def __init__(self, amount_micros: _Optional[int] = ..., currency_code: _Optional[str] = ...) -> None: ...

class CustomAttribute(_message.Message):
    __slots__ = ("name", "value", "group_values")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    GROUP_VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    group_values: _containers.RepeatedCompositeFieldContainer[CustomAttribute]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., group_values: _Optional[_Iterable[_Union[CustomAttribute, _Mapping]]] = ...) -> None: ...

class Destination(_message.Message):
    __slots__ = ()
    class DestinationEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DESTINATION_ENUM_UNSPECIFIED: _ClassVar[Destination.DestinationEnum]
        SHOPPING_ADS: _ClassVar[Destination.DestinationEnum]
        DISPLAY_ADS: _ClassVar[Destination.DestinationEnum]
        LOCAL_INVENTORY_ADS: _ClassVar[Destination.DestinationEnum]
        FREE_LISTINGS: _ClassVar[Destination.DestinationEnum]
        FREE_LOCAL_LISTINGS: _ClassVar[Destination.DestinationEnum]
        YOUTUBE_SHOPPING: _ClassVar[Destination.DestinationEnum]
    DESTINATION_ENUM_UNSPECIFIED: Destination.DestinationEnum
    SHOPPING_ADS: Destination.DestinationEnum
    DISPLAY_ADS: Destination.DestinationEnum
    LOCAL_INVENTORY_ADS: Destination.DestinationEnum
    FREE_LISTINGS: Destination.DestinationEnum
    FREE_LOCAL_LISTINGS: Destination.DestinationEnum
    YOUTUBE_SHOPPING: Destination.DestinationEnum
    def __init__(self) -> None: ...

class ReportingContext(_message.Message):
    __slots__ = ()
    class ReportingContextEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPORTING_CONTEXT_ENUM_UNSPECIFIED: _ClassVar[ReportingContext.ReportingContextEnum]
        SHOPPING_ADS: _ClassVar[ReportingContext.ReportingContextEnum]
        DISCOVERY_ADS: _ClassVar[ReportingContext.ReportingContextEnum]
        DEMAND_GEN_ADS: _ClassVar[ReportingContext.ReportingContextEnum]
        DEMAND_GEN_ADS_DISCOVER_SURFACE: _ClassVar[ReportingContext.ReportingContextEnum]
        VIDEO_ADS: _ClassVar[ReportingContext.ReportingContextEnum]
        DISPLAY_ADS: _ClassVar[ReportingContext.ReportingContextEnum]
        LOCAL_INVENTORY_ADS: _ClassVar[ReportingContext.ReportingContextEnum]
        VEHICLE_INVENTORY_ADS: _ClassVar[ReportingContext.ReportingContextEnum]
        FREE_LISTINGS: _ClassVar[ReportingContext.ReportingContextEnum]
        FREE_LOCAL_LISTINGS: _ClassVar[ReportingContext.ReportingContextEnum]
        FREE_LOCAL_VEHICLE_LISTINGS: _ClassVar[ReportingContext.ReportingContextEnum]
        YOUTUBE_SHOPPING: _ClassVar[ReportingContext.ReportingContextEnum]
        CLOUD_RETAIL: _ClassVar[ReportingContext.ReportingContextEnum]
        LOCAL_CLOUD_RETAIL: _ClassVar[ReportingContext.ReportingContextEnum]
    REPORTING_CONTEXT_ENUM_UNSPECIFIED: ReportingContext.ReportingContextEnum
    SHOPPING_ADS: ReportingContext.ReportingContextEnum
    DISCOVERY_ADS: ReportingContext.ReportingContextEnum
    DEMAND_GEN_ADS: ReportingContext.ReportingContextEnum
    DEMAND_GEN_ADS_DISCOVER_SURFACE: ReportingContext.ReportingContextEnum
    VIDEO_ADS: ReportingContext.ReportingContextEnum
    DISPLAY_ADS: ReportingContext.ReportingContextEnum
    LOCAL_INVENTORY_ADS: ReportingContext.ReportingContextEnum
    VEHICLE_INVENTORY_ADS: ReportingContext.ReportingContextEnum
    FREE_LISTINGS: ReportingContext.ReportingContextEnum
    FREE_LOCAL_LISTINGS: ReportingContext.ReportingContextEnum
    FREE_LOCAL_VEHICLE_LISTINGS: ReportingContext.ReportingContextEnum
    YOUTUBE_SHOPPING: ReportingContext.ReportingContextEnum
    CLOUD_RETAIL: ReportingContext.ReportingContextEnum
    LOCAL_CLOUD_RETAIL: ReportingContext.ReportingContextEnum
    def __init__(self) -> None: ...

class Channel(_message.Message):
    __slots__ = ()
    class ChannelEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANNEL_ENUM_UNSPECIFIED: _ClassVar[Channel.ChannelEnum]
        ONLINE: _ClassVar[Channel.ChannelEnum]
        LOCAL: _ClassVar[Channel.ChannelEnum]
    CHANNEL_ENUM_UNSPECIFIED: Channel.ChannelEnum
    ONLINE: Channel.ChannelEnum
    LOCAL: Channel.ChannelEnum
    def __init__(self) -> None: ...
