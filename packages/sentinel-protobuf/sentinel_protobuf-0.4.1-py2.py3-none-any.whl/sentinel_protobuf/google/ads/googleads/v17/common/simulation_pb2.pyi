from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CpcBidSimulationPointList(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[CpcBidSimulationPoint]
    def __init__(self, points: _Optional[_Iterable[_Union[CpcBidSimulationPoint, _Mapping]]] = ...) -> None: ...

class CpvBidSimulationPointList(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[CpvBidSimulationPoint]
    def __init__(self, points: _Optional[_Iterable[_Union[CpvBidSimulationPoint, _Mapping]]] = ...) -> None: ...

class TargetCpaSimulationPointList(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[TargetCpaSimulationPoint]
    def __init__(self, points: _Optional[_Iterable[_Union[TargetCpaSimulationPoint, _Mapping]]] = ...) -> None: ...

class TargetRoasSimulationPointList(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[TargetRoasSimulationPoint]
    def __init__(self, points: _Optional[_Iterable[_Union[TargetRoasSimulationPoint, _Mapping]]] = ...) -> None: ...

class PercentCpcBidSimulationPointList(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[PercentCpcBidSimulationPoint]
    def __init__(self, points: _Optional[_Iterable[_Union[PercentCpcBidSimulationPoint, _Mapping]]] = ...) -> None: ...

class BudgetSimulationPointList(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[BudgetSimulationPoint]
    def __init__(self, points: _Optional[_Iterable[_Union[BudgetSimulationPoint, _Mapping]]] = ...) -> None: ...

class TargetImpressionShareSimulationPointList(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[TargetImpressionShareSimulationPoint]
    def __init__(self, points: _Optional[_Iterable[_Union[TargetImpressionShareSimulationPoint, _Mapping]]] = ...) -> None: ...

class CpcBidSimulationPoint(_message.Message):
    __slots__ = ("required_budget_amount_micros", "biddable_conversions", "biddable_conversions_value", "clicks", "cost_micros", "impressions", "top_slot_impressions", "cpc_bid_micros", "cpc_bid_scaling_modifier")
    REQUIRED_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_VALUE_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOP_SLOT_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_SCALING_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    required_budget_amount_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    cpc_bid_micros: int
    cpc_bid_scaling_modifier: float
    def __init__(self, required_budget_amount_micros: _Optional[int] = ..., biddable_conversions: _Optional[float] = ..., biddable_conversions_value: _Optional[float] = ..., clicks: _Optional[int] = ..., cost_micros: _Optional[int] = ..., impressions: _Optional[int] = ..., top_slot_impressions: _Optional[int] = ..., cpc_bid_micros: _Optional[int] = ..., cpc_bid_scaling_modifier: _Optional[float] = ...) -> None: ...

class CpvBidSimulationPoint(_message.Message):
    __slots__ = ("cpv_bid_micros", "cost_micros", "impressions", "views")
    CPV_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    cpv_bid_micros: int
    cost_micros: int
    impressions: int
    views: int
    def __init__(self, cpv_bid_micros: _Optional[int] = ..., cost_micros: _Optional[int] = ..., impressions: _Optional[int] = ..., views: _Optional[int] = ...) -> None: ...

class TargetCpaSimulationPoint(_message.Message):
    __slots__ = ("required_budget_amount_micros", "biddable_conversions", "biddable_conversions_value", "app_installs", "in_app_actions", "clicks", "cost_micros", "impressions", "top_slot_impressions", "interactions", "target_cpa_micros", "target_cpa_scaling_modifier")
    REQUIRED_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_VALUE_FIELD_NUMBER: _ClassVar[int]
    APP_INSTALLS_FIELD_NUMBER: _ClassVar[int]
    IN_APP_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOP_SLOT_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_SCALING_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    required_budget_amount_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    app_installs: float
    in_app_actions: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    interactions: int
    target_cpa_micros: int
    target_cpa_scaling_modifier: float
    def __init__(self, required_budget_amount_micros: _Optional[int] = ..., biddable_conversions: _Optional[float] = ..., biddable_conversions_value: _Optional[float] = ..., app_installs: _Optional[float] = ..., in_app_actions: _Optional[float] = ..., clicks: _Optional[int] = ..., cost_micros: _Optional[int] = ..., impressions: _Optional[int] = ..., top_slot_impressions: _Optional[int] = ..., interactions: _Optional[int] = ..., target_cpa_micros: _Optional[int] = ..., target_cpa_scaling_modifier: _Optional[float] = ...) -> None: ...

class TargetRoasSimulationPoint(_message.Message):
    __slots__ = ("target_roas", "required_budget_amount_micros", "biddable_conversions", "biddable_conversions_value", "clicks", "cost_micros", "impressions", "top_slot_impressions")
    TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_VALUE_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOP_SLOT_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    target_roas: float
    required_budget_amount_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    def __init__(self, target_roas: _Optional[float] = ..., required_budget_amount_micros: _Optional[int] = ..., biddable_conversions: _Optional[float] = ..., biddable_conversions_value: _Optional[float] = ..., clicks: _Optional[int] = ..., cost_micros: _Optional[int] = ..., impressions: _Optional[int] = ..., top_slot_impressions: _Optional[int] = ...) -> None: ...

class PercentCpcBidSimulationPoint(_message.Message):
    __slots__ = ("percent_cpc_bid_micros", "biddable_conversions", "biddable_conversions_value", "clicks", "cost_micros", "impressions", "top_slot_impressions")
    PERCENT_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_VALUE_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOP_SLOT_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    percent_cpc_bid_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    def __init__(self, percent_cpc_bid_micros: _Optional[int] = ..., biddable_conversions: _Optional[float] = ..., biddable_conversions_value: _Optional[float] = ..., clicks: _Optional[int] = ..., cost_micros: _Optional[int] = ..., impressions: _Optional[int] = ..., top_slot_impressions: _Optional[int] = ...) -> None: ...

class BudgetSimulationPoint(_message.Message):
    __slots__ = ("budget_amount_micros", "required_cpc_bid_ceiling_micros", "biddable_conversions", "biddable_conversions_value", "clicks", "cost_micros", "impressions", "top_slot_impressions", "interactions")
    BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_VALUE_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOP_SLOT_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    budget_amount_micros: int
    required_cpc_bid_ceiling_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    interactions: int
    def __init__(self, budget_amount_micros: _Optional[int] = ..., required_cpc_bid_ceiling_micros: _Optional[int] = ..., biddable_conversions: _Optional[float] = ..., biddable_conversions_value: _Optional[float] = ..., clicks: _Optional[int] = ..., cost_micros: _Optional[int] = ..., impressions: _Optional[int] = ..., top_slot_impressions: _Optional[int] = ..., interactions: _Optional[int] = ...) -> None: ...

class TargetImpressionShareSimulationPoint(_message.Message):
    __slots__ = ("target_impression_share_micros", "required_cpc_bid_ceiling_micros", "required_budget_amount_micros", "biddable_conversions", "biddable_conversions_value", "clicks", "cost_micros", "impressions", "top_slot_impressions", "absolute_top_impressions")
    TARGET_IMPRESSION_SHARE_MICROS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CPC_BID_CEILING_MICROS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_CONVERSIONS_VALUE_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOP_SLOT_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_TOP_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    target_impression_share_micros: int
    required_cpc_bid_ceiling_micros: int
    required_budget_amount_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    absolute_top_impressions: int
    def __init__(self, target_impression_share_micros: _Optional[int] = ..., required_cpc_bid_ceiling_micros: _Optional[int] = ..., required_budget_amount_micros: _Optional[int] = ..., biddable_conversions: _Optional[float] = ..., biddable_conversions_value: _Optional[float] = ..., clicks: _Optional[int] = ..., cost_micros: _Optional[int] = ..., impressions: _Optional[int] = ..., top_slot_impressions: _Optional[int] = ..., absolute_top_impressions: _Optional[int] = ...) -> None: ...
