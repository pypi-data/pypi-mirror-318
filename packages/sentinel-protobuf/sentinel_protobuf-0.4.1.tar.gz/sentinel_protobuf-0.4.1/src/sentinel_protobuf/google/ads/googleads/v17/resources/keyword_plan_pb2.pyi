from google.ads.googleads.v17.common import dates_pb2 as _dates_pb2
from google.ads.googleads.v17.enums import keyword_plan_forecast_interval_pb2 as _keyword_plan_forecast_interval_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlan(_message.Message):
    __slots__ = ("resource_name", "id", "name", "forecast_period")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORECAST_PERIOD_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    forecast_period: KeywordPlanForecastPeriod
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., forecast_period: _Optional[_Union[KeywordPlanForecastPeriod, _Mapping]] = ...) -> None: ...

class KeywordPlanForecastPeriod(_message.Message):
    __slots__ = ("date_interval", "date_range")
    DATE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    date_interval: _keyword_plan_forecast_interval_pb2.KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    date_range: _dates_pb2.DateRange
    def __init__(self, date_interval: _Optional[_Union[_keyword_plan_forecast_interval_pb2.KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval, str]] = ..., date_range: _Optional[_Union[_dates_pb2.DateRange, _Mapping]] = ...) -> None: ...
