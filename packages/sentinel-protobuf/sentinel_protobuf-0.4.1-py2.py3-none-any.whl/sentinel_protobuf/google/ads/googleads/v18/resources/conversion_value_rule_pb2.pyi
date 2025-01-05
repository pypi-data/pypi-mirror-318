from google.ads.googleads.v18.enums import conversion_value_rule_status_pb2 as _conversion_value_rule_status_pb2
from google.ads.googleads.v18.enums import value_rule_device_type_pb2 as _value_rule_device_type_pb2
from google.ads.googleads.v18.enums import value_rule_geo_location_match_type_pb2 as _value_rule_geo_location_match_type_pb2
from google.ads.googleads.v18.enums import value_rule_operation_pb2 as _value_rule_operation_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionValueRule(_message.Message):
    __slots__ = ('resource_name', 'id', 'action', 'geo_location_condition', 'device_condition', 'audience_condition', 'itinerary_condition', 'owner_customer', 'status')

    class ValueRuleAction(_message.Message):
        __slots__ = ('operation', 'value')
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        operation: _value_rule_operation_pb2.ValueRuleOperationEnum.ValueRuleOperation
        value: float

        def __init__(self, operation: _Optional[_Union[_value_rule_operation_pb2.ValueRuleOperationEnum.ValueRuleOperation, str]]=..., value: _Optional[float]=...) -> None:
            ...

    class ValueRuleGeoLocationCondition(_message.Message):
        __slots__ = ('excluded_geo_target_constants', 'excluded_geo_match_type', 'geo_target_constants', 'geo_match_type')
        EXCLUDED_GEO_TARGET_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_GEO_MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        GEO_TARGET_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
        GEO_MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        excluded_geo_target_constants: _containers.RepeatedScalarFieldContainer[str]
        excluded_geo_match_type: _value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
        geo_target_constants: _containers.RepeatedScalarFieldContainer[str]
        geo_match_type: _value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType

        def __init__(self, excluded_geo_target_constants: _Optional[_Iterable[str]]=..., excluded_geo_match_type: _Optional[_Union[_value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType, str]]=..., geo_target_constants: _Optional[_Iterable[str]]=..., geo_match_type: _Optional[_Union[_value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType, str]]=...) -> None:
            ...

    class ValueRuleDeviceCondition(_message.Message):
        __slots__ = ('device_types',)
        DEVICE_TYPES_FIELD_NUMBER: _ClassVar[int]
        device_types: _containers.RepeatedScalarFieldContainer[_value_rule_device_type_pb2.ValueRuleDeviceTypeEnum.ValueRuleDeviceType]

        def __init__(self, device_types: _Optional[_Iterable[_Union[_value_rule_device_type_pb2.ValueRuleDeviceTypeEnum.ValueRuleDeviceType, str]]]=...) -> None:
            ...

    class ValueRuleAudienceCondition(_message.Message):
        __slots__ = ('user_lists', 'user_interests')
        USER_LISTS_FIELD_NUMBER: _ClassVar[int]
        USER_INTERESTS_FIELD_NUMBER: _ClassVar[int]
        user_lists: _containers.RepeatedScalarFieldContainer[str]
        user_interests: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, user_lists: _Optional[_Iterable[str]]=..., user_interests: _Optional[_Iterable[str]]=...) -> None:
            ...

    class ValueRuleItineraryCondition(_message.Message):
        __slots__ = ('advance_booking_window', 'travel_length', 'travel_start_day')
        ADVANCE_BOOKING_WINDOW_FIELD_NUMBER: _ClassVar[int]
        TRAVEL_LENGTH_FIELD_NUMBER: _ClassVar[int]
        TRAVEL_START_DAY_FIELD_NUMBER: _ClassVar[int]
        advance_booking_window: ConversionValueRule.ValueRuleItineraryAdvanceBookingWindow
        travel_length: ConversionValueRule.ValueRuleItineraryTravelLength
        travel_start_day: ConversionValueRule.ValueRuleItineraryTravelStartDay

        def __init__(self, advance_booking_window: _Optional[_Union[ConversionValueRule.ValueRuleItineraryAdvanceBookingWindow, _Mapping]]=..., travel_length: _Optional[_Union[ConversionValueRule.ValueRuleItineraryTravelLength, _Mapping]]=..., travel_start_day: _Optional[_Union[ConversionValueRule.ValueRuleItineraryTravelStartDay, _Mapping]]=...) -> None:
            ...

    class ValueRuleItineraryAdvanceBookingWindow(_message.Message):
        __slots__ = ('min_days', 'max_days')
        MIN_DAYS_FIELD_NUMBER: _ClassVar[int]
        MAX_DAYS_FIELD_NUMBER: _ClassVar[int]
        min_days: int
        max_days: int

        def __init__(self, min_days: _Optional[int]=..., max_days: _Optional[int]=...) -> None:
            ...

    class ValueRuleItineraryTravelLength(_message.Message):
        __slots__ = ('min_nights', 'max_nights')
        MIN_NIGHTS_FIELD_NUMBER: _ClassVar[int]
        MAX_NIGHTS_FIELD_NUMBER: _ClassVar[int]
        min_nights: int
        max_nights: int

        def __init__(self, min_nights: _Optional[int]=..., max_nights: _Optional[int]=...) -> None:
            ...

    class ValueRuleItineraryTravelStartDay(_message.Message):
        __slots__ = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        MONDAY_FIELD_NUMBER: _ClassVar[int]
        TUESDAY_FIELD_NUMBER: _ClassVar[int]
        WEDNESDAY_FIELD_NUMBER: _ClassVar[int]
        THURSDAY_FIELD_NUMBER: _ClassVar[int]
        FRIDAY_FIELD_NUMBER: _ClassVar[int]
        SATURDAY_FIELD_NUMBER: _ClassVar[int]
        SUNDAY_FIELD_NUMBER: _ClassVar[int]
        monday: bool
        tuesday: bool
        wednesday: bool
        thursday: bool
        friday: bool
        saturday: bool
        sunday: bool

        def __init__(self, monday: bool=..., tuesday: bool=..., wednesday: bool=..., thursday: bool=..., friday: bool=..., saturday: bool=..., sunday: bool=...) -> None:
            ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    GEO_LOCATION_CONDITION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    ITINERARY_CONDITION_FIELD_NUMBER: _ClassVar[int]
    OWNER_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    action: ConversionValueRule.ValueRuleAction
    geo_location_condition: ConversionValueRule.ValueRuleGeoLocationCondition
    device_condition: ConversionValueRule.ValueRuleDeviceCondition
    audience_condition: ConversionValueRule.ValueRuleAudienceCondition
    itinerary_condition: ConversionValueRule.ValueRuleItineraryCondition
    owner_customer: str
    status: _conversion_value_rule_status_pb2.ConversionValueRuleStatusEnum.ConversionValueRuleStatus

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., action: _Optional[_Union[ConversionValueRule.ValueRuleAction, _Mapping]]=..., geo_location_condition: _Optional[_Union[ConversionValueRule.ValueRuleGeoLocationCondition, _Mapping]]=..., device_condition: _Optional[_Union[ConversionValueRule.ValueRuleDeviceCondition, _Mapping]]=..., audience_condition: _Optional[_Union[ConversionValueRule.ValueRuleAudienceCondition, _Mapping]]=..., itinerary_condition: _Optional[_Union[ConversionValueRule.ValueRuleItineraryCondition, _Mapping]]=..., owner_customer: _Optional[str]=..., status: _Optional[_Union[_conversion_value_rule_status_pb2.ConversionValueRuleStatusEnum.ConversionValueRuleStatus, str]]=...) -> None:
        ...