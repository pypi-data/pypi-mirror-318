from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.type import date_pb2 as _date_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataLayerView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_LAYER_VIEW_UNSPECIFIED: _ClassVar[DataLayerView]
    DSM_LAYER: _ClassVar[DataLayerView]
    IMAGERY_LAYERS: _ClassVar[DataLayerView]
    IMAGERY_AND_ANNUAL_FLUX_LAYERS: _ClassVar[DataLayerView]
    IMAGERY_AND_ALL_FLUX_LAYERS: _ClassVar[DataLayerView]
    FULL_LAYERS: _ClassVar[DataLayerView]

class ImageryQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMAGERY_QUALITY_UNSPECIFIED: _ClassVar[ImageryQuality]
    HIGH: _ClassVar[ImageryQuality]
    MEDIUM: _ClassVar[ImageryQuality]
    LOW: _ClassVar[ImageryQuality]

class SolarPanelOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOLAR_PANEL_ORIENTATION_UNSPECIFIED: _ClassVar[SolarPanelOrientation]
    LANDSCAPE: _ClassVar[SolarPanelOrientation]
    PORTRAIT: _ClassVar[SolarPanelOrientation]
DATA_LAYER_VIEW_UNSPECIFIED: DataLayerView
DSM_LAYER: DataLayerView
IMAGERY_LAYERS: DataLayerView
IMAGERY_AND_ANNUAL_FLUX_LAYERS: DataLayerView
IMAGERY_AND_ALL_FLUX_LAYERS: DataLayerView
FULL_LAYERS: DataLayerView
IMAGERY_QUALITY_UNSPECIFIED: ImageryQuality
HIGH: ImageryQuality
MEDIUM: ImageryQuality
LOW: ImageryQuality
SOLAR_PANEL_ORIENTATION_UNSPECIFIED: SolarPanelOrientation
LANDSCAPE: SolarPanelOrientation
PORTRAIT: SolarPanelOrientation

class FindClosestBuildingInsightsRequest(_message.Message):
    __slots__ = ("location", "required_quality", "exact_quality_required")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_QUALITY_FIELD_NUMBER: _ClassVar[int]
    EXACT_QUALITY_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    required_quality: ImageryQuality
    exact_quality_required: bool
    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., required_quality: _Optional[_Union[ImageryQuality, str]] = ..., exact_quality_required: bool = ...) -> None: ...

class LatLngBox(_message.Message):
    __slots__ = ("sw", "ne")
    SW_FIELD_NUMBER: _ClassVar[int]
    NE_FIELD_NUMBER: _ClassVar[int]
    sw: _latlng_pb2.LatLng
    ne: _latlng_pb2.LatLng
    def __init__(self, sw: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., ne: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ...) -> None: ...

class BuildingInsights(_message.Message):
    __slots__ = ("name", "center", "bounding_box", "imagery_date", "imagery_processed_date", "postal_code", "administrative_area", "statistical_area", "region_code", "solar_potential", "imagery_quality")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    IMAGERY_DATE_FIELD_NUMBER: _ClassVar[int]
    IMAGERY_PROCESSED_DATE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATIVE_AREA_FIELD_NUMBER: _ClassVar[int]
    STATISTICAL_AREA_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    SOLAR_POTENTIAL_FIELD_NUMBER: _ClassVar[int]
    IMAGERY_QUALITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    center: _latlng_pb2.LatLng
    bounding_box: LatLngBox
    imagery_date: _date_pb2.Date
    imagery_processed_date: _date_pb2.Date
    postal_code: str
    administrative_area: str
    statistical_area: str
    region_code: str
    solar_potential: SolarPotential
    imagery_quality: ImageryQuality
    def __init__(self, name: _Optional[str] = ..., center: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., bounding_box: _Optional[_Union[LatLngBox, _Mapping]] = ..., imagery_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., imagery_processed_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., postal_code: _Optional[str] = ..., administrative_area: _Optional[str] = ..., statistical_area: _Optional[str] = ..., region_code: _Optional[str] = ..., solar_potential: _Optional[_Union[SolarPotential, _Mapping]] = ..., imagery_quality: _Optional[_Union[ImageryQuality, str]] = ...) -> None: ...

class SolarPotential(_message.Message):
    __slots__ = ("max_array_panels_count", "panel_capacity_watts", "panel_height_meters", "panel_width_meters", "panel_lifetime_years", "max_array_area_meters2", "max_sunshine_hours_per_year", "carbon_offset_factor_kg_per_mwh", "whole_roof_stats", "building_stats", "roof_segment_stats", "solar_panels", "solar_panel_configs", "financial_analyses")
    MAX_ARRAY_PANELS_COUNT_FIELD_NUMBER: _ClassVar[int]
    PANEL_CAPACITY_WATTS_FIELD_NUMBER: _ClassVar[int]
    PANEL_HEIGHT_METERS_FIELD_NUMBER: _ClassVar[int]
    PANEL_WIDTH_METERS_FIELD_NUMBER: _ClassVar[int]
    PANEL_LIFETIME_YEARS_FIELD_NUMBER: _ClassVar[int]
    MAX_ARRAY_AREA_METERS2_FIELD_NUMBER: _ClassVar[int]
    MAX_SUNSHINE_HOURS_PER_YEAR_FIELD_NUMBER: _ClassVar[int]
    CARBON_OFFSET_FACTOR_KG_PER_MWH_FIELD_NUMBER: _ClassVar[int]
    WHOLE_ROOF_STATS_FIELD_NUMBER: _ClassVar[int]
    BUILDING_STATS_FIELD_NUMBER: _ClassVar[int]
    ROOF_SEGMENT_STATS_FIELD_NUMBER: _ClassVar[int]
    SOLAR_PANELS_FIELD_NUMBER: _ClassVar[int]
    SOLAR_PANEL_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    FINANCIAL_ANALYSES_FIELD_NUMBER: _ClassVar[int]
    max_array_panels_count: int
    panel_capacity_watts: float
    panel_height_meters: float
    panel_width_meters: float
    panel_lifetime_years: int
    max_array_area_meters2: float
    max_sunshine_hours_per_year: float
    carbon_offset_factor_kg_per_mwh: float
    whole_roof_stats: SizeAndSunshineStats
    building_stats: SizeAndSunshineStats
    roof_segment_stats: _containers.RepeatedCompositeFieldContainer[RoofSegmentSizeAndSunshineStats]
    solar_panels: _containers.RepeatedCompositeFieldContainer[SolarPanel]
    solar_panel_configs: _containers.RepeatedCompositeFieldContainer[SolarPanelConfig]
    financial_analyses: _containers.RepeatedCompositeFieldContainer[FinancialAnalysis]
    def __init__(self, max_array_panels_count: _Optional[int] = ..., panel_capacity_watts: _Optional[float] = ..., panel_height_meters: _Optional[float] = ..., panel_width_meters: _Optional[float] = ..., panel_lifetime_years: _Optional[int] = ..., max_array_area_meters2: _Optional[float] = ..., max_sunshine_hours_per_year: _Optional[float] = ..., carbon_offset_factor_kg_per_mwh: _Optional[float] = ..., whole_roof_stats: _Optional[_Union[SizeAndSunshineStats, _Mapping]] = ..., building_stats: _Optional[_Union[SizeAndSunshineStats, _Mapping]] = ..., roof_segment_stats: _Optional[_Iterable[_Union[RoofSegmentSizeAndSunshineStats, _Mapping]]] = ..., solar_panels: _Optional[_Iterable[_Union[SolarPanel, _Mapping]]] = ..., solar_panel_configs: _Optional[_Iterable[_Union[SolarPanelConfig, _Mapping]]] = ..., financial_analyses: _Optional[_Iterable[_Union[FinancialAnalysis, _Mapping]]] = ...) -> None: ...

class RoofSegmentSizeAndSunshineStats(_message.Message):
    __slots__ = ("pitch_degrees", "azimuth_degrees", "stats", "center", "bounding_box", "plane_height_at_center_meters")
    PITCH_DEGREES_FIELD_NUMBER: _ClassVar[int]
    AZIMUTH_DEGREES_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    PLANE_HEIGHT_AT_CENTER_METERS_FIELD_NUMBER: _ClassVar[int]
    pitch_degrees: float
    azimuth_degrees: float
    stats: SizeAndSunshineStats
    center: _latlng_pb2.LatLng
    bounding_box: LatLngBox
    plane_height_at_center_meters: float
    def __init__(self, pitch_degrees: _Optional[float] = ..., azimuth_degrees: _Optional[float] = ..., stats: _Optional[_Union[SizeAndSunshineStats, _Mapping]] = ..., center: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., bounding_box: _Optional[_Union[LatLngBox, _Mapping]] = ..., plane_height_at_center_meters: _Optional[float] = ...) -> None: ...

class SizeAndSunshineStats(_message.Message):
    __slots__ = ("area_meters2", "sunshine_quantiles", "ground_area_meters2")
    AREA_METERS2_FIELD_NUMBER: _ClassVar[int]
    SUNSHINE_QUANTILES_FIELD_NUMBER: _ClassVar[int]
    GROUND_AREA_METERS2_FIELD_NUMBER: _ClassVar[int]
    area_meters2: float
    sunshine_quantiles: _containers.RepeatedScalarFieldContainer[float]
    ground_area_meters2: float
    def __init__(self, area_meters2: _Optional[float] = ..., sunshine_quantiles: _Optional[_Iterable[float]] = ..., ground_area_meters2: _Optional[float] = ...) -> None: ...

class SolarPanel(_message.Message):
    __slots__ = ("center", "orientation", "yearly_energy_dc_kwh", "segment_index")
    CENTER_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    YEARLY_ENERGY_DC_KWH_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    center: _latlng_pb2.LatLng
    orientation: SolarPanelOrientation
    yearly_energy_dc_kwh: float
    segment_index: int
    def __init__(self, center: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., orientation: _Optional[_Union[SolarPanelOrientation, str]] = ..., yearly_energy_dc_kwh: _Optional[float] = ..., segment_index: _Optional[int] = ...) -> None: ...

class SolarPanelConfig(_message.Message):
    __slots__ = ("panels_count", "yearly_energy_dc_kwh", "roof_segment_summaries")
    PANELS_COUNT_FIELD_NUMBER: _ClassVar[int]
    YEARLY_ENERGY_DC_KWH_FIELD_NUMBER: _ClassVar[int]
    ROOF_SEGMENT_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    panels_count: int
    yearly_energy_dc_kwh: float
    roof_segment_summaries: _containers.RepeatedCompositeFieldContainer[RoofSegmentSummary]
    def __init__(self, panels_count: _Optional[int] = ..., yearly_energy_dc_kwh: _Optional[float] = ..., roof_segment_summaries: _Optional[_Iterable[_Union[RoofSegmentSummary, _Mapping]]] = ...) -> None: ...

class RoofSegmentSummary(_message.Message):
    __slots__ = ("pitch_degrees", "azimuth_degrees", "panels_count", "yearly_energy_dc_kwh", "segment_index")
    PITCH_DEGREES_FIELD_NUMBER: _ClassVar[int]
    AZIMUTH_DEGREES_FIELD_NUMBER: _ClassVar[int]
    PANELS_COUNT_FIELD_NUMBER: _ClassVar[int]
    YEARLY_ENERGY_DC_KWH_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    pitch_degrees: float
    azimuth_degrees: float
    panels_count: int
    yearly_energy_dc_kwh: float
    segment_index: int
    def __init__(self, pitch_degrees: _Optional[float] = ..., azimuth_degrees: _Optional[float] = ..., panels_count: _Optional[int] = ..., yearly_energy_dc_kwh: _Optional[float] = ..., segment_index: _Optional[int] = ...) -> None: ...

class FinancialAnalysis(_message.Message):
    __slots__ = ("monthly_bill", "default_bill", "average_kwh_per_month", "panel_config_index", "financial_details", "leasing_savings", "cash_purchase_savings", "financed_purchase_savings")
    MONTHLY_BILL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BILL_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_KWH_PER_MONTH_FIELD_NUMBER: _ClassVar[int]
    PANEL_CONFIG_INDEX_FIELD_NUMBER: _ClassVar[int]
    FINANCIAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LEASING_SAVINGS_FIELD_NUMBER: _ClassVar[int]
    CASH_PURCHASE_SAVINGS_FIELD_NUMBER: _ClassVar[int]
    FINANCED_PURCHASE_SAVINGS_FIELD_NUMBER: _ClassVar[int]
    monthly_bill: _money_pb2.Money
    default_bill: bool
    average_kwh_per_month: float
    panel_config_index: int
    financial_details: FinancialDetails
    leasing_savings: LeasingSavings
    cash_purchase_savings: CashPurchaseSavings
    financed_purchase_savings: FinancedPurchaseSavings
    def __init__(self, monthly_bill: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., default_bill: bool = ..., average_kwh_per_month: _Optional[float] = ..., panel_config_index: _Optional[int] = ..., financial_details: _Optional[_Union[FinancialDetails, _Mapping]] = ..., leasing_savings: _Optional[_Union[LeasingSavings, _Mapping]] = ..., cash_purchase_savings: _Optional[_Union[CashPurchaseSavings, _Mapping]] = ..., financed_purchase_savings: _Optional[_Union[FinancedPurchaseSavings, _Mapping]] = ...) -> None: ...

class FinancialDetails(_message.Message):
    __slots__ = ("initial_ac_kwh_per_year", "remaining_lifetime_utility_bill", "federal_incentive", "state_incentive", "utility_incentive", "lifetime_srec_total", "cost_of_electricity_without_solar", "net_metering_allowed", "solar_percentage", "percentage_exported_to_grid")
    INITIAL_AC_KWH_PER_YEAR_FIELD_NUMBER: _ClassVar[int]
    REMAINING_LIFETIME_UTILITY_BILL_FIELD_NUMBER: _ClassVar[int]
    FEDERAL_INCENTIVE_FIELD_NUMBER: _ClassVar[int]
    STATE_INCENTIVE_FIELD_NUMBER: _ClassVar[int]
    UTILITY_INCENTIVE_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_SREC_TOTAL_FIELD_NUMBER: _ClassVar[int]
    COST_OF_ELECTRICITY_WITHOUT_SOLAR_FIELD_NUMBER: _ClassVar[int]
    NET_METERING_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    SOLAR_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_EXPORTED_TO_GRID_FIELD_NUMBER: _ClassVar[int]
    initial_ac_kwh_per_year: float
    remaining_lifetime_utility_bill: _money_pb2.Money
    federal_incentive: _money_pb2.Money
    state_incentive: _money_pb2.Money
    utility_incentive: _money_pb2.Money
    lifetime_srec_total: _money_pb2.Money
    cost_of_electricity_without_solar: _money_pb2.Money
    net_metering_allowed: bool
    solar_percentage: float
    percentage_exported_to_grid: float
    def __init__(self, initial_ac_kwh_per_year: _Optional[float] = ..., remaining_lifetime_utility_bill: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., federal_incentive: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., state_incentive: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., utility_incentive: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., lifetime_srec_total: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., cost_of_electricity_without_solar: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., net_metering_allowed: bool = ..., solar_percentage: _Optional[float] = ..., percentage_exported_to_grid: _Optional[float] = ...) -> None: ...

class SavingsOverTime(_message.Message):
    __slots__ = ("savings_year1", "savings_year20", "present_value_of_savings_year20", "savings_lifetime", "present_value_of_savings_lifetime", "financially_viable")
    SAVINGS_YEAR1_FIELD_NUMBER: _ClassVar[int]
    SAVINGS_YEAR20_FIELD_NUMBER: _ClassVar[int]
    PRESENT_VALUE_OF_SAVINGS_YEAR20_FIELD_NUMBER: _ClassVar[int]
    SAVINGS_LIFETIME_FIELD_NUMBER: _ClassVar[int]
    PRESENT_VALUE_OF_SAVINGS_LIFETIME_FIELD_NUMBER: _ClassVar[int]
    FINANCIALLY_VIABLE_FIELD_NUMBER: _ClassVar[int]
    savings_year1: _money_pb2.Money
    savings_year20: _money_pb2.Money
    present_value_of_savings_year20: _money_pb2.Money
    savings_lifetime: _money_pb2.Money
    present_value_of_savings_lifetime: _money_pb2.Money
    financially_viable: bool
    def __init__(self, savings_year1: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., savings_year20: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., present_value_of_savings_year20: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., savings_lifetime: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., present_value_of_savings_lifetime: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., financially_viable: bool = ...) -> None: ...

class LeasingSavings(_message.Message):
    __slots__ = ("leases_allowed", "leases_supported", "annual_leasing_cost", "savings")
    LEASES_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    LEASES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_LEASING_COST_FIELD_NUMBER: _ClassVar[int]
    SAVINGS_FIELD_NUMBER: _ClassVar[int]
    leases_allowed: bool
    leases_supported: bool
    annual_leasing_cost: _money_pb2.Money
    savings: SavingsOverTime
    def __init__(self, leases_allowed: bool = ..., leases_supported: bool = ..., annual_leasing_cost: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., savings: _Optional[_Union[SavingsOverTime, _Mapping]] = ...) -> None: ...

class CashPurchaseSavings(_message.Message):
    __slots__ = ("out_of_pocket_cost", "upfront_cost", "rebate_value", "payback_years", "savings")
    OUT_OF_POCKET_COST_FIELD_NUMBER: _ClassVar[int]
    UPFRONT_COST_FIELD_NUMBER: _ClassVar[int]
    REBATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    PAYBACK_YEARS_FIELD_NUMBER: _ClassVar[int]
    SAVINGS_FIELD_NUMBER: _ClassVar[int]
    out_of_pocket_cost: _money_pb2.Money
    upfront_cost: _money_pb2.Money
    rebate_value: _money_pb2.Money
    payback_years: float
    savings: SavingsOverTime
    def __init__(self, out_of_pocket_cost: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., upfront_cost: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., rebate_value: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., payback_years: _Optional[float] = ..., savings: _Optional[_Union[SavingsOverTime, _Mapping]] = ...) -> None: ...

class FinancedPurchaseSavings(_message.Message):
    __slots__ = ("annual_loan_payment", "rebate_value", "loan_interest_rate", "savings")
    ANNUAL_LOAN_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    REBATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    LOAN_INTEREST_RATE_FIELD_NUMBER: _ClassVar[int]
    SAVINGS_FIELD_NUMBER: _ClassVar[int]
    annual_loan_payment: _money_pb2.Money
    rebate_value: _money_pb2.Money
    loan_interest_rate: float
    savings: SavingsOverTime
    def __init__(self, annual_loan_payment: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., rebate_value: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., loan_interest_rate: _Optional[float] = ..., savings: _Optional[_Union[SavingsOverTime, _Mapping]] = ...) -> None: ...

class GetDataLayersRequest(_message.Message):
    __slots__ = ("location", "radius_meters", "view", "required_quality", "pixel_size_meters", "exact_quality_required")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RADIUS_METERS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_QUALITY_FIELD_NUMBER: _ClassVar[int]
    PIXEL_SIZE_METERS_FIELD_NUMBER: _ClassVar[int]
    EXACT_QUALITY_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    radius_meters: float
    view: DataLayerView
    required_quality: ImageryQuality
    pixel_size_meters: float
    exact_quality_required: bool
    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., radius_meters: _Optional[float] = ..., view: _Optional[_Union[DataLayerView, str]] = ..., required_quality: _Optional[_Union[ImageryQuality, str]] = ..., pixel_size_meters: _Optional[float] = ..., exact_quality_required: bool = ...) -> None: ...

class DataLayers(_message.Message):
    __slots__ = ("imagery_date", "imagery_processed_date", "dsm_url", "rgb_url", "mask_url", "annual_flux_url", "monthly_flux_url", "hourly_shade_urls", "imagery_quality")
    IMAGERY_DATE_FIELD_NUMBER: _ClassVar[int]
    IMAGERY_PROCESSED_DATE_FIELD_NUMBER: _ClassVar[int]
    DSM_URL_FIELD_NUMBER: _ClassVar[int]
    RGB_URL_FIELD_NUMBER: _ClassVar[int]
    MASK_URL_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_FLUX_URL_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_FLUX_URL_FIELD_NUMBER: _ClassVar[int]
    HOURLY_SHADE_URLS_FIELD_NUMBER: _ClassVar[int]
    IMAGERY_QUALITY_FIELD_NUMBER: _ClassVar[int]
    imagery_date: _date_pb2.Date
    imagery_processed_date: _date_pb2.Date
    dsm_url: str
    rgb_url: str
    mask_url: str
    annual_flux_url: str
    monthly_flux_url: str
    hourly_shade_urls: _containers.RepeatedScalarFieldContainer[str]
    imagery_quality: ImageryQuality
    def __init__(self, imagery_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., imagery_processed_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., dsm_url: _Optional[str] = ..., rgb_url: _Optional[str] = ..., mask_url: _Optional[str] = ..., annual_flux_url: _Optional[str] = ..., monthly_flux_url: _Optional[str] = ..., hourly_shade_urls: _Optional[_Iterable[str]] = ..., imagery_quality: _Optional[_Union[ImageryQuality, str]] = ...) -> None: ...

class GetGeoTiffRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
