from google.ads.googleads.v18.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v18.common import dates_pb2 as _dates_pb2
from google.ads.googleads.v18.enums import frequency_cap_time_unit_pb2 as _frequency_cap_time_unit_pb2
from google.ads.googleads.v18.enums import reach_plan_age_range_pb2 as _reach_plan_age_range_pb2
from google.ads.googleads.v18.enums import reach_plan_network_pb2 as _reach_plan_network_pb2
from google.ads.googleads.v18.enums import reach_plan_surface_pb2 as _reach_plan_surface_pb2
from google.ads.googleads.v18.enums import target_frequency_time_unit_pb2 as _target_frequency_time_unit_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListPlannableLocationsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPlannableLocationsResponse(_message.Message):
    __slots__ = ("plannable_locations",)
    PLANNABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    plannable_locations: _containers.RepeatedCompositeFieldContainer[PlannableLocation]
    def __init__(self, plannable_locations: _Optional[_Iterable[_Union[PlannableLocation, _Mapping]]] = ...) -> None: ...

class PlannableLocation(_message.Message):
    __slots__ = ("id", "name", "parent_country_id", "country_code", "location_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    parent_country_id: int
    country_code: str
    location_type: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., parent_country_id: _Optional[int] = ..., country_code: _Optional[str] = ..., location_type: _Optional[str] = ...) -> None: ...

class ListPlannableProductsRequest(_message.Message):
    __slots__ = ("plannable_location_id",)
    PLANNABLE_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    plannable_location_id: str
    def __init__(self, plannable_location_id: _Optional[str] = ...) -> None: ...

class ListPlannableProductsResponse(_message.Message):
    __slots__ = ("product_metadata",)
    PRODUCT_METADATA_FIELD_NUMBER: _ClassVar[int]
    product_metadata: _containers.RepeatedCompositeFieldContainer[ProductMetadata]
    def __init__(self, product_metadata: _Optional[_Iterable[_Union[ProductMetadata, _Mapping]]] = ...) -> None: ...

class ProductMetadata(_message.Message):
    __slots__ = ("plannable_product_code", "plannable_product_name", "plannable_targeting")
    PLANNABLE_PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    PLANNABLE_PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANNABLE_TARGETING_FIELD_NUMBER: _ClassVar[int]
    plannable_product_code: str
    plannable_product_name: str
    plannable_targeting: PlannableTargeting
    def __init__(self, plannable_product_code: _Optional[str] = ..., plannable_product_name: _Optional[str] = ..., plannable_targeting: _Optional[_Union[PlannableTargeting, _Mapping]] = ...) -> None: ...

class PlannableTargeting(_message.Message):
    __slots__ = ("age_ranges", "genders", "devices", "networks", "youtube_select_lineups", "surface_targeting")
    AGE_RANGES_FIELD_NUMBER: _ClassVar[int]
    GENDERS_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_SELECT_LINEUPS_FIELD_NUMBER: _ClassVar[int]
    SURFACE_TARGETING_FIELD_NUMBER: _ClassVar[int]
    age_ranges: _containers.RepeatedScalarFieldContainer[_reach_plan_age_range_pb2.ReachPlanAgeRangeEnum.ReachPlanAgeRange]
    genders: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.GenderInfo]
    devices: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.DeviceInfo]
    networks: _containers.RepeatedScalarFieldContainer[_reach_plan_network_pb2.ReachPlanNetworkEnum.ReachPlanNetwork]
    youtube_select_lineups: _containers.RepeatedCompositeFieldContainer[YouTubeSelectLineUp]
    surface_targeting: SurfaceTargetingCombinations
    def __init__(self, age_ranges: _Optional[_Iterable[_Union[_reach_plan_age_range_pb2.ReachPlanAgeRangeEnum.ReachPlanAgeRange, str]]] = ..., genders: _Optional[_Iterable[_Union[_criteria_pb2.GenderInfo, _Mapping]]] = ..., devices: _Optional[_Iterable[_Union[_criteria_pb2.DeviceInfo, _Mapping]]] = ..., networks: _Optional[_Iterable[_Union[_reach_plan_network_pb2.ReachPlanNetworkEnum.ReachPlanNetwork, str]]] = ..., youtube_select_lineups: _Optional[_Iterable[_Union[YouTubeSelectLineUp, _Mapping]]] = ..., surface_targeting: _Optional[_Union[SurfaceTargetingCombinations, _Mapping]] = ...) -> None: ...

class GenerateReachForecastRequest(_message.Message):
    __slots__ = ("customer_id", "currency_code", "campaign_duration", "cookie_frequency_cap", "cookie_frequency_cap_setting", "min_effective_frequency", "effective_frequency_limit", "targeting", "planned_products", "forecast_metric_options", "customer_reach_group")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DURATION_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FREQUENCY_CAP_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FREQUENCY_CAP_SETTING_FIELD_NUMBER: _ClassVar[int]
    MIN_EFFECTIVE_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_FREQUENCY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TARGETING_FIELD_NUMBER: _ClassVar[int]
    PLANNED_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    FORECAST_METRIC_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_REACH_GROUP_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    currency_code: str
    campaign_duration: CampaignDuration
    cookie_frequency_cap: int
    cookie_frequency_cap_setting: FrequencyCap
    min_effective_frequency: int
    effective_frequency_limit: EffectiveFrequencyLimit
    targeting: Targeting
    planned_products: _containers.RepeatedCompositeFieldContainer[PlannedProduct]
    forecast_metric_options: ForecastMetricOptions
    customer_reach_group: str
    def __init__(self, customer_id: _Optional[str] = ..., currency_code: _Optional[str] = ..., campaign_duration: _Optional[_Union[CampaignDuration, _Mapping]] = ..., cookie_frequency_cap: _Optional[int] = ..., cookie_frequency_cap_setting: _Optional[_Union[FrequencyCap, _Mapping]] = ..., min_effective_frequency: _Optional[int] = ..., effective_frequency_limit: _Optional[_Union[EffectiveFrequencyLimit, _Mapping]] = ..., targeting: _Optional[_Union[Targeting, _Mapping]] = ..., planned_products: _Optional[_Iterable[_Union[PlannedProduct, _Mapping]]] = ..., forecast_metric_options: _Optional[_Union[ForecastMetricOptions, _Mapping]] = ..., customer_reach_group: _Optional[str] = ...) -> None: ...

class EffectiveFrequencyLimit(_message.Message):
    __slots__ = ("effective_frequency_breakdown_limit",)
    EFFECTIVE_FREQUENCY_BREAKDOWN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    effective_frequency_breakdown_limit: int
    def __init__(self, effective_frequency_breakdown_limit: _Optional[int] = ...) -> None: ...

class FrequencyCap(_message.Message):
    __slots__ = ("impressions", "time_unit")
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_UNIT_FIELD_NUMBER: _ClassVar[int]
    impressions: int
    time_unit: _frequency_cap_time_unit_pb2.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    def __init__(self, impressions: _Optional[int] = ..., time_unit: _Optional[_Union[_frequency_cap_time_unit_pb2.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit, str]] = ...) -> None: ...

class Targeting(_message.Message):
    __slots__ = ("plannable_location_id", "plannable_location_ids", "age_range", "genders", "devices", "network", "audience_targeting")
    PLANNABLE_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    PLANNABLE_LOCATION_IDS_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGE_FIELD_NUMBER: _ClassVar[int]
    GENDERS_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_TARGETING_FIELD_NUMBER: _ClassVar[int]
    plannable_location_id: str
    plannable_location_ids: _containers.RepeatedScalarFieldContainer[str]
    age_range: _reach_plan_age_range_pb2.ReachPlanAgeRangeEnum.ReachPlanAgeRange
    genders: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.GenderInfo]
    devices: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.DeviceInfo]
    network: _reach_plan_network_pb2.ReachPlanNetworkEnum.ReachPlanNetwork
    audience_targeting: AudienceTargeting
    def __init__(self, plannable_location_id: _Optional[str] = ..., plannable_location_ids: _Optional[_Iterable[str]] = ..., age_range: _Optional[_Union[_reach_plan_age_range_pb2.ReachPlanAgeRangeEnum.ReachPlanAgeRange, str]] = ..., genders: _Optional[_Iterable[_Union[_criteria_pb2.GenderInfo, _Mapping]]] = ..., devices: _Optional[_Iterable[_Union[_criteria_pb2.DeviceInfo, _Mapping]]] = ..., network: _Optional[_Union[_reach_plan_network_pb2.ReachPlanNetworkEnum.ReachPlanNetwork, str]] = ..., audience_targeting: _Optional[_Union[AudienceTargeting, _Mapping]] = ...) -> None: ...

class CampaignDuration(_message.Message):
    __slots__ = ("duration_in_days", "date_range")
    DURATION_IN_DAYS_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    duration_in_days: int
    date_range: _dates_pb2.DateRange
    def __init__(self, duration_in_days: _Optional[int] = ..., date_range: _Optional[_Union[_dates_pb2.DateRange, _Mapping]] = ...) -> None: ...

class PlannedProduct(_message.Message):
    __slots__ = ("plannable_product_code", "budget_micros", "advanced_product_targeting")
    PLANNABLE_PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    BUDGET_MICROS_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_PRODUCT_TARGETING_FIELD_NUMBER: _ClassVar[int]
    plannable_product_code: str
    budget_micros: int
    advanced_product_targeting: AdvancedProductTargeting
    def __init__(self, plannable_product_code: _Optional[str] = ..., budget_micros: _Optional[int] = ..., advanced_product_targeting: _Optional[_Union[AdvancedProductTargeting, _Mapping]] = ...) -> None: ...

class GenerateReachForecastResponse(_message.Message):
    __slots__ = ("on_target_audience_metrics", "reach_curve")
    ON_TARGET_AUDIENCE_METRICS_FIELD_NUMBER: _ClassVar[int]
    REACH_CURVE_FIELD_NUMBER: _ClassVar[int]
    on_target_audience_metrics: OnTargetAudienceMetrics
    reach_curve: ReachCurve
    def __init__(self, on_target_audience_metrics: _Optional[_Union[OnTargetAudienceMetrics, _Mapping]] = ..., reach_curve: _Optional[_Union[ReachCurve, _Mapping]] = ...) -> None: ...

class ReachCurve(_message.Message):
    __slots__ = ("reach_forecasts",)
    REACH_FORECASTS_FIELD_NUMBER: _ClassVar[int]
    reach_forecasts: _containers.RepeatedCompositeFieldContainer[ReachForecast]
    def __init__(self, reach_forecasts: _Optional[_Iterable[_Union[ReachForecast, _Mapping]]] = ...) -> None: ...

class ReachForecast(_message.Message):
    __slots__ = ("cost_micros", "forecast", "planned_product_reach_forecasts")
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    FORECAST_FIELD_NUMBER: _ClassVar[int]
    PLANNED_PRODUCT_REACH_FORECASTS_FIELD_NUMBER: _ClassVar[int]
    cost_micros: int
    forecast: Forecast
    planned_product_reach_forecasts: _containers.RepeatedCompositeFieldContainer[PlannedProductReachForecast]
    def __init__(self, cost_micros: _Optional[int] = ..., forecast: _Optional[_Union[Forecast, _Mapping]] = ..., planned_product_reach_forecasts: _Optional[_Iterable[_Union[PlannedProductReachForecast, _Mapping]]] = ...) -> None: ...

class Forecast(_message.Message):
    __slots__ = ("on_target_reach", "total_reach", "on_target_impressions", "total_impressions", "viewable_impressions", "effective_frequency_breakdowns", "on_target_coview_reach", "total_coview_reach", "on_target_coview_impressions", "total_coview_impressions", "views")
    ON_TARGET_REACH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REACH_FIELD_NUMBER: _ClassVar[int]
    ON_TARGET_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    VIEWABLE_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_FREQUENCY_BREAKDOWNS_FIELD_NUMBER: _ClassVar[int]
    ON_TARGET_COVIEW_REACH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COVIEW_REACH_FIELD_NUMBER: _ClassVar[int]
    ON_TARGET_COVIEW_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COVIEW_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    on_target_reach: int
    total_reach: int
    on_target_impressions: int
    total_impressions: int
    viewable_impressions: int
    effective_frequency_breakdowns: _containers.RepeatedCompositeFieldContainer[EffectiveFrequencyBreakdown]
    on_target_coview_reach: int
    total_coview_reach: int
    on_target_coview_impressions: int
    total_coview_impressions: int
    views: int
    def __init__(self, on_target_reach: _Optional[int] = ..., total_reach: _Optional[int] = ..., on_target_impressions: _Optional[int] = ..., total_impressions: _Optional[int] = ..., viewable_impressions: _Optional[int] = ..., effective_frequency_breakdowns: _Optional[_Iterable[_Union[EffectiveFrequencyBreakdown, _Mapping]]] = ..., on_target_coview_reach: _Optional[int] = ..., total_coview_reach: _Optional[int] = ..., on_target_coview_impressions: _Optional[int] = ..., total_coview_impressions: _Optional[int] = ..., views: _Optional[int] = ...) -> None: ...

class PlannedProductReachForecast(_message.Message):
    __slots__ = ("plannable_product_code", "cost_micros", "planned_product_forecast")
    PLANNABLE_PRODUCT_CODE_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    PLANNED_PRODUCT_FORECAST_FIELD_NUMBER: _ClassVar[int]
    plannable_product_code: str
    cost_micros: int
    planned_product_forecast: PlannedProductForecast
    def __init__(self, plannable_product_code: _Optional[str] = ..., cost_micros: _Optional[int] = ..., planned_product_forecast: _Optional[_Union[PlannedProductForecast, _Mapping]] = ...) -> None: ...

class PlannedProductForecast(_message.Message):
    __slots__ = ("on_target_reach", "total_reach", "on_target_impressions", "total_impressions", "viewable_impressions", "on_target_coview_reach", "total_coview_reach", "on_target_coview_impressions", "total_coview_impressions", "average_frequency", "views")
    ON_TARGET_REACH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REACH_FIELD_NUMBER: _ClassVar[int]
    ON_TARGET_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    VIEWABLE_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    ON_TARGET_COVIEW_REACH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COVIEW_REACH_FIELD_NUMBER: _ClassVar[int]
    ON_TARGET_COVIEW_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COVIEW_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    on_target_reach: int
    total_reach: int
    on_target_impressions: int
    total_impressions: int
    viewable_impressions: int
    on_target_coview_reach: int
    total_coview_reach: int
    on_target_coview_impressions: int
    total_coview_impressions: int
    average_frequency: float
    views: int
    def __init__(self, on_target_reach: _Optional[int] = ..., total_reach: _Optional[int] = ..., on_target_impressions: _Optional[int] = ..., total_impressions: _Optional[int] = ..., viewable_impressions: _Optional[int] = ..., on_target_coview_reach: _Optional[int] = ..., total_coview_reach: _Optional[int] = ..., on_target_coview_impressions: _Optional[int] = ..., total_coview_impressions: _Optional[int] = ..., average_frequency: _Optional[float] = ..., views: _Optional[int] = ...) -> None: ...

class OnTargetAudienceMetrics(_message.Message):
    __slots__ = ("youtube_audience_size", "census_audience_size")
    YOUTUBE_AUDIENCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CENSUS_AUDIENCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    youtube_audience_size: int
    census_audience_size: int
    def __init__(self, youtube_audience_size: _Optional[int] = ..., census_audience_size: _Optional[int] = ...) -> None: ...

class EffectiveFrequencyBreakdown(_message.Message):
    __slots__ = ("effective_frequency", "on_target_reach", "total_reach", "effective_coview_reach", "on_target_effective_coview_reach")
    EFFECTIVE_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    ON_TARGET_REACH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REACH_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_COVIEW_REACH_FIELD_NUMBER: _ClassVar[int]
    ON_TARGET_EFFECTIVE_COVIEW_REACH_FIELD_NUMBER: _ClassVar[int]
    effective_frequency: int
    on_target_reach: int
    total_reach: int
    effective_coview_reach: int
    on_target_effective_coview_reach: int
    def __init__(self, effective_frequency: _Optional[int] = ..., on_target_reach: _Optional[int] = ..., total_reach: _Optional[int] = ..., effective_coview_reach: _Optional[int] = ..., on_target_effective_coview_reach: _Optional[int] = ...) -> None: ...

class ForecastMetricOptions(_message.Message):
    __slots__ = ("include_coview",)
    INCLUDE_COVIEW_FIELD_NUMBER: _ClassVar[int]
    include_coview: bool
    def __init__(self, include_coview: bool = ...) -> None: ...

class AudienceTargeting(_message.Message):
    __slots__ = ("user_interest",)
    USER_INTEREST_FIELD_NUMBER: _ClassVar[int]
    user_interest: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.UserInterestInfo]
    def __init__(self, user_interest: _Optional[_Iterable[_Union[_criteria_pb2.UserInterestInfo, _Mapping]]] = ...) -> None: ...

class AdvancedProductTargeting(_message.Message):
    __slots__ = ("surface_targeting_settings", "target_frequency_settings", "youtube_select_settings")
    SURFACE_TARGETING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TARGET_FREQUENCY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_SELECT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    surface_targeting_settings: SurfaceTargeting
    target_frequency_settings: TargetFrequencySettings
    youtube_select_settings: YouTubeSelectSettings
    def __init__(self, surface_targeting_settings: _Optional[_Union[SurfaceTargeting, _Mapping]] = ..., target_frequency_settings: _Optional[_Union[TargetFrequencySettings, _Mapping]] = ..., youtube_select_settings: _Optional[_Union[YouTubeSelectSettings, _Mapping]] = ...) -> None: ...

class YouTubeSelectSettings(_message.Message):
    __slots__ = ("lineup_id",)
    LINEUP_ID_FIELD_NUMBER: _ClassVar[int]
    lineup_id: int
    def __init__(self, lineup_id: _Optional[int] = ...) -> None: ...

class YouTubeSelectLineUp(_message.Message):
    __slots__ = ("lineup_id", "lineup_name")
    LINEUP_ID_FIELD_NUMBER: _ClassVar[int]
    LINEUP_NAME_FIELD_NUMBER: _ClassVar[int]
    lineup_id: int
    lineup_name: str
    def __init__(self, lineup_id: _Optional[int] = ..., lineup_name: _Optional[str] = ...) -> None: ...

class SurfaceTargetingCombinations(_message.Message):
    __slots__ = ("default_targeting", "available_targeting_combinations")
    DEFAULT_TARGETING_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TARGETING_COMBINATIONS_FIELD_NUMBER: _ClassVar[int]
    default_targeting: SurfaceTargeting
    available_targeting_combinations: _containers.RepeatedCompositeFieldContainer[SurfaceTargeting]
    def __init__(self, default_targeting: _Optional[_Union[SurfaceTargeting, _Mapping]] = ..., available_targeting_combinations: _Optional[_Iterable[_Union[SurfaceTargeting, _Mapping]]] = ...) -> None: ...

class SurfaceTargeting(_message.Message):
    __slots__ = ("surfaces",)
    SURFACES_FIELD_NUMBER: _ClassVar[int]
    surfaces: _containers.RepeatedScalarFieldContainer[_reach_plan_surface_pb2.ReachPlanSurfaceEnum.ReachPlanSurface]
    def __init__(self, surfaces: _Optional[_Iterable[_Union[_reach_plan_surface_pb2.ReachPlanSurfaceEnum.ReachPlanSurface, str]]] = ...) -> None: ...

class TargetFrequencySettings(_message.Message):
    __slots__ = ("time_unit", "target_frequency")
    TIME_UNIT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    time_unit: _target_frequency_time_unit_pb2.TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit
    target_frequency: int
    def __init__(self, time_unit: _Optional[_Union[_target_frequency_time_unit_pb2.TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit, str]] = ..., target_frequency: _Optional[int] = ...) -> None: ...
