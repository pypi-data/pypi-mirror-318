from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.type import decimal_pb2 as _decimal_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RebillingBasis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REBILLING_BASIS_UNSPECIFIED: _ClassVar[RebillingBasis]
    COST_AT_LIST: _ClassVar[RebillingBasis]
    DIRECT_CUSTOMER_COST: _ClassVar[RebillingBasis]
REBILLING_BASIS_UNSPECIFIED: RebillingBasis
COST_AT_LIST: RebillingBasis
DIRECT_CUSTOMER_COST: RebillingBasis

class CustomerRepricingConfig(_message.Message):
    __slots__ = ('name', 'repricing_config', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPRICING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    repricing_config: RepricingConfig
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., repricing_config: _Optional[_Union[RepricingConfig, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ChannelPartnerRepricingConfig(_message.Message):
    __slots__ = ('name', 'repricing_config', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPRICING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    repricing_config: RepricingConfig
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., repricing_config: _Optional[_Union[RepricingConfig, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RepricingConfig(_message.Message):
    __slots__ = ('entitlement_granularity', 'channel_partner_granularity', 'effective_invoice_month', 'adjustment', 'rebilling_basis', 'conditional_overrides')

    class EntitlementGranularity(_message.Message):
        __slots__ = ('entitlement',)
        ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
        entitlement: str

        def __init__(self, entitlement: _Optional[str]=...) -> None:
            ...

    class ChannelPartnerGranularity(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    ENTITLEMENT_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PARTNER_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_INVOICE_MONTH_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    REBILLING_BASIS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONAL_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    entitlement_granularity: RepricingConfig.EntitlementGranularity
    channel_partner_granularity: RepricingConfig.ChannelPartnerGranularity
    effective_invoice_month: _date_pb2.Date
    adjustment: RepricingAdjustment
    rebilling_basis: RebillingBasis
    conditional_overrides: _containers.RepeatedCompositeFieldContainer[ConditionalOverride]

    def __init__(self, entitlement_granularity: _Optional[_Union[RepricingConfig.EntitlementGranularity, _Mapping]]=..., channel_partner_granularity: _Optional[_Union[RepricingConfig.ChannelPartnerGranularity, _Mapping]]=..., effective_invoice_month: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., adjustment: _Optional[_Union[RepricingAdjustment, _Mapping]]=..., rebilling_basis: _Optional[_Union[RebillingBasis, str]]=..., conditional_overrides: _Optional[_Iterable[_Union[ConditionalOverride, _Mapping]]]=...) -> None:
        ...

class RepricingAdjustment(_message.Message):
    __slots__ = ('percentage_adjustment',)
    PERCENTAGE_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    percentage_adjustment: PercentageAdjustment

    def __init__(self, percentage_adjustment: _Optional[_Union[PercentageAdjustment, _Mapping]]=...) -> None:
        ...

class PercentageAdjustment(_message.Message):
    __slots__ = ('percentage',)
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    percentage: _decimal_pb2.Decimal

    def __init__(self, percentage: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]]=...) -> None:
        ...

class ConditionalOverride(_message.Message):
    __slots__ = ('adjustment', 'rebilling_basis', 'repricing_condition')
    ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    REBILLING_BASIS_FIELD_NUMBER: _ClassVar[int]
    REPRICING_CONDITION_FIELD_NUMBER: _ClassVar[int]
    adjustment: RepricingAdjustment
    rebilling_basis: RebillingBasis
    repricing_condition: RepricingCondition

    def __init__(self, adjustment: _Optional[_Union[RepricingAdjustment, _Mapping]]=..., rebilling_basis: _Optional[_Union[RebillingBasis, str]]=..., repricing_condition: _Optional[_Union[RepricingCondition, _Mapping]]=...) -> None:
        ...

class RepricingCondition(_message.Message):
    __slots__ = ('sku_group_condition',)
    SKU_GROUP_CONDITION_FIELD_NUMBER: _ClassVar[int]
    sku_group_condition: SkuGroupCondition

    def __init__(self, sku_group_condition: _Optional[_Union[SkuGroupCondition, _Mapping]]=...) -> None:
        ...

class SkuGroupCondition(_message.Message):
    __slots__ = ('sku_group',)
    SKU_GROUP_FIELD_NUMBER: _ClassVar[int]
    sku_group: str

    def __init__(self, sku_group: _Optional[str]=...) -> None:
        ...