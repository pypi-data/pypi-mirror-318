from google.ads.searchads360.v0.common import criteria_pb2 as _criteria_pb2
from google.ads.searchads360.v0.enums import call_conversion_reporting_state_pb2 as _call_conversion_reporting_state_pb2
from google.ads.searchads360.v0.enums import call_to_action_type_pb2 as _call_to_action_type_pb2
from google.ads.searchads360.v0.enums import location_ownership_type_pb2 as _location_ownership_type_pb2
from google.ads.searchads360.v0.enums import mime_type_pb2 as _mime_type_pb2
from google.ads.searchads360.v0.enums import mobile_app_vendor_pb2 as _mobile_app_vendor_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class YoutubeVideoAsset(_message.Message):
    __slots__ = ("youtube_video_id", "youtube_video_title")
    YOUTUBE_VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_TITLE_FIELD_NUMBER: _ClassVar[int]
    youtube_video_id: str
    youtube_video_title: str
    def __init__(self, youtube_video_id: _Optional[str] = ..., youtube_video_title: _Optional[str] = ...) -> None: ...

class ImageAsset(_message.Message):
    __slots__ = ("file_size", "mime_type", "full_size")
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FULL_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_size: int
    mime_type: _mime_type_pb2.MimeTypeEnum.MimeType
    full_size: ImageDimension
    def __init__(self, file_size: _Optional[int] = ..., mime_type: _Optional[_Union[_mime_type_pb2.MimeTypeEnum.MimeType, str]] = ..., full_size: _Optional[_Union[ImageDimension, _Mapping]] = ...) -> None: ...

class ImageDimension(_message.Message):
    __slots__ = ("height_pixels", "width_pixels", "url")
    HEIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_PIXELS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    height_pixels: int
    width_pixels: int
    url: str
    def __init__(self, height_pixels: _Optional[int] = ..., width_pixels: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class TextAsset(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class UnifiedCalloutAsset(_message.Message):
    __slots__ = ("callout_text", "start_date", "end_date", "ad_schedule_targets", "use_searcher_time_zone")
    CALLOUT_TEXT_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULE_TARGETS_FIELD_NUMBER: _ClassVar[int]
    USE_SEARCHER_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    callout_text: str
    start_date: str
    end_date: str
    ad_schedule_targets: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AdScheduleInfo]
    use_searcher_time_zone: bool
    def __init__(self, callout_text: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., ad_schedule_targets: _Optional[_Iterable[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]]] = ..., use_searcher_time_zone: bool = ...) -> None: ...

class UnifiedSitelinkAsset(_message.Message):
    __slots__ = ("link_text", "description1", "description2", "start_date", "end_date", "ad_schedule_targets", "tracking_id", "use_searcher_time_zone", "mobile_preferred")
    LINK_TEXT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION1_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULE_TARGETS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    USE_SEARCHER_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    MOBILE_PREFERRED_FIELD_NUMBER: _ClassVar[int]
    link_text: str
    description1: str
    description2: str
    start_date: str
    end_date: str
    ad_schedule_targets: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AdScheduleInfo]
    tracking_id: int
    use_searcher_time_zone: bool
    mobile_preferred: bool
    def __init__(self, link_text: _Optional[str] = ..., description1: _Optional[str] = ..., description2: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., ad_schedule_targets: _Optional[_Iterable[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]]] = ..., tracking_id: _Optional[int] = ..., use_searcher_time_zone: bool = ..., mobile_preferred: bool = ...) -> None: ...

class UnifiedPageFeedAsset(_message.Message):
    __slots__ = ("page_url", "labels")
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    page_url: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, page_url: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...

class MobileAppAsset(_message.Message):
    __slots__ = ("app_id", "app_store")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_STORE_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    app_store: _mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor
    def __init__(self, app_id: _Optional[str] = ..., app_store: _Optional[_Union[_mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor, str]] = ...) -> None: ...

class UnifiedCallAsset(_message.Message):
    __slots__ = ("country_code", "phone_number", "call_conversion_reporting_state", "call_conversion_action", "ad_schedule_targets", "call_only", "call_tracking_enabled", "use_searcher_time_zone", "start_date", "end_date")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_REPORTING_STATE_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULE_TARGETS_FIELD_NUMBER: _ClassVar[int]
    CALL_ONLY_FIELD_NUMBER: _ClassVar[int]
    CALL_TRACKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USE_SEARCHER_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    phone_number: str
    call_conversion_reporting_state: _call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState
    call_conversion_action: str
    ad_schedule_targets: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AdScheduleInfo]
    call_only: bool
    call_tracking_enabled: bool
    use_searcher_time_zone: bool
    start_date: str
    end_date: str
    def __init__(self, country_code: _Optional[str] = ..., phone_number: _Optional[str] = ..., call_conversion_reporting_state: _Optional[_Union[_call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState, str]] = ..., call_conversion_action: _Optional[str] = ..., ad_schedule_targets: _Optional[_Iterable[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]]] = ..., call_only: bool = ..., call_tracking_enabled: bool = ..., use_searcher_time_zone: bool = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class CallToActionAsset(_message.Message):
    __slots__ = ("call_to_action",)
    CALL_TO_ACTION_FIELD_NUMBER: _ClassVar[int]
    call_to_action: _call_to_action_type_pb2.CallToActionTypeEnum.CallToActionType
    def __init__(self, call_to_action: _Optional[_Union[_call_to_action_type_pb2.CallToActionTypeEnum.CallToActionType, str]] = ...) -> None: ...

class UnifiedLocationAsset(_message.Message):
    __slots__ = ("place_id", "business_profile_locations", "location_ownership_type")
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_PROFILE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_OWNERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    place_id: str
    business_profile_locations: _containers.RepeatedCompositeFieldContainer[BusinessProfileLocation]
    location_ownership_type: _location_ownership_type_pb2.LocationOwnershipTypeEnum.LocationOwnershipType
    def __init__(self, place_id: _Optional[str] = ..., business_profile_locations: _Optional[_Iterable[_Union[BusinessProfileLocation, _Mapping]]] = ..., location_ownership_type: _Optional[_Union[_location_ownership_type_pb2.LocationOwnershipTypeEnum.LocationOwnershipType, str]] = ...) -> None: ...

class BusinessProfileLocation(_message.Message):
    __slots__ = ("labels", "store_code", "listing_id")
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STORE_CODE_FIELD_NUMBER: _ClassVar[int]
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedScalarFieldContainer[str]
    store_code: str
    listing_id: int
    def __init__(self, labels: _Optional[_Iterable[str]] = ..., store_code: _Optional[str] = ..., listing_id: _Optional[int] = ...) -> None: ...
