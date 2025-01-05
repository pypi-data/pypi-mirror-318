from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.channel.v1 import common_pb2 as _common_pb2
from google.cloud.channel.v1 import products_pb2 as _products_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PromotionalOrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROMOTIONAL_TYPE_UNSPECIFIED: _ClassVar[PromotionalOrderType]
    NEW_UPGRADE: _ClassVar[PromotionalOrderType]
    TRANSFER: _ClassVar[PromotionalOrderType]
    PROMOTION_SWITCH: _ClassVar[PromotionalOrderType]

class PaymentPlan(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYMENT_PLAN_UNSPECIFIED: _ClassVar[PaymentPlan]
    COMMITMENT: _ClassVar[PaymentPlan]
    FLEXIBLE: _ClassVar[PaymentPlan]
    FREE: _ClassVar[PaymentPlan]
    TRIAL: _ClassVar[PaymentPlan]
    OFFLINE: _ClassVar[PaymentPlan]

class PaymentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYMENT_TYPE_UNSPECIFIED: _ClassVar[PaymentType]
    PREPAY: _ClassVar[PaymentType]
    POSTPAY: _ClassVar[PaymentType]

class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_TYPE_UNSPECIFIED: _ClassVar[ResourceType]
    SEAT: _ClassVar[ResourceType]
    MAU: _ClassVar[ResourceType]
    GB: _ClassVar[ResourceType]
    LICENSED_USER: _ClassVar[ResourceType]
    MINUTES: _ClassVar[ResourceType]
    IAAS_USAGE: _ClassVar[ResourceType]
    SUBSCRIPTION: _ClassVar[ResourceType]

class PeriodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERIOD_TYPE_UNSPECIFIED: _ClassVar[PeriodType]
    DAY: _ClassVar[PeriodType]
    MONTH: _ClassVar[PeriodType]
    YEAR: _ClassVar[PeriodType]
PROMOTIONAL_TYPE_UNSPECIFIED: PromotionalOrderType
NEW_UPGRADE: PromotionalOrderType
TRANSFER: PromotionalOrderType
PROMOTION_SWITCH: PromotionalOrderType
PAYMENT_PLAN_UNSPECIFIED: PaymentPlan
COMMITMENT: PaymentPlan
FLEXIBLE: PaymentPlan
FREE: PaymentPlan
TRIAL: PaymentPlan
OFFLINE: PaymentPlan
PAYMENT_TYPE_UNSPECIFIED: PaymentType
PREPAY: PaymentType
POSTPAY: PaymentType
RESOURCE_TYPE_UNSPECIFIED: ResourceType
SEAT: ResourceType
MAU: ResourceType
GB: ResourceType
LICENSED_USER: ResourceType
MINUTES: ResourceType
IAAS_USAGE: ResourceType
SUBSCRIPTION: ResourceType
PERIOD_TYPE_UNSPECIFIED: PeriodType
DAY: PeriodType
MONTH: PeriodType
YEAR: PeriodType

class Offer(_message.Message):
    __slots__ = ('name', 'marketing_info', 'sku', 'plan', 'constraints', 'price_by_resources', 'start_time', 'end_time', 'parameter_definitions', 'deal_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MARKETING_INFO_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    PRICE_BY_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    DEAL_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    marketing_info: _products_pb2.MarketingInfo
    sku: _products_pb2.Sku
    plan: Plan
    constraints: Constraints
    price_by_resources: _containers.RepeatedCompositeFieldContainer[PriceByResource]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    parameter_definitions: _containers.RepeatedCompositeFieldContainer[ParameterDefinition]
    deal_code: str

    def __init__(self, name: _Optional[str]=..., marketing_info: _Optional[_Union[_products_pb2.MarketingInfo, _Mapping]]=..., sku: _Optional[_Union[_products_pb2.Sku, _Mapping]]=..., plan: _Optional[_Union[Plan, _Mapping]]=..., constraints: _Optional[_Union[Constraints, _Mapping]]=..., price_by_resources: _Optional[_Iterable[_Union[PriceByResource, _Mapping]]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., parameter_definitions: _Optional[_Iterable[_Union[ParameterDefinition, _Mapping]]]=..., deal_code: _Optional[str]=...) -> None:
        ...

class ParameterDefinition(_message.Message):
    __slots__ = ('name', 'parameter_type', 'min_value', 'max_value', 'allowed_values', 'optional')

    class ParameterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARAMETER_TYPE_UNSPECIFIED: _ClassVar[ParameterDefinition.ParameterType]
        INT64: _ClassVar[ParameterDefinition.ParameterType]
        STRING: _ClassVar[ParameterDefinition.ParameterType]
        DOUBLE: _ClassVar[ParameterDefinition.ParameterType]
        BOOLEAN: _ClassVar[ParameterDefinition.ParameterType]
    PARAMETER_TYPE_UNSPECIFIED: ParameterDefinition.ParameterType
    INT64: ParameterDefinition.ParameterType
    STRING: ParameterDefinition.ParameterType
    DOUBLE: ParameterDefinition.ParameterType
    BOOLEAN: ParameterDefinition.ParameterType
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    parameter_type: ParameterDefinition.ParameterType
    min_value: _common_pb2.Value
    max_value: _common_pb2.Value
    allowed_values: _containers.RepeatedCompositeFieldContainer[_common_pb2.Value]
    optional: bool

    def __init__(self, name: _Optional[str]=..., parameter_type: _Optional[_Union[ParameterDefinition.ParameterType, str]]=..., min_value: _Optional[_Union[_common_pb2.Value, _Mapping]]=..., max_value: _Optional[_Union[_common_pb2.Value, _Mapping]]=..., allowed_values: _Optional[_Iterable[_Union[_common_pb2.Value, _Mapping]]]=..., optional: bool=...) -> None:
        ...

class Constraints(_message.Message):
    __slots__ = ('customer_constraints',)
    CUSTOMER_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    customer_constraints: CustomerConstraints

    def __init__(self, customer_constraints: _Optional[_Union[CustomerConstraints, _Mapping]]=...) -> None:
        ...

class CustomerConstraints(_message.Message):
    __slots__ = ('allowed_regions', 'allowed_customer_types', 'promotional_order_types')
    ALLOWED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CUSTOMER_TYPES_FIELD_NUMBER: _ClassVar[int]
    PROMOTIONAL_ORDER_TYPES_FIELD_NUMBER: _ClassVar[int]
    allowed_regions: _containers.RepeatedScalarFieldContainer[str]
    allowed_customer_types: _containers.RepeatedScalarFieldContainer[_common_pb2.CloudIdentityInfo.CustomerType]
    promotional_order_types: _containers.RepeatedScalarFieldContainer[PromotionalOrderType]

    def __init__(self, allowed_regions: _Optional[_Iterable[str]]=..., allowed_customer_types: _Optional[_Iterable[_Union[_common_pb2.CloudIdentityInfo.CustomerType, str]]]=..., promotional_order_types: _Optional[_Iterable[_Union[PromotionalOrderType, str]]]=...) -> None:
        ...

class Plan(_message.Message):
    __slots__ = ('payment_plan', 'payment_type', 'payment_cycle', 'trial_period', 'billing_account')
    PAYMENT_PLAN_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_CYCLE_FIELD_NUMBER: _ClassVar[int]
    TRIAL_PERIOD_FIELD_NUMBER: _ClassVar[int]
    BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    payment_plan: PaymentPlan
    payment_type: PaymentType
    payment_cycle: Period
    trial_period: Period
    billing_account: str

    def __init__(self, payment_plan: _Optional[_Union[PaymentPlan, str]]=..., payment_type: _Optional[_Union[PaymentType, str]]=..., payment_cycle: _Optional[_Union[Period, _Mapping]]=..., trial_period: _Optional[_Union[Period, _Mapping]]=..., billing_account: _Optional[str]=...) -> None:
        ...

class PriceByResource(_message.Message):
    __slots__ = ('resource_type', 'price', 'price_phases')
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRICE_PHASES_FIELD_NUMBER: _ClassVar[int]
    resource_type: ResourceType
    price: Price
    price_phases: _containers.RepeatedCompositeFieldContainer[PricePhase]

    def __init__(self, resource_type: _Optional[_Union[ResourceType, str]]=..., price: _Optional[_Union[Price, _Mapping]]=..., price_phases: _Optional[_Iterable[_Union[PricePhase, _Mapping]]]=...) -> None:
        ...

class Price(_message.Message):
    __slots__ = ('base_price', 'discount', 'effective_price', 'external_price_uri')
    BASE_PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PRICE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PRICE_URI_FIELD_NUMBER: _ClassVar[int]
    base_price: _money_pb2.Money
    discount: float
    effective_price: _money_pb2.Money
    external_price_uri: str

    def __init__(self, base_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., discount: _Optional[float]=..., effective_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., external_price_uri: _Optional[str]=...) -> None:
        ...

class PricePhase(_message.Message):
    __slots__ = ('period_type', 'first_period', 'last_period', 'price', 'price_tiers')
    PERIOD_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIRST_PERIOD_FIELD_NUMBER: _ClassVar[int]
    LAST_PERIOD_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRICE_TIERS_FIELD_NUMBER: _ClassVar[int]
    period_type: PeriodType
    first_period: int
    last_period: int
    price: Price
    price_tiers: _containers.RepeatedCompositeFieldContainer[PriceTier]

    def __init__(self, period_type: _Optional[_Union[PeriodType, str]]=..., first_period: _Optional[int]=..., last_period: _Optional[int]=..., price: _Optional[_Union[Price, _Mapping]]=..., price_tiers: _Optional[_Iterable[_Union[PriceTier, _Mapping]]]=...) -> None:
        ...

class PriceTier(_message.Message):
    __slots__ = ('first_resource', 'last_resource', 'price')
    FIRST_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    LAST_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    first_resource: int
    last_resource: int
    price: Price

    def __init__(self, first_resource: _Optional[int]=..., last_resource: _Optional[int]=..., price: _Optional[_Union[Price, _Mapping]]=...) -> None:
        ...

class Period(_message.Message):
    __slots__ = ('duration', 'period_type')
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PERIOD_TYPE_FIELD_NUMBER: _ClassVar[int]
    duration: int
    period_type: PeriodType

    def __init__(self, duration: _Optional[int]=..., period_type: _Optional[_Union[PeriodType, str]]=...) -> None:
        ...