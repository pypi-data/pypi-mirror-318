from google.ads.googleads.v18.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v18.enums import bid_modifier_source_pb2 as _bid_modifier_source_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupBidModifier(_message.Message):
    __slots__ = ("resource_name", "ad_group", "criterion_id", "bid_modifier", "base_ad_group", "bid_modifier_source", "hotel_date_selection_type", "hotel_advance_booking_window", "hotel_length_of_stay", "hotel_check_in_day", "device", "hotel_check_in_date_range")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    BASE_AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    BID_MODIFIER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_DATE_SELECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_ADVANCE_BOOKING_WINDOW_FIELD_NUMBER: _ClassVar[int]
    HOTEL_LENGTH_OF_STAY_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CHECK_IN_DAY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CHECK_IN_DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    ad_group: str
    criterion_id: int
    bid_modifier: float
    base_ad_group: str
    bid_modifier_source: _bid_modifier_source_pb2.BidModifierSourceEnum.BidModifierSource
    hotel_date_selection_type: _criteria_pb2.HotelDateSelectionTypeInfo
    hotel_advance_booking_window: _criteria_pb2.HotelAdvanceBookingWindowInfo
    hotel_length_of_stay: _criteria_pb2.HotelLengthOfStayInfo
    hotel_check_in_day: _criteria_pb2.HotelCheckInDayInfo
    device: _criteria_pb2.DeviceInfo
    hotel_check_in_date_range: _criteria_pb2.HotelCheckInDateRangeInfo
    def __init__(self, resource_name: _Optional[str] = ..., ad_group: _Optional[str] = ..., criterion_id: _Optional[int] = ..., bid_modifier: _Optional[float] = ..., base_ad_group: _Optional[str] = ..., bid_modifier_source: _Optional[_Union[_bid_modifier_source_pb2.BidModifierSourceEnum.BidModifierSource, str]] = ..., hotel_date_selection_type: _Optional[_Union[_criteria_pb2.HotelDateSelectionTypeInfo, _Mapping]] = ..., hotel_advance_booking_window: _Optional[_Union[_criteria_pb2.HotelAdvanceBookingWindowInfo, _Mapping]] = ..., hotel_length_of_stay: _Optional[_Union[_criteria_pb2.HotelLengthOfStayInfo, _Mapping]] = ..., hotel_check_in_day: _Optional[_Union[_criteria_pb2.HotelCheckInDayInfo, _Mapping]] = ..., device: _Optional[_Union[_criteria_pb2.DeviceInfo, _Mapping]] = ..., hotel_check_in_date_range: _Optional[_Union[_criteria_pb2.HotelCheckInDateRangeInfo, _Mapping]] = ...) -> None: ...
