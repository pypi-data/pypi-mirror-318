from google.ads.googleads.v17.enums import budget_delivery_method_pb2 as _budget_delivery_method_pb2
from google.ads.googleads.v17.enums import budget_period_pb2 as _budget_period_pb2
from google.ads.googleads.v17.enums import budget_status_pb2 as _budget_status_pb2
from google.ads.googleads.v17.enums import budget_type_pb2 as _budget_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignBudget(_message.Message):
    __slots__ = ("resource_name", "id", "name", "amount_micros", "total_amount_micros", "status", "delivery_method", "explicitly_shared", "reference_count", "has_recommended_budget", "recommended_budget_amount_micros", "period", "recommended_budget_estimated_change_weekly_clicks", "recommended_budget_estimated_change_weekly_cost_micros", "recommended_budget_estimated_change_weekly_interactions", "recommended_budget_estimated_change_weekly_views", "type", "aligned_bidding_strategy_id")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    EXPLICITLY_SHARED_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_RECOMMENDED_BUDGET_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_BUDGET_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_BUDGET_ESTIMATED_CHANGE_WEEKLY_CLICKS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_BUDGET_ESTIMATED_CHANGE_WEEKLY_COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_BUDGET_ESTIMATED_CHANGE_WEEKLY_INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_BUDGET_ESTIMATED_CHANGE_WEEKLY_VIEWS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ALIGNED_BIDDING_STRATEGY_ID_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    amount_micros: int
    total_amount_micros: int
    status: _budget_status_pb2.BudgetStatusEnum.BudgetStatus
    delivery_method: _budget_delivery_method_pb2.BudgetDeliveryMethodEnum.BudgetDeliveryMethod
    explicitly_shared: bool
    reference_count: int
    has_recommended_budget: bool
    recommended_budget_amount_micros: int
    period: _budget_period_pb2.BudgetPeriodEnum.BudgetPeriod
    recommended_budget_estimated_change_weekly_clicks: int
    recommended_budget_estimated_change_weekly_cost_micros: int
    recommended_budget_estimated_change_weekly_interactions: int
    recommended_budget_estimated_change_weekly_views: int
    type: _budget_type_pb2.BudgetTypeEnum.BudgetType
    aligned_bidding_strategy_id: int
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., amount_micros: _Optional[int] = ..., total_amount_micros: _Optional[int] = ..., status: _Optional[_Union[_budget_status_pb2.BudgetStatusEnum.BudgetStatus, str]] = ..., delivery_method: _Optional[_Union[_budget_delivery_method_pb2.BudgetDeliveryMethodEnum.BudgetDeliveryMethod, str]] = ..., explicitly_shared: bool = ..., reference_count: _Optional[int] = ..., has_recommended_budget: bool = ..., recommended_budget_amount_micros: _Optional[int] = ..., period: _Optional[_Union[_budget_period_pb2.BudgetPeriodEnum.BudgetPeriod, str]] = ..., recommended_budget_estimated_change_weekly_clicks: _Optional[int] = ..., recommended_budget_estimated_change_weekly_cost_micros: _Optional[int] = ..., recommended_budget_estimated_change_weekly_interactions: _Optional[int] = ..., recommended_budget_estimated_change_weekly_views: _Optional[int] = ..., type: _Optional[_Union[_budget_type_pb2.BudgetTypeEnum.BudgetType, str]] = ..., aligned_bidding_strategy_id: _Optional[int] = ...) -> None: ...
