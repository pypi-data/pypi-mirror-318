from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.talent.v4 import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class JobQuery(_message.Message):
    __slots__ = ('query', 'query_language_code', 'companies', 'location_filters', 'job_categories', 'commute_filter', 'company_display_names', 'compensation_filter', 'custom_attribute_filter', 'disable_spell_check', 'employment_types', 'language_codes', 'publish_time_range', 'excluded_jobs')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    COMPANIES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FILTERS_FIELD_NUMBER: _ClassVar[int]
    JOB_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    COMMUTE_FILTER_FIELD_NUMBER: _ClassVar[int]
    COMPANY_DISPLAY_NAMES_FIELD_NUMBER: _ClassVar[int]
    COMPENSATION_FILTER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTE_FILTER_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SPELL_CHECK_FIELD_NUMBER: _ClassVar[int]
    EMPLOYMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_JOBS_FIELD_NUMBER: _ClassVar[int]
    query: str
    query_language_code: str
    companies: _containers.RepeatedScalarFieldContainer[str]
    location_filters: _containers.RepeatedCompositeFieldContainer[LocationFilter]
    job_categories: _containers.RepeatedScalarFieldContainer[_common_pb2.JobCategory]
    commute_filter: CommuteFilter
    company_display_names: _containers.RepeatedScalarFieldContainer[str]
    compensation_filter: CompensationFilter
    custom_attribute_filter: str
    disable_spell_check: bool
    employment_types: _containers.RepeatedScalarFieldContainer[_common_pb2.EmploymentType]
    language_codes: _containers.RepeatedScalarFieldContainer[str]
    publish_time_range: _common_pb2.TimestampRange
    excluded_jobs: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, query: _Optional[str]=..., query_language_code: _Optional[str]=..., companies: _Optional[_Iterable[str]]=..., location_filters: _Optional[_Iterable[_Union[LocationFilter, _Mapping]]]=..., job_categories: _Optional[_Iterable[_Union[_common_pb2.JobCategory, str]]]=..., commute_filter: _Optional[_Union[CommuteFilter, _Mapping]]=..., company_display_names: _Optional[_Iterable[str]]=..., compensation_filter: _Optional[_Union[CompensationFilter, _Mapping]]=..., custom_attribute_filter: _Optional[str]=..., disable_spell_check: bool=..., employment_types: _Optional[_Iterable[_Union[_common_pb2.EmploymentType, str]]]=..., language_codes: _Optional[_Iterable[str]]=..., publish_time_range: _Optional[_Union[_common_pb2.TimestampRange, _Mapping]]=..., excluded_jobs: _Optional[_Iterable[str]]=...) -> None:
        ...

class LocationFilter(_message.Message):
    __slots__ = ('address', 'region_code', 'lat_lng', 'distance_in_miles', 'telecommute_preference')

    class TelecommutePreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TELECOMMUTE_PREFERENCE_UNSPECIFIED: _ClassVar[LocationFilter.TelecommutePreference]
        TELECOMMUTE_EXCLUDED: _ClassVar[LocationFilter.TelecommutePreference]
        TELECOMMUTE_ALLOWED: _ClassVar[LocationFilter.TelecommutePreference]
        TELECOMMUTE_JOBS_EXCLUDED: _ClassVar[LocationFilter.TelecommutePreference]
    TELECOMMUTE_PREFERENCE_UNSPECIFIED: LocationFilter.TelecommutePreference
    TELECOMMUTE_EXCLUDED: LocationFilter.TelecommutePreference
    TELECOMMUTE_ALLOWED: LocationFilter.TelecommutePreference
    TELECOMMUTE_JOBS_EXCLUDED: LocationFilter.TelecommutePreference
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    LAT_LNG_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_IN_MILES_FIELD_NUMBER: _ClassVar[int]
    TELECOMMUTE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    address: str
    region_code: str
    lat_lng: _latlng_pb2.LatLng
    distance_in_miles: float
    telecommute_preference: LocationFilter.TelecommutePreference

    def __init__(self, address: _Optional[str]=..., region_code: _Optional[str]=..., lat_lng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., distance_in_miles: _Optional[float]=..., telecommute_preference: _Optional[_Union[LocationFilter.TelecommutePreference, str]]=...) -> None:
        ...

class CompensationFilter(_message.Message):
    __slots__ = ('type', 'units', 'range', 'include_jobs_with_unspecified_compensation_range')

    class FilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILTER_TYPE_UNSPECIFIED: _ClassVar[CompensationFilter.FilterType]
        UNIT_ONLY: _ClassVar[CompensationFilter.FilterType]
        UNIT_AND_AMOUNT: _ClassVar[CompensationFilter.FilterType]
        ANNUALIZED_BASE_AMOUNT: _ClassVar[CompensationFilter.FilterType]
        ANNUALIZED_TOTAL_AMOUNT: _ClassVar[CompensationFilter.FilterType]
    FILTER_TYPE_UNSPECIFIED: CompensationFilter.FilterType
    UNIT_ONLY: CompensationFilter.FilterType
    UNIT_AND_AMOUNT: CompensationFilter.FilterType
    ANNUALIZED_BASE_AMOUNT: CompensationFilter.FilterType
    ANNUALIZED_TOTAL_AMOUNT: CompensationFilter.FilterType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_JOBS_WITH_UNSPECIFIED_COMPENSATION_RANGE_FIELD_NUMBER: _ClassVar[int]
    type: CompensationFilter.FilterType
    units: _containers.RepeatedScalarFieldContainer[_common_pb2.CompensationInfo.CompensationUnit]
    range: _common_pb2.CompensationInfo.CompensationRange
    include_jobs_with_unspecified_compensation_range: bool

    def __init__(self, type: _Optional[_Union[CompensationFilter.FilterType, str]]=..., units: _Optional[_Iterable[_Union[_common_pb2.CompensationInfo.CompensationUnit, str]]]=..., range: _Optional[_Union[_common_pb2.CompensationInfo.CompensationRange, _Mapping]]=..., include_jobs_with_unspecified_compensation_range: bool=...) -> None:
        ...

class CommuteFilter(_message.Message):
    __slots__ = ('commute_method', 'start_coordinates', 'travel_duration', 'allow_imprecise_addresses', 'road_traffic', 'departure_time')

    class RoadTraffic(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROAD_TRAFFIC_UNSPECIFIED: _ClassVar[CommuteFilter.RoadTraffic]
        TRAFFIC_FREE: _ClassVar[CommuteFilter.RoadTraffic]
        BUSY_HOUR: _ClassVar[CommuteFilter.RoadTraffic]
    ROAD_TRAFFIC_UNSPECIFIED: CommuteFilter.RoadTraffic
    TRAFFIC_FREE: CommuteFilter.RoadTraffic
    BUSY_HOUR: CommuteFilter.RoadTraffic
    COMMUTE_METHOD_FIELD_NUMBER: _ClassVar[int]
    START_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_DURATION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_IMPRECISE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ROAD_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
    DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    commute_method: _common_pb2.CommuteMethod
    start_coordinates: _latlng_pb2.LatLng
    travel_duration: _duration_pb2.Duration
    allow_imprecise_addresses: bool
    road_traffic: CommuteFilter.RoadTraffic
    departure_time: _timeofday_pb2.TimeOfDay

    def __init__(self, commute_method: _Optional[_Union[_common_pb2.CommuteMethod, str]]=..., start_coordinates: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., travel_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., allow_imprecise_addresses: bool=..., road_traffic: _Optional[_Union[CommuteFilter.RoadTraffic, str]]=..., departure_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=...) -> None:
        ...