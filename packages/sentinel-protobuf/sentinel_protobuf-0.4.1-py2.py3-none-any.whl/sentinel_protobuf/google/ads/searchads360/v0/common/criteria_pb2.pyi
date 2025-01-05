from google.ads.searchads360.v0.enums import age_range_type_pb2 as _age_range_type_pb2
from google.ads.searchads360.v0.enums import day_of_week_pb2 as _day_of_week_pb2
from google.ads.searchads360.v0.enums import device_pb2 as _device_pb2
from google.ads.searchads360.v0.enums import gender_type_pb2 as _gender_type_pb2
from google.ads.searchads360.v0.enums import keyword_match_type_pb2 as _keyword_match_type_pb2
from google.ads.searchads360.v0.enums import listing_group_type_pb2 as _listing_group_type_pb2
from google.ads.searchads360.v0.enums import location_group_radius_units_pb2 as _location_group_radius_units_pb2
from google.ads.searchads360.v0.enums import minute_of_hour_pb2 as _minute_of_hour_pb2
from google.ads.searchads360.v0.enums import webpage_condition_operand_pb2 as _webpage_condition_operand_pb2
from google.ads.searchads360.v0.enums import webpage_condition_operator_pb2 as _webpage_condition_operator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeywordInfo(_message.Message):
    __slots__ = ("text", "match_type")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    text: str
    match_type: _keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType
    def __init__(self, text: _Optional[str] = ..., match_type: _Optional[_Union[_keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType, str]] = ...) -> None: ...

class LocationInfo(_message.Message):
    __slots__ = ("geo_target_constant",)
    GEO_TARGET_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    geo_target_constant: str
    def __init__(self, geo_target_constant: _Optional[str] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _device_pb2.DeviceEnum.Device
    def __init__(self, type: _Optional[_Union[_device_pb2.DeviceEnum.Device, str]] = ...) -> None: ...

class ListingGroupInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _listing_group_type_pb2.ListingGroupTypeEnum.ListingGroupType
    def __init__(self, type: _Optional[_Union[_listing_group_type_pb2.ListingGroupTypeEnum.ListingGroupType, str]] = ...) -> None: ...

class AdScheduleInfo(_message.Message):
    __slots__ = ("start_minute", "end_minute", "start_hour", "end_hour", "day_of_week")
    START_MINUTE_FIELD_NUMBER: _ClassVar[int]
    END_MINUTE_FIELD_NUMBER: _ClassVar[int]
    START_HOUR_FIELD_NUMBER: _ClassVar[int]
    END_HOUR_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    start_minute: _minute_of_hour_pb2.MinuteOfHourEnum.MinuteOfHour
    end_minute: _minute_of_hour_pb2.MinuteOfHourEnum.MinuteOfHour
    start_hour: int
    end_hour: int
    day_of_week: _day_of_week_pb2.DayOfWeekEnum.DayOfWeek
    def __init__(self, start_minute: _Optional[_Union[_minute_of_hour_pb2.MinuteOfHourEnum.MinuteOfHour, str]] = ..., end_minute: _Optional[_Union[_minute_of_hour_pb2.MinuteOfHourEnum.MinuteOfHour, str]] = ..., start_hour: _Optional[int] = ..., end_hour: _Optional[int] = ..., day_of_week: _Optional[_Union[_day_of_week_pb2.DayOfWeekEnum.DayOfWeek, str]] = ...) -> None: ...

class AgeRangeInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _age_range_type_pb2.AgeRangeTypeEnum.AgeRangeType
    def __init__(self, type: _Optional[_Union[_age_range_type_pb2.AgeRangeTypeEnum.AgeRangeType, str]] = ...) -> None: ...

class GenderInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _gender_type_pb2.GenderTypeEnum.GenderType
    def __init__(self, type: _Optional[_Union[_gender_type_pb2.GenderTypeEnum.GenderType, str]] = ...) -> None: ...

class UserListInfo(_message.Message):
    __slots__ = ("user_list",)
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    user_list: str
    def __init__(self, user_list: _Optional[str] = ...) -> None: ...

class LanguageInfo(_message.Message):
    __slots__ = ("language_constant",)
    LANGUAGE_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    language_constant: str
    def __init__(self, language_constant: _Optional[str] = ...) -> None: ...

class WebpageInfo(_message.Message):
    __slots__ = ("criterion_name", "conditions", "coverage_percentage")
    CRITERION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    criterion_name: str
    conditions: _containers.RepeatedCompositeFieldContainer[WebpageConditionInfo]
    coverage_percentage: float
    def __init__(self, criterion_name: _Optional[str] = ..., conditions: _Optional[_Iterable[_Union[WebpageConditionInfo, _Mapping]]] = ..., coverage_percentage: _Optional[float] = ...) -> None: ...

class WebpageConditionInfo(_message.Message):
    __slots__ = ("operand", "operator", "argument")
    OPERAND_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    operand: _webpage_condition_operand_pb2.WebpageConditionOperandEnum.WebpageConditionOperand
    operator: _webpage_condition_operator_pb2.WebpageConditionOperatorEnum.WebpageConditionOperator
    argument: str
    def __init__(self, operand: _Optional[_Union[_webpage_condition_operand_pb2.WebpageConditionOperandEnum.WebpageConditionOperand, str]] = ..., operator: _Optional[_Union[_webpage_condition_operator_pb2.WebpageConditionOperatorEnum.WebpageConditionOperator, str]] = ..., argument: _Optional[str] = ...) -> None: ...

class LocationGroupInfo(_message.Message):
    __slots__ = ("geo_target_constants", "radius", "radius_units", "feed_item_sets")
    GEO_TARGET_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    RADIUS_UNITS_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_SETS_FIELD_NUMBER: _ClassVar[int]
    geo_target_constants: _containers.RepeatedScalarFieldContainer[str]
    radius: int
    radius_units: _location_group_radius_units_pb2.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    feed_item_sets: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, geo_target_constants: _Optional[_Iterable[str]] = ..., radius: _Optional[int] = ..., radius_units: _Optional[_Union[_location_group_radius_units_pb2.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits, str]] = ..., feed_item_sets: _Optional[_Iterable[str]] = ...) -> None: ...

class AudienceInfo(_message.Message):
    __slots__ = ("audience",)
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    audience: str
    def __init__(self, audience: _Optional[str] = ...) -> None: ...
