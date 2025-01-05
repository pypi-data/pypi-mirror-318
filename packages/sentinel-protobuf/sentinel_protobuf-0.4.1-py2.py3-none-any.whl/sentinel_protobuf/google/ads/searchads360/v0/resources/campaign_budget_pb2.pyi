from google.ads.searchads360.v0.enums import budget_delivery_method_pb2 as _budget_delivery_method_pb2
from google.ads.searchads360.v0.enums import budget_period_pb2 as _budget_period_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignBudget(_message.Message):
    __slots__ = ("resource_name", "amount_micros", "delivery_method", "period")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    amount_micros: int
    delivery_method: _budget_delivery_method_pb2.BudgetDeliveryMethodEnum.BudgetDeliveryMethod
    period: _budget_period_pb2.BudgetPeriodEnum.BudgetPeriod
    def __init__(self, resource_name: _Optional[str] = ..., amount_micros: _Optional[int] = ..., delivery_method: _Optional[_Union[_budget_delivery_method_pb2.BudgetDeliveryMethodEnum.BudgetDeliveryMethod, str]] = ..., period: _Optional[_Union[_budget_period_pb2.BudgetPeriodEnum.BudgetPeriod, str]] = ...) -> None: ...
